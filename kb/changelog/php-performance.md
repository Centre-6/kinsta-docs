---
url: "https://kinsta.com/changelog/php-performance/"
title: "Manage your site's PHP threads and memory use for optimal performance"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Manage your site\u2019s PHP threads and memory use for optimal performance"]
kinsta_last_updated: "2026-04-20T09:32:12+00:00"
sitemap_lastmod: "2026-04-20T09:32:12+00:00"
fetched_at: "2026-10-07T22:36:00Z"
sha256: "9056e519c9cdcdec4a4f93dde2146f66696d25f297073b4c38aced15ecc80246"
body_chars: 7680
extracted_with: "main article"
status: "live"
---

# Manage your site's PHP threads and memory use for optimal performance

**Section:** Changelog > Manage your site’s PHP threads and memory use for optimal performance
**Product:** Changelog
**Source:** https://kinsta.com/changelog/php-performance/
**Kinsta last updated:** 2026-04-20T09:32:12+00:00

## On this page

- [About PHP threads and memory limits](#about-php-threads-and-memory-limits)
- [Managing PHP performance](#managing-php-performance)
  - [How to determine the best PHP performance values](#how-to-determine-the-best-php-performance-values)
- [Kinsta’s WordPress hosting is built for performance](#kinstas-wordpress-hosting-is-built-for-performance)

---

Updated
:   April 20, 2026

![An illustration representing a MyKinsta dialog with the words: PHP performance.](https://kinsta.com/wp-content/uploads/2024/12/mykinsta-php-performance-1024x536.png)

We’re giving customers more control over the performance of their WordPress websites with a new option to allocate PHP threads and memory.

The [PHP Performance tool](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/) allows customers on most of Kinsta’s hosting plans to easily adjust the total amount of memory available to PHP behind their websites and manage the allocation of that memory among PHP threads (often referred to as “workers” around here).

By balancing the number of threads and the amount of memory available to each, website operators can fine-tune the performance of live and [Premium Staging](https://kinsta.com/wordpress-hosting/staging/) environments to meet the demands on their WordPress sites.

## About PHP threads and memory limits

Threads are the processes that execute the PHP code that powers a WordPress site and are called on for database queries, building pages, and performing a variety of background tasks. Unless a website is serving up cached pages or static content like an image, a PHP thread is probably doing the work.

The number of threads available determines how many requests a WordPress site can process simultaneously. And each thread requires some memory (RAM) in which to execute. How many threads your website requires and how much memory each thread demands depends on how busy your site is and the kinds of tasks those threads are required to perform.

If your site has four PHP threads and six requests arrive simultaneously, the first four will be processed immediately, while the remaining two will wait in the queue. While threads wait to execute, a visitor’s browser might be waiting, too. Worse, extreme cases could end with visitors seeing a [504 Gateway Timeout](https://kinsta.com/blog/504-gateway-timeout/#needs-more-php-workers) error report.

By default, most Kinsta hosting plans allocate 256MB of memory to each PHP thread. A plan with a PHP memory pool of 1GB would support four threads with that configuration. The new PHP Performance tool in the [MyKinsta dashboard](https://kinsta.com/mykinsta/) allows you to change the number of available threads within an existing memory pool and to expand (or reduce) the total PHP memory limit.

Running out of memory can mean your visitors are greeted with [500 Internal Server Error](https://kinsta.com/blog/500-internal-server-error/) messages.

## Managing PHP performance

For a quick look at how your site’s PHP threads and memory are currently performing, you can view recent activity in MyKinsta at **WordPress Sites** > ***sitename*** > **Analytics**. Select the **Performance** tab at the top of the page and scroll down to the **PHP memory limit reached** and **PHP thread limit** sections. If these resources have been maxed out in the previous 24 hours, that will be reported here.

In the example below, simultaneous requests have exceeded the number of available threads twice in the previous 24 hours:

![Screenshot of PHP thread errors within MyKinsta analytics.](https://kinsta.com/wp-content/uploads/2024/12/php-performance-threads-limit-exceeded-analytics.png)

Analytics in MyKinsta revealing thread-limit errors.

To view and possibly modify these PHP performance factors, go to **WordPress Sites** > ***sitename*** > **Info**. On the **Site Information page**, scroll down to the PHP performance section. The site whose analytics we viewed above might report something like this:

![A screenshot showing PHP performance information in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/12/php-performance-threads-limit-exceeded.png)

PHP performance details on the **Site Information** page.

Above, a typical website with a PHP memory pool of 1GB is configured to support four threads with 256MB of memory available to each.

Click the **Change** button, and you will see a visual representation of this configuration:

![Screenshot of the Change PHP performance dialog in MyKinsta for a site with 1GB of PHP memory and four PHP threads.](https://kinsta.com/wp-content/uploads/2024/12/php-performance-slider-four-threads.png)

The **Change PHP performance** dialog in MyKinsta

The **Total memory pool** dropdown allows you to select a new value for a PHP memory limit. The amount included in your hosting plan is indicated. The costs of increasing the memory pool beyond the plan’s default are shown along with the available options for a new limit.

![Screenshot showing a user choosing a new size for a website's PHP memory pool.](https://kinsta.com/wp-content/uploads/2024/12/php-performance-memory-pool-dropdown.png)

Selecting a new value for the PHP memory pool.

After selecting a new value for the size of the memory pool, a **Continue** button will appear. After clicking **Continue**, you will be asked to confirm the update and any changes to billing required by the new pool value:

![Screenshot showing the confirmation dialog for a PHP memory pool upgrade in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/12/php-performance-memory-pool-increase.png)

Confirming an increase in the size of the PHP memory pool.

Even without changing the size of the memory pool, you can use the slider below the dropdown to select new values for the number of threads available. Below, we’ve kept our memory pool at the 1GB included in the plan but increased the number of PHP threads to eight:

![Screenshot showing a user selecting a count of eight PHP threads using a slider control](https://kinsta.com/wp-content/uploads/2024/12/php-performance-slider-eight-threads.png)

Choosing eight PHP threads within an existing memory pool of 1GB.

To support eight threads within 1GB of memory, the amount of memory per thread is reduced to 128MB.

After selecting new values for the thread count, click the **Change PHP performance** button to update your site.

### How to determine the best PHP performance values

The analytics report in MyKinsta is your friend when determining the optimal PHP performance settings for your site.

In the example above, we increased the maximum number of threads to eight while keeping the total PHP memory pool at 1GB. Our next step would be to monitor the analytics to see if site traffic can now be handled by eight threads without generating errors related to thread or memory limits.

With our example site, we still have the option to increase the thread count to 16 (with 64MB each), but if errors persist, it would be time to consider increasing the size of the PHP memory pool itself.

## Kinsta’s WordPress hosting is built for performance

In addition to giving you immediate control over performance factors like PHP threads and memory, Kinsta’s [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/) platform uses the fastest-available virtual machines in each data center on Google’s [low-latency Premium Tier network](https://kinsta.com/blog/cloud-platform-for-developers/). Our [Cloudflare integration](https://kinsta.com/blog/cloudflare-integration/) boosts the speed and reliability even further with a [robust CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#kinstas-cdn), [edge caching](https://kinsta.com/changelog/edge-caching/), [early hints](https://kinsta.com/changelog/early-hints/), and built-in [image optimization](https://kinsta.com/changelog/wordpress-image-optimization/).

If you aren’t already a Kinsta customer, it’s time to find a [WordPress Hosting package](https://kinsta.com/pricing/) that’s right for you.
