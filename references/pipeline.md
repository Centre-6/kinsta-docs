# How the ingest pipeline works

Read this before changing `scripts/kinsta_kb.py`, or when a page converts badly
and you need to know which stage to blame.

## Contents

- [The four stages](#the-four-stages)
- [Enumeration: why the blog uses a different source](#enumeration-why-the-blog-uses-a-different-source)
- [Change detection, and what is actually available](#change-detection-and-what-is-actually-available)
- [Body extraction and the sanity floor](#body-extraction-and-the-sanity-floor)
- [Segmentation: what one page file looks like](#segmentation-what-one-page-file-looks-like)
- [The manifest](#the-manifest)
- [Tombstones](#tombstones)
- [Things that look like bugs and are not](#things-that-look-like-bugs-and-are-not)

## The four stages

```
enumerate  ->  decide  ->  fetch + extract  ->  write
(sitemaps,     (compare   (HTTP, bs4, md     (markdown files,
 WP REST)       change     conversion,        manifest, INDEX.md,
                signals)   sanity floor)      taxonomy, git commit)
```

Everything is staged in memory and written only after the sanity floor passes
for the whole run. That is deliberate: a half-applied sync that wrote 300 good
pages and 270 pages of navigation chrome is much harder to recover from than one
that wrote nothing and told you why.

## Enumeration: why the blog uses a different source

Three tiers come from sitemaps. The blog comes from the WordPress REST API, and
that asymmetry is load-bearing rather than an inconsistency.

Kinsta re-touches old blog posts, which bumps their sitemap `lastmod`. Measured
October 7, 2026: **1,308 of 1,551 posts carried a `lastmod` inside the last 12
months, while only ~140 were actually published in that window.** A recency
filter built on `lastmod` therefore looks like it is working and quietly pulls
almost the entire blog — a nine-fold overshoot with no error anywhere.

`kinsta.com/wp-json/wp/v2/posts?after=<cutoff>` filters on the publish date,
returns `X-WP-Total` so the count is known up front, and costs two requests for
the whole enumeration. The lesson generalizes: **before filtering on a
timestamp, find out what event that timestamp records.**

Tier routing is on `(host, path prefix)`, not path alone, because the API
reference lives on `api-docs.kinsta.com` with its own sitemap. Non-English
locales (`/de/`, `/es/`, `/fr/`, `/it/`, `/jp/`, `/nl/`, `/pt/`) are excluded in
`tier_for` — translations lag the English originals, so mirroring them would put
a stale translation in competition with a current source for the same answer.

## Change detection, and what is actually available

**Kinsta serves docs pages with `cache-control: private, no-cache, no-store` and
no `ETag` or `Last-Modified`.** Verified October 7, 2026 on
`kinsta.com/docs/wordpress-hosting/`. There is no conditional GET to make there
and no 304 to collect.

So the two layers use different signals, and neither is the one you would reach
for first:

| Layer | Signal | Cost |
|---|---|---|
| `sync` | sitemap `<lastmod>` (present on all 190 docs URLs) vs the stored value | a few sitemap fetches, then one GET per moved page |
| `check` | SHA-256 of the extracted body text vs the stored hash | one full GET per page checked |

The conditional-GET headers are still sent, because `api-docs.kinsta.com` is a
different stack and may honor them, and sending them costs nothing. Do not
mistake the presence of that code for a claim that 304s are happening — the
`check` code path treats a 200 with a matching body hash as `FRESH` precisely
because that is the case that actually occurs.

Hashing the **body** rather than the whole file matters: frontmatter carries
`fetched_at`, so a whole-file hash would report a change on every sync and the
git history would be noise.

## Body extraction and the sanity floor

`BODY_SELECTORS` is a list tried in order, most specific first, and the first
selector producing a body over `MIN_BODY_CHARS` (200) wins. `STRIP_SELECTORS`
removes nav, aside, footer, feedback widgets and related-article blocks *before*
conversion, so chrome cannot inflate the length and defeat the floor.

The failure mode this guards against does not look like a failure. A site
redesign returns HTTP 200, the selector matches some wrapper div, markdownify
happily converts it, and you get a file full of sidebar links. Nothing errors.

`_guard_extraction_quality` is the detector, and the **ratio** is the half that
does the work: if more than 20% of a run's pages come out under the floor (and
at least 3 do), the run aborts and writes nothing. One short page is plausible
content. A fifth of the corpus going short simultaneously is a redesign.

When it fires, the repair order matters:

1. Fetch one known-good page by hand and **look at the HTML yourself**. Do not
   infer the new selector from the old one.
2. Update `BODY_SELECTORS`.
3. `sync --full --dry-run`, which reports per-page body lengths and writes
   nothing. Confirm real content across several sections, not just the one page
   you were looking at.
4. `sync --full`.

Breadcrumbs come from the markup first and **JSON-LD `BreadcrumbList` second**.
The JSON-LD fallback exists because scraped breadcrumbs vanish the moment a
class name moves, and structured data is more stable than presentation markup.
Grouping, though, prefers the **URL-derived subsection** over breadcrumbs for
the same reason — `/docs/wordpress-hosting/caching/x/` tells you `caching`
without reading any markup at all.

## Segmentation: what one page file looks like

One page becomes one markdown file: frontmatter, an H1, a provenance block, a
per-page table of contents, then the body.

```markdown
---
url: "https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/"
title: "Edge Caching"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "caching"
section: ["WordPress Hosting", "Caching"]
kinsta_last_updated: "2026-08-14T10:22:00+00:00"
sitemap_lastmod: "2026-08-14"
fetched_at: "2026-10-07T22:20:17Z"
sha256: "..."
body_chars: 4210
extracted_with: "main article"
status: "live"
---

# Edge Caching

**Section:** WordPress Hosting > Caching
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/...
**Kinsta last updated:** 2026-08-14T10:22:00+00:00

## On this page

- [How it works](#how-it-works)
- [Purging](#purging)
...
```

The per-page TOC is not decoration. It is what makes a search hit list usable:
you can see a page's whole shape without loading its body, which is how you pick
the right page out of eight candidates. Emitted only when a page has 3+
headings, because below that it is just clutter.

`kinsta_last_updated` comes from `article:modified_time`, `og:updated_time`,
JSON-LD `dateModified`, or a "Last updated" string in the text, in that order.
It answers "when did Kinsta change this?", which is a different and more useful
question than "when did we fetch it?"

## The manifest

`kb/manifest.json` is the operational index — one record per URL with its local
path, tier, product, subsection, hashes, change signals, and status. It is what
`check`, `status`, `search` metadata, `INDEX.md` and `taxonomy.md` all read from.

`kb/INDEX.md` and `references/taxonomy.md` are **generated** from it on every
sync. Edit the generators (`build_index`, `build_taxonomy`), never the files —
your edit will be overwritten by the next cron run and you will not find out for
a day.

## Tombstones

A URL that leaves the sitemap, or returns 404/410, is marked `status: removed`
with a date and reason. The file is **kept**, with a banner at the top saying it
was removed and must not be cited as current.

Deleting it would be the obvious move and it is the wrong one. A page Kinsta
pulled is evidence — when someone asks why a documented procedure vanished, or
whether a behavior was ever documented at all, the tombstone plus the git commit
that created it is the entire answer. `INDEX.md` lists removals in their own
section so they cannot be mistaken for current docs.

Content that moved shows up as a removal plus an addition in the same run, and
`sync` reports both so the pair is visible.

## Things that look like bugs and are not

- **`sync` fetches a page whose `lastmod` did not change.** It also re-fetches
  when the manifest claims a file that is not on disk. That check exists because
  a manifest-without-file state is silently unanswerable otherwise.
- **`check` on a page `sync` just fetched still does a full GET.** Yes — see the
  change-detection table. There is no cheaper correct option on this host.
- **Two tiers share one sitemap.** `docs` and `changelog` both come from
  `sitemap_index.xml`; `enumerate_scope` de-duplicates the fetch and routes by
  tier afterward.
- **`--limit 0` does not mean "zero pages".** It is falsy, so it means no limit.
  Use `--dry-run` if you want to fetch nothing.
- **The lock survives a crash for up to 2 hours.** `sync` clears locks older
  than `LOCK_STALE_SECONDS` itself; `--force-unlock` is for when you know the
  holder is dead and do not want to wait. A quiet filesystem is not evidence
  that no other sync is running, which is why the lock exists at all.
