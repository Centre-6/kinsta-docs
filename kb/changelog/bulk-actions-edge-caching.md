---
url: "https://kinsta.com/changelog/bulk-actions-edge-caching/"
title: "Configure Edge Caching for multiple WordPress sites with Bulk Actions"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Configure Edge Caching for multiple WordPress sites with Bulk Actions"]
kinsta_last_updated: "2026-05-14T18:59:50+00:00"
sitemap_lastmod: "2026-05-14T18:59:50+00:00"
fetched_at: "2026-10-07T22:37:32Z"
sha256: "ab07984cc7b2de3ca078ea71a1c578ffd7681c1243436680d470aa2dd3cca6d8"
body_chars: 3385
extracted_with: "main article"
status: "live"
---

# Configure Edge Caching for multiple WordPress sites with Bulk Actions

**Section:** Changelog > Configure Edge Caching for multiple WordPress sites with Bulk Actions
**Product:** Changelog
**Source:** https://kinsta.com/changelog/bulk-actions-edge-caching/
**Kinsta last updated:** 2026-05-14T18:59:50+00:00

---

Updated
:   May 14, 2026

![Illustration showing the Actions menu in MyKinsyta with the words: Bulk actions — Edge Caching](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-bulk-actions-change-edge-caching-1024x536.png)

Kinsta has added to the list of tasks that can be accomplished with the [Bulk Actions](https://kinsta.com/changelog/bulk-actions/) feature available to [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/) customers. With just a few clicks, you can now enable or disable [Edge Caching](https://kinsta.com/edge-caching/) across multiple website environments.

Edge Caching can be [enabled and disabled](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/) for individual sites within the [MyKinsta dashboard](https://kinsta.com/mykinsta/). The latest addition to Bulk Actions adds this functionality to the cross-site updaters that already include:

- Clearing site caches
- Updating plugins
- Updating themes
- [Changing PHP versions](https://kinsta.com/changelog/change-php-bulk-action/)
- Exporting site information to CSV
- Changing MyKinsta’s site labels

## How to bulk-update Edge Caching status in MyKinsta

To enable or disable Edge Caching for multiple website environments, select **WordPress Sites** in MyKinsta’s main menu and then use the checkboxes on the left-hand side of the sites list to choose the environments you want to update.

When environments have been selected, an **Actions** button and a count of the number of selected environments will appear above the sites list:

![Screenshot showing multiple environments selected in the WordPress Sites list.](https://kinsta.com/wp-content/uploads/2024/05/bulk-action-change-edge-caching-menu.png)

The **Actions** menu is available when environments are selected.

Select **Change edge** **caching** from the **Actions** menu. You will be asked whether you want to **Enable** or **Disable** edge caching on the targeted environments:

![Screenshot of the dialog used to select which Edge Caching bulk action to perform: Enable or Disable.](https://kinsta.com/wp-content/uploads/2024/05/bulk-action-change-edge-caching-dialog.png)

Choosing whether to **Enable** or **Disable** Edge Caching as a bulk action.

Click the **Change edge caching** button to launch the Bulk Action.

Remember that Edge Caching is available only for live sites and environments with the [Premium Staging Environment add-on](https://kinsta.com/add-ons/). The **Change edge caching** Bulk Action will not affect free staging environments.

## Perform bulk actions with the Kinsta API

You can create your own bulk-action tools for WordPress sites using the [Kinsta API](https://api-docs.kinsta.com/). The API provides a gateway to managing WordPress sites, as well as [Web Applications](https://sevalla.com/application-hosting/), [Managed Databases](https://sevalla.com/database-hosting/), and [Static Sites](https://sevalla.com/static-site-hosting/) hosted by Kinsta.

Currently, you can’t enable or disable Edge Caching via the API, but you can use it to clear content from edge caches and the [Kinsta CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/), just as you can with the Bulk Actions feature in MyKinsta.

Here’s an example of an application that uses the Kinsta API for [multi-site plugin updates](https://kinsta.com/blog/bulk-update-plugins-wordpress/).
