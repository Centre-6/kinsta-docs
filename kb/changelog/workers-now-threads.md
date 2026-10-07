---
url: "https://kinsta.com/changelog/workers-now-threads/"
title: "Those things we called PHP workers? Now we\u2019re calling them threads"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Those things we called PHP workers? Now we\u2019re calling them threads"]
kinsta_last_updated: "2024-12-18T20:51:20+00:00"
sitemap_lastmod: "2024-12-18T20:51:20+00:00"
fetched_at: "2026-10-07T22:37:00Z"
sha256: "e2093d2beed7114145923f95865f4f9bf86c7c310502b442b96f6981af61af76"
body_chars: 3561
extracted_with: "main article"
status: "live"
---

# Those things we called PHP workers? Now we’re calling them threads

**Section:** Changelog > Those things we called PHP workers? Now we’re calling them threads
**Product:** Changelog
**Source:** https://kinsta.com/changelog/workers-now-threads/
**Kinsta last updated:** 2024-12-18T20:51:20+00:00

## On this page

- [What’s the deal with PHP workers and threads?](#whats-the-deal-with-php-workers-and-threads)
- [Why Kinsta customers should be aware of threads](#why-kinsta-customers-should-be-aware-of-threads)
- [Our goal: The fastest, most reliable WordPress hosting](#our-goal-the-fastest-most-reliable-wordpress-hosting)

---

Updated
:   December 18, 2024

![An illustration representing the change in terminology at Kinsta, with workers now being called threads.](https://kinsta.com/wp-content/uploads/2024/12/changelog-terminology-threads-workers-1024x536.png)

This isn’t exactly an update to any of Kinsta’s services: Instead, it’s a heads-up that we’re changing the terminology for something we’ve always called PHP “workers” and adopting the more industry-standard term “threads.”

Anyone who spends much time reading Kinsta’s [Documentation](https://kinsta.com/docs/), our [Blog](https://kinsta.com/blog/), or [Knowledge Base](https://kinsta.com/blog/) might get the feeling some characters in our story have changed, but the same PHP workers we’ve talked about for a long time are simply performing the same tasks under a different name.

## What’s the deal with PHP workers and threads?

The reason we care about this terminology is because the PHP interpreter that processes the scripts behind an application like the [WordPress CMS](https://kinsta.com/wordpress) runs single-threaded. That means requests that arrive (more or less) simultaneously would naturally be queued for processing one at a time. That can slow things down for your website’s visitors.

A solution we’ve employed at Kinsta for a long time is to simulate a multi-threaded environment by providing access to PHP in multiple distinct partitions of memory. Each block of memory can still serve just one PHP thread, but all of them can execute simultaneously to share the work.

So, “workers” was a term that seemed like a good idea (at the time).

## Why Kinsta customers should be aware of threads

For customers with higher-traffic WordPress sites, optimizing [PHP performance](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/) can be a delicate balancing act between the number of PHP threads available to process requests simultaneously and the amount of memory available to each.

PHP is not invoked when a website delivers cached content in response to a browser request, but it’s required whenever a script needs to be interpreted for tasks like querying the database and building pages on the fly.

Sites with many simultaneous users might benefit by having more threads available. Sites that depend on intensive database queries and processing large arrays of data might benefit by having more memory available to each thread.

We expect that Kinsta’s new [PHP Performance Add-on](https://kinsta.com/changelog/php-performance/) (available within the [MyKinsta dashboard](https://kinsta.com/mykinsta/) and the [Kinsta API](https://kinsta.com/docs/kinsta-api/)) will raise the profile of threads for many customers. By using a term common across the hosting industry for these processes, we hope users will be able to better picture what’s happening under the hood of our platform.

![Screenshot showing the PHP Performance Add-on tool in the MyKinsta dashboard.](https://kinsta.com/wp-content/uploads/2024/12/php-performance-allocation.png)

Juggling the total PHP memory pool with individual threads in MyKinsta.

## Our goal: The fastest, most reliable WordPress hosting

We are always looking for ways to make [managed hosting for WordPress](https://kinsta.com/wordpress-hosting/) more powerful, more reliable — and simpler.

If you need a [fast](https://kinsta.com/blog/migrate-to-kinsta/) WordPress site that’s also [secure](https://kinsta.com/wordpress-hosting/security/), check out our [hosting plans](https://kinsta.com/pricing/) to find the one that meets your needs.
