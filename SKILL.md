---
name: kinsta-docs
description: Authoritative local mirror of Kinsta's documentation (kinsta.com/docs), the Kinsta API reference and OpenAPI spec, the Kinsta changelog, and Kinsta blog articles — with a revalidate-before-you-answer step so answers reflect what Kinsta publishes right now, not a stale cache. Use this skill whenever Kinsta comes up in any form: MyKinsta, Kinsta hosting, Application Hosting, Static Site Hosting, Database Hosting, DevKinsta, the Kinsta API, Kinsta cache or CDN or edge caching, Kinsta staging environments, Kinsta backups, Kinsta redirects, Kinsta SSH/SFTP/WP-CLI, PHP or nginx settings on Kinsta, Kinsta DNS, Kinsta plans and limits, or migrating a site to or from Kinsta. Use it even when the user does not say the word "docs" — if the question is about how something works on Kinsta, or you are about to write code, config, a CLI command, or a client-facing explanation that depends on Kinsta behavior, consult this skill first rather than answering from memory. Kinsta ships changes frequently and model recall of their docs goes stale silently.
---

# Kinsta Docs

A complete, segmented, local mirror of Kinsta's published documentation, plus the
machinery to keep it current and to prove it is current at the moment you answer.

The point of this skill is not just "we have the docs on disk." Having a copy is
easy; the hard part is that a cached copy quietly becomes wrong. Kinsta changes
PHP version availability, plan limits, cache behavior, API endpoints and UI
labels without announcement. An answer drawn from a three-week-old mirror reads
exactly as confident as a correct one. So this skill treats **freshness as part
of the answer**, not as housekeeping you do later.

## Where things live

```
<skill>/kb/
├── INDEX.md              # the map: section tree -> page titles -> paths. Read this first.
├── manifest.json         # per-URL state: path, product, subsection, sha256, lastmod, fetched_at
├── SYNC-LOG.md           # append-only history of what each sync changed
├── docs/<section>/<slug>.md
├── api/
│   ├── openapi.json      # OpenAPI 3.1.0 spec, 84 endpoints (also as .yaml)
│   └── api-reference/<tag>/<endpoint>.md
├── changelog/<slug>.md
└── blog/<slug>.md
```

Every page file carries YAML frontmatter with its source URL, `product` and
`subsection`, Kinsta's own last-updated date, the body hash, and when we last
fetched it. That frontmatter is what lets you cite precisely, scope to the right
product, and judge staleness per page instead of per-mirror. (`section` holds
scraped breadcrumbs and is often empty — Kinsta does not render them
consistently. `subsection` comes from the URL path and is always there, which is
why grouping and scoping use it.)

The whole skill is one git repo (private, `Centre-6/kinsta-docs`), and `kb/` is
tracked inside it. That is deliberate: `git log -p kb/docs/...` shows you the
exact wording Kinsta changed and when we noticed. When a client asks "did this
always work this way?", the diff is the answer.

## First: establish what the user actually has

Answering about the wrong thing is the most damaging mistake available here,
because a wrong-surface answer is coherent, confident, well-sourced and wrong.
It is often *almost* right, so it survives a skim and fails in production. Two
separate traps, and they are different problems.

### Trap 1: Kinsta is now WordPress-only. Three products left the company.

**Kinsta spun Application Hosting, Database Hosting and Static Site Hosting out
into a separate company, Sevalla.** `kinsta.com/docs/application-hosting/` now
301-redirects to `docs.sevalla.com`. Verified October 7, 2026.

What that means for you:

- **This mirror covers Kinsta only, by decision.** Sevalla is not in it and is
  not to be added without asking Tim. Their docs declare
  `Content-Signal: ai-input=no`; Kinsta's declare `ai-input=yes`.
- If someone asks about app hosting, managed Postgres, or static site hosting on
  Kinsta, **there is no answer in here**. Say that it is outside what Kinsta's
  own docs now cover. Do not reach into the WordPress tree for something
  adjacent-sounding — the WordPress `database-management` pages are about a
  WordPress site's own MySQL, not a standalone managed database, and conflating
  them produces exactly the wrong-product answer this section exists to stop.
- A user may still *have* a legacy Kinsta account for one of those products.
  Their having it and Kinsta documenting it are now different facts.

### Trap 2: within WordPress hosting, one word covers several mechanisms

What is actually in the mirror, with page counts as of October 7, 2026:

| Area | `product` slug | Pages | What it is |
|---|---|---|---|
| Managed WordPress Hosting | `wordpress-hosting` | 112 | The product. Sites, environments, caching, CDN, PHP, backups, migrations |
| DevKinsta | `devkinsta` | 25 | A **local** dev tool on your own machine. Not hosting. Shares vocabulary with it anyway |
| Service Information | `service-information` | 17 | Policies, regions, limits, service-level facts |
| Billing | `billing` | 13 | Plans, invoices, overage |
| MyKinsta Company Settings | `company-settings` | 12 | Company-level users, roles, API keys |
| MyKinsta User Settings | `user-settings` | 5 | Individual account settings, 2FA |
| Support | `support` | 4 | How to reach support, what they cover |
| Kinsta API Reference | `api` (tier) | 120 | Every endpoint, plus `kb/api/openapi.json` (84 endpoints, v1.111.0) |
| Changelog | `changelog` | 210 | What shipped when, back to 2016 |
| Blog | `blog` | ~140 | Last 12 months only. Secondary, never outranks docs |

Inside `wordpress-hosting`, the subsection is where the real distinction lives —
`caching`, `wordpress-cdn`, `site-management`, `php`, `database-management`,
`wordpress-backups-and-disaster-recovery`, `staging-environment`,
`redirect-rules`, `connect-to-ssh`, and others. `search` and `tree` both expose
these, and every page file carries `product` and `subsection` in its
frontmatter.

**The ambiguous words.** Each of these maps to more than one mechanism in
Kinsta's own docs, so a grep hit is "right topic, which mechanism?" and not an
answer:

| Word | The mechanisms it could mean |
|---|---|
| `cache` | Edge caching (Kinsta's CDN layer) · page cache · object cache · the `kinsta-mu-plugin`'s cache purging · browser cache · DevKinsta's local cache |
| `CDN` | Kinsta CDN (Cloudflare-backed) vs a third-party CDN you point at the site |
| `backup` | Automatic daily · hourly add-on · manual · downloadable · system-generated before a change — different retention and different restore paths |
| `environment` | Live vs staging vs premium staging, plus "push to live" which is not symmetric |
| `database` | A WordPress site's own MySQL (in scope) vs standalone managed Database Hosting (gone to Sevalla) |
| `logs` | Error logs · access logs · the MyKinsta log viewer · `kinsta-mu-plugin` output |
| `domain` | Primary domain · domain alias · the `*.kinsta.cloud` temp URL · DNS hosted at Kinsta vs elsewhere |
| `restart` | Restart PHP vs restart the site vs clear cache — commonly confused in support threads |

### How to establish it, cheapest first

1. **The user said it.** "my WordPress site on Kinsta", "the staging
   environment" settles it. Take them at their word about what they have.
2. **The surrounding work says it.** A repo with `wp-config.php` and
   `wp-content/` is WordPress hosting. A DevKinsta question usually mentions
   running things locally, Docker Desktop, or `*.local`.
3. **Ask the Kinsta API** if a key is available — the only method that is
   evidence rather than inference, because it reports what the account actually
   contains:
   ```bash
   ls ~/.claude/secrets/ | grep -i kinsta
   ```
   With a key, `GET /sites` and `GET /sites/{id}/environments` answer it
   definitively (see `kb/api/openapi.json`). With no key, say so rather than
   guessing — "I can't see the account, is this the live or staging
   environment?" is a one-line question that prevents a whole wrong answer.
4. **Ask.** If 1–3 leave it open, ask. A few seconds of the user's time against
   a confidently wrong procedure applied to a live site is not a close call.

### When the question genuinely spans surfaces

Sometimes the comparison *is* the answer ("does staging get edge caching too?").
Answer per surface and label each line rather than blending them:

> - **Live environment:** <answer> — <url>
> - **Staging environment:** <answer> — <url>

And scope negative claims to the surface you actually checked. "Kinsta's
DevKinsta docs don't cover X" is a different and much safer claim than "Kinsta
doesn't support X."

## The one rule: revalidate the pages you are about to rely on

Before you state anything as current Kinsta behavior — in an answer, a config
file, a script, a client email, a Trello comment — revalidate the specific pages
backing that claim:

```bash
python3 <skill>/scripts/kinsta_kb.py check --url <url> [--url <url> ...]
```

It prints one verdict per URL:

| Verdict | Meaning | What you do |
|---|---|---|
| `FRESH` | Server confirmed our copy is current | Answer from the local file |
| `CHANGED` | Page differs; it was re-ingested and a diff was written | **Read the updated file and the diff before answering.** The change may be the whole answer |
| `GONE` | 404/410 — Kinsta removed or moved the page | Do not cite it. Re-run `sync` to find where the content went |
| `UNVERIFIED` | Network error, timeout, bot challenge, rate limit | You did **not** verify anything. Say so |

`UNVERIFIED` is the one that matters most, and it is the one that is tempting to
round down to `FRESH` because the local file is sitting right there and looks
fine. Don't. A check that failed to run proves nothing about the page, and
"I couldn't reach Kinsta, so this is from our mirror as of <date>" is a perfectly
good answer. Silently serving a cache you failed to validate, while sounding
certain, is the failure this whole skill exists to prevent.

Revalidate the handful of pages you will actually cite, not the whole mirror.
Two to five pages is normal and takes a few seconds.

**How it actually works.** Kinsta serves docs pages with `cache-control:
private, no-cache, no-store` and emits **no `ETag` and no `Last-Modified`**
(verified October 7, 2026), so there is no conditional GET to make and no 304 to
collect. Instead:

- **docs, changelog and blog pages** revalidate through kinsta.com's WordPress
  REST API — one small JSON object per page. It returns both the current
  `content.rendered` (hashed and compared to the stored body hash) and
  `modified_gmt` (an independent change signal from Kinsta's own database). Two
  signals, and cheap enough that revalidating is never the reason not to.
- **API reference pages** (api-docs.kinsta.com) have no WordPress behind them,
  so those fetch the rendered page and compare the body hash alone.

`FRESH` means the body is byte-identical, which is a stronger claim than a 304.
Revalidate the pages you are citing, not the mirror.

`sync` and `check` do different jobs and you want both: `sync` keeps the corpus
complete (new pages, deletions, hierarchy changes), `check` makes one specific
answer defensible right now.

## Finding the right pages

Work outside-in, cheapest first:

1. **`kb/INDEX.md`** — every page title grouped by product and subsection, with
   its local path and URL. Read this to orient. It is built to be skimmed, so you
   can usually name the two or three pages that matter without searching at all.
2. **Full-text search** when you need a specific term, flag, header, or limit:
   ```bash
   python3 <skill>/scripts/kinsta_kb.py search "edge cache purge" --limit 10
   ```
   This is ripgrep underneath with the manifest metadata joined on, so hits come
   back with product, subsection, title and URL rather than a bare path. Add
   `--tier docs` to exclude blog noise, or `--product wordpress-hosting` to scope
   it. When results straddle products and the query is one of the ambiguous words
   above, `search` says so rather than letting you pick the first hit.
3. **Read the page file.** Read the whole page, not just the matched line. Kinsta
   docs routinely qualify a procedure three paragraphs later ("this does not
   apply to staging environments", "available on Business plans and above",
   "clear any plugin cache first"), and a grep hit on the happy path with the
   caveat left unread is how you ship a confidently wrong answer. The per-page
   `## On this page` table of contents is there so you can see a page's full
   shape before committing to reading it.

If you searched and found nothing, say what you searched for: "I did not find
anything in the Kinsta docs for `<term>`" is honest and useful. "Kinsta does not
support that" is a much stronger claim and usually not one a failed grep earns —
a feature can exist under vocabulary you did not guess. When the stakes justify
it, re-run `sync` first so you know you are searching a current corpus, then try
Kinsta's own site search for the term before concluding it is absent.

## Tiers, and which source wins

Not all of this mirror carries equal weight. When sources disagree, prefer in
this order:

1. **`api/openapi.json`** — machine-readable, generated from the API itself.
   For endpoint paths, methods, required parameters and response shapes, the
   spec beats prose every time.
2. **`docs/`** — Kinsta's official documentation. The default authority for
   behavior, procedures, limits and UI navigation.
3. **`changelog/`** — authoritative for *when* something changed, and invaluable
   for explaining why a doc page or UI label moved. Not a substitute for the doc.
4. **`blog/`** — marketing and tutorial content. Useful for context, worked
   examples and the occasional explanation the docs skip. **Never let a blog post
   outrank `docs/` on a factual or procedural claim.** Blog posts are dated,
   often written against an older UI, and are not maintained the way docs are.
   If a blog post is your only source for something load-bearing, say that
   explicitly and treat it as unconfirmed.

## How to cite

Give the user the Kinsta URL, because that is what they can open and what they
can send to Kinsta support. Include the revalidation state so they know how much
to trust it:

> <the behavior, in the user's terms> —
> https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/
> (revalidated just now; Kinsta's own last-updated on that page is <date>).

Fill that in from the page you actually read. Do not carry an example's numbers
into a real answer — every limit, default and retention figure in Kinsta's docs
is a thing to read off the page at the time you answer, not to recall.

If a page came back `CHANGED` during your check, lead with that. A doc that moved
under you is usually more interesting to the user than the answer itself.

If you are relying on a page you could not revalidate, date it plainly:
"from our mirror, fetched 2026-09-28; I couldn't reach Kinsta to confirm."

## Keeping the mirror current

```bash
python3 <skill>/scripts/kinsta_kb.py sync              # incremental; all four tiers
python3 <skill>/scripts/kinsta_kb.py sync --tier docs  # one tier only
python3 <skill>/scripts/kinsta_kb.py sync --full       # ignore lastmod, re-fetch everything
python3 <skill>/scripts/kinsta_kb.py sync --dry-run    # report changes, write nothing
python3 <skill>/scripts/kinsta_kb.py status            # per-tier counts, age, staleness flags
python3 <skill>/scripts/kinsta_kb.py tree -v           # the taxonomy, with page titles
```

`sync` is cheap by design. docs, changelog and blog come from kinsta.com's
WordPress REST API, which returns each post's content **with** the listing — so
all 537 of those pages are enumerated and ingested in about a dozen requests
rather than 537. Only the 120 API-reference pages are fetched individually.

Two things worth knowing about why it works this way, because both were
discovered the hard way:

- **Kinsta's changelog sitemap is incomplete.** Yoast lists 122 entries; the
  REST API reports 210. The 89 it omits span 2016 through June 2025 and include
  live, relevant posts. A sitemap-driven changelog silently missed 42% of it.
  If you ever add a tier, check the REST count against the sitemap count before
  trusting either.
- **Blog recency uses the publish date, not `lastmod`.** Kinsta re-touches old
  posts, so a `lastmod` window pulls ~1,300 posts where a publish window pulls
  ~140. To widen the blog, raise `--blog-months`; do not switch the signal.

It also handles the cases a naive crawler gets wrong:

- **New URLs** are fetched, segmented, and added to `INDEX.md`.
- **Removed URLs** are tombstoned, not deleted — the file stays with
  `status: removed` in its frontmatter and the date we noticed. A page Kinsta
  pulled is evidence, and you will want it when someone asks why a documented
  procedure vanished.
- **Moved content** shows up as a removal plus an addition. `sync` reports both
  together so you can see the pair.
- Every run appends to `SYNC-LOG.md` and commits to the skill's git repo with a
  `kb:` prefix, so the history of Kinsta's documentation as we observed it is
  reconstructable with `git log -p kb/docs/...`.

A daily cron runs `sync`. `status` tells you when it last succeeded — if that
number is old, the cron is broken and the pre-answer `check` is doing all the
work. Say so rather than assuming the mirror is current.

## Before you trust this skill the first time in a session

Run `status`. It costs nothing and tells you whether you are working against a
real mirror or an empty directory:

```bash
python3 <skill>/scripts/kinsta_kb.py status
```

If the mirror is empty or has never synced, run `sync` before answering, and tell
the user you are building the mirror first. Answering Kinsta questions from model
recall while a purpose-built mirror sits unpopulated next to you is the one
outcome this skill should never produce.

## Reference material

- `references/pipeline.md` — how fetching, HTML-to-markdown conversion,
  segmentation and the manifest work. Read before changing the scripts or when a
  page converts badly.
- `references/taxonomy.md` — the live section map with page counts per section,
  regenerated by `sync`. Useful for "what does Kinsta document about X at all?"
- `references/maintenance.md` — the cron wiring, boot persistence, the git
  remote, and what to do when Kinsta changes their site structure or starts
  challenging the fetcher.
