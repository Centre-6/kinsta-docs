---
url: "https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-understand-your-traffic-and-usage/"
title: "Understand Your Traffic and Usage"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "using-kinsta"
section: ["WordPress Hosting", "Using Kinsta"]
kinsta_last_updated: "2026-10-12T16:36:07"
change_signal: "2026-10-12T16:36:07"
fetched_at: "2026-11-11T13:03:01Z"
sha256: "07897015dfdc857573652bbe4148c3ecc9b73b54eeb9d7fb51a494cd488b7a44"
body_chars: 5905
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Understand Your Traffic and Usage

**Section:** WordPress Hosting > Using Kinsta
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-understand-your-traffic-and-usage/
**Kinsta last updated:** 2026-10-12T16:36:07

## On this page

- [Check your plan usage](#check-your-plan-usage)
- [Choose between visits and bandwidth pricing](#choose-between-visits-and-bandwidth-pricing)
- [Investigate a traffic spike](#investigate-a-traffic-spike)
- [Watch your site’s performance](#watch-your-sites-performance)
- [Use logs to troubleshoot](#use-logs-to-troubleshoot)
- [Stay within your plan](#stay-within-your-plan)
- [In your routine](#in-your-routine)

---

MyKinsta [Analytics](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/) shows how your site is performing, where its traffic comes from, and how much of your plan you’re using. Checking it once a month helps you spot problems early and avoid unexpected overage charges.

## Check your plan usage

**Why it matters:** Depending on the pricing you chose, your plan is measured either by monthly visits or by monthly server bandwidth. Every plan also has limits on disk space and CDN bandwidth. Knowing where you stand lets you act before you go over.

**How to start:** Go to **Sites** > ***sitename*** > **Analytics** > **Plan usage**, where the **Visits** and **Bandwidth** charts show your usage for the current billing period. See [Analytics](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/), [Counting Visits](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/counting-visits/) for how a visit is measured, and [Calculating Server Bandwidth](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/wordpress-calculating-bandwidth/) for how bandwidth is measured.

**Worth knowing:** If you’re on a visits-based plan, Kinsta’s visit count can differ from Google Analytics, because the two measure traffic in different ways.

## Choose between visits and bandwidth pricing

**Why it matters:** Every Kinsta plan comes in two versions at the same price: one measured by monthly visits, and one measured by monthly server bandwidth. The right one depends on how your site is used. For example, bandwidth pricing can suit sites that receive a lot of automated or bot traffic, where visit counts rise without real visitors.

**How to start:** Make a note of your usage on the [Visits](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#visits) and [Bandwidth](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#bandwidth) charts, ideally over two full billing cycles. Then compare both against Kinsta’s plans in [Choosing the Right Plan](https://kinsta.com/docs/billing/wordpress-hosting-plans/wordpress-choosing-the-right-plan/). To switch, go to **Company settings** > **My Plan**, select **Update plan**, and choose **Visits** pricing or **Bandwidth** pricing. You can switch in either direction at any time.

**Worth knowing:** Server bandwidth is separate from CDN bandwidth. Files served through Kinsta CDN count toward your CDN bandwidth, not your server bandwidth.

## Investigate a traffic spike

**Why it matters:** A sudden jump in visits or bandwidth isn’t always good news. It could be bots, and some bot traffic counts toward your usage.

**What counts:** Traffic from bots and crawlers that clearly identify themselves is excluded from your plan usage automatically. Traffic classified only as likely automated may still count if it reaches your site.

**How to start:** Look for the spike in the [Visits](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#visits) or [Bandwidth](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#bandwidth) chart under **Plan usage**. Then check the bot traffic charts in **[Analytics](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#bot-traffic)**, which show the top paths, user agents, countries, and IPs for each type of traffic over the last 24 hours. If bots are the cause, see [Protect Your Site](https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-protect-your-site/).

## Watch your site’s performance

**Why it matters:** Slow response times usually show up in the charts before visitors start complaining.

**How to start:** Open the **[Performance](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#performance)** charts under **Analytics**. If response times are rising or a particular page stands out, use the [APM tool](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/) to find the cause; see [Speed Up Your Site](https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-speed-up-your-site/).

## Use logs to troubleshoot

**Why it matters:** When something breaks, the error and access logs usually show what happened and when.

**How to start:** View your logs in MyKinsta; see [Server Logs](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/). For PHP errors, turn on [WordPress debugging](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/#wordpress-debugging) under **Tools** in MyKinsta, which shows warnings and errors without editing wp-config.php. Turn it off when you’re done. The same page lets you restart PHP if your site stops responding.

## Stay within your plan

If you’re regularly close to your limits, you have three options:

- Reduce unwanted traffic with [bot protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/), if bots make up a large share.
- Add only what you need with add-ons: extra disk space in 20 GB blocks at $20 a month, or extra WordPress sites without changing plan. See [Add-Ons](https://kinsta.com/docs/wordpress-hosting/wordpress-add-ons/).
- Move to a plan that fits your traffic, or switch between visits and bandwidth pricing if the other measure suits your site better; see [Choosing the Right Plan](https://kinsta.com/docs/billing/wordpress-hosting-plans/wordpress-choosing-the-right-plan/).

For how charges are calculated if you go over, see [Overages](https://kinsta.com/docs/billing/wordpress-hosting-plans/overages/).

## In your routine

Each month, check plan usage, disk space, and bot traffic. Each quarter, look at longer-term trends so you can plan ahead, whether that’s tightening bot protection or moving to a larger plan. See [Your Maintenance Routine](https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-your-maintenance-routine/).
