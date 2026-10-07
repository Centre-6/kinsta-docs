---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/go-live-checklist/"
title: "Get Started - Go Live Checklist"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-getting-started"
section: []
kinsta_last_updated: "April 9, 2026"
sitemap_lastmod: "2026-04-09T12:22:55+00:00"
fetched_at: "2026-10-07T22:39:52Z"
sha256: "9d3bc7dd3ef9fa4610a1f3bc4588202ee24c1e7d0e6aa81f41be792f74cf7aed"
body_chars: 5721
extracted_with: "main article"
status: "live"
---

# Get Started - Go Live Checklist

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/go-live-checklist/
**Kinsta last updated:** April 9, 2026

## On this page

- [1. Test your site](#1-test-your-site)
  - [Previewing your site with your live domain](#previewing-your-site-with-your-live-domain)
- [2. Add your domain to Kinsta](#2-add-your-domain-to-kinsta)
- [3. Set up HTTPS](#3-set-up-https)
- [4. Install the Kinsta MU plugin](#4-install-the-kinsta-mu-plugin)
- [5. Enable Kinsta’s CDN](#5-enable-kinstas-cdn)
- [6. Add redirects](#6-add-redirects)
- [7. Run a speed test](#7-run-a-speed-test)

---

If you’ve just created your first site at Kinsta, and you’re ready to make it live, follow the go-live checklist below to get your website up and running quickly. If you run into any problems or have questions, our Support team is available 24/7, and we’re happy to help.

**Note:** If you’re looking for information on migrating a site, Kinsta includes [free migrations](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrating-to-kinsta/). If you want to migrate the site yourself, we have several resources to help guide you:

- [Manual Migration](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/wordpress-manual-migration/)
- [Migrate with Duplicator](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrate-wordpress-duplicator-plugin/)
- [Migrate with Migrate Guru](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrate-guru/)
- [Migrate WordPress.com to WordPress.org](https://kinsta.com/blog/wordpress-com-to-wordpress-org/)
- [Powerful WordPress Migration Plugins](https://kinsta.com/blog/wordpress-migration-plugins/)

## 1. Test your site

When you [add a site](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/new-site/ "How can I add a new site?") at Kinsta, a [temporary URL](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-temporary-url/) is automatically created for you. You can use this to test your site. (**sitename.kinsta.cloud**). You can see it in [MyKinsta](https://my.kinsta.com/) on the **Domains** tab of your site.

![Kinsta temporary URL.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-domains-temporary-domain.png)

Kinsta temporary URL.

Some plugins are incompatible or banned at Kinsta. For a full list, refer to [Banned and incompatible plugins](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-banned-incompatible-plugins/).

Here’s a handy checklist before moving forward:

- Have a valid WordPress install
- Theme looks good
- Plugins work as needed
- Content is in place

### Previewing your site with your live domain

If you are migrating an existing site and you want to test it before pointing the domain to Kinsta, check out our article on how to [preview your site with our Site Preview tool](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/site-preview/) before updating DNS.

## 2. Add your domain to Kinsta

After you’ve confirmed your site is all good, it’s time to go live with your custom domain. You have two options to achieve this: keep your existing DNS provider and add a DNS record, or use [Kinsta’s premium DNS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/) service powered by Amazon Route53. Both options support our [free Cloudflare integration](https://kinsta.com/blog/cloudflare-integration/), including HTTP/3 support, an enterprise-level firewall, free DDoS protection, and more.

Check out our guide on how to [add a domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/) on Kinsta.

## 3. Set up HTTPS

Once your domain is pointed to your site at Kinsta, it’ll automatically be protected by a free Cloudflare SSL with support for wildcard domains. For customers who prefer to use a custom SSL certificate, we support those as well. For more information on adding a custom SSL, check out our guide on [how to install an SSL certificate](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/).

If you want to redirect all HTTP traffic to HTTPS (we recommend this), we have a handy [**Force HTTPS** tool](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/#redirect-http-to-https-in-mykinsta) in MyKinsta for that.

## 4. Install the Kinsta MU plugin

Our [Kinsta MU plugin](https://kinsta.com/docs/wordpress-hosting/kinsta-mu-plugin/) is automatically installed on new WordPress installations created here at Kinsta. If you migrated your site yourself, you’ll need to download and install the Kinsta MU plugin manually. This includes our full-page caching and other functionality, such as integration with [Kinsta’s CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/).

## 5. Enable Kinsta’s CDN

When you add a new site in MyKinsta, CDN is enabled by default. If you disabled the CDN during testing, be sure to [enable the CDN again on your site](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/).

A CDN typically offloads 70% of bandwidth requests from your web server and can reduce load times by up to 50%! Turning it on is done with a flip of a switch.

If you choose not to use our CDN, we still recommend you set one up. Cloudflare is another great choice. Check out our tutorial on [how to install Cloudflare on your site](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/cloudflare/).

## 6. Add redirects

If you had redirects (301, 302) set up with your old hosting provider, you’ll want to add those in MyKinsta. Using WordPress plugins to implement redirects can sometimes cause performance issues. [Adding redirects in MyKinsta](https://kinsta.com/docs/wordpress-hosting/redirect-rules/) means the rules are implemented at the server level, which is a much more optimal way. For multi-regional sites, our redirects tool supports IP geolocation-based rules as well.

## 7. Run a speed test

Once your site is live on Kinsta, you may want to run a [speed test](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/website-testing-tools/) to measure your site’s performance. Speed test results can vary depending on how you run them, so you’ll want to make sure you are using the correct testing method.
