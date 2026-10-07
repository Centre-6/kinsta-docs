---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/ezoic/"
title: "CDN - Ezoic"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-cdn"
section: []
kinsta_last_updated: "March 9, 2026"
sitemap_lastmod: "2026-03-09T10:55:39+00:00"
fetched_at: "2026-10-07T22:39:44Z"
sha256: "2d4522402f320d1ae9b03a957985f33f262f09913dbaaf780dab180e8efba42c"
body_chars: 10496
extracted_with: "main article"
status: "live"
---

# CDN - Ezoic

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/ezoic/
**Kinsta last updated:** March 9, 2026

## On this page

- [Turn off Ezoic’s Cloudflare integration](#turn-off-ezoics-cloudflare-integration)
- [Install and configure Ezoic](#install-and-configure-ezoic)
  - [Method 1: Connect your site using Ezoic’s name servers (recommended)](#method-1-connect-your-site-using-ezoics-name-servers-recommended)
    - [1. Log in and select name servers](#1-log-in-and-select-name-servers)
    - [2. Copy name servers](#2-copy-name-servers)
    - [3. Log in to your domain registrar](#3-log-in-to-your-domain-registrar)
    - [4. Paste name servers into your registrar](#4-paste-name-servers-into-your-registrar)
    - [5. DNS propogation](#5-dns-propogation)
    - [6. Check DNS records](#6-check-dns-records)
  - [Method 2: Connect your site using Ezoic’s WordPress plugin](#method-2-connect-your-site-using-ezoics-wordpress-plugin)
- [Troubleshooting common issues with Ezoic](#troubleshooting-common-issues-with-ezoic)
  - [SSL errors or redirect loops](#ssl-errors-or-redirect-loops)
  - [Changes aren’t showing up on your site](#changes-arent-showing-up-on-your-site)
  - [Discrepancies in analytics](#discrepancies-in-analytics)
- [Automatic cache clearing with Ezoic’s WordPress plugin](#automatic-cache-clearing-with-ezoics-wordpress-plugin)
    - [1. Enable Ezoic API](#1-enable-ezoic-api)
    - [2. Copy API key](#2-copy-api-key)
    - [3. Paste API key in WordPress](#3-paste-api-key-in-wordpress)
- [Summary](#summary)

---

Ezoic is an AI-powered platform for publishers with a set of tools to improve website performance and ad revenue. Think of [split-testing](https://kinsta.com/blog/wordpress-ab-testing-tools/), site speed and [UX improvements](https://kinsta.com/blog/website-usability-testing/), better ad positioning, and more, all combined in one tool. Once you’ve [launched your site at Kinsta](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/go-live-checklist/), if you would like to use Ezoic instead of [Kinsta’s CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/), this guide shows you how.

## Turn off Ezoic’s Cloudflare integration

Unfortunately, Ezoic’s Cloudflare integration method isn’t compatible with Kinsta’s Cloudflare integration. If you currently have Ezoic configured with Cloudflare (either your own Cloudflare account or an Ezoic-owned Cloudflare DNS zone), you’ll need to turn that off and use the name server integration method with Ezoic before starting the Cloudflare integration steps (**Get Cloudflare** button) in MyKinsta.

First, make a note of or take screenshots of your existing DNS records so that you can compare them after you’ve switched to the name server method outlined below.

1. In your Ezoic account, go to **Settings** and under **Cloudflare** or **Site Integration**, click the **Remove Cloudflare** button to disconnect the Cloudflare integration method.
2. If you have your own Cloudflare account, log in to your Cloudflare account and delete your site’s domain there. If Ezoic owns your Cloudflare DNS zone (you don’t have your own Cloudflare account), you can skip this step.

Now you’re ready to configure your site to use Ezoic’s name servers as detailed below. Once you have that set up and DNS has fully propagated, you can begin the steps in MyKinsta to [add your domain to MyKinsta](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/) or [enable Kinsta’s Cloudflare integration](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/cloudflare/) for an existing domain in MyKinsta. If you see a message in MyKinsta that your domain is using Cloudflare or have any trouble enabling Kinsta’s Cloudflare integration, [contact our Support team](https://kinsta.com/docs/support/contact-support/).

## Install and configure Ezoic

If you don’t already have an Ezoic account, you should visit their [registration page to join](https://pubdash.ezoic.com/join). During the registration process, you’ll be asked to add your site’s live domain, i.e. the one visitors will use to reach your site.

In this article, we’ll cover two methods for connecting your site hosted at Kinsta to Ezoic. Specifically, we’ll cover how to do that using:

- Ezoic’s Name Servers
- Ezoic’s WordPress Plugin

### Method 1: Connect your site using Ezoic’s name servers (recommended)

This method is preferred because it doesn’t require a plugin to do the heavy lifting, which means your site will usually perform a bit better using this option. Here’s how to get started.

#### 1. Log in and select name servers

Log in to your Ezoic account and click **Settings** > **Name Servers** > **View Instructions**.

![Select the Name Server integration method in your Ezoic Settings.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-ezoic-nameservers.png)

Select the Name Server integration method in your Ezoic Settings.

#### 2. Copy name servers

This will show you a table of your Ezoic name servers. Keep this information handy (like opened in a different tab), so you’ll be able to copy your name servers more quickly using the copy icon next to each one.

![Disregard any warnings at Ezoic related to Cloudflare IP addresses in your DNS records.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-ezoic-nameservers-integration.png)

Disregard any warnings at Ezoic related to Cloudflare IP addresses in your DNS records.

Alternatively, to remove any warnings related to Cloudflare IP addresses, you can update the www (or other subdomain) CNAME record pointing to **hosting.kinsta.cloud** and set an ALIAS record for the root/apex domain (@) pointing **hosting.kinsta.cloud** as well. Once those are set, you can delete the A record pointing to your Site IP Address.

#### 3. Log in to your domain registrar

In a new browser tab, log in to your [domain registrar](https://kinsta.com/blog/best-domain-registrar/). If you’re not sure how to do that at your registrar, check their support documentation or contact their support team to help you with that.

#### 4. Paste name servers into your registrar

Before updating your name servers, this is a good time to note or take screenshots of your existing DNS records so that you can compare them to the records imported by Ezoic later on. Copy each of the name servers from Ezoic and paste them in at your registrar. Be sure to **either overwrite the existing name servers or delete them and add the new ones**.

#### 5. DNS propogation

Allow for [DNS to propagate](https://kinsta.com/blog/dns-propagation/) the name server change. This will usually be in 24 hours, but in some cases may take 48*–*72 hours.

![Integration complete notification in Ezoic dashboard.](https://kinsta.com/wp-content/uploads/2021/07/ezoic-name-servers-complete.png)

Integration complete notification in Ezoic dashboard.

Once propagation is finished, your site integration will show as complete in Ezoic.

#### 6. Check DNS records

On the **Settings** tab, scroll down to the **DNS Settings** to double-check that [your DNS records](https://kinsta.com/blog/what-is-dns/) match those at your previous DNS provider. These should have been automatically imported in, but it’s best to make sure everything is there and configured properly.

Just want to test things out without changing DNS records? Then, let’s take a look at the second method you can use.

### Method 2: Connect your site using Ezoic’s WordPress plugin

While using the [Ezoic WordPress plugin](https://wordpress.org/plugins/ezoic-integration/) on its own for Ezoic integration isn’t generally recommended as a long-term integration method, it can be helpful for initial set up or if you’re unable to point your name servers to Ezoic. To integrate your site with Ezoic using the plugin method, [log in to your WordPress dashboard](https://kinsta.com/blog/wordpress-login-url/), then install and activate the Ezoic plugin ([here’s a guide on installing a plugin](https://kinsta.com/blog/how-to-install-wordpress-plugins/#dashboard)). It may take **up to an hour** for the WordPress plugin option to be displayed and be marked as integrated under Settings > Site Integration in your Ezoic dashboard. Once the process successfully goes through, you can then manage your settings as needed in your Ezoic dashboard as normal. If you’re using this connection method temporarily as recommended, when you are ready to change your name servers, Ezoic recommends keeping the plugin active on your site for CDN management and automated cache clearing.

## Troubleshooting common issues with Ezoic

Now that your site is connected to Ezoic, there may be times when something isn’t working quite right. Here are some tips and recommendations for fixing some of the typical issues you may see.

### SSL errors or redirect loops

If you’ve enabled the SSL option Ezoic, make sure Full SSL is selected there to prevent any conflicts with [Kinsta’s Cloudflare integration](https://kinsta.com/blog/cloudflare-integration/) or other SSL issues.

### Changes aren’t showing up on your site

Using Ezoic with your sites means there’s an additional layer of caching that will need to be cleared anytime you need to clear the [cache](https://kinsta.com/blog/what-is-cache/). If you’re having [trouble seeing changes on your site](https://kinsta.com/blog/wordpress-changes-not-showing/) or a plugin isn’t behaving as expected after installing or reinstalling, be sure you clear cache at all layers, including:

1. Plugins (if applicable)
2. Themes (if applicable)
3. [Site/server cache at Kinsta](https://kinsta.com/blog/wordpress-cache/#clearing-wordpress-cache) (from either MyKinsta or the Kinsta MU plugin)
4. [Using Ezoic’s Caching](https://support.ezoic.com/kb/article/using-ezoic-s-caching/)
5. [Browser cache](https://kinsta.com/blog/how-to-clear-browser-cache/)

### Discrepancies in analytics

Due to differences in the data collected and the calculation method, it’s possible that analytics shown in your Ezoic dashboard may vary from [those shown in MyKinsta](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/counting-visits/). This is common with any third-party analytics tool and is expected.

## Automatic cache clearing with Ezoic’s WordPress plugin

To automatically purge pages from the Ezoic CDN whenever a post or page is updated, you can [install and activate the Ezoic WordPress plugin](https://kinsta.com/blog/how-to-install-wordpress-plugins/#1-how-to-install-wordpress-plugins-via-dashboard). This can be used (and is recommended) along with the name server Ezoic integration method.

#### 1. Enable Ezoic API

After installing the Ezoic WordPress plugin on your site, on your Ezoic dashboard go to **Settings** > **API** > **Enable**.

![Enable API to get your API key in Ezoic settings.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-ezoic-enable-api.png)

Enable API to get your API key in Ezoic settings.

#### 2. Copy API key

Copy the API key once it’s generated.

![Copy your API key from Ezoic.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-ezoic-copy-api.png)

Copy your API key from Ezoic.

#### 3. Paste API key in WordPress

Back in your WordPress dashboard, go to **Settings** > **Ezoic** > **CDN Settings**, paste in your API Key, enable **Automatic Recaching**, enable **Purge Home**, then click **Save Settings**.

![Paste your API key into the Ezoic plugin settings in your WordPress dashboard.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-ezoic-plugin-settings.png)

Paste your API key into the Ezoic plugin settings in your WordPress dashboard.

## Summary

Your site is now ready to take advantage of the features in Ezoic. If you’re experiencing any server-side issues, feel free to reach out to [Kinsta support](https://kinsta.com/docs/support/contact-support/), and we’ll be happy to help. If you have any trouble with your Ezoic integration or any of its settings, make sure to check with their support team instead.
