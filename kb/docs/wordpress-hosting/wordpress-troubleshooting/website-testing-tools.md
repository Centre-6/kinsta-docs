---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/website-testing-tools/"
title: "Troubleshooting - Speed and Load Testing"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-troubleshooting"
section: []
kinsta_last_updated: "July 29, 2024"
sitemap_lastmod: "2024-07-29T12:36:50+00:00"
fetched_at: "2026-10-07T22:36:49Z"
sha256: "85ed55d9d0b9f8d832382b29ee08408e68008fa53759d90cefb2d2a090d439f7"
body_chars: 5367
extracted_with: "main article"
status: "live"
---

# Troubleshooting - Speed and Load Testing

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/website-testing-tools/
**Kinsta last updated:** July 29, 2024

## On this page

- [Speed testing](#speed-testing)
  - [1. Confirm caching is enabled](#1-confirm-caching-is-enabled)
  - [2. Confirm the CDN is enabled](#2-confirm-the-cdn-is-enabled)
  - [3. Choose a tool and run your test](#3-choose-a-tool-and-run-your-test)
  - [4. Run your speed test more than once](#4-run-your-speed-test-more-than-once)
  - [If your site is running slow](#if-your-site-is-running-slow)
- [Load testing](#load-testing)

---

Testing your website, especially before [making it live](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/go-live-checklist/), is a best practice for most developers and site owners. There’s sometimes confusion, though, about the different types of testing and how they’re done. Two of the most common are speed testing and load testing.

## Speed testing

Speed testing measures a page’s size and how long it takes to load. It’s commonly used to identify large or slow requests so bottlenecks can be improved or eliminated.

To check your site’s performance, or see how a change, like migrating to Kinsta, enabling the CDN, or installing a new plugin or theme, affects load times, you can run a speed test.

Speed test tools measure how fast your site loads at the moment you run the test. The first time a page is requested after its cache is cleared, or if you’re testing a staging environment, where caching is off by default, your site has to generate that page from scratch instead of serving a stored copy. That takes longer, so your results will show a slower load time than what your visitors actually experience. Before running a speed test, make sure caching and the CDN are enabled and have already served the page at least once.

### 1. Confirm caching is enabled

Live sites have [server caching](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/) enabled by default.

Staging environments have caching disabled by default, since they’re meant for development and debugging. If you’re testing a staging site, enable caching first: within the staging environment, click **Caching** > **Server caching** > **Enable**.

### 2. Confirm the CDN is enabled

To check or enable the Kinsta CDN for a site, go to **Sites** > ***sitename*** > **Caching** > **CDN** > **Enable CDN**.

### 3. Choose a tool and run your test

Pick a speed test tool; there are multiple options available, including the following:

- [Pingdom](https://tools.pingdom.com/)
- [Google PageSpeed Insights](https://pagespeed.web.dev/)
- [WebPageTest](https://www.webpagetest.org/)
- [GTmetrix](https://gtmetrix.com/)
- [KeyCDN Website Speed Test](https://tools.keycdn.com/speed)
- [LogicMonitor WebPageTest](https://www.logicmonitor.com/webpagetest)
- [YSlow](https://yslow.org/)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/performance)
- [dotcom-monitor](https://www.dotcom-tools.com/website-speed-test)
- [New Relic](https://newrelic.com/blog/dem/website-performance-monitoring)

Different tools use different metrics, so use the same tool each time for consistent results. Once you’ve picked one, enter your site’s URL, choose a test location, and run the test.

Load time depends on the distance between the visitor and your site’s data center ([TTFB](https://kinsta.com/blog/ttfb/) and [network latency](https://kinsta.com/blog/network-latency/) both increase with distance). Test from a location near your data center and one far away to see the range your visitors might experience. Keep your test location consistent between runs.

### 4. Run your speed test more than once

The first request after a cache is cleared (or after enabling caching for the first time) will always be a cache **MISS**, which makes that first test result unreliable; the page hasn’t been generated and stored yet, so that request is always the slowest one. Run your speed test two or three times in a row so the page has a chance to be requested, cached, and then served from cache before you record a result.

You can confirm whether a request was served from cache by checking its response headers:

- `x-kinsta-cache`: Shown on requests served directly from your Kinsta server. **MISS** means the page wasn’t cached yet; **HIT** means it was served from cache.
- `x-cache`: Shown on requests served from the Kinsta CDN. **MISS** means the page wasn’t cached yet; **HIT** means it was served from cache.

Most speed test tools display response headers as part of their results. Look for these headers on your test’s requests to confirm the page was actually served from cache before comparing results.

### If your site is running slow

As a general benchmark, a load time of 2.5 seconds or less is considered good, and anything over 4 seconds is considered poor. Most speed test tools report this as “Largest Contentful Paint” or “LCP” in their results.

Slow load times are usually caused by a plugin, theme, or custom code issue rather than the server itself. If your speed test results are consistently slow even with caching and the CDN active, see [Troubleshooting Performance](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/troubleshooting-wordpress-performance/) for how to isolate the cause using your staging environment, along with tools like [Kinsta’s APM tool](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/), [New Relic](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/custom-new-relic-tracking/), and [server logs](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/).

## Load testing

Load testing (stress testing your site with simulated traffic) is prohibited on the MyKinsta platform. For more information, see our [Terms of Service](https://kinsta.com/legal/terms-service/#h-5-acceptable-use-policy-and-protection-of-the-services).
