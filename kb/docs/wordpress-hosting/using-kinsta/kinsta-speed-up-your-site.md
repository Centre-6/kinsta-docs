---
url: "https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-speed-up-your-site/"
title: "Speed Up Your Site"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "using-kinsta"
section: ["WordPress Hosting", "Using Kinsta"]
kinsta_last_updated: "2026-10-12T16:28:41"
change_signal: "2026-10-12T16:28:41"
fetched_at: "2026-11-11T13:03:01Z"
sha256: "8a476c895a552336f63c02ad9b22bd9adaa7466a7248fce2724474c778d854fd"
body_chars: 5170
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Speed Up Your Site

**Section:** WordPress Hosting > Using Kinsta
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-speed-up-your-site/
**Kinsta last updated:** 2026-10-12T16:28:41

## On this page

- [Kinsta CDN](#kinsta-cdn)
- [Edge caching](#edge-caching)
- [Clear the cache when changes don’t show](#clear-the-cache-when-changes-dont-show)
- [Early Hints](#early-hints)
- [Find what’s slowing a page down with APM](#find-whats-slowing-a-page-down-with-apm)
- [When to add more performance](#when-to-add-more-performance)
- [Test the right way](#test-the-right-way)
- [In your routine](#in-your-routine)

---

Most of Kinsta’s performance features are free and already switched on for every site. Here’s how to confirm they’re working, find out what’s slowing a page down, and decide when it’s worth adding more.

## Kinsta CDN

**Why it matters:** The [CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/) serves your images, scripts, and stylesheets from locations close to each visitor, which takes load off your server and shortens load times.

**What’s included:** Kinsta CDN is powered by Cloudflare and is free for every site. It includes HTTP/3 support, primary domain support, and image optimization.

**How to start:** It’s enabled by default when you add a site. If you turned it off during testing, switch it back on in MyKinsta.

**Watch out for:** Use only one CDN. Running Kinsta CDN alongside another CDN can cause problems on your site.

## Edge caching

**Why it matters:**  [Edge caching](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/) copies the cached pages from your site’s data center out to Cloudflare’s network of more than 300 locations. Visitors get pages from the location nearest to them, and your server handles fewer requests.

**When to use it:** It helps every site and makes the biggest difference when your visitors are spread across countries or continents.

**How to start:** It’s free on all plans and needs no plugin. See [Edge Caching](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/) for how to manage it and clear the cache.

**Watch out for:** Edge caching and Kinsta CDN only run on live sites and premium staging environments. Speed tests on a standard [staging environment](https://kinsta.com/docs/wordpress-hosting/staging-environment/) won’t reflect how fast your live site is.

## Clear the cache when changes don’t show

**Why it matters:** Caching is what makes your site fast, but it also means visitors can briefly see an older version of a page after you edit it.

**How to start:** Clear the server, CDN, and edge cache for a single site; go to **Sites** > ***sitename*** > **Caching** > **Clear all caches**. To clear several sites at once, select them on the **Sites** page and choose **Actions** > **Clear cache**. See [Caching](https://kinsta.com/docs/wordpress-hosting/caching/).

## Early Hints

**Why it matters:** Early Hints lets browsers start loading important files before the full page response arrives, which can make pages appear sooner.

**How to start:** See [**Early Hints**](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/early-hints/) in MyKinsta **Tools**.

## Find what’s slowing a page down with APM

**Why it matters:** When one page is slow, guessing at the cause wastes time. [Kinsta’s APM tool](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/) records timestamped details of your site’s PHP processes, MySQL database queries, and external HTTP calls, so you can see exactly where the time goes.

**When to use it:** When a specific page, such as checkout or search, is noticeably slower than the rest of your site, or after installing a new plugin.

**How to start:** It’s included free on every plan. See [Kinsta’s APM Tool](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/).

**Watch out for:** APM is off by default because it uses extra server resources. When you turn it on, you choose how long it monitors for, so run it while you investigate rather than leaving it on. It only records data from the moment it’s enabled, so give it time to collect some before you look.

## When to add more performance

If your site is still slow after the free options are working, two add-ons can help. See [Add-Ons](https://kinsta.com/docs/wordpress-hosting/wordpress-add-ons/) for details and pricing.

- **Redis caching:** Stores the results of database queries so they don’t have to run every time. It suits dynamic sites that can’t be fully page-cached, such as WooCommerce stores, membership sites, and forums.
- **PHP performance:** Gives your site more PHP memory and threads. It suits sites that handle many uncached requests at once, such as busy stores during a sale.

The [Performance](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#performance) charts in Analytics can show whether you need either one; see [Understand Your Traffic and Usage](https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-understand-your-traffic-and-usage/).

## Test the right way

Compare each result with an earlier test, ideally one taken soon after your site went live. Run each test several times with the same tool and settings, because single results vary. See [Speed and Load Testing](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/website-testing-tools/).

## In your routine

Sites slow down gradually as plugins, scripts, and content build up. Run a speed test each month and compare it with earlier results, then use APM on any page that’s gotten slower. Each quarter, look for large images that could be compressed. See [Your Maintenance Routine](https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-your-maintenance-routine/).
