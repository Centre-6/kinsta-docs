# kinsta-docs

A local mirror of Kinsta's published documentation, built as an Agent Skill for Claude.

It covers the documentation at kinsta.com/docs, the Kinsta API reference and its OpenAPI spec, the Kinsta changelog, and Kinsta blog articles. Roughly 660 pages, segmented one file per page, each carrying the source URL, Kinsta's own last-updated timestamp, and a hash of the body.

## Why it exists

Having a copy of a vendor's docs is easy. The hard part is that a cached copy goes wrong quietly, and an answer drawn from a three-week-old mirror reads exactly as confident as a correct one. Kinsta changes PHP version availability, plan limits, cache behavior, API endpoints and UI labels without announcement.

So this skill treats freshness as part of the answer. Before relying on a page, it re-checks that page against Kinsta and reports what it found: current, changed, or unreachable. If it cannot reach Kinsta, it says so and dates the answer rather than presenting a stale page as current.

## Installing

Most people want the first option. You do not need Claude Code, a terminal, or a developer account.

### Claude app (claude.ai on web, desktop or mobile)

**1. Turn on code execution.** The skill cannot run without it, and this is a separate switch from the skill itself. Settings > Capabilities for an individual account. On Team or Enterprise an owner does it at Organization settings > Plugins & skills, where both code execution and Skills have to be on.

**2. Download the packaged skill:**

https://github.com/Centre-6/kinsta-docs/releases/latest/download/kinsta-docs.zip

**3. Upload it.** Customize > Skills > + > Create skill > Upload a skill, and choose the file you just downloaded. On newer builds the menu is Customize > Plugins.

That file is already packaged the way Claude expects, so there is nothing to unzip or rename.

> **Do not use the green Code > Download ZIP button on this page.** GitHub names the folder inside it `kinsta-docs-main`, which no longer matches the skill's name, and the upload is rejected. Use the release link above.

If your build offers it, you can skip the download entirely: Customize > Plugins > Add > Add marketplace, then paste this repository's URL.

### Claude Code

Claude Code runs on your own machine, so the skill keeps full network access and the freshness check works as designed. It is available as a terminal command and as a desktop app for Mac and Windows: https://code.claude.com/docs/en/desktop

As a plugin:

```
claude plugin marketplace add Centre-6/kinsta-docs
claude plugin install kinsta-docs@centre6-plugins
```

As a plain skill, clone the repository to `~/.claude/skills/kinsta-docs` for all your projects, or to `.claude/skills/kinsta-docs` inside one repository. The directory name has to stay `kinsta-docs`, because it must match the `name` in `SKILL.md`.

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
