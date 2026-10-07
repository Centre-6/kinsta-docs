---
url: "https://kinsta.com/blog/ai-bot-traffic-surpassing-human-web/"
title: "Bots are surpassing human traffic on the web. What is really going on?"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "Bot Traffic", "Bots are surpassing human traffic on the web. What is really going on?"]
kinsta_last_updated: "2026-06-29T19:49:51+00:00"
sitemap_lastmod: "2026-06-29T19:49:51"
fetched_at: "2026-10-07T22:42:17Z"
sha256: "b88d80756a4df99c56fabfa567cba6f345c7b2d510ef426b239c41e560e8587a"
body_chars: 17271
extracted_with: "main article"
status: "live"
---

# Bots are surpassing human traffic on the web. What is really going on?

**Section:** Resource Center > Blog > Bot Traffic > Bots are surpassing human traffic on the web. What is really going on?
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/ai-bot-traffic-surpassing-human-web/
**Kinsta last updated:** 2026-06-29T19:49:51+00:00

## On this page

- [What are bots and why do the old definitions no longer work](#what-are-bots-and-why-do-the-old-definitions-no-longer-work)
- [What do we mean by human traffic?](#what-do-we-mean-by-human-traffic)
- [Why now?](#why-now)
  - [1. Financial reward](#1-financial-reward)
  - [2. Weak regulatory environment](#2-weak-regulatory-environment)
  - [3. User agents are no longer providing trusted signals](#3-user-agents-are-no-longer-providing-trusted-signals)
- [How to gauge bots today](#how-to-gauge-bots-today)
- [Implications and the trends to watch](#implications-and-the-trends-to-watch)
  - [Hosting infrastructure costs](#hosting-infrastructure-costs)
  - [Distorted analytics](#distorted-analytics)
  - [The advent of the “dead web”](#the-advent-of-the-dead-web)
  - [Heightened security risks from malicious bots](#heightened-security-risks-from-malicious-bots)
  - [The scraper economy and economic inversion](#the-scraper-economy-and-economic-inversion)
  - [AI-powered browsers and autonomous agents](#ai-powered-browsers-and-autonomous-agents)
- [The line between human and machine is gone](#the-line-between-human-and-machine-is-gone)

---

Author
:   [Bud Kraus](https://kinsta.com/blog/author/budkraus/ "Posts by Bud Kraus")

Published
:   June 30, 2026

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![](https://kinsta.com/wp-content/uploads/2026/06/the-web-is-becoming-bot-first-traffic-not-human-first-1024x512.png)

This year, the general press has been reporting a historic shift in automated traffic surpassing human-initiated traffic online. And the numbers behind that shift are harder to dismiss than most milestone moments in internet history.

The most widely cited data point comes from [Imperva’s 2025 Bad Bot Report](https://www.imperva.com/resources/resource-library/reports/2025-bad-bot-report/), the 12th edition of their annual series tracking automated traffic trends since 2013. Analyzing traffic patterns from 2024, the report found that automated activity accounted for more than 50% of all web traffic for the first time in its records, reaching 51%. It is worth noting that Imperva came close to this threshold before. Their 2024 report recorded bots at 49.6%, so this is less a sudden crossing than the confirmation of a trend that has been building for years across multiple vendors and measurement frameworks.

Imperva is not the only one documenting it. Cloudflare, Akamai, TollBit, and Human Security have all published data pointing in the same direction. At Kinsta, [our own analysis](https://kinsta.com/ai-bot-traffic/) of over 10 billion requests across managed infrastructure tells a consistent story: AI bot traffic surged 300% in a single year, and the effects are no longer abstract.

And while the margin between human and automated traffic is still small, the implications are enormous. Let’s take an over-the-horizon view of how this shift in bot traffic is shaping the web.

## What are bots and why do the old definitions no longer work

Traditionally, bots (short for robots) are software applications designed to perform automated tasks without human intervention. The most widely known is [Googlebot](https://kinsta.com/blog/crawler-list/#1-googlebot), Google’s automated crawler that scans and indexes webpages for search. Other common bots handle uptime monitoring, indexing, analytics, security scans, and other utility functions that help keep the web operating efficiently.

While many of these bots are harmless (even beneficial), another class of bots has evolved over time that is far more problematic. These are the [AI crawlers](https://kinsta.com/blog/ai-crawlers-wordpress/) operating at a scale that strains infrastructure regardless of intent.

In our [AI & bot traffic report](https://kinsta.com/ai-bot-traffic/), David Belson, formerly Head of Data Insights at Cloudflare, shared that “Most of what we’re seeing isn’t malicious. It’s bots behaving inefficiently at scale, and that’s where the real problems start.”

Historically, bots were relatively easy to identify as they typically could not execute JavaScript, simulate pointer movement, maintain realistic browser sessions, or rotate IP addresses effectively. That has changed dramatically. AI-powered automation now allows bots to imitate human behavior with surprising sophistication, disguising the traditional signals used for detection.

As Belson puts it, “There’s the person who didn’t know what the hell they were doing yesterday, but vibe coded a bot today and let it loose, they’re not even bothering to check robots.txt.”

The result is that systems are increasingly shifting away from identity-based detection and toward behavioral analysis.

## What do we mean by human traffic?

Lest there be any confusion, when we speak of human traffic, we are not simply referring to clicks or obvious user interactions. Human traffic encompasses the many requests generated as part of delivering and rendering a webpage or application experience.

A single human page visit can generate dozens (sometimes hundreds) of requests. These may include requests for HTML, CSS, JavaScript, fonts, images, APIs, analytics scripts, advertising assets, and other resources required to render a modern webpage.

This distinction is important because discussions about bot traffic versus human traffic are typically measured by requests and network activity, rather than by the number of real human beings online. A relatively small number of aggressive bots can generate enormous volumes of traffic by repeatedly requesting pages, scraping APIs, downloading assets, or executing automated actions at machine scale.

## Why now?

Several factors are accelerating the growth of bot traffic beyond generative AI alone.

### 1. Financial reward

The days when pranks, curiosity, or technical prowess were the primary motivations behind malicious online activity are largely over. Today’s internet fosters an environment in which illegal operations carried out by individuals or large organized crime syndicates can generate profits in the millions of dollars.

Fraud, data theft, system exploitation and destruction, market manipulation, large-scale content scraping, ransomware distribution, and other forms of illicit revenue generation are now carried out on an enormous scale by automated systems and malicious bots.

Unauthorized and illegal access to personal data has become a massive business, and AI-powered bots are making these activities increasingly difficult to detect, trace, and stop.

### 2. Weak regulatory environment

The internet is a globally fragmented environment where laws, enforcement, and jurisdiction vary dramatically across countries and regions. That fragmentation creates fertile ground for malicious automation to thrive.

Weak regulatory environments allow harmful AI bots to flourish because laws, enforcement, and international coordination have not kept pace with the rapid evolution of AI-driven automation. While this has long been a challenge in technology, the speed and scale of AI development have dramatically intensified the problem.

### 3. User agents are no longer providing trusted signals

For years, user agents provided one of the most trusted identity signals on the web. A user agent reliably identified the browser, operating system, and sometimes the device making a request. Systems relied heavily on these identifiers to distinguish between legitimate browsers, search engine crawlers, mobile devices, and automated bots.

That model is breaking down. Modern bots can cloak, spoof, or manipulate user agents so effectively that the signal itself is becoming increasingly unreliable. A malicious bot can now impersonate a legitimate browser, mimic a mobile device, or even disguise itself as a trusted crawler. AI-driven automation has accelerated this trend by making sophisticated impersonation easier and cheaper to deploy at scale.

As a result, modern security systems increasingly rely on behavior rather than identity alone.

## How to gauge bots today

Since IP reputation and other traditional signals are no longer fully trustworthy, detection systems increasingly look for behavioral patterns that suggest automation or malicious activity.

Requests arriving at speeds, scale, and frequency impossible for humans to reproduce remain one of the clearest warning signs. Repeated login attempts, highly sequential scraping behavior, aggressive API usage, and large bursts of requests often indicate automation at work.

Kinsta’s own infrastructure data recorded a single bot generating 3.75 million requests to add-to-cart URLs on one site in 24 hours, which is roughly one request every 23 milliseconds, all day, each one hitting the server as a fresh uncacheable request.

![7.67 million requests hit add-to-cart URLs in 24 hours](https://kinsta.com/wp-content/uploads/2026/05/7-67-million-requests-hit-add-to-cart-urls-24-hours.png)

7.67 million requests hit add-to-cart URLs in 24 hours

Human browsing behavior tends to be somewhat unpredictable. Bots, even sophisticated ones, often produce highly repetitive interaction patterns, predictable navigation flows, or unusually systematic extraction, even when they successfully mimic JavaScript execution, realistic browser sessions, and mouse movement. This is why detection has shifted toward evaluating behavioral intent rather than claimed identity.

At Kinsta, this is exactly the logic [we use to classify traffic](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#how-traffic-is-classified-in-mykinsta) across managed sites. Rather than a simple human-or-bot binary, our bot protection system works across six categories: verified bots, likely humans, likely bots, automated traffic, unclassified traffic, and malicious traffic, with a separate designation for excessive-rate AI crawlers that are verified but generating load that strains infrastructure regardless of intent.

![Kinsta bot request breakdown](https://kinsta.com/wp-content/uploads/2026/05/kinsta-bot-request-breakdown.png)

Kinsta bot request breakdown

Each category is handled differently because the right response to a misconfigured AI training crawler is not the same as to a credential stuffing attack. By default, Kinsta’s platform-level defenses stop approximately 15–20% of traffic classified as malicious before it ever reaches your site. Bot protection layers above that baseline enable site owners to challenge or block additional categories based on their own traffic patterns and risk tolerance.

![Kinsta bot protection level](https://kinsta.com/wp-content/uploads/2026/05/bot-protection-level.png)

Kinsta bot protection level

## Implications and the trends to watch

As these systems evolve, the implications extend far beyond cybersecurity alone and begin to affect infrastructure, publishing, analytics, e-commerce, and the overall quality of the web itself.

Is there anything on the horizon that may slow the growth of bot traffic? The data suggests not. AI bot traffic surged 300% in a single year, and the ratio of AI bot visits shifted from 1 in 200 to 1 in 31 in under 12 months. As Daniel Pataki, CTO of Kinsta, puts it: “At scale, inefficient crawling stops being a traffic problem and becomes a resource problem.” The conditions driving that scale are not easing.

### Hosting infrastructure costs

One of the most immediate impacts of increased [bot traffic](https://kinsta.com/blog/bot-traffic-vs-real-visits/) is rising infrastructure costs. Every request to a website consumes bandwidth, compute resources, database queries, memory, caching systems, and storage infrastructure.

The problem is especially acute on WordPress sites running [WooCommerce](https://kinsta.com/blog/woocommerce-bot-traffic/), search, or plugin-heavy functionality. Unlike static pages served from cache, dynamic endpoints require the server to do real work on every single request. A bot trapped in a query-string loop cannot tell the difference between a cacheable page and an expensive one. A single such loop across one Kinsta-managed site triggered 550 million requests in 30 days before a dedicated mitigation rule caught it.

As Daniel Pataki puts it, “There’s no such thing as ‘just bot traffic.’ Every request is real work. At scale, inefficient crawling stops being a traffic problem and becomes a resource problem.”

Smaller publishers and independent site owners are especially vulnerable because they often lack the enterprise-grade mitigation systems available to larger organizations.

### Distorted analytics

AI bot traffic increasingly skews analytics metrics in ways that can be highly misleading. Inflated pageviews, fake engagement, artificial referral traffic, and automated interactions can lead decision-makers to [draw faulty conclusions from unreliable data](https://kinsta.com/blog/analytics-scaling-tool-optimize-or-scale/).

The problem is compounding as bots become more human-like. Tools that rely on JavaScript tracking, like Google Analytics, tend to undercount bot activity because many bots don’t execute JavaScript. Server-level analytics, which count every IP-based request, tend to overcount because they catch bots that JavaScript misses.

At Kinsta, [MyKinsta analytics](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/) are built on server-level access logs and explicitly exclude known bot user agents from billable visit counts, but even that distinction has limits, because automated traffic that closely mimics human behavior can still appear in reported numbers.

From November 2025, Kinsta’s [Top Requests charts](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#top-requests) began reflecting all traffic including bots, precisely to give site owners a clearer picture of what is actually hitting their infrastructure versus what is being billed.

![Kinsta top requests by bandwidth](https://kinsta.com/wp-content/uploads/2026/05/top-requests-by-bandwidth.png)

Kinsta top requests by bandwidth

When your pageviews are climbing but branded search volume, conversions, and direct traffic remain flat, bots are almost certainly responsible for the gap.

### The advent of the “dead web”

The so-called “dead web” phenomenon refers to the growing flood of low-quality, machine-generated content appearing across the internet. While some of the more extreme versions of the theory veer into speculation, there is little doubt that AI is making it dramatically easier to generate synthetic articles, fake reviews, spam blogs, automated media, and low-value content at a massive scale.

The result may be a polluted web in which discovering trustworthy, genuinely useful information becomes increasingly difficult.

### Heightened security risks from malicious bots

AI-powered bots are significantly increasing the sophistication of cyberattacks. Credential stuffing attacks, account takeovers, API abuse, phishing campaigns, vulnerability scanning, and ransomware deployment are becoming faster, more scalable, and more adaptive through automation.

Because AI systems can learn from failures and continuously refine their methods, traditional rule-based defenses increasingly struggle to keep pace.

### The scraper economy and economic inversion

Historically, [search crawlers](https://kinsta.com/blog/crawler-list/) like Googlebot created a relatively balanced economic relationship with publishers. They crawled content, indexed it, and then returned traffic back to the originating websites.

Modern AI scraping systems are changing that relationship. Increasingly, AI systems extract content, summarize information elsewhere, and provide answers directly without necessarily returning traffic to the original source. This creates a growing “scraper economy” where publishers and creators bear the cost of producing content and maintaining infrastructure while automated systems extract much of the downstream value.

### AI-powered browsers and autonomous agents

These systems are moving far beyond simple web crawling. [AI-powered agents](https://cloud.google.com/discover/what-are-ai-agents) can now browse the web, interact with applications, conduct research, shop online, schedule appointments, fill out forms, and make decisions with little or no human involvement.

As these systems continue to improve, the line separating human activity from machine-driven activity is becoming increasingly difficult to recognize. That shift could fundamentally change what we even mean when we talk about “web traffic” in the future.

The internet was originally built on the assumption that humans were the primary participants. That assumption is rapidly eroding. As AI-driven automation becomes increasingly autonomous, the future of the web may depend less on distinguishing humans from bots – and more on deciding what kind of machine-driven internet we are willing to accept.

## The line between human and machine is gone

The impact of this shift reaches further than most site owners realize. Infrastructure costs are rising. Analytics are becoming harder to trust. The scraper economy is shifting value away from the publishers who create content toward the systems that extract it. And as AI-powered agents become capable of browsing, researching, and making decisions autonomously, the question stops being “how do I manage bot traffic” and starts being something larger.

The internet was built on the assumption that there was a person on the other side of every request. That assumption is eroding faster than the infrastructure, the regulations, and the business models built on top of it can adapt.

We are well into an age where machines talk to machines without the need for human interaction.

For a deeper look at the data behind this shift, read the [full Kinsta AI & Bot Traffic Report](https://kinsta.com/ai-bot-traffic/). If you’re already seeing the effects on your site, Kinsta’s [Bot Protection](https://kinsta.com/bot-protection/) gives you the controls you need to manage them.

Bud Kraus

Bud Kraus has been working with WordPress as an in-class and online instructor, site developer, and content creator since 2009. He has produced instructional videos and written many articles for WordPress businesses.
