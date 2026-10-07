#!/usr/bin/env python3
"""
kinsta_kb.py - build, refresh and query a local mirror of Kinsta's documentation.

Subcommands
-----------
  sync      Sitemap-driven incremental ingest. Cheap when nothing changed.
  check     Revalidate specific URLs before you cite them. The honest freshness gate.
  search    Full-text search across the mirror (ripgrep), scoped by tier/product.
  show      Print a page by URL or local path.
  status    Per-tier counts, mirror age, last successful sync.
  tree      The section taxonomy with page counts.

Design notes for whoever maintains this
---------------------------------------
Two things in here are load-bearing and easy to break by accident:

1. `check` must never report FRESH for a request that did not actually complete.
   A network failure is UNVERIFIED, which is a different and weaker claim. The
   whole point of the skill is that a cached page is not evidence of a current
   page, and a failed validation is not evidence either.

2. The body extraction uses a *list* of candidate selectors plus a sanity floor,
   not a single pinned selector. Site redesigns do not return errors - they
   return HTTP 200 with navigation chrome where the article used to be. The
   ratio check in `_guard_extraction_quality` is what catches that, because one
   short page is plausible while a fifth of the corpus going short at once is a
   redesign.
"""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import gzip
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Sequence
from urllib.parse import urlparse

try:
    import requests
    from bs4 import BeautifulSoup
    from markdownify import markdownify
except ImportError as exc:  # pragma: no cover
    sys.exit(
        f"Missing dependency: {exc.name}. "
        "This script needs requests, beautifulsoup4 and markdownify.\n"
        "They are present on FloydTower already; if you are elsewhere, install "
        "them into a venv rather than globally."
    )

# --------------------------------------------------------------------------- #
# Configuration. Everything site-shaped lives here so a Kinsta redesign is a
# one-place edit rather than a hunt through the code.
# --------------------------------------------------------------------------- #

SKILL_DIR = Path(__file__).resolve().parent.parent
KB = SKILL_DIR / "kb"
MANIFEST = KB / "manifest.json"
INDEX_MD = KB / "INDEX.md"
SYNC_LOG = KB / "SYNC-LOG.md"
DIFF_DIR = KB / ".diffs"
LOCK = KB / ".sync.lock"
TAXONOMY_MD = SKILL_DIR / "references" / "taxonomy.md"

BASE = "https://kinsta.com"
ROBOTS = f"{BASE}/robots.txt"

USER_AGENT = (
    "Centre6-KinstaDocsMirror/1.0 (+documentation mirror for internal reference; "
    "polite, sitemap-driven, one request per changed page)"
)

# --- Scope, and the one thing to understand before changing it -------------- #
#
# Kinsta spun Application Hosting, Database Hosting and Static Site Hosting out
# into a separate company, Sevalla. As of October 2026 `/docs/application-
# hosting/` and friends 301 to docs.sevalla.com, and kinsta.com/docs covers
# **WordPress hosting plus the account surfaces around it** and nothing else.
#
# This mirror deliberately covers Kinsta only. Sevalla is out of scope by
# decision, not oversight, and docs.sevalla.com additionally declares
# `Content-Signal: ai-input=no` in its robots.txt. Do not add it without asking.
# Kinsta's own robots declares `ai-input=yes`, which is why this mirror exists.
#
# Practical consequence worth knowing: an Application/Database/Static Site
# Hosting question has no answer in here. Say that it is outside what Kinsta's
# docs cover rather than reaching into the WordPress tree for something
# adjacent - a wrong-product answer is the expensive failure here.
SCOPE_NOTE = (
    "kinsta.com/docs covers Managed WordPress Hosting, DevKinsta, and the "
    "MyKinsta account/billing surfaces. Application, Database and Static Site "
    "Hosting moved to a separate company (Sevalla) and are not mirrored here."
)

# Tier definitions. Matched on (host, path prefix) - host matters now because
# the API reference lives on its own subdomain with its own sitemap.
#   mode "sitemap" -> enumerate from the listed sitemaps
#   mode "wp_rest" -> enumerate from kinsta.com's WordPress REST API, which is
#                     the only source of true publish dates (see BLOG_MONTHS)
TIERS: dict[str, dict] = {
    "docs": {
        "host": "kinsta.com", "prefix": "/docs/", "dir": "docs",
        "mode": "sitemap", "sitemaps": [f"{BASE}/sitemap_index.xml"],
    },
    "api": {
        "host": "api-docs.kinsta.com", "prefix": "/", "dir": "api",
        "mode": "sitemap", "sitemaps": ["https://api-docs.kinsta.com/sitemap.xml"],
    },
    "changelog": {
        "host": "kinsta.com", "prefix": "/changelog/", "dir": "changelog",
        "mode": "sitemap", "sitemaps": [f"{BASE}/sitemap_index.xml"],
    },
    "blog": {
        "host": "kinsta.com", "prefix": "/blog/", "dir": "blog",
        "mode": "wp_rest", "wp_rest": f"{BASE}/wp-json/wp/v2/posts",
    },
}
DEFAULT_TIERS = ["docs", "api", "changelog", "blog"]

# Blog recency window, in months. The blog is ~1,550 posts and mostly marketing;
# only recent material is worth carrying.
#
# This MUST come from the publish date, not from sitemap `lastmod`. Kinsta
# re-touches old articles, so 1,308 of 1,551 posts carry a lastmod inside the
# last 12 months while only ~140 were actually published in that window. A
# lastmod filter looks like it is working and silently pulls nearly the whole
# blog. The WP REST API's `after=` parameter filters on publish date, which is
# why the blog tier uses it instead of the sitemap.
BLOG_MONTHS = 12

# Non-English locales are present in the sitemaps and excluded on purpose:
# translations lag the English originals, so a stale translation would compete
# with a current source for the same answer.
LANG_PREFIXES = ("/de/", "/es/", "/fr/", "/it/", "/jp/", "/nl/", "/pt/")

# The OpenAPI spec. Found at the "Download OpenAPI Specification" link on
# api-docs.kinsta.com; it is YAML, not JSON, and there is no spec at any
# api.kinsta.com path (all 404 or redirect to the docs page).
OPENAPI_CANDIDATES = [
    "https://api-docs.kinsta.com/assets/kinsta-openapi.yaml",
]

# Body extraction. Tried in order; the first selector yielding a body above the
# sanity floor wins. Keep the most specific first.
BODY_SELECTORS = [
    "article.kinsta-docs-content",
    "div.kinsta-docs-content",
    "main article",
    "article .entry-content",
    "div.entry-content",
    "main",
    "article",
]

# Elements that are never article content. Stripped before conversion so they
# cannot inflate the body length and defeat the sanity floor.
STRIP_SELECTORS = [
    "script", "style", "noscript", "svg", "iframe",
    "nav", "header", "footer", "aside", "form",
    ".breadcrumb", ".breadcrumbs", ".toc", ".table-of-contents",
    ".sidebar", ".kinsta-sidebar", ".docs-sidebar",
    ".feedback", ".article-feedback", ".was-this-helpful",
    ".related-articles", ".related-posts", ".share", ".social",
    ".newsletter", ".cta", ".banner", ".cookie", ".subscribe",
    "[aria-hidden=true]", "[role=navigation]", "[role=complementary]",
]

MIN_BODY_CHARS = 200          # below this, a page is suspect, not short
ABORT_SHORT_RATIO = 0.20      # >20% suspect in one run => selectors broke
DEFAULT_DELAY = 1.0           # seconds between requests; politeness, not speed
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
LOCK_STALE_SECONDS = 2 * 60 * 60

# Pretty labels for the area slugs derived from /docs/<slug>/. Counts are from
# the October 7, 2026 sitemap and are here to make drift obvious: if `tree`
# reports wildly different numbers, Kinsta reorganized and the taxonomy in
# references/taxonomy.md is the thing to re-read.
#
# Unknown slugs pass through as-is rather than being dropped, so a new Kinsta
# area shows up in the taxonomy the day they publish it instead of being
# silently uncategorized.
PRODUCT_LABELS = {
    "wordpress-hosting": "Managed WordPress Hosting",   # 112 pages
    "devkinsta": "DevKinsta (local dev tool, not hosting)",  # 25
    "service-information": "Service Information",       # 17
    "billing": "Billing",                               # 13
    "company-settings": "MyKinsta Company Settings",    # 12
    "user-settings": "MyKinsta User Settings",          # 5
    "support": "Support",                               # 4
    "kinsta-api": "Kinsta API (overview page)",         # 1
    "api": "Kinsta API Reference",                      # api-docs.kinsta.com
    "changelog": "Changelog",
    "blog": "Blog (secondary - never outranks docs)",
}

# Terms whose meaning differs by product. Used by `search` to warn when results
# straddle products, which is the moment a wrong-product answer gets written.
CROSS_PRODUCT_TERMS = {
    "backup", "backups", "restore", "rollback", "cache", "caching", "cdn",
    "custom domain", "domain", "deployment", "deploy", "environment",
    "environments", "staging", "redirect", "redirects", "log", "logs",
    "metrics", "ssh", "sftp", "cron", "scheduled task", "build", "process",
    "processes", "edge", "plan", "plans", "limit", "limits", "dns",
}

UTC = dt.timezone.utc


def now_iso() -> str:
    return dt.datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


# --------------------------------------------------------------------------- #
# Manifest
# --------------------------------------------------------------------------- #


@dataclass
class Manifest:
    path: Path = MANIFEST
    version: int = 1
    last_sync: dict = field(default_factory=dict)
    pages: dict = field(default_factory=dict)
    notes: dict = field(default_factory=dict)

    @classmethod
    def load(cls, path: Path = MANIFEST) -> "Manifest":
        if not path.exists():
            return cls(path=path)
        data = json.loads(path.read_text())
        return cls(
            path=path,
            version=data.get("version", 1),
            last_sync=data.get("last_sync", {}),
            pages=data.get("pages", {}),
            notes=data.get("notes", {}),
        )

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "version": self.version,
            "last_sync": self.last_sync,
            "notes": self.notes,
            "pages": dict(sorted(self.pages.items())),
        }
        tmp = self.path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n")
        tmp.replace(self.path)

    def live(self, tier: str | None = None) -> dict:
        out = {}
        for url, rec in self.pages.items():
            if rec.get("status") == "removed":
                continue
            if tier and rec.get("tier") != tier:
                continue
            out[url] = rec
        return out


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #


class Fetcher:
    """Polite HTTP with conditional GET support and honest failure reporting."""

    def __init__(self, delay: float = DEFAULT_DELAY):
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update(
            {"User-Agent": USER_AGENT, "Accept-Encoding": "gzip, deflate"}
        )
        self._last_request = 0.0

    def _wait(self) -> None:
        gap = time.monotonic() - self._last_request
        if gap < self.delay:
            time.sleep(self.delay - gap)
        self._last_request = time.monotonic()

    def get(
        self,
        url: str,
        etag: str | None = None,
        last_modified: str | None = None,
    ) -> tuple[int | None, bytes | None, dict, str | None]:
        """
        Returns (status, body, headers, error).

        `error` is non-None exactly when the request did not complete. Callers
        must distinguish that from a completed request with an unhappy status -
        conflating the two is how an unverified page gets reported as fresh.
        """
        headers = {}
        if etag:
            headers["If-None-Match"] = etag
        if last_modified:
            headers["If-Modified-Since"] = last_modified

        last_err = None
        for attempt in range(1, MAX_RETRIES + 1):
            self._wait()
            try:
                r = self.session.get(
                    url, headers=headers, timeout=REQUEST_TIMEOUT, allow_redirects=True
                )
            except requests.RequestException as exc:
                last_err = f"{type(exc).__name__}: {exc}"
                time.sleep(min(2 ** attempt, 10))
                continue

            # 429/5xx are worth retrying; everything else is a real answer.
            if r.status_code == 429 or 500 <= r.status_code < 600:
                last_err = f"HTTP {r.status_code}"
                retry_after = r.headers.get("Retry-After")
                backoff = (
                    float(retry_after)
                    if retry_after and retry_after.isdigit()
                    else min(2 ** attempt, 15)
                )
                time.sleep(backoff)
                continue

            return r.status_code, r.content, r.headers, None

        return None, None, {}, last_err or "exhausted retries"


# --------------------------------------------------------------------------- #
# Sitemaps
# --------------------------------------------------------------------------- #


def _maybe_gunzip(body: bytes) -> bytes:
    if body[:2] == b"\x1f\x8b":
        return gzip.decompress(body)
    return body


def discover_sitemaps(fetcher: Fetcher) -> list[str]:
    status, body, _, err = fetcher.get(ROBOTS)
    if err or status != 200 or not body:
        # Fall back to the conventional location rather than giving up; report
        # the robots failure so it is visible rather than silently assumed away.
        print(f"  ! robots.txt unavailable ({err or status}); trying /sitemap.xml",
              file=sys.stderr)
        return [f"{BASE}/sitemap.xml"]
    maps = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", body.decode("utf-8", "replace"))
    return maps or [f"{BASE}/sitemap.xml"]


def parse_sitemap(fetcher: Fetcher, url: str, depth: int = 0) -> list[tuple[str, str | None]]:
    """Recursively expand a sitemap or sitemap index into [(loc, lastmod)]."""
    if depth > 3:
        return []
    status, body, _, err = fetcher.get(url)
    if err or status != 200 or not body:
        print(f"  ! sitemap {url}: {err or status}", file=sys.stderr)
        return []
    try:
        root = ET.fromstring(_maybe_gunzip(body))
    except ET.ParseError as exc:
        print(f"  ! sitemap {url} unparseable: {exc}", file=sys.stderr)
        return []

    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    out: list[tuple[str, str | None]] = []

    if root.tag.endswith("sitemapindex"):
        for sm in root.findall(f"{ns}sitemap"):
            loc = (sm.findtext(f"{ns}loc") or "").strip()
            if loc:
                out.extend(parse_sitemap(fetcher, loc, depth + 1))
        return out

    for entry in root.findall(f"{ns}url"):
        loc = (entry.findtext(f"{ns}loc") or "").strip()
        lastmod = (entry.findtext(f"{ns}lastmod") or "").strip() or None
        if loc:
            out.append((loc, lastmod))
    return out


def tier_for(url: str) -> str | None:
    """Route a URL to its tier on (host, path prefix). Host is load-bearing:
    the API reference lives on its own subdomain."""
    parts = urlparse(url)
    host, path = parts.netloc.lower(), parts.path
    if path.startswith(LANG_PREFIXES):
        return None  # translation; see LANG_PREFIXES
    for name, cfg in TIERS.items():
        if host == cfg["host"] and path.startswith(cfg["prefix"]):
            return name
    return None


def product_for(url: str, tier: str) -> str:
    """The area a page belongs to, derived from its URL path.

    For /docs/ this is the first segment after /docs/, which is Kinsta's own
    top-level split (wordpress-hosting, devkinsta, billing, ...). For other
    tiers the tier name is the honest answer - there is no finer product
    distinction to make.
    """
    segments = [s for s in urlparse(url).path.strip("/").split("/") if s]
    if tier == "docs" and len(segments) >= 2:
        return segments[1]
    return tier


def subsection_for(url: str, tier: str) -> str | None:
    """One level below the product, e.g. caching / site-management / php under
    wordpress-hosting. This is the level at which Kinsta's docs actually
    disambiguate, so it is worth indexing separately from the product."""
    segments = [s for s in urlparse(url).path.strip("/").split("/") if s]
    if tier == "docs" and len(segments) >= 3:
        return segments[2]
    if tier == "api" and len(segments) >= 2:
        return segments[1]
    return None


def local_path_for(url: str, tier: str) -> Path:
    """Mirror the URL hierarchy on disk so the tree is navigable by hand."""
    segments = [s for s in urlparse(url).path.strip("/").split("/") if s]
    prefix_segments = len([s for s in TIERS[tier]["prefix"].strip("/").split("/") if s])
    rest = segments[prefix_segments:] or ["index"]
    rest = [re.sub(r"[^a-z0-9._-]+", "-", s.lower()) for s in rest]
    return Path(TIERS[tier]["dir"], *rest[:-1], rest[-1] + ".md")


# --------------------------------------------------------------------------- #
# Enumeration - what is in scope, per tier
# --------------------------------------------------------------------------- #


def enumerate_blog(fetcher: Fetcher, months: int) -> dict[str, str | None]:
    """Blog posts published within the window, via the WordPress REST API.

    The REST API rather than the sitemap because `after=` filters on the
    publish date. See the BLOG_MONTHS comment for why the sitemap's lastmod is
    the wrong signal here - it is a trap that quietly pulls the whole blog.
    """
    cutoff = (dt.datetime.now(UTC) - dt.timedelta(days=30 * months)).strftime(
        "%Y-%m-%dT00:00:00"
    )
    out: dict[str, str | None] = {}
    page = 1
    while page <= 20:  # hard stop; 100/page means 2000 posts is already absurd
        url = (
            f"{TIERS['blog']['wp_rest']}?per_page=100&page={page}"
            f"&after={cutoff}&orderby=date&order=desc"
            f"&_fields=link,date,modified"
        )
        status, body, headers, err = fetcher.get(url)
        if err or status == 400:
            break  # 400 is how WP says "past the last page"
        if status != 200 or not body:
            print(f"  ! blog REST page {page}: HTTP {status}", file=sys.stderr)
            break
        try:
            posts = json.loads(body)
        except json.JSONDecodeError:
            print(f"  ! blog REST page {page}: non-JSON response", file=sys.stderr)
            break
        if not isinstance(posts, list) or not posts:
            break
        if page == 1:
            total = headers.get("X-WP-Total", "?")
            print(f"  blog: {total} post(s) published since {cutoff[:10]} "
                  f"(publish date, not lastmod)")
        for p in posts:
            link = (p.get("link") or "").rstrip("/") + "/"
            if link and tier_for(link) == "blog":
                # Carry `modified` as the change signal, `date` for recency.
                out[link] = (p.get("modified") or p.get("date") or None)
        if len(posts) < 100:
            break
        page += 1
    return out


def enumerate_scope(
    fetcher: Fetcher, tiers: list[str], blog_months: int
) -> dict[str, str | None]:
    """URL -> change-signal (sitemap lastmod, or WP `modified`) for every tier."""
    entries: dict[str, str | None] = {}

    sitemap_tiers = [t for t in tiers if TIERS[t]["mode"] == "sitemap"]
    if sitemap_tiers:
        wanted = set(sitemap_tiers)
        seen_sitemaps: set[str] = set()
        for t in sitemap_tiers:
            for sm in TIERS[t]["sitemaps"]:
                if sm in seen_sitemaps:
                    continue
                seen_sitemaps.add(sm)
                found = parse_sitemap(fetcher, sm)
                print(f"  {sm} -> {len(found)} urls")
                for loc, lastmod in found:
                    norm = loc.rstrip("/") + "/"
                    if tier_for(norm) in wanted:
                        entries[norm] = lastmod

    if "blog" in tiers:
        entries.update(enumerate_blog(fetcher, blog_months))

    return entries


# --------------------------------------------------------------------------- #
# Extraction and segmentation
# --------------------------------------------------------------------------- #


@dataclass
class Extracted:
    title: str
    breadcrumbs: list[str]
    body_md: str
    headings: list[tuple[int, str]]
    page_lastmod: str | None
    selector_used: str | None


def _clean(soup: BeautifulSoup) -> None:
    for sel in STRIP_SELECTORS:
        for node in soup.select(sel):
            node.decompose()


def _breadcrumbs(soup: BeautifulSoup) -> list[str]:
    """Kinsta's own category path, which is better taxonomy than we could infer."""
    for sel in ("nav.breadcrumb", ".breadcrumbs", "[aria-label=Breadcrumb]",
                "[class*=breadcrumb]"):
        node = soup.select_one(sel)
        if not node:
            continue
        parts = [
            a.get_text(" ", strip=True)
            for a in node.find_all(["a", "span", "li"])
            if a.get_text(strip=True)
        ]
        seen, uniq = set(), []
        for p in parts:
            low = p.lower()
            if low in seen or low in ("home", "kinsta", "docs", "/"):
                continue
            seen.add(low)
            uniq.append(p)
        if uniq:
            return uniq
    # JSON-LD BreadcrumbList is the reliable fallback when the markup changes.
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "{}")
        except (json.JSONDecodeError, TypeError):
            continue
        for block in data if isinstance(data, list) else [data]:
            if isinstance(block, dict) and block.get("@type") == "BreadcrumbList":
                items = sorted(
                    block.get("itemListElement", []),
                    key=lambda i: i.get("position", 0),
                )
                names = [
                    (i.get("name") or i.get("item", {}).get("name") or "").strip()
                    for i in items
                ]
                names = [n for n in names if n and n.lower() not in ("home", "docs")]
                if names:
                    return names
    return []


def _page_lastmod(soup: BeautifulSoup) -> str | None:
    """Kinsta's own 'last updated' signal, which is more meaningful than our
    fetch time because it reflects when the content actually changed."""
    for prop in ("article:modified_time", "og:updated_time"):
        node = soup.find("meta", property=prop)
        if node and node.get("content"):
            return node["content"].strip()
    node = soup.find("meta", attrs={"name": "last-modified"})
    if node and node.get("content"):
        return node["content"].strip()
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "{}")
        except (json.JSONDecodeError, TypeError):
            continue
        for block in data if isinstance(data, list) else [data]:
            if isinstance(block, dict) and block.get("dateModified"):
                return str(block["dateModified"]).strip()
    text = soup.get_text(" ", strip=True)
    m = re.search(r"(?i)(?:last updated|updated on)[:\s]+([A-Z][a-z]+ \d{1,2},? \d{4})", text)
    return m.group(1) if m else None


def extract(html: bytes, url: str) -> Extracted:
    soup = BeautifulSoup(html, "lxml")

    title = ""
    og = soup.find("meta", property="og:title")
    if og and og.get("content"):
        title = og["content"].strip()
    if not title and soup.title:
        title = soup.title.get_text(strip=True)
    title = re.sub(r"\s*[|\-–]\s*Kinsta.*$", "", title).strip()

    crumbs = _breadcrumbs(soup)
    page_lastmod = _page_lastmod(soup)

    body_md, used = "", None
    for sel in BODY_SELECTORS:
        node = soup.select_one(sel)
        if not node:
            continue
        candidate = BeautifulSoup(str(node), "lxml")
        _clean(candidate)
        for h1 in candidate.find_all("h1"):
            h1.decompose()  # the H1 becomes the frontmatter title; no duplicate
        md = markdownify(
            str(candidate),
            heading_style="ATX",
            bullets="-",
            code_language="",
            escape_asterisks=False,
            escape_underscores=False,
        )
        md = re.sub(r"\n{3,}", "\n\n", md).strip()
        if len(md) >= MIN_BODY_CHARS:
            body_md, used = md, sel
            break
        if len(md) > len(body_md):
            body_md, used = md, sel  # keep the best bad option for reporting

    headings = [
        (len(m.group(1)), m.group(2).strip())
        for m in re.finditer(r"(?m)^(#{2,4})\s+(.+)$", body_md)
    ]
    if not title:
        title = urlparse(url).path.strip("/").split("/")[-1].replace("-", " ").title()

    return Extracted(title, crumbs, body_md, headings, page_lastmod, used)


def anchor(text: str) -> str:
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_]+", "-", slug).strip("-")


def render_page(url: str, tier: str, product: str, ex: Extracted,
                sitemap_lastmod: str | None, sha: str) -> str:
    """One page -> one markdown file with frontmatter and a navigable TOC.

    The per-page TOC is not decoration. It lets a reader (human or model) see a
    page's full shape without loading the whole body, which is what makes it
    practical to pick the right page out of a search hit list.
    """
    fm = {
        "url": url,
        "title": ex.title,
        "tier": tier,
        "product": product,
        "product_label": PRODUCT_LABELS.get(product, product),
        "subsection": subsection_for(url, tier),
        "section": ex.breadcrumbs,
        "kinsta_last_updated": ex.page_lastmod,
        "sitemap_lastmod": sitemap_lastmod,
        "fetched_at": now_iso(),
        "sha256": sha,
        "body_chars": len(ex.body_md),
        "extracted_with": ex.selector_used,
        "status": "live",
    }
    lines = ["---"]
    for k, v in fm.items():
        if v is None:
            lines.append(f"{k}:")
        elif isinstance(v, list):
            lines.append(f"{k}: [{', '.join(json.dumps(s) for s in v)}]")
        elif isinstance(v, int):
            lines.append(f"{k}: {v}")
        else:
            lines.append(f"{k}: {json.dumps(str(v))}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {ex.title}")
    lines.append("")
    if ex.breadcrumbs:
        lines.append(f"**Section:** {' > '.join(ex.breadcrumbs)}")
    lines.append(f"**Product:** {PRODUCT_LABELS.get(product, product)}")
    lines.append(f"**Source:** {url}")
    if ex.page_lastmod:
        lines.append(f"**Kinsta last updated:** {ex.page_lastmod}")
    lines.append("")
    if len(ex.headings) >= 3:
        lines.append("## On this page")
        lines.append("")
        for level, text in ex.headings:
            if text.lower() == "on this page":
                continue
            lines.append(f"{'  ' * (level - 2)}- [{text}](#{anchor(text)})")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(ex.body_md)
    lines.append("")
    return "\n".join(lines)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def body_of(markdown_file: Path) -> str:
    """The content below the frontmatter, for hashing and diffing. Frontmatter
    carries fetch timestamps, so hashing the whole file would report a change on
    every sync and make the git history useless."""
    text = markdown_file.read_text(encoding="utf-8", errors="replace")
    parts = text.split("---\n", 2)
    return parts[2] if len(parts) == 3 else text


# --------------------------------------------------------------------------- #
# Locking
# --------------------------------------------------------------------------- #


def acquire_lock(force: bool) -> None:
    KB.mkdir(parents=True, exist_ok=True)
    if LOCK.exists():
        age = time.time() - LOCK.stat().st_mtime
        holder = LOCK.read_text().strip()
        if force or age > LOCK_STALE_SECONDS:
            print(f"  clearing lock held by [{holder}], age {age / 60:.0f}m")
            LOCK.unlink()
        else:
            sys.exit(
                f"Another sync is running (lock held by [{holder}], age {age / 60:.0f}m).\n"
                "If you know it is dead, re-run with --force-unlock."
            )
    LOCK.write_text(f"pid={os.getpid()} started={now_iso()}\n")


def release_lock() -> None:
    LOCK.unlink(missing_ok=True)


# --------------------------------------------------------------------------- #
# sync
# --------------------------------------------------------------------------- #


def _guard_extraction_quality(short: list[str], total: int) -> None:
    """A redesign returns HTTP 200 with chrome where the article used to be, so
    nothing errors and the mirror quietly fills with junk. The ratio is the
    tell: one short page is plausible, a fifth of them at once is not."""
    if total == 0:
        return
    ratio = len(short) / total
    if ratio > ABORT_SHORT_RATIO and len(short) >= 3:
        print(
            f"\nABORTING: {len(short)}/{total} pages ({ratio:.0%}) extracted under "
            f"{MIN_BODY_CHARS} chars of body text.\n"
            "That pattern means the body selector no longer matches Kinsta's markup, "
            "not that the pages are short.\n"
            "Nothing was written. Fetch one page by hand, look at the HTML yourself, "
            "update BODY_SELECTORS, then re-run with --dry-run before a real sync.\n"
            "Short pages included:\n  " + "\n  ".join(short[:10]),
            file=sys.stderr,
        )
        sys.exit(2)


def cmd_sync(args: argparse.Namespace) -> int:
    tiers = [t.strip() for t in args.tier.split(",")] if args.tier else DEFAULT_TIERS
    unknown = [t for t in tiers if t not in TIERS]
    if unknown:
        sys.exit(f"Unknown tier(s): {', '.join(unknown)}. Known: {', '.join(TIERS)}")

    acquire_lock(args.force_unlock)
    try:
        return _sync(args, tiers)
    finally:
        release_lock()


def _sync(args: argparse.Namespace, tiers: list[str]) -> int:
    fetcher = Fetcher(delay=args.delay)
    mf = Manifest.load()
    KB.mkdir(parents=True, exist_ok=True)
    DIFF_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Sync starting {now_iso()}  tiers={','.join(tiers)}"
          f"{'  [DRY RUN]' if args.dry_run else ''}")

    # ---- 1. Enumerate what is in scope ----------------------------------- #
    print("\nEnumerating scope...")
    entries = enumerate_scope(fetcher, tiers, args.blog_months)

    if not entries:
        print("\nNo URLs found for the requested tiers. Either the sitemaps moved or "
              "the (host, prefix) pairs in TIERS no longer match Kinsta's URL "
              "structure. Nothing written.", file=sys.stderr)
        return 2

    by_tier: dict[str, int] = {}
    for url in entries:
        by_tier[tier_for(url)] = by_tier.get(tier_for(url), 0) + 1
    print(f"  {len(entries)} URLs in scope: " +
          ", ".join(f"{k}={v}" for k, v in sorted(by_tier.items())))

    if args.section:
        before = len(entries)
        entries = {u: lm for u, lm in entries.items() if f"/{args.section}/" in u}
        print(f"  --section {args.section}: {len(entries)} of {before}")

    # ---- 2. Decide what needs fetching ----------------------------------- #
    to_fetch: list[tuple[str, str | None]] = []
    for url, lastmod in entries.items():
        rec = mf.pages.get(url)
        if rec is None or rec.get("status") == "removed":
            to_fetch.append((url, lastmod))
        elif args.full:
            to_fetch.append((url, lastmod))
        elif lastmod and rec.get("sitemap_lastmod") != lastmod:
            to_fetch.append((url, lastmod))
        elif not Path(KB / rec["path"]).exists():
            to_fetch.append((url, lastmod))  # manifest says we have it; we don't
        else:
            # Unchanged lastmod. Still cheap to confirm via conditional GET, but
            # only when asked - that is what `check` is for on the hot path.
            pass

    if args.limit:
        to_fetch = to_fetch[: args.limit]

    removed = [
        url for url, rec in mf.pages.items()
        if rec.get("status") != "removed"
        and rec.get("tier") in tiers
        and url not in entries
    ]

    print(f"\n{len(to_fetch)} page(s) to fetch, {len(removed)} no longer in sitemap")
    if not to_fetch and not removed:
        print("Mirror already matches the sitemap. Nothing to do.")
        for t in tiers:
            mf.last_sync[t] = now_iso()
        if not args.dry_run:
            mf.save()
        return 0

    # ---- 3. Fetch, extract, stage ---------------------------------------- #
    staged: dict[str, tuple[dict, str]] = {}   # url -> (record, rendered markdown)
    short_pages: list[str] = []
    unverified: list[tuple[str, str]] = []
    gone: list[str] = []
    changed, added = [], []

    for i, (url, lastmod) in enumerate(to_fetch, 1):
        rec = mf.pages.get(url) or {}
        status, body, headers, err = fetcher.get(
            url,
            etag=None if args.full else rec.get("etag"),
            last_modified=None if args.full else rec.get("last_modified"),
        )
        prefix = f"  [{i}/{len(to_fetch)}]"

        if err:
            unverified.append((url, err))
            print(f"{prefix} UNVERIFIED {url}  ({err})")
            continue
        if status == 304:
            print(f"{prefix} 304 unchanged {url}")
            rec["sitemap_lastmod"] = lastmod
            mf.pages[url] = rec
            continue
        if status in (404, 410):
            gone.append(url)
            print(f"{prefix} {status} GONE {url}")
            continue
        if status != 200 or not body:
            unverified.append((url, f"HTTP {status}"))
            print(f"{prefix} UNVERIFIED {url}  (HTTP {status})")
            continue

        t = tier_for(url)
        product = product_for(url, t)
        ex = extract(body, url)
        if len(ex.body_md) < MIN_BODY_CHARS:
            short_pages.append(f"{url}  ({len(ex.body_md)} chars, sel={ex.selector_used})")

        sha = sha256_text(ex.body_md)
        rel = local_path_for(url, t)
        rendered = render_page(url, t, product, ex, lastmod, sha)

        new_rec = {
            "path": str(rel),
            "tier": t,
            "product": product,
            "subsection": subsection_for(url, t),
            "section": ex.breadcrumbs,
            "title": ex.title,
            "etag": headers.get("ETag"),
            "last_modified": headers.get("Last-Modified"),
            "sitemap_lastmod": lastmod,
            "kinsta_last_updated": ex.page_lastmod,
            "sha256": sha,
            "body_chars": len(ex.body_md),
            "extracted_with": ex.selector_used,
            "fetched_at": now_iso(),
            "status": "live",
        }
        staged[url] = (new_rec, rendered)

        if rec and rec.get("sha256") and rec["sha256"] != sha:
            changed.append(url)
            print(f"{prefix} CHANGED  {url}")
        elif rec and rec.get("sha256") == sha:
            print(f"{prefix} same     {url}")
        else:
            added.append(url)
            print(f"{prefix} NEW      {url}")

    _guard_extraction_quality(short_pages, len(staged))

    if args.dry_run:
        print(f"\nDRY RUN - nothing written.")
        print(f"  would add {len(added)}, change {len(changed)}, "
              f"tombstone {len(removed) + len(gone)}")
        if short_pages:
            print(f"  {len(short_pages)} short page(s):")
            for s in short_pages[:15]:
                print(f"    {s}")
        return 0

    # ---- 4. Write ---------------------------------------------------------- #
    for url, (rec, rendered) in staged.items():
        dest = KB / rec["path"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists() and url in changed:
            old, new = body_of(dest), rendered.split("---\n", 2)[-1]
            diff = "\n".join(
                difflib.unified_diff(
                    old.splitlines(), new.splitlines(),
                    fromfile=f"{url} (previous)", tofile=f"{url} (current)",
                    lineterm="", n=2,
                )
            )
            if diff:
                dp = DIFF_DIR / (rec["path"].replace("/", "__") + ".diff")
                dp.write_text(diff + "\n")
        dest.write_text(rendered, encoding="utf-8")
        mf.pages[url] = rec

    for url in removed + gone:
        rec = mf.pages.get(url)
        if not rec:
            continue
        rec["status"] = "removed"
        rec["removed_at"] = now_iso()
        rec["removed_reason"] = "absent from sitemap" if url in removed else "404/410"
        mf.pages[url] = rec
        # Tombstone the file rather than deleting it. A page Kinsta pulled is
        # evidence, and you want it when someone asks why a documented
        # procedure vanished.
        f = KB / rec["path"]
        if f.exists():
            text = f.read_text(encoding="utf-8", errors="replace")
            if 'status: "live"' in text:
                text = text.replace('status: "live"', 'status: "removed"', 1)
                text = text.replace(
                    "---\n\n# ",
                    f'removed_at: "{rec["removed_at"]}"\n---\n\n'
                    f"> **REMOVED FROM KINSTA'S DOCS** as of {rec['removed_at']} "
                    f"({rec['removed_reason']}). Kept as a record of what was "
                    f"published. Do not cite as current.\n\n# ",
                    1,
                )
                f.write_text(text, encoding="utf-8")

    if "api" in tiers:
        _fetch_openapi(fetcher, mf)

    for t in tiers:
        mf.last_sync[t] = now_iso()
    mf.notes["last_sync_unverified"] = len(unverified)
    mf.save()

    build_index(mf)
    build_taxonomy(mf)

    summary = (f"{len(changed)} changed, {len(added)} added, "
               f"{len(removed) + len(gone)} removed, {len(unverified)} unverified")
    _append_sync_log(summary, changed, added, removed + gone, unverified, short_pages)
    print(f"\nSync complete: {summary}")

    if unverified:
        print("\nUnverified (these were NOT checked - do not treat as current):")
        for url, why in unverified[:15]:
            print(f"  {url}  {why}")

    if not args.no_commit:
        _git_commit(f"kb: sync {summary}")

    return 0


def _fetch_openapi(fetcher: Fetcher, mf: Manifest) -> None:
    """The spec is generated from the API itself, so it beats prose on endpoint
    shape - paths, methods, required parameters, response schemas.

    Stored as both YAML (as served, so it can be diffed against upstream byte
    for byte) and JSON (so anything can read it without a YAML parser). The
    `info.version` is worth watching: it moves when Kinsta ships API changes,
    which is an earlier signal than the prose docs catching up.
    """
    print("\nFetching the OpenAPI spec...")
    for url in OPENAPI_CANDIDATES:
        status, body, _, err = fetcher.get(url)
        if err:
            print(f"  {url} -> {err}")
            continue
        if status != 200 or not body:
            print(f"  {url} -> HTTP {status}")
            continue
        try:
            import yaml  # stdlib-adjacent; present on this box
            spec = yaml.safe_load(body)
        except Exception as exc:
            try:
                spec = json.loads(body)
            except json.JSONDecodeError:
                print(f"  {url} -> HTTP 200 but parsed as neither YAML nor JSON "
                      f"({exc}); skipping")
                continue
        if not isinstance(spec, dict) or "paths" not in spec:
            print(f"  {url} -> parsed, but has no `paths`; not an OpenAPI doc")
            continue

        (KB / "api").mkdir(parents=True, exist_ok=True)
        (KB / "api" / "kinsta-openapi.yaml").write_bytes(body)
        (KB / "api" / "openapi.json").write_text(
            json.dumps(spec, indent=2, sort_keys=False) + "\n"
        )

        info = spec.get("info", {})
        prev = (mf.notes.get("openapi") or {}).get("version")
        new_version = info.get("version")
        mf.notes["openapi"] = {
            "url": url,
            "fetched_at": now_iso(),
            "openapi": spec.get("openapi"),
            "title": info.get("title"),
            "version": new_version,
            "endpoints": len(spec.get("paths", {})),
            "tags": [t.get("name") for t in spec.get("tags", []) if t.get("name")],
        }
        print(f"  {info.get('title')} v{new_version} "
              f"(OpenAPI {spec.get('openapi')}), "
              f"{len(spec.get('paths', {}))} paths")
        if prev and prev != new_version:
            print(f"  API VERSION MOVED: {prev} -> {new_version}. "
                  f"Check `git diff kb/api/openapi.json` - the prose docs may "
                  f"not have caught up yet.")
        return

    mf.notes["openapi"] = {"url": None, "checked_at": now_iso(),
                           "result": "no spec found at known locations"}
    print("  No OpenAPI spec at any known location. If Kinsta moved it, the "
          "'Download OpenAPI Specification' link on api-docs.kinsta.com is "
          "where to look.")


def _append_sync_log(summary, changed, added, removed, unverified, short) -> None:
    SYNC_LOG.parent.mkdir(parents=True, exist_ok=True)
    out = [f"\n## {now_iso()}\n", f"{summary}\n"]
    for label, items in (
        ("Changed", changed), ("Added", added), ("Removed", removed),
        ("Short/suspect", short),
    ):
        if items:
            out.append(f"\n**{label}** ({len(items)})\n")
            out.extend(f"- {i}\n" for i in items[:50])
            if len(items) > 50:
                out.append(f"- ...and {len(items) - 50} more\n")
    if unverified:
        out.append(f"\n**Unverified** ({len(unverified)})\n")
        out.extend(f"- {u}  `{w}`\n" for u, w in unverified[:50])
    with SYNC_LOG.open("a") as fh:
        fh.writelines(out)


def _git_commit(message: str) -> None:
    if not (SKILL_DIR / ".git").exists():
        print("  (no git repo yet - run the setup in references/maintenance.md)")
        return
    try:
        subprocess.run(["git", "-C", str(SKILL_DIR), "add", "-A", "kb"],
                       check=True, capture_output=True)
        r = subprocess.run(
            ["git", "-C", str(SKILL_DIR), "commit", "-m", message],
            capture_output=True, text=True,
        )
        if r.returncode == 0:
            print(f"  committed: {message}")
        elif "nothing to commit" in (r.stdout + r.stderr):
            print("  nothing to commit")
        else:
            print(f"  git commit failed: {r.stderr.strip()[:200]}", file=sys.stderr)
    except subprocess.CalledProcessError as exc:
        print(f"  git add failed: {exc.stderr[:200]}", file=sys.stderr)


# --------------------------------------------------------------------------- #
# check - the pre-answer freshness gate
# --------------------------------------------------------------------------- #


def cmd_check(args: argparse.Namespace) -> int:
    mf = Manifest.load()
    fetcher = Fetcher(delay=args.delay)
    verdicts: list[tuple[str, str, str]] = []
    worst = 0

    for raw in args.url:
        url = _resolve_to_url(raw, mf)
        if url is None:
            verdicts.append((raw, "UNKNOWN", "not in the mirror; run `sync` first"))
            worst = max(worst, 1)
            continue

        rec = mf.pages[url]
        if rec.get("status") == "removed":
            verdicts.append((url, "GONE",
                             f"tombstoned {rec.get('removed_at')} "
                             f"({rec.get('removed_reason')})"))
            worst = max(worst, 1)
            continue

        status, body, headers, err = fetcher.get(
            url, etag=rec.get("etag"), last_modified=rec.get("last_modified")
        )

        if err:
            verdicts.append((url, "UNVERIFIED", err))
            worst = max(worst, 2)
            continue
        if status == 304:
            verdicts.append((url, "FRESH",
                             f"304; mirror copy fetched {rec.get('fetched_at')}"))
            continue
        if status in (404, 410):
            verdicts.append((url, "GONE", f"HTTP {status}"))
            worst = max(worst, 1)
            continue
        if status != 200 or not body:
            verdicts.append((url, "UNVERIFIED", f"HTTP {status}"))
            worst = max(worst, 2)
            continue

        ex = extract(body, url)
        sha = sha256_text(ex.body_md)
        if sha == rec.get("sha256"):
            # 200 rather than 304 just means the validators rotated; the body
            # is byte-identical, so the page genuinely has not changed.
            rec["etag"] = headers.get("ETag")
            rec["last_modified"] = headers.get("Last-Modified")
            rec["fetched_at"] = now_iso()
            mf.pages[url] = rec
            verdicts.append((url, "FRESH", "body hash identical"))
            continue

        # Changed. Re-ingest now so the answer is written against current text.
        t = tier_for(url) or rec.get("tier", "docs")
        dest = KB / rec["path"]
        old_body = body_of(dest) if dest.exists() else ""
        rendered = render_page(url, t, product_for(url, t), ex,
                               rec.get("sitemap_lastmod"), sha)
        diff = "\n".join(difflib.unified_diff(
            old_body.splitlines(), rendered.split("---\n", 2)[-1].splitlines(),
            fromfile=f"{url} (mirror)", tofile=f"{url} (live)", lineterm="", n=2))
        DIFF_DIR.mkdir(parents=True, exist_ok=True)
        dp = DIFF_DIR / (rec["path"].replace("/", "__") + ".diff")
        dp.write_text(diff + "\n")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(rendered, encoding="utf-8")

        rec.update({
            "etag": headers.get("ETag"),
            "last_modified": headers.get("Last-Modified"),
            "kinsta_last_updated": ex.page_lastmod,
            "sha256": sha, "body_chars": len(ex.body_md),
            "fetched_at": now_iso(), "title": ex.title,
            "section": ex.breadcrumbs,
        })
        mf.pages[url] = rec
        verdicts.append((url, "CHANGED",
                         f"re-ingested; diff at {dp.relative_to(SKILL_DIR)}"))
        worst = max(worst, 1)

    mf.save()

    print(f"Revalidated {len(verdicts)} page(s) at {now_iso()}\n")
    for url, verdict, note in verdicts:
        print(f"{verdict:<12} {url}")
        print(f"             {note}")
        rec = mf.pages.get(url, {})
        if verdict in ("FRESH", "CHANGED") and rec:
            print(f"             local: kb/{rec.get('path')}  "
                  f"product: {rec.get('product')}  "
                  f"kinsta_last_updated: {rec.get('kinsta_last_updated')}")
        print()

    if any(v == "CHANGED" for _, v, _ in verdicts):
        print("At least one page CHANGED. Read the updated file and its diff "
              "before answering - the change may be the answer.")
    if any(v == "UNVERIFIED" for _, v, _ in verdicts):
        print("At least one page is UNVERIFIED. You did not confirm anything about "
              "it. If you answer from the mirror anyway, date the claim explicitly "
              "rather than presenting it as current.")
    return worst


def _resolve_to_url(raw: str, mf: Manifest) -> str | None:
    """Accept a full URL, a bare doc path, or a local kb/ path."""
    if raw.startswith("http"):
        for cand in (raw, raw.rstrip("/") + "/", raw.rstrip("/")):
            if cand in mf.pages:
                return cand
        return None
    if raw.startswith("/"):
        cand = BASE + raw.rstrip("/") + "/"
        return cand if cand in mf.pages else None
    norm = raw.removeprefix("kb/")
    for url, rec in mf.pages.items():
        if rec.get("path") == norm:
            return url
    return None


# --------------------------------------------------------------------------- #
# search
# --------------------------------------------------------------------------- #


def cmd_search(args: argparse.Namespace) -> int:
    mf = Manifest.load()
    if not KB.exists():
        sys.exit("No mirror on disk. Run `sync` first.")
    if not shutil.which("rg"):
        sys.exit("ripgrep (rg) not found; it is the search engine here.")

    roots = []
    if args.product:
        for tier in ("docs", "api"):
            p = KB / TIERS[tier]["dir"] / args.product
            if p.exists():
                roots.append(p)
        if not roots:
            known = sorted({r.get("product") for r in mf.live().values() if r.get("product")})
            sys.exit(f"No pages for product '{args.product}'.\nKnown: {', '.join(known)}")
    elif args.tier:
        for t in args.tier.split(","):
            t = t.strip()
            if t not in TIERS:
                sys.exit(f"Unknown tier '{t}'. Known: {', '.join(TIERS)}")
            roots.append(KB / TIERS[t]["dir"])
    else:
        roots = [KB / cfg["dir"] for cfg in TIERS.values()]
    roots = [r for r in roots if r.exists()]
    if not roots:
        sys.exit("Nothing to search - those paths are not in the mirror yet.")

    cmd = ["rg", "--line-number", "--no-heading", "--color=never",
           "--smart-case", "--max-columns", "400", "-g", "*.md"]
    if args.context:
        cmd += ["--context", str(args.context)]
    cmd += [args.query, *[str(r) for r in roots]]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode not in (0, 1):
        sys.exit(f"rg failed: {r.stderr[:300]}")

    by_path: dict[str, list[str]] = {}
    for line in r.stdout.splitlines():
        try:
            path, lineno, text = line.split(":", 2)
        except ValueError:
            continue
        rel = str(Path(path).relative_to(KB))
        by_path.setdefault(rel, []).append(f"{lineno}: {text.strip()[:220]}")

    meta = {rec["path"]: (url, rec) for url, rec in mf.pages.items() if "path" in rec}
    ranked = sorted(by_path.items(), key=lambda kv: -len(kv[1]))[: args.limit]

    if not ranked:
        print(f'No matches for "{args.query}" in the mirror.')
        print("That means the phrase is absent from these files - not that Kinsta "
              "lacks the feature. Try a synonym, widen --tier, or `sync` first if "
              "the mirror is stale.")
        return 1

    products_hit: set[str] = set()
    print(f'{len(by_path)} file(s) match "{args.query}"; showing top {len(ranked)}\n')
    for rel, hits in ranked:
        url, rec = meta.get(rel, (None, {}))
        products_hit.add(rec.get("product") or "?")
        removed = " [REMOVED FROM KINSTA'S DOCS]" if rec.get("status") == "removed" else ""
        print(f"kb/{rel}{removed}")
        print(f"  {rec.get('title', '?')}")
        print(f"  product: {PRODUCT_LABELS.get(rec.get('product'), rec.get('product'))}"
              f"   tier: {rec.get('tier')}   hits: {len(hits)}")
        if rec.get("section"):
            print(f"  section: {' > '.join(rec['section'])}")
        print(f"  {url}")
        for h in hits[:3]:
            print(f"    {h}")
        print()

    if len(products_hit - {"?"}) > 1 and _is_cross_product(args.query):
        print("NOTE: these hits span multiple Kinsta products "
              f"({', '.join(sorted(products_hit - {'?'}))}), and \"{args.query}\" is a "
              "term that means different things per product. Establish which product "
              "the user has before answering, then re-search with --product.")
    return 0


def _is_cross_product(query: str) -> bool:
    q = query.lower()
    return any(term in q for term in CROSS_PRODUCT_TERMS)


# --------------------------------------------------------------------------- #
# show / status / tree
# --------------------------------------------------------------------------- #


def cmd_show(args: argparse.Namespace) -> int:
    mf = Manifest.load()
    url = _resolve_to_url(args.target, mf)
    if url is None:
        p = KB / args.target.removeprefix("kb/")
        if p.exists():
            print(p.read_text(encoding="utf-8", errors="replace"))
            return 0
        sys.exit(f"Not in the mirror: {args.target}")
    p = KB / mf.pages[url]["path"]
    if not p.exists():
        sys.exit(f"Manifest lists {p} but the file is missing. Run `sync`.")
    print(p.read_text(encoding="utf-8", errors="replace"))
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    if not MANIFEST.exists():
        print("No mirror yet. manifest.json does not exist.")
        print(f"Expected at: {MANIFEST}")
        print("\nRun `sync` before answering any Kinsta question - there is nothing "
              "here to answer from, and model recall of Kinsta's docs is not a "
              "substitute for the docs.")
        return 1

    mf = Manifest.load()
    live = mf.live()
    removed = [r for r in mf.pages.values() if r.get("status") == "removed"]

    print(f"Kinsta docs mirror at {KB}")
    print(f"Pages: {len(live)} live, {len(removed)} tombstoned\n")

    print(f"{'tier':<12}{'pages':>7}  {'last successful sync':<24} age")
    for t in TIERS:
        n = len(mf.live(t))
        ls = mf.last_sync.get(t)
        if ls:
            age_h = (dt.datetime.now(UTC)
                     - dt.datetime.strptime(ls, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=UTC)
                     ).total_seconds() / 3600
            age = f"{age_h / 24:.1f}d" if age_h > 48 else f"{age_h:.1f}h"
            flag = "  <-- STALE" if age_h > 72 else ""
        else:
            age, flag = "never", "  <-- NEVER SYNCED"
        print(f"{t:<12}{n:>7}  {ls or '-':<24} {age}{flag}")

    counts: dict[str, int] = {}
    for rec in live.values():
        counts[rec.get("product", "?")] = counts.get(rec.get("product", "?"), 0) + 1
    if counts:
        print("\nPages per product:")
        for prod, n in sorted(counts.items(), key=lambda kv: -kv[1]):
            print(f"  {PRODUCT_LABELS.get(prod, prod):<36} {n:>5}")

    oa = mf.notes.get("openapi") or {}
    print(f"\nOpenAPI spec: {oa.get('url') or 'none found'}"
          + (f"  ({oa.get('endpoints')} paths, v{oa.get('version')})"
             if oa.get("url") else ""))

    if mf.notes.get("last_sync_unverified"):
        print(f"\nLast sync left {mf.notes['last_sync_unverified']} page(s) "
              "UNVERIFIED. See kb/SYNC-LOG.md.")

    stale = [t for t in TIERS if not mf.last_sync.get(t)]
    if stale:
        print(f"\nNever synced: {', '.join(stale)}. "
              "Answers about those areas have no local source.")
    return 0


def cmd_tree(args: argparse.Namespace) -> int:
    mf = Manifest.load()
    live = mf.live(args.tier) if args.tier else mf.live()
    if not live:
        sys.exit("Nothing in the mirror for that tier. Run `sync`.")
    tree: dict[str, dict[str, list[str]]] = {}
    for url, rec in live.items():
        prod = rec.get("product", "?")
        sub = _group_key(rec)
        tree.setdefault(prod, {}).setdefault(sub, []).append(rec.get("title", url))
    for prod in sorted(tree, key=lambda p: -sum(len(v) for v in tree[p].values())):
        total = sum(len(v) for v in tree[prod].values())
        print(f"\n{PRODUCT_LABELS.get(prod, prod)}  ({total} pages)  [{prod}]")
        for sub in sorted(tree[prod]):
            print(f"  {sub}  ({len(tree[prod][sub])})")
            if args.verbose:
                for title in sorted(tree[prod][sub]):
                    print(f"    - {title}")
    return 0


# --------------------------------------------------------------------------- #
# Generated navigation artifacts
# --------------------------------------------------------------------------- #


def _group_key(rec: dict) -> str:
    """How a page is filed under its product.

    The URL-derived subsection is preferred over the breadcrumb trail because
    it comes from Kinsta's own path hierarchy and survives markup changes,
    whereas breadcrumbs are scraped and go empty the moment a class name moves.
    """
    sub = rec.get("subsection")
    if sub:
        return sub.replace("-", " ")
    crumbs = rec.get("section") or []
    return crumbs[1] if len(crumbs) > 1 else "General"


def build_index(mf: Manifest) -> None:
    """kb/INDEX.md - the map read first, so the common case needs no search.

    Grouped by product rather than alphabetically, because 'which product' is
    the question that has to be settled before any other one here.
    """
    live = mf.live()
    by_product: dict[str, list[tuple[str, dict]]] = {}
    for url, rec in live.items():
        by_product.setdefault(rec.get("product", "?"), []).append((url, rec))

    out = [
        "# Kinsta documentation mirror - index",
        "",
        f"Generated {now_iso()} from `manifest.json`. "
        f"{len(live)} live pages.",
        "",
        "Read this to orient before searching. Pages are grouped by **product**, "
        "because Kinsta's products reuse the same vocabulary for different "
        "mechanics and picking the wrong tree produces a confident wrong answer. "
        "Revalidate any page you intend to cite:",
        "",
        "```bash",
        "python3 scripts/kinsta_kb.py check --url <url>",
        "```",
        "",
    ]
    for prod in sorted(by_product, key=lambda p: -len(by_product[p])):
        pages = sorted(by_product[prod], key=lambda kv: kv[1].get("title") or "")
        out.append(f"## {PRODUCT_LABELS.get(prod, prod)}  (`{prod}`, {len(pages)} pages)")
        out.append("")
        by_section: dict[str, list[tuple[str, dict]]] = {}
        for url, rec in pages:
            by_section.setdefault(_group_key(rec), []).append((url, rec))
        for section in sorted(by_section):
            out.append(f"### {section}")
            out.append("")
            for url, rec in sorted(by_section[section],
                                   key=lambda kv: kv[1].get("title") or ""):
                out.append(f"- **{rec.get('title')}** - `kb/{rec['path']}`  \n"
                           f"  {url}")
            out.append("")
    removed = [(u, r) for u, r in mf.pages.items() if r.get("status") == "removed"]
    if removed:
        out.append(f"## Removed from Kinsta's docs ({len(removed)})")
        out.append("")
        out.append("Kept as a record of what was once published. Do not cite as "
                   "current behavior.")
        out.append("")
        for url, rec in sorted(removed):
            out.append(f"- {rec.get('title')} - removed {rec.get('removed_at')} - {url}")
        out.append("")
    INDEX_MD.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"  wrote {INDEX_MD.relative_to(SKILL_DIR)}")


def build_taxonomy(mf: Manifest) -> None:
    live = mf.live()
    counts: dict[str, dict[str, int]] = {}
    for rec in live.values():
        prod = rec.get("product", "?")
        sub = _group_key(rec)
        counts.setdefault(prod, {})
        counts[prod][sub] = counts[prod].get(sub, 0) + 1

    out = [
        "# Kinsta docs taxonomy (generated)",
        "",
        f"Regenerated by `sync` on {now_iso()}. {len(live)} live pages.",
        "",
        "Use this to answer \"what does Kinsta document about X at all?\" and to "
        "pick a `--product` / `--section` scope for search. This file is "
        "generated - edit the generator, not the file.",
        "",
        "| Product | Section | Pages |",
        "|---|---|---|",
    ]
    for prod in sorted(counts, key=lambda p: -sum(counts[p].values())):
        for sub, n in sorted(counts[prod].items(), key=lambda kv: -kv[1]):
            out.append(f"| {PRODUCT_LABELS.get(prod, prod)} | {sub} | {n} |")
    TAXONOMY_MD.parent.mkdir(parents=True, exist_ok=True)
    TAXONOMY_MD.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"  wrote {TAXONOMY_MD.relative_to(SKILL_DIR)}")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="kinsta_kb.py",
        description="Build, refresh and query a local mirror of Kinsta's docs.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("sync", help="sitemap-driven incremental ingest")
    s.add_argument("--tier", help=f"comma-separated; default {','.join(DEFAULT_TIERS)}")
    s.add_argument("--section", help="limit to one URL section, e.g. wordpress-hosting")
    s.add_argument("--full", action="store_true",
                   help="ignore lastmod/ETag and re-fetch everything in scope")
    s.add_argument("--dry-run", action="store_true",
                   help="report what would change, write nothing")
    s.add_argument("--limit", type=int, help="cap pages fetched (for testing)")
    s.add_argument("--blog-months", type=int, default=BLOG_MONTHS,
                   help=f"blog recency window in months by PUBLISH date "
                        f"(default {BLOG_MONTHS}); ignored for other tiers")
    s.add_argument("--delay", type=float, default=DEFAULT_DELAY,
                   help=f"seconds between requests (default {DEFAULT_DELAY})")
    s.add_argument("--no-commit", action="store_true", help="skip the git commit")
    s.add_argument("--force-unlock", action="store_true",
                   help="clear a lock you know is dead")
    s.set_defaults(func=cmd_sync)

    c = sub.add_parser("check", help="revalidate pages before citing them")
    c.add_argument("--url", action="append", required=True,
                   help="full URL, /docs/ path, or kb/ path; repeatable")
    c.add_argument("--delay", type=float, default=0.3)
    c.set_defaults(func=cmd_check)

    g = sub.add_parser("search", help="full-text search the mirror")
    g.add_argument("query")
    g.add_argument("--tier", help="comma-separated tiers to search")
    g.add_argument("--product", help="scope to one product slug, e.g. wordpress-hosting")
    g.add_argument("--limit", type=int, default=10)
    g.add_argument("--context", type=int, help="lines of context around each hit")
    g.set_defaults(func=cmd_search)

    sh = sub.add_parser("show", help="print a mirrored page")
    sh.add_argument("target", help="URL or kb/ path")
    sh.set_defaults(func=cmd_show)

    st = sub.add_parser("status", help="mirror size, age and coverage")
    st.set_defaults(func=cmd_status)

    tr = sub.add_parser("tree", help="section taxonomy with page counts")
    tr.add_argument("--tier")
    tr.add_argument("--verbose", "-v", action="store_true", help="list page titles")
    tr.set_defaults(func=cmd_tree)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        release_lock()
        sys.exit(130)
