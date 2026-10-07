---
url: "https://kinsta.com/changelog/edge-caching/"
title: "New Edge Caching Feature Slashes Page Load Times"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "New Edge Caching Feature Slashes Page Load Times"]
kinsta_last_updated: "2024-02-13T15:02:36+00:00"
sitemap_lastmod: "2024-02-13T15:02:36+00:00"
fetched_at: "2026-10-07T22:36:48Z"
sha256: "9b1dc1707d905dc105f47ffbba9c9a89050c1115c4e08a82b86aebd0f9631d37"
body_chars: 8921
extracted_with: "main article"
status: "live"
---

# New Edge Caching Feature Slashes Page Load Times

**Section:** Changelog > New Edge Caching Feature Slashes Page Load Times
**Product:** Changelog
**Source:** https://kinsta.com/changelog/edge-caching/
**Kinsta last updated:** 2024-02-13T15:02:36+00:00

## On this page

- [Introducing Edge Caching](#introducing-edge-caching)
- [Take Control of Edge Caching](#take-control-of-edge-caching)
  - [Mobile Content? Edge Caching Has That Covered](#mobile-content-edge-caching-has-that-covered)
- [Easily Manage Your Cached Content](#easily-manage-your-cached-content)
- [Opting Out of Edge Caching](#opting-out-of-edge-caching)
- [Are You Ready For Edge Caching?](#are-you-ready-for-edge-caching)
- [It’s All About Speed](#its-all-about-speed)

---

Updated
:   February 13, 2024

![Edge Caching Feature Update](https://kinsta.com/wp-content/uploads/2022/12/New-Edge-Caching_Feature_Updates_EN-1024x536.jpg)

Picture this: Your WordPress site is hosted in one of [Kinsta’s North American data centers](https://kinsta.com/docs/service-information/data-center-locations/). Your next visitor is at home in Germany. But instead of traveling halfway around the globe, your site’s pages are delivered to that user at lightning speed from a nearby European server.

How’s that possible? That’s the magic of [Edge Caching](https://kinsta.com/blog/edge-caching/), Kinsta’s newest feature for [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/) customers, with the capability to dramatically reduce the time it takes for your website’s pages to be delivered to browsers around the world. In fact, during Beta testing by Kinsta customers in 2022, we saw Edge Caching cut the time needed to serve cached WordPress HTML by an average of more than 50%.

And Edge Caching is now **available at no additional cost** everywhere.

## Introducing Edge Caching

When we first announced our [Cloudflare integration timeline](https://kinsta.com/blog/cloudflare-integration/#what-is-the-timeline-for-kinstas-cloudflare-integration), we promised to build and deliver unmatched managed WordPress hosting solutions leveraging that platform.

We began by integrating Cloudflare security features to provide firewalls and protection from DDoS attacks. Next, we adopted Cloudflare’s content delivery network for [Kinsta’s CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#kinstas-cdn) to place your static assets — like images and files containing CSS, JavaScript, and fonts — in 300+ locations around the globe.

Now, with the release of Edge Caching, pages cached in your site’s local data center are distributed across that same network, delivering that cached HTML worldwide — practically to your visitors’ doorsteps.

This is in addition to the static assets you may be serving up through Kinsta’s CDN. Edge Caching can deliver your site’s pages to your visitors faster and reduce the number of requests that need to be handled by the server in your chosen data center.

Edge caching does for the HTML of pages what Kinsta’s CDN does for those static assets.

In hundreds of tests during our Edge Caching Beta period, the average time required to serve a cached page from an edge server was about one-quarter of a second, compared with nearly a half second to get pages to the same browsers from the test sites’ local data center caches. (And you can compare that to the average of nearly two seconds required when there were no caches at all.)

Not surprisingly, performance improvements were the most dramatic when the distance between the browser and the origin server’s data center was greatest. We saw some delivery times for cached pages drop by more than 80% between North America and our data centers in Australia and Asia.

And most Kinsta customers won’t have to lift a finger to take site performance up another notch with Edge Caching.

## Take Control of Edge Caching

With the service’s launch, Edge Caching is enabled by default on new WordPress websites created in the [MyKinsta dashboard](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/new-site/). Starting in January 2023, we will automatically update existing sites that are candidates for Edge Caching and enable the service.

If you’d like to take advantage of edge caching for an existing site right away, enable it in MyKinsta by following these steps:

- Select **WordPress Sites** on the left-hand navigation.
- Select the name of a site for which you want Edge Caching enabled.
- Select **Edge Caching**.
- Click on the **Enable Edge Caching** button.

![Screenshot: Enabling Edge Caching in the MyKinsta dashboard.](https://kinsta.com/wp-content/uploads/2022/12/edge-caching-enable-with-opt-out-feature-update.png)

Enabling Edge Caching in the MyKinsta dashboard.

Edge caching is available for all live WordPress sites and [premium staging environments](https://kinsta.com/docs/wordpress-hosting/staging-environment/#premium-staging-environments).

### Mobile Content? Edge Caching Has That Covered

If your website detects mobile browsers and generates pages with markup unique to those devices, you can enable a mobile cache separate from the content for desktop users.

When Edge Caching is enabled, you can flip the switch on mobile caching in MyKinsta here:

- Select **WordPress Sites** on the left-hand navigation.
- Select the name of a site for which Edge Caching is enabled.
- Select **Edge Caching**.

![Screenshot: Enabling Edge Caching for mobile content.](https://kinsta.com/wp-content/uploads/2022/12/enable-mobile-edge-caching-feature-update.png)

Enabling Edge Caching for mobile devices.

Click the **Enable Mobile Cache** button to take advantage of Edge Caching for mobile devices.

Note that you don’t need to enable mobile caching if your website design supports both desktop and mobile browsers with the same responsive HTML/CSS markup.

## Easily Manage Your Cached Content

You also have the power to manage the global cache of your site’s pages. Clearing cached pages can ensure that your latest content updates are immediately visible to your visitors.

If you’re familiar with [clearing cached content](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/#manage-and-clear-cache-in-your-wordpress-dashboard) within the dashboard of your WordPress site, you already know how to refresh your local site cache and, now, the global edge cache.

Additionally, MyKinsta allows you to target the edge cache directly with just a few clicks. When Edge Caching is enabled, you’ll find this capability in MyKinsta here:

- Select **WordPress Sites** on the left-hand navigation.
- Select the name of a site for which Edge Caching is enabled.
- Select **Edge Caching**.

![Screenshot: Clearing edge-cached content in the MyKinsta dashboard.](https://kinsta.com/wp-content/uploads/2022/12/clear-edge-caches-feature-update.png)

Clearing the edge caches in the MyKinsta dashboard.

To clear all of your site’s pages from the global edge cache, click the **Clear Cache** button.

If you need to clear only specific pages or paths, paste a target URL in the **Clear URL Cache** field and click the **Clear URL Cache** button. Clear the cache for all content on a specific path by checking the option to **Clear cache of every subdirectory under the specified URL**.

## Opting Out of Edge Caching

If you know Edge Caching isn’t going to be a fit for your website, you can opt-out before we begin enabling the service for most existing sites in January of 2023.

In MyKinsta:

- Select **WordPress Sites** on the left-hand navigation.
- Select the name of your WordPress site.
- Select **Edge Caching**.
- Enable the “**I want to opt-out…**” toggle.

![Screenshot: Opting out of automatic enabling of Edge Caching.](https://kinsta.com/wp-content/uploads/2022/12/edge-caching-opting-out-feature-update.png)

Opting out of Edge Caching using the MyKinsta dashboard.

At any time, if Edge Caching is already enabled for a website, you’ll find a **Disable** button in the upper-right corner of the page, above the cache-clearing controls:

![Screenshot: Disabling all Edge Caching, or just mobile Edge Caching.](https://kinsta.com/wp-content/uploads/2022/12/disable-edge-caching-feature-update.png)

Disabling Edge Caching in MyKinsta.

The **Disable** Edge Caching button will also disable any mobile caching. Alternatively, you can disable mobile caching independently.

## Are You Ready For Edge Caching?

Site content that is already problematic for a local site cache is also a poor candidate for Edge Caching. Examples include sites that generate unique content based on a visitor’s exact geographic location.

A caching configuration that relies on cookies and targeted URLs for custom exclusions might not be compatible with Edge Caching.

But don’t miss out just because you are not sure! Contact Kinsta Support for answers to your questions about Edge Caching.

## It’s All About Speed

As a Kinsta customer, your website is already hosted on Google’s fastest C2 or [C3D machines](https://kinsta.com/blog/wordpress-performance-benchmarks/) on its Premium Tier network. You might already be taking advantage of Kinsta’s CDN to speed up the delivery of your site’s static assets. Now, Edge Caching offers yet another tool to optimize your site for speed.

Edge Caching is available to all Kinsta customers in all [hosting plans](https://kinsta.com/pricing/). If you’re not yet a customer, learn how our Managed WordPress Hosting works by [scheduling a demo](https://kinsta.com/talk-to-sales/).

[Subscribe to our newsletter](https://kinsta.com/wordpress-newsletter/) to be the first to hear about Kinsta’s latest feature releases.
