---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/fastly-cdn/"
title: "CDN - Fastly CDN"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-cdn"
section: []
kinsta_last_updated: "February 11, 2026"
sitemap_lastmod: "2026-02-11T16:46:41+00:00"
fetched_at: "2026-10-07T22:39:23Z"
sha256: "9afc961dca5e340e699fb000123c3dc0ed00713e732bfd1c0b0266a952f35383"
body_chars: 12626
extracted_with: "main article"
status: "live"
---

# CDN - Fastly CDN

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/fastly-cdn/
**Kinsta last updated:** February 11, 2026

## On this page

- [How to install and configure Fastly CDN](#how-to-install-and-configure-fastly-cdn)
  - [1. Create a CDN service](#1-create-a-cdn-service)
  - [2. Configure your hostname](#2-configure-your-hostname)
  - [3. Activate Fastly](#3-activate-fastly)
  - [4. Test your service](#4-test-your-service)
  - [5. Add TLS](#5-add-tls)
  - [6. Make it live](#6-make-it-live)
- [Troubleshooting common issues with Fastly CDN](#troubleshooting-common-issues-with-fastly-cdn)
  - [Changes aren’t showing up on your site](#changes-arent-showing-up-on-your-site)
  - [IP address blocked by false positive](#ip-address-blocked-by-false-positive)
  - [HTTP-HTTPS redirect loops or TLS version errors](#http-https-redirect-loops-or-tls-version-errors)
  - [When you should set host override](#when-you-should-set-host-override)
  - [Serverless computing](#serverless-computing)
  - [Fastly WordPress plugin](#fastly-wordpress-plugin)
- [Summary](#summary)

---

While Fastly is a newer CDN compared to some others, it’s a reliable platform that offers a range of services, including [DDoS](https://kinsta.com/blog/what-is-a-ddos-attack/) mitigation.

## How to install and configure Fastly CDN

In order for Fastly to serve your site over [HTTPS](https://kinsta.com/blog/http-to-https/#what-is-https) (recommended), **you’ll need to have a paid plan** at Fastly so you can add an [SSL certificate](https://kinsta.com/blog/types-of-ssl-certificates/).

If you don’t already have a Fastly account, visit their [signup page](https://www.fastly.com/signup) to get started.

### 1. Create a CDN service

Log in to your Fastly account and click **CDN** > **Create a CDN service**.

![Create a CDN service in Fastly.](https://kinsta.com/wp-content/uploads/2023/11/fastle-create-cdn-service.png)

Create a CDN service in Fastly.

Complete the fields as follows:

- **Service name:**Enter a name for your service, for example, your site name.
- **Domain:** Add your domain. Due to DNS constraints, using the www-version of your domain name (e.g. www.example.com) rather than the apex/non-www version of your domain is generally recommended. If you must use an apex domain, check out this guide to [Using Fastly with apex domains](https://docs.fastly.com/en/guides/using-fastly-with-apex-domains).
- **Host:** Your hostname is your [Site IP address](https://kinsta.com/docs/wordpress-hosting/site-management/ip-addresses/) or hosting.kinsta.cloud. You cannot use the primary domain because it has to be pointed to Fastly to take the service live. While you could technically use the temp domain as your hostname, we recommend using hosting.kinsta.cloud instead because the temp domain can be removed from the site.

Leave the recommended settings as they are and click **Save draft**. Do not Activate the service yet, once it is active you cannot change the configuration settings. If you do activate the service in error, deactivate the service to continue the configuration.

![Add your site information to the Fastly CDN service. ](https://kinsta.com/wp-content/uploads/2023/11/fastle-setup-cdn-service.png)

Add your site information to the Fastly CDN service.

### 2. Configure your hostname

Click **Origins** and then click the edit (pencil) icon next to your hostname or IP address and configure the following fields:

- **Name:** This is a label for the origin, so it can be anything you want. (Default is “Host 1” or similar).
- **Address:** hosting.kinsta.cloud or Site IP address.
- **Enable TLS:** Yes.
- **Verify certificate?** Yes.
- **Certificate hostname:** Your site’s primary domain at Kinsta.
- **SNI hostname:** Your site’s primary domain at Kinsta.

Note: If your site at Kinsta has a different primary domain than the domain used at Fastly, please see the additional information for this under [When You Should Set Host Override](#when-you-should-set-host-override) below.

![Configure your hostname on Fastly.](https://kinsta.com/wp-content/uploads/2023/11/fastle-edit-origin.png)

Configure your hostname on Fastly.

### 3. Activate Fastly

Now that you have your domain and origin details configured, you’re ready to activate your Fastly service, click **Activate**.

Activating the service won’t affect your live site just yet; this will just save your origin server and domain details in your Fastly service.

![Activate Fastly.](https://kinsta.com/wp-content/uploads/2023/11/fastly-activate-1.png)

Activate Fastly.

### 4. Test your service

Now it’s time to test your service to make sure it’s working as expected before you make it live.

This is another step that isn’t technically required but strongly recommended in case any adjustments are needed before making your service live (which will affect your live site).

To test your domain, click **Domains** > **Test domain** on your domain name, which will open your test domain in a new tab in your browser.

![Opening your Fastly test domain.](https://kinsta.com/wp-content/uploads/2023/11/fastly-test-domain-1.png)

Opening your Fastly test domain.

Your test domain’s URL will look like: http://example.com.global.prod.fastly.net (replace www.example.com with your domain name). You can bookmark or send that to someone else if needed.

### 5. Add TLS

After confirming your website looks good on the test domain, it’s time to add [TLS](https://kinsta.com/blog/tls-vs-ssl/) so your site will be loaded over HTTPS.

Fastly offers a couple of different options for TLS, but we’ll only be covering the Fastly-managed certificates option here.

If you need to upload a third-party certificate at Fastly, that option is [available for an additional fee](https://www.fastly.com/pricing/#tls/ssl-secure-connections), and you’ll need to follow their guide for [using certificates you manage](https://docs.fastly.com/en/guides/serving-https-traffic-using-certificates-you-manage) instead of the instructions here.

1. Click **Security** and within **TLS Management**, click **Manage certificates**.
   ![Manage TLS certificates within Fastly.](https://kinsta.com/wp-content/uploads/2023/11/fastly-tls-management.png)

   Manage TLS certificates within Fastly.
2. If this is your first time setting up TLS on a domain in Fastly, click **Get started**. Otherwise, click **Secure another domain** on the right side of the page. In the dropdown that appears, select **Use certificates Fastly obtains for you**.
3. On the **Subscription details** page, within **Domains**, enter your domain name and click **Add**. Select **Let’s Encrypt** as the certification authority and if you’re adding a domain, leave TLS configuration on the default of **TLS 1.3**, click **Submit**.
   ![Add your TLS subscription details within Fastly.](https://kinsta.com/wp-content/uploads/2023/11/fastly-tls-subscription-1.png)

   Add your TLS subscription details within Fastly.
4. On the **Subscription details** page, click the copy (clipboard) icon to copy the target for custom CNAME you’ll need to add to your DNS records for verification.  
   **Note:** When you add your domain in MyKinsta it includes a CNAME verification record, you’ll need to remove that record to verify the domain with Fastly. This won’t affect your domain’s functionality in MyKinsta, the verification record is only required during the initial setup and can be safely deleted afterward.
   ![CNAME record details to verify your domain.](https://kinsta.com/wp-content/uploads/2023/11/fastly-tls-cname.png)

   CNAME record details to verify your domain.
5. To enter your custom CNAME record, log into where you manage your domain’s DNS.  
   We’ll show you how to create this custom [CNAME in Kinsta’s DNS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/#cname-record) as an example here. If you use a different DNS provider (this may be your registrar or other DNS hosting, depending on where you have pointed your domain’s nameservers), the steps may be a little different.
   1. Within MyKinsta, click **DNS management** and select the domain you want to add a DNS record to.
   2. Click **Add a DNS record**, select **CNAME** and add your **Hostname** and **Points to** values. The Hostname needs to be in the format _acme-challenge.www.DOMAIN_NAME (e.g., _acme-challenge.www.myawesomesite.com) and the Points to value needs to be the target you copied from the Verify domain ownership pop-up at Fastly.
   3. Click **Add DNS record** to save your new CNAME record. Note: It may take up to 1 hour for the [DNS record to propagate](https://kinsta.com/blog/dns-propagation/).
      ![Adding your domain verification CNAME in Kinsta's DNS.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-add-fastly-dns-cname-1024x465.png)

      Adding your domain verification CNAME in Kinsta’s DNS.

### 6. Make it live

Once TLS is set up on your Fastly service, you’re ready to take it live. This is done by pointing your domain’s www CNAME to Fastly. The steps to add a CNAME may vary depending on your provider. We’ll use Kinsta’s DNS as an example again here.

1. In MyKinsta, click **DNS management** and select the domain you want to add a DNS record to.
2. If you already have an existing CNAME record for the www hostname, click the Edit (pencil) icon to update it. Otherwise, click the **Add a DNS record** button.
   - Hostname: www
   - Points to: j.sni.global.fastly.net
3. Click **Change DNS record** (updating a DNS record) or **Add DNS record** (adding a new DNS record) to save your DNS record. Note: It may take up to 1 hour for this DNS change to propagate.
   ![Pointing your domain’s www CNAME to Fastly in Kinsta's DNS.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-change-fastly-dns-cname-1024x465.png)

   Pointing your domain’s www CNAME to Fastly in Kinsta’s DNS.

That’s it for setup and configuration.

## Troubleshooting common issues with Fastly CDN

Even if the setup process went through smoothly, it could be the case that you might experience some issues. Here below, we’ve grouped tips on how to troubleshoot the most common ones, along with some advanced settings.

### Changes aren’t showing up on your site

Serving your site through Fastly adds an additional layer of caching that will need to be cleared anytime you need to clear the [cache](https://kinsta.com/blog/what-is-cache/). If you’re having [trouble seeing changes on your site](https://kinsta.com/blog/wordpress-changes-not-showing/) or a plugin isn’t behaving as expected after installing or reinstalling, be sure you clear cache at all layers, including:

1. Plugins (if applicable)
2. Themes (if applicable)
3. [Site/server cache at Kinsta](https://kinsta.com/blog/wordpress-clear-cache/#how-to-clear-wordpress-cache-in-mykinsta) (from either MyKinsta or the Kinsta MU plugin)
4. [Caching at Fastly](https://docs.fastly.com/en/guides/single-purges)
5. [Browser cache](https://kinsta.com/blog/how-to-clear-browser-cache/)

### IP address blocked by false positive

If you have DDoS mitigation or bot detection enabled at Fastly and you or a site visitor are being incorrectly blocked from viewing your site, this may be due to a false positive. If this happens, you’ll need to work with both Fastly support and our [Support team at Kinsta](https://kinsta.com/docs/support/contact-support/) to track down where the block is occurring.

### HTTP-HTTPS redirect loops or TLS version errors

If you see a [redirect loop](https://kinsta.com/blog/err_too_many_redirects/) or TLS version error on your site, check the following settings:

1. Make sure the HTTPS/TLS options from Fastly to the Origin match (**Origin** > **Hosts** > **Show all details).** [See step 4 above](#step-4).
2. Make sure the hostname matches your Kinsta domain. [See step 3 above](#step-3).

### When you should set host override

By default, the host header at Fastly will be the domain you set at Fastly. For your Kinsta site to recognize the request, the host header needs to match a domain in the site’s domains list.

That means if the domain you’re configuring at Fastly is not in your site’s domains list at Kinsta, you’ll need to set the host override for the origin that requests content from Kinsta. That host override needs to be a domain that is in your site’s domains list at Kinsta.

For example, if you’re configuring example.com at Fastly but only have example.kinsta.cloud in your site’s domains list at Kinsta, you’ll need to set the host override for the origin pulling from Kinsta to be example.kinsta.cloud.

### Serverless computing

This can be used for other paths or subdomains that aren’t hosted at Kinsta (e.g. for API calls or other paths outside of your WordPress site).

### Fastly WordPress plugin

[Fastly offers a plugin](https://wordpress.org/plugins/fastly/) that makes managing many of your settings from your WordPress dashboard possible.

Once the [plugin is installed](https://kinsta.com/blog/how-to-install-wordpress-plugins/) and activated, fill in your service ID and API token on the Fastly General settings page in your [WordPress dashboard](https://kinsta.com/blog/wordpress-admin/).

Instructions for finding and creating those are linked from that page. Be sure to save those entries before testing the connection.

## Summary

If you run into any issues with Fastly, we’re happy to help investigate any issues on the server side, but you’ll need to work with Fastly’s support team or your developer for troubleshooting the Fastly side of things.

Be sure to [subscribe to our newsletter](https://kinsta.com/wordpress-newsletter/) to stay up to date with our Cloudflare integration updates (and new content every month).
