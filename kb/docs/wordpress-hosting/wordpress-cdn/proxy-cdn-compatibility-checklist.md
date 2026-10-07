---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/proxy-cdn-compatibility-checklist/"
title: "Other CDN Providers"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-cdn"
section: ["WordPress Hosting", "CDN"]
kinsta_last_updated: "2026-03-09T10:53:20"
change_signal: "2026-03-09T10:53:20"
fetched_at: "2026-10-07T22:58:19Z"
sha256: "ce15df0de3237a9f65f45decf4d70d0ba63231c0070a9800fbafb262d7038503"
body_chars: 5628
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Other CDN Providers

**Section:** WordPress Hosting > CDN
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/proxy-cdn-compatibility-checklist/
**Kinsta last updated:** 2026-03-09T10:53:20

## On this page

- [Preliminary proxy and CDN checklist](#preliminary-proxy-and-cdn-checklist)
  - [1. Does the service allow you to use Cloudflare IP addresses for your site’s server (backend host)?](#1-does-the-service-allow-you-to-use-cloudflare-ip-addresses-for-your-sites-server-backend-host)
  - [2. Does the proxy service support sending Server Name Indication (SNI) or host header details?](#2-does-the-proxy-service-support-sending-server-name-indication-sni-or-host-header-details)
- [Advanced proxy and CDN checks](#advanced-proxy-and-cdn-checks)
  - [Cache](#cache)
  - [SSL, HTTPS, and TLS](#ssl-https-and-tls)
  - [Firewall, WAF, DDoS mitigation, and bot detection](#firewall-waf-ddos-mitigation-and-bot-detection)
  - [Analytics](#analytics)
  - [Image optimization](#image-optimization)
- [Summary](#summary)

---

While we generally recommend Kinsta customers take advantage of our [Cloudflare integration](https://kinsta.com/blog/cloudflare-integration/), we understand that some sites may need to use an external proxy or CDN. We’ve tested several notable CDN and proxy services for compatibility, which we’ve documented in the articles below:

1. [Fastly](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/fastly-cdn)
2. [CloudFront](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/cloudfront/)
3. [Imperva](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/imperva-cdn/)
4. [Sucuri](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/sucuri/)
5. [Ezoic](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/ezoic/)

This article doesn’t focus on a specific service, but rather, it’ll provide you with guidelines on how to check for compatibility of an external proxy or CDN provider with Kinsta’s Cloudflare integration.

## Preliminary proxy and CDN checklist

### 1. Does the service allow you to use Cloudflare IP addresses for your site’s server (backend host)?

This determines how the service connects to your Kinsta-hosted site. In some rare cases, a service may block certain IP addresses from being added.

If you can add your site’s IP address to the proxy service’s backend host or server configuration, you can proceed to the next step. If the proxy service shows an error and doesn’t allow you to add the IP, try using `hosting.kinsta.cloud` as the hostname instead.

### 2. Does the proxy service support sending Server Name Indication (SNI) or host header details?

Modern browsers use Server Name Indication (SNI), and your proxy or CDN provider should also support this. The service must be able to send the correct host header in its requests to your site’s server so that it matches the domain you’ve configured at Kinsta.

For example, if your proxy or CDN is using example.com, but your Kinsta site’s primary domain is production-site.com, the proxy needs to allow you to override the host header so it uses production-site.com.

This ensures your site’s server recognizes the incoming request correctly and responds with the [correct SSL certificate](https://kinsta.com/blog/types-of-ssl-certificates/) and the right website content.

If you’re unsure where to configure this setting, ask your proxy or CDN provider’s support team for guidance.

## Advanced proxy and CDN checks

If your service passes the preliminary checks above, you can move on to checking for individual service features for your specific needs.

We can’t cover all scenarios here, but below are some features to consider when checking for compatibility:

### Cache

If the service provides [caching](https://kinsta.com/blog/what-is-cache/), keep this extra layer of cache in mind when making site changes. This redundant layer of caching will also need to be cleared anytime you need to clear cache.

If you’re having [trouble seeing changes on your site](https://kinsta.com/blog/wordpress-changes-not-showing/), or a plugin isn’t behaving as expected after installing or reinstalling, be sure you clear cache at all layers, including:

1. Plugins (if applicable)
2. Themes (if applicable)
3. [Site/server cache at Kinsta](https://kinsta.com/blog/wordpress-cache/#clearing-wordpress-cache) (from either MyKinsta or the Kinsta MU plugin)
4. Caching at your proxy or CDN
5. [Browser cache](https://kinsta.com/blog/how-to-clear-browser-cache/)

### SSL, HTTPS, and TLS

Kinsta supports [TLS](https://kinsta.com/blog/tls-vs-ssl/) versions 1.2 and above, and the proxy or CDN service should too.

You can use SSL between your proxy service and Kinsta, but it’s important to not set conflicting settings. For example, if you [force HTTPS at Kinsta](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/#redirect-http-to-https-in-mykinsta), you may not be able to force HTTPS at your service too. If you try to force HTTP in one place and HTTPS in another, it will undoubtedly cause a [redirect loop](https://kinsta.com/blog/err_too_many_redirects/).

### Firewall, WAF, DDoS mitigation, and bot detection

You can use a combination of these at your proxy or CDN service in addition to what Kinsta’s Cloudflare integration provides, but do so with caution. If you need to troubleshoot any IP blocks caused by false positives, you’ll first need to check with your proxy or CDN service to see if they’re blocking the IP address in question. If they aren’t, you’ll also need to check with our [Support team](https://kinsta.com/docs/support/contact-support/) to see if the IP is blocked at Kinsta.

### Analytics

If your proxy service sends a proper X-Forwarded-For or similar header containing the original visitor IP address, analytics should continue to work as expected through both your proxy service and Kinsta.

### Image optimization

This feature can be used at your CDN or proxy service, **or** with a WordPress plugin. To avoid unexpected results, you shouldn’t use multiple image optimization tools.

## Summary

Now that you have a checklist for your third-party CDN or proxy service compatibility, you can use it to determine if your service is likely to be compatible with Kinsta’s Cloudflare integration.

If things aren’t working as expected at your service, we recommend checking settings and contacting your CDN or proxy service support team for help with troubleshooting and resolving any conflicts. If anything on the server-side needs to be checked or fixed, our [Support team is available to assist you 24/7 via chat](https://kinsta.com/docs/support/contact-support/).
