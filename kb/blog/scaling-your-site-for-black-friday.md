---
url: "https://kinsta.com/blog/scaling-your-site-for-black-friday/"
title: "How to scale your site for Black Friday with Kinsta\u2019s PHP performance add-on"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "WordPress Performance", "How to scale your site for Black Friday with Kinsta\u2019s PHP performance add-on"]
kinsta_last_updated: "2025-10-06T16:04:57+00:00"
sitemap_lastmod: "2025-10-06T16:04:57"
fetched_at: "2026-10-07T22:41:56Z"
sha256: "0bd689afbad22770e020e7aa474092c427e3b000eb13cfb021543bad070bced1"
body_chars: 11677
extracted_with: "main article"
status: "live"
---

# How to scale your site for Black Friday with Kinsta’s PHP performance add-on

**Section:** Resource Center > Blog > WordPress Performance > How to scale your site for Black Friday with Kinsta’s PHP performance add-on
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/scaling-your-site-for-black-friday/
**Kinsta last updated:** 2025-10-06T16:04:57+00:00

## On this page

- [Why Black Friday traffic causes downtime](#why-black-friday-traffic-causes-downtime)
  - [PHP thread limits](#php-thread-limits)
  - [Memory limits](#memory-limits)
- [A smarter way to handle holiday traffic surges](#a-smarter-way-to-handle-holiday-traffic-surges)
- [How to turn on the add-on in MyKinsta (step-by-step)](#how-to-turn-on-the-add-on-in-mykinsta-step-by-step)
  - [Step 1: Log in to MyKinsta](#step-1-log-in-to-mykinsta)
  - [Step 2: Select your site](#step-2-select-your-site)
  - [Step 3: Adjust threads and memory](#step-3-adjust-threads-and-memory)
  - [Step 4: Save and confirm changes](#step-4-save-and-confirm-changes)
  - [Step 5: Roll back after the sale](#step-5-roll-back-after-the-sale)
- [What this looks like in a WooCommerce store](#what-this-looks-like-in-a-woocommerce-store)
- [Summary](#summary)

---

Author
:   [Jeremy Holcombe](https://kinsta.com/blog/author/jeremyholcombe/ "Posts by Jeremy Holcombe")

Published
:   October 30, 2025

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![](https://kinsta.com/wp-content/uploads/2025/10/how-to-scale-your-site-for-black-friday-with-kinstas-php-performance-add-on-1024x512.png)

Black Friday is one of the [busiest shopping weekends](https://kinsta.com/blog/black-friday-cyber-monday-insights/) of the year for [WooCommerce](https://kinsta.com/blog/woocommerce-tutorial/) stores. It’s also one of the most stressful. A sudden wave of shoppers can push your site to its limits, causing slow load times, errors at checkout, and even complete downtime.

Instead of locking yourself into a more expensive hosting plan just to cover a few high-traffic days, you can temporarily scale up your site’s power by increasing [PHP threads and memory](https://kinsta.com/blog/php-threads-vs-php-memory-limit/) with Kinsta’s [PHP performance add-on](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/).

This ensures your store can handle more simultaneous requests, keep plugins running smoothly, and prevent checkout bottlenecks when [traffic surges](https://kinsta.com/blog/high-traffic-wordpress-hosting/).

In this guide, we examine why Black Friday traffic can overwhelm WooCommerce sites, how the PHP performance add-on addresses these issues, and the steps to get it running smoothly in [MyKinsta](https://kinsta.com/mykinsta/).

## Why Black Friday traffic causes downtime

When a [WooCommerce store](https://kinsta.com/blog/woocommerce-optimization/) experiences a surge of visitors, two key resources are usually the first to run out: [PHP threads](https://kinsta.com/blog/php-threads/) and [memory](https://kinsta.com/blog/php-threads-vs-php-memory-limit/#managing-php-memory-limits).

### PHP thread limits

Think of each [PHP thread](https://kinsta.com/blog/php-threads-vs-php-memory-limit/) as a checkout lane. Every thread can only process one request at a time, whether that’s adding a product to the cart, running a plugin function, or completing payment.

If you don’t have enough threads to handle the sudden spike in activity, requests pile up. That leads to long wait times, stuck [checkouts](https://kinsta.com/blog/woocommerce-one-page-checkout/), and frustrated shoppers.

### Memory limits

[Themes](https://kinsta.com/blog/hybrid-themes/), [plugins](https://kinsta.com/blog/wordpress-plugins-for-educational-sites/), and third-party integrations all consume memory. Under heavy traffic, that usage balloons. Once your site maxes out its available memory, pages slow to a crawl, requests time out, and in the worst cases, the site crashes.

When these [memory limits](https://kinsta.com/blog/php-memory-limit/) are reached, the problems are hard to miss:

- [500 errors](https://kinsta.com/blog/500-internal-server-error/) when requests can’t be completed.
- [Gateway timeouts](https://kinsta.com/blog/504-gateway-timeout/) as pages stall under load
- [Checkout forms](https://kinsta.com/blog/woocommerce-checkout/) freezing or failing to submit
- Shoppers [leaving carts behind](https://kinsta.com/blog/shopping-cart-abandonment/) because the site won’t respond

And while the traffic surge only lasts a few days, the damage can linger. Slow or broken checkouts cost immediate revenue and leave a bad impression that can hurt long-term customer loyalty.

The upside here is you don’t need to permanently upgrade your [hosting plan](https://kinsta.com/blog/wordpress-hosting-plans/) just to survive [Black Friday](https://kinsta.com/webinars/website-prep-black-friday-cyber-monday/). Temporary scaling allows you to expand PHP threads and memory only when it really matters.

## A smarter way to handle holiday traffic surges

Instead of overspending on a bigger hosting plan you don’t really need, Kinsta’s [PHP performance add-on](https://kinsta.com/docs/wordpress-hosting/wordpress-add-ons/#php-performance-add-on) gives you a smarter, more flexible way to scale. It’s designed for moments like Black Friday, when a sudden surge in traffic can push your WooCommerce store to the edge.

Here’s why it works so well:

- **Scales PHP threads and memory on demand.** With just a few clicks in [MyKinsta](https://kinsta.com/mykinsta/), you can increase the number of PHP threads to handle more simultaneous requests and raise memory limits to keep plugins and dynamic features running smoothly under load.
- **Activate it only when needed.** The add-on can be activated only for the Black Friday weekend or any other sales event, and then rolled back once traffic levels return to normal.
- **Pay only for what you use.** Because billing is prorated, you only pay for the time the add-on is active. That means no long-term plan upgrades, no wasted resources, and no surprise costs after the sale ends.

This performance add-on lets you match your hosting power to your busiest shopping days without committing to a permanent change. It’s a fast and affordable way to keep your WooCommerce store stable when demand increases suddenly.

## How to turn on the add-on in MyKinsta (step-by-step)

Activating the PHP performance add-on is straightforward. You don’t need to make complicated server settings adjustments or wait for support to assist. It’s all handled inside your MyKinsta dashboard.

Here’s how to do it.

### Step 1: Log in to MyKinsta

After signing in, head to your dashboard. You should see a list of the sites you currently host with Kinsta.

![wordpress sites](https://kinsta.com/wp-content/uploads/2025/10/wordpress-sites-1.png)

You can view all your WordPress sites listed in MyKinsta.

### Step 2: Select your site

Select the appropriate site, then click **Info** > **PHP performance**. Next, click **Change** on the right-hand side of the screen:

![PHP performance options](https://kinsta.com/wp-content/uploads/2025/10/php-performance-options.png)

Find the PHP performance options under Info for your site.

Alternatively, you can go to **Add-ons** and click **“Change”** next to **PHP performance**.

![PHP performance in Add-ons](https://kinsta.com/wp-content/uploads/2025/10/php-addons.png)

You can find PHP performance under Add-ons in MyKinsta.

In either case, you can then upgrade your performance settings.

### Step 3: Adjust threads and memory

Inside the add-on settings, you’ll see controls to increase PHP threads and memory. Use these sliders to set the right balance for your expected traffic.

![Adjusting PHP performance settings](https://kinsta.com/wp-content/uploads/2025/10/php-settings.png)

Adjust the threads and memory you need in the PHP performance add-on settings.

For a detailed breakdown of how threads and memory are distributed across different pool sizes, refer to our [documentation](https://kinsta.com/docs/wordpress-hosting/wordpress-add-ons/#pool-threads-and-memory-distribution-values).

### Step 4: Save and confirm changes

Click **Continue**, and the adjustments take effect almost immediately. There’s no downtime while scaling up.

### Step 5: Roll back after the sale

Once the Black Friday rush is over, return to the same settings and remove the add-on. Your site will revert to its normal resource levels, and billing will cease immediately.

![roll back add-on](https://kinsta.com/wp-content/uploads/2025/10/roll-back.png)

Roll back the add-on after the sale is over.

The entire process takes just a few minutes, providing you with the flexibility to prepare for heavy traffic without complicating your hosting setup or incurring unnecessary expenses.

## What this looks like in a WooCommerce store

Picture a WooCommerce shop that normally processes 50 orders per hour on a steady day. When Black Friday hits, that number can easily triple. Or more! Suddenly, you’ve got hundreds of people browsing products, adding items to their carts, and trying to check out at the same time.

Without scaling prior to the surge in traffic, this store is likely to experience:

- **PHP threads max out.** Every new checkout request has to wait its turn, creating a backlog that feels like standing in line at the register.
- **Pages crawl or stall.** As requests pile up, customers see slow load times or gateway timeouts.
- **Errors appear.** 500 errors or frozen checkout forms disrupt the flow, leaving shoppers uncertain whether their order has gone through.
- **Sales slip away.** Frustrated buyers abandon carts and head to competitors, leaving [revenue](https://kinsta.com/blog/build-recurring-revenue-into-agency/) on the table.

With scaling, the outcome will be much different:

- **Additional PHP threads absorb the surge.** More checkout requests are processed simultaneously, so the “line” keeps moving.
- **Memory increases keep things stable.** Even with [multiple plugins](https://kinsta.com/blog/wordpress-ecommerce-plugins/) for features such as [payment gateways](https://kinsta.com/blog/payment-gateway-integration/), shipping calculators, and loyalty programs all running simultaneously, the site doesn’t run out of resources.
- **The checkout experience stays smooth.** Customers can move from the [product page](https://kinsta.com/blog/conversions-woocommerce-product-pages/) to payment confirmation without delays or interruptions.
- **Revenue climbs instead of slipping.** More orders are completed successfully, and shoppers leave with a positive experience they’ll remember.

The result is night and day. Instead of worrying about downtime or errors, store owners can focus on fulfilling orders and making the most of the biggest sales weekend of the year.

In one of our [case studies](https://kinsta.com/case-studies/dartdrones/), DARTdrones, a Kinsta WooCommerce customer, experienced a massive traffic spike after appearing on Shark Tank. Their site served **over 1 million pageviews in just six hours** and generated **$300,000 in revenue** without a single minute of downtime. By scaling PHP threads and optimizing their infrastructure on Kinsta, they reduced page load times by 50% and maintained a smooth checkout process even under extreme pressure.

This is exactly the kind of resilience the PHP performance add-on brings to Black Friday. It enables your WooCommerce store to handle sudden demand without compromising speed, reliability, or sales.

## Summary

Black Friday brings in the kind of traffic that can overwhelm even well-optimized WooCommerce stores. When PHP threads and memory reach their limits, customers encounter errors, slow load times, and stalled checkouts. All of these unfortunate factors translate into lost sales.

The Kinsta PHP performance add-on takes the stress out of preparing for peak demand. Since it lets you temporarily boost threads and memory, it keeps your site responsive when it matters most. You can activate it for just the weekend, pay only for what you use, and roll back when traffic returns to normal.

Don’t let downtime eat into your biggest sales opportunity of the year. Stay prepared, stay fast, and keep every checkout running smoothly.

Start scaling with the [Kinsta PHP performance add-on](https://kinsta.com/docs/wordpress-hosting/wordpress-add-ons/#php-performance-add-on) today and head into Black Friday with confidence.

Jeremy Holcombe
[Kinsta](https://kinsta.com/)

Senior Editor at Kinsta, WordPress Web Developer, and Content Writer. Outside of all things WordPress, I enjoy the beach, golf, and movies. I also have tall people problems.

- [LinkedIn](https://www.linkedin.com/in/jeremyholcombe/)
