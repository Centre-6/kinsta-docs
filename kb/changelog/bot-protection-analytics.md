---
url: "https://kinsta.com/changelog/bot-protection-analytics/"
title: "See exactly where your site\u2019s traffic goes with bot protection"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-07-23T14:58:51"
change_signal: "2026-07-23T14:58:51"
fetched_at: "2026-10-07T22:58:21Z"
sha256: "fa03e1cf0daeb4a0822c5352061bdea61e0aa9b20ea4441496b4f126c1912ac2"
body_chars: 5738
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# See exactly where your site’s traffic goes with bot protection

**Product:** Changelog
**Source:** https://kinsta.com/changelog/bot-protection-analytics/
**Kinsta last updated:** 2026-07-23T14:58:51

## On this page

- [A bot protection widget, right on your site’s dashboard](#a-bot-protection-widget-right-on-your-sites-dashboard)
- [Follow traffic from classification to outcome](#follow-traffic-from-classification-to-outcome)
- [Three new traffic types in the breakdown](#three-new-traffic-types-in-the-breakdown)
- [Find out exactly what’s generating any type of traffic](#find-out-exactly-whats-generating-any-type-of-traffic)
- [Filter the Requests chart by traffic type](#filter-the-requests-chart-by-traffic-type)
- [Try it out](#try-it-out)

---

Back in May, we [launched the bot protection tool](https://kinsta.com/changelog/bot-protection/) in MyKinsta to everyone, giving you control over how automated traffic is handled on your site.

Since then, one feedback has come up again and again: *knowing how much* traffic was being challenged or blocked is useful, but customers want to know *what* that traffic actually was and *where it went* once bot protection made a decision about it.

This release is our answer to that. Bot protection’s analytics have been rebuilt to trace every request from classification to outcome, and to make that view available in more places than just the bot protection page itself.

## A bot protection widget, right on your site’s dashboard

You no longer need to go looking for your traffic protection numbers. A new bot protection widget now lives in the right-hand column of **Sites** > ***sitename*** > **Info**, showing a quick breakdown of allowed, challenged, and blocked requests over the last 24 hours at a glance.

![Bot protection donut widget on the Site Info page](https://kinsta.com/wp-content/uploads/2026/07/bot-protection-widget.png)

The bot protection widget on the Site Info page.

It’s a small addition, but it means you can catch a spike in blocked or challenged traffic the moment you land on a site, without navigating anywhere else.

## Follow traffic from classification to outcome

The biggest change is to the **Request breakdown** section on **Sites** > ***sitename*** > **Bot protection**.

Previously, this page showed a bar chart for how traffic was classified, and another for how bot protection acted on it. Figuring out how the two connected meant doing the math yourself.

Now, a Sankey diagram connects them directly, covering the last 24 hours of traffic. You can see, at a glance, how much of your **Likely bots** traffic was challenged versus how much of your **Malicious traffic** was blocked outright, without cross-referencing two charts.

![Request breakdown flow chart showing traffic types flowing into allowed, challenged, and blocked outcomes](https://kinsta.com/wp-content/uploads/2026/07/request-breakdown.png)

Tracing traffic types through to their outcomes in the Request breakdown chart.

## Three new traffic types in the breakdown

We’ve also added three new categories to the breakdown:

- **Malicious traffic:** the attack, [DDoS](https://kinsta.com/blog/what-is-a-ddos-attack/), and abuse traffic Kinsta has always blocked by default, even before bot protection existed, are now visible in your analytics for the first time.
- **Custom rules:** traffic affected by exceptions you’ve added in **Always Allow**, or by any custom WAF rules our Support team has configured for your site.
- **WP automations:** traffic allowed through because you’ve enabled **Allow typical WordPress automations**.

![Three new traffic types in the breakdown](https://kinsta.com/wp-content/uploads/2026/07/new-traffic-types.png)

Three new traffic types in the breakdown

Between these additions and the existing categories, you now get a complete picture of everything hitting your site, not just the categories bot protection actively controls.

## Find out exactly what’s generating any type of traffic

New **Top traffic** tables now appear on both **Sites** > ***sitename*** > **Bot protection** and **Sites** > ***sitename*** > **Analytics** > **Bot traffic**, showing the most common paths, user agents, countries, and IPs behind your site’s traffic.

![The Top traffic table, filtered to Malicious traffic.](https://kinsta.com/wp-content/uploads/2026/07/type-of-traffic.png)

The Top traffic table, filtered to Malicious traffic.

On the bot protection page, this table always reflects the last 24 hours, matching the rest of that page. On the **Analytics** > **Bot traffic** page, it follows [whatever date range you’ve selected](https://kinsta.com/changelog/analytics-improvements/), so you can pull up **Top traffic** for the past 7, 30, or 90 days, not just the day before.

Use the dropdown above the table to filter by traffic type. For example, switch to **Malicious traffic** to see exactly which paths are being targeted, or to **AI crawlers** to see which bots are generating the most requests.

![The Top traffic types](https://kinsta.com/wp-content/uploads/2026/07/top-traffic-classification.png)

The Top traffic types

If you’ve ever wanted to know exactly what `/wp-login.php` or `/xmlrpc.php` traffic looks like on your site before deciding whether to tighten your protection level, this is where you’ll find it.

## Filter the Requests chart by traffic type

Over on **Sites** > ***sitename*** > **Analytics** > **Bot traffic**, the **Requests** chart now includes a traffic type selector. Instead of viewing all traffic types stacked together, you can isolate just the ones you care about.

![Traffic type dropdown with checkboxes for each classification](https://kinsta.com/wp-content/uploads/2026/07/traffic-type-breakdown.png)

Selecting specific traffic types to display in the Requests chart.

All traffic types are selected by default, so nothing changes unless you want it to.

## Try it out

[Bot protection](https://kinsta.com/bot-protection/) remains a Beta feature, and this analytics refresh is very much part of that ongoing work. We’d love to know whether the new flow chart and Top traffic tables make it easier to understand your site’s traffic.

[Let us know](https://kinsta.com/kinsta-support/) what you find, and check our [documentation](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) for a full [walkthrough of every chart](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#bot-traffic) on the page.
