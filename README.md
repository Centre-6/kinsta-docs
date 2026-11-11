# kinsta-docs

A local mirror of Kinsta's published documentation, built as an Agent Skill for Claude.

It covers the documentation at kinsta.com/docs, the Kinsta API reference and its OpenAPI spec, the Kinsta changelog, and Kinsta blog articles. Roughly 660 pages, segmented one file per page, each carrying the source URL, Kinsta's own last-updated timestamp, and a hash of the body.

## Why it exists

Having a copy of a vendor's docs is easy. The hard part is that a cached copy goes wrong quietly, and an answer drawn from a three-week-old mirror reads exactly as confident as a correct one. Kinsta changes PHP version availability, plan limits, cache behavior, API endpoints and UI labels without announcement.

So this skill treats freshness as part of the answer. Before relying on a page, it re-checks that page against Kinsta and reports what it found: current, changed, or unreachable. If it cannot reach Kinsta, it says so and dates the answer rather than presenting a stale page as current.

## Installing

**Claude Code, as a plugin:**

```
claude plugin marketplace add Centre-6/kinsta-docs
claude plugin install kinsta-docs@centre6-plugins
```

**Claude Code, as a plain skill:** clone the repository to `~/.claude/skills/kinsta-docs` for all your projects, or to `.claude/skills/kinsta-docs` inside one repository. The directory name has to stay `kinsta-docs`, because it must match the `name` in `SKILL.md`.

**claude.ai, from this repository:** Customize > Plugins > Add > Add marketplace, then give it this repository's URL. On older builds the menu is Customize > Skills. Code execution has to be enabled: Settings > Capabilities for an individual account, or Organization settings > Plugins & skills for Team and Enterprise.

**claude.ai, from a ZIP:** Customize > Skills > + > Create skill > Upload a skill. Build the archive so the skill folder is its top level, because Claude looks for `kinsta-docs/SKILL.md` inside it:

```
zip -r kinsta-docs.zip kinsta-docs/
unzip -l kinsta-docs.zip
```

Do not use GitHub's "Download ZIP" button for this. It names the top folder `kinsta-docs-main`, which no longer matches the skill name, and the upload will be rejected. Unzip it, rename the folder to `kinsta-docs`, and re-zip from the parent directory.

## Dependencies

The mirror itself is plain markdown and needs nothing. The sync and search scripts need three Python packages:

```
python3 -m pip install requests beautifulsoup4 markdownify
```

PyYAML is optional, used only when Kinsta serves its OpenAPI spec as YAML rather than JSON. Ripgrep is used for search when it is present on your PATH; without it the search falls back to a pure-Python scan that returns the same results more slowly. If your Python is managed by the operating system, install into a virtualenv instead.

## What it needs to work fully

The revalidation step needs outbound network access to `kinsta.com` and `api-docs.kinsta.com`. Claude Code has that by default. The claude.ai sandbox does not: its default tier reaches package registries only, and Kinsta is not on that list. On a default claude.ai account the skill still works as a documentation corpus, but it cannot confirm a page is current, so read the sync date before citing anything.

## Keeping it current

```
python3 scripts/kinsta_kb.py sync       # incremental, all four tiers
python3 scripts/kinsta_kb.py status     # when did it last succeed
python3 scripts/kinsta_kb.py check URL  # revalidate specific pages
```

`scripts/install-cron.sh` wires a daily sync. `references/pipeline.md` explains how ingestion works and is worth reading before changing `scripts/kinsta_kb.py`.

## Before you install this skill

An Agent Skill is instructions and code that Claude loads and can run with your own user privileges. Anthropic does not review or verify third-party skills, and Claude Code's permission rules do not cover code a plugin runs on its own. Read `SKILL.md` and everything under `scripts/` before you install, and treat it the way you would treat any other software you are about to run on your machine.

This skill contains no credentials. Its scripts make outbound requests to `kinsta.com` and `api-docs.kinsta.com` only, to fetch documentation. If you want to pin what you reviewed, install from a tagged ref rather than the default branch.

## About the documentation in this repository

The contents of `kb/` are Kinsta's documentation, reproduced from their published pages. That content belongs to Kinsta and is not ours to license. Every mirrored page records the URL it came from. The tooling in `scripts/` and the written material in `references/` are Centre 6's.
