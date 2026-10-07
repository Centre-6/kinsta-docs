---
url: "https://kinsta.com/changelog/free-migrations-php-threads/"
title: "More Free Migrations, PHP Threads, Improved Caching, Emails"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-05-21T14:46:04"
change_signal: "2026-05-21T14:46:04"
fetched_at: "2026-10-07T22:58:23Z"
sha256: "57df7768b6a6022017b4838877ed2af6fd78541be45ca248df269e0ddadebc46"
body_chars: 6136
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# More Free Migrations, PHP Threads, Improved Caching, Emails

**Product:** Changelog
**Source:** https://kinsta.com/changelog/free-migrations-php-threads/
**Kinsta last updated:** 2026-05-21T14:46:04

## On this page

  - [Starter Plan Free Migration – No More Annual Pay!](#starter-plan-free-migration-no-more-annual-pay)
  - [Added More Free Migrations to Pro, Business 1, and Business 2 Plans](#added-more-free-migrations-to-pro-business-1-and-business-2-plans)
  - [We’ve Added More Hosts to Our Unlimited Free Migrations Offer](#weve-added-more-hosts-to-our-unlimited-free-migrations-offer)
  - [Increased PHP Threads on Business 1 and Business 3 Plans](#increased-php-threads-on-business-1-and-business-3-plans)
  - [We Now Cache 404 Pages](#we-now-cache-404-pages)
  - [POST Requests Now Show in MyKinsta Analytics](#post-requests-now-show-in-mykinsta-analytics)
  - [You Can Now Add CAA DNS Records](#you-can-now-add-caa-dns-records)
  - [Downloadable Backup Emails](#downloadable-backup-emails)

---

It’s that time again, we’ve got another round of feature updates to share with you regarding exciting changes to Kinsta’s hosting plans and our MyKinsta dashboard!

Our team has listened to your feedback, and we’ve made it happen. While other hosts are raising prices, we are dedicated to finding ways to add even more value to our existing plans.

### Starter Plan Free Migration – No More Annual Pay!

Previously our Single plan required that you pay annually to be eligible for a free migration by our support team. No more! 🥳 All plans from Single 35k to Enterprise WP now include one or more free migrations, no exceptions.

You can see how many free migrations you have available in the MyKinsta dashboard under [Migrations](https://my.kinsta.com/migrations). These changes are already in place across the board.

![MyKinsta free migrations](https://kinsta.com/wp-content/uploads/2019/06/mykinsta-free-migrations.png)

MyKinsta free migrations

### Added More Free Migrations to Pro, Business 1, and Business 2 Plans

We’ve added more free migrations (handled by our team) to a few of our hosting plans. Changes:

- WP 2 plan now includes **2 free migrations** (previously 1).
- Wp 5 plan now includes **3 free migrations** (previously 1).
- WP 10 plan now includes **3 free migrations** (previously 2).

This includes all types of plans, such as our [15% discount for nonprofits and charities](https://kinsta.com/wordpress-hosting/nonprofits/).

### We’ve Added More Hosts to Our Unlimited Free Migrations Offer

We’ve **added [SiteGround](https://kinsta.com/siteground-alternative/), [A2 Hosting](https://kinsta.com/a2-hosting-alternative/), and tsoHost** to our unlimited free migrations offer! If you have a lot of WordPress sites and are thinking of moving to Kinsta, make sure to [check out this offer](https://kinsta.com/wordpress-hosting/migration/).

### Increased PHP Threads on Business 1 and Business 3 Plans

[PHP threads](https://kinsta.com/blog/php-threads/) determine **how many simultaneous requests your site can handle at a given time**. To put it simply, each uncached request for your website is handled by a PHP Thread.

We [recommend](https://kinsta.com/blog/php-threads-ecommerce/) our Business 1 or higher plans to those of you running membership sites, ecommerce (WooCommerce, Easy Digital Downloads), LMS, etc. This is due to the fact that they typically have a lot of uncacheable content and concurrent users.

To improve performance for you, we’ve increased the number of PHP threads on the following plans:

- Business 1 plan now includes **4 PHP threads** (previously 2)
- Business 3 plan now includes **6 PHP threads** (previously 4)

This change has been made for all current Kinsta clients.

### We Now Cache 404 Pages

404 pages can be very resource intensive. A lot of WordPress sites, especially large membership sites, generate more 404 errors than you might think. Perhaps you changed the location of a page and forgot to add a redirect, or you have a wrong link on something you shared on social media.

In other words, there are many things that cause a visitor to end up on your 404 page. These pages also tend to have queries to pull alternate search results which then hit the database.

To ensure better performance on your WordPress site, **Kinsta now caches 404 pages for 15 minutes**. The `X-Kinsta-Cache` header value will show a `HIT`, meaning it’s being served from cache. If you create a page which previously was a 404, the cache is purged immediately.

Our [MyKinsta analytics](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/) tool can help you determine the exact amount of 404 errors happening on your site.

![404 error breakdown](https://kinsta.com/wp-content/uploads/2017/11/404-error-breakdown.png)

404 error breakdown

It’s important to clarify though that we don’t cache all 404 requests. There are two different kinds: those from PHP pages which land on your 404 page, and those from missing files or images which no longer exist or have been moved. We cache 404 pages, 404 requests to missing files and images are handled differently.

### POST Requests Now Show in MyKinsta Analytics

**We want our analytics and caching statistics to be as accurate as possible**. It’s important because when troubleshooting performance issues, you typically will look at your total cache HIT ratio, which you want to be as high as possible. Therefore, we’ve now added POST requests to our reporting.

POST requests cannot be cached, apart from some highly specialized setups. The `X-Kinsta-Cache` header value will show a `BYPASS` for these requests. These are not to be confused with blog posts or any type of WordPress post (which are cacheable). A POST request is used to send data to the server. So for example, the data sent when you submit a web form.

### You Can Now Add CAA DNS Records

Kinsta includes Amazon Route 53 premium DNS with all our hosting plans. We’ve now added the ability to add [CAA records](https://docs.aws.amazon.com/acm/latest/userguide/setup-caa.html) within our [Kinsta DNS tool](https://my.kinsta.com/domains).

![CAA DNS record](https://kinsta.com/wp-content/uploads/2019/06/CAA-dns-records.png)

CAA DNS record

### Downloadable Backup Emails

Kinsta offers 6 [different types of backups](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/#wordpress-backups), one of those being downloadable backups. These are an archive file with your website’s files as well as the SQL file containing the contents of your database.

Previously when you downloaded a backup you would simply get a message via the MyKinsta dashboard. However, many of you let us know that you also wanted an email. So in addition to the MyKinsta message, you will also now **get an email with a download link** when your downloadable backup is ready.

![Downloadable backup email](https://kinsta.com/wp-content/uploads/2019/06/downloadable-backup-email-kinsta.png)

Downloadable backup email

If you like seeing these smaller updates that the Kinsta team is constantly pushing out, let us know on Twitter [@kinsta](https://twitter.com/kinsta).
