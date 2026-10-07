---
url: "https://kinsta.com/changelog/php-8-5-available/"
title: "PHP 8.5 is now available to Kinsta customers"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "PHP 8.5 is now available to Kinsta customers"]
kinsta_last_updated: "2026-03-19T16:27:54+00:00"
sitemap_lastmod: "2026-03-19T16:27:54+00:00"
fetched_at: "2026-10-07T22:35:57Z"
sha256: "636a0d967c02e52c88ade737fd2ee48f6532be7476a755b0b001ccd6bb6d13f5"
body_chars: 5659
extracted_with: "main article"
status: "live"
---

# PHP 8.5 is now available to Kinsta customers

**Section:** Changelog > PHP 8.5 is now available to Kinsta customers
**Product:** Changelog
**Source:** https://kinsta.com/changelog/php-8-5-available/
**Kinsta last updated:** 2026-03-19T16:27:54+00:00

## On this page

- [Think twice (or more) before adopting a new PHP release](#think-twice-or-more-before-adopting-a-new-php-release)
  - [PHP and WordPress release matchups](#php-and-wordpress-release-matchups)
- [How to switch to PHP 8.5 in MyKinsta](#how-to-switch-to-php-85-in-mykinsta)
- [How to switch to PHP 8.5 using the Kinsta API](#how-to-switch-to-php-85-using-the-kinsta-api)

---

Updated
:   March 19, 2026

![An illustration representing the dialog used to select PHP versions within the MyKinsta dashboard.](https://kinsta.com/wp-content/uploads/2025/12/php-8.5-mykinsta-1024x536.png)

Following the release of [PHP 8.5](https://kinsta.com/blog/php-8-5/) in November, this latest version of the server-side scripting language is now available to customers on our [Managed Hosting for WordPress](https://kinsta.com/wordpress-hosting/) platform.

Those who want to adopt PHP 8.5 can make the move within the [MyKinsta dashboard](https://kinsta.com/mykinsta/) or via the [Kinsta API](https://api-docs.kinsta.com/api-reference/wordpress-site-tools/modify-an-environments-php-version). We’ve already put the release through its paces across several CMS platforms in our annual [PHP benchmarking tests](https://kinsta.com/blog/php-benchmarks/).

Here’s what you need to know about making the switch here at Kinsta.

## Think twice (or more) before adopting a new PHP release

Changing the PHP version on your WordPress website is simple with Kinsta. But incompatibilities between a new PHP engine and old PHP code can have serious ramifications for a site, including knocking it offline altogether.

That’s why we recommend testing your website and any new PHP release in a [staging environment](https://kinsta.com/docs/wordpress-hosting/staging-environment/). Make the switch on your live site only after confirming that the staged environment performs without errors.

We also recommend backups. As you should before any major change to your WordPress site, [create a backup](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/#wordpress-backups) in case something goes wrong. The solution to a broken website after moving to a new PHP engine is usually reverting to the release you were using before the change.

### PHP and WordPress release matchups

Many website owners would describe the relationship between their WordPress installations and PHP releases as “complicated.” We provide [long-term support](https://kinsta.com/changelog/end-of-life-php-support/) for PHP releases (as old as 7.4) that the PHP Group deems [past end-of-life](https://www.php.net/eol.php). We do this because so many WordPress users have significant applications (usually found in the code of themes or plugins) that break on more recent releases of PHP.

Life is easier for site owners who stay up to date. [WordPress 6.9](https://kinsta.com/blog/wordpress-6-9/) is scheduled for release and has already been [tested successfully](https://make.wordpress.org/core/2025/11/21/php-8-5-support-in-wordpress-6-9/) with PHP 8.5. However, this compatibility with new PHP releases is always considered “Beta” by WordPress developers until at least 10% of all known instances of the CMS are running on that PHP engine or a newer version.

## How to switch to PHP 8.5 in MyKinsta

To upgrade a WordPress environment to PHP 8.5, log in to MyKinsta and navigate to **WordPress Sites** > ***environment name*** > **Tools**, then click the **Change** button on the **PHP settings** card:

![Screenshot showing the MyKinsta Tools menu and the PHP settings option.](https://kinsta.com/wp-content/uploads/2025/12/php-settings-8-5-release.png)

Changing PHP settings for a WordPress environment in MyKinsta.

You can perform a PHP update in bulk for multiple environments from the **WordPress sites** page. In the example below, we’ve selected the checkboxes beside the names of staging environments for two sites and are choosing **Change PHP settings** from the **Actions** dropdown menu:

![Screenshot of the WordPress sites page in MyKnsta with multiple environments selected for a PHP update.](https://kinsta.com/wp-content/uploads/2025/12/php-settings-8-5-release-multi.png)

Changing the PHP settings for multiple WordPress environments.

Whichever path you choose, the next step is to select the PHP version you want to adopt and click the **Change PHP version** button:

![Screenshot of the PHP settings dialog in MyKinsta with PHP 8.5 selected.](https://kinsta.com/wp-content/uploads/2025/12/php-settings-8-5-release-select.png)

Selecting **PHP 8.5** while performing PHP settings update.

While updating the version of PHP behind your website, you have the option to enable **Automatic PHP updates**. This feature ensures that your website never runs on a release of PHP that has reached end of life. It will not automatically upgrade from a PHP release that is still supported by PHP’s developers.

Switching to a different PHP engine takes a few minutes. The change requires a PHP restart, which will make the admin dashboard in WordPress briefly unavailable. The MyKinsta dashboard will report when the process is complete.

## How to switch to PHP 8.5 using the Kinsta API

The Kinsta API’s `/tools` endpoint can be used to update the version of PHP running on an environment and also enable or disable the automatic PHP updates feature.

Here’s an example using the cURL tool along with a Kinsta [API access key (token)](https://kinsta.com/blog/kinsta-api-key/) and an environment’s ID:

```
curl -i -X PUT 
  https://api.kinsta.com/v2/sites/tools/modify-php-version 
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' 
  -H 'Content-Type: application/json' 
  -d '{
    "environment_id": "{env_id}",
    "php_version": "8.5",
    "is_opt_out_from_automatic_php_update": false
  }
```

A successful request for a PHP version update will return a **202** status code.

And check this out: Austin Ginder of Anchor Hosting has a useful article on [bulk updating PHP on Kinsta websites](https://anchor.host/bulk-php-upgrades-with-kinstas-api/) using the API.
