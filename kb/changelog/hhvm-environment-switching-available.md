---
url: "https://kinsta.com/changelog/hhvm-environment-switching-available/"
title: "HHVM Environment Switching Available"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-09-16T09:44:21"
change_signal: "2026-09-16T09:44:21"
fetched_at: "2026-10-07T22:58:23Z"
sha256: "bff692ac03c0df122d87a8becac53eb753ce4bcce635dbb5625d339e866a3c9d"
body_chars: 951
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# HHVM Environment Switching Available

**Product:** Changelog
**Source:** https://kinsta.com/changelog/hhvm-environment-switching-available/
**Kinsta last updated:** 2026-09-16T09:44:21

---

A few weeks back we introduced the ability to switch your environment between PHP 5.6 and PHP 7. We’re happy to announce today that the ability to use HHVM has also been added to our Google Cloud plans.

HHVM is great because it provides 2-5x better performance than the official PHP FastCGI interpreter. To make sure you can test your website before making the switch (which you should) you can also select HHVM for your test environments.

[![Switching PHP Versions at Kinsta](https://kinsta.com/wp-content/uploads/2016/08/php_version.gif)](https://kinsta.com/wp-content/uploads/2016/08/php_version.gif)

Switching PHP Versions at Kinsta

Before you use HHVM on your live site please note the following:

- Some themes and plugins may not be compatible with HHVM so make sure to perform a full website test using a test environment
- New Relic does not support HHVM yet so we won’t be able to see backend processes if something is slowing your site.
