---
url: "https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/early-hints/"
title: "Tools - Early Hints"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "mykinsta-tools"
section: []
kinsta_last_updated: "August 5, 2025"
sitemap_lastmod: "2025-08-05T12:37:53+00:00"
fetched_at: "2026-10-07T22:37:31Z"
sha256: "9c2817514d89508f69aa0941249bbc258a567c0d866c533862583f301c1c16dd"
body_chars: 5646
extracted_with: "main article"
status: "live"
---

# Tools - Early Hints

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/early-hints/
**Kinsta last updated:** August 5, 2025

## On this page

- [Set up Early Hints on your WordPress site](#set-up-early-hints-on-your-wordpress-site)
- [Important notes](#important-notes)
- [Enable Early Hints in Cloudflare](#enable-early-hints-in-cloudflare)
- [Enable Early Hints in MyKinsta](#enable-early-hints-in-mykinsta)
- [Test Early Hints](#test-early-hints)
- [Disable Early Hints](#disable-early-hints)

---

Early Hints is a [web standard](https://httpwg.org/specs/rfc8297.html) you can implement to improve page load times by up to 30%. This web standard defines a new [HTTP status code](https://kinsta.com/blog/what-is-an-http-request/): 103 Early Hints.

When the [Early Hints](https://blog.cloudflare.com/early-hints/) feature is enabled, and a visitor loads your site in a compatible browser, 103 responses are sent to the browser (before 200 responses) with information about linked assets that may appear in the final response from the server. With this information, the browser can begin preparing the page before it receives the [200 OK response](https://kinsta.com/blog/http-status-codes/#200-status-codes) from the server. This allows the browser to more efficiently prepare the page for loading while the server is “thinking.”

The Early Hints mechanism can be used with any type of Link header or resource hint, such as `preload` and `preconnect`. It helps improve web page performance by allowing browsers to start fetching or preparing resources before the final response is received.

As part of [Kinsta’s Cloudflare integration](https://kinsta.com/blog/cloudflare-integration/), Early Hints can be enabled for your WordPress site in MyKinsta for your custom domain. You cannot use Early Hints with a temporary kinsta.cloud domain.

## Set up Early Hints on your WordPress site

Early Hints is designed to enhance the performance benefits of resource hints like `preload` and `preconnect` by sending these directives to the browser before the final server response is ready. This allows the browser to begin loading or connecting to critical resources earlier, improving page load times and user experience.

- `Preload`: The `preload` directive tells the browser to fetch important resources (e.g., CSS, JavaScript, fonts) as early as possible. When used with Early Hints, these `preload` instructions are delivered immediately after the initial request, allowing the browser to start downloading critical assets even before the full response is received. This reduces render-blocking time and improves perceived and actual performance.
- `Preconnect`: The `preconnect` directive initiates early connections to important third-party domains (e.g., analytics, CDN, APIs). Early Hints sends these `preconnect` signals upfront, enabling the browser to perform DNS lookups, TCP handshakes, and TLS negotiations in advance. This reduces connection latency and speeds up resource loading from external origins.

To take advantage of Early Hints, you must first configure `preload` and `preconnect` properly by adding the appropriate `Link:` headers to the desired assets on your WordPress site. This can be done using optimization plugins such as:

- [WP Rocket](https://wp-rocket.me/)
- [Perfmatters](https://perfmatters.io/)

These tools allow you to easily define and manage `preload` and `preconnect` headers without editing code manually.

## Important notes

1. You must enable the `Link:` response header with either the `preload` or `preconnect`[rel type](https://blog.cloudflare.com/early-hints/#now-turning-200-ok-link-headers-into-103-early-hints) to indicate the resources you want to include in the Early Hints response. You can use a WordPress plugin to add `preload` or `preconnect` headers to your assets in WordPress.
2. The 103 Early Hints status code is compatible with the latest versions of Chrome, Edge, Safari, and Firefox. If a browser doesn’t support Early Hints and a 103 response header is sent to it, nothing will happen; the browser will simply ignore it.
3. If your site has more than 20 domains, enabling Early Hints may take 5 or more minutes, depending on the total number of domains.
4. You cannot use Early Hints with a temporary kinsta.cloud domain.

## Enable Early Hints in Cloudflare

Within your Cloudflare account, select your domain and click **Speed** > **Optimization** > **Content Optimization** and toggle **Early Hints** on.

![Enable Early Hints within Cloudflare.](https://kinsta.com/wp-content/uploads/2023/11/cloudflare-enable-early-hints.png)

Enable Early Hints within Cloudflare.

## Enable Early Hints in MyKinsta

1. To enable Early Hints, log in to [MyKinsta](https://my.kinsta.com/) and go to**Sites** > ***sitename*** > **Tools**.
2. Under **Early Hints**, click the **Enable** button.

![Enable Early Hints in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/06/wordpress-tools-early-hints.png)

Enable Early Hints in MyKinsta.

A notification that Early Hints is enabled will appear in the upper-right corner.

## Test Early Hints

To confirm Early Hints is working, inspect the HTTP headers of a page on your site, and look for any `Link:` headers with the `rel` type of `preload` or `preconnect` that you added. To inspect your site’s HTTP headers, you can use any of the following:

- Our free [HTTP status and redirect checker](https://kinsta.com/tools/redirect-checker/).
- Your web browser’s built-in developer tools.
- The `curl` command in Terminal (command line), substituting the URL at the end of this example with the URL of the page you want to test:

Copy

```
curl -L -s -o /dev/null -D - https://kinstaexample.com
```

## Disable Early Hints

1. To disable Early Hints, log in to [MyKinsta](https://my.kinsta.com/) and go to**Sites** > ***sitename*** > **Tools**.
2. Under **Early Hints**, click the **Disable** button.

![Disable Early Hints in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/06/wordpress-tools-early-hints-disable.png)

Disable Early Hints in MyKinsta.

A notification that Early Hints is disabled will appear in the upper-right corner.
