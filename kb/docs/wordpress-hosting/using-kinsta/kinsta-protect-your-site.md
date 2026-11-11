---
url: "https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-protect-your-site/"
title: "Protect Your Site"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "using-kinsta"
section: ["WordPress Hosting", "Using Kinsta"]
kinsta_last_updated: "2026-10-12T16:31:07"
change_signal: "2026-10-12T16:31:07"
fetched_at: "2026-11-11T13:03:01Z"
sha256: "68ac4cc2f44b2643c4b8e2ba78f952befade6cd42130365948c36034f754d47b"
body_chars: 11106
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Protect Your Site

**Section:** WordPress Hosting > Using Kinsta
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-protect-your-site/
**Kinsta last updated:** 2026-10-12T16:31:07

## On this page

- [What’s already protecting your site](#whats-already-protecting-your-site)
- [Vulnerability protection](#vulnerability-protection)
- [Bot protection](#bot-protection)
- [Block AI crawlers](#block-ai-crawlers)
- [Keep plugins and themes up to date](#keep-plugins-and-themes-up-to-date)
- [Plan for recovery](#plan-for-recovery)
- [Restrict access when you need to](#restrict-access-when-you-need-to)
- [In your routine](#in-your-routine)

---

Every Kinsta site is protected by default, with no setup needed. Here’s what’s already working for you, including vulnerability protection, and the extra layers you can control: bot protection, automatic updates, backups, and access restrictions.

## What’s already protecting your site

- **Firewall and DDoS protection:** Cloudflare’s enterprise-level firewall filters incoming traffic and blocks IPs linked to hacking attempts and DDoS attacks before they reach your server.
- **Malicious traffic blocking:** Kinsta’s platform-level defences stop roughly 15–20% of traffic, the share classified as malicious, before it affects your site.
- **Vulnerability protection:** Blocks attempts to exploit known weaknesses in your plugins, themes, and WordPress version, even before a fix is released.
- **Daily vulnerability scans:** MyKinsta checks every plugin and theme each day for known security vulnerabilities.
- **Daily backups and uptime monitoring:** Your site is backed up automatically every day and checked every 3 minutes.

## Vulnerability protection

**Why it matters:** Most attacks on WordPress sites target known vulnerabilities in plugins and themes. There’s often a gap between a vulnerability becoming public and a fix being released and installed, and that’s when sites are most at risk.

**How it works:**  [Vulnerability protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-vulnerability-protection/), powered by Patchstack, checks your WordPress core, plugins, and themes against an up-to-date vulnerability database. When it finds a vulnerability affecting your site, it blocks requests that try to exploit it, without changing your plugin or theme files. It adds a different layer to the firewall and bot protection. Those focus on who is sending traffic and filter out known bad sources. Vulnerability protection focuses on what a request is trying to do, so it can block an attack even when it comes from a source that looks legitimate.

**How to start:** there’s nothing to set up, and it’s included at no extra cost. It’s installed automatically as a must-use plugin on every WordPress site created in MyKinsta. New sites have it from 7 October 2026, and existing sites from 14 October 2026. To check that it’s active, look for the status indicator on your site’s **Info** page in MyKinsta.

**Watch out for:**

- **It isn’t a replacement for updates:** It blocks known ways of exploiting a vulnerability, while an update fixes the code itself. Keep [updating](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-manage-plugins-themes/) as soon as fixes are released.
- **Your own Patchstack plugin:** If you have one installed, Kinsta’s vulnerability protection is turned off on that site, and you’ll need your own Patchstack licence. Remove your plugin and Kinsta’s protection switches on within 12 hours.
- **It prevents, not cleans up:** It doesn’t scan for or remove existing malware; see [Malware Removal](https://kinsta.com/docs/service-information/malware-removal/) if your site has already been compromised.
- **It can’t be turned off:** If you think it’s causing a problem on your site, [contact Support](https://kinsta.com/docs/support/contact-support/), who can investigate.

## Bot protection

**Why it matters:** Not every unwanted visitor is clearly malicious. Scrapers, spam bots, and aggressive crawlers can slow your site, distort your analytics, and count toward your plan usage. [Bot protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) lets you decide how strictly that traffic is handled.

**Choose a protection level:**

- **Block malicious traffic (default):** Blocks attack, DDoS, and abuse traffic. Right for most sites, day-to-day.
- **Block automations:** Also blocks confirmed automated traffic. Useful when you’re seeing unexplained traffic or resource use.
- **Challenge bots:** Also asks likely bots to pass a verification check. Useful against fake checkouts, form spam, login attacks, and scraping.
- **Challenge everyone:** Asks every visitor to pass a verification check. Use it for short periods during an active attack or a high-traffic launch.

Verified bots such as Googlebot and Bingbot are allowed at every level, so your search rankings aren’t affected. A visitor who passes a challenge isn’t challenged again for at least 10 days on the same browser and IP address.

**When to raise the level:** during a sudden traffic spike, when you see performance problems you can’t explain, or ahead of a sale or launch. Use the [Visits](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#visits) and [Performance](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#performance) charts in **Analytics** to spot these; see [Understand Your Traffic and Usage](https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-understand-your-traffic-and-usage/).

**How to start:** Go to **Sites** > ***sitename*** > **Bot protection** and click **Change** under **Protection level**. To change several sites at once, select them on the **Sites** page and use **Actions** > **Bot protection** > **Change bot protection level**.

**Watch out for:**

- **Plugins and integrations:** Above the default level, plugins and services that connect to your site may be blocked. These include form-to-CRM connections, SEO tools, Zapier, and payment webhooks. Turn on **Allow typical WordPress automations**, or add an exception for each service.
- **Visitor experience:** Challenging everyone adds a brief verification step, and some challenges can be difficult for visitors using assistive technology. Use this level for short periods.
- **Other security services:** Bot protection can’t be used with a reverse proxy or third-party services such as Sucuri, another CDN, AWS, or Azure.

**Exceptions:** You can add up to 50 rules that always allow, challenge, or block a specific IP address, path, user agent, or country. When rules overlap, **Allow** wins over **Challenge**, and **Challenge** wins over **Block**. Allow exceptions don’t override vulnerability protection and Kinsta’s underlying security protections, so exploit attempts are still blocked even from sources you’ve allowed.

## Block AI crawlers

**Why it matters:** AI crawlers collect content to train or power AI tools. Some make large numbers of requests, which use your resources and can inflate your traffic figures.

**When to use it:** When AI crawlers are scraping content-heavy pages, putting load on your server, or collecting premium or gated content.

**How to start:** Turn on [**Block AI crawlers**](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#block-ai-crawlers) under **Bot protection**. Unlike some Cloudflare settings, it only blocks AI and training crawlers, not Googlebot, Bingbot, or other major search engines.

**Watch out for:** Blocking AI crawlers may reduce how often your content appears in AI-powered search results and summaries. Monitor your traffic after making the change.

## Keep plugins and themes up to date

**Why it matters:** Plugins are where almost all WordPress security problems start. Of the 11,334 new WordPress vulnerabilities reported in 2025, 91% were in plugins, and only a handful were in WordPress core. MyKinsta flags known vulnerabilities daily, and vulnerability protection blocks known exploits in the meantime, but only an update fixes the underlying code. Apply updates within days of a fix being released.

**How to start:** Review flagged items under [**Plugins and themes**](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-manage-plugins-themes/). To have updates applied for you, add [Kinsta Automatic Updates](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-plugins-themes-automatic-updates/). It updates your plugins and themes daily, in a time window you choose, and compares screenshots of up to five key pages before and after each update. If an update visibly breaks a page, it rolls back automatically and emails you. It costs $3 per environment per month after a month-long free trial, and you can turn it on for several sites at once with bulk actions.

**Watch out for:** Pages with changing content, such as sliders or rotating banners, can look different between screenshots and trigger a rollback. You can hide those elements from the comparison in the [Automatic updates settings](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-plugins-themes-automatic-updates/#settings).

## Plan for recovery

**Why it matters:** If something goes wrong, the gap between your last backup and the problem is the work you could lose.

**What’s included:**  [Daily automatic backups](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#wordpress-backups), kept for 14 to 30 days depending on your plan, plus backups created automatically before certain events. A backup is only useful if it restores, so restore one to staging every month or so to check.

**When to add more:** If your site changes often, such as a store taking orders throughout the day, consider the [6-hourly or hourly backup add-ons](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#hourly-backups-add-on-cost). To keep copies off Kinsta, use [external backups](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#external-backups-add-on). For business-critical sites on dedicated servers, see the [Disaster Recovery add-on](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/disaster-recovery/). See [Add-On](https://kinsta.com/docs/wordpress-hosting/wordpress-add-ons/)s for pricing. If your site is ever infected, see [Malware Removal](https://kinsta.com/docs/service-information/malware-removal/).

## Restrict access when you need to

- **[Password protection (htpasswd)](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/htpasswd/):** Keeps staging sites and sites under construction private. It also stops uptime monitoring, so remove it when the site goes live.
- **[Block IP addresses](https://kinsta.com/docs/wordpress-hosting/site-management/block-ip-address/):** Stops a specific address that’s causing problems.

## In your routine

- **Weekly:** Apply updates, or check the [vulnerability notifications](https://kinsta.com/docs/user-settings/notifications/#vulnerability-notifications).
- **Monthly:**  [Restore a recent backup](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#restoring-wordpress-backups-to-staging) to staging to check it works, and review your bot traffic.
- **Quarterly:** Delete plugins and themes you don’t use, and remove bot protection exceptions you no longer need.

See [Your Maintenance Routine](https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-your-maintenance-routine/) for the full checklist.
