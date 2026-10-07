---
url: "https://kinsta.com/changelog/bulk-actions/"
title: "Update multiple WordPress sites with MyKinsta's Bulk Actions"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Update multiple WordPress sites with MyKinsta\u2019s Bulk Actions"]
kinsta_last_updated: "2026-05-14T19:00:13+00:00"
sitemap_lastmod: "2026-05-14T19:00:13+00:00"
fetched_at: "2026-10-07T22:37:32Z"
sha256: "9b7a89f280de9e72a2db15fa9ab3ec1db0f9c18d5fbfe3c3c339d0a36b85f5b9"
body_chars: 6638
extracted_with: "main article"
status: "live"
---

# Update multiple WordPress sites with MyKinsta's Bulk Actions

**Section:** Changelog > Update multiple WordPress sites with MyKinsta’s Bulk Actions
**Product:** Changelog
**Source:** https://kinsta.com/changelog/bulk-actions/
**Kinsta last updated:** 2026-05-14T19:00:13+00:00

## On this page

- [How to perform Bulk Actions in MyKinsta](#how-to-perform-bulk-actions-in-mykinsta)
  - [Clear cache](#clear-cache)
  - [Update plugins](#update-plugins)
  - [Update themes](#update-themes)
  - [Export to CSV](#export-to-csv)
  - [Change labels](#change-labels)
- [The Kinsta API: Another way to perform bulk updates](#the-kinsta-api-another-way-to-perform-bulk-updates)

---

Updated
:   May 14, 2026

![Illustration reflecting the bulk actions interface with the words, 'Updating multiple websites.'](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-wordpress-bulk-actions-1024x536.png)

Kinsta has introduced a new Bulk Actions feature in [MyKinsta](https://kinsta.com/mykinsta/) that makes it easier for [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/) customers to perform common tasks across multiple website environments simultaneously.

Targets for Bulk Actions can be live and staged environments of the same site or any combination of those environments across multiple web properties.

In the initial rollout of this time-saving feature, supported actions are:

- Clearing site caches
- Updating plugins
- Updating themes
- Exporting site information to CSV
- Changing MyKinsta’s site labels

Users can now perform these tasks without logging in to [WordPress admin dashboards](https://kinsta.com/blog/wordpress-admin/) or digging into the MyKinsta dashboard any deeper than the WordPress sites list.

## How to perform Bulk Actions in MyKinsta

To initiate a Bulk Action, select **WordPress Sites** in MyKinsta’s main menu and then use the checkboxes on the left-hand side of the sites list to select target environments.

Selecting or deselecting the checkbox beside a site name will select or deselect all its environments. Or, you can select and deselect environments individually:

![Screenshot showing the selection of environments for Bulk Actions in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-bulk-actions-select-environments.png)

Selecting environments for Bulk Actions.

When environments are selected, an **Actions** button will appear above the sites list, along with an indicator of the number of selected environments.

Click **Actions** to choose a task from the drop-down menu:

![Screenshot showing the selection of a task in MyKinsta's Bulk Actions menu.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-bulk-actions-select-action.png)

Choosing a task from the Actions menu.

Let’s take a look at what each action does.

### Clear cache

The **Clear cache** Bulk Action allows you to flush the [server](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/#clear-cache-in-mykinsta), [CDN](https://kinsta.com/blog/wordpress-cdn/), and [Edge Cache](https://kinsta.com/edge-caching/). When you select that action, you’ll be asked which cache(s) you want to clear:

![Screenshot of the Clear Cache Bulk Actions dialog in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-bulk-actions-clear-cache.png)

Choosing caches for the **Clear cache** action.

### Update plugins

[Updating plugins](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-manage-plugins-themes/) is one of the most common tasks for WordPress site owners. The **Update plugins** Bulk Action reveals a list of plugins across your select environments that have updates available.

You’ll see the names of the plugins available for update and a count of the environments you’ve selected that have the plugin installed:

![Screenshot showing the Update Plugins Bulk Action dialog in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-bulk-actions-update-plugins.png)

Choosing plugins to update across one or more environments.

### Update themes

The **Update themes** Bulk Action works much like **Update plugins**. Only [themes](https://kinsta.com/blog/what-is-a-wordpress-theme/) with available updates will appear in the following dialog:

![Screenshot showing the Update Themes Bulk Action dialog in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-bulk-actions-update-themes.png)

Selecting themes to update as a Bulk Action

### Export to CSV

The **Export to CSV** Bulk Action generates a file containing information about the selected environments and formatted for viewing in a spreadsheet. Selecting the action will launch the save-file dialog on your computer:

![Screenshot showing the save-file dialog for a Bulk Action CSV export.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-bulk-actions-cvs-export.png)

Saving a CSV file containing details for bulk-selected environments.

The file created with the **Export to CSV** action will include the following information for each selected environment:

- Site name
- Environment name (like “Live” or “Staging”)
- Identifier (an internal reference name for your site)
- Staging type (“Standard” or “Premium”)
- Location (your data center)
- Visits
- Bandwidth
- Disk Usage
- Force HTTPS (status)
- Domains
- Primary domain
- IP (for public-facing web access)
- Load balancer (the IP used for SSH/SFTP access)
- Path (to website root on the server)
- Port (for SSH/SFTP access)
- Current External IP address (for outbound connections)
- PHP version
- Date/time created

### Change labels

The **Change labels** Bulk Action allows you to [edit labels](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-labels/) across multiple sites.

The labeling tool in MyKinsta helps organize and filter your WordPress sites using unique tags.

Labels are applied at the site level, even if you have selected just one of multiple site environments before beginning the Bulk Action:

![Screenshot showing the Change Labels Bulk Action dialog in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-bulk-actions-change-labels.png)

Adding and removing site labels as a Bulk Action.

## The Kinsta API: Another way to perform bulk updates

We hope you find Bulk Actions within MyKinsta useful. Remember that you can create your own bulk-action tools for WordPress sites using the [Kinsta API](https://api-docs.kinsta.com/). The API provides the raw materials for managing WordPress sites, [Web Applications](https://sevalla.com/application-hosting/), [Managed Databases](https://sevalla.com/database-hosting/), and [Static Sites](https://sevalla.com/static-site-hosting/) at Kinsta.

Calls made through the Kinsta API for actions like clearing caches and updating themes and plugins typically target one WordPress environment at a time. However, your custom application can discover its own [list of sites](https://api-docs.kinsta.com/api-reference/wordpress-sites/get-list-of-company-sites) and [site environments](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-site-environments) to launch bulk actions.

Check out our example application bringing it all together for [multi-site plugin updates](https://kinsta.com/blog/bulk-update-plugins-wordpress/) using the Kinsta API.
