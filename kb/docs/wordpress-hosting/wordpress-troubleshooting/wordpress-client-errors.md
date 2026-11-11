---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/wordpress-client-errors/"
title: "Client Errors"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-troubleshooting"
section: ["WordPress Hosting", "Troubleshooting"]
kinsta_last_updated: "2026-11-02T17:57:56"
change_signal: "2026-11-02T17:57:56"
fetched_at: "2026-11-11T13:03:01Z"
sha256: "c129487ac6b81879b9768071d9199b4ddc3c28c1ff4d8944744e5b813a1e9cce"
body_chars: 17295
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Client Errors

**Section:** WordPress Hosting > Troubleshooting
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/wordpress-client-errors/
**Kinsta last updated:** 2026-11-02T17:57:56

## On this page

- [401 Unauthorized](#401-unauthorized)
- [403 Forbidden](#403-forbidden)
  - [Identify what blocked the request](#identify-what-blocked-the-request)
  - [Blocked by an access rule in MyKinsta](#blocked-by-an-access-rule-in-mykinsta)
  - [Blocked by the web server](#blocked-by-the-web-server)
  - [Blocked by Vulnerability protection](#blocked-by-vulnerability-protection)
  - [Blocked by a security plugin or CDN](#blocked-by-a-security-plugin-or-cdn)
  - [Blocked by WordPress](#blocked-by-wordpress)
  - [When to contact Support](#when-to-contact-support)
- [404 Not Found](#404-not-found)
- [405 Method Not Allowed](#405-method-not-allowed)
- [413 Request Entity Too Large](#413-request-entity-too-large)
- [429 Too Many Requests](#429-too-many-requests)
- [451 Unavailable For Legal Reasons](#451-unavailable-for-legal-reasons)
- [499 Client Closed Request](#499-client-closed-request)

---

Errors with a status code starting with 4 mean your site received the request but wouldn’t or couldn’t complete it: the page doesn’t exist, the visitor isn’t allowed to see it, the request was too large, or too many requests arrived at once. Unlike [server errors](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/server-errors/), they don’t mean your site is down, but they usually point to a setting or file you can change. Kinsta’s [uptime monitoring](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/uptime-monitoring/) doesn’t send notifications for any of the errors on this page; it only alerts you to 500, 502, and 504 server errors and to redirect loops.

## 401 Unauthorized

A 401 Unauthorized error means the page requires a username and password, and the visitor didn’t enter one or entered the wrong one.

- **Password protection:** If [htpasswd protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/htpasswd/) is enabled on your site or staging environment, visitors see a login prompt before the site loads. Enter the username and password set in MyKinsta, or turn off htpasswd protection if the site should be public.
- **API requests:** Tools and integrations that connect to your site through the WordPress REST API get a 401 if their credentials, such as an application password, are missing, wrong, or revoked. Check the credentials in the tool’s settings.

## 403 Forbidden

A 403 Forbidden error means the request was blocked on purpose. Several layers can block a request to your site, and each shows a different page, so the page you see is the quickest way to find the cause.

### Identify what blocked the request

Open the page that shows the error and compare it with the list below. If a visitor reported the error, ask them for a screenshot.

| What the page shows | What blocked the request | In your logs? |
| --- | --- | --- |
| Only a “403 Forbidden” heading in the top-left corner | An access rule in MyKinsta: bot protection, a bot protection exception, or the Block IP Address tool | No |
| A centered “403 Forbidden” heading with a line and “nginx” underneath | The web server, because of the file or folder requested | Yes, as 403 in access.log |
| A page showing a firewall rule ID | Vulnerability protection | Yes, as 403 in access.log |
| A page branded by a security plugin or CDN | That plugin or service | Depends on the plugin or service |
| A WordPress message, such as “Sorry, you are not allowed to access this page” | WordPress user permissions or an expired link | Yes, as 403 in access.log |

Then follow the steps for that type of block below.

### Blocked by an access rule in MyKinsta

If the page shows only a “403 Forbidden” heading, the request was blocked by your site’s access rules before it reached your site, so it doesn’t appear in your site’s logs.

1. In MyKinsta, go to **Sites** > ***sitename*** > **Bot protection** and go to the [**Top traffic** report](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#top-traffic). Select the traffic type that was blocked to see the IP addresses, paths, user agents, and countries involved.
2. Check your **Protection level**. Stricter levels block automated traffic, which can include legitimate tools such as uptime monitors, payment webhooks, and plugin integrations. Enable **Allow typical WordPress automations**, or add an **Allow** exception for the tool. For more information, see [Bot protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/).
3. Check your bot protection **Exceptions** for a **Block** rule that matches the visitor’s IP address, path, user agent, or country.
4. Check whether the visitor’s IP address is listed in the [Block IP Address](https://kinsta.com/docs/wordpress-hosting/site-management/block-ip-address/) tool.

If you’re testing with your own IP address, turn off any VPN or privacy relay, such as iCloud Private Relay, first. Otherwise, your site sees the relay’s IP address instead of yours, and an exception for your IP won’t match.

### Blocked by the web server

If the page shows “nginx” under the heading, the web server refused to serve the file or folder requested. Search your site’s [access.log](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/#access-log) for `403` to find the URL, then check:

- **A folder without an index file:** Visiting a folder that doesn’t contain an `index.php` or `index.html` file returns a 403 rather than listing the folder’s contents. Add an index file, or link to a specific file instead of the folder.

### Blocked by Vulnerability protection

If the page shows a firewall rule ID, [Vulnerability protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-vulnerability-protection/) blocked the request because it matched a rule for a known vulnerability in a plugin, theme, or WordPress version installed on your site. These blocks are recorded as `403` in your site’s [access.log](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/#access-log), so you can search it to see which URLs were blocked and when.

This usually means part of your site is out of date. Some vulnerabilities affect common features, such as uploading files through a form, so a rule can block normal visitors as well as attackers until the affected plugin is updated.

1. In MyKinsta, go to **Sites** > ***sitename*** > **Plugins and themes** and filter the list by **Vulnerable plugins**. A vulnerable version is marked with an exclamation mark, and its version number is highlighted in red. For more information, see [Manage Plugins and Themes](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-manage-plugins-themes/).
2. [Update](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-manage-plugins-themes/) the vulnerable plugins first, along with the plugin that handles the blocked page or feature. If you can’t tell which plugin is involved, update all your plugins, themes, and WordPress core.
3. Test the blocked page or action again.
4. To keep this from happening again, enable [automatic updates](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-plugins-themes-automatic-updates/).

Vulnerability protection can’t be turned off, and **Allow** exceptions in bot protection don’t override it. If the error continues after you’ve updated everything, [contact Support](https://kinsta.com/docs/support/contact-support/) and include the firewall rule ID shown on the page.

### Blocked by a security plugin or CDN

If the page is branded by a security plugin, such as Wordfence or Solid Security, or by a third-party CDN or firewall, that service blocked the request. Check its settings or logs for the blocked request, and add an exception there. If you use your own Cloudflare account, don’t enable Cloudflare’s WAF or bot protection features alongside Kinsta’s bot protection, because the two can block legitimate traffic.

### Blocked by WordPress

WordPress shows its own message when a logged-in user’s role doesn’t allow an action, or when a security link has expired:

- **“Sorry, you are not allowed to access this page”:** The user’s role doesn’t have permission. Check the [user’s role](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-users/) in **Users** in WordPress, or log in as an administrator.
- **“The link you followed has expired”:** The page was open too long or was loaded from cache. Reload the page and try again. If you see this when uploading, the file may also be too large; see [413 Request Entity Too Large](#413-request-entity-too-large).

### When to contact Support

If you can’t find what’s blocking the request, [contact Support](https://kinsta.com/docs/support/contact-support/) with the URL, the time and timezone of the error, a screenshot of the error page, and the visitor’s IP address if you know it.

## 404 Not Found

A 404 Not Found error means the page or file requested doesn’t exist at that URL. A few 404s are normal, such as visitors mistyping a URL or bots requesting files your site doesn’t have. Look into them when real pages or files return 404s, or when 404s start after a change to your site.

Your site’s [access.log](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/#access-log) records each 404 with the URL requested, so search it for `404` to see which URLs are affected.

- **All posts and pages return 404s, but the homepage works:** WordPress’s permalink settings need refreshing. In WordPress, go to **Settings** > **Permalinks** and click **Save Changes** without changing anything.
- **After a migration, domain change, or environment push:** Links and file paths may still point to the old domain or folder. Use the [Search and Replace tool](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/mykinsta-search-replace-tool/) to update old URLs, and check that uploaded files were copied across.
- **A file that exists returns a 404:** The web server may not have permission to read it. Your site’s error.log shows `open() "..." failed (13: Permission denied)` with the file’s path. This often happens after uploading files over [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/) or deploying code. Check the file’s permissions in your SFTP client (most show them when you right-click a file and open its permissions or info) or over [SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) with `ls -l`. Files should be set to `644` and folders to `755`.
- **A page or file was moved or deleted:** Add a [redirect](https://kinsta.com/docs/wordpress-hosting/redirect-rules/) from the old URL to the new one, so existing links and search results still work.
- **A page you just published still shows a 404:** The 404 may be cached. [Clear your site’s cache](https://kinsta.com/docs/wordpress-hosting/caching/#clear-cache-in-mykinsta) and any [CDN cache](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#clear-cdn-cache-in-mykinsta).

## 405 Method Not Allowed

A 405 Method Not Allowed error means the URL exists, but it doesn’t accept the type of request that was sent. Every request uses a method, such as `GET` to load a page or `POST` to submit a form, and some URLs only accept certain methods. You’ll most often see this error from forms, webhooks, and integrations rather than from visitors loading pages.  
Search your site’s [access.log](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/#access-log) for `405` to see which URL and method were used.

- **A form or tool sends data to a static file:** Submitting a form (a `POST` request) to a static file, such as an `.html` file or an image, returns a 405 because static files can only be loaded. Check that the form’s action or the tool’s URL points to a WordPress page or endpoint, not to a file.
- **A webhook or integration uses the wrong method:** Payment providers, form services, and other integrations need the exact URL and method their documentation gives. Check the integration’s settings, and copy the URL again from the plugin that provides it.
- **A redirect changes the request:** When a request is redirected, for example from `http://` to `https://` or from `www.` to the non-www domain, many tools resend it as a `GET`, so an endpoint that expects a `POST` rejects it. Use the final URL, including `https://` and the correct domain, in the tool’s settings.

## 413 Request Entity Too Large

A 413 Request Entity Too Large error means a request, usually a file upload, was too large to accept. Your site has two upload limits, and which one a file goes over decides what you see:

- **The web server’s limit (128 MB):** Requests larger than 128 MB are rejected before they reach WordPress. Tools such as curl and API clients show the 413 error, but browser upload tools, such as the WordPress media uploader, usually show a general upload error instead. Your site’s error.log records the request as `client intended to send too large body`, followed by its size in bytes.
- **Your plan’s PHP upload limit:** The request reaches WordPress, but PHP drops the file, so there’s no 413. Instead, WordPress shows its own message, such as “exceeds the maximum upload size for this site” or **The link you followed has expired**.

Your plan’s PHP upload limit (`upload_max_filesize` and `post_max_size`) is:

- **128 MB:** Single 125k visits and below, Single 65 GB bandwidth and below, WP 2, Launch, Launch Plus, Build, and Expand.
- **256 MB:** Single 315k visits and above, Single 125 GB bandwidth and above, WP 5 and above, Scale, and Lead.
- **Dedicated servers:** The limit can be increased to 500 MB. [Contact Support](https://kinsta.com/docs/support/contact-support/) to change it.

If you need to upload files larger than your limit, use one of the options below.

- **Upload large files another way:** Upload large files, such as videos, backups, or import files, over [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/) instead of through the browser. For WordPress media, you can then add them to the Media Library with [WP-CLI](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-wp-cli/) (`wp media import`).
- **Reduce the file size:** Compress images and videos, or split large import files into smaller ones.
- **Large database imports:** Use WP-CLI as described in [Import MySQL Database](https://kinsta.com/docs/wordpress-hosting/database-management/restore-import-mysql-database/).
- **Third-party CDN:** If you use another CDN or proxy, it may have a lower size limit than Kinsta. Check its upload limit.

## 429 Too Many Requests

A 429 Too Many Requests error means too many requests came from the same source in a short time, so your site’s web server temporarily limited them. Requests over the limit are rejected until the rate drops, and other visitors aren’t affected.

Your site’s [error.log](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/#error-log) records each limited request as `limiting requests, excess: ... by zone "phpzone"`.

- **Bots and scrapers:** Automated traffic crawling many pages quickly is the most common cause. Use the [Top traffic report in Bot protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#top-traffic) to find the source, then block it or raise your protection level.
- **Plugins and integrations:** Tools that sync, import, or check your site can send bursts of requests, for example to `admin-ajax.php` or the WordPress REST API. Reduce how often they run, or set them to send requests in smaller batches.
- **Load testing:** Tools that simulate heavy traffic from one source are rate-limited quickly. Load testing isn’t allowed on Kinsta; for more information, see our [Terms of Service](https://kinsta.com/legal/terms-service/#h-5-acceptable-use-policy-and-protection-of-the-services).

If legitimate traffic is being limited, [contact Support](https://kinsta.com/docs/support/contact-support/) with the time of the errors and the IP address or tool involved.

## 451 Unavailable For Legal Reasons

A 451 Unavailable For Legal Reasons error means access to the page was blocked to comply with a law or legal order. This error usually doesn’t come from your site or from Kinsta.

- **Visitors in one country see the error:** Their internet service provider or government is most likely blocking your site at the network level. Your site is still working, visitors in other locations can still reach it, and there’s nothing to change in MyKinsta or WordPress.
- **A plugin blocks visitors by location:** Some plugins restrict access from certain countries for privacy or legal compliance and return a 451. Check your plugins’ settings, or deactivate them one at a time to find the one responsible.

If you blocked a country yourself with a bot protection exception, visitors from that country see a 403, not a 451; see [403 Forbidden](#403-forbidden).

## 499 Client Closed Request

Visitors never see a 499. It’s recorded in your site’s [access.log](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/#access-log) when the visitor’s browser, or another service connecting to your site, closes the connection before your site finishes responding.

- **A few 499s are normal:** They’re logged whenever a visitor closes a tab, clicks away, or stops a page from loading.
- **499s with a request time of about 180 seconds:** The request reached the 180-second limit, Cloudflare closed the connection, and the visitor saw a 524 timeout error. Treat these as timeouts; see [504 Gateway Timeout Error](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/server-errors/#504-gateway-timeout-error).
- **Many 499s from the same tool:** An uptime monitor, integration, or other service may have a shorter timeout than your site needs to respond. Check the tool’s timeout setting, or use [Kinsta’s APM tool](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/) to find out why the request is slow.
