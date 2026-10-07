---
url: "https://kinsta.com/changelog/php-8-availability/"
title: "PHP 8.0 Beta is Now Available for Staging Environments"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-04-20T09:33:29"
change_signal: "2026-04-20T09:33:29"
fetched_at: "2026-10-07T22:58:23Z"
sha256: "dff9d884ed7a175d31292b804fcd67b728bea077a1a5e8816ca8d7d062fbf515"
body_chars: 3185
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# PHP 8.0 Beta is Now Available for Staging Environments

**Product:** Changelog
**Source:** https://kinsta.com/changelog/php-8-availability/
**Kinsta last updated:** 2026-04-20T09:33:29

---

PHP 8.0 is slated for a December 2020 release, and it’ll bring a variety of performance-enhancing features and syntax improvements like the [JIT compiler](https://kinsta.com/blog/php-8/#jit--the-just-in-time-compiler), [negative index arrays](https://kinsta.com/blog/php-8/#negative-array-index), [Union Types 2.0](https://kinsta.com/blog/php-8/#union-types-2-0), and more.

To learn more about all the new features coming in the latest version of PHP, be sure to check out our in-depth [guide on PHP 8.0](https://kinsta.com/blog/php-8/).

At Kinsta, providing our customers with the latest technologies is an important part of what we do. We were among the first hosts to push [PHP 7.4](https://kinsta.com/blog/php-7-4/) across our entire infrastructure.

Today, we are excited to announce that **PHP 8.0 is now available for all** [**Kinsta staging environments**](https://kinsta.com/docs/wordpress-hosting/staging-environment/)**.**

![Enable PHP 8.0 on staging environments.](https://kinsta.com/wp-content/uploads/2020/10/kinsta-php-8-staging-environment.jpg)

Enable PHP 8.0 on staging environments.

At this time, PHP 8.0 is still in active development, and the version available on Kinsta staging environments is PHP 8.0 RC1 (Release Candidate 1). During our testing of PHP 8.0 RC1, we found that it is not fully compatible with certain configurations of WordPress.

Therefore, PHP 8.0 support is limited to staging environments to prevent live sites from throwing [PHP fatal errors](https://kinsta.com/blog/500-internal-server-error/). Once the final version of PHP 8.0 is released later this year, we will make it available for live environments as well.

Here are a few things to keep in mind when enabling PHP 8.0 on Kinsta:

- For now, only staging environments can be upgraded to PHP 8.0. Support for live environments will come after the official release of PHP 8.0 in December.
- If you [push a PHP 8.0 staging environment to live](https://kinsta.com/docs/wordpress-hosting/staging-environment/#push-staging-to-live-1), the resulting live container will automatically be set to PHP 7.4.
- Cloning a PHP 8.0 staging environment to live will result in a live container running PHP 7.4.
- [IonCube Loader](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/#ioncube-loader) is not compatible with PHP 8.0, so the ionCube Loader in MyKinsta is disabled for staging environments running PHP 8.0.

As the official release of PHP 8.0 draws closer, we recommend testing the compatibility of your site with a [WordPress developer](https://kinsta.com/trusted-tools-for-wordpress/). Since PHP 8.0 is not fully compatible with all configurations of WordPress at this time, our support team is [unable to assist with code compatibility issues](https://kinsta.com/docs/support/scope-of-support/).

If you find that PHP 8.0 causes a fatal error on your site, we recommend downgrading back to PHP 7.x until a developer can assist with [debugging](https://kinsta.com/blog/wordpress-debug/) your site.

To stay up to date with future updates including support for PHP 8.0 on live environments, don’t forget to [subscribe to our newsletter](https://kinsta.com/wordpress-newsletter/)!
