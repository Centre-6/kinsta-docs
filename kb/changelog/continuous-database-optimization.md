---
url: "https://kinsta.com/changelog/continuous-database-optimization/"
title: "Continuous Database Optimization: Always Working for You"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2024-08-01T14:43:55"
change_signal: "2024-08-01T14:43:55"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "7ced60ab169fc3f49e450e4aaa5d15173a1f29ea3cded01e69c06c0f17b176bd"
body_chars: 3249
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Continuous Database Optimization: Always Working for You

**Product:** Changelog
**Source:** https://kinsta.com/changelog/continuous-database-optimization/
**Kinsta last updated:** 2024-08-01T14:43:55

---

In late 2019 we introduced a system that automatically fine-tuned low-level database settings for all our [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/) customers. Back then, our auto-optimization routines would run once a week for each customer’s WordPress site, looking for ways to make [its database](https://kinsta.com/blog/wordpress-database/) operate more efficiently.

Now, **automatic database optimization happens continuously**, 24 hours a day.

At Kinsta, each Managed WordPress site is backed by an open-source MariaDB relational database, a drop-in replacement for [MySQL](https://kinsta.com/blog/mariadb-vs-mysql/), the long-time workhorse of the [web hosting](https://kinsta.com/blog/what-is-web-hosting/) world.

The MariaDB/MySQL technology and its InnoDB storage engine use data caching to speed up responses to queries. Caches use up chunks of RAM, as do other database actions, like wrangling connections. By tweaking the settings for such processes on the fly, our automated optimization helps ensure customer databases are ready to handle the loads they can expect without gobbling up memory they don’t need.

## Additional Tips for WordPress DB Optimization

It’s important to highlight that Kinsta’s automatic [database optimization](https://kinsta.com/blog/wordpress-database-optimization/) works at a low level and does **not** involve optimizing tables in the RDBMS. This means there are additional steps you can take to further optimize your WordPress database.

The database behind a WordPress site often ends up with a significant amount of unused records in a table known as **wp_options**. You might find data from [long-removed plugins](https://kinsta.com/blog/uninstall-wordpress-plugin/) and themes in that table, taking up space and slowing responses to queries. That’s why we’ve got some tips on cleaning up **[wp_options](https://kinsta.com/blog/wp-options-autoloaded-data/)** [auto-loaded data](https://kinsta.com/blog/wp-options-autoloaded-data/).

On top of this, Kinsta customers can run `wp db optimize` on the command line of an SSH session, which copies and rebuilds database tables, loading all the valid records in index order for more efficient querying.

## We Make Your WordPress Site Faster

When thinking about WordPress optimization, remember that your [hosting platform can affect site performance](https://kinsta.com/blog/how-hosting-affects-seo/). Kinsta’s Managed WordPress Hosting is powered by Google Cloud’s lightning-fast [C2](https://kinsta.com/wordpress-hosting/) and [C3D](https://kinsta.com/blog/wordpress-performance-benchmarks/) virtual machines and [its low-latency Premium Tier network](https://kinsta.com/blog/cloud-platform-for-developers/).

On top of that is our [blazingly fast CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#kinstas-cdn) with 300+ PoPs and [HTTP/3 support](https://kinsta.com/blog/http3/), [edge caching](https://kinsta.com/changelog/edge-caching/), [early hints](https://kinsta.com/changelog/early-hints/), and built-in [image optimization](https://kinsta.com/changelog/wordpress-image-optimization/).

Find a Managed WordPress Hosting package here at Kinsta that’s [right for you](https://kinsta.com/pricing/).
