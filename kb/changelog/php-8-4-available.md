---
url: "https://kinsta.com/changelog/php-8-4-available/"
title: "PHP 8.4 is now available for Kinsta\u2019s WordPress customers"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2025-02-26T18:23:47"
change_signal: "2025-02-26T18:23:47"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "6eb69d391981c77b536bd3d649767bed69edfc2ca7b7b5385b1644597b67fa52"
body_chars: 4297
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# PHP 8.4 is now available for Kinsta’s WordPress customers

**Product:** Changelog
**Source:** https://kinsta.com/changelog/php-8-4-available/
**Kinsta last updated:** 2025-02-26T18:23:47

## On this page

- [Before you switch to PHP 8.4](#before-you-switch-to-php-84)
- [How to switch to PHP 8.4 in MyKinsta](#how-to-switch-to-php-84-in-mykinsta)
- [Kinsta: Always looking ahead](#kinsta-always-looking-ahead)

---

[PHP 8.4](https://kinsta.com/blog/php-8-4/) was released in November 2024, and we’re happy to announce that this latest version of the server-side scripting language is available to customers on our [Managed Hosting](https://kinsta.com/wordpress-hosting/) platform.

[WordPress](https://kinsta.com/wordpress) site operators who want to adopt the very latest version of PHP can make the move within the [MyKinsta dashboard](https://kinsta.com/mykinsta/) or via the [Kinsta API](https://api-docs.kinsta.com/).

## Before you switch to PHP 8.4

PHP has some new features you might be eager to use in your projects, but there are a few things to consider before making the jump.

- This latest version of PHP is billed as having just beta support within [WordPress 6.7](https://kinsta.com/blog/wordpress-6-7/) (currently the most recent) and is officially unsupported in earlier WordPress releases. (Even [PHP 8.3](https://kinsta.com/blog/php-8-3/), released last year, is supported only in beta back through [WordPress 6.4](https://kinsta.com/blog/wordpress-6-4/), so that’s why our recommendation for most WordPress customers at this time is [PHP 8.2](https://kinsta.com/blog/php-8-2/).)
- Please make backups! As we recommend to anyone making major changes to their website, [create a site backup](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/#wordpress-backups) in case things go very wrong. (Fortunately, in most cases, the solution to a broken website after moving to a new PHP engine is simply reverting to the previous release, which is easily done in MyKinsta or through the Kinsta API.)
- Even if you’ve made backups and have determined that your site’s current theme and plugins support PHP 8.4, we still suggest that you make your first foray into the new release on a [staging environment](https://kinsta.com/docs/wordpress-hosting/staging-environment/). Repeat on your live site only when you’ve confirmed that staging performs without errors.

## How to switch to PHP 8.4 in MyKinsta

To upgrade a WordPress environment PHP 8.4, log in to MyKinsta and navigate to **WordPress Sites** > ***environment name*** > **Tools** , then click the **Change** button on the **PHP settings** card:

![Screenshot showing the WordPress site Tools page within the MyKinsta dashboard.](https://kinsta.com/wp-content/uploads/2024/12/wordpress-site-change-php-settings.png)

Starting a PHP update for a single WordPress environment.

Alternatively, you can perform a PHP update in bulk for multiple environments from the **WordPress Sites** page. In the example below, we’ve selected the checkboxes beside the names of multiple staging environments and are choosing **Change PHP settings** from the Actions dropdown menu:

![A screenshot showing bulk actions being performed on multiple WordPress environments within the MyKinsta dashboard.](https://kinsta.com/wp-content/uploads/2024/12/wordpress-site-change-php-settings-multiple.png)

Starting a PHP update for multiple WordPress environments.

Whichever path you choose, the next step is to choose the PHP version you want to adopt and click the **Change PHP settings** button:

![A screenshot showing the selection of PHP 8.4 during an update of PHP settings within the MyKinsta dashboard.](https://kinsta.com/wp-content/uploads/2024/12/wordpress-site-change-php-settings-1.png)

Selecting a PHP version update to the 8.4 release.

**Note:** When bulk-updating multiple WordPress environments, the version of PHP chosen above will be applied to all of them.

The switch to a different version of PHP takes a few minutes. The PHP engine will restart to load the new version, making your WordPress admin dashboard unavailable for a few seconds. You will receive a notification within MyKinsta when the process is complete.

## Kinsta: Always looking ahead

We’re excited to make PHP 8.4 available on our servers for our hosting customers. Keep an eye out for our annual [PHP benchmarking](https://kinsta.com/blog/php-benchmarks/), where we’ll be testing how this new release performs behind a number of [PHP-powered content management systems](https://kinsta.com/blog/php-frameworks/), including WordPress.

Looking for premium hosting on PHP 8.4? Find a [Managed Hosting package](https://kinsta.com/pricing/) here that’s right for you.
