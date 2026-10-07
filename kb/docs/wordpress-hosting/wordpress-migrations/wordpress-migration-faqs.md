---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/wordpress-migration-faqs/"
title: "Migrations - Migration FAQs"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-migrations"
section: []
kinsta_last_updated: "April 20, 2026"
sitemap_lastmod: "2026-04-20T09:41:51+00:00"
fetched_at: "2026-10-07T22:39:59Z"
sha256: "d9765027898d02fd2670959da6b59caffd8801447c7a0f2ec59d02975908ebbe"
body_chars: 8467
extracted_with: "main article"
status: "live"
---

# Migrations - Migration FAQs

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/wordpress-migration-faqs/
**Kinsta last updated:** April 20, 2026

## On this page

- [How long will it take to migrate my website to Kinsta?](#how-long-will-it-take-to-migrate-my-website-to-kinsta)
- [What is maintenance mode?](#what-is-maintenance-mode)
- [How long will my eCommerce site be in maintenance mode?](#how-long-will-my-ecommerce-site-be-in-maintenance-mode)
- [Does my website need to be on WordPress to migrate to Kinsta?](#does-my-website-need-to-be-on-wordpress-to-migrate-to-kinsta)
- [Can I migrate my website from a backup?](#can-i-migrate-my-website-from-a-backup)
- [How do I migrate an ecommerce site that changes continuously?](#how-do-i-migrate-an-ecommerce-site-that-changes-continuously)
- [Can I request a second migration for the same site?](#can-i-request-a-second-migration-for-the-same-site)
- [I’ve entered incorrect credentials in the migration request, do I need to submit it again?](#ive-entered-incorrect-credentials-in-the-migration-request-do-i-need-to-submit-it-again)
- [Can I migrate my site using a .wpress backup file?](#can-i-migrate-my-site-using-a-wpress-backup-file)
- [Can you install node/node.js/npm on my site?](#can-you-install-nodenodejsnpm-on-my-site)
- [Can I migrate multiple individual WordPress sites into a multisite or a single site from a multisite?](#can-i-migrate-multiple-individual-wordpress-sites-into-a-multisite-or-a-single-site-from-a-multisite)
- [Can I migrate my site to a staging environment?](#can-i-migrate-my-site-to-a-staging-environment)
- [Can you migrate my site to a dedicated server?](#can-you-migrate-my-site-to-a-dedicated-server)
- [What happens if an infection is discovered during migration?](#what-happens-if-an-infection-is-discovered-during-migration)
- [Can I migrate files and directories outside of the WordPress site?](#can-i-migrate-files-and-directories-outside-of-the-wordpress-site)
- [Does Bedrock/Trellis need to be removed or reconfigured when migrating to Kinsta?](#does-bedrocktrellis-need-to-be-removed-or-reconfigured-when-migrating-to-kinsta)
- [When are expedited migrations performed?](#when-are-expedited-migrations-performed)
- [Can I migrate a specific blog post or page from an old site to Kinsta?](#can-i-migrate-a-specific-blog-post-or-page-from-an-old-site-to-kinsta)
- [How do I export content from WordPress to import it again?](#how-do-i-export-content-from-wordpress-to-import-it-again)

---

Below we’ve compiled all the **most common migration questions** in one place. If you have any other questions we’ve perhaps missed, make sure to feedback using the options at the bottom of the article, or you can always [open a chat with our Support team](https://kinsta.com/docs/support/contact-support/).

## How long will it take to migrate my website to Kinsta?

We will complete your migrations as soon as possible, which could take up to 2 business days. If we believe processing your migrations may take longer, we will let you know at the time we receive the request. If you’re concerned about downtime or need to get your site live on Kinsta quickly, we offer [expedited migrations](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrating-to-kinsta/#expedited-migrations) for just $49 per site; we aim to complete expedited migrations within 8 hours, between 9 AM and 11 PM, Monday to Friday (UTC). 

## What is maintenance mode?

Placing a site in maintenance mode means that the site content cannot be updated. This is usually done by installing [a maintenance plugin from the WordPress.org repository](https://wordpress.org/plugins/maintenance/). However, if you have a preferred method for placing the site into [maintenance mode](https://kinsta.com/blog/wordpress-maintenance-mode/), that can also be accommodated.

While the site is in maintenance mode, a maintenance message is displayed, orders cannot be placed, users cannot register or edit their profiles, and new content cannot be published on the site.

## How long will my eCommerce site be in maintenance mode?

It depends on the following variables:

- The size of your site.
- The speed of data transfer between our infrastructure and the prior host.
- The time-to-live (TTL) values associated with your DNS records.
- How quickly you can begin reviewing your site after the migration is complete.
- How much time you need to review your site thoroughly following the migration.
- Any unforeseen complications that arise during the migration process.

As a general rule of thumb, most migrations take between 1 and 3 hours. After that, most clients need between 1 and 3 hours to review the site. DNS propagation usually takes about 1 hour but may take much longer in some cases if extended TTL values are associated with your current DNS records.

You can use this information to get a sense of how long your site will need to be in maintenance mode, but please note that the factors mentioned above do mean that we are unable to accurately predict how long a specific site will need to be in maintenance mode.

## Does my website need to be on WordPress to migrate to Kinsta?

Yes, you must have a WordPress website to migrate it to a [Managed WordPress plan at Kinsta](https://kinsta.com/wordpress-hosting/). If you are trying to migrate a non-WordPress site, please contact our partner, [WordHerd](https://wordherd.io/), and follow up with our [customer support](https://kinsta.com/kinsta-support/).

## Can I migrate my website from a backup?

Yes, Kinsta customers can migrate their websites by sharing a link to a backup file using cloud storage services such as Drive, Dropbox, etc., or uploading their backup file to an existing Kinsta website, whether it’s created with Duplicator, ManageWP, or cPanel.

## How do I migrate an ecommerce site that changes continuously?

Sites that change continuously (ecommerce sites, membership sites, etc.) often require placing them into maintenance mode and careful scheduling to avoid data loss.

## Can I request a second migration for the same site?

Yes. If you have migrated your site already and there have been changes on the original site since the migration, there are a few different options available. Find out more in [Perform a second migration](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/perform-a-second-migration/).

## I’ve entered incorrect credentials in the migration request, do I need to submit it again?

No. We can obtain the correct information from you when our Migrations team contacts you to start the migration.

## Can I migrate my site using a .wpress backup file?

No. This is a WP-All-In-One backup file which is a plugin we do not support. You must provide the backup in a supported format, such as .zip, .gz, or .tar.gz.

## Can you install node/node.js/npm on my site?

If you’re on a Single 1.25M or above plan or a WP 60 or above plan, you can request node/node.js/npm on our server for your site. You must add this information to the special instructions when submitting the migration request.

## Can I migrate multiple individual WordPress sites into a multisite or a single site from a multisite?

No. We only support direct like-for-like migrations; this can be a single site or a multisite, but we cannot import or export individual multisite data. More information about migrating multisite subsites can be found in [Recommended WordPress Multisite Plugins (Network Management, Migrations, and Backups)](https://kinsta.com/blog/wordpress-multisite-plugins/).

## Can I migrate my site to a staging environment?

Yes. If you add this information to special instructions when submitting the migration request, we can migrate your site to a staging environment. If you don’t have a migration slot available and want to migrate to a staging site, [contact our Support team](https://kinsta.com/docs/support/contact-support/).

## Can you migrate my site to a dedicated server?

Yes. If you haven’t already requested a [dedicated server](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/dedicated-server/), this will need to be created first and is not part of the migration request. A dedicated server takes time to provision and configure, so it’s crucial that you [contact our Account Management team](https://kinsta.com/docs/support/contact-support/) to start the process as early as possible. Once you have approved the quote and paid for the first month of service, our team will need up to 3 business days to configure the dedicated server.

If the dedicated server is already set up, we can migrate your site directly to it.

## What happens if an infection is discovered during migration?

A deep scan of all site files is a standard step in our migration process. If we determine that your site is infected during a migration, we will pause the migration and report the issue to you. At that time, you will be provided with two options:

1. Proceed with the migration and have Kinsta remove the infection.
2. Cancel the migration, work with a third party to repair the hacked site in the prior hosting environment or repair it yourself, and then reschedule the migration.

Find out more about Kinsta’s approach to [Malware Removal](https://kinsta.com/docs/service-information/malware-removal/).

## Can I migrate files and directories outside of the WordPress site?

If the files and directories are within the same WordPress directory (e.g., public_html), they will typically be included in the migration by default.

If the files or folders are outside the WordPress directory and need to be migrated, you must specify this within the special instructions when submitting the migration request.

## Does Bedrock/Trellis need to be removed or reconfigured when migrating to Kinsta?

No, we can migrate Bedrock/Trellis and keep their setup as-is.

## When are expedited migrations performed?

[Expedited migrations](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrating-to-kinsta/#expedited-migrations) are performed between 9 AM and 11 PM (UTC), Monday to Friday. They are not available on the weekend.

## Can I migrate a specific blog post or page from an old site to Kinsta?

No. We cannot migrate specific sections or content; we can only migrate the full site like-for-like.

## How do I export content from WordPress to import it again?

If you want to perform your own migration, you can follow our guide on [How to Do a WordPress Migration on Your Own (With No Downtime)](https://kinsta.com/blog/migrate-wordpress-site/). These steps include information about how to export and import your WordPress content in XML format.

Migrating a large or complex site by yourself could cause data loss or other issues if you’re not familiar with the process. We generally recommend that you let our expert Migrations team take care of migrating your site for you. We’ll even help you check your site prior to going live.
