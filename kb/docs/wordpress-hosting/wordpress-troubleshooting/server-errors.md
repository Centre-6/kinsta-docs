---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/server-errors/"
title: "Server Errors"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-troubleshooting"
section: ["WordPress Hosting", "Troubleshooting"]
kinsta_last_updated: "2026-11-02T17:40:09"
change_signal: "2026-11-02T17:40:09"
fetched_at: "2026-11-11T13:03:01Z"
sha256: "3f51a5961ff5cc2a3420053903d41d579dcbb2d60acb599f91945a81317e8c7b"
body_chars: 13715
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Server Errors

**Section:** WordPress Hosting > Troubleshooting
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/server-errors/
**Kinsta last updated:** 2026-11-02T17:40:09

## On this page

- [500 Internal Server Error](#500-internal-server-error)
  - [Check your error log](#check-your-error-log)
  - [Common causes and fixes](#common-causes-and-fixes)
  - [When to contact Support](#when-to-contact-support)
- [501 Not Implemented](#501-not-implemented)
- [502 Bad Gateway Error](#502-bad-gateway-error)
  - [Check whether the error reached your site](#check-whether-the-error-reached-your-site)
  - [If the error came from your site’s server](#if-the-error-came-from-your-sites-server)
  - [If you use a third-party CDN or proxy](#if-you-use-a-third-party-cdn-or-proxy)
  - [When to contact Support](#when-to-contact-support)
- [503 Service Unavailable](#503-service-unavailable)
- [504 Gateway Timeout Error](#504-gateway-timeout-error)
  - [Find the slow request](#find-the-slow-request)
  - [If one request or action is slow](#if-one-request-or-action-is-slow)
  - [If many requests are slow at the same time](#if-many-requests-are-slow-at-the-same-time)
  - [If you use a third-party CDN or proxy](#if-you-use-a-third-party-cdn-or-proxy)
  - [When to contact Support](#when-to-contact-support)

---

Kinsta’s [uptime monitoring](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/uptime-monitoring/) checks your site regularly and emails you if it detects a **500**, **502**, or **504** error. Other errors on this page, such as 501 and 503, don’t trigger a notification, so you’ll only find out about them if you or your visitors see them.

## 500 Internal Server Error

A 500 Internal Server Error means your site’s code ran into a problem it couldn’t recover from. On WordPress sites, this is usually a PHP fatal error from a plugin, a theme, or custom code, or a process that runs out of memory. Because the error happens inside your site, it’s almost always recorded in your logs.

### Check your error log

1. Note the time of the error and the URL.
2. In MyKinsta, open your site’s [error.log](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/#error-log) and look for entries from the same time. Fatal errors include `PHP Fatal error` and usually name the file and line where the problem happened.
3. The file path usually shows the cause. A path under `wp-content/plugins/` or `wp-content/themes/` points to that plugin or theme.

If error.log has no matching entry, check whether [WordPress debugging](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/wordpress-debugging/) is turned on in MyKinsta. While it’s on, errors go to the debug log instead of error.log.

### Common causes and fixes

- **Plugin or theme errors:** Deactivate the plugin or theme named in the error. If you can’t reach the WordPress dashboard, rename the plugin’s folder in [File Manager](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-file-manager/), over [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/), or use [WP-CLI](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-wp-cli/). If the error started after an update, restore a [backup](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#restore-wordpress-backups) or roll back the update, then send the error to the developer.
- **Memory limit errors** (`Allowed memory size ... exhausted`)**:** A plugin or process used more memory than PHP allows, which is 256 MB per PHP thread by default. To see how often this happens, check the [PHP memory limit reached](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#php-memory-limit-reached) chart in MyKinsta under **Sites** > ***sitename*** > **Analytics** > **Performance**. Fix the plugin or process named in the error first, because a broken script can use up any amount of memory. If your site genuinely needs more memory per thread, you can change your [PHP performance settings](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/) under **Sites** > ***sitename*** > **Info** > **PHP performance**. The number of PHP threads and the memory per thread are set together, so giving each thread more memory may mean running fewer threads; see [Reduce and optimize your PHP thread usage](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/#reduce-and-optimize-php-thread-usage).
- **Time limit errors** (`Maximum execution time ... exceeded`)**:** These come from processes that don’t go through a browser, such as WP-CLI commands or cron jobs, or from a plugin that sets its own lower time limit. Check which command, scheduled task, or plugin was running at the time.
- **PHP version incompatibility:** If the errors started after a PHP version change, a plugin or theme may not support the new version. [Update it](https://kinsta.com/docs/wordpress-hosting/php/wordpress-restart-update-php/) or switch back temporarily.

### When to contact Support

If you can’t find the cause, or the errors continue after you’ve tried these steps, [contact Support](https://kinsta.com/docs/support/contact-support/) with the URL, the time and timezone of the error, and any related error.log entries.

## 501 Not Implemented

A 501 Not Implemented error means the server doesn’t support what the request asked it to do. It’s rare on Kinsta, and it’s usually not caused by your plugins or theme.

- **A stopped staging environment:** If you see a 501 on a staging site, the staging environment may have been stopped. In MyKinsta, open the [staging environment and start it](https://kinsta.com/docs/wordpress-hosting/staging-environment/#restart-staging-environment).
- **An unusual request method:** Tools and integrations that send requests using a method the server doesn’t support, such as some file-sync clients, can get a 501. Check the tool’s settings or documentation.

If you see a 501 on your live site, check Kinsta’s status page, then [contact Support](https://kinsta.com/docs/support/contact-support/) with the URL and the time and timezone of the error.

## 502 Bad Gateway Error

A 502 Bad Gateway error means the web server couldn’t get a valid response from PHP, the part of your site’s server that runs WordPress. Usually, this means PHP crashed while handling a request or wasn’t running. These errors happen on your site’s server, so they’re recorded in your site’s logs.

Errors between Cloudflare and your site look different. Visitors see a Cloudflare-branded error page with a Ray ID, and these errors are never recorded in your site’s logs.

### Check whether the error reached your site

1. Note the time of the error.
2. If you saw the error yourself, check which page appeared:
   - A plain white page with **502 Bad Gateway** and “nginx” underneath came from your site’s server. Continue with the next step.
   - A Cloudflare-branded error page with a Ray ID happened before the request reached your site. [Contact Support](https://kinsta.com/docs/support/contact-support/).
3. In MyKinsta, open your site’s [access.log](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/#access-log) and search for `502` around that time.
4. If you find a matching entry, the error came from your site’s server. Check [error.log](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/#error-log) for entries from the same time, `connect() to unix:...php-fpm.sock failed` means PHP wasn’t accepting requests; a `PHP Fatal error` names the file that caused a crash.
5. If there’s no matching entry, the error happened before the request reached your site. If you use a third-party CDN, see below; otherwise, [contact Support](https://kinsta.com/docs/support/contact-support/).

### If the error came from your site’s server

- **PHP stopped or isn’t responding:** If error.log shows `connect() to unix:...php-fpm.sock failed`, [restart PHP](https://kinsta.com/docs/wordpress-hosting/php/wordpress-restart-update-php/) in MyKinsta. If it keeps happening, look in error.log for fatal errors just before the 502s.
- **Plugins and themes:** A plugin or theme can crash a PHP process partway through a request. If error.log shows a fatal error or crash at the time of the 502, deactivate the plugin or theme involved, or test by deactivating all plugins and switching to a default theme.

### If you use a third-party CDN or proxy

If your site uses a third-party CDN or proxy in addition to Kinsta’s Cloudflare integration, temporarily bypass it. If the 502 errors stop, contact your CDN provider about its settings or firewall rules.

### When to contact Support

If the errors keep happening, there’s no matching 502 in your access.log, or nothing in your logs explains them, [contact Support](https://kinsta.com/docs/support/contact-support/) with the URL, the time and timezone of the error, and how often it happens. If visitors saw a Cloudflare error page, include the Ray ID shown on it.

## 503 Service Unavailable

A 503 Service Unavailable error means your site is temporarily refusing requests. On WordPress sites, this is usually because the site is in maintenance mode, either on purpose or because an update didn’t finish.

- **“Briefly unavailable for scheduled maintenance”:** WordPress shows this while it installs updates, then removes the message when the updates finish. If an update is interrupted, the site can stay in maintenance mode. Delete the `.maintenance` file from your site’s root folder over [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/), then check that the plugin, theme, or WordPress update completed and run it again if not.
- **A maintenance mode or coming soon plugin:** These plugins return a 503 so search engines know the site will be back. Turn off maintenance mode in the plugin’s settings, or deactivate the plugin.
- **A plugin or theme returning a 503:** If neither of these applies, deactivate your plugins one at a time to find the one responsible.

If you can’t find the cause, [contact Support](https://kinsta.com/docs/support/contact-support/) with the URL and the time and timezone of the error.

## 504 Gateway Timeout Error

A 504 Gateway Timeout error means a request to your site took too long to finish. Requests to your site can run for up to 180 seconds. If a request hasn’t finished by then, the web server stops waiting and returns a 504, and visitors see a plain white page with **504 Gateway Time-out** and “nginx” underneath. Occasionally, Cloudflare’s own 180-second limit is reached first, and visitors see a Cloudflare **524: A timeout occurred** page instead. Both errors mean the same thing: the request took too long.

Timeouts usually happen because a single request is doing too much work, or because many requests arrive at once and some have to wait in line until they run out of time.

### Find the slow request

Timeouts are recorded in your site’s logs, so you can find the request that took too long:

1. Note the time of the error.
2. In MyKinsta, open your site’s [access.](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/#access-log)[log](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/#access-log)and search for `504` around that time. A timed-out request shows an `upstream_response_time` (the last value on each line) of about 180 seconds. Note the URLs.
3. Your site’s error.log has a matching entry for each one: `upstream timed out ... while reading response header from upstream`, followed by the request URL.
4. If visitors saw a Cloudflare 524 page instead, look in access.log for entries with a `499` status code and a request time of about 180 seconds.
5. If there are no matching entries, the timeout happened before the request reached your site. If you use a third-party CDN, see below; otherwise, [contact Support](https://kinsta.com/docs/support/contact-support/).

### If one request or action is slow

If the slow entries all point to the same URL or action:

- **Imports, exports, and bulk operations:** Run them directly on the server with [WP-CLI](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-wp-cli/) or a script. These don’t go through the 180-second limit.
- **Uploads:** Uploads usually time out because of processing that happens after the file arrives: resizing or optimizing images, or plugins that copy files to cloud storage such as Amazon S3 or Google Cloud Storage. Check the settings of the plugin doing that work, or set it to process in the background if it supports that.
- **Plugins and themes:** A plugin or theme may be running slow code or waiting on a slow external service. Use [Kinsta’s APM tool](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/) to find the slow process, or deactivate plugins one at a time.
- **Database:** Slow or locked database queries can keep a request from finishing.

### If many requests are slow at the same time

If the slow entries are spread across many URLs, your site may be getting more requests than its PHP threads can handle. Requests wait in line for a free thread, and any request that waits more than 180 seconds times out. Once that happens, nearly every request can time out, because PHP keeps working through requests that visitors have already been sent an error for.

- Check the [Visits](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#visits) report in Analytics for traffic spikes, and check [kinsta-cache-perf.log](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/#kinsta-cache-perf-log) for a high number of uncached requests.
- If the traffic is legitimate and regular, your site may need more PHP threads. You can increase the PHP threads within [PHP performance](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/); however, increasing the number of threads reduces the amount of memory per thread if you don’t also increase the PHP memory pool. To find out more, read [Reduce and optimize PHP thread usage](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/#reduce-and-optimize-php-thread-usage).
- For short traffic spikes you expect, such as a sale or launch, a queuing service such as [Queue-it](https://queue-it.com/), [Queue-Fair](https://queue-fair.com/), or [CrowdHandler](https://www.crowdhandler.com/) can limit how many visitors reach your site at once.

### If you use a third-party CDN or proxy

Some CDNs have shorter timeouts than Kinsta. Temporarily bypass the CDN; if the errors stop, check its timeout settings or contact your CDN provider.

### When to contact Support

If the errors keep happening and you can’t find the slow request, [contact Support](https://kinsta.com/docs/support/contact-support/) with the URL, the time and timezone of the error, and how often it happens.
