---
url: "https://kinsta.com/blog/block-bots-wordpress-cloudflare/"
title: "How to protect your WordPress site from unwanted bot traffic with Cloudflare"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: []
kinsta_last_updated: "2025-11-18T10:23:37"
change_signal: "2025-11-18T10:23:37"
fetched_at: "2026-10-07T22:58:28Z"
sha256: "4a96c334089879a63af5fd0b97003d92773c0d6b4e7467dc0393da85adf207a2"
body_chars: 9832
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# How to protect your WordPress site from unwanted bot traffic with Cloudflare

**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/block-bots-wordpress-cloudflare/
**Kinsta last updated:** 2025-11-18T10:23:37

## On this page

- [Setting up Cloudflare for bot protection](#setting-up-cloudflare-for-bot-protection)
  - [Connect your site to Cloudflare](#connect-your-site-to-cloudflare)
  - [Enable bot fight mode](#enable-bot-fight-mode)
  - [Set up JavaScript and managed challenges](#set-up-javascript-and-managed-challenges)
- [Monitor the results](#monitor-the-results)
  - [Check Cloudflare’s security analytics](#check-cloudflares-security-analytics)
  - [Check MyKinsta analytics](#check-mykinsta-analytics)
- [Summary](#summary)

---

The web is busier than ever, with not just human visitors, but an increasing wave of automated bots, [crawlers](https://kinsta.com/blog/crawler-list/), and AI tools constantly scanning websites for content and data.

While some bots are helpful, such as search engine crawlers that aid in discovering your content, others can quickly inflate your traffic metrics, skew analytics, and even trigger unnecessary hosting overages. In fact, [bot traffic now makes up more than half of all web activity](https://kinsta.com/ai-bot-traffic/), with AI crawler activity alone growing 300% over the past year.

In this guide, we show how to use Cloudflare’s free security tools, like Bot fight mode, JavaScript and managed challenges, and other Cloudflare settings to help you reduce unwanted bot traffic, protect your WordPress site, and ensure your hosting resources are reserved for real visitors.

## Setting up Cloudflare for bot protection

You don’t need a premium account or complex configuration to stop unwanted bot traffic with Cloudflare. The free Cloudflare plan offers several powerful features that can make a big difference.

Let’s walk you through how to get started.

### Connect your site to Cloudflare

If you’re hosting your WordPress site with Kinsta, you’re already benefiting from a powerful [Cloudflare integration](https://kinsta.com/cloudflare-integration/), including enterprise-grade performance and a global [CDN](https://kinsta.com/blog/what-is-a-cdn/). However, to access advanced security tools, you need to connect your own Cloudflare account.

Fortunately, this process is quick and straightforward. We offer a detailed, step-by-step tutorial that guides you through the entire process, from adding your domain to configuring [DNS records](https://kinsta.com/blog/what-is-dns/) and nameservers. Follow this guide to get your site connected:

👉 [How to install and configure Cloudflare on your WordPress site](https://kinsta.com/blog/install-cloudflare/)

Once your domain is connected and active on Cloudflare, you’ll be ready to enable features that help protect your site from unwanted bot and scraper traffic, without impacting real visitors.

### Enable bot fight mode

Once your site is connected to Cloudflare, one of the quickest and most effective ways to start filtering out unwanted automated traffic is by enabling [Bot fight mode](https://developers.cloudflare.com/bots/get-started/bot-fight-mode/).

This free Cloudflare feature helps detect and mitigate known bots that may crawl, scrape, or overload your website, even when they try to disguise themselves as human visitors.

To turn on bot fight mode, follow these steps:

1. From the left-hand menu, go to **Security** > **Settings**.
2. Under the **Filter by** section, choose **Bot traffic**.
3. Find **Bot fight mode** and toggle it on.

![Cloudflare dashboard showing Bot Fight Mode configuration options for enhanced security.](https://kinsta.com/wp-content/uploads/2025/11/bot-fight-mode-cloudflare.png)

Cloudflare dashboard showing Bot Fight Mode option.

After activation, you can monitor results inside your [MyKinsta analytics](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/), as the visit counts begin to drop since Cloudflare filters more non-human requests before they ever reach your site.

If you’re using a paid Cloudflare plan, you have access to [Super Bot fight mode](https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/), an enhanced version of Bot fight mode with more flexibility. It builds on the same technology but lets you choose how to handle different traffic types, enabling JavaScript detections to catch headless browsers, stealthy scrapers, and other malicious traffic.

For example, instead of blocking all crawlers, you can configure the tool to block only “definitely automated traffic” and allow “verified bots” like search engine crawlers:

![Cloudflare’s Super Bot Fight Mode dashboard displaying bot protection settings and analytics.](https://kinsta.com/wp-content/uploads/2025/11/super-bot-fight-mode.png)

Cloudflare’s Super Bot Fight Mode.

### Set up JavaScript and managed challenges

Even with Bot fight mode active, some automated crawlers or AI tools can still slip through, especially those that imitate normal browsing behavior.

Cloudflare’s [security rules](https://developers.cloudflare.com/security/rules/) allow you to apply additional protection in the form of challenges, which verify that visitors are human before granting access.

You can apply JS Challenges site-wide, but for most WordPress sites, they’re best used on targeted paths such as:

- `/wp-login.php` (WordPress login page)
- `/xmlrpc.php` (common bot target)
- `/wp-admin/` (admin area)

To add a JavaScript or Managed Challenge rule:

- Navigate to **Security** > **Security Rules**.
- Click **Create rule** > **Custom rules**.
- Enter a **Rule name** (for example, *JS Challenge for wp-login*).
- Under **When incoming requests match**, configure:
  - **Field:** URI Path
  - **Operator:** contains
  - **Value:** `/wp-login.php`

![Custom rule setup in Cloudflare for managing and filtering web traffic.](https://kinsta.com/wp-content/uploads/2025/11/custom-rule-cloudflare.png)

Custom rule setup in Cloudflare.

You can add more conditions as needed by clicking **Edit expression**, and then you can add an expression like below:

```
(http.host in {"example.com" "www.example.com"} and 
 starts_with(http.request.uri.path, "/wp-admin") and 
 not cf.client.bot and 
 not http.request.uri.path contains "/wp-admin/admin-ajax.php")
```

The example above targets the `/wp-admin` area, skips verified bots, and excludes the AJAX endpoint used by WordPress plugins.

Under **Then take action**, choose one of the following:

- **JavaScript Challenge** – runs a browser test for every visitor.
- **Managed Challenge** – let Cloudflare’s AI decide when to challenge, based on behavior and risk level.

Finally, click **Deploy** to activate the rule. If you want to test it first, choose **Save as Draft**.

## Monitor the results

Once you’ve enabled Bot fight mode or set up your own Cloudflare rules, it’s important to confirm that your changes are working and that the automated traffic that inflated your visits is being filtered effectively.

Both Cloudflare and MyKinsta offer analytics tools that enable you to measure the impact. Here’s how to use them together.

### Check Cloudflare’s security analytics

In your Cloudflare dashboard, go to **Security** > **Analytics** > **Bot Analysis.**

![Cloudflare Bot Analytics dashboard displaying bot traffic statistics and activity trends.](https://kinsta.com/wp-content/uploads/2025/11/bot-analytics-cloudflare.png)

Cloudflare Bot Analytics.

This view provides a clear breakdown of how much of your total site traffic is generated by humans versus bots.

Cloudflare assigns a bot score to every incoming request based on patterns, machine learning, and behavioral signals. These scores are grouped into traffic types such as:

- **Automated** – Clearly non-human bots.
- **Likely automated** – Suspicious, bot-like requests (for example, headless browsers or AI scrapers).
- **Likely human** – Normal visitors using real browsers.
- **Verified bot** – Legitimate bots (like Googlebot or PayPal).

The [Bot Analysis](https://developers.cloudflare.com/bots/bot-analytics/) graph displays these categories in real-time. You can use the filters (by country, IP address, browser, or operating system) to identify where most of the automated traffic originates.

![Cloudflare analytics interface showing filtered traffic analysis and security insights.](https://kinsta.com/wp-content/uploads/2025/11/filter-analysis-cloudflare.png)

Filter traffic analysis.

### Check MyKinsta analytics

Next, open your **MyKinsta dashboard** > **Analytics** > **Visits** report.

![Visits analytics view in MyKinsta showing traffic trends and usage insights.](https://kinsta.com/wp-content/uploads/2025/11/visit-analytics-mykinsta.png)

Visits analytics view in MyKinsta.

Because Kinsta [measures visits](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/counting-visits/) based on unique IP addresses seen each day (and not JavaScript tracking like Google Analytics), it provides an accurate view of all traffic hitting your site, including bots that slip through other filters.

After Cloudflare starts blocking automated requests, you should notice a drop in total visits (since bots no longer reach your origin).

If you still see spikes, review your **Top Requests** and **Top Client IPs** reports to identify any URLs or IPs that are repeatedly requested. These are likely candidates for new Cloudflare challenges or country blocks.

![Top client IP addresses displayed in MyKinsta analytics for monitoring site traffic sources.](https://kinsta.com/wp-content/uploads/2025/11/top-clients-ip-mykinsta.png)

Top client IP addresses displayed in MyKinsta analytics.

## Summary

Managing unwanted bot traffic has become part of running a modern website. With Cloudflare’s free tools, you can quickly filter out automated crawlers and scrapers before they impact performance or inflate hosting usage.

For Kinsta customers, pairing these Cloudflare protections with your hosting setup helps your analytics accurately reflect real visitors and maintains consistent resource use. Prefer a built-in, no-configuration option? Kinsta’s own [Bot Protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) tool in MyKinsta covers much of the same ground, including blocking AI crawlers without needing a separate Cloudflare account.

Together, Cloudflare and Kinsta provide you with the visibility and control to focus on your content and users, rather than chasing down bots.
