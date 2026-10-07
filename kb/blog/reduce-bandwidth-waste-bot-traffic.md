---
url: "https://kinsta.com/blog/reduce-bandwidth-waste-bot-traffic/"
title: "How to reduce bandwidth waste without blocking legitimate users"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "Bot Traffic", "How to reduce bandwidth waste without blocking legitimate users"]
kinsta_last_updated: "2026-05-14T14:11:26+00:00"
sitemap_lastmod: "2026-05-14T14:11:26"
fetched_at: "2026-10-07T22:42:20Z"
sha256: "9a5ac1c691a75d04fb3fd52f6c04246b6d3571a319317e38d01850c7038141d2"
body_chars: 16091
extracted_with: "main article"
status: "live"
---

# How to reduce bandwidth waste without blocking legitimate users

**Section:** Resource Center > Blog > Bot Traffic > How to reduce bandwidth waste without blocking legitimate users
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/reduce-bandwidth-waste-bot-traffic/
**Kinsta last updated:** 2026-05-14T14:11:26+00:00

## On this page

- [Why blanket blocking traffic isn’t the answer](#why-blanket-blocking-traffic-isnt-the-answer)
- [Understanding the traffic you’re actually managing](#understanding-the-traffic-youre-actually-managing)
  - [How to understand your resource usage using MyKinsta](#how-to-understand-your-resource-usage-using-mykinsta)
- [How Kinsta’s Bot Protection works](#how-kinstas-bot-protection-works)
  - [Choosing a protection level](#choosing-a-protection-level)
  - [Allowing typical WordPress automations](#allowing-typical-wordpress-automations)
  - [Blocking AI crawlers](#blocking-ai-crawlers)
  - [Creating exceptions with Always allow](#creating-exceptions-with-always-allow)
- [Stop serving bandwidth to traffic that returns nothing](#stop-serving-bandwidth-to-traffic-that-returns-nothing)

---

Author
:   [Joel Olawanle](https://kinsta.com/blog/author/joelolawanle/ "Posts by Joel Olawanle")

Published
:   June 16, 2026

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![](https://kinsta.com/wp-content/uploads/2026/05/how-to-reduce-bandwidth-waste-without-blocking-legitimate-users-1024x512.png)

When resource usage on a client site starts climbing without a matching increase in visits, [bot traffic](https://kinsta.com/blog/bot-traffic-vs-real-visits/) is likely the cause. Bots hitting uncacheable endpoints such as cart actions, filtered product pages, and search queries trigger PHP execution and database queries on every request. As such, your page cache never gets the chance to absorb them.

While your instinct is to block all automated traffic, Googlebot, Bingbot, RSS readers, and uptime monitors fall into the same automated category as the bots you want to stop. Blocking everything removes the traffic that keeps your sites visible and functioning.

Kinsta’s [Bot Protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) lets you filter out requests that incur costs without value and let the ones that matter through. These controls sit at the infrastructure layer, meaning filtering occurs before requests even reach your WordPress site.

## Why blanket blocking traffic isn’t the answer

A [hard block on all automated traffic](https://kinsta.com/blog/block-bots-wordpress-cloudflare/) is, in theory, a valid tactic for reducing bandwidth waste. However, doing this also removes the requests you depend on. For example, hard blocks mean Googlebot and Bingbot can’t crawl your content, uptime monitoring tools won’t do the jobs you need them to, and API integrations that connect your client workflows to WordPress stop working.

In contrast, the traffic worth stopping is a specific subset of the whole: unverified bots and automation that hit non-cacheable endpoints. These don’t contribute to SEO, user experience, or revenue in many cases.

However, this is [typical behavior](https://kinsta.com/ai-bot-traffic/) for lots of bot-based action, according to David Belson, formerly Head of Data Insights at Cloudflare:

> Most of what we’re seeing isn’t malicious. It’s bots behaving inefficiently at scale, and that’s where the real problems start.

A bot following URL variations cannot recognize that it is looping. For example, consider each product filter, query string, or cart parameter treated as a distinct page. Our own infrastructure data recorded 550 million requests filtered by a single loop-detection rule in a 30-day window. A server processes each one as real work, regardless of intent.

Kinsta’s platform-level security already handles the clearest threats by blocking traffic classified as malicious before it reaches your site. This covers [DDoS mitigation](https://kinsta.com/blog/what-is-a-ddos-attack/) and requests from IPs associated with known attack sources. However, between this baseline protection and the traffic you want to allow through is a middle layer of security from unverified and unwanted bots.

Selectively filtering the remaining automated traffic is what prevents resource usage from climbing while visit counts stay flat. It’s this pattern that many agencies running [WordPress hosting](https://kinsta.com/wordpress-hosting/agencies/) for multiple clients recognize as a sign that bot-driven load has crossed the threshold of what the default security layer alone can handle.

## Understanding the traffic you’re actually managing

Kinsta [classifies every request](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) using a combination of its own traffic analysis and [Cloudflare’s machine learning system](https://blog.cloudflare.com/scalable-machine-learning-at-cloudflare/), which assigns each visitor a bot score from one to 99. A score of 99 indicates the request most likely came from a human; a score of one confirms automated activity.

There are five categories that matter for protection decisions:

- **Verified bots** are automated traffic from recognized organizations. This includes Googlebot, Bingbot, and other services on [Cloudflare’s verified bot directory](https://radar.cloudflare.com/traffic/verified-bots). These pass through at every protection level, regardless of your settings.
- **Likely humans** score between 30 and 99 and represent real visitors with normal browsing behavior.
- **Likely bots** score between two and 29 and represent unverified automation detected as probable bot activity.
- **Automated traffic** sits at a score of one and covers confirmed bots, but also includes tools that connect to your site programmatically without a verified identity. These are custom integrations, deployment scripts, self-hosted uptime monitors, and more.
- **Excessive-rate AI crawlers** are AI bots that generate load through high-frequency or looping requests.

There are two other categories worth mentioning. First, malicious traffic is automatically blocked at every protection level, requiring no configuration. However, there is also unclassified traffic. This is typically very small, harmless amounts of traffic. It usually consists of internal service requests that do not impact the origin server, such as requests generated when your site returns an error page.

### How to understand your resource usage using MyKinsta

Understanding which category of traffic is [driving resource usage](https://kinsta.com/blog/bandwidth-based-plans/) is your first step. The **Bot and automated traffic** analytics view within MyKinsta shows how requests reaching your site are classified, making it easier to identify when automated traffic is contributing to increased load.

To find this data, head to **Sites** > **sitename** > **Analytics** > **Bot and automated traffic**.

![The MyKinsta analytics screen showing a history of requests displayed as a bar graph.](https://kinsta.com/wp-content/uploads/2026/05/kinsta-analytics.png)

The MyKinsta analytics screen showing a history of requests displayed as a bar graph.

This view categorizes traffic into verified bots, likely bots, AI crawlers, aggressive crawlers, automated traffic, and likely humans. Instead of inferring bot activity indirectly from bandwidth or visit counts alone, you can see how much automated traffic is actually reaching your site and how Kinsta classifies it.

For example, spikes in aggressive crawlers or automated traffic often indicate bots repeatedly hitting uncached endpoints. Similarly, high volumes of AI crawler traffic can explain unexpected bandwidth growth or increased origin load, even when human traffic remains relatively stable.

The Bot protection results chart also shows how requests are handled after classification, including traffic that was allowed, challenged, or blocked. This gives you a clearer picture of how your protection settings affect incoming traffic before changing protection levels.

![The Bot and automated traffic analytics view within MyKinsta.](https://kinsta.com/wp-content/uploads/2026/05/bot-results.png)

The Bot and automated traffic analytics view within MyKinsta.

The **Top requests by views** report in **Analytics** also helps identify the exact endpoints that receive the highest volume of requests. A cluster of repeated requests to non-cacheable paths, such as add-to-cart URLs, filtered product pages, search queries, and checkout endpoints, usually indicates that bots are consuming server resources that the cache cannot absorb.

![Top requests by views.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-analytics-top-views.png)

Top requests by views.

Together, these analytics provide the clearest way to correlate traffic patterns with resource usage before deciding which protection level to apply.

## How Kinsta’s Bot Protection works

The Bot Protection controls in [MyKinsta](https://my.kinsta.com/) operate at the infrastructure layer. Filtering happens before requests reach the PHP or database level, so the reduction in server load applies to the full cost of the request. This means there’s no need for a plugin or any required WordPress configuration changes.

Kinsta classifies incoming traffic using a combination of its own traffic analysis and Cloudflare’s enterprise-grade bot detection system. Requests are categorized into traffic groups such as verified bots, likely bots, AI crawlers, aggressive crawlers, automated traffic, and likely humans. Your selected protection level then determines how each category is handled.

All bot protection controls live under **Sites** > **sitename** > **Bot Protection**.

![MyKinsta's Bot Protection screen showing a toggle to block AI crawlers and the option to change the protection level.](https://kinsta.com/wp-content/uploads/2026/05/protection-level.png)

The Bot Protection screen with options to block AI crawlers and change the protection level.

There are four main components within the Bot Protection screen:

- Protection levels that determine whether traffic is allowed, challenged, or blocked.
- A separate toggle to **Block AI crawlers**.
- An **Allow typical WordPress automations** settings for common WordPress APIs and background functionality.
- **Always allow** exceptions for trusted traffic sources.

As part of Kinsta’s [Cloudflare integration](https://kinsta.com/cloudflare-integration/), the underlying bot scoring and verification infrastructure is enterprise-grade by default.

### Choosing a protection level

You have four levels to choose from within the **Protection level** panel on the **Bot Protection** screen:

- **Block malicious traffic** is the default on every Kinsta site. It handles DDoS mitigation and blocks traffic from IPs and endpoints associated with known attack sources.
- **Block automations** extends the default option to also block confirmed automated traffic, while leaving human and likely-human visitors untouched.
- **Challenge bots**, block automated and malicious traffic and adds a verification step for likely bots. Visitors who pass are not challenged again for ten days on the same browser and IP address. Note that CAPTCHA-based challenges can be difficult for visitors using assistive technologies, which is worth factoring in for sites with accessibility requirements.
- **Challenge everyone** applies challenges to likely humans as well, making it better suited to short-term use during a traffic spike than as a permanent setting.

To change the level, go to **Sites** > `sitename` > **Bot Protection** and click the **Change** button. You can also apply a change across multiple sites by going to **Sites**, selecting the relevant sites, and using **Actions** > **Change bot protection**.

![The Protection level screen within MyKinsta showing the four protection levels available.](https://kinsta.com/wp-content/uploads/2026/05/change-level.png)

The Protection level screen within MyKinsta showing the four protection levels available.

Escalating to **Challenge bots** or above may affect tools that connect to your site programmatically. Any service not listed on [Cloudflare’s verified bot directory](https://radar.cloudflare.com/traffic/verified-bots) will be blocked or challenged at these levels.

### Allowing typical WordPress automations

Some WordPress functionality relies on automated requests to operate normally. This includes features such as the WordPress REST API, scheduled background tasks, plugin integrations, SEO tools, forms, analytics connections, and synchronization services.

The Allow typical WordPress automations setting helps preserve these common WordPress workflows while still filtering unwanted automated traffic. This helps reduce the risk of legitimate functionality being blocked when using stricter protection levels.

![The Allow typical WordPress automations toggle panel within MyKinsta.](https://kinsta.com/wp-content/uploads/2026/05/typical-automation.png)

The Allow typical WordPress automations toggle panel within MyKinsta.

If your site depends on custom integrations or third-party services, it’s still worth testing critical functionality after enabling stronger protection settings.

### Blocking AI crawlers

The **Block AI crawlers** toggle targets [AI crawlers](https://kinsta.com/blog/ai-crawlers-wordpress/) that collect content for model training, retrieval-augmented generation, and AI-powered search features. It blocks these crawlers, including verified ones such as GPTBot, but it does not affect search engine crawlers. Googlebot and Bingbot continue to crawl and index your site, whether the toggle is on or off.

To enable it, go to **Sites** > `sitename` > **Bot Protection** and click the slider next to **Block AI crawlers**. For multiple sites, use **Actions** > **Change AI crawler block** from the **Sites** view.

![The Bot Protection screen in MyKinsta showing the Block AI Crawlers toggle switch.](https://kinsta.com/wp-content/uploads/2026/05/block-crawler.png)

The Bot Protection screen in MyKinsta showing the Block AI Crawlers toggle switch.

For sites where you suspect AI crawler volume has an impact based on your analytics data, the toggle removes it without affecting traditional search visibility. However, the trade-off is reduced visibility in AI overviews and content summaries.

Crawlers blocked by this toggle feed the systems that surface content in AI-generated answers and recommendations. For content strategies that rely on this exposure, look to monitor the impact before leaving the toggle permanently enabled.

### Creating exceptions with Always allow

The Always allow section lets you create exceptions for traffic that should never be blocked or challenged by bot Protection.

![The Always allow panel within the MyKinsta Bit Protection screen.](https://kinsta.com/wp-content/uploads/2026/05/always-allow.png)

The Always allow panel within the MyKinsta Bot Protection screen.

This is useful for trusted integrations, monitoring services, deployment systems, internal APIs, or specific visitors that need uninterrupted access to your site.

You can create exceptions based on:

- IP addresses or IP ranges
- Paths or endpoints
- User agents

For example, you might allowlist a monitoring service, exempt a custom API endpoint from challenges, or ensure that a deployment workflow continues to work normally under stricter protection levels.

![The Add New Exception panel within MyKinsta's Bot Protection panel.](https://kinsta.com/wp-content/uploads/2026/05/new-exception.png)

The Add New Exception panel within MyKinsta’s Bot Protection panel.

Because exceptions apply before protection rules are enforced, they should be used carefully and reviewed periodically to avoid unintentionally bypassing security protections.

## Stop serving bandwidth to traffic that returns nothing

Unmanaged bot traffic generates server load that no code optimization reaches as it arrives before the cache can absorb it. This traffic consumes [PHP threads](https://kinsta.com/blog/php-threads/) and database connections on every request.

The answer is not to block all automation, but to selectively filter the traffic that wastes resources while allowing the bots and services your site depends on.

If you want more control over how automated traffic is handled on your site, Kinsta’s [Bot Protection](https://kinsta.com/bot-protection/) gives you the tools to monitor, classify, challenge, and block unwanted traffic directly from MyKinsta.

Joel Olawanle
[Kinsta](https://kinsta.com/)

Joel is a Frontend developer working at Kinsta as a Technical Editor. He is a passionate teacher with love for open source and has written over 300 technical articles majorly around JavaScript and it's frameworks.

- [Website](https://joelolawanle.com/)
- [LinkedIn](https://www.linkedin.com/in/olawanlejoel/)
- [Twitter](https://twitter.com/olawanle_joel)
- [YouTube](https://www.youtube.com/@joelolawanle)
