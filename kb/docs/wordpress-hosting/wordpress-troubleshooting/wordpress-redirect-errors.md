---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/wordpress-redirect-errors/"
title: "Redirect Errors"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-troubleshooting"
section: ["WordPress Hosting", "Troubleshooting"]
kinsta_last_updated: "2026-11-02T18:15:06"
change_signal: "2026-11-02T18:15:06"
fetched_at: "2026-11-11T13:03:01Z"
sha256: "fe7d442d2cd27d78238d2dfc5cf39aa9328c2df46e4f4035437e93b4a288e667"
body_chars: 8472
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Redirect Errors

**Section:** WordPress Hosting > Troubleshooting
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/wordpress-redirect-errors/
**Kinsta last updated:** 2026-11-02T18:15:06

## On this page

- [Redirect status codes](#redirect-status-codes)
  - [301 Moved Permanently](#301-moved-permanently)
  - [302 Found](#302-found)
  - [304 Not Modified](#304-not-modified)
- [Too many redirects](#too-many-redirects)
  - [Find the two addresses that loop](#find-the-two-addresses-that-loop)
  - [HTTP and HTTPS loops](#http-and-https-loops)
  - [www and non-www loops](#www-and-non-www-loops)
  - [Conflicting redirect rules](#conflicting-redirect-rules)
  - [Plugins](#plugins)
  - [If our monitoring reports a loop but your site loads](#if-our-monitoring-reports-a-loop-but-your-site-loads)
  - [After you fix the loop](#after-you-fix-the-loop)
  - [When to contact Support](#when-to-contact-support)

---

## Redirect status codes

Status codes starting with 3 aren’t errors on their own. They tell the browser that the content it asked for is somewhere else, or that it hasn’t changed since the browser last loaded it. You’ll see them in your site’s [access.log](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/#access-log) and when you trace a URL with `curl -IL`. They only need attention when they send visitors to the wrong place or repeat in a loop.

### 301 Moved Permanently

A 301 redirect tells browsers and search engines that a page has moved for good. Your site uses them for HTTPS, for your primary domain (with or without `www.`), and for adding a trailing slash to folder URLs, and you can add your own with [redirect rules](https://kinsta.com/docs/wordpress-hosting/redirect-rules/).

Browsers remember 301 redirects, so if you change or remove one, clear your browser’s cache or test in a private window to see the new behavior. If a URL passes through several 301s before it loads, point the first redirect straight at the final URL.

### 302 Found

A 302 redirect is temporary, so browsers and search engines don’t remember it. WordPress and plugins use them for things that change from visit to visit, such as sending logged-out users from `/wp-admin/` to the login page, redirecting after a form is submitted, or sending visitors to a language or country version of a page.

If a page has moved for good, use a 301 instead, so search engines update their records and pass the old page’s ranking to the new one.

### 304 Not Modified

A 304 isn’t a redirect. It means the visitor’s browser already has a copy of the file, and your site confirmed it hasn’t changed, so the browser reuses its copy instead of downloading it again. Seeing 304s in your access.log is normal, and it means caching is working.

If you’ve changed a file but visitors still see the old version, [clear your site’s cache](https://kinsta.com/docs/wordpress-hosting/caching/#clear-cache-in-mykinsta) and any [CDN cache](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#clear-cdn-cache-in-mykinsta).

## Too many redirects

A “too many redirects” error means a page keeps redirecting instead of loading. Usually two settings point at each other: one sends visitors to address A, the other sends them back to address B, and the browser gives up after a set number of attempts. Browsers show this as **ERR_TOO_MANY_REDIRECTS** or a message such as “redirected redirected you too many times.”

A redirect loop almost always comes from your site’s configuration, not from a temporary problem, so it won’t clear up on its own. It often starts right after a change to SSL, domains, a CDN, or redirect rules.

### Find the two addresses that loop

Tracing the redirects shows which two addresses the request bounces between, which points to the cause.

1. Run `curl -IL https://yourdomain.com` in a terminal, or enter your URL in an online redirect checker.
2. Look at the `Location` value in each response. These are the addresses the request is sent to.
3. Compare the addresses that repeat:
   - Only `http://` and `https://` differ: see HTTP and HTTPS loops.
   - Only `www.` differs: see www and non-www loops.
   - The paths differ, such as `/shop/` and `/store/:` see Conflicting redirect rules.

If you can’t run these checks, start with whatever you changed most recently.

### HTTP and HTTPS loops

This is the most common type of redirect loop. One layer sends visitors to `https://`, and another sends the request back to `http://`.

1. **Your own Cloudflare account set to Flexible SSL:** If you use your own [Cloudflare](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/cloudflare/) account in front of Kinsta, check the SSL/TLS encryption mode in your Cloudflare dashboard. In Flexible mode, Cloudflare connects to your site over HTTP, and your site redirects that request to HTTPS, which repeats forever. Change the mode to **Full (strict)**; your Kinsta site already has an [SSL certificate](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/).
2. **Another CDN or proxy:** If you use another [third-party CDN or proxy](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/proxy-cdn-compatibility-checklist/), make sure it connects to Kinsta over HTTPS, not HTTP. If [Force HTTPS](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/#force-https) is enabled in MyKinsta and you’re not sure which layer is causing the loop, temporarily disable Force HTTPS to test.
3. **A redirect from HTTPS to HTTP:** Check your [redirect rules](https://kinsta.com/docs/wordpress-hosting/redirect-rules/) and plugins for anything that sends visitors from `https://` to `http://` and remove it.

### www and non-www loops

One setting sends visitors to `www.example.com`, and another sends them back to `example.com`. This usually happens after a migration or domain change.

1. Decide which version of your domain is the main one: with or without `www`.
2. In MyKinsta, make sure that version is set as your site’s [primary domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/#2-set-your-domain-as-primary).
3. In WordPress, go to **Settings** > **General** and make sure the **WordPress Address (URL)** and **Site Address (URL)** both use that exact version, including `https://`.
4. If those fields are greyed out, the URLs are set in `wp-config.php` with `WP_HOME` and `WP_SITEURL`, which override the dashboard settings. Update them there.

If you can’t reach the WordPress dashboard, check and update the URLs with [WP-CLI](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-wp-cli/): `wp option get siteurl` and `wp option get home` show the current values, and `wp option update` changes them.

### Conflicting redirect rules

Two redirect rules point at each other, often because the same redirect is set in more than one place. Check each place redirects can be set, and keep each redirect in only one of them:

- [Redirect rules in MyKinsta](https://kinsta.com/docs/wordpress-hosting/redirect-rules/).
- Redirect plugins in WordPress.
- Page rules or redirect rules in a third-party CDN, such as your own Cloudflare account.

### Plugins

SSL, redirect, security, and caching plugins can each add their own redirects, which can conflict with each other or with your server settings. If the loop started after you installed, updated, or changed the settings of a plugin, deactivate it. If you can’t reach the WordPress dashboard, deactivate it with [WP-CLI](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-wp-cli/) (`wp plugin deactivate plugin-name`) or by renaming its folder over [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/).

If Force HTTPS is enabled in MyKinsta, a plugin that also forces HTTPS is unnecessary and is a common source of loops. Use one or the other, not both.

### If our monitoring reports a loop but your site loads

Kinsta’s [uptime monitoring](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/uptime-monitoring/) checks your site the way a new visitor would, without cookies or a saved session. If you got a redirect alert but your site loads normally in your browser, the loop may only affect first-time visitors:

- **Cookie-based redirects:** Language or location redirects, age checks, and cookie consent pages can redirect visitors until a cookie is set. Visitors who block cookies, as well as search engines and monitoring tools, can get stuck in a loop.
- **Your own browser:** Open your site in a private or incognito window to see it as a new visitor would.

### After you fix the loop

Browsers save permanent (301) redirects, so the error can keep appearing in your browser after the cause is fixed.

1. [Clear your site’s cache](https://kinsta.com/docs/wordpress-hosting/caching/#clear-cache-in-mykinsta) in MyKinsta, and any [CDN cache](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#how-to-clear-kinstas-cdn-cache).
2. Clear your browser’s cache and cookies for your site, or test in a private or incognito window.

### When to contact Support

If you can’t find the cause, or the loop continues after you’ve checked these settings, [contact Support](https://kinsta.com/docs/support/contact-support/) with the URL, the output of curl -IL or your redirect checker, and any changes you made recently.
