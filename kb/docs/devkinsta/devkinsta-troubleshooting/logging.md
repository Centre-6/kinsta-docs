---
url: "https://kinsta.com/docs/devkinsta/devkinsta-troubleshooting/logging/"
title: "Troubleshooting - Logs and Debugging"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-troubleshooting"
section: []
kinsta_last_updated: "July 18, 2024"
sitemap_lastmod: "2024-07-18T08:40:27+00:00"
fetched_at: "2026-10-07T22:36:45Z"
sha256: "2fe483afd1f3e6da0ee880c83aefdab6bb9558085c19c5c23461b99127eaaa27"
body_chars: 2349
extracted_with: "main article"
status: "live"
---

# Troubleshooting - Logs and Debugging

**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-troubleshooting/logging/
**Kinsta last updated:** July 18, 2024

## On this page

- [WordPress debug log](#wordpress-debug-log)
  - [Location](#location)
- [Access log](#access-log)
  - [Location](#location)
  - [Example](#example)
- [Error log](#error-log)
  - [Location](#location)
- [PHP-FPM logs](#php-fpm-logs)
  - [Location](#location)
- [Service logs](#service-logs)

---

Logs can be very helpful when troubleshooting and debugging issues on your WordPress sites. To view your WordPress logs, navigate to the **<projectPath>/logs/** folder on your hard drive and open any log file in your favorite text editor.

The default **<projectPath>** is **/Users/user/DevKinsta**

## WordPress debug log

On your site’s info page, enable **WP_DEBUG**. Enabling this in DevKinsta will also enable saving errors to your site’s **debug.log** file. Read more on [wordpress.org](https://wordpress.org/support/article/debugging-in-wordpress/)

![Enable WP_DEBUG on your site in DevKinsta. ](https://kinsta.com/wp-content/uploads/2023/11/devkinsta-enable-wpdebug-1024x195.png)

Enable WP_DEBUG on your site in DevKinsta.

### Location

**<projectPath>/public/<siteName>/wp-content/debug.log**

## Access log

The access log is a log of all requests processed by DevKinsta. When you visit your site in a browser, the request is logged in the **access.log** file with the following data:

- Date and time
- Request (Method and URI)
- [HTTP Status Code](https://kinsta.com/blog/http-status-codes/) (200 if everything is fine).
- Bytes sent
- HTTP referer
- User-agent
- HTTP X Forwarded for

### Location

**<projectPath>/logs/<siteName>_access.log**

### Example

Copy

```
[30/Dec/2020:13:49:35 +0000] "GET /wp-content/themes/twentytwentyone/assets/css/print.css?ver=1.0 HTTP/1.1" 200 2897 "http://testsite.local/?skip_cache=1" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.119 Electron/9.0.5 Safari/537.36" "-"
```

## Error log

Specific PHP errors are logged in the **_error.log** file.

### Location

**<projectPath>/logs/<siteName>_error.log**

## PHP-FPM logs

To view the PHP FastCGI Process Manager logs (PHP-FPM logs), check the file that corresponds to the PHP version used by your local WordPress site.

### Location

**<projectPath>/logs/php7.2-fpm.log  
<projectPath>/logs/php7.3-fpm.log  
<projectPath>/logs/php7.4-fpm.log  
<projectPath>/logs/php8.0-fpm.log**

## Service logs

To view Docker container logs, use the commands below in the terminal/command line:

**NGINX logs:** `docker logs -f devkinsta_nginx`

**PHP-FPM logs:** `docker logs -f devkinsta_fpm`

**MariaDB logs:** `docker logs -f devkinsta_db`

**MailHog logs:** `docker logs -f devkinsta_mailhog`
