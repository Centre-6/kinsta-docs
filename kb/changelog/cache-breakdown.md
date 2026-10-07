---
url: "https://kinsta.com/changelog/cache-breakdown/"
title: "A new view of cache performance for your WordPress site"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-04-05T15:11:44"
change_signal: "2026-04-05T15:11:44"
fetched_at: "2026-10-07T22:58:21Z"
sha256: "85d6fb0805571d61f62b1d35530ba361863c87e7dbe368ecb82df94d85cdc89b"
body_chars: 2169
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# A new view of cache performance for your WordPress site

**Product:** Changelog
**Source:** https://kinsta.com/changelog/cache-breakdown/
**Kinsta last updated:** 2026-04-05T15:11:44

---

We’ve updated website analytics reporting in MyKinsta to provide a better picture of cache performance, all the way from your site’s server to Kinsta’s Cloudflare-based CDN and edge cache.

Within analytics for a single site or the amalgamated data for what could be multiple sites at the company level, you will find this improved reporting in the new [Cache Breakdown chart](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#cache-breakdown).

## Getting a breakdown of cache performance

Navigate to the **Cache Breakdown** chart from a company **Dashboard** or the **Site Information** page for a particular WordPress environment by selecting **Analytics** in the left-hand menu and then clicking on the **Cache** tab at the top of the **Analytics** landing page:

![A screenshot of the Cache Breakdown chart in MyKinsta Analytics.](https://kinsta.com/wp-content/uploads/2026/04/mykinsta-anaytics-cache-breakdown.png)

The Cache Breakdown chart in MyKinsta Analytics.

This chart tallies the number of requests resolved by:

- Server cache
- Edge cache
- The CDN
- Non-cached responses

Your server cache consists of complete website pages generated dynamically by WordPress and then stored for a period on your website’s own hard drive. WordPress can deliver these again to website browsers without having to generate them from content in its database.

The contents of server cache can also end up in edge cache if you have enabled that free service. Pages served from edge cache don’t require any resources from your site’s server.

The CDN works like an edge cache for static content like images, video, linked JavaScript and CSS files, and downloads in numerous other document formats.

The new Cache breakdown chart gives you a clear view of the relative performances of the caches available to a Kinsta-hosted WordPress site.

And don’t forget that you can now [dig deeper into MyKinsta Analytics](https://kinsta.com/changelog/analytics-improvements/) data for charts like this one and view up to 90 days of traffic history.

Not already a Kinsta customer? Let us introduce you to the [MyKinsta dashboard](https://kinsta.com/mykinsta/).
