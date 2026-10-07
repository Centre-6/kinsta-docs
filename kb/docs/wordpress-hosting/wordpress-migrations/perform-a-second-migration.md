---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/perform-a-second-migration/"
title: "Migrations - Updating a Migrated Site Before Going Live"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-migrations"
section: []
kinsta_last_updated: "April 20, 2026"
sitemap_lastmod: "2026-04-20T09:55:58+00:00"
fetched_at: "2026-10-07T22:40:00Z"
sha256: "e68a2591451442d8095308ea760277910767b1f06dad9b7b3a75aeef92d0e4f4"
body_chars: 2840
extracted_with: "main article"
status: "live"
---

# Migrations - Updating a Migrated Site Before Going Live

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/perform-a-second-migration/
**Kinsta last updated:** April 20, 2026

---

In some cases, you may have us migrate a site, but not be able to go live in a timely manner. When the site is ready to go live, its content may need to be updated to reflect changes made while it’s been live and hosted elsewhere. If this happens, you have the following options:

## Migrate the changes manually

The first option is to manually migrate the changes yourself. This can be done in at least three different ways:

- Use the content export and import features built into WordPress to export content from your prior host and import it here at Kinsta. Then, install any necessary new plugins and themes and apply updates or settings to themes, plugins, and the WordPress core.
- There are many backup and [migration plugins](https://kinsta.com/blog/wordpress-migration-plugins/) that can be used to migrate a WordPress site. While [we don’t allow backup plugins](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-banned-incompatible-plugins/) for ongoing backups on our platform, if there’s a backup or migration plugin you’re familiar with and comfortable with, you’re welcome to use it to migrate a fresh copy of your site.
- Copy changed files to our servers using [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/) or [SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/). Then, use a fresh dump of the live site [database](https://kinsta.com/docs/wordpress-hosting/database-management/create-wordpress-database-backup/) and import it using either [phpMyAdmin or WP-CLI.](https://kinsta.com/docs/wordpress-hosting/database-management/restore-import-mysql-database/) This process is described in [Manual Migration](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/wordpress-manual-migration/).

Prior to beginning this process, it’s important to note any changes that were made to the site here at Kinsta after the initial migration. If you modified the WordPress configuration, changed files, or added or removed plugins or themes here at Kinsta after the initial migration, those changes may be overwritten when you migrate the site a second time, depending on the process you use.

## Ask Kinsta for a second migration

If you’re unable to handle the update on your own, the Company Owner or Company Administrator can [contact our team within MyKinsta](https://kinsta.com/docs/support/contact-support/) for assistance.

If the original migration took place within the last week, we can copy over the updated files and import a fresh copy of the database. Note: The live site may need to go into [maintenance mode](https://kinsta.com/blog/wordpress-maintenance-mode/) during this process.

If it has been more than a week since the original migration, it’s probable that we will want to migrate the entire site as if it were a brand-new migration.

##
