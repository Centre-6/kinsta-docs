---
url: "https://kinsta.com/blog/bot-traffic-server-load-wordpress/"
title: "Why scaling infrastructure doesn\u2019t fix bot traffic problems"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: []
kinsta_last_updated: "2026-06-19T10:48:21"
change_signal: "2026-06-19T10:48:21"
fetched_at: "2026-10-07T22:58:25Z"
sha256: "9cb08a2d3c4d2b4cbf43e04ed3d4396b2432ab576747ddbd13946166683b0b5f"
body_chars: 15340
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Why scaling infrastructure doesn’t fix bot traffic problems

**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/bot-traffic-server-load-wordpress/
**Kinsta last updated:** 2026-06-19T10:48:21

## On this page

- [Why bots don’t behave like real traffic](#why-bots-dont-behave-like-real-traffic)
- [What the cost of bot traffic looks like](#what-the-cost-of-bot-traffic-looks-like)
- [How Kinsta’s Bot Protection works](#how-kinstas-bot-protection-works)
  - [Choosing a protection level](#choosing-a-protection-level)
  - [Blocking AI crawlers](#blocking-ai-crawlers)
- [Managing protection across a client portfolio](#managing-protection-across-a-client-portfolio)
- [Stop scaling around a problem you can control](#stop-scaling-around-a-problem-you-can-control)

---

When resource usage on a client site starts climbing without any real rise in visits, a plan upgrade feels like the right move. It’s a sound principle when growth is coming from real traffic that increases load and the need for capacity.

However, while scaling adds resources, it doesn’t reduce the number of requests reaching the server. If [bot traffic](https://kinsta.com/blog/bot-traffic-vs-real-visits/) adds to those requests and server load, greater capacity only gives them more room to run.

As a result, the running costs increase, but the performance problems remain the same. [Kinsta Bot Protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) tool is designed for this type of situation, as it gives you control over what reaches your server, rather than expanding the surface area that absorbs it.

## Why bots don’t behave like real traffic

A human visitor who encounters a slow page might wait, reload it, or simply leave. In contrast, a bot keeps sending the same volume of requests regardless of how your server is responding. This core problem of bot traffic not being able to self-regulate when you add resources means upgrading your plan gives bots more capacity to consume.

It’s more complex once you factor in how modern WordPress sites handle requests. Most bot traffic doesn’t land on static pages that your cache can absorb. Instead, it hits endpoints that bypass caching systems and force the server to work harder. On any site running WooCommerce, search, or filtering, it means bots are landing on several elements:

- Cart actions and `?add-to-cart=` parameter variants.
- Filtered product pages with different query string combinations.
- Search queries.
- Checkout steps and wishlist actions.
- [AJAX-powered interactions](https://kinsta.com/blog/admin-ajax-php/).

None of those are cacheable in the way a static page is. For each request that lands on one of these endpoints, there are a few things that happen server-side:

- **PHP execution.** A [PHP thread](https://kinsta.com/blog/php-threads/) is reserved for the full duration of the request. Under a sustained bot load, threads exhaust and your visitors have to wait.
- **Database queries.** Dynamic pages query the database on every load because there’s no cache layer to absorb it.
- **Session handling.** Cart and checkout pages create or validate sessions on each request, which adds overhead even for bots that don’t convert.

From [our own infrastructure data](https://kinsta.com/ai-bot-traffic/), a single bot was able to generate 3.75 million requests against add-to-cart URLs in a 24-hour period. That equals roughly one request every 23 milliseconds, around the clock. Also, a single loop-detection rule filtered 550 million requests across the platform in a 30-day window.

However, these aren’t attack volumes in the traditional sense. They’re the result of bots designed to follow every URL they find, including some query string variations and parameter-based paths.

*“From an infrastructure perspective, there’s no such thing as ‘just bot traffic.’ Every request is real work. At scale, inefficient crawling stops being a traffic problem and becomes a resource problem.” – Daniel Pataki, CTO, Kinsta*

## What the cost of bot traffic looks like

A common pattern for agencies runs in a cycle: once resource usage climbs, clients upgrade the plan, then resource usage climbs again. All the while, performance won’t improve because the underlying request volume hasn’t changed.

Because [Kinsta’s billing excludes bot traffic](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/counting-visits/) from your plan usage, you have a quick way to diagnose whether bots are a problem. Recognized bot user agents are already filtered from the **Visits** screen in MyKinsta’s **Analytics**. If these stats look normal while your server is under strain, automated traffic is a likely cause.

The **Bot and automated traffic** analytics view in MyKinsta provides a clearer breakdown of the traffic reaching your site, including verified bots, likely bots, AI crawlers, aggressive crawlers, automated traffic, and likely humans.

![The MyKinsta analytics screen showing a history of requests displayed as a bar graph.](https://kinsta.com/wp-content/uploads/2026/05/kinsta-analytics.png)

The MyKinsta analytics screen showing a history of requests displayed as a bar graph.

This makes it easier to identify when automated traffic is driving resource usage. For example, spikes in aggressive crawlers or automated traffic often indicate bots repeatedly hitting uncached endpoints.

The Bot protection results chart also shows how requests are handled after classification, including traffic that was allowed, challenged, or blocked. This gives you a clearer picture of how your current protection settings affect incoming traffic.

![The Bot and automated traffic analytics view within MyKinsta.](https://kinsta.com/wp-content/uploads/2026/05/bot-results.png)

The Bot and automated traffic analytics view within MyKinsta.

The **Top requests by views** report also reflects what’s generating load on your server, and it includes all traffic, not just billable visits. The gap between those two readings is where your costs accumulate without a clear explanation.

Here’s how to read that gap:

- Check **Visits** under **Sites** > `sitename` > **Analytics** > **Plan usage** first. If visits look normal, you’re not dealing with a genuine surge in human traffic.
- Open **Top requests by views** to show all traffic including bots. A cluster of high-volume requests against non-cacheable paths (add-to-cart URLs, query string variations, or checkout steps) confirms that bots are consuming resources your cache can’t reach.
- Take a quick look at the **Performance** report. Here, elevated PHP response times or thread limits being hit is where bot-driven load shows up as server stress.

If you manage client portfolios, every site affected by bot-driven load is a cost that’s hard to account for, especially when performance hasn’t improved after an upgrade. [AI bot traffic has grown 300%](https://www.akamai.com/site/en/documents/state-of-the-internet/2025/akamai-soti-ai-botnet-report-2025-report.pdf) in the past year, while one in every [31 web visits is an AI bot](https://tollbit.com/state-of-the-bots/q3-q4-2025/). This isn’t a volume that resolves on its own.

Kinsta’s platform-level security already blocks incoming traffic classified as malicious before it reaches your site, which includes [DDoS mitigation](https://kinsta.com/blog/what-is-a-ddos-attack/) and requests from IPs associated with known attack sources. Between this and the traffic you want is a category of unverified, high-volume, resource-intensive automated requests that reaches your server anyway. Kinsta’s Bot Protection controls help reduce that volume.

## How Kinsta’s Bot Protection works

The Bot Protection controls in MyKinsta operate at the infrastructure layer, and filtering happens before WordPress is even involved. As such, there’s no plugin to install or WordPress configuration to adjust.

Kinsta classifies every request using a combination of its own traffic analysis and [Cloudflare’s machine learning system](https://blog.cloudflare.com/scalable-machine-learning-at-cloudflare/), which assigns each visitor a bot score from one to 99. High scores mean the request most likely came from a human; low scores mean it’s automated activity.

Traffic is grouped into categories such as verified bots, likely bots, AI crawlers, aggressive crawlers, automated traffic, and likely humans. Your selected protection level determines how each category is handled.

You can manage Bot Protection within MyKinsta under **Sites** > **sitename** > **Bot Protection**.

![MyKinsta's Bot Protection screen showing a toggle to block AI crawlers and the option to change the protection level.](https://kinsta.com/wp-content/uploads/2026/05/protection-level.png)

The Bot Protection screen with options to block AI crawlers and change the protection level.

### Choosing a protection level

![The Protection level screen within MyKinsta showing the four protection levels available.](https://kinsta.com/wp-content/uploads/2026/05/change-level.png)

The Protection level screen within MyKinsta showing the four protection levels available.

There are four levels to choose from within the **Protection level** panel on the **Bot Protection** screen:

- **Block malicious traffic** is the default, which handles DDoS mitigation and blocks traffic from IPs and endpoints associated with known attack sources.
- **Block automations** builds on the default to also block confirmed automated traffic, while letting verified bots and real visitors through.
- **Challenge bots** blocks automated and malicious traffic and adds a verification step for likely bots. Visitors who pass aren’t challenged again for ten days on the same browser and IP address.
- **Challenge everyone** applies challenges to likely humans as well. This level suits short-term use during traffic spikes.

To change the level, go to **Sites** > `sitename` > **Bot Protection** and click **Change**. Through **Sites**, you can select the relevant sites, and use **Actions** > **Change Bot Protection**.

However, when escalating to **Challenge bots** or above, any tool that connects to your site programmatically and isn’t listed on [Cloudflare’s verified bot directory](https://radar.cloudflare.com/traffic/verified-bots) will be blocked or challenged. This covers custom integrations, deployment scripts, and self-hosted uptime monitors. If you rely on any of these, it’s worth verifying they appear on the list before raising the protection level.

### Blocking AI crawlers

The **Block AI crawlers** toggle switch targets [AI crawlers](https://kinsta.com/blog/ai-crawlers-wordpress/) specifically. These are bots that collect content for model training, retrieval-augmented generation, and AI-powered search features. This doesn’t affect search engine crawlers, but it does include dedicated crawlers such as GPTBot. Googlebot and Bingbot continue to index your site whether the toggle is on or off.

In general, 80% of all AI crawling activity is for model training rather than user-triggered queries. This generates no referral traffic back to your site. As such, turning this on is a good idea. To enable it, go to **Sites** > `sitename` > **Bot Protection** and click the slider next to **Block AI crawlers**. For multiple sites, use **Actions** > **Change AI crawler block** from the **Sites** view.

![The Bot Protection screen in MyKinsta showing the Block AI Crawlers toggle switch.](https://kinsta.com/wp-content/uploads/2026/05/block-crawler.png)

The Bot Protection screen in MyKinsta showing the Block AI Crawlers toggle switch.

However, the trade-off is reduced exposure in AI-generated overviews and content summaries. If this visibility matters for your content strategy, it’s worth monitoring the impact before leaving the toggle permanently on.

If your priority is managing server load, it’s a cleaner option than modifying [robots.txt](https://kinsta.com/blog/wordpress-robots-txt/) or writing per-bot rules. Unlike those approaches, it operates at the infrastructure layer before a request ever reaches WordPress.

## Managing protection across a client portfolio

Different sites require varying protection levels, so a [WooCommerce store](https://kinsta.com/wordpress-hosting/woocommerce/) with filtered product pages won’t be the same as a content platform. What’s more, each site in a client portfolio carries a different traffic profile, set of integrations, and tolerance for the verification steps. This means applying a single policy across an entire portfolio will over-restrict some sites or leave others under-protected.

When you spot the signs that bot traffic is inflating costs on a client site, here’s a practical workflow:

- Start in the **Bot and automated traffic** analytics view within MyKinsta. If human traffic remains stable while automated traffic, aggressive crawlers, or AI crawler activity increases, bot-driven load is the likely cause.
- Next, open **Top requests by views** under **Analytics** and look for high request volumes against non-cacheable paths. A cluster of activity against add-to-cart URLs, filtered product pages, checkout steps, search queries, or query string variations is a strong indicator of bot-driven resource usage.
- The **Performance** report helps confirm the impact. Rising PHP response times, elevated throughput, or thread limits being hit are where automated traffic starts becoming visible as server stress.
- From there, apply the appropriate protection level for the site. **Block automations** is typically the right starting point, while **Challenge bots** adds another layer of verification for likely-bot traffic that continues reaching the origin.
- For sites that rely on integrations, APIs, or automated WordPress functionality, settings such as **Allow typical WordPress automations** and **Always allow** exceptions help reduce the risk of legitimate services being blocked.
- Changes take effect without any downtime and you can reverse it immediately if a setting turns out to be more restrictive than a site’s integrations can handle. Because the controls sit outside WordPress, there’s no risk to the site itself while you evaluate.

For agencies running large portfolios across [WordPress hosting](https://kinsta.com/wordpress-hosting/agencies/), this makes it a task rather than a project. When protection settings match each site’s actual traffic profile, the resource usage can reflect real user activity. Performance metrics correspond to what real visitors experience:

*“The misconception is thinking bot traffic is a simple ‘block or allow’ problem. In reality, it’s about policy, visibility, and economic control.” – Cristian Lopez, Managing Editor, HostingAdvice*

The explanation you give a client for costs should relate to decisions you’ve made about their traffic, not capacity you’ve added in response to load you can’t identify.

## Stop scaling around a problem you can control

Scaling your infrastructure increases the amount of load your server can absorb. Bot Protection reduces the amount of load that reaches it. These aren’t equivalent responses to the same problem: one adds capacity, while the other removes the pressure that made more capacity look necessary in the first place.

Using [MyKinsta’s analytics](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/), you can identify when automated traffic is contributing to rising resource usage, even when human traffic remains stable. From there, Bot Protection gives you the controls to classify, challenge, and block unwanted traffic before it reaches WordPress, PHP, or the database.

For sites dealing with excessive crawler activity, the **Block AI crawlers** toggle also reduces AI-driven traffic without affecting traditional search engine crawlers such as Googlebot or Bingbot.

If you want more control over how automated traffic reaches your infrastructure, Kinsta’s [Bot Protection](https://kinsta.com/bot-protection/) gives you the visibility and filtering tools to reduce unnecessary load directly from MyKinsta.
