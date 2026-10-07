---
url: "https://kinsta.com/changelog/selective-push-from-live/"
title: "Selective Push now supports deployments from live to staging"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Selective Push now supports deployments from live to staging"]
kinsta_last_updated: "2024-07-05T20:21:04+00:00"
sitemap_lastmod: "2024-07-05T18:21:04+00:00"
fetched_at: "2026-10-07T22:36:52Z"
sha256: "165a3e0fd926e81ea9c8fdd7917d6274b5619c6e775b93ddbb8c599c1376d2f8"
body_chars: 3591
extracted_with: "main article"
status: "live"
---

# Selective Push now supports deployments from live to staging

**Section:** Changelog > Selective Push now supports deployments from live to staging
**Product:** Changelog
**Source:** https://kinsta.com/changelog/selective-push-from-live/
**Kinsta last updated:** 2024-07-05T20:21:04+00:00

---

Published
:   July 5, 2024

![An illustration representing the deployment of assets from a live site and the words: Selective Push Environment.](https://kinsta.com/wp-content/uploads/2024/07/mykinsta-wordpress-selective-push-from-live-1024x536.png)

We’ve enhanced [Selective Push](https://kinsta.com/changelog/selective-push-environment/) functionality in the MyKinsta dashboard to support the deployment of files, folders, and database tables from live WordPress websites to staging environments.

Previously, [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/) customers could [create a staging environment](https://kinsta.com/docs/wordpress-hosting/staging-environment/#create-wordpress-standard-or-premium-staging-environment) by cloning a live site, but the recently released [Selective Push](https://kinsta.com/docs/wordpress-hosting/staging-environment/#push-staging-to-live-with-selective-push) initially supported deployments only from staging to a live site and between staging environments. Being able to push code, media, and database tables from a live site to what might be a development environment offers new flexibility for website builders.

When content is generated directly on a live site — by your publishing team or website visitors — a staged site used for development can quickly slip out of sync. Being able to move [media library](https://kinsta.com/blog/wordpress-media-library/) uploads and selected [database tables](https://kinsta.com/blog/wordpress-database/) back to staging is a good example of using Selective Push to equip a development environment with the latest content.

## How to use Selective Push from a live environment

Pushing assets from your live website begins by making that environment active in [MyKinsta](https://kinsta.com/mykinsta/) (if it’s not already):

1. Select **Info** in the main menu to display the **Site Information** page.
2. Click the current environment name in the top menu bar.
3. Select the **Live** environment in the **Jump to or search…** dialog.

![Screenshot showing the selection of website environments in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/07/selective-push-from-live-environment.png)

Selecting a **Live** environment in the **Jump to or search** dialog.

With your live site selected, the **Push Environment** button appears near the top of the page. Click the button to select a target staging environment:

![Screenshot showing the menu for selecting the target of a Selective Push.](https://kinsta.com/wp-content/uploads/2024/07/selective-push-from-live-target.png)

Choosing a staging environment to receive the live site’s assets.

Now, you can select which files, folders, and database tables you want to push from the live site. Below, our target staging environment is named “Development”:

![Screenshot of the dialog used to select which assets will be deployed during a Selective Push from Live.](https://kinsta.com/wp-content/uploads/2024/07/selective-push-from-live-database.png)

Choosing assets to push from a live site to a staging environment.

Remember: We make an automatic backup of the target environment before beginning the push actions.

## WordPress development made easier

We’re dedicated to delivering tools that make [WordPress maintenance](https://kinsta.com/blog/wordpress-maintenance/) simpler. So, if you’re looking for [fast](https://kinsta.com/blog/migrate-to-kinsta/) and [secure](https://kinsta.com/wordpress-hosting/security/) WordPress hosting, check out [Kinsta’s plans](https://kinsta.com/pricing/) to find the one that fits you best.
