---
url: "https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/"
title: "Edge Caching"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "caching"
section: ["WordPress Hosting", "Caching"]
kinsta_last_updated: "2026-05-28T07:52:18"
change_signal: "2026-05-28T07:52:18"
fetched_at: "2026-10-07T22:58:18Z"
sha256: "b461073a3a627a5502c1e7362561bbc0034718fcb790fdf69d1de230058916eb"
body_chars: 17511
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Edge Caching

**Section:** WordPress Hosting > Caching
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/
**Kinsta last updated:** 2026-05-28T07:52:18

## On this page

- [Things to know before enabling edge caching](#things-to-know-before-enabling-edge-caching)
- [Enable edge caching](#enable-edge-caching)
- [Enable mobile cache](#enable-mobile-cache)
- [Clear edge cache](#clear-edge-cache)
  - [Clear cache in MyKinsta](#clear-cache-in-mykinsta)
  - [Clear cache in your WordPress Dashboard](#clear-cache-in-your-wordpress-dashboard)
  - [Clear cache with WP-CLI](#clear-cache-with-wp-cli)
- [Edge cache expiration](#edge-cache-expiration)
- [Test edge caching](#test-edge-caching)
  - [Check edge caching with Kinsta’s HTTP status and redirect checker](#check-edge-caching-with-kinstas-http-status-and-redirect-checker)
  - [Check edge caching with a web browser](#check-edge-caching-with-a-web-browser)
  - [Check edge caching in Terminal](#check-edge-caching-in-terminal)
- [Troubleshooting edge caching](#troubleshooting-edge-caching)
- [Disable edge caching](#disable-edge-caching)
- [Important notes](#important-notes)
- [Performance data](#performance-data)
- [Summary](#summary)

---

[Edge caching](https://kinsta.com/blog/edge-caching/) saves your Kinsta site/page cache (which is only saved to your site’s data center) to any of Cloudflare’s global network of 300+ data centers. When your site visitors load your website in their browser, cached responses will be delivered from the location closest to them, increasing performance and website speed by up to 40%.

Edge caching is included for free with all Kinsta plans. Unlike some similar caching solutions, there’s no additional cost to you, and edge caching doesn’t require a separate plugin.

By default, the cache expires every 24 hours; you can change the [expiration time](#edge-cache-expiration), and you can manually clear the cache. If you manually clear the cache either in MyKinsta, through the WordPress dashboard, or using WP-CLI, it is limited to 1 request every 10 seconds.

## Things to know before enabling edge caching

- Edge caching does not currently respect narrow-scope geolocation cache variations (near country borders, state, city). When IP Geolocation is enabled in MyKinsta (**Sites** > ***sitename*** > **Tools** > **Geolocation**), the cache is saved in each PoP location based on the location of the first visitor to request that particular page.
- Advanced Site Cache custom exclusions (such as combinations of custom cookies and URIs) are not respected by edge caching.
- You can enable edge caching if our Support team has not configured custom cache rules for your site that use custom cookies or geolocation.

## Enable edge caching

To enable edge caching for a single site, go to**Sites** > ***sitename*** > **Caching** > **Edge Caching** > **Enable**.

To enable edge caching for multiple sites, including staging sites, at once, go to the **Sites** page, select the checkboxes next to the sites you want, click **Actions**, then **Caching**, and choose **Change edge caching**.

![Enable edge caching in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-caching-enable-edge.png)

Enable edge caching in MyKinsta.

To confirm, click **Enable Edge Cache**.

![Confirm enabling Edge Caching in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-enable-edge-caching-confirm-1024x558.png)

Confirm enabling edge caching in MyKinsta.

If we detect that custom cache rules have been added, a warning will be shown. If you’re sure those rules will not conflict with edge caching, you can proceed by clicking **Enable Edge Caching**. If you’re not sure, [check with a developer](https://kinsta.com/blog/hire-wordpress-developer/) to see if your site’s custom caching rules will be compatible with edge caching.

## Enable mobile cache

If your website detects mobile browsers and generates pages with markup unique to those devices, you can enable a mobile cache separate from the content for desktop users. If you are unsure about this, please consult with your site developer first.

When edge caching is enabled, you can turn on mobile caching in your site’s **Edge Caching** settings (**Sites** > ***sitename*** > **Caching** > **Edge Caching**). Click the **Enable Mobile Cache** button to take advantage of edge caching for mobile devices.

![Enable mobile edge caching.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-edge-caching-mobile-1.png)

Enable mobile edge caching.

## Clear edge cache

There are a couple of ways you can clear your site’s edge cache. **Note:** If your theme or an active plugin on your site has built-in cache, we recommend clearing the cache there first.

### Clear cache in MyKinsta

To clear the edge cache for a single site, go to**Sites** > ***sitename*** > **Caching** > **Edge Caching** > **Clear cache**.

To clear the [server](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/), [CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/), and [edge cache](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/) together for one or more sites, including staging sites, at once, go to **Sites**, select the checkboxes next to the sites you want, click **Actions**, then **Caching**, and choose **Clear cache**. This also clears the Redis object cache if you’ve added the [Redis addon](https://kinsta.com/docs/wordpress-hosting/caching/redis-cache/) to your site.

![Clear edge cache in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-edge-caching-clear-1.png)

Clear edge cache in MyKinsta.

If you only need to clear specific URLs or paths, enter the URL in the **Clear URL cache** field in the format `https://mydomain.com/path` and click the Clear URL cache button. To also clear the cache for subdirectories under the URL, check the box next to **Clear cache of every subdirectory under the specified URL**.

![Clear edge cache for specific URLs.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-edge-clear-URL-cache-1.png)

Clear edge cache for specific URLs.

This only clears edge caching. If your site cache also needs to be cleared, you’ll need to clear that separately by going to **Caching** > **Server Caching** and clicking the **Clear cache** button.

### Clear cache in your WordPress Dashboard

If the Kinsta Must Use (MU) plugin is installed, you can clear edge caching (and other types of cache) in your WordPress dashboard. Log in to your WordPress dashboard and do one of the following:

- Click the **Clear All Caches** button on the **Kinsta Cache** plugin page in your WordPress dashboard.
- Click the **Clear Caches** link on the WordPress admin toolbar.

Either of these methods will clear both **edge caching** and **site cache**.

![Clear cache in WordPress with Kinsta MU plugin.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-muplugin-clear-caches.png)

Clear cache in WordPress with Kinsta MU plugin.

If you would like the cache to be automatically cleared for specific URLs or paths when you make changes on your site, you can configure those in the Kinsta MU plugin Settings. Click **Kinsta Cache** in the left sidebar and add the URLs you want to purge when updates are made to your site. For more information, check out our guide on [Adding Custom Caching URLs](https://kinsta.com/docs/wordpress-hosting/kinsta-mu-plugin#add-custom-caching-urls) in the Kinsta MU plugin.

### Clear cache with WP-CLI

If the Kinsta Must Use (MU) plugin is installed, you can clear edge caching (and other types of cache) with WP-CLI.

[Connect to your server with SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) and navigate to your site’s document root:

```
cd public
```

If the Kinsta Must Use (MU) Plugin is installed on the site, you can clear the full-page cache and the edge cache (when [edge caching](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/) is enabled) with this command:

```
wp kinsta cache purge
```

To clear **all** cache, add the `--all` flag:

```
wp kinsta cache purge --all
```

## Edge cache expiration

The cache is set to expire every 24 hours by default, but you can adjust this to be longer if needed. To change the cache expiration:

1. Go to [MyKinsta](https://my.kinsta.com/) >**Sites** > ***sitename*** > **Caching** > **Server Caching**.

   ![Change the cache expiration in the Caching tab in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-server-caching-change-expiration.png)

   Change the cache expiration in the Caching tab in MyKinsta.
2. Select **Change cache expiration**, in the modal/pop-up that appears, select your desired cache expiration, and click **Change expiration**.

   ![Select the cache expiration time.](https://kinsta.com/wp-content/uploads/2024/07/wordpress-cache-expiration-confirm-1024x664.png)

   Select the cache expiration time.

This changes the server cache and edge cache expiration. For sites that don’t often change, having a longer cache expiration can be beneficial for performance.

## Test edge caching

Before testing your site with a [website speed test tool](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/website-testing-tools), we recommend inspecting the HTTP headers of a page to confirm it is loading from the edge cache. Below are a few ways to check your site’s HTTP headers.

### Check edge caching with Kinsta’s HTTP status and redirect checker

You can check the HTTP status and redirect chain of any URL with our free [HTTP status and redirect checker](https://kinsta.com/tools/redirect-checker/). Using this tool, you can review the response headers to check whether edge caching is working.

Choose a page that should be served from the edge cache and copy the URL from your browser’s address bar. Paste this URL into the redirect checker tool and run the check.

You should see results like this:

![Edge Cache headers, ki-cache-type and Ki-CFCache-Status, in HTTP status and redirect checker.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-redirect-checker-edge-caching.png)

Edge cache headers, ki-cache-type and Ki-CFCache-Status, in HTTP status and redirect checker.

Scroll down until you see **Response headers**. In this section, there are two headers to check the values of: `ki-cache-type` and `Ki-CF-Cache-Status`. The `ki-cache-type` header should have a value of `Edge`. The `Ki-CF-Cache-Status` header should have a value of `HIT` or `SAVING`.

### Check edge caching with a web browser

You can use your web browser’s built-in developer tools to check whether edge caching is working. For this example, we’ll use Google Chrome to inspect HTTP headers for our site’s homepage. To launch the Chrome developer tools, right-click anywhere on the page and click **Inspect**.

![Inspect with browser dev tools in Chrome.](https://kinsta.com/wp-content/uploads/2022/07/pasted-image-0-1.png "Inspect with browser dev tools in Chrome")

Inspect with browser dev tools in Chrome.

Next, click on the **Network** tab and reload the page. As the page loads, you’ll see a list of the requests on the left-hand side of the developer tools window. Click on the initial page request to verify that edge caching is working correctly.

![Edge Cache headers, ki-cache-type and Ki-CFCache-Status, in the Network tab of browser dev tools.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-edge-caching-console.png)

Edge cache headers, ki-cache-type and Ki-CFCache-Status, in the Network tab of browser dev tools.

In the **Headers** tab, scroll down until you see the **Response Headers**. In this section, there are two headers to check the values of: `ki-cache-type` and `Ki-CF-Cache-Status`. The `ki-cache-type` header should have a value of `Edge`. The `Ki-CF-Cache-Status` header should have a value of `HIT` or `SAVING`.

### Check edge caching in Terminal

If you’re familiar with using Terminal (command line), you can also check HTTP headers with the `curl` command. Use the command below and substitute the URL at the end of the command with your site’s URL.

```
curl -L -s -o /dev/null -D - https://kinstaexample.com
```

After running this command, you should get a response like this:

![Edge Cache headers, ki-cache-type and Ki-CFCache-Status, in the command line.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-edge-caching-terminal-1024x478.png)

Edge cache headers, ki-cache-type and Ki-CFCache-Status, in the command line.

There are two headers to check the values of: `ki-cache-type` and `Ki-CF-Cache-Status`. The `ki-cache-type` header should have a value of `Edge`. The `Ki-CF-Cache-Status` header should have a value of `HIT` or `SAVING`.

## Troubleshooting edge caching

If edge caching doesn’t seem to be working, there are a few things you can check for:

- The value of the `X-Kinsta-Cache` header: Edge caching only caches the response if it was already cached in [Site cache](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/) (full page caching). If the value of `X-Kinsta-Cache` isn’t `HIT`, then the page isn’t cached in Site cache and cannot be cached by edge caching.
- If you expect the page to be cached and it isn’t one commonly excluded from the cache (e.g. wp-admin, cart, my-account, checkout, etc.), you can [check with our Support team](https://kinsta.com/docs/support/contact-support/) to make sure the page doesn’t contain an excluded URL pattern or cookie in the site’s Nginx settings.

## Disable edge caching

To disable edge caching on a single site, go to**Sites** > ***sitename*** > **Caching** > **Edge Caching** > **Disable**.

To disable edge caching for multiple sites, including staging sites, at once, go to the **Sites** page, select the checkboxes next to the sites you want, click **Actions**, then **Caching**, and choose **Change edge caching**.

![Disable Edge Caching.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-caching-edge-disable.png)

Disable Edge Caching.

## Important notes

1. Edge caching will be enabled by default in the near future.
2. Clearing edge cache in all of Cloudflare’s data centers may take 2-5 minutes to fully complete. Once you see the completion notice in MyKinsta, please allow 2-5 minutes for the cache to be cleared in all data centers. If you have a page that needs to be updated more often, our [Support team](https://kinsta.com/docs/support/contact-support/) can help you exclude that page from edge caching.
3. Edge caching can be enabled on live sites and [Premium Staging Environments](https://kinsta.com/docs/wordpress-hosting/staging-environment/). It cannot be enabled for [Standard Staging Environments](https://kinsta.com/docs/wordpress-hosting/staging-environment/).
4. Edge caching is incompatible with narrow-scope geolocation cache variations or advanced site cache custom exclusions like combinations of custom cookies and URIs.
5. Edge caching serves your Kinsta site/page cache but does not serve static assets like images, JavaScript files, and CSS files. [Kinsta CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/), which is independent of edge caching, can be enabled to serve your site’s static assets. If Kinsta CDN is enabled, your site has an additional caching layer managed separately from edge caching. The CDN cache can be cleared with the [Kinsta MU plugin](https://kinsta.com/docs/wordpress-hosting/kinsta-mu-plugin), with [WP-CLI](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/#clear-cache-with-wp-cli) (if the Kinsta MU plugin is installed), or by [clearing the CDN cache](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#how-to-disable-or-purge-kinstas-cdn) in MyKinsta.
6. We have caching rules in place for edge caching to work with standard WordPress, BuddyPress, WooCommerce, and Easy Digital Downloads sites. We exclude common private URIs and cookies, so your WordPress dashboard, forums, cart pages, or anywhere a user is logged in will automatically bypass caching. If you’re using a customized WordPress setup, there may be additional sections of your site that need to bypass the cache or additional rules that need to be added for compatibility. If that is the case, you can always [contact our Support team](https://kinsta.com/docs/support/contact-support/).
7. Edge caching will not work for requests that return a [`Set-Cookie` Response Header](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/#remove-set-cookie-headers). By default, the `Set-Cookie` response header is removed from cached responses in all newly created sites at Kinsta. A `Set-Cookie` response header is typically used to provide data intended for a specific client. Caching that response header could show visitors data that isn’t intended for them.
8. When updating pages in WordPress, there’s no need to manually clear the Site cache or edge caching; both will be automatically cleared.
9. If you [use your own Cloudflare account](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/cloudflare/) for your site, you can use edge caching if you do **not** use [Cloudflare’s Automatic Platform Optimizations (APO)](https://kinsta.com/blog/cloudflare-apo-wordpress/). These two caching methods are incompatible, so you’ll want to use one or the other, not both.
10. Edge caching is incompatible with geolocation-based blocking (geo-blocking) and geolocation-based redirects set in MyKinsta, for example, allowing only certain countries to access your site, or redirecting visitors from specific countries to a different page. Both are enforced at the Nginx level, not at the Cloudflare level, so Cloudflare has no visibility into these rules. When edge caching is enabled, a cached version of your site could be served directly from a Cloudflare data center, bypassing your geo-blocking or redirect rules for that visitor. If it doesn’t matter whether a blocked or redirected location can still reach a cached version of your site, you can enable edge caching.

## Performance data

During our beta phase, we gathered performance data from 91 sites to test the speed improvements of our new edge caching feature. Here are the results:

- The average HTML load time for a site using our page cache (`X-Kinsta-Cache: HIT`) was 0.4909 seconds. The average load time with edge caching was 0.2239 seconds, a 45.6% improvement in speed, or almost cutting load time for HTML in half!
- The average TTFB difference was 51% (0.4025 – 0.2069).

## Summary

If you want a way to speed up your site, give edge caching a try. It makes serving cached content from multiple data centers possible with minimal setup and no additional plugin required.
