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
├── manifest.json         # per-URL state: path, etag, last_modified, sha256, lastmod, fetched_at
├── SYNC-LOG.md           # append-only history of what each sync changed
├── docs/<section>/<slug>.md
├── api/
│   ├── openapi.json      # machine-readable spec, when Kinsta publishes one
│   └── <section>/<slug>.md
├── changelog/<slug>.md
└── blog/<slug>.md
```

Every page file carries YAML frontmatter with its source URL, breadcrumb section
path, Kinsta's own `lastmod`, the content hash, and when we last fetched it.
That frontmatter is what lets you cite precisely and judge staleness per page
instead of per-mirror.

The whole skill is one git repo (private, `Centre-6/kinsta-docs`), and `kb/` is
tracked inside it. That is deliberate: `git log -p kb/docs/...` shows you the
exact wording Kinsta changed and when we noticed. When a client asks "did this
always work this way?", the diff is the answer.

## First: establish which Kinsta product you are talking about

Kinsta sells several products that are documented separately, behave differently,
and reuse the same words for different things. Getting this wrong is the single
most damaging mistake available here, because the answer is coherent, confident,
well-sourced, and about the wrong product. The user asks about their WordPress
site and gets Database Hosting semantics. Worse, the answer is often *almost*
right, so it survives a skim and fails in production.

The product lines, each with its own docs tree:

| Product | What it hosts | Section in `kb/docs/` |
|---|---|---|
| **Managed WordPress Hosting** | WordPress sites. The original product, and what most people mean by "my Kinsta site" | `wordpress-hosting/` |
| **Application Hosting** | Arbitrary apps from a git repo, built via Dockerfile, Nixpacks or buildpacks | `application-hosting/` |
| **Database Hosting** | Managed standalone databases (Postgres, MySQL, MariaDB, Redis, Valkey) | `database-hosting/` |
| **Static Site Hosting** | Static output from a repo build step. Free tier, deliberately minimal | `static-site-hosting/` |
| **DevKinsta** | A local development tool on your own machine, not hosting at all | `devkinsta/` |
| **MyKinsta** | The control panel shared across all of the above (account, billing, users, DNS) | `mykinsta/` |

`kb/docs/` mirrors Kinsta's own taxonomy, and every page file carries a
`product:` field in its frontmatter. Use it. `search` takes `--product` for
exactly this reason:

```bash
python3 <skill>/scripts/kinsta_kb.py search "custom domain" --product wordpress-hosting
```

### The words that mean different things per product

These terms appear in all or most of the trees with genuinely different
mechanics behind them. A grep hit on one of these is **not** an answer until you
know which product's page you landed on:

`backups` · `cache` / `caching` · `CDN` · `custom domain` · `deployment` ·
`environments` · `staging` · `redirects` · `logs` · `metrics` · `SSH` ·
`SFTP` · `database access` · `cron` / `scheduled tasks` · `restore` ·
`rollback` · `build` · `processes` · `edge` · `plans and limits`

Treat a hit on one of these as "I found the right topic, now which product?"
rather than as the answer.

### How to establish the product, cheapest first

1. **The user said it.** "my WordPress site", "my Node app on Kinsta", "the
   Postgres instance" settles it. Take them at their word on what they have.
2. **The surrounding work says it.** A repo with `wp-config.php` and a `wp-content/`
   tree is WordPress Hosting. A `Dockerfile` or `Procfile` with a web process is
   Application Hosting. A build command producing `dist/` with no server is
   probably Static Site Hosting. A connection string and no application code is
   Database Hosting.
3. **Ask the Kinsta API**, if credentials for the account are available. This is
   the only method that is evidence rather than inference — it reports what the
   account actually contains. Check for a key before assuming there isn't one:
   ```bash
   ls ~/.claude/secrets/ | grep -i kinsta
   ```
   If a key exists, the `/sites`, `/applications` and `/databases` endpoints
   (see `kb/api/`) answer the question definitively. If no key exists, say so
   rather than guessing — "I can't see the account, so which product is this?"
   is a one-line question that prevents a whole wrong answer.
4. **Ask.** If 1–3 leave it open, ask. One short question costs the user a few
   seconds. A confidently wrong product-specific procedure can cost them a site.

### When the question spans products

Some things genuinely differ across products and the comparison is the answer
("can I get staging on static hosting?"). When that is the case, answer per
product and label each line, rather than blending them into one paragraph:

> - **WordPress Hosting:** <answer> — <url>
> - **Static Site Hosting:** <answer> — <url>

And when a product simply does not document a feature, say that about *that
product* specifically. "Static Site Hosting's docs don't cover X" is a different
and much safer claim than "Kinsta doesn't support X."

## The one rule: revalidate the pages you are about to rely on

Before you state anything as current Kinsta behavior — in an answer, a config
file, a script, a client email, a Trello comment — revalidate the specific pages
backing that claim:

```bash
python3 <skill>/scripts/kinsta_kb.py check --url <url> [--url <url> ...]
```

This does a conditional GET using the stored ETag / Last-Modified, so a fresh
page costs one cheap 304 and no download. It prints one verdict per URL:

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
Two to five pages is normal and takes a couple of seconds.

## Finding the right pages

Work outside-in, cheapest first:

1. **`kb/INDEX.md`** — the section tree with page titles and one-line summaries.
   Read this to orient. It is built to be skimmed, so you can usually name the
   two or three pages that matter without searching at all.
2. **Full-text search** when you need a specific term, flag, header, or limit:
   ```bash
   python3 <skill>/scripts/kinsta_kb.py search "edge cache purge" --limit 10
   ```
   This is ripgrep underneath with the frontmatter decoded, so hits come back as
   `path | section | title | matching line`. Add `--tier docs` to exclude blog
   noise, or `--section application-hosting` to scope it.
3. **Read the page file.** Read the whole page, not just the matched line. Kinsta
   docs routinely qualify a procedure three paragraphs later ("this does not
   apply to Static Site Hosting", "available on Business plans and above"), and a
   grep hit on the happy path with the caveat left unread is how you ship a
   confidently wrong answer.

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

> Kinsta's edge caching holds HTML for 1 hour by default and purges on post
> update — https://kinsta.com/docs/<path>/ (revalidated just now; Kinsta's own
> last-modified on that page is 2026-08-14).

If a page came back `CHANGED` during your check, lead with that. A doc that moved
under you is usually more interesting to the user than the answer itself.

If you are relying on a page you could not revalidate, date it plainly:
"from our mirror, fetched 2026-09-28; I couldn't reach Kinsta to confirm."

## Keeping the mirror current

```bash
python3 <skill>/scripts/kinsta_kb.py sync             # incremental, sitemap-driven
python3 <skill>/scripts/kinsta_kb.py sync --tier docs # just the docs tier
python3 <skill>/scripts/kinsta_kb.py sync --full      # ignore lastmod, revalidate everything
python3 <skill>/scripts/kinsta_kb.py status           # per-tier counts and age
```

`sync` is cheap by design. It reads Kinsta's sitemaps, compares each URL's
`lastmod` and our stored ETag against `manifest.json`, and only downloads pages
that are new, newer, or whose conditional GET says they changed. A no-op sync on
an unchanged corpus is a few sitemap fetches.

It also handles the cases a naive crawler gets wrong:

- **New URLs** are fetched, segmented, and added to `INDEX.md`.
- **Removed URLs** are tombstoned, not deleted — the file stays with
  `status: removed` in its frontmatter and the date we noticed. A page Kinsta
  pulled is evidence, and you will want it when someone asks why a documented
  procedure vanished.
- **Moved content** shows up as a removal plus an addition. `sync` reports both
  together so you can see the pair.
- Every run appends to `SYNC-LOG.md` and commits to the `kb/` git repo, so the
  history of Kinsta's documentation as we observed it is reconstructable.

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
