---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/server-errors/"
title: "Troubleshooting - Server Errors"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-troubleshooting"
section: []
kinsta_last_updated: "March 9, 2026"
sitemap_lastmod: "2026-03-09T10:35:34+00:00"
fetched_at: "2026-10-07T22:39:40Z"
sha256: "9da4e513de5fc3f38e64dee5a624ee5e7bd14bdeebef5d5200d51f14db0c027f"
body_chars: 8422
extracted_with: "main article"
status: "live"
---

# Troubleshooting - Server Errors

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/server-errors/
**Kinsta last updated:** March 9, 2026

## On this page

- [502 Bad Gateway Error](#502-bad-gateway-error)
  - [Finding and resolving a 502 Bad Gateway Error](#finding-and-resolving-a-502-bad-gateway-error)
    - [Third-party CDN](#third-party-cdn)
    - [Error log](#error-log)
    - [MyKinsta analytics](#mykinsta-analytics)
    - [Plugins and themes](#plugins-and-themes)
    - [Request PHP timeout increase](#request-php-timeout-increase)
    - [Increase PHP threads](#increase-php-threads)
- [504 Gateway Timeout Error](#504-gateway-timeout-error)
  - [Finding and resolving a 504 Gateway Timeout Error](#finding-and-resolving-a-504-gateway-timeout-error)
    - [Errors during import](#errors-during-import)
    - [Third-party CDN](#third-party-cdn)
    - [Check upload path](#check-upload-path)
    - [File size of uploads](#file-size-of-uploads)
    - [Corrupted database](#corrupted-database)
    - [Plugins and themes](#plugins-and-themes)
    - [Error log](#error-log)
    - [Traffic and caching](#traffic-and-caching)
    - [Increase PHP threads](#increase-php-threads)
    - [Throttling traffic](#throttling-traffic)

---

## 502 Bad Gateway Error

A 502 error is usually displayed if a single PHP process runs for longer than the `max_execution_time` or `max_input_time` set in the PHP configuration, causing a PHP timeout to occur.

You’ll first need to determine what’s causing the 502 error to find a solution. You may need to increase resources, adjust settings, or find an alternative workflow in some cases.

For instance, if the error occurs when you’re attempting an import, running the import directly on the container using [WP-CLI](https://kinsta.com/docs/devkinsta/wp-cli/) or a local PHP or Bash script is a recommended alternative.

### Finding and resolving a 502 Bad Gateway Error

There may be a number of places to check and solutions to try when hunting down the source of a 502 Bad Gateway Error.

#### Third-party CDN

If your site uses a [third-party CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/proxy-cdn-compatibility-checklist/) in addition to Kinsta’s [Cloudflare integration](https://kinsta.com/cloudflare-integration/), temporarily disable or bypass that CDN. If the issue is resolved, you’ll need to adjust settings or check with your CDN provider’s support to see if a firewall or other feature is interfering with your site.

#### Error log

[Check the **error.log**](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/) for your site in MyKinsta (or download via [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/)) to narrow down the source of the error. If nothing obvious stands out, it may be helpful to [enable `WP-DEBUG`](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/wordpress-debugging/).

#### MyKinsta analytics

View the [500 error breakdown report](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#500-error-breakdown) in MyKinsta Analytics to see the total number of 502 errors and when they occur.

#### Plugins and themes

Deactivate all plugins and switch to a default theme. If the issue is resolved, reactivate plugins one by one and reactivate your theme until the issue reoccurs. Once you’ve determined which plugin or theme is the source, send a copy of the error to the plugin or theme developer so they can help you resolve the issue.

#### Request PHP timeout increase

Here at Kinsta, the `max_execution_time` or `max_input_time` values are set to 300 seconds (5 minutes) by default. The maximum PHP timeout values available are based on your current [hosting plan](https://kinsta.com/pricing/). If you need these increased, start a new [chat with our Support team](https://kinsta.com/docs/support/contact-support/).

#### Increase PHP threads

In some cases, more [PHP threads](https://kinsta.com/docs/wordpress-hosting/php/#php-threads) may be needed. You can increase the number of PHP threads within [PHP performance](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/). If you’re not sure, our Support team can help you determine if adding more PHP threads is needed for your site.

## 504 Gateway Timeout Error

A 504 error is usually displayed when the connection between your browser and the web server is held open for more than 180 seconds, causing an HTTP timeout to occur.

When multiple requests come in at or near the same time, some requests may need to wait in line to be handled. So, even though the server may be processing requests, if each one is taking a long time to be processed, a large number of requests can stack up. When the queue gets too big, and processes wait too long, the older requests are disregarded by the server, causing a 504 gateway error to be returned.

Like most error troubleshooting, the first step is to figure out the root cause of the error.

### Finding and resolving a 504 Gateway Timeout Error

#### Errors during import

If the error is occurring during an import, try running the import directly on the server using [WP-CLI](https://kinsta.com/docs/devkinsta/wp-cli/) or a local PHP or Bash script. This will bypass the HTTP connection entirely, allowing you to complete the import without a 504 error.

#### Third-party CDN

If your site uses a [third-party CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/proxy-cdn-compatibility-checklist/) in addition to Kinsta’s [Cloudflare integration](https://kinsta.com/cloudflare-integration/), temporarily disable or bypass that CDN.

#### Check upload path

If you’re seeing an error related to the file path when trying to upload a file (e.g. adding and uploading an image to content), the upload path may be incorrect. This is most common right after migrating a site. Depending on the configuration at your previous host, the upload path may have been customized. This can be seen in either the `wp_options` table or in the WordPress dashboard (**Settings** > **Media** > **Uploading Files**).

In the WordPress dashboard, if you see options labeled **Store uploads in this folder** and **Full URL path to files**, they have been customized. The corresponding data in the database can be found in the `wp_options table` in the `upload_path` and `upload_url_path` options.

You can delete anything in those fields (either in the WordPress dashboard or the database) to set them back to their defaults.

#### File size of uploads

If you’re seeing an error related to file size when trying to upload a file, check the size of the file(s) you’re trying to upload. Some CDNs limit the size of files you can upload. If you’re using a third-party CDN, check the maximum upload size in your CDN settings and make sure your uploads are less than the maximum. Or, if your site requires the file size to be that large, adjust the maximum upload size at your CDN (if possible).

#### Corrupted database

Occasionally, a corrupted database can be the source of 504 errors. If you see errors that indicate a corrupted database (e.g. “One or more database tables are unavailable. The database may need to be repaired.” when logging into the WordPress dashboard) see our guide on [repairing a corrupt database](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/fix-error-establishing-a-database-connection-in-wordpress/).

#### Plugins and themes

While it isn’t as common, sometimes a plugin or theme can be the source of a 504 error. The best way to test for this is to deactivate all plugins and switch to a default theme. If the issue is resolved, reactivate plugins one by one and reactivate your theme until the issue reoccurs. Once you’ve determined which plugin or theme is the source, send a copy of the error to the plugin or theme developer so they can help you resolve the issue.

#### Error log

[Check the **error.log**](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/) for your site in MyKinsta (or download via [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/)) to narrow down the source of the error. If nothing obvious stands out, it may be helpful to [enable `WP-DEBUG`](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/wordpress-debugging/).

#### Traffic and caching

Check the [Visitors report in MyKinsta analytics](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#visits) to see if your site is experiencing a traffic spike and/or a large number of un-cached requests. Opening a chat with our Support team can be helpful in this case, so we can help you determine if the requests are legitimate and if more resources (like PHP threads) may be needed.

#### Increase PHP threads

In some cases, more [PHP threads](https://kinsta.com/docs/wordpress-hosting/php/#php-threads) may be needed. You can increase the number of PHP threads within [PHP performance](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/). If you’re not sure, our [Support team](https://kinsta.com/docs/support/contact-support/) can help you determine if adding more PHP threads is needed for your site.

#### Throttling traffic

If your site is experiencing a traffic spike or just more traffic in general, and increasing resources isn’t an option, an alternative to keep too many requests from coming in all at once to the server is to implement a queuing system like one of the following:

- [Queue-it](https://queue-it.com/)
- [Queue-Fair](https://queue-fair.com/)
- [Crowdhandler](https://www.crowdhandler.com/)
