---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-maintenance-mode/"
title: "Plugins and Themes - WordPress Maintenance Mode"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-plugins-themes"
section: []
kinsta_last_updated: "March 12, 2025"
sitemap_lastmod: "2025-03-12T10:57:54+00:00"
fetched_at: "2026-10-07T22:37:12Z"
sha256: "10fc3990ce01e9691834d20106289163ff2b63a4a279a86a3af2eb8d0767c48b"
body_chars: 2190
extracted_with: "main article"
status: "live"
---

# Plugins and Themes - WordPress Maintenance Mode

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-maintenance-mode/
**Kinsta last updated:** March 12, 2025

## On this page

- [Disable WordPress maintenance mode](#disable-wordpress-maintenance-mode)
  - [Clear the WordPress maintenance page](#clear-the-wordpress-maintenance-page)
  - [Prevent WordPress from getting stuck in maintenance mode](#prevent-wordpress-from-getting-stuck-in-maintenance-mode)

---

WordPress Maintenance Mode is a temporary state that displays a maintenance message to visitors while updates or changes are being applied to your site. In MyKinsta, you can enable Maintenance Mode during plugin or theme updates.

When Maintenance Mode is enabled, WordPress creates a `.maintenance` file in your site’s root directory. Your visitors see a simple “Briefly unavailable for scheduled maintenance” message instead of your site. Once the updates are complete, the `.maintenance` file is removed, and the site becomes accessible again.

## Disable WordPress maintenance mode

When updates are complete, the maintenance message should be removed. However, there are occasions when an issue may arise and cause the maintenance page to get stuck, which requires some manual intervention to fix.

### Clear the WordPress maintenance page

To clear this maintenance message, you must connect to your site with [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/) or [SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) and delete the `.maintenance` file in your site’s **public** directory (aka root directory or document root).

Once you’re connected to your site and viewing the **public** directory, you’ll see a list of your site’s files and subdirectories. Look for and delete the file named `.maintenance`.

### Prevent WordPress from getting stuck in maintenance mode

A few scenarios may cause the maintenance page to get stuck and not clear automatically. To prevent this, here are a few quick tips:

1. Make sure plugins/themes are compatible with your version of WordPress before updating.
2. Update plugins often so you don’t have to run a large number of updates at once. In MyKinsta, you can enable [Kinsta Automatic Updates](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-plugins-themes-automatic-updates/), so you don’t need to worry about manually updating your plugins and themes.
3. Avoid updating a large number of plugins or themes at the same time. Depending on the plugins and the extent of the update needed, run 2-3 at a time, or even 1 at a time, to avoid potential conflicts or connection issues.
