---
url: "https://kinsta.com/docs/wordpress-hosting/caching/"
title: "WordPress Hosting - Caching"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "caching"
section: []
kinsta_last_updated: "May 28, 2026"
sitemap_lastmod: "2026-05-28T07:48:52+00:00"
fetched_at: "2026-10-07T22:38:57Z"
sha256: "ee427accebb59a8d6749c4ff0c37ed4bb61fc0f1617a98ed7e09265cf9e2b129"
body_chars: 5480
extracted_with: "main article"
status: "live"
---

# WordPress Hosting - Caching

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/caching/
**Kinsta last updated:** May 28, 2026

## On this page

- [Clearing cache](#clearing-cache)
  - [Clear cache in MyKinsta](#clear-cache-in-mykinsta)
  - [Clear cache in your WordPress Dashboard](#clear-cache-in-your-wordpress-dashboard)
  - [Clear cache with WP-CLI](#clear-cache-with-wp-cli)
  - [Clear Redis cache with SSH](#clear-redis-cache-with-ssh)

---

Caching is an important part of optimizing your WordPress website, and we make it easy at Kinsta. The following caching options are available within **Sites** > ***sitename*** > **Caching**:

- [Edge caching](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/)
- [CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/)
- [Server caching](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/) (aka full-page caching)
- [Redis](https://kinsta.com/docs/wordpress-hosting/caching/redis-cache/)

![Caching options for your environment in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-caching-1.png)

Caching options for your environment in MyKinsta.

## Clearing cache

**Note:** If your theme or an active plugin on your site has built-in caching, that cache is managed separately from the caching implemented by Kinsta. If you need to clear all cache, we recommend clearing any theme or plugin cache first.

You can clear the cache in your WordPress dashboard, in MyKinsta, or with WP-CLI (in a terminal/SSH client). We outline how to clear each type of cache in its respective guide and combine that information below.

### Clear cache in MyKinsta

To clear the [server](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/), [CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/), and [edge cache](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/) for a single site, go to**Sites** > ***sitename*** > **Caching** > **Clear all caches**. This also clears the Redis object cache if you’ve enabled the [Redis addon](https://kinsta.com/docs/wordpress-hosting/caching/redis-cache/) for your site.

To clear the server, CDN, and edge cache together for one or more sites, including staging sites, at once, go to the **Sites** page, select the checkboxes next to the sites you want, click **Actions**, then **Caching**, and choose **Clear cache**. This also clears the Redis object cache if you’ve enabled the [Redis addon](https://kinsta.com/docs/wordpress-hosting/caching/redis-cache/) for your site.

![Clear all caches for a single site. ](https://kinsta.com/wp-content/uploads/2023/11/wordpress-caching-clear-all.png)

Clear all caches for a single site.

### Clear cache in your WordPress Dashboard

With the [Kinsta MU plugin](https://kinsta.com/docs/wordpress-hosting/kinsta-mu-plugin/) (installed by default on all Kinsta-hosted sites), you can purge cache right from the WordPress dashboard, including:

- Full-page cache.
- Object cache.
- CDN cache.
- All cache.

Log in to your WordPress dashboard.

If you need to clear the cache for the entire site, click the **Clear Cache** link in the admin toolbar near the upper right corner of the page.

![Clear cache from your WordPress dashboard with the Kinsta MU plugin.](https://kinsta.com/wp-content/uploads/2024/03/wordpress-admin-clear-cache.png)

Clear cache from your WordPress dashboard with the Kinsta MU plugin.

To clear the cache for specific URLs or paths automatically when you make changes to your site, you can configure those URLs in the Kinsta MU Plugin Settings. Click **Kinsta Cache** in the left sidebar and add the URLs you want to purge when updates are made. For more information, check out our guide on [Adding Custom Caching URLs](https://kinsta.com/docs/wordpress-hosting/kinsta-mu-plugin/#add-custom-caching-urls) in the Kinsta MU plugin.

- When [Edge Caching](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/) is enabled on your site, clearing the cache with the Kinsta MU plugin also clears the Edge Cache.
- When [Kinsta’s CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/) is enabled, clearing the cache with the Kinsta MU plugin also clears the CDN cache.

### Clear cache with WP-CLI

[Connect to your server with SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) and navigate to your site’s document root:

Copy

```
cd public
```

If the Kinsta Must Use (MU) Plugin is installed on the site, you can clear the full-page cache and the edge cache (when [Edge Caching](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/) is enabled) with this command:

Copy

```
wp kinsta cache purge
```

If you only want to clear the site cache without clearing the edge cache, add the `--site` flag:

Copy

```
wp kinsta cache purge --site
```

When Kinsta CDN is enabled, you can clear the CDN cache by adding the `--cdn` flag:

Copy

```
wp kinsta cache purge --cdn
```

If you’ve added the [Redis addon](https://kinsta.com/docs/wordpress-hosting/caching/redis-cache/) to your site, you can clear the Redis cache by adding the `--object` flag:

Copy

```
wp kinsta cache purge --object
```

To clear **all** cache, add the `--all` flag:

Copy

```
wp kinsta cache purge --all
```

Flush your site’s object cache with the following command:

Copy

```
wp cache flush
```

You can also chain both commands on a single line:

Copy

```
wp kinsta cache purge && wp cache flush
```

Exit SSH with the following command:

Copy

```
quit
```

### Clear Redis cache with SSH

If you’ve added the [Redis addon](https://kinsta.com/docs/wordpress-hosting/caching/redis-cache/) to your site, you can connect to your server with [SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) and flush the Redis cache with the following command:

Copy

```
redis-cli flushall async
```

Exit SSH with the following command:

Copy

```
quit
```
