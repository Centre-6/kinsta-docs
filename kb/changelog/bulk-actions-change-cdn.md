---
url: "https://kinsta.com/changelog/bulk-actions-change-cdn/"
title: "Change CDN status added to MyKinsta\u2019s Bulk Actions"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-05-14T18:59:21"
change_signal: "2026-05-14T18:59:21"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "fe6b6de483417a5e60a39629e82222cb061d920a13b27e65bb86299a57f26c03"
body_chars: 3857
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Change CDN status added to MyKinsta’s Bulk Actions

**Product:** Changelog
**Source:** https://kinsta.com/changelog/bulk-actions-change-cdn/
**Kinsta last updated:** 2026-05-14T18:59:21

---

We’ve added the ability to enable and disable Kinsta CDN support to the [Bulk Actions](https://kinsta.com/changelog/bulk-actions/) available to [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/) customers. With just a few clicks, you can simultaneously change Kinsta CDN status across multiple website environments .

The CDN can be [enabled and disabled](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/) for individual sites within the [MyKinsta dashboard](https://kinsta.com/mykinsta/). This Bulk Actions functionality adds to a list of multi-site updaters that already includes:

- Clearing site caches
- Updating plugins
- Updating themes
- [Change Edge Caching](https://kinsta.com/changelog/bulk-actions-edge-caching/)
- [Changing PHP versions](https://kinsta.com/changelog/change-php-bulk-action/)
- Exporting site information to CSV
- Changing MyKinsta’s site labels

## How to bulk-update CDN status in MyKinsta

To change Kinsta CDN status for multiple website environments:

1. Select **WordPress Sites** in MyKinsta’s main menu and use the checkboxes on the left-hand side of the sites list to choose the environments you want to update.
2. When one or more environments have been selected, an **Actions** button and a count of the selected environments appear above the sites list:

![Screenshot showing the Bulk Actions menu in the MyKinsta dashboard with WordPress site environments selected.](https://kinsta.com/wp-content/uploads/2024/06/mykinsta-bulk-action-change-cdn-menu.png)

The **Actions** menu is available when environments are selected.

3. Select **Change CDN** from the **Actions** menu. A prompt asks whether you want to **Enable** or **Disable** CDN on the selected environments:

![Screenshow showing the Change CDN Bulk Actions dialog.](https://kinsta.com/wp-content/uploads/2024/06/mykinsta-bulk-action-change-cdn-dialog.png)

Choosing whether to **Enable** or **Disable** CDN as a Bulk Action.

4. Click the **Change CDN** button to launch the Bulk Action.

The Kinsta CDN is available only for live sites and environments with the [Premium Staging Environment add-on](https://kinsta.com/add-ons/). The **Change CDN** Bulk Action does not affect a free, basic staging environment. For example, in the screenshot below, MyKinsta is reporting a failed attempt to change the CDN status for a basic staging environment:

![Screenshot showing success and failure notices after performing Bulk Actions.](https://kinsta.com/wp-content/uploads/2024/06/mykinsta-bulk-action-change-cdn-report.png)

Status reports for two environments that support the CDN and one that doesn’t.

## Create your own bulk actions using the Kinsta API

Did you know you can use the [Kinsta API](https://api-docs.kinsta.com/) to create your own bulk-action tools for WordPress sites? The API provides a gateway to managing WordPress sites, [Web Applications](https://sevalla.com/application-hosting/), [Managed Databases](https://sevalla.com/database-hosting/), and [Static Sites](https://sevalla.com/static-site-hosting/) hosted by Kinsta.

Currently, you can’t enable or disable the CDN via the API, but you can use it to [clear the CDN cache](https://api-docs.kinsta.com/api-reference/wordpress-cdn/clear-site-cdn-cache), just as you can with Bulk Actions in MyKinsta.

We’ve got some tips on [optimizing your WordPress site environment](https://kinsta.com/blog/optimize-wordpress-site-environment/) using the Kinsta API.

At Kinsta, we’re dedicated to engineering new ways to simplify [WordPress maintenance](https://kinsta.com/blog/wordpress-maintenance/). If you’re looking for a [blazingly fast](https://kinsta.com/blog/migrate-to-kinsta/) and [secure hosting provider](https://kinsta.com/wordpress-hosting/security/), check out [Kinsta’s plans](https://kinsta.com/pricing/) to find the one that best suits you.
