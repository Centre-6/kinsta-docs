# Maintaining the Kinsta docs mirror

Read this when the scheduled sync stops firing, when `sync` starts failing, or
when Kinsta changes their site structure.

## Contents

- [Where the mirror lives](#where-the-mirror-lives)
- [The daily sync](#the-daily-sync)
- [Making the schedule survive a reboot](#making-the-schedule-survive-a-reboot)
- [The git repo](#the-git-repo)
- [When Kinsta changes their site](#when-kinsta-changes-their-site)
- [When the fetcher starts getting blocked](#when-the-fetcher-starts-getting-blocked)
- [When the mirror gets too big](#when-the-mirror-gets-too-big)

## Where the mirror lives

The mirror is `kb/` inside the skill directory. Everything the scripts read and
write is resolved relative to that directory at runtime — there are no absolute
paths baked into the code — so the skill works wherever you cloned it:
`~/.claude/skills/kinsta-docs/` for a user-wide install, `.claude/skills/kinsta-docs/`
inside a single project, or a plugin directory if you installed it as a plugin.

Two consequences worth knowing:

- **Run the scripts by their real path, not by a guess.** `python3 scripts/kinsta_kb.py status`
  from the skill directory always works. The cron installer derives the path from
  its own location for the same reason.
- **If your home directory or skill directory is on ephemeral storage** — a RAM
  disk, a container layer, a scratch volume — the mirror is as ephemeral as the
  directory holding it. On-disk is not a backup. The git remote is.

## The daily sync

`sync` is designed to run unattended once a day. `scripts/install-cron.sh`
installs it into your own user crontab:

```bash
bash scripts/install-cron.sh          # install or refresh
bash scripts/install-cron.sh --check  # report state, change nothing
bash scripts/install-cron.sh --remove # uninstall
```

The installed line runs at 04:17 local time, off the hour on purpose so it does
not pile up with every other job that fires at :00. The installer writes the
absolute path of *your* checkout and *your* `python3`, resolved when you run it.

`sync` is idempotent and safe to run concurrently with a manual sync — it takes a
lock file at `kb/.sync.lock` and the second caller exits rather than interleaving
writes into `manifest.json`. If a crashed run leaves a stale lock, `sync` clears
locks older than 2 hours on its own; `--force-unlock` is there for the case where
you know the holder is dead and do not want to wait.

A quiet filesystem is not proof the sync ran. Check it explicitly:

```bash
python3 scripts/kinsta_kb.py status        # prints last successful sync per tier
tail -40 kb/cron.log
crontab -l | grep kinsta
```

If `status` shows a last-sync date well in the past, the schedule is broken and
the pre-answer `check` is carrying the whole freshness story alone. That still
works, but it only validates pages you happen to look at — new pages and
deletions go unnoticed. Fix the schedule rather than relying on the per-answer
check indefinitely.

**No cron available?** `launchd` on macOS, a systemd timer on Linux, or any
scheduler that can run one command will do. The command is the only thing that
matters:

```
<your python3> <skill dir>/scripts/kinsta_kb.py sync >> <skill dir>/kb/cron.log 2>&1
```

Run `bash scripts/install-cron.sh --check` to see the exact line for your
install, then adapt it. Note that macOS `cron` and `launchd` jobs may need Full
Disk Access granted to the launching process before they can write into your home
directory.

## Making the schedule survive a reboot

On most machines a user crontab is stored on persistent disk and survives a
reboot on its own, and there is nothing further to do. Check it once rather than
assuming:

```bash
bash scripts/install-cron.sh          # install
# reboot, then:
crontab -l | grep kinsta              # still there?
python3 scripts/kinsta_kb.py status   # still syncing?
```

Some systems do not keep it: a crontab held on a RAM disk or a tmpfs, a container
that is rebuilt from an image, or an immutable/appliance OS that restores system
state at boot. If you are on one of those, `install-cron.sh` is idempotent and
safe to call from whatever startup mechanism that platform gives you, which is
exactly what it is written for.

Wire that in when you add the schedule, not later. A sync that works today and
silently disappears on the next reboot is worse than no sync at all, because
`status` keeps reporting a once-fresh mirror while it drifts.

## The git repo

The **whole skill** is one git repo — `SKILL.md`, `scripts/`, `references/` and
`kb/` together. One repo rather than a nested one, so a single `git log` shows
both how the tooling evolved and what Kinsta changed, in the order it happened.

`sync` commits automatically. Mirror commits are prefixed `kb:` and name what
moved (`kb: 3 changed, 1 added, 1 removed`), so they are easy to filter out when
you only want the tooling history:

```bash
git log --oneline --invert-grep --grep='^kb:'   # tooling changes only
git log --oneline -- kb/docs                    # Kinsta's doc changes only
```

Push it somewhere. The whole value of the history is that it survives, and a
local checkout is not a backup:

```bash
git remote add origin <your remote>
git push -u origin main
```

Because the repo root is the live skill directory, a `git checkout` of an older
commit changes the skill Claude is running. That is occasionally what you want
(bisecting a bad sync) but do it deliberately, and come back to the branch tip.

The mirror contains only Kinsta's own published documentation — no credentials,
no account data, nothing from MyKinsta behind a login. Keep it that way. Notes
about how a particular site is configured belong with that site's own project,
not in a shared mirror of a vendor's public docs. The same goes for API keys:
the skill neither stores one nor looks for one.

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
- Check whether robots.txt changed. If Kinsta disallowed the paths this mirror
  covers, that settles it — stop syncing those paths rather than working around
  the block.
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
`/docs/` paths now 301 to `docs.sevalla.com`. Two reasons not to add it: it is a
different vendor, and `docs.sevalla.com/robots.txt` declares
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
which is fast for ripgrep and unremarkable on any disk. The blog is the only
tier with real growth potential, and it is already bounded by the 12-month
publish window rather than growing without limit.

If it does become a problem, in order of preference:

1. Tighten the window: `sync --blog-months 6`.
2. `sync --tier docs,api,changelog` on the schedule, blog on demand. Docs
   freshness is what answers actually depend on.
3. If full-text search ever gets slow (it should not below a few hundred MB),
   add a SQLite FTS index *alongside* the markdown rather than replacing it. The
   markdown files are the artifact; an index is a cache and must stay
   rebuildable from them with one command.

Measure before acting on a hunch:

```bash
du -sh kb/docs kb/api kb/changelog kb/blog
python3 scripts/kinsta_kb.py status
```
