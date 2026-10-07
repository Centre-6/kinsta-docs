---
url: "https://kinsta.com/changelog/auto-db-optimize/"
title: "Automatic MySQL Database Optimizations, Self-Healing PHP, GCP Firewall"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Automatic MySQL Database Optimizations, Self-Healing PHP, GCP Firewall"]
kinsta_last_updated: "2026-02-11T16:13:12+00:00"
sitemap_lastmod: "2026-02-11T16:13:12+00:00"
fetched_at: "2026-10-07T22:35:54Z"
sha256: "8004065902f88ac57c7246451428a2ae556d1d1f4adc2637b969b42d55615fc7"
body_chars: 8047
extracted_with: "main article"
status: "live"
---

# Automatic MySQL Database Optimizations, Self-Healing PHP, GCP Firewall

**Section:** Changelog > Automatic MySQL Database Optimizations, Self-Healing PHP, GCP Firewall
**Product:** Changelog
**Source:** https://kinsta.com/changelog/auto-db-optimize/
**Kinsta last updated:** 2026-02-11T16:13:12+00:00

## On this page

- [Automatic MySQL Database Optimizations](#automatic-mysql-database-optimizations)
- [Self-Healing PHP](#self-healing-php)
- [Now Secured Behind Google Cloud Platform Firewall](#now-secured-behind-google-cloud-platform-firewall)
- [Newsletter Subscription in User Settings](#newsletter-subscription-in-user-settings)
- [Add Domain with and without www on Site Creation](#add-domain-with-and-without-www-on-site-creation)
- [Charts on the Dashboard Got a Slick New Look](#charts-on-the-dashboard-got-a-slick-new-look)
- [We Now Support Wordfence](#we-now-support-wordfence)

---

Updated
:   February 11, 2026

![Automatic MySQL database optimizations](https://kinsta.com/wp-content/uploads/2019/09/auto-db-optimize-v2-1024x512.png)

If you’re already a Kinsta client, you’ve probably become accustomed to our monthly (sometimes weekly) feature updates. It’s very important for us to share what we’re working on so that you can see first-hand that your feedback, suggestions, and even complaints aren’t going unnoticed. Without you, we wouldn’t be here.

We just [increased disk space](https://kinsta.com/changelog/more-disk-space/) on all of our hosting plans, but the following features we are even more excited about. Why? Because everyone on our platform will benefit from them. Some of these changes will **help improve the performance and stability of your WordPress sites**.

## Automatic MySQL Database Optimizations

Optimizing your database is one of those things that often gets neglected. But in fact, it can be one of the most important factors to ensure fast performance, especially for the long-term health of your site.

One of the great things about Kinsta is that every WordPress site runs in an isolated container. This gives us more control as it means each site has its own separate MySQL instance.

To help combat database performance woes, we have implemented a new system that **automatically fine-tunes your MySQL database settings** **based on the needs of your WordPress site.** This optimization runs once per week and will ensure better [MariaDB](https://kinsta.com/blog/mariadb-vs-mysql/) performance. If our automated process detects something wrong that it can’t fix itself, it notifies our sysadmin team.

Not to worry developers, this does not run `wp db optimize` or change your database contents in any way. While we’re proud of this awesome new feature, it doesn’t mean you can ignore best practices though, such as:

- [Uninstalling plugins the right way](https://kinsta.com/blog/uninstall-wordpress-plugin/) to remove left-behind database tables.
- Regularly checking your [wp_options table for autoloaded data](https://kinsta.com/blog/wp-options-autoloaded-data/) or using a plugin like WP Rocket to clean up left behind revisions, transients, etc.

This automation is just one more way that Kinsta helps to ensure the health, stability, and performance of your sites behind the scenes.

## Self-Healing PHP

If you weren’t already aware, we’ve had a tool in the MyKinsta dashboard for quite some time that allows you to one-click [restart PHP](https://kinsta.com/docs/wordpress-hosting/php/#restart-php) (as seen below). While this is definitely helpful, it’s still not perfect. Why? One, it’s still a manual process. Two, if PHP has failed, how are you supposed to know? So we decided to take this a step further.

![Restart PHP in MyKinsta dashboard](https://kinsta.com/wp-content/uploads/2019/09/restart-php-mykinsta-dashboard.png)

Restart PHP in MyKinsta dashboard

Introducing what we call **self-healing PHP**. 🏥 From now on, if PHP goes down for any reason, we try to auto-restart it back up. In a lot of cases, this is all that’s needed and you’re good to go! On rare occasions, it might be a bigger issue. In which case, our system automatically logs this for our sysadmin team to check out.

## Now Secured Behind Google Cloud Platform Firewall

As you might imagine, we are huge fans of [Google Cloud Platform](https://kinsta.com/blog/cloud-platform-for-developers/). Their machines, along with their premium tier network, are part of why sites at Kinsta are blazing fast. In the past, we’ve used a third-party firewall solution. But no more. All WordPress sites at Kinsta are now **secured behind the Google Cloud Platform (GCP) Firewall**.

Here’s how it works. Each site container (where your WordPress site resides) runs on a virtual machine in one of multiple Google Cloud Platform (GCP) data centers. This is behind a load balancer, which is then secured behind the GCP firewall.

![Kinsta hosting architecture](https://kinsta.com/wp-content/uploads/2018/04/kinsta-hosting-architecture-v9.png)

Kinsta hosting architecture

Making this move allows our team to work even closer with GCP’s solutions and in turn provide a better experience all around. The GCP firewall is also integrated with our load balancer to ensure that third-party web application firewalls (WAF) and CDN solutions like Cloudflare still work as they should.

Should you remove your current WAF solution? The short answer is no. A WAF such as Sucuri/Cloudflare is still going to help mitigate a lot of bad traffic. This is because these providers have decades of rules and filters already in place.

## Newsletter Subscription in User Settings

Every month we send out a [newsletter](https://kinsta.com/wordpress-newsletter/) that contains WordPress news, industry trends, and applicable tips on how to drive more traffic and revenue to your business.

We have now integrated the **newsletter subscription into the MyKinsta dashboard**. You can easily subscribe and unsubscribe, or even change the language. To access this, click on your avatar at the bottom left and then on “User Settings.” You can then scroll down to the “Newsletter subscription” section.

![Newsletter subscription in MyKinsta](https://kinsta.com/wp-content/uploads/2019/09/newsletter-subscription-mykinsta.png)

Newsletter subscription in MyKinsta

## Add Domain with and without www on Site Creation

We are always looking for pain points in workflows to see how we can speed things up. One of these we discovered was when adding your domain to MyKinsta. Many would add their non-www version or vice versa and forget to later add the other one. In most cases, you want to add both and redirect the non-primary one.

Therefore we’ve made this a lot easier. Now when you go to add a domain there is a new option: “**Add domain(s) with and without www**” which is selected by default.

When checked, we automatically add both the non-www and www versions of the domains. Example: adding mydomain.com will result in both mydomain.com and www.mydomain.com being added.

![Add domain(s) with and without www](https://kinsta.com/wp-content/uploads/2019/09/add-domain-www-no-www.png)

Add domain(s) with and without www

## Charts on the Dashboard Got a Slick New Look

Every pixel is important to our UX and design team. And we aren’t just saying that. 😉 Their attention to detail and constant drive to improve the user experience in MyKinsta and our website shouldn’t go unnoticed.

The charts on the MyKinsta dashboard just got a slick new look! There is a new tooltip component which lets you more easily see the exact up and down movements on your site.

![MyKinsta new dashboard charts](https://kinsta.com/wp-content/uploads/2019/09/mykinsta-updates-analytics-dashboard.png)

MyKinsta new dashboard charts

## We Now Support Wordfence

If you’re already a Kinsta client then you are probably familiar with our [list of plugins we don’t allow](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-banned-incompatible-plugins/).

We take no joy in banning plugins. However, we’ve optimized our platform for high-performance, reliability, and security. Because of this, there are some plugins that are not allowed or won’t work properly in the Kinsta environment. If a plugin is on our list, it’s because our sysadmin team has identified an issue with it. These problems are typically tied to performance or functionality.

With that being said, we are always working with third-party plugin developers to ensure compatibility with our platform. For example, [WP Rocket](https://kinsta.com/blog/wp-rocket/) used to be on our banned list and now we are partners with them.

We are excited to share that the most recent removal from the list is Wordfence! **You can now use Wordfence at Kinsta.**

Note: Due to how our infrastructure is set up with Google Cloud Platform, in some cases, certain features like IP blocking might not work as intended.

We hope you like all the changes! We’ll keep them coming.
