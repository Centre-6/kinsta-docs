---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/troubleshooting-wordpress-performance/"
title: "Troubleshooting - Troubleshooting Performance"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-troubleshooting"
section: []
kinsta_last_updated: "July 1, 2025"
sitemap_lastmod: "2025-07-01T16:33:39+00:00"
fetched_at: "2026-10-07T22:38:47Z"
sha256: "239eb7e4287062d0970c637fe6d486aaf7a5d17297263c44b9838aa304520a8e"
body_chars: 5644
extracted_with: "main article"
status: "live"
---

# Troubleshooting - Troubleshooting Performance

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/troubleshooting-wordpress-performance/
**Kinsta last updated:** July 1, 2025

## On this page

- [Recommendations](#recommendations)
  - [Check for high admin-ajax.php usage](#check-for-high-admin-ajaxphp-usage)
  - [Check your WordPress site’s plugins and themes](#check-your-wordpress-sites-plugins-and-themes)
  - [Transients Manager plugin](#transients-manager-plugin)
  - [Hire a WordPress developer or agency](#hire-a-wordpress-developer-or-agency)
- [Troubleshooting tools](#troubleshooting-tools)
  - [Query Monitor plugin](#query-monitor-plugin)
  - [Kinsta’s APM tool](#kinstas-apm-tool)
  - [New Relic](#new-relic)
  - [Blackfire monitoring](#blackfire-monitoring)
  - [Server logs](#server-logs)
  - [WP_DEBUG](#wp-debug)
  - [Xdebug](#xdebug)
- [Additional resources](#additional-resources)

---

In our experience, most performance issues originate from glitches in plugin or theme updates, inefficient code, or a plugin or theme not supporting the latest version of PHP or WordPress. In this article, we’ll make recommendations on what to look for and tools to help you troubleshoot common performance issues on your site.

## Recommendations

### Check for high admin-ajax.php usage

Make sure [Ajax is properly implemented on your site](https://kinsta.com/blog/admin-ajax-php/#how-to-debug-high-adminajaxphp-usage-on-wordpress). Plugins are typically (but not always) behind high **admin-ajax.php** usage. This usually presents on the front of the site and can often be seen in [speed test reports](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/website-testing-tools/).

Another common cause for high **admin-ajax.php** usage is due to many logged-in users at the same time in the WordPress dashboard triggering the WordPress Heartbeat API to generate frequent Ajax calls.

### Check your WordPress site’s plugins and themes

Minimize the number of plugins installed on your site as much as possible. Ensure that the remaining plugins are necessary, still supported, and updated.

Using your [staging environment](https://kinsta.com/docs/wordpress-hosting/staging-environment/), you can [deactivate all plugins](https://kinsta.com/blog/disable-wordpress-plugins/) and switch to a default theme. If performance improves, reactivate plugins one by one and reactivate your theme until the performance issue reoccurs. Once you’ve determined which plugin or theme is the source (sometimes it’s a combination of two or more plugins), work with the developer(s) so they can help you resolve the issue and implement the change(s) on your live site.

### Transients Manager plugin

If you trace performance issues to an excessive number of transients clogging up your database, the free [Transients Manager](https://wordpress.org/plugins/transients-manager/) plugin is an excellent resource for clearing those.

### Hire a WordPress developer or agency

If you’re not familiar with troubleshooting performance issues, [working with a developer or agency](https://kinsta.com/agency-directory/) to help you track down and resolve issues is recommended.

## Troubleshooting tools

### Query Monitor plugin

The Query Monitor plugin is a free plugin that helps with debugging a number of different areas in WordPress. It can help you track down slow database queries, AJAX calls, REST API requests, and much more. For more details, we have a blog post on [how to use the Query Monitor plugin](https://kinsta.com/blog/query-monitor/).

### Kinsta’s APM tool

[Kinsta’s APM tool](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/) helps you identify PHP performance bottlenecks on your WordPress site without having to sign up for third-party monitoring services like New Relic.

### New Relic

[New Relic](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/custom-new-relic-tracking/) is a monitoring tool that gives you detailed performance breakdowns on a granular level. Go to the **WordPress** > **Plugins and themes** tab and sort by **Most time consuming**. This can help show which plugins (or a theme) are associated with the processes that take the longest to complete. Then, go to the **Transactions** tab to see which specific transactions are most time consuming.

### Blackfire monitoring

[Blackfire](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/wordpress-blackfire-monitoring/) is a monitoring tool that provides detailed information about your site’s performance in real-time to identify issues and optimize your site.

### Server logs

[Log files are available](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/) in MyKinsta and can also be downloaded via [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/). These files can be helpful when troubleshooting performance issues on your site.

### WP_DEBUG

WordPress has a built-in [debug mode](https://kinsta.com/blog/wordpress-debug/) to help you track down what’s going on by displaying all PHP errors, notices, and warnings. There are also additional debugging options that can be helpful when investigating specific types of issues.

### Xdebug

Xdebug is a PHP extension that can be used with your preferred IDE integrated development environment) in your staging environment to step through your site’s code to troubleshoot issues. To enable Xdebug for your environment, start a new [chat with our Support team](https://kinsta.com/docs/support/contact-support/).

## Additional resources

To take a deeper dive into troubleshooting some common performance issues and other errors, check out these resources:

- [How to Find WordPress Performance Bottlenecks with New Relic](https://kinsta.com/blog/wordpress-performance-new-relic/)
- [Query Monitor – Debug WordPress and Improve Website Performance](https://kinsta.com/blog/query-monitor/)
- [How to Eliminate Render-Blocking JavaScript and CSS in WordPress](https://kinsta.com/blog/eliminate-render-blocking-javascript-css/)
- [Leverage Browser Caching](https://kinsta.com/blog/leverage-browser-caching/)
- [How to Fix a 500 Internal Server Error](https://kinsta.com/blog/500-internal-server-error/)
- [How to Fix a 502 Bad Gateway Error](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/server-errors/#502-bad-gateway-error)
- [How to Fix a 504 Gateway Timeout Error](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/server-errors/#504-gateway-timeout-error)
