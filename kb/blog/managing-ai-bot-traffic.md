---
url: "https://kinsta.com/blog/managing-ai-bot-traffic/"
title: "The 7 biggest mistakes site owners make after discovering AI bot traffic"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: []
kinsta_last_updated: "2026-09-17T12:00:59"
change_signal: "2026-09-17T12:00:59"
fetched_at: "2026-10-07T22:58:24Z"
sha256: "263eb8ee1284ba011effcf368c7ec9aaf2e303465c6c8e27136f2d3e964dd878"
body_chars: 17783
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# The 7 biggest mistakes site owners make after discovering AI bot traffic

**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/managing-ai-bot-traffic/
**Kinsta last updated:** 2026-09-17T12:00:59

## On this page

- [Mistake 1: treating the percentage as the diagnosis](#mistake-1-treating-the-percentage-as-the-diagnosis)
- [Mistake 2: blocking every bot because the traffic is automated](#mistake-2-blocking-every-bot-because-the-traffic-is-automated)
- [Mistake 3: treating every AI crawler spike as a security emergency](#mistake-3-treating-every-ai-crawler-spike-as-a-security-emergency)
- [Mistake 4: watching request volume while ignoring where the requests go](#mistake-4-watching-request-volume-while-ignoring-where-the-requests-go)
- [Mistake 5: blocking the crawler and leaving the crawl trap behind](#mistake-5-blocking-the-crawler-and-leaving-the-crawl-trap-behind)
- [Mistake 6: assuming robots.txt has stopped the traffic](#mistake-6-assuming-robotstxt-has-stopped-the-traffic)
- [Mistake 7: copying another site’s firewall rules without checking what they would block](#mistake-7-copying-another-sites-firewall-rules-without-checking-what-they-would-block)
- [What to do when you discover AI bot traffic](#what-to-do-when-you-discover-ai-bot-traffic)

---

When you discover that a large share of your website traffic comes from bots, blocking them can feel like the obvious next step. In some cases, the numbers do call for an immediate response.

PatronView recently documented [3.6 million requests hitting its site in a single day](https://patronview.com/news/99-percent-of-my-website-traffic-is-bots/), with traffic coming from more than 360,000 IP addresses. The site owner eventually built a fairly aggressive set of Cloudflare rules to get the traffic under control.

We’ve seen extreme cases on our own infrastructure, too. In our [AI and bot traffic report](https://kinsta.com/ai-bot-traffic/), one crawler generated 3.75 million requests to add-to-cart URLs in 24 hours. Another repeating loop pattern drove hundreds of millions of requests before we introduced a rule to catch it.

Those cases are real, but they don’t describe every website.

In [our latest analysis](https://kinsta.com/ai-crawler-traffic) of more than 5,000 WordPress sites, AI bots accounted for just 1.57% of bandwidth at the median site, compared with 17.8% at the 90th percentile and 90.3% at the 99th, while more than 1,000 sites recorded no AI-bot bandwidth at all.

That spread is why discovering AI bot traffic and diagnosing an AI bot problem are two different things.

The decisions you make next can affect site performance, integrations, search visibility, and whether AI tools can surface your content. Before changing anything, you need to know what the bots are actually doing.

Here are some mistakes we see site owners make when they skip that step.

## Mistake 1: treating the percentage as the diagnosis

If AI crawlers account for 20% of your site’s requests, that number alone doesn’t tell you whether there’s a problem.

A large share of requests to cached articles may place relatively little pressure on the application, while a smaller number repeatedly hitting search results, filtered product pages, or cart URLs can create far more work.

This is one reason network-wide bot statistics require some care when applied to an individual site.

Our [latest research](https://kinsta.com/ai-crawler-traffic) found that the mean number of AI-bot requests per site ranged from 667 to 928 a day across four measurements, compared with a median of just 33 to 67 requests, while roughly 20% to 27% of sites received no AI-bot requests on a measured day.

In other words, a small group of heavily crawled sites pulls the average upward.

So if you read that bots make up more than half of web traffic, or see another site owner reporting 99% bot traffic, don’t use that number to decide what your own site needs.

Start with your own traffic.

For Kinsta customers, the [Bot protection section](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) in MyKinsta shows how requests are being classified, including likely humans, verified bots, likely bots, AI crawlers, excessive-rate AI crawlers, automated traffic, and malicious traffic.

![Request breakdown chart.](https://kinsta.com/wp-content/uploads/2026/08/kinsta-bot-protection-data.png)

Request breakdown chart.

You can then use **Top traffic** to see the paths, user agents, countries, and IP addresses behind a specific traffic type.

![Top traffic report.](https://kinsta.com/wp-content/uploads/2026/08/top-traffic-bot-data.png)

Top traffic report.

Before taking action, you should be able to answer a few basic questions:

- How much AI traffic is actually reaching the site?
- Which pages or endpoints is it requesting?
- Which crawlers, agents, or other automated systems are responsible?
- Is any of that traffic affecting performance, bandwidth, PHP threads, or the experience of real visitors?

Our latest report frames this as looking at the **position, pattern, and profile** of the traffic. A site receiving very little AI traffic with ordinary request behavior may need no action, while one seeing sustained crawler traffic against expensive dynamic URLs deserves a much closer look.

## Mistake 2: blocking every bot because the traffic is automated

The term “AI bot” now covers several different kinds of traffic. Some crawlers collect public content for model training or AI search, while others fetch pages in response to a user’s request.

Those differences matter when you decide what to allow. OpenAI, for example, uses GPTBot for content that may be used to improve its models, while OAI-SearchBot helps make websites discoverable in ChatGPT search. Blocking OAI-SearchBot can therefore affect whether your content appears in ChatGPT search results.

Anthropic makes a similar distinction. ClaudeBot collects web content that may contribute to model training, Claude-SearchBot is used for search, and Claude-User can retrieve a website when someone using Claude asks for it.

Perplexity reports that PerplexityBot is used for its search index and Perplexity-User for requests made in response to a user’s question.

Google gives publishers a separate `Google-Extended` control for how crawled content can be used with Gemini. Google explicitly says changing that setting doesn’t affect inclusion or ranking in Google Search.

Putting all of these systems into a single “AI” bucket throws away information you can use.

If you’d prefer not to expend site resources on model training, you may choose to restrict training crawlers while leaving search and retrieval systems accessible. If your problem is an AI agent repeatedly hitting a dynamic endpoint, changing your training-crawler policy may not solve it.

There is a business question here, too. Our consumer research found that 44.7% of respondents said they always or most of the time visit a company’s website after receiving an AI recommendation. That doesn’t mean AI crawler access automatically produces referral traffic, but it does mean AI discovery is worth considering before you make a blanket decision about visibility.

At Kinsta, the **Block AI crawlers** control lets customers block AI crawlers, including verified ones, without blocking traditional search engine crawlers such as Googlebot and Bing.

![Block AI crawlers.](https://kinsta.com/wp-content/uploads/2026/08/block-ai-crawlers.png)

Block AI crawlers.

We also warn customers that blocking AI crawlers can reduce visibility in AI-powered search results, summaries, or recommendations.

## Mistake 3: treating every AI crawler spike as a security emergency

Bots can create security problems through brute-force attempts, DDoS attacks, credential attacks, and other abusive automation, but a verified AI crawler sending too many legitimate requests is a different kind of problem.

During our [bot traffic live event](https://kinsta.com/webinars/bot-traffic-reality-check/), Kinsta CTO Daniel Pataki explained why he worries about the way site owners respond when those two things get mixed together:

*“I fear overreaction in this case more than I fear underreaction because it is not a security issue.”*

He was talking about the wider AI crawler problem, where much of the troublesome traffic we’re seeing comes from legitimate systems crawling inefficiently rather than an attacker trying to compromise the site.

The response changes when the site is already suffering. If bots are tying up server resources, slowing pages, or stopping real customers from using the site, stabilizing the site comes first. Daniel recommended temporarily blocking bot traffic when it is causing an active problem, then investigating once the site is under control.

The mistake is turning that emergency measure into a permanent policy without finding out what happened.

[Kinsta’s Bot Protection](https://kinsta.com/bot-protection/) gives you several levels of control, from baseline protection against malicious traffic to blocking automations or challenging likely bots when stricter protection is needed. Excessive-rate AI crawlers can also be challenged at the appropriate protection levels.

![Select the level of bot protection for your site.](https://kinsta.com/wp-content/uploads/2026/08/chnage-bot-protection-level.png)

Select the level of bot protection for your site.

A sudden performance incident may justify stronger controls today. Once the incident has passed, check what was hitting the site and whether those stronger controls still make sense.

## Mistake 4: watching request volume while ignoring where the requests go

Our infrastructure data makes this difference easy to see. A request for a cached blog post and one for an uncached WooCommerce search page both count as a single request, even though the second can require far more server work.

Here is an illustration from the [bot traffic reality check live event](https://kinsta.com/webinars/bot-traffic-reality-check/):

![Static vs dynamic page request.](https://kinsta.com/wp-content/uploads/2026/08/website-request-flow.png)

Static vs dynamic page request.

When a cached page is available, WordPress can handle much of the request without regenerating the page.

A dynamic request may need a PHP thread (also known as a worker), database queries, page generation, and sometimes session handling before WordPress can return anything. Cart and checkout activity can add more work.

Now repeat that process thousands of times.

Across three measurements in [our latest study](https://kinsta.com/ai-crawler-traffic), between 76.9% and 90.5% of AI crawler requests went to dynamic content. Human traffic stayed between 18.3% and 18.9%.

That difference tells you much more about potential infrastructure pressure than a raw request count.

Consider the add-to-cart incident we found in our [AI bot traffic research](https://kinsta.com/ai-bot-traffic/). One crawler generated 3.75 million requests in 24 hours, roughly one request every 23 milliseconds. Each request could make WordPress perform work for a “visitor” who was never going to buy anything.

This is also why two sites with the same percentage of AI traffic can behave very differently.

A content site where crawlers mostly request cached articles may handle a large volume without much trouble, while a WooCommerce store can feel the impact much sooner if even a smaller number of requests repeatedly hit search, filters, cart actions, account pages, or other uncached routes.

Once you discover a spike, look past the user agent.

In MyKinsta, you can filter **Top traffic** by **AI crawlers** and inspect the paths they request most often.

![Filter traffic type.](https://kinsta.com/wp-content/uploads/2026/08/filter-traffic-type.png)

Filter traffic type.

Then compare that with cache information, server bandwidth, and performance data to see whether those requests are reaching the application and creating work.

![Top requests by server bandwidth.](https://kinsta.com/wp-content/uploads/2026/08/top-requests-server-bandwidth.png)

Top requests by server bandwidth.

Seeing `GPTBot` or another crawler at the top of a report is useful. Seeing that thousands of its requests are going to `/blog/` tells you one thing. Seeing them go to search results or a parameterized WooCommerce URL tells you something else.

## Mistake 5: blocking the crawler and leaving the crawl trap behind

Sometimes the bot is only the thing that exposes a problem already sitting in your URL structure.

WordPress sites can generate a lot of URLs from query parameters, search pages, filtered archives, pagination, calendars, product variations, and ecommerce actions.

A person may recognize that two slightly different URLs lead to essentially the same page, while a crawler simply sees more links to follow.

If each page produces another set of URLs that appear new, the crawler can keep following them. That is how you end up with patterns that look much more aggressive than anyone intended.

We saw this in our [earlier infrastructure research](https://kinsta.com/ai-bot-traffic/). One repeating pattern became large enough that a single rule designed to catch it filtered 550 million requests in 30 days.

Blocking the crawler may stop the immediate load, but it doesn’t remove the URL pattern that caused the crawler to find new pages.

When a particular path suddenly dominates AI crawler traffic, inspect the path itself:

- Is WordPress generating large numbers of parameter combinations?
- Can a crawler keep moving through calendar or pagination URLs indefinitely?
- Are search and filter pages exposing thousands of URL variations?
- Are action URLs such as add-to-cart links crawlable when they don’t need to be?
- Does every URL being generated need to exist and be discoverable?

You may still decide to block or challenge the crawler, but first understand what kept bringing it back.

This is especially important for agencies. If several client sites use the same plugin, WooCommerce configuration, theme, or URL pattern, an aggressive crawler can expose the same issue across more than one site. Fixing the behavior can be more useful than maintaining an ever-growing list of bot names.

## Mistake 6: assuming robots.txt has stopped the traffic

A `robots.txt` change can be the right response when you want to tell a reputable crawler not to access part or all of your site, but you still need to check the traffic afterward.

`robots.txt` relies on the crawler honoring the instruction and doesn’t physically prevent the request from reaching your site.

We’ve covered this distinction in detail in our [guide to AI crawlers](https://kinsta.com/blog/llms-txt-vs-robots-txt-wordpress/). `robots.txt` communicates crawl preferences, while `llms.txt` provides a structured content index for tools that choose to read it. *Enforcement happens elsewhere.*

This matters after discovering a performance problem, because just editing a file can make you feel like the problem has been handled.

Check your logs or bot analytics. If requests from the crawler fall after your `robots.txt` change, you have evidence that it worked. If the traffic continues, or you are dealing with another automated system that doesn’t follow the instruction, you need an enforcement control.

The same applies when your problem is request rate rather than access itself. A crawler may be allowed to read your content and still request it at a rate your site cannot comfortably serve.

## Mistake 7: copying another site’s firewall rules without checking what they would block

The [PatronView example](https://patronview.com/news/99-percent-of-my-website-traffic-is-bots/) is useful because the site’s response was based on its own data.

Its audience is overwhelmingly in North America, so the owner challenges traffic coming from other continents. He checked his real visitor data before challenging users with old browser versions. He also monitors how many challenged visitors actually complete the challenge. In one period, only 0.24% of more than 100,000 challenges were solved.

Those numbers make the rules easier to justify for that site, but applying the same setup to an international e-commerce store could end up challenging legitimate customers. The same risk appears when teams stack several security tools because each one seems useful on its own.

A WordPress site might have hosting-level bot protection, Cloudflare rules, a security plugin, rate limiting, country blocks, and custom WAF rules all making decisions about the same request. Debugging a false positive becomes much harder when you don’t know which layer made the decision.

For Kinsta customers, we specifically recommend against combining [Kinsta Bot Protection with additional custom bot protection layers](https://kinsta.com/blog/kinsta-bot-protection-vs-cloudflare/). Conflicting classifications can cause legitimate visitors or integrations to be blocked.

Higher protection levels can also affect legitimate automation such as APIs, monitoring tools, webhooks, and WordPress integrations. MyKinsta therefore includes an **Allow typical WordPress automations** option and always-allow exceptions for trusted IP addresses, paths, and user agents.

![Allow typical WordPress automations.](https://kinsta.com/wp-content/uploads/2026/08/allow-typical-wp-automation-and-exceptions.png)

Allow typical WordPress automations.

If you run an agency, a standard process is more useful than a standard rule set. You can use the same process across 20 client sites by identifying the traffic, inspecting its paths, checking performance, choosing a control, testing it, and monitoring the result.

## What to do when you discover AI bot traffic

Start with what is happening on your site. If bot traffic is affecting real visitors, protect the site first, then inspect how much traffic you are receiving, which paths it reaches, and which systems are responsible.

From there, choose the smallest change that solves the problem. That could mean updating `robots.txt`, blocking or challenging a crawler, fixing a crawlable URL pattern, or doing nothing if the traffic isn’t causing harm.

Kinsta customers can do much of this investigation directly in MyKinsta. [Bot traffic analytics](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#bot-traffic) separates AI crawlers, excessive-rate AI crawlers, verified bots, automated traffic, and other request types, while **Top traffic** shows the paths, user agents, countries, and IPs behind them.

You can also compare that activity with [cache behavior](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#cache), [server bandwidth](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#bandwidth), and [PHP performance](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#performance) to see whether the traffic is actually pressuring your site before deciding what to block.
