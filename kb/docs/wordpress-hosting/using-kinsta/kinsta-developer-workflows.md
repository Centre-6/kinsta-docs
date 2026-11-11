---
url: "https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-developer-workflows/"
title: "Developer Workflows"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "using-kinsta"
section: ["WordPress Hosting", "Using Kinsta"]
kinsta_last_updated: "2026-10-12T16:38:28"
change_signal: "2026-10-12T16:38:28"
fetched_at: "2026-11-11T13:03:01Z"
sha256: "a9f8c3ee8c3c3a7cbb87ab3defa312ba59e5be232b9e084180aa971bac5e787b"
body_chars: 3471
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Developer Workflows

**Section:** WordPress Hosting > Using Kinsta
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-developer-workflows/
**Kinsta last updated:** 2026-10-12T16:38:28

## On this page

- [Connect with SFTP and SSH](#connect-with-sftp-and-ssh)
- [Manage WordPress from the command line](#manage-wordpress-from-the-command-line)
- [Deploy with Git and CI/CD](#deploy-with-git-and-cicd)
- [Automate with the Kinsta API](#automate-with-the-kinsta-api)
- [Other tools worth knowing](#other-tools-worth-knowing)
- [Watch out for bot protection](#watch-out-for-bot-protection)

---

Every Kinsta plan includes SSH, SFTP, WP-CLI, and Git, so developers can work the way they’re used to. Here’s which tools fit which jobs, from editing a single file to fully automated deployments.

## Connect with SFTP and SSH

**Why it matters:** SFTP gives you secure access to your site’s files. SSH gives you a command line on the server, where you can run Git, Composer, and WP-CLI.

**How to start:** Find your connection details in MyKinsta; see [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/) and [SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/). For a quick edit without connecting, use the [File Manager](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-file-manager/) in MyKinsta.

## Manage WordPress from the command line

**Why it matters:** WP-CLI handles tasks like updating plugins, managing users, and running search and replace far faster than the WordPress dashboard, and it can be scripted.

**How to start:** Connect over [SSH](https://kinsta.com/blog/vocabulary/ssh/) and run wp commands; see [WP-CLI](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-wp-cli/).

## Deploy with Git and CI/CD

**Why it matters:** Deploying from version control gives you a history of every change and a repeatable process. It also makes rolling back a bad release straightforward.

**How to start:** See [Git](https://kinsta.com/docs/wordpress-hosting/site-management/git/), then set up automated deployments with [GitHub Actions](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-github-cicd/), [GitLab CI/CD](https://kinsta.com/docs/wordpress-hosting/site-management/gitlab-ci-cd/), or [Bitbucket Pipelines](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-bitbucket-pipelines/). Deploy to staging first, then push to live; see [Make Changes Safely](https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-make-changes-safely/).

## Automate with the Kinsta API

**Why it matters:** If you manage many sites, repeating the same steps in MyKinsta takes time. The API lets you script tasks such as creating sites, clearing caches, or running backups.

**How to start:** See [Kinsta API](https://kinsta.com/docs/kinsta-api/) and the [API reference](https://api-docs.kinsta.com/pages/introduction).

## Other tools worth knowing

- **[Database management](https://kinsta.com/docs/wordpress-hosting/database-management/):** Run queries and edit data directly in MyKinsta.
- **[Cron jobs](https://kinsta.com/docs/wordpress-hosting/site-management/cron-jobs/):** Schedule server-level tasks.
- **[PHP constants and PHP modules](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-constants/):** Check what’s available and configurable on the server.
- **[New Relic](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/custom-new-relic-tracking/) and [Blackfire](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/wordpress-blackfire-monitoring/):** Use your own monitoring tools alongside [Kinsta’s APM](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/).

## Watch out for bot protection

If a site’s bot protection is set above the default level, deployment scripts, API integrations, and self-hosted monitors may be blocked. Add an exception for your tools’ IP addresses or user agents; see [Protect Your Site](https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-protect-your-site/).
