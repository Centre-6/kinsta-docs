---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/cloudflare/"
title: "CDN - Cloudflare"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-cdn"
section: []
kinsta_last_updated: "June 23, 2026"
sitemap_lastmod: "2026-06-23T10:54:50+00:00"
fetched_at: "2026-10-07T22:39:15Z"
sha256: "a10d01c7d4be54247d5cc447fd7e1161cbdc78f64466118de50c998da1727cbf"
body_chars: 15033
extracted_with: "main article"
status: "live"
---

# CDN - Cloudflare

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/cloudflare/
**Kinsta last updated:** June 23, 2026

## On this page

- [Use your Cloudflare account with Kinsta’s Cloudflare integration](#use-your-cloudflare-account-with-kinstas-cloudflare-integration)
- [Install and configure Cloudflare](#install-and-configure-cloudflare)
  - [1. Add your domain](#1-add-your-domain)
  - [2. Check your DNS records](#2-check-your-dns-records)
  - [3. Add CNAME records](#3-add-cname-records)
  - [4. Update your domain’s name servers](#4-update-your-domains-name-servers)
- [Cloudflare WordPress plugin](#cloudflare-wordpress-plugin)
- [Troubleshooting common Cloudflare issues](#troubleshooting-common-cloudflare-issues)
  - [Changes aren’t showing up on your site](#changes-arent-showing-up-on-your-site)
  - [SSL error](#ssl-error)
- [Advanced settings and compatibility](#advanced-settings-and-compatibility)
  - [Comparison and compatibility of Cloudflare settings with Kinsta’s Cloudflare integration](#comparison-and-compatibility-of-cloudflare-settings-with-kinstas-cloudflare-integration)
  - [Cache details](#cache-details)
  - [Firewall / WAF details](#firewall-waf-details)
  - [JavaScript challenges](#javascript-challenges)

---

While our free [Cloudflare integration](https://kinsta.com/cloudflare-integration/) will work great for most customers, if you want a little more fine-grained control or need to implement something at Cloudflare not offered by our integration, you can switch your site to use your own Cloudflare account along with Kinsta’s Cloudflare integration.

## Use your Cloudflare account with Kinsta’s Cloudflare integration

Notes:

- This tutorial assumes that you’ve already [added, verified, and pointed](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/) your site’s domain to Kinsta.
- These instructions are for switching your existing domain to use your own Cloudflare account in addition to Kinsta’s Cloudflare integration (a “[Cloudflare domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/#if-your-domain-uses-cloudflare)“).
- In order to use your own Cloudflare account, you’ll need to point your domain’s name servers to Cloudflare. This means if you’re currently using Kinsta’s DNS, you’ll no longer be able to use that, and your domain’s DNS will be managed at Cloudflare.

## Install and configure Cloudflare

If you don’t already have a Cloudflare account, visit their [signup page](https://dash.cloudflare.com/sign-up/) to get started.

### 1. Add your domain

When you log in to your Cloudflare account, enter the domain you want to transfer to Cloudflare select **Quick scan for DNS records**, and click **Continue**.

![Add a site to your Cloudflare account.](https://kinsta.com/wp-content/uploads/2023/11/cloudflare-connect-domain-1.png)

Add a site to your Cloudflare account.

You must then select the required Cloudflare plan for your domain (no minimum plan is required for this to work with Kinsta).

### 2. Check your DNS records

Cloudflare will attempt to pull in DNS records for your domain. Double-check these to make sure all of your domain’s DNS records were correctly copied over.

![Review your DNS records.](https://kinsta.com/wp-content/uploads/2023/11/cloudflare-review-dns-records.png)

Review your DNS records.

### 3. Add CNAME records

1. Remove all existing A records in Cloudflare DNS
2. Add a CNAME record for the root/apex domain, pointing to **[sitename].hosting.kinsta.cloud**. The **[sitename]** must be the **Database name** from the **Database access** section of your site’s **Info** page.
   ![Add a new CNAME record to your domain in Cloudflare.](https://kinsta.com/wp-content/uploads/2023/11/cloudflare-cname-record.png)

   Add a new CNAME record to your domain in Cloudflare.
3. If you already have a CNAME for www, point that to **[sitename].hosting.kinsta.cloud**. If you do not have a CNAME for www, create one pointing to **[sitename].hosting.kinsta.cloud**.
4. Be sure the orange cloud (proxy) is enabled for both CNAME records, and click **Continue to activation**.

### 4. Update your domain’s name servers

At your domain registrar, update your domain’s name servers to point to the ones provided in your Cloudflare account.

![Update your nameservers.](https://kinsta.com/wp-content/uploads/2023/11/cloudflare-update-nameservers.png)

Update your nameservers.

During the propagation period, your site should remain up without any downtime. The domain’s status in MyKinsta may change to “We’re checking to see if your domain’s DNS records point to Kinsta.” This is normal and should resolve itself once propagation is complete.

## Cloudflare WordPress plugin

The Cloudflare plugin isn’t required but is recommended. Features include:

- Fix for WordPress comments appearing from the same IP address
- Automatic cache purging
- Header rewrite to prevent a redirect loop when Cloudflare’s Universal SSL is enabled
- Ability to change settings on Cloudflare account from within the plugin itself (cache purge, security level, [image optimization](https://kinsta.com/blog/optimize-images-for-web/), etc.)
- View analytics such as total visitors, bandwidth saved, and threats blocked
- Support for [HTTP2/Server Push](https://blog.cloudflare.com/announcing-support-for-http-2-server-push-2/)

After [installing the plugin](https://kinsta.com/blog/how-to-install-wordpress-plugins/), you’ll need to enter the email address you use with your Cloudflare account and your [API token](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/). You can view your API token on the [API Tokens page](https://dash.cloudflare.com/profile/api-tokens/) in your Cloudflare profile. Copy the **Global API Key**, add it to the plugin settings, and click on **Save API Credentials**.

![Cloudflare plugin settings in the WordPress dashboard.](https://kinsta.com/wp-content/uploads/2023/11/cloudflare-plugin.png)

Cloudflare plugin settings in the WordPress dashboard.

## Troubleshooting common Cloudflare issues

When adding an extra layer of complexity like a CDN and/or proxy, there may be times when something doesn’t work as expected. Below are some of the most common issues that may arise when using your own Cloudflare account and solutions for those issues.

### Changes aren’t showing up on your site

Using your own Cloudflare account means your site will have an additional [layer of caching](https://kinsta.com/blog/what-is-cache/) that may need to be cleared. If you’re having [trouble seeing changes on your site](https://kinsta.com/blog/wordpress-changes-not-showing/) or a plugin isn’t behaving as expected after installing or reinstalling, be sure you clear cache at all layers, including:

1. Plugins (if applicable)
2. Themes (if applicable)
3. [Site/server cache at Kinsta](https://kinsta.com/blog/wordpress-cache/#clearing-wordpress-cache) (from either MyKinsta or the Kinsta MU plugin)
4. Cache at Cloudflare either in the [Cloudflare dashboard](https://developers.cloudflare.com/cache/how-to/purge-cache#purge-everything) or the [Cloudflare plugin](https://wordpress.org/plugins/cloudflare/).
5. [Browser cache](https://kinsta.com/blog/how-to-clear-browser-cache/)

### SSL error

If you see either of the following errors, this is usually caused by having Flexible SSL enabled in Cloudflare settings:

- “ERR_TOO_MANY_REDIRECTS” in Chrome or
- “The page isn’t redirecting properly” (Firefox).

To resolve this issue, make sure your domain’s SSL/TLS encryption mode (**SSL/TLS** > **Overview**) in Cloudflare is set to **Full**.

## Advanced settings and compatibility

When you use your own Cloudflare account for your site here at Kinsta, there are a few things to be aware of when it comes to Cloudflare settings and compatibility with [Kinsta’s Cloudflare integration](https://kinsta.com/blog/cloudflare-integration/). Below we explain some setting behaviors, including caching, Cloudflare apps, and other [Cloudflare services and features](https://kinsta.com/blog/cloudflare-apo-wordpress/).

While some setting types give your Cloudflare account first priority (and the ability to override our Kinsta Cloudflare integration settings), this isn’t true for all features. We’ll do our best to go over each here.

If you have any questions about specific Cloudflare settings not answered below, open a new [chat with our Support team](https://kinsta.com/docs/support/contact-support/), and we’ll be happy to check into those for you.

### Comparison and compatibility of Cloudflare settings with Kinsta’s Cloudflare integration

| Setting or feature | Your Cloudflare account | Kinsta Cloudflare integration |
| --- | --- | --- |
| [APO](https://www.cloudflare.com/en-gb/automatic-platform-optimization/wordpress/) | This should work as expected.** | You can use APO if you do not use [Edge Caching](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/) at Kinsta. These two caching methods are incompatible, so you’ll want to use one or the other, not both. |
| [Apps](https://www.cloudflare.com/apps/) | Works. | Apps aren’t used with our Cloudflare integration, but you can use and manage them in your Cloudflare account. |
| [Argo Smart Routing](https://www.cloudflare.com/products/argo-smart-routing/) | Not supported. | Not enabled. |
| [Argo Tiered Cache or Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/) | Settings ignored. | Enabled with Kinsta’s Cloudflare integration and cannot be turned off or overwritten by settings in your Cloudflare account. This does not work with [IP Geolocation](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/ip-geolocation/). |
| [Argo Tunnel](https://blog.cloudflare.com/tunnel-for-everyone/) | Not supported. | Not supported. |
| [Bot Management](https://www.cloudflare.com/products/bot-management/) | This should work as expected. | Not enabled, but can be enabled and managed in your Cloudflare account. Note: A configuration that is too strict may block legitimate traffic. |
| [Brotli](https://blog.cloudflare.com/brotli-compression-using-a-reduced-dictionary/) | Settings ignored. | Enabled with Kinsta’s Cloudflare integration and cannot be turned off or overwritten by settings in your Cloudflare account. Even if you disable this in your Cloudflare account, Kinsta’s Brotli setting will still be turned on and will keep it enabled for the site. |
| [Caching](https://developers.cloudflare.com/cache/about/default-cache-behavior) | Works. | Custom caching rules are implemented with our Cloudflare integration. See the [Cache Details section](#cache-details) below for priority details. |
| [Cloudflare Access](https://www.cloudflare.com/en-gb/teams/access/) | This should work as expected.** | Not enabled. |
| [Early Hints](https://developers.cloudflare.com/cache/about/early-hints) | Works. | Can be enabled in Cloudflare and in MyKinsta (**Sites** > ***sitename*** > **Tools**), but there’s no benefit to enabling it in both. |
| [Firewall](https://developers.cloudflare.com/firewall/cf-firewall-rules) / [WAF](https://www.cloudflare.com/waf/) | Works. | Works. Rules can be in place in both your account and our Cloudflare integration. See the [Firewall / WAF Details section](#firewall-waf-details) below for priority details. |
| [Page Rules](https://www.cloudflare.com/features-page-rules/) | Works. | Works, but we don’t set Page Rules for individual sites. Page rules set in your Cloudflare account are applied first in priority. **Note:** Certain cache-related page Rules may behave unexpectedly. If you run into any issues with those, open a new chat with our Support team to help you troubleshoot any cache-related conflicts. |
| [Pages](https://www.cloudflare.com/products/pages/) | Not supported. | Cloudflare Pages isn’t compatible with Kinsta’s hosting services. |
| [Polish + Webp](https://blog.cloudflare.com/introducing-polish-automatic-image-optimizati/) | Works. | Enabled when [Kinsta’s CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/) is enabled and [Image Optimization](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#image-optimization-1) is enabled in CDN settings. Can be enabled in Cloudflare and Kinsta’s CDN, but there’s no benefit to enabling it in both. Settings from your Cloudflare account are not applied. |
| [Rocket Loader](https://blog.cloudflare.com/how-cloudflare-rocket-loader-redefines-the-modern-cdn/) | Works. | Not enabled, but will work if you turn it on in your Cloudflare account (your account’s settings have priority). |
| [Railgun](https://blog.cloudflare.com/deprecating-railgun/) | Not supported. | Not supported. |
| SSL | Works. | Free wildcard SSL is installed by default with our Cloudflare integration. You can also upload a [custom SSL](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/) to Cloudflare (through MyKinsta) if you want. |
| [Signed Exchanges (SXGs)](https://developers.cloudflare.com/speed/optimization/other/signed-exchanges/) | This should work as expected. | Not enabled, but can be enabled and managed in your Cloudflare account. Note: When combined with performance plugins that preload resources, this may interfere with some analytics tools like Google’s mobile speed test. |
| [Waiting Room](https://www.cloudflare.com/en-gb/waiting-room/) | This should work as expected.** | Not enabled, but can be enabled in your Cloudflare account. |
| Websocket | Not supported. | Not supported. |
| [Workers](https://workers.cloudflare.com/) | Works.* | Compatible as long as the worker script doesn’t transform the site’s URL in such a way that it prevents it from loading the domain(s) added to the site in MyKinsta. Traffic goes through your Cloudflare account’s Worker as the first priority. |

* It works, but due to the nature of Workers, Kinsta cannot control how your Worker code manipulates the original request or response. This could lead to an error returned from your Worker code directly (not from the Kinsta container).

** Cloudflare has stated APO should work, but it hasn’t been tested by Kinsta.

### Cache details

You can have your own cache rules in your Cloudflare account, and these should generally work fine with Kinsta’s cache rules. However, there is potential for conflicts, depending on the rules you set in your account.

Cache purging should work both in your Cloudflare account and through MyKinsta ([Tools > Clear cache)](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/). **Note:** With an additional layer of cache, you may need to clear cache in multiple places when making changes to your site.

If unexpected cache behavior is seen, [open a new chat with our Support team](https://kinsta.com/docs/support/contact-support/) and provide your exact Cloudflare cache settings so we can review and advise.

### Firewall / WAF details

The Firewall / WAF settings in your Cloudflare account are applied first, followed by settings in our Cloudflare integration. This means if we block an IP address, your account’s settings cannot override that, and the request will be blocked by our Cloudflare integration.

You can block an IP address in your Cloudflare account, and it will be blocked and will not make it to our Cloudflare integration. So, you can tighten your firewall / WAF settings beyond what we have configured with our Cloudflare integration, but you cannot loosen settings or allow IP addresses that Kinsta has blocked. To learn more about how Kinsta protects your site, refer to [Kinsta Firewall](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/wordpress-infrastructure/#kinsta-firewall).

### JavaScript challenges

[JavaScript challenges](https://developers.cloudflare.com/waf/reference/cloudflare-challenges/#js-challenge) in Cloudflare challenge visitor traffic to determine if it should be allowed to access your site.

To enable JavaScript challenges within Cloudflare, select your domain, open **Security** > **Settings** > **Bot management**, and toggle it to on.

![Enable bot management in Cloudflare.](https://kinsta.com/wp-content/uploads/2023/11/cloudflare-bot-management.png)

Enable bot management in Cloudflare.
