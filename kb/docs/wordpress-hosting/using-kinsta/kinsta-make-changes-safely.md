---
url: "https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-make-changes-safely/"
title: "Make Changes Safely"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "using-kinsta"
section: ["WordPress Hosting", "Using Kinsta"]
kinsta_last_updated: "2026-10-12T16:32:57"
change_signal: "2026-10-12T16:32:57"
fetched_at: "2026-11-11T13:03:01Z"
sha256: "903cace475c558af0d45f5f037430ddd57601ac5de7c3b42f6a92e2fccbf01e2"
body_chars: 5227
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Make Changes Safely

**Section:** WordPress Hosting > Using Kinsta
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-make-changes-safely/
**Kinsta last updated:** 2026-10-12T16:32:57

## On this page

- [The safe-change workflow](#the-safe-change-workflow)
- [Use your free staging environment](#use-your-free-staging-environment)
- [Push changes to live](#push-changes-to-live)
- [Back up before any risky change](#back-up-before-any-risky-change)
- [Update URLs across your site with Search and Replace](#update-urls-across-your-site-with-search-and-replace)
- [Start new sites from an existing one](#start-new-sites-from-an-existing-one)
- [Show visitors a maintenance message during updates](#show-visitors-a-maintenance-message-during-updates)
- [In your routine](#in-your-routine)

---

The safest way to change your site is to test the change on a copy first. Every Kinsta site comes with a free staging environment, so you never need to experiment on the site your visitors are using.

## The safe-change workflow

1. Create or refresh your staging environment from live.
2. Make and test your change on staging.
3. Take a manual backup of your live site.
4. Push the change from staging to live.
5. Check your live site. If anything’s wrong, restore the backup.

## Use your free staging environment

**Why it matters:** A plugin update, theme change, or new PHP version can break a page in ways you won’t see until a visitor does. Staging is a separate, private copy of your site where you can find those problems first.

**When to use it:** Before updating WordPress core, major plugins, or your theme; before changing PHP version; and for any design or code work.

**How to start:** In MyKinsta, select your site, click the environment name (for example, Live), select **Create new environment**, and clone your live site into a standard environment. For step-by-step instructions, see [Create a WordPress Standard or Premium staging environment](https://kinsta.com/docs/wordpress-hosting/staging-environment/#create-a-wordpress-standard-or-premium-staging-environment). If you need more resources, or several environments for different projects, see the premium staging add-on under [Add-Ons](https://kinsta.com/docs/wordpress-hosting/wordpress-add-ons/#premium-staging-environments-add-on).

## Push changes to live

**Why it matters:** Once a change works on staging, pushing it to live copies it across in one step, without redoing the work by hand.

**How to start:** See [Push Environments](https://kinsta.com/docs/wordpress-hosting/wordpress-push-environments/). You can push the whole site, or use a selective push to send only the files and folders or database tables you choose. When pushing database tables, you can run an automatic search and replace so links point to the right domain. You can also push from live to staging, which is a quick way to bring new posts and uploads into your test copy. Kinsta automatically backs up the environment you’re pushing to before the push starts.

**Watch out for:** Pushing the whole database replaces the live database. Any orders, comments, form entries, or new users added to your live site since staging was created will be lost. On a store or membership site, push only files, or select specific database tables and leave out tables such as WooCommerce’s order tables. On a multisite network, a full database push affects every subsite.

## Back up before any risky change

**Why it matters:** Daily backups may be up to a day old. A manual backup taken just before a change means you can roll back without losing anything.

**How to start:** Create a manual backup under [Backups](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#create-a-manual-wordpress-backup). You can also restore a backup to staging, which is useful for checking an older version without touching live.

## Update URLs across your site with Search and Replace

**Why it matters:** Changing your domain or moving to HTTPS can leave old URLs stored throughout your database.

**How to start:** Use the [Search and Replace tool](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/mykinsta-search-replace-tool/) in MyKinsta. Kinsta takes a backup automatically before making the replacement, and can clear your site cache afterwards. Try the replacement on staging first if you’re unsure what it will match.

## Start new sites from an existing one

**Why it matters:** If you build several similar sites, setting up the same theme and plugins each time takes hours.

**How to start:** [Clone a site](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/clone-wordpress-site/) to create a new site from an existing one, including its theme, plugins, and settings.

## Show visitors a maintenance message during updates

**Why it matters:** While plugins or themes are updating, visitors could see a half-updated page. Maintenance mode shows them a short message instead.

**How to start:** You can turn on maintenance mode when updating plugins or themes in MyKinsta. See [WordPress Maintenance Mode](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-maintenance-mode/).

**Watch out for:** If an update fails, the site can get stuck showing the message. To fix it, delete the .maintenance file from your site’s root folder using the [File Manager](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-file-manager/), [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/), or [SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/).

## In your routine

Use the safe-change workflow for anything bigger than a minor plugin update: New major WordPress versions, theme updates, PHP upgrades, and new plugins. A monthly check that a backup restores to staging means you’ll know your safety net works before you need it. See [Your Maintenance Routine](https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-your-maintenance-routine/).
