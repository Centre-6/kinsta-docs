# Maintaining the Kinsta docs mirror

Read this when the cron stops firing, when `sync` starts failing, or when Kinsta
changes their site structure.

## Contents

- [Where the mirror physically lives](#where-the-mirror-physically-lives)
- [The daily sync cron](#the-daily-sync-cron)
- [Boot persistence](#boot-persistence)
- [The git repo and its remote](#the-git-repo-and-its-remote)
- [When Kinsta changes their site](#when-kinsta-changes-their-site)
- [When the fetcher starts getting blocked](#when-the-fetcher-starts-getting-blocked)
- [When the mirror gets too big](#when-the-mirror-gets-too-big)

## Where the mirror physically lives

The skill lives at `~/.claude/skills/kinsta-docs/`. On FloydTower `~/.claude` is
a symlink to `/mnt/user/appdata/home-persist/.claude/`, so despite living under
`/home/tim` the mirror is on the 66 TB array, not on the root RAM disk. This
matters: anything genuinely under `/home/tim` is wiped on reboot. Verify the
symlink is intact before concluding the mirror was lost:

```bash
ls -ld ~/.claude          # expect: -> /mnt/user/appdata/home-persist/.claude/
```

The array has **no parity**. On-disk is not a backup. The git remote below is.

## The daily sync cron

Scheduled work on this box defaults to a Cloudflare Worker, and that default is
right for most things. This job is a deliberate exception: the mirror is a
directory of files on the array and a git repo on local disk, so the job has to
run where the filesystem is. That is the stated reason it is local rather than a
Worker — not an oversight.

The cron runs as `tim`:

```
17 4 * * * /usr/bin/python3 /home/tim/.claude/skills/kinsta-docs/scripts/kinsta_kb.py sync >> /home/tim/.claude/skills/kinsta-docs/kb/cron.log 2>&1
```

04:17 local, off the hour on purpose so it does not pile up with every other
job that fires at :00.

`sync` is idempotent and safe to run concurrently with a manual sync — it takes a
lock file at `kb/.sync.lock` and the second caller exits rather than interleaving
writes into `manifest.json`. If a crashed run leaves a stale lock, `sync` clears
locks older than 2 hours on its own; `--force-unlock` is there for the case where
you know the holder is dead and do not want to wait.

A quiet filesystem is not proof the cron ran. Check it explicitly:

```bash
python3 scripts/kinsta_kb.py status        # prints last successful sync per tier
tail -40 kb/cron.log
crontab -l | grep kinsta
```

If `status` shows a last-sync date well in the past, the cron is broken and the
pre-answer `check` is carrying the whole freshness story alone. That still works,
but it only validates pages you happen to look at — new pages and deletions go
unnoticed. Fix the cron rather than relying on the per-answer check indefinitely.

## Boot persistence

Crontabs on this box live on the root RAM disk and **do not survive a reboot**
unless they are reinstalled by the boot chain (`/boot/config/go` →
`restore-persistence.sh` → per-project installers). `scripts/install-cron.sh`
exists for this: it is idempotent, installs the line above into the `tim`
crontab, and is safe to call from the boot chain.

Wire it when you add the cron, not later. A cron that works today and silently
disappears on the next reboot is worse than no cron, because `status` will keep
reporting a once-fresh mirror that is drifting.

```bash
bash scripts/install-cron.sh          # idempotent; run after any reboot
grep -n kinsta /boot/config/*.sh      # confirm the boot chain calls it
```

## The git repo and its remote

The **whole skill** is one git repo — `SKILL.md`, `scripts/`, `references/` and
`kb/` together — with a private remote at `Centre-6/kinsta-docs`. One repo rather
than a nested one, so a single `git log` shows both how the tooling evolved and
what Kinsta changed, in the order it happened.

`sync` commits automatically. Mirror commits are prefixed `kb:` and name what
moved (`kb: 3 changed, 1 added, 1 removed`), so they are easy to filter out when
you only want the tooling history:

```bash
git log --oneline --invert-grep --grep='^kb:'   # tooling changes only
git log --oneline -- kb/docs                    # Kinsta's doc changes only
```

Push it. The array has no parity, so on-disk is not a backup and the whole value
of the history is that it survives. Per the standing rule, **private**:

```bash
cd ~/.claude/skills/kinsta-docs
git init && git add -A && git commit -m "feat: kinsta docs mirror skill"
gh repo create Centre-6/kinsta-docs --private --source=. --push
```

Commit identity: Centre 6 internal tooling, so set the local override rather than
inheriting the personal global default:

```bash
git config --local user.name "Tim Phelps"
git config --local user.email "tim@centre6.com"
```

Credentials come from the git credential helper, which is already wired
globally. Do not put a token in the remote URL — the remote stays clean at
`https://github.com/Centre-6/kinsta-docs.git`.

Because the repo root is the live skill directory, a `git checkout` of an older
commit changes the skill Claude is running. That is occasionally what you want
(bisecting a bad sync) but do it deliberately, and come back to the branch tip.

The mirror contains only Kinsta's own published documentation — no credentials,
no client data, nothing from MyKinsta behind a login. Keep it that way. If you
ever want to annotate a page with "this is how we configured it for <client>",
that annotation belongs on the client's board or in the client's project, not in
a shared mirror of a vendor's public docs.

## When Kinsta changes their site

The fetcher pins a CSS selector for the article body and a selector for
breadcrumbs. Those are the brittle parts, and a site redesign breaks them in a
way that is easy to miss: the fetch still returns HTTP 200, the conversion still
produces a markdown file, and the file is near-empty or full of navigation
chrome.

`sync` guards against this with a sanity floor. If a page converts to fewer than
200 characters of body text, or if more than 20% of the pages in a run fail the
floor, it aborts the run, writes nothing, and reports the selector as suspect.
That ratio check is the important half — a single short page is plausible, but
a fifth of the corpus going short at once is a redesign, not content.

To repair:

1. Fetch one known-good page by hand and look at the HTML yourself. Do not infer
   the new selector from the old one.
2. Update the selector in `scripts/kinsta_kb.py` (see `references/pipeline.md`
   for where).
3. Run `sync --full --dry-run` first. It reports per-page body lengths without
   writing, so you can confirm the new selector extracts real content across
   several sections before it touches the mirror.
4. Then `sync --full`. The git diff will be large and mostly formatting; that is
   expected after a redesign and is exactly why the repo exists.

## When the fetcher starts getting blocked

Symptoms: `UNVERIFIED` across the board, HTTP 403, HTML containing a challenge
page, or a sudden run of identical short bodies.

Do not escalate to anything that pretends not to be a bot. Kinsta's docs are
public and their robots.txt is the agreement; keep to it. The honest fixes:

- Slow down. The fetcher sleeps between requests by default; raise it with
  `--delay`. A sync that takes an hour and succeeds beats a fast one that gets
  the IP throttled.
- Check whether robots.txt changed. If Kinsta disallowed the paths we mirror,
  that settles it — stop syncing those paths and tell Tim, rather than working
  around it.
- Prefer the sitemap + conditional-GET path, which is what `sync` already does.
  It is a small fraction of the requests a full recrawl would make.

Report the block as the error you actually observed. "Kinsta returned 403 on 12
of 14 requests starting 2026-10-07" is actionable; "the docs seem unavailable"
is not.

## Scope, and the drift to watch for

Four tiers, measured October 7, 2026:

| Tier | Source | Pages | Notes |
|---|---|---|---|
| `docs` | `kinsta.com/sitemap_index.xml`, `/docs/` | 190 | WordPress hosting, DevKinsta, billing, account, support |
| `api` | `api-docs.kinsta.com/sitemap.xml` | 120 | Plus `kb/api/openapi.json` — OpenAPI 3.1.0, 84 endpoints |
| `changelog` | same sitemap, `/changelog/` | 122 | What shipped when |
| `blog` | `kinsta.com/wp-json/wp/v2/posts` | ~140 | Last 12 months by **publish** date |

**Sevalla is out of scope by decision.** Kinsta spun Application Hosting,
Database Hosting and Static Site Hosting into a separate company; those
`/docs/` paths now 301 to `docs.sevalla.com`. Two reasons not to add it without
asking Tim: it is a different vendor, and `docs.sevalla.com/robots.txt` declares
`Content-Signal: ai-input=no`. Kinsta's and api-docs.kinsta.com's both declare
`ai-input=yes`, which is the basis for mirroring them.

Re-read `robots.txt` on both hosts if you are about to widen scope. A
`Content-Signal` can change, and it is the kind of thing nobody notices because
nothing breaks when you ignore it.

**The drift that would hurt most** is Kinsta moving or renaming a top-level
`/docs/` area. `tree` and `references/taxonomy.md` are how you would see it:
`PRODUCT_LABELS` in the script carries the October 2026 page counts as inline
comments precisely so a comparison is cheap. Wildly different numbers mean a
reorganization, and `INDEX.md` plus the skill's own product table need updating
along with the labels.

## When the mirror gets too big

Current footprint is small — roughly 8 MB of markdown across all four tiers,
which is nothing on the array and fast for ripgrep. The blog is the only tier
with real growth potential, and it is already bounded by the 12-month publish
window rather than growing without limit.

If it does become a problem, in order of preference:

1. Tighten the window: `sync --blog-months 6`.
2. `sync --tier docs,api,changelog` on the cron, blog on demand. Docs freshness
   is what answers actually depend on.
3. If full-text search ever gets slow (it should not below a few hundred MB),
   add a SQLite FTS index *alongside* the markdown rather than replacing it. The
   markdown files are the artifact; an index is a cache and must stay
   rebuildable from them with one command.

Measure before acting on a hunch:

```bash
du -sh kb/docs kb/api kb/changelog kb/blog
python3 scripts/kinsta_kb.py status
```
