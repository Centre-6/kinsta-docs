---
url: "https://kinsta.com/changelog/kinsta-cdn-cloudflare/"
title: "Kinsta CDN Is Now Powered by Cloudflare"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2021-07-13T10:44:40"
change_signal: "2021-07-13T10:44:40"
fetched_at: "2026-10-07T22:58:23Z"
sha256: "686f518854beda22c961ac4d629e799f275d9406c374a9ca405b705c563f6e9e"
body_chars: 6359
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Kinsta CDN Is Now Powered by Cloudflare

**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-cdn-cloudflare/
**Kinsta last updated:** 2021-07-13T10:44:40

## On this page

- [Why Your Site Needs a CDN](#why-your-site-needs-a-cdn)
- [Introducing the New Kinsta CDN (Now Powered by Cloudflare)](#introducing-the-new-kinsta-cdn-now-powered-by-cloudflare)
  - [Larger CDN Network With 200+ PoPs](#larger-cdn-network-with-200-pops)
  - [No Secondary CDN Domain Needed](#no-secondary-cdn-domain-needed)
  - [Up to 40% Improved CDN Performance](#up-to-40-improved-cdn-performance)
- [How to Enable the New Kinsta CDN in MyKinsta](#how-to-enable-the-new-kinsta-cdn-in-mykinsta)
- [Summary](#summary)

---

Earlier in 2021, we announced a [free Cloudflare integration](https://kinsta.com/cloudflare-integration/) for all sites hosted on Kinsta. The first phase of our Cloudflare integration brought a variety of security enhancements such as an enterprise-level firewall, free [DDoS](https://kinsta.com/blog/what-is-a-ddos-attack/) protection, [HTTP/3](https://kinsta.com/blog/http3/) support, and more.

Today, we’re excited to kick off the next phase of our Cloudflare integration and finally release our brand new implementation of [Kinsta CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#kinstas-cdn), now powered by Cloudflare’s global edge network.

## Why Your Site Needs a CDN

In 2026, a content delivery network (CDN) is a [must-have for your WordPress site](https://kinsta.com/blog/wordpress-cdn/). A CDN works by caching static assets like [images](https://kinsta.com/blog/image-file-types/), [CSS](https://kinsta.com/blog/wordpress-css/) and JS files, [web fonts](https://kinsta.com/blog/local-fonts/), and more in [data centers](https://kinsta.com/docs/service-information/data-center-locations/) around the world.

This allows static assets to be served from locations that are closer to your visitor. Since static assets typically account for the majority of total page size, serving them from a CDN can increase site performance significantly.

## Introducing the New Kinsta CDN (Now Powered by Cloudflare)

Kinsta CDN is a high-performance content delivery network that can be **enabled on** [**all Kinsta plans**](https://kinsta.com/pricing/) **at no additional cost**.

Let’s take a look at what’s new!

### Larger CDN Network With 200+ PoPs

Until today, Kinsta CDN was powered by KeyCDN, a popular CDN provider with 40+ points of presence (PoPs) around the world. Compared to KeyCDN, Cloudflare’s global network spans over 200 cities.

This means with the new Kinsta CDN powered by Cloudflare, your images, fonts, and other static assets will live closer to your visitors.

### No Secondary CDN Domain Needed

Points of presence is not the only differentiating factor between Cloudflare CDN and KeyCDN. The previous version of Kinsta CDN, which was powered by KeyCDN, required customers to use randomly generated custom domains to serve static assets from.

While this CDN configuration doesn’t cause any SEO-related penalties, many of our customers expressed interest in a cleaner CDN solution that doesn’t require a secondary domain.

With the new Kinsta CDN powered by Cloudflare, your site will no longer need to serve static assets via a secondary CDN domain (kinstalife.kinstacdn.com/image.jpg). Instead, all static assets will be cached and served via your site’s primary domain (kinstalife.com/image.jpg).

### Up to 40% Improved CDN Performance

At Kinsta, we are always looking for new ways to make our [high-performance hosting stack](https://kinsta.com/wordpress-hosting/) even faster. Thanks to the new Kinsta CDN, customers can expect to see a boost in performance for site visitors that are far away from the origin server.

To compare the before vs after performance of our Kinsta CDN, we ran a series of speed tests from 10 locations around the world.

For these benchmark tests, we set up duplicate WordPress sites with a variety of CSS, JS, [fonts](https://kinsta.com/blog/wordpress-fonts/), images, and other static assets. We enabled KeyCDN on one site, and the new Kinsta CDN powered by Cloudflare on the other site.

Here are the results!

|  |  |  |  |
| --- | --- | --- | --- |
| **Location** | **KeyCDN (seconds)** | **Cloudflare CDN (seconds)** | **Percent Change** |
| Frankfurt | 2.89 | 2.19 | -24.22% |
| Amsterdam | 2.77 | 1.70 | -38.63% |
| London | 2.60 | 1.55 | **-40.38%** |
| New York | 1.03 | 0.835 | -18.93% |
| Dallas | 1.29 | 0.849 | -34.19% |
| San Francisco | 1.75 | 1.20 | -31.43% |
| Singapore | 4.30 | 3.41 | -20.70% |
| Sydney | 4.45 | 3.95 | -11.24% |
| Tokyo | 3.23 | 2.18 | -32.51% |
| Bangalore | 5.40 | 4.82 | -10.74% |

As you can see, Cloudflare performed between 10% up to a **whopping 40% faster in all ten locations around the world**! The biggest improvements can be seen in London where page load time dropped from 2.6 seconds to 1.55 seconds.

## How to Enable the New Kinsta CDN in MyKinsta

To enable the new Cloudflare-powered Kinsta CDN, log in to [MyKinsta](https://kinsta.com/mykinsta/) and go to **Sites > Your Site > Kinsta CDN**, and click **Enable Kinsta CDN**.

![Enable Kinsta CDN in MyKinsta.](https://kinsta.com/wp-content/uploads/2021/07/mykinsta-enable-kinsta-cdn.jpg)

Enable Kinsta CDN in MyKinsta.

Next, confirm the zone creation by clicking **Enable Kinsta CDN** on the popup dialog box.

![Confirm Kinsta CDN deployment.](https://kinsta.com/wp-content/uploads/2021/07/mykinsta-enable-kinsta-cdn-confirmation.jpg)

Confirm Kinsta CDN deployment.

Enabling Kinsta CDN should only take a few seconds. After Kinsta CDN has been enabled, you should see a green checkmark.

On the Kinsta CDN page, you should see two additional buttons:

![Kinsta CDN settings in MyKinsta.](https://kinsta.com/wp-content/uploads/2021/07/disable-clear-cdn-cache.jpg)

Kinsta CDN settings in MyKinsta.

1. **Disable** – click this button to disable Kinsta CDN.
2. **Clear CDN Cache** – click this button to flush the CDN cache. Clearing the CDN cache is a good first troubleshooting step if you see discrepancies on the frontend of your site. For example, if you make some changes to your CSS but don’t see the changes on the frontend, it’s possible that the old CSS file is cached. In this situation, you can clear the CDN cache during your troubleshooting process.

## Summary

We’re thrilled to release the new Kinsta CDN and make Cloudflare’s global CDN network available for all our customers. After introducing security features like an enterprise-level firewall and industry-leading DDoS protection in the [first phase of our Cloudflare integration](https://kinsta.com/blog/cloudflare-integration/#what-is-the-timeline-for-kinstas-cloudflare-integration), our Kinsta CDN migration from KeyCDN marks the first step towards the new and exciting performance enhancements we’ve planned throughout the year.

To stay up to date with upcoming Cloudflare integration developments, be sure to [subscribe to our newsletter](https://kinsta.com/wordpress-newsletter/)!
