---
url: "https://kinsta.com/blog/campaign-spikes-bot-traffic/"
title: "Why bandwidth spikes during campaigns are often bot-driven"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "Ecommerce Tips", "Why bandwidth spikes during campaigns are often bot-driven"]
kinsta_last_updated: "2026-06-02T13:49:46+00:00"
sitemap_lastmod: "2026-06-02T13:49:46"
fetched_at: "2026-10-07T22:41:04Z"
sha256: "4527947f1d0882ca60d788b89446282de64f240488bf7b500c4bc3354918495b"
body_chars: 16000
extracted_with: "main article"
status: "live"
---

# Why bandwidth spikes during campaigns are often bot-driven

**Section:** Resource Center > Blog > Ecommerce Tips > Why bandwidth spikes during campaigns are often bot-driven
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/campaign-spikes-bot-traffic/
**Kinsta last updated:** 2026-06-02T13:49:46+00:00

## On this page

- [A traffic spike doesn’t always mean what it looks like](#a-traffic-spike-doesnt-always-mean-what-it-looks-like)
  - [Why campaigns attract more than just users](#why-campaigns-attract-more-than-just-users)
  - [Not all automated traffic behaves the same way](#not-all-automated-traffic-behaves-the-same-way)
  - [AI crawlers are adding a new layer of load](#ai-crawlers-are-adding-a-new-layer-of-load)
- [Why traffic can look great while results disappoint](#why-traffic-can-look-great-while-results-disappoint)
  - [Not all traffic shows up the same way in your data](#not-all-traffic-shows-up-the-same-way-in-your-data)
- [The real cost of non-human campaign traffic](#the-real-cost-of-non-human-campaign-traffic)
- [Why reactive infrastructure isn’t enough during a launch](#why-reactive-infrastructure-isnt-enough-during-a-launch)
- [What campaign-ready hosting should do](#what-campaign-ready-hosting-should-do)
- [How Kinsta helps protect campaigns from avoidable traffic waste](#how-kinsta-helps-protect-campaigns-from-avoidable-traffic-waste)
- [Best practices before your next campaign launch](#best-practices-before-your-next-campaign-launch)
- [Campaign success starts with protecting access for real visitors](#campaign-success-starts-with-protecting-access-for-real-visitors)

---

Author
:   [Joel Olawanle](https://kinsta.com/blog/author/joelolawanle/ "Posts by Joel Olawanle")

Updated
:   June 2, 2026

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![](https://kinsta.com/wp-content/uploads/2026/04/why-bandwidth-spikes-during-campaigns-are-often-bot-driven-1024x512.png)

When a campaign goes live, a [spike in traffic](https://kinsta.com/blog/bot-traffic-vs-real-visits/) is usually the first sign that things are working. But sometimes, as the data settles, you notice visits increase, conversions lag behind, and hosting usage climbs faster than planned.

One reason is that increased visibility does not only attract potential customers. It can also draw automated traffic. [AI crawlers](https://kinsta.com/blog/ai-crawlers-wordpress/), scrapers, [monitoring tools](https://kinsta.com/blog/apm-tools/), and other bots often track that activity, especially when something new starts to gain attention.

This isn’t always obvious in [analytics](https://kinsta.com/topic/analytics/), and it’s not always significant, but when bots begin requesting dynamic or uncached content at scale, they can create real infrastructure load alongside genuine traffic.

In this article, we look at why that happens, why campaign traffic and outcomes don’t always align, and what to watch for during high-visibility launches.

## A traffic spike doesn’t always mean what it looks like

A campaign spike can absolutely reflect real customer interest. But it doesn’t always show up as a clean increase in human engagement. Sometimes, as visibility grows, the traffic mix changes accordingly.

A bigger number at the top of your analytics dashboard can include both real visitors and automated requests arriving at the same time. In practice, that means traffic can rise while conversions lag behind expectations and infrastructure usage climbs faster than planned.

This shift has become more noticeable over the past year. Our [AI and bot traffic report](https://kinsta.com/ai-bot-traffic/) highlights how quickly automated activity is growing, with research showing that by the end of 2025, roughly 1 in 31 web visits came from AI bots, up from about 1 in 200 at the start of the year.

The important point is not that traffic is “bad,” but that it’s no longer purely human by default.

### Why campaigns attract more than just users

Campaigns create signals that go far beyond your intended audience. New [landing pages](https://kinsta.com/blog/wordpress-landing-page-plugins/), paid ads, promotions, and increased social activity all make a site more visible, not just to potential customers but also to automated systems that constantly scan the web.

As pages get discovered, linked, and updated, they begin to attract a range of automated requests. Some of these come from legitimate systems checking for changes or indexing content. Others come from tools tracking pricing, monitoring uptime, or collecting competitive data. In many cases, these systems operate independently of user intent, but they still generate real traffic.

The more momentum a campaign builds, the more likely these systems are to interact with the same pages as human visitors, sometimes repeatedly and at scale.

### Not all automated traffic behaves the same way

Automated traffic isn’t a single category, and treating it that way can make it harder to understand what’s actually happening. In most cases, it falls into a few broad groups:

- **Verified bots**: Known crawlers like search engines that identify themselves and *try to* follow expected patterns.
- **Likely humans**: Traffic that behaves like real users, even if it can’t be fully verified.
- **Likely bots**: Unverified traffic that shows automated behavior.
- **Automated systems**: Monitoring tools, integrations, scripts, and services making repeated requests.
- **Malicious traffic**: Scrapers, abuse attempts, or systems designed to exploit resources.

Some of this activity is expected and even necessary. Some of it is simply noise. And some of it can be actively harmful.

The distinction matters because all of these categories contribute to traffic volume, but not all of them contribute to meaningful outcomes.

### AI crawlers are adding a new layer of load

On top of existing automation, [AI crawlers](https://kinsta.com/blog/ai-crawlers-wordpress/) have introduced a newer and often heavier source of demand. Unlike traditional bots, they tend to make more frequent requests and are more likely to access dynamic or uncached content.

That difference matters during campaigns. When new pages, assets, and updates are being published, AI crawlers often hit those resources early and repeatedly, adding to the same spike you’re seeing from real users.

[Data from Cloudflare](https://blog.cloudflare.com/radar-2025-year-in-review/), cited in our report, shows that AI crawlers accounted for an average of 4.2% of HTML requests on its network by late 2025, with that share fluctuating between 2.4% and 6.4% over a short period.

Individually, that may not seem overwhelming, but combined with other forms of automated traffic, it adds up quickly, especially when requests target uncached or resource-intensive parts of a site.

## Why traffic can look great while results disappoint

A campaign can generate a real surge in activity without producing a matching lift in outcomes. Traffic volume and useful traffic aren’t the same thing, and the gap becomes more visible when automated requests are part of the mix.

[Our report](https://kinsta.com/ai-bot-traffic/) highlights how significant that gap can be. Around 80% of AI crawling activity is tied to model training rather than search or user queries, which means much of that traffic never sends visitors back to your site.

The result is a familiar pattern: visits rise, but conversions, engagement, or revenue don’t move in the same direction. In many cases, automated traffic is not the root cause of underperformance, but it amplifies existing gaps and makes them harder to interpret.

### Not all traffic shows up the same way in your data

One reason this disconnect is hard to interpret is that different systems measure traffic in different ways.

Browser-based analytics tools depend on scripts running in the user’s browser. If a request never executes that script, it may not appear in those reports at all. Server-side systems, on the other hand, count requests regardless of whether any browser interaction happens.

That gap becomes more noticeable when automation is involved. Some bots never run client-side scripts, while others attempt to look like legitimate browsers. As a result, the same traffic spike can produce very different numbers depending on where you’re looking.

## The real cost of non-human campaign traffic

When non-human traffic shows up during a campaign, the damage isn’t limited to messy reporting. It can affect what you pay for, how the site performs under pressure, and how confidently you can explain campaign results afterward.

At Kinsta, well-known bots are excluded from plan usage calculations, but large volumes of automated traffic can still affect performance if left unmanaged. Our report shows how large that activity can get in practice, including 550 million requests filtered by a single loop rule in 30 days.

Automated traffic can still affect performance, [server bandwidth](https://kinsta.com/blog/bandwidth-based-plans/), and the interpretation of analytics, even when clearly identified bots are excluded from plan usage calculations. These patterns tend to surface as a few recurring questions during and after campaigns:

**Why did bandwidth spike if conversions didn’t?**  
Traffic volume includes every request, not just meaningful visits. A single session can generate multiple requests, and automated systems can quickly amplify them. That’s how bandwidth can climb even when conversions stay flat.

**Why did the site use so many resources during the launch?**  
Every request still needs to be processed. When automated traffic increases alongside real visitors, it adds to the total load, especially on uncached or resource-heavy endpoints.

**If traffic was high, why did the site feel slow?**  
Not all requests carry equal value, but they can compete for the same resources. When automated traffic hits frequently or targets uncached content, it can affect response times for real users.

**Why don’t the numbers match across tools?**  
Different systems track different things. Server-side metrics count requests, while browser analytics depend on scripts and filtering rules. During traffic spikes, especially those involving bots, the gap between them can widen.

**How do we explain high traffic with weak results?**  
Because not all traffic represents intent. A campaign can attract attention from both humans and automated systems, and without separating the two, the headline numbers can be misleading.

## Why reactive infrastructure isn’t enough during a launch

[Reactive infrastructure](https://kinsta.com/blog/what-enterprise-ready-means/) helps, but it does not solve the whole problem. If bad traffic hits the site before protections tighten, real visitors may already be experiencing slower performance, delayed [page loads](https://kinsta.com/blog/wp-agency-performance-automation/), or added friction.

Raising protection levels during traffic spikes, performance issues, or suspicious traffic is a good idea because automated requests can still affect performance even when some are excluded from usage calculations.

That is the bigger issue during a campaign. The goal isn’t to welcome every request equally and hope the infrastructure absorbs the load. The goal is to protect access for real visitors and high-intent visitors while reducing the impact of traffic that adds load without adding value.

Kinsta’s [challenge-based approach](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#how-traffic-is-classified-in-mykinsta) reflects that idea: instead of automatically allowing or blocking everything, challenges help distinguish legitimate users from automated traffic, so real visitors can keep moving through the site.

## What campaign-ready hosting should do

At a minimum, campaign-ready hosting should do four things:

- **Maintain stability during spikes:** It should help reduce bad or unnecessary load before it affects the experience for real visitors. Higher bot protection during sudden traffic surges for exactly this reason.
- **Distinguish between traffic types:** It should give teams visibility into whether traffic is [likely human, likely bot](https://kinsta.com/blog/bot-traffic-vs-real-visits/), verified bot, automated, or malicious instead of treating every spike as equal demand.
- **Filter or challenge non-essential traffic:** It should give you ways to block [malicious traffic](https://kinsta.com/blog/wordpress-security-plugins/) by default and escalate to stronger controls when needed. Options include blocking automated traffic at higher protection levels and using challenges to verify visitors before letting them through.
- **Support investigation without plugin guesswork:** It should let teams respond at the server level, where traffic is actually being handled, rather than relying on WordPress plugins to patch over a traffic-control issue.

That is the standard worth aiming for during a launch. A hosting environment that only absorbs traffic is doing part of the job. A campaign-ready environment helps you decide which traffic should keep flowing in the first place.

## How Kinsta helps protect campaigns from avoidable traffic waste

One approach is to handle this at the infrastructure level, where traffic is processed before it affects performance or analytics. Kinsta gives teams a way to avoid treating all traffic equally during a campaign. [Bot protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) settings include a “Challenge bots” option that blocks automated and malicious traffic while challenging likely bots and unclassified traffic, rather than letting everything pass unchecked.

![change bot protection level ](https://kinsta.com/wp-content/uploads/2026/04/wordpress-change-bot-protection-options-1.png)

You can change the Bot Protection level in MyKinsta

This matters during high-visibility launches, when the goal is to absorb demand while reducing unnecessary load and preserving access for real visitors.

Kinsta also offers the option to block AI crawlers when needed, which can help when frequent crawler requests contribute to performance issues or bandwidth waste.

![Kinsta Bot Protection](https://kinsta.com/wp-content/uploads/2026/03/wordpress-change-ai-crawlers.png)

Block AI crawlers in MyKinsta

These settings are especially useful when you want to raise protection during a launch window, reduce unnecessary load, and keep the site more available for real customers.

For sites that need finer control, Kinsta also includes options for allowing trusted WordPress automations, and creating custom exceptions. See the [Bot Protection documentation](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) for a complete overview of the available settings and protection levels.

## Best practices before your next campaign launch

Here are a few things to account for before starting a new campaign and while getting it off the ground:

1. Before launch, review expected traffic and make sure the site is ready for more than just human visitors.
2. Once the campaign is live, compare server-side traffic with [browser-based analytics](https://kinsta.com/blog/wordpress-analytics-limitations/) to spot gaps between raw request volume and actual user activity.
3. Decide in advance whether a higher bot-protection setting makes sense during the campaign window, especially if the launch involves paid traffic, fresh landing pages, or other visibility spikes.
4. During the campaign, watch performance and plan usage closely rather than relying on conversion numbers alone.
5. Finally, document what normal traffic, [conversion rates](https://kinsta.com/blog/conversion-rate-optimization-tips/), and resource usage look like before launch, so it is easier to spot anomalies and explain what changed if the numbers stop lining up.

## Campaign success starts with protecting access for real visitors

A strong campaign attracts attention and protects the path for real visitors to reach the page, load it quickly, and take action, without being drowned out by a wave of low-value automated traffic.

That is the main takeaway here: traffic spikes are not always clear signs of demand, and treating every request as equally valuable can lead to higher usage, slower performance, and murkier reporting than expected.

Kinsta gives teams more control during those moments with [Bot Protection settings](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) that can block, challenge, or filter automated traffic, and the option to block AI crawlers when they contribute to avoidable load. If you want a hosting setup that helps you manage campaign traffic more deliberately, explore Kinsta [managed hosting plans](https://kinsta.com/wordpress-hosting/) to see how we support performance, visibility, and traffic control during high-visibility launches.

Joel Olawanle
[Kinsta](https://kinsta.com/)

Joel is a Frontend developer working at Kinsta as a Technical Editor. He is a passionate teacher with love for open source and has written over 300 technical articles majorly around JavaScript and it's frameworks.

- [Website](https://joelolawanle.com/)
- [LinkedIn](https://www.linkedin.com/in/olawanlejoel/)
- [Twitter](https://twitter.com/olawanle_joel)
- [YouTube](https://www.youtube.com/@joelolawanle)
