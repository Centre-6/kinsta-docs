---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/bunny/"
title: "CDN - Bunny"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-cdn"
section: []
kinsta_last_updated: "November 7, 2025"
sitemap_lastmod: "2025-11-07T10:26:59+00:00"
fetched_at: "2026-10-07T22:39:03Z"
sha256: "362e3ea7787085a6d7441aa88c41c60b9a825533f1d69133cf809f6d21233dfc"
body_chars: 8452
extracted_with: "main article"
status: "live"
---

# CDN - Bunny

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/bunny/
**Kinsta last updated:** November 7, 2025

## On this page

- [Method 1: Full DNS (nameserver) integration (recommended)](#method-1-full-dns-nameserver-integration-recommended)
  - [Set up your DNS in Bunny](#set-up-your-dns-in-bunny)
  - [Update your nameservers](#update-your-nameservers)
  - [Add your DNS records](#add-your-dns-records)
- [Method 2: Custom CDN Hostname](#method-2-custom-cdn-hostname)
  - [Create a Pull Zone in Bunny](#create-a-pull-zone-in-bunny)
  - [Add a custom hostname](#add-a-custom-hostname)
  - [Add the CNAME record to your DNS](#add-the-cname-record-to-your-dns)
- [Method 3: Use the Bunny.net WordPress plugin](#method-3-use-the-bunnynet-wordpress-plugin)
  - [Install the bunny.net WordPress plugin](#install-the-bunnynet-wordpress-plugin)
  - [Configure the bunny.net plugin](#configure-the-bunnynet-plugin)
- [Clear the CDN cache](#clear-the-cdn-cache)
- [Bunny Shield](#bunny-shield)

---

[Bunny](https://bunny.net/) provides a range of services to enhance your website’s performance and security, including a global CDN, DNS management, caching, storage zones, and video delivery solutions.

Once you’ve [launched your site at Kinsta](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/go-live-checklist/), if you would like to use Bunny’s CDN instead of [Kinsta’s CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/), this guide shows you how.

If you haven’t already signed up for Bunny, head on over to the [Bunny signup page](https://dash.bunny.net/auth/register) to get started.

Bunny offers several ways to integrate its CDN with your WordPress site. The setup method you choose determines how traffic is routed, how Bunny Shield works, and whether your CDN is branded under your own domain.

- **Method 1: Full DNS (nameserver) integration (recommended).** By pointing your domain’s nameservers to Bunny, Bunny manages your DNS and routes all website traffic through its global edge network.
  - Setup: Requires moving DNS to Bunny.
  - Shield: Bunny Shield protects all site traffic, not just static assets.
  - Benefits: Maximum performance, full-site caching, and enhanced security.
  - Limitations: More advanced setup.
- **Method 2: Custom CDN Hostname.** You can create a branded CDN URL by adding a CNAME record in your DNS (for example, cdn.example.com) that points to your Bunny Pull Zone.
  - Setup: Add one CNAME record in your DNS provider.
  - Shield: Bunny Shield protects your origin for static assets only.
  - Benefits: Branded CDN domain, full SSL support, and origin protection.
  - Limitations: Doesn’t cache full site traffic.
- ****Method 3:Plugin Setup.**** The simplest option is to connect Bunny using the Bunny.net WordPress plugin.
  - Setup: No DNS changes needed.
  - Shield: Bunny Shield protects your origin for static assets only.
  - Benefits: Quick setup and easy performance boost.
  - Limitations: Uses Bunny’s shared hostname and doesn’t cache full site traffic.

We recommend using the full DNS (nameserver) integration method, as it offers the highest level of performance and protection for your entire site. In comparison, the custom CDN hostname and plugin methods only protect and accelerate your site’s static assets. Additionally, the plugin setup uses Bunny’s shared CDN hostname instead of one associated with your own domain.

## Method 1: Full DNS (nameserver) integration (recommended)

### Set up your DNS in Bunny

Log in to Bunny, click **DNS**, and then click **Add a Domain**.

![Add a domain in Bunny.](https://kinsta.com/wp-content/uploads/2025/11/bunny-add-domain-1.png)

Add a domain in Bunny.

Enter your domain name and click **Add DNS Zone**.

![Add your DNS zone to Bunny.](https://kinsta.com/wp-content/uploads/2025/11/bunny-add-dns-zone.png)

Add your DNS zone to Bunny.

### Update your nameservers

In a new browser tab, log in to your [domain registrar](https://kinsta.com/blog/best-domain-registrar/). If you’re unsure how to do that with your registrar, check their support documentation or contact their support team for assistance.

Before updating your name servers, take note of or capture screenshots of your existing DNS records, so you can manually add them to Bunny later on. Copy each of the name servers from Bunny and paste them into your registrar. Be sure to **either overwrite the existing name servers or delete them and add the new ones**. Click **Okay, I’m Done**.

![Bunny nameservers.](https://kinsta.com/wp-content/uploads/2025/11/bunny-nameservers.png)

Bunny nameservers.

### Add your DNS records

Within **DNS records**, add each of your DNS records from your domain registrar.

![DNS records in Bunny.](https://kinsta.com/wp-content/uploads/2025/11/bunny-dns-records.png)

DNS records in Bunny.

Allow for [DNS to propagate](https://kinsta.com/blog/dns-propagation/) the name server change. This usually happens within 24 hours, but in some cases it may take 48*–*72 hours. For information on how to verify that your website is correctly configured, refer to [Bunny’s knowledge base](https://support.bunny.net/hc/en-us/articles/360000548992-How-to-check-if-your-website-is-correctly-configured-with-bunny-net/).

## Method 2: Custom CDN Hostname

### Create a Pull Zone in Bunny

Within Bunny, navigate to **CDN** and click **Create Your First Pull Zone**.

![](https://kinsta.com/wp-content/uploads/2025/11/bunny-create-pull-zone.png)

Add a **Pull Zone Name** and **Origin URL**, select the other settings as required, and click **Add Pull Zone**. For more information about these settings, refer to [Bunny’s knowledge base](https://support.bunny.net/hc/en-us/articles/207790269-How-to-create-your-first-Pull-Zone/).

![Pull Zone details in Bunny. ](https://kinsta.com/wp-content/uploads/2025/11/bunny-pull-zone-details.png)

Pull Zone details in Bunny.

### Add a custom hostname

In Bunny, click on the pull zone you set up in the previous step, then click **Hostnames.** Add a custom hostname for your site and click **Add Hostname**.

![Add a custom hostname in Bunny.](https://kinsta.com/wp-content/uploads/2025/11/bunny-add-custom-hostname.png)

Add a custom hostname in Bunny.

### Add the CNAME record to your DNS

When you add the hostname, Bunny provides you with the details for the CNAME record to add to your DNS records at your domain registrar. Log in to your domain registrar and add this record. Make sure the CNAME record is set as non-proxied (proxy disabled, DNS only). Once you’ve added the record, click **Verify & Activate SSL** in Bunny. It may take a few minutes for the DNS to propagate.

![CNAME record details in Bunny.](https://kinsta.com/wp-content/uploads/2025/11/bunny-cname-record.png)

CNAME record details in Bunny.

For information on how to verify that your website is correctly configured, refer to [Bunny’s knowledge base](https://support.bunny.net/hc/en-us/articles/360000548992-How-to-check-if-your-website-is-correctly-configured-with-bunny-net/).

## Method 3: Use the Bunny.net WordPress plugin

### Install the bunny.net WordPress plugin

On the WordPress Dashboard for the website you want to add Bunny to, navigate to **Plugins** > **Add New** and search for “bunny.net”. Install and activate “bunny.net – WordPress CDN Plugin”.

![Install the bunny.net plugin.](https://kinsta.com/wp-content/uploads/2025/11/bunny-install-plugin.png)

Install the bunny.net plugin.

### Configure the bunny.net plugin

In your WordPress dashboard, go to the bunny.net plugin, log in, and click **Integration Wizard**.

![Start the bunny integration wizard.](https://kinsta.com/wp-content/uploads/2025/11/bunny-integration-wizard.png)

Start the bunny integration wizard.

Confirm your site’s URL and go back to the Overview page. Bunny is now set up as your CDN provider. For information on how to verify that your website is correctly configured, refer to [Bunny’s knowledge base](https://support.bunny.net/hc/en-us/articles/360000548992-How-to-check-if-your-website-is-correctly-configured-with-bunny-net/).

You can purge the CDN cache, exclude paths, include directories, and manage various other settings within the WordPress plugin or on the Bunny.net dashboard.

![CDN settings in the Bunny.net plugin.](https://kinsta.com/wp-content/uploads/2025/11/bunny-cdn-settings.png)

CDN settings in the Bunny.net plugin.

## Clear the CDN cache

To clear your CDN cache in the Bunny dashboard, click **CDN**, select your pull zone, and click **Purge Cache**. You can also install and use the bunny.net plugin to clear the cache, as this connects to your Bunny account to retrieve your site’s details.

![Purge the CDN cache in the Bunny dashboard.](https://kinsta.com/wp-content/uploads/2025/11/bunny-purge-cache.png)

Purge the CDN cache in the Bunny dashboard.

To perform a full cache purge, click **Purge**.

![Purge the full CDN cache in Bunny.](https://kinsta.com/wp-content/uploads/2025/11/bunny-purge-cache-confirm.png)

Purge the full CDN cache in Bunny.

## Bunny Shield

You can also set up and configure [Bunny Shield](https://support.bunny.net/hc/en-us/articles/22699526402332-Understanding-and-enabling-Bunny-Shield/) within the Bunny dashboard. It includes a Web Application Firewall (WAF), DDoS mitigation, Rate limiting, Bot detection, and access lists.

![Bunny Shield.](https://kinsta.com/wp-content/uploads/2025/11/bunny-shield.png)

Bunny Shield.
