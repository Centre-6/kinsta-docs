---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/imperva-cdn/"
title: "CDN - Imperva CDN"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-cdn"
section: []
kinsta_last_updated: "February 11, 2026"
sitemap_lastmod: "2026-02-11T16:47:51+00:00"
fetched_at: "2026-10-07T22:39:24Z"
sha256: "b1d705ef66a9f0e8046207cffd872729a84b85705d70ea743d76a591693b2f5c"
body_chars: 15518
extracted_with: "main article"
status: "live"
---

# CDN - Imperva CDN

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/imperva-cdn/
**Kinsta last updated:** February 11, 2026

## On this page

- [How to install and configure Imperva](#how-to-install-and-configure-imperva)
  - [1. Go to the Imperva application](#1-go-to-the-imperva-application)
  - [2. Add your website](#2-add-your-website)
  - [3. Add SAN](#3-add-san)
  - [4. Activate SSL](#4-activate-ssl)
  - [5. Verify ownership](#5-verify-ownership)
    - [How to verify domain ownership](#how-to-verify-domain-ownership)
  - [6. Add TXT record](#6-add-txt-record)
  - [7. Start validation](#7-start-validation)
  - [8. Point DNS](#8-point-dns)
  - [9. Point your site](#9-point-your-site)
  - [10. Complete onboarding](#10-complete-onboarding)
  - [11. Create a custom cache rule](#11-create-a-custom-cache-rule)
- [Troubleshoot common Imperva issues](#troubleshoot-common-imperva-issues)
  - [Changes aren’t showing up on your site](#changes-arent-showing-up-on-your-site)
  - [Potential cache conflicts](#potential-cache-conflicts)
  - [IP address blocked by false positive](#ip-address-blocked-by-false-positive)
  - [Plugin or theme issues](#plugin-or-theme-issues)
- [Advanced settings and compatibility](#advanced-settings-and-compatibility)
  - [Web protection — DDoS settings](#web-protection-ddos-settings)
  - [HTTP to HTTPS redirection](#http-to-https-redirection)
  - [Login protect](#login-protect)
- [Summary](#summary)

---

Imperva’s Content Delivery Network is the current generation of what was formerly known as Incapsula CDN, which stood on its own as a separate company until it was fully acquired by Imperva and became a product line there in 2014. Once you’ve [launched your site at Kinsta](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/go-live-checklist/), if you would like to use Imperva’s CDN instead of [Kinsta’s CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/), this guide shows you how.

## How to install and configure Imperva

If you don’t already have an Imperva account, you can sign up for a [free trial](https://www.imperva.com/free-trial/) to get started.

### 1. Go to the Imperva application

Log into your Imperva Cloud Security Console and go to the **Application** tab.

![Navigate to the Application tab in Imperva.](https://kinsta.com/wp-content/uploads/2021/08/imperva-application-tab.png)

Navigate to the Application tab in Imperva.

### 2. Add your website

Under **Add Your Website** enter your site’s domain name in the **Add a website** field. Be sure to enter the one visitors will use to reach your site ([www or non-www](https://kinsta.com/blog/wordpress-seo/#16-choose-your-preferred-domain), or even a [subdomain](https://kinsta.com/blog/wordpress-subdomain/) if that’s what your site uses) and click the **Add website** button.

![Enter your site’s domain name in the Imperva console.](https://kinsta.com/wp-content/uploads/2021/08/imperva-add-website.png)

Enter your site’s domain name in the Imperva console.

### 3. Add SAN

This will kick off a scan of your domain’s DNS records. Once that’s complete, you’ll see your current DNS records and options for the Imperva SSL certificate. In most cases, you’ll want to select both **Add wildcard domain SAN** and **Add naked domain SAN**, especially if your site uses the www prefix. An exception will be if the site you’re adding uses a subdomain. In that case, you would want to only select the **Add full domain SAN** option and uncheck **Add naked domain SAN**. Once you’ve made your selections, click the **Continue** button in the lower right corner.

![Select add wildcard domain SAN and Add naked domain SAN.](https://kinsta.com/wp-content/uploads/2021/08/imperva-scan-complete-wildcard-san-naked-domain.png)

Select add wildcard domain SAN and Add naked domain SAN.

### 4. Activate SSL

After a few minutes, you’ll see the Configure SSL step. Click on the **Let’s start** button in the lower right corner to activate SSL.

![Click the Let's start button to configure your SSL at Imperva.](https://kinsta.com/wp-content/uploads/2021/08/imperva-activate-ssl-start.png)

Click the Let’s start button to configure your SSL at Imperva.

### 5. Verify ownership

The next screen shows you a TXT record to add to your domain in order to verify ownership so SSL can be installed.

#### How to verify domain ownership

There are two methods for you to verify ownership of your domain and successfully proceed with installing an [SSL certificate](https://kinsta.com/blog/types-of-ssl-certificates/). You can:

1. Verify via email
2. Verify via DNS (TXT Record) — Recommended

While you could use email, the process is limited to certain email addresses only. That’s why we strongly recommend the DNS method, and that’s what we’ll cover here. Click the copy (clipboard) icon to copy the value field that starts with globalsign-domain-verification= so you can add it to your DNS records for verification (see the next step).

![Copy the TXT record to verify your domain for SSL installation.](https://kinsta.com/wp-content/uploads/2021/08/imperva-activate-ssl-copy-txt-record.png)

Copy the TXT record to verify your domain for SSL installation.

### 6. Add TXT record

To add the TXT record, log into where you manage your domain’s DNS. For this example, we’ll show you how to add this [TXT record in Kinsta’s DNS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/#txt-record). If you have a different DNS provider (could be your registrar or other DNS hosting, depending on where you’ve pointed your domain’s nameservers), the steps may be a little different.

1. In [MyKinsta](https://kinsta.com/MyKinsta/), click **DNS management**.
2. Click on the domain you want to add a DNS record to.
3. Click the **Add a DNS record** button.
4. Click on the **TXT** tab and add the value you copied from Imperva to the **Content** value. Leave the Hostname blank unless you’re adding this to a subdomain, in which case you’d add the subdomain to the Hostname field. Click the **Add DNS record** button to save your new TXT record.

![Add the DNS TXT record to verify your domain for your SSL.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-add-imperva-dns-txt-1024x637.png)

Add the DNS TXT record to verify your domain for your SSL.

Note: It may take up to 1 hour for your new [DNS record to propagate](https://kinsta.com/blog/dns-propagation/).

### 7. Start validation

After [DNS has propagated](https://kinsta.com/blog/dns-propagation/#What-is-DNS-Propagation?), you can click the **I added the TXT records** button in Imperva to start the validation.

![Click I added the TXT records button.](https://kinsta.com/wp-content/uploads/2021/08/imperva-activate-ssl-txt-added.png)

Click I added the TXT records button.

Once that’s complete, you’ll see the notification that an SSL certificate was issued and SSL traffic is enabled. Click the **Continue** button in the lower right corner to move on to the next step.

![Click continue to activate your SSL certificate at Imperva.](https://kinsta.com/wp-content/uploads/2021/08/imperva-ssl-certificate-issued-and-enabled.png)

Click continue to activate your SSL certificate at Imperva.

### 8. Point DNS

![Update your DNS records.](https://kinsta.com/wp-content/uploads/2021/08/imperva-copy-dns-to-change.png)

Update your DNS records.

With SSL installed and enabled, you’ll see information on pointing DNS. Copy both of the A records and the CNAME shown in step 4 in your Imperva console.

### 9. Point your site

Next, you’ll need to point your site to Imperva. Once again, we’ll be showing you how to do this in Kinsta’s DNS. These steps may vary depending on your DNS provider.

1. If you aren’t already in DNS in MyKinsta, click [**DNS management**](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/#how-to-add-dns-records).
2. Click on the domain you want to add a DNS record to.
3. If you already have an existing A record for your domain, click the Edit (pencil) icon to update this to the first IP address shown at Imperva. Otherwise, click the **Add a DNS record** button.
   1. Leave the Hostname blank unless you’re adding the A record to a subdomain (add the subdomain as Hostname in that case)
   2. IPv4 Address: The first IP address shown in your Imperva console.
   3. Click the **Change DNS record** button (updating a DNS record) or **Add DNS record** button (adding a new DNS record) to save your DNS record.
      ![Change your A record to point to Imperva.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-update-imperva-dns-a-1-1024x469.png)

      Change your A record to point to Imperva.

      ![Add an A record to point to Imperva.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-add-imperva-dns-a-1024x536.png)

      Add an A record to point to Imperva.
4. Click the **Add a DNS record** button again and add an A record for the second IP address from Imperva.
   1. Leave the Hostname blank unless you’re adding the A record to a subdomain (add the subdomain as Hostname in that case)
   2. IPv4 Address: The second IP address shown in your Imperva console.
   3. Click the **Add DNS record** button to save your DNS record.
      ![Add an A second record to point to Imperva.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-add-imperva-dns-a-2-1024x534.png)

      Add an A second record to point to Imperva.
5. If you already have an existing CNAME record for the www hostname, click the Edit (pencil) icon to update it. Otherwise, click the **Add a DNS record** button and select the CNAME tab.
   1. Hostname: www
   2. Points to: The hostname to point www to as shown in your Imperva console.
   3. Click the **Change DNS record** button (updating a DNS record) or **Add DNS record** button (adding a new DNS record) to save your DNS record.
      ![Edit your www CNAME record to point to Imperva.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-update-imperva-dns-cname-1024x466.png)

      Edit your www CNAME record to point to Imperva.

      ![Add a www CNAME record to point to Imperva.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-add-imperva-dns-cname-1024x467.png)

      Add a www CNAME record to point to Imperva.

Note: It may take up to 1 hour for your DNS records to propagate.

### 10. Complete onboarding

Once DNS propagates back in your Imperva console, click the **Done** button in the lower right corner to complete the initial onboarding steps.

![Click the Done button to complete onboarding in Imperva.](https://kinsta.com/wp-content/uploads/2021/08/imperva-dns-records-added.png)

Click the Done button to complete onboarding in Imperva.

### 11. Create a custom cache rule

Now that DNS is pointed and onboarding is complete, you’ll be taken to the Website Settings screen. The last step is to create a Custom Cache Rule to prevent caching of pages that contain certain WordPress cookies. This prevents unintentional caching of dynamic data.

1. In the left sidebar, go to **Cache** (under Configure) and scroll down until you see the **Custom Cache Rules** section. Click on the **Add Rule** button.
   ![Add a custom rule in Impeva cache settings.](https://kinsta.com/wp-content/uploads/2021/08/imperva-cache-custom-add-rule.png)

   Add a custom rule in Impeva cache settings.
2. Set the following rule filters and click the **Add** button:
   1. if: *Cookie Exists
   2. ==
   3. Value: comment_author|wp-postpass|wordpress_logged_in|edd_items_in_cart|woocommerce_items_in_cart
      ![Set the filter for your custom cache rule.](https://kinsta.com/wp-content/uploads/2021/08/imperva-cache-custom-add-rule-filter.png)

      Set the filter for your custom cache rule.
3. In the Editor window, you’ll see your new custom cache rule has been added.
   ![New custom cache rule in the cache rule editor.](https://kinsta.com/wp-content/uploads/2021/08/imperva-cache-custom-rule-filter-added-to-editor.png)

   New custom cache rule in the cache rule editor.
4. Under the Ruler Filter section, set the **Rule Action** to **Don’t Cache Resource**.
   ![Set the Rule Action to Don’t Cache Resource.](https://kinsta.com/wp-content/uploads/2021/08/imperva-cache-custom-select-rule-action.png)

   Set the Rule Action to Don’t Cache Resource.
5. Under **General**, add your Rule Name (e.g., WordPress) and click the **Save** button.
   ![Name your new custom cache rule and save it.](https://kinsta.com/wp-content/uploads/2021/08/imperva-cache-custom-add-rule-name-enable-save.png)

   Name your new custom cache rule and save it.
6. Back on the Cache Settings page, you’ll see your custom rule has been added and enabled.
   ![New custom cache rule saved and enabled.](https://kinsta.com/wp-content/uploads/2021/08/imperva-wordpress-custom-cache-rule.png)

   New custom cache rule saved and enabled.

Now your site is set up and configured at Imperva. If you run into any issues, check out some common issues and solutions in the next section.

## Troubleshoot common Imperva issues

Now that you have Imperva set up with your Kinsta hosted site, what happens if something doesn’t work the way you expect it to? With an additional CDN layer, there are a few things to try when troubleshooting. We’ve covered the most common ones below.

### Changes aren’t showing up on your site

Serving your site through Imperva adds an additional [layer of caching](https://kinsta.com/blog/what-is-cache/) that will need to be cleared anytime you need to clear the cache. If you’re having trouble seeing changes on your site or a plugin isn’t behaving as expected after installing or reinstalling, be sure you clear cache at all layers, including:

1. Plugins (if applicable)
2. Themes (if applicable)
3. [Site/server cache at Kinsta](https://kinsta.com/blog/wordpress-cache/#clearing-wordpress-cache) (from either MyKinsta or the Kinsta MU plugin)
4. [Caching at Imperva](https://docs.imperva.com/bundle/cloud-application-security/page/settings/caching-settings.htm#Purgethecache)
5. [Browser cache](https://kinsta.com/blog/how-to-clear-browser-cache/)

### Potential cache conflicts

A couple of important notes to keep in mind if you enable caching at Imperva:

- Imperva caching may interfere with [IP Geolocation redirections](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/ip-geolocation/) set at Kinsta.
- Including HTML resources in your Imperva cache could lead to exposure of personal information tied to your site visitors or customers.

### IP address blocked by false positive

If false positives occur with DDoS protection, bot detection, and/or WAF enabled at Imperva, you or site visitors may be inadvertently blocked from your site. To see where the IP is being blocked and fix the issue, you’ll need to first check with Imperva’s support team and see if the block is occurring there. If the block isn’t at Imperva, you’ll then need to reach out to our [Support team at Kinsta](https://kinsta.com/docs/support/contact-support/).

### Plugin or theme issues

Some of Imperva’s default rules may interfere with some [plugins](https://kinsta.com/topic/wordpress-plugins/) or [themes](https://kinsta.com/blog/fastest-wordpress-theme/). If a plugin or theme appears to be broken or not working as expected, try disabling the Imperva WAF while [debugging](https://kinsta.com/blog/wordpress-debug/).

## Advanced settings and compatibility

Now that we’ve covered the configuration and some common troubleshooting tips, there are a few more important aspects to keep in mind when your site is using both Imperva CDN and [Kinsta’s Cloudflare integration](https://kinsta.com/blog/cloudflare-integration/).

### Web protection — DDoS settings

Automatic mode is set as default, and Imperva will turn DDoS mitigation rules on when traffic to your site exceeds the threshold. The default threshold is 1,000 requests per second, which can be adjusted in **Advanced DDoS Settings**.

### HTTP to HTTPS redirection

Redirecting from HTTP to HTTPS is recommended and can be set in Imperva by going to **Content and Network Optimization** > **Delivery Settings** > **Redirection**.

### Login protect

If your [WordPress login page](https://kinsta.com/blog/wordpress-login-url/) or directories are [password protected at Kinsta](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/htpasswd/), do not enable this feature in Imperva. You can use one or the other but cannot have both enabled at the same time.

## Summary

If you have any trouble with Imperva on your site, our [Support team](https://kinsta.com/docs/support/contact-support/) is happy to check into and resolve any server-side issues. For any troubleshooting of the Imperva side of things, you’ll need to work with their support team or your developer to resolve those. To stay up to date with the latest on our Cloudflare integration (and new content every month), be sure to [subscribe to our newsletter](https://kinsta.com/wordpress-newsletter/).
