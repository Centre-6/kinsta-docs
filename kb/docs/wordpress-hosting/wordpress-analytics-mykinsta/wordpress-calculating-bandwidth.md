---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/wordpress-calculating-bandwidth/"
title: "Analytics - Calculating Server Bandwidth"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-analytics-mykinsta"
section: []
kinsta_last_updated: "March 9, 2026"
sitemap_lastmod: "2026-03-09T10:54:04+00:00"
fetched_at: "2026-10-07T22:39:42Z"
sha256: "3f3aebab057541f28631b7092b101adbbe07b1bb97bd7803613603501472a220"
body_chars: 5178
extracted_with: "main article"
status: "live"
---

# Analytics - Calculating Server Bandwidth

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/wordpress-calculating-bandwidth/
**Kinsta last updated:** March 9, 2026

## On this page

- [What is a request, and what data is transferred?](#what-is-a-request-and-what-data-is-transferred)
- [What is excluded?](#what-is-excluded)
- [How do I view my server bandwidth usage?](#how-do-i-view-my-server-bandwidth-usage)
- [How can I reduce the amount of bandwidth consumed?](#how-can-i-reduce-the-amount-of-bandwidth-consumed)
  - [Optimize images and media](#optimize-images-and-media)
  - [Use caching](#use-caching)
  - [Use a Content Delivery Network (CDN)](#use-a-content-delivery-network-cdn)
  - [Minify and Combine Files](#minify-and-combine-files)
  - [Limit or Replace Heavy Plugins](#limit-or-replace-heavy-plugins)

---

At Kinsta, you can choose a hosting plan based on the total number of [monthly visits to your sites](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/counting-visits/) or the total monthly server bandwidth used by your sites. Server bandwidth is measured in bytes and reflects the amount of data your site’s data center sends in response to requests. Only data delivered directly from the server is counted; anything served by a [CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/) or [edge cache](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/) is excluded.  Server bandwidth is shared across all sites on your WordPress Hosting plan.

## What is a request, and what data is transferred?

A request to your website happens whenever a browser or an app asks your server for information so it can load or interact with your site. Each request is essentially a message from the client (the visitor’s browser or tool) to your server asking for a specific resource.

When a visitor loads your site, their browser may send multiple requests to your server. For example, a single page load might generate requests for:

- The main HTML file that structures the page
- CSS stylesheets that control the design
- JavaScript files that add functionality
- Images, videos, or other media assets
- API calls to fetch dynamic data

In response, your server sends back the requested resources. What the server delivers, such as the page itself, an image, or a file, is the data transferred.

This data transfer is measured in bytes. However, the size of the file on disk is not always equal to the amount of bandwidth used to deliver it. Modern servers typically compress responses before sending them, and web browsers automatically decompress them once received. For example, an HTML file that is 80 KB in size might only use 40 KB of bandwidth after compression during transfer.

Every element of a page requires its own request; therefore, a single visit to your site can result in multiple requests, each contributing to the total bandwidth consumed.

## What is excluded?

The following are excluded from the server bandwidth usage:

- Requests served from the [CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/) or [Edge Cache](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/).
- Requests to the `wp-login.php` page.
- We filter out traffic from common bots and any user agent that signals it’s a bot or crawler.

## How do I view my server bandwidth usage?

You can view your site’s bandwidth usage within **Analytics** > **Bandwidth**. This chart is split into Server, CDN, and edge bandwidth. You can also view how much of your plan’s bandwidth you’ve used within **Plan usage**.

![Bandwidth chart in Analytics.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-analytics-bandwidth.png)

Bandwidth chart in Analytics.

You can also identify which requests consume the most server bandwidth on your sites with the **Top requests by server bandwidth** report, within **Analytics** > **Top requests**.

![Top requests by server bandwidth report in Analytics.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-top-requests-server.png)

Top requests by server bandwidth report in Analytics.

## How can I reduce the amount of bandwidth consumed?

Unlike visits, which you have no control over, you can control the amount of bandwidth your site uses by sending fewer requests and making each request smaller.

You can look at the **Top requests by server bandwidth** report to see which requests are consuming the most bandwidth and consider the following to optimize your site and reduce your overall bandwidth:

### Optimize images and media

- Compress your images to reduce their size.
- Serve modern formats like WebP or AVIF instead of JPG/PNG where possible.
- Lazy load images and videos so they only load when a visitor scrolls to them.
- Host large media (e.g., videos) on platforms like YouTube, Vimeo, or a CDN.

### Use caching

- [Edge caching](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/) delivers content from the server location closest to the client and is not included in the server bandwidth.

### Use a Content Delivery Network (CDN)

- [Kinsta’s CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/) is **enabled by default** on all new sites here at Kinsta.
- A CDN caches and serves your site’s static content (images, CSS, JS) from servers around the world.
- This reduces the bandwidth used on your site’s data center and speeds up load times for visitors.
- Check out our in-depth post on the [benefits of a WordPress CDN](https://kinsta.com/blog/wordpress-cdn/) and why you should use one.

### Minify and Combine Files

- Minify CSS, JavaScript, and HTML to remove unnecessary characters and whitespace.
- Combine smaller files where possible to reduce the total number of requests.

### Limit or Replace Heavy Plugins

- Some plugins load large scripts or unnecessary assets. Audit your plugins and remove or replace any that cause excessive requests.
- Use lightweight themes and plugins optimized for performance.
