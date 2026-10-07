---
url: "https://kinsta.com/changelog/mu-plugin-changelog/"
title: "Kinsta Must-Use Plugin \u2014 Changelog"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-06-02T10:19:41"
change_signal: "2026-06-02T10:19:41"
fetched_at: "2026-10-07T22:58:23Z"
sha256: "8eb163a82cc08819b8666999163c3765268b0eef25d2814b16937b74ae649262"
body_chars: 12000
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Kinsta Must-Use Plugin — Changelog

**Product:** Changelog
**Source:** https://kinsta.com/changelog/mu-plugin-changelog/
**Kinsta last updated:** 2026-06-02T10:19:41

## On this page

- [3.7.0 (August 25, 2026)](#370-august-25-2026)
  - [Added](#added)
- [3.6.0 (June 02, 2026)](#360-june-02-2026)
  - [Changed](#changed)
  - [Fixed](#fixed)
- [3.5.1 (January 15, 2026)](#351-january-15-2026)
  - [Fixed](#fixed)
- [3.5.0 (January 01, 2026)](#350-january-01-2026)
  - [Changed](#changed)
  - [Fixed](#fixed)
- [3.4.0 (December 01, 2025)](#340-december-01-2025)
  - [Added](#added)
  - [Changed](#changed)
- [3.3.2 (August 04, 2025)](#332-august-04-2025)
  - [Changed](#changed)
- [3.3.1 (July 30, 2025)](#331-july-30-2025)
  - [Fixed](#fixed)
- [3.3.0 (July 29, 2025)](#330-july-29-2025)
  - [Fixed](#fixed)
  - [Changed](#changed)
  - [Added](#added)
- [3.2.0 (May 26, 2025)](#320-may-26-2025)
  - [Fixed](#fixed)
  - [Changed](#changed)
  - [Added](#added)
- [3.1.1 (February 28, 2024)](#311-february-28-2024)
  - [Fixed](#fixed)
- [3.1.0 (February 22, 2024)](#310-february-22-2024)
  - [Changed](#changed)
  - [Fixed](#fixed)
- [3.0.1 (September 28, 2023)](#301-september-28-2023)
  - [Added](#added)
  - [Changed](#changed)
  - [Fixed](#fixed)
- [3.0.0 (December 8, 2022)](#300-december-8-2022)
  - [Added](#added)
  - [Changed](#changed)
  - [Fixed](#fixed)
- [2.4.8 (July 11, 2022)](#248-july-11-2022)
  - [Added](#added)
  - [Changed](#changed)
  - [Fixed](#fixed)
- [2.4.7](#247)
  - [Added](#added)
  - [Changed](#changed)
- [2.4.6](#246)
  - [Added](#added)
  - [Changed](#changed)
- [2.4.5](#245)
  - [Fixed](#fixed)
- [2.4.4](#244)
  - [Added](#added)
- [2.4.3](#243)
  - [Fixed](#fixed)
- [2.4.2](#242)
  - [Fixed](#fixed)
  - [Changed](#changed)
- [2.4.1](#241)
  - [Fixed](#fixed)
- [2.4.0](#240)
  - [Added](#added)
- [2.3.9](#239)
  - [Fixed](#fixed)
- [2.3.8](#238)
  - [Added](#added)
- [2.3.7](#237)
  - [Fixed](#fixed)
- [2.3.4](#234)
  - [Changed](#changed)
- [2.3.3](#233)
  - [Changed](#changed)
  - [Fixed](#fixed)
- [2.3.2](#232)
  - [Fixed](#fixed)
- [2.3.1](#231)
  - [Added](#added)
  - [Changed](#changed)
- [2.3.0](#230)
  - [Added](#added)
- [2.2.4](#224)
  - [Changed](#changed)
- [2.2.3](#223)
  - [Changed](#changed)
- [2.2.2](#222)
  - [Changed](#changed)
- [2.2.1](#221)
  - [Changed](#changed)
- [2.2.0](#220)
  - [Changed](#changed)
  - [Added](#added)
- [2.1.2](#212)
  - [Changed](#changed)
- [2.1.1](#211)
  - [Changed](#changed)
- [2.1.0](#210)
  - [Changed](#changed)
  - [Added](#added)
- [2.0.21](#2021)
  - [Changed](#changed)
- [2.0.20](#2020)
  - [Changed](#changed)
  - [Added](#added)
- [2.0.19](#2019)
  - [Changed](#changed)
- [2.0.18](#2018)
  - [Added](#added)
- [2.0.17](#2017)
  - [Changed](#changed)
- [2.0.16](#2016)
  - [Added](#added)
  - [Changed](#changed)
- [2.0.15](#2015)
  - [Fixed](#fixed)
- [2.0 – 2.0.14](#20-2014)
  - [Added](#added)
  - [Changed](#changed)
  - [Fixed](#fixed)
- [1.5](#15)
  - [Added](#added)
  - [Changed](#changed)
  - [Removed](#removed)

---

The [Kinsta MU plugin](https://kinsta.com/docs/wordpress-hosting/kinsta-mu-plugin/) is installed by default on every site hosted at Kinsta and is required to make sure your site runs smoothly in our environment. Check out our documentation on [how to manage its settings](https://kinsta.com/docs/wordpress-hosting/kinsta-mu-plugin/#kinsta-mu-plugin-settings) or [update it](https://kinsta.com/docs/wordpress-hosting/kinsta-mu-plugin#update-the-kinsta-mu-plugin).

Below, you’ll find all the notable changes to this project.

## 3.7.0 (August 25, 2026)

### Added

- CDN Cache Autopurge.

## 3.6.0 (June 02, 2026)

### Changed

- Improved the Whitelabel feature to make it more customizable.
- Improved cache autopurge compatibility when publishing posts with the Yoast Duplicate Post plugin.

### Fixed

- Fixed a stability issue during object cache purging that could cause site crashes on high-traffic sites.
- Fixed custom purge URLs not being added correctly when they contained query strings.
- Fixed an issue where scheduled posts did not trigger a cache purge upon publishing.
- Fixed WooCommerce product pages not updating correctly when stock levels change.

## 3.5.1 (January 15, 2026)

### Fixed

- Manual cache clearing now works correctly when autopurge is disabled.
- Removed duplicate entries of banned plugins from the warning list.

## 3.5.0 (January 01, 2026)

### Changed

- Disabled `curl_close` on PHP 8.5 due to deprecation.

### Fixed

- Improved compatibility with WP Pusher.
- Resolved issues with global autopurge status in WP-CLI.

## 3.4.0 (December 01, 2025)

### Added

- Improved compatibility with some of the WordPress Core features, i.e. it should now automatically clear cache when header, widgets, and theme are updated or changed.
- Improved compatibility with WooCommerce, i.e. it should now automatically clear cache of the corresponding product page when the product stock is changed.
- Improved compatibility with Advanced Custom Fields (ACF), i.e. it should now automatically clear cache when ACF options are updated.
- Improved compatibility with Oxygen Builder i.e. it should now automatically clear cache when content on the builder editor is updated.
- New `wp kinsta cache autopurge` command to manage cache autopurge via WP-CLI.
- New WordPress filter hooks to manage cache autopurge via plugins or themes.

### Changed

- Lifted BackWPup restriction i.e. we’re now allowing to install BackWPup 5.6.0 or the latest..

## 3.3.2 (August 04, 2025)

### Changed

- Remove `strict_types` declarations
- Add namespace on main plugin file

## 3.3.1 (July 30, 2025)

### Fixed

- Fix calling `purge_complete_caches` method on `null` error

## 3.3.0 (July 29, 2025)

### Fixed

- Invalid URLs shown on the UI for adding custom URL to purge.

### Changed

- Improve all cache clearing in CLI.
- Clear all cache after running `wp cache flush`.
- Improve “litespeed-cache” from the banned plugin list.

### Added

- Elementor cache integration .

## 3.2.0 (May 26, 2025)

### Fixed

- Compatibility with `opcache_reset` function before executing the function.
- Compatibility with WP Rocket plugin.

### Changed

- Standardize notices, and messages shown for better clarity and consistency.

### Added

- - Loading state when triggering cache clearing.

</ul

## 3.1.1 (February 28, 2024)

### Fixed

- - - Readd the missing `--all` option to the  
      `wp kinsta cache purge` cli command

## 3.1.0 (February 22, 2024)

### Changed

- - - Updated dashboard styling to rely on WP core styles as much as  
      possible.

### Fixed

- - - Fixed unexpected extra slash adding issues when the home URL and the  
      custom clear path are combined.

## 3.0.1 (September 28, 2023)

### Added

- - - CDN Cache clearing functionality
    - Properly detect Kinsta Cache headers in Site Health Check when Edge  
      Cache is disabled

### Changed

- - - `KINSTAMU_ROLE` is now deprecated in favor of  
      `KINSTAMU_CAPABILITY`
    - Clean up and standardize wording in WP-CLI output
    - `wp kinsta cache purge` now takes `--site`,  
      `--cdn`, and `--object` to clear all the forms of  
      cache

### Fixed

- - - “Clear All Caches” from the admin bar now works properly
    - Fixed PHP 8.2 deprecation notices

## 3.0.0 (December 8, 2022)

### Added

- - - Admin setting to disable autopurge
    - Object cache clearing also clears PHP OPCache

### Changed

- - - Revamp styling to be simpler and match the new style of  
      MyKinsta
    - Better detection for which pages to purge on save
    - File and folder organization
    - Clean up unused code

### Fixed

- - - Corrupt settings will no longer break the site
    - Comment edits clear the cache

## 2.4.8 (July 11, 2022)

### Added

- - - Added `KINSTAMU_CACHE_PURGE_TIMEOUT` to override the  
      default 5 second timeout

### Changed

- - - Switched cache clearing calls to use curl instead of  
      `wp_remote_post`

### Fixed

- - - Banned plugins banner is no longer broken for a deleted plugin not  
      properly deactivated
    - Term and menu edits no longer purge the cache if  
      `KINSTAMU_DISABLE_AUTOPURGE` is set to `true`

## 2.4.7

### Added

- - - Added WordPress-Docs to PHPCS standards.

### Changed

- - - Cache classes refactor to modernize code.

## 2.4.6

### Added

- - - New action hook after full page/object cache purging is  
      complete.
    - New filter hook to block clearing cache from WP Admin.
    - Better detection for WordPress mobile mode via the wp_is_mobile  
      filter.

### Changed

- - - Post types that are not viewable will no longer be purged from  
      cache.

## 2.4.5

### Fixed

- - - Cache purge should now work again for comments added to a post via  
      the front-end comments form.

## 2.4.4

### Added

- - - Cache purge will now happen automatically for term update and  
      deletion.

## 2.4.3

### Fixed

- - - Make Admin Bar cache clear links request the plugin page so referrer  
      works correctly.
    - Fix PHP warnings.

## 2.4.2

### Fixed

- - - Fix PHP to be testable with PHPCS against WordPress-Core coding  
      standards.

### Changed

- - - Remove WP-Optimize from warning list.

## 2.4.1

### Fixed

- - - Fix referrer URL for Admin Bar cache clear links duplicating the  
      Subsite path in Multisite Networks.

## 2.4.0

### Added

- - - Add Duplicator Pro to warning list.

## 2.3.9

### Fixed

- - - The Clear Cache links on the Admin Toolbar will now try to redirect  
      to the referring URL instead of getting redirected to the admin-ajax.php  
      URL displaying 0.
    - Fix accessibility issue on Clear Cache submenu when Object Cache is  
      enabled.

## 2.3.8

### Added

- - - The plugin now has a local development environment to make  
      development a better process for contributors.

## 2.3.7

### Fixed

- - - Undefined index in cache clear function.
    - Deprecated code for PHP 8.0.

## 2.3.4

### Changed

- - - UpdraftPlus removed from the banned plugins list.
    - EWWW Image Optimizer removed from the banned plugins list.

## 2.3.3

### Changed

- - - Banned plugins list update.
    - Plugin URL points to the Kinsta KB page.
    - Better cache purge hook handling on post status change.

### Fixed

- - - Undefined function get_current_screen in some cases.

## 2.3.2

### Fixed

- - - KINSTA_CDN_USERDIRS related bug fix.

## 2.3.1

### Added

- - - Disable Swift Performance plugin cache.

### Changed

- - - Wordfence plugin integration enhancements.

## 2.3.0

### Added

- - - Handling of CDN asset rewrites in REST API requests.

## 2.2.4

### Changed

- - - Quick fix: extend function result check.

## 2.2.3

### Changed

- - - Quick fix: a missing variable.

## 2.2.2

### Changed

- - - Quick fix: image source rewrite bug in case of assets starts with  
      “//” or loaded from third-party source.

## 2.2.1

### Changed

- - - Quick fix: Undefined index: excludes.

## 2.2.0

### Changed

- - - Fixed minor dashboard issues.
    - Improved security.
    - Switched from absolute file path includes to the relative file  
      path.
    - Prevent CDN rewriting of admin-ajax.php.
    - Rewrite Image Attachment URLs in WP-API sub-resources.

### Added

- - - Add an option to exclude file types from CDN URL.

## 2.1.2

### Changed

- - - Quick fix: removed unnecessary span tags from the plugin’s “Add A  
      Custom URL” dashboard when the site has a very long domain.

## 2.1.1

### Changed

- - - Quick fix for an odd WP behavior of including the functions.php in  
      the compat folder.

## 2.1.0

### Changed

- - - Removed the PushEngage plugin from the plugin warning list.
    - Removed the WordFence plugin from the plugin warning list.
    - Removed abandoned plugin API endpoints.

### Added

- - - Set `WORDFENCE_DISABLE_LIVE_TRAFFIC` to true and show  
      error message if it is already set to false.

## 2.0.21

### Changed

- - - Fixed missing `wp_json_encode` function before WP  
      4.1.
    - Fixed minor CSS issue.

## 2.0.20

### Changed

- - - Minor bug fixes.
    - Add UTM source to the Kinsta.com link.

### Added

- - - The `KINSTAMU_ROLE` constant.
    - The `KINSTA_CDN_USERURL` constant.
    - The `wp kinsta plugin list` WP CLI command.

## 2.0.19

### Changed

- - - Updated the white-labeling options for the banned plugin  
      messages.

## 2.0.18

### Added

- - - PDF file is added to the CDN rewritable list.
    - Banned plugins are deactivated from now on.
    - Disallowed plugins are detected and a notice showed to the  
      appropriate admin users.
    - These plugins can’t be installed via the online plugin installer  
      from now on.

## 2.0.17

### Changed

- - - Updated an init hooks priority.

## 2.0.16

### Added

- - - Added a variable to prevent repeted single page cache purge during  
      the same action.
    - Added a variable to prevent repeted all cache purge during the same  
      init.
    - Added JS level HTML escape.

### Changed

- - - Update the cache purge class initiate order.
    - Fixed a white-label related minor issue.

## 2.0.15

### Fixed

- - - Backward compatible issue with WP Rocket plugin version 3.0.1.

## 2.0 – 2.0.14

### Added

- - - Integrated CDN.
    - A PHP constant for defining custom path for the mu plugin’s assets,  
      e.g.  
      `define( 'KINSTAMU_CUSTOM_MUPLUGIN_URL', 'http://yourdomain.com/custom-wp-content/mu-plugins');`.
    - A PHP constant for switching of the server level cache’s auto purge  
      on add/update/delete posts, e.g.  
      `define('KINSTAMU_DISABLE_AUTOPURGE', true);`.
    - WP CLI issue warning.
    - Sitemap to the purge list.
    - Purge list filters/hooks.
    - The `KINSTA_CACHE_DEBUG` constant.
    - Option to add further directories to the CDN replaceable paths.
    - Default AMP pages purge added.

### Changed

- - - New Kinsta UI design.

### Fixed

- - - Several multisite issues with purge part.
    - The `og:images` URL. It seems OG images don’t like the  
      “//” beginning.
    - The RegEx made possible that some links which directly called from  
      “/” were replaced.
    - Sometimes, the script made unnecessary replaces. Now it only does it  
      when the asset belongs to the following extensions:  
      `ogg|ogv|svg|svgz|eot|otf|woff|woff2|mp4|mp3|ttf|css|js|jpg|jpeg|gif|png|ico|webp|zip|tgz|gz|rar|bz2|doc|xls|exe|ppt|tar|mid|midi|wav|bmp|rtf`.
    - Symlink issue with Bedrock installs. Using WPMU_PLUGIN_URL constant  
      from now on.
    - HTTP – HTTPS asset issue when the site URL is HTTP but the site is  
      called via HTTPS.
    - Poor looking URL path in case of long URL.
    - Text update related to Object Cache.
    - Some rare warning issues.
    - Feed URLs are purged inmediattely after updates.

## 1.5

### Added

- - - Timeouts to internal `curl` calls.

### Changed

- - - HTTP detection.
    - Replaced `site_url()` with `home_url()` to be  
      more reliable.

### Removed

- - Unnecessary remaining test files.
