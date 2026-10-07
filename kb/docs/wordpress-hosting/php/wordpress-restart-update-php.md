---
url: "https://kinsta.com/docs/wordpress-hosting/php/wordpress-restart-update-php/"
title: "PHP - Restart and Update PHP"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "php"
section: []
kinsta_last_updated: "May 28, 2026"
sitemap_lastmod: "2026-05-28T07:57:50+00:00"
fetched_at: "2026-10-07T22:40:19Z"
sha256: "bca25f96ffba5c14438404c743c977ce13006d17edd90db756b2b81b2662b9f8"
body_chars: 3377
extracted_with: "main article"
status: "live"
---

# PHP - Restart and Update PHP

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/php/wordpress-restart-update-php/
**Kinsta last updated:** May 28, 2026

## On this page

- [Restart PHP](#restart-php)
  - [How to restart PHP manually](#how-to-restart-php-manually)
- [Update PHP](#update-php)

---

## Restart PHP

If PHP goes down, our system automatically logs this for our Systems Administration (sysadmin) team to check out. However, you can manually restart PHP for any of your websites individually with a simple click of a button from MyKinsta.

### How to restart PHP manually

To restart PHP on your WordPress site, follow the steps below.

1. Log in to [MyKinsta](https://my.kinsta.com), go to **Sites**, and select the site on which you’d like to restart PHP.
2. Go to **Tools**, then click **Restart PHP** in the **Restart PHP section**.

![Restart PHP in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/06/wordpress-tools-restart-php.png)

Restart PHP in MyKinsta.

Please note that restarting PHP will take about 5-10 seconds. You will receive a notification at the bottom of the screen when it is completed.

Note: You will also need to [delete your site’s cache](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/) to see the changes.

## Update PHP

We’ve made [updating your site’s PHP version](https://kinsta.com/blog/php-versions/) as easy as possible in MyKinsta.

To update the PHP version for a single site, go to**Sites** > ***sitename*** > **Tools**. Under **PHP settings**, click **Change**.

To update the PHP version for multiple sites, including staging sites, at once, go to **Sites**, select the checkboxes next to the sites you want, click **Actions**, then **PHP settings**, and choose **Change PHP settings**.

![Change your PHP settings in the site's Tools menu.](https://kinsta.com/wp-content/uploads/2025/06/wordpress-tools-change-php-settings.png)

Change your PHP settings in the site’s Tools menu.

Choose a **PHP version**, and choose whether to enable or disable **Automatic PHP Updates**. When enabled, Kinsta automatically upgrades your site to the latest supported PHP version once your current version reaches end of life. To turn on **Automatic PHP Updates** without changing your PHP version, leave the PHP version field as is.

![Choose your PHP version and enable or disable automatic updates.](https://kinsta.com/wp-content/uploads/2024/10/wordpress-change-php-settings-1-1024x479.png)

Choose your PHP version and enable or disable automatic updates.

If you select a Long-Term Support (LTS) PHP version, automatic updates are disabled. The latest officially supported PHP version is 8.1; LTS versions only receive security patches, which may result in reduced performance compared to an officially supported version. To enhance your website’s performance, we recommend upgrading to the latest officially supported PHP version.

![Select a long-term support (LTS) PHP version.](https://kinsta.com/wp-content/uploads/2024/10/wordpress-change-php-settings-lts-1-1024x652.png)

Select a long-term support (LTS) PHP version.

At the end of the update, your [PHP engine](https://kinsta.com/blog/php-benchmarks/) will be restarted, and the backend (WordPress dashboard) of your site may be down for a couple of seconds. The front of the site will remain up, and visitors will not experience any downtime.

While the update process is running, you can navigate to other parts of MyKinsta, but some actions, like cache management, will be unavailable until the PHP engine has restarted.

Once the update is complete (usually within 3 minutes or less), you’ll receive a notification in MyKinsta that it’s finished.
