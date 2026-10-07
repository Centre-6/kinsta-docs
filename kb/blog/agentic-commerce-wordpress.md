---
url: "https://kinsta.com/blog/agentic-commerce-wordpress/"
title: "Your WordPress site now has a third type of visitor (and it completes purchases)"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "Bot Traffic", "Your WordPress site now has a third type of visitor (and it completes purchases)"]
kinsta_last_updated: "2026-08-18T18:18:38+00:00"
sitemap_lastmod: "2026-08-18T18:18:38"
fetched_at: "2026-10-07T22:42:02Z"
sha256: "a3af0f8878fe398dc39d86dce25c88b45811e63a606c68f8e27476faa270608c"
body_chars: 16513
extracted_with: "main article"
status: "live"
---

# Your WordPress site now has a third type of visitor (and it completes purchases)

**Section:** Resource Center > Blog > Bot Traffic > Your WordPress site now has a third type of visitor (and it completes purchases)
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/agentic-commerce-wordpress/
**Kinsta last updated:** 2026-08-18T18:18:38+00:00

## On this page

- [Meet the visitor that reads like a bot and buys like a customer](#meet-the-visitor-that-reads-like-a-bot-and-buys-like-a-customer)
- [AI-referred traffic converts better than human traffic](#ai-referred-traffic-converts-better-than-human-traffic)
- [Cloudflare splits AI bot blocking into three categories](#cloudflare-splits-ai-bot-blocking-into-three-categories)
- [3 things that decide whether an agent completes your checkout](#3-things-that-decide-whether-an-agent-completes-your-checkout)
  - [Pricing and availability need to live in HTML](#pricing-and-availability-need-to-live-in-html)
  - [Your page needs to respond before the agent times out](#your-page-needs-to-respond-before-the-agent-times-out)
  - [Your Bot Protection settings need to let the converting sessions through](#your-bot-protection-settings-need-to-let-the-converting-sessions-through)
- [Check what’s happening on your own site in MyKinsta](#check-whats-happening-on-your-own-site-in-mykinsta)
  - [Test your checkout without JavaScript](#test-your-checkout-without-javascript)
  - [Watch response times under a concurrent load](#watch-response-times-under-a-concurrent-load)
- [Agent traffic is no longer bot noise but a full channel](#agent-traffic-is-no-longer-bot-noise-but-a-full-channel)

---

Author
:   [Joel Olawanle](https://kinsta.com/blog/author/joelolawanle/ "Posts by Joel Olawanle")

Published
:   September 8, 2026

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![](https://kinsta.com/wp-content/uploads/2026/08/the-rise-of-ai-means-every-website-now-has-machine-visitors-1024x512.png)

Bots now generate more web traffic than humans, but what’s more interesting is the type of bot driving these interactions. In addition, studying what those bots do when landing on your site is a worthwhile pursuit.

The typical AI traffic discourse centers on [crawlers](https://kinsta.com/blog/ai-crawlers-wordpress/) scraping your content to train a model, which costs you resources. However, there’s a second category: AI agents that visit on a person’s behalf to read your site and interact on it as a customer would. This has revenue potential, but the current tech, without tweaking, stops both types of bots rather than only the resource hogs.

## Meet the visitor that reads like a bot and buys like a customer

For most of the internet’s history, a WordPress site has received three kinds of visitors: humans, search crawlers, and scripts running repeatable tasks.

AI agents are now a fourth kind. These read a page’s structure like a crawler, but interact like a human. It’s relatively straightforward for an AI agent to check a product’s price, compare it, and complete the checkout.

Given this, agentic bots deserve your attention. Cloudflare’s traffic data now shows [automated requests outweighing human requests](https://www.techtimes.com/articles/317877/20260605/bot-traffic-passes-humans-online-cloudflare-says-agentic-ai-drove-575-share.htm) for the first time. Within that automated share, [HUMAN Security’s State of AI Traffic research](https://www.humansecurity.com/learn/blog/ai-traffic-growth-2025-key-findings/) found traffic from AI agents and agentic browsers growing at a pace that dwarfs every other category.

In fact, AI agents are already shipping in some popular products:

- **Chrome’s built-in auto-browse functionality** [researches, compares, and completes](https://blog.google/products-and-platforms/products/chrome/gemini-3-auto-browse/) multi-step tasks such as checkouts across the sites you visit.
- **OpenAI’s browsing agent**, which is [within the ChatGPT app](https://help.openai.com/en/articles/20001371-evolving-atlas-into-chatgpt-for-browser-based-agentic-work) and its Chrome extension, navigates pages and completes tasks on a person’s behalf.
- **Perplexity’s Comet browser** reads across a person’s open tabs to research and act for them. It’s [available as a free download](https://www.perplexity.ai/comet).
- **Claude for Chrome** ([Anthropic’s browser extension](https://claude.com/claude-for-chrome)) navigates, clicks, and fills forms on a person’s behalf.

These and many more are shipping to production traffic on your site, but the settings built to stop training crawlers aren’t designed with them in mind.

## AI-referred traffic converts better than human traffic

[Adobe’s Q1 2026 retail data](https://techcrunch.com/2026/04/16/ai-traffic-to-us-retailers-rose-393-in-q1-and-its-boosting-their-revenue-too/), drawn from over one trillion visits to US retail sites, tells a story that was impossible to predict a year ago.

In March 2025, AI-referred traffic converted 38% worse than standard channels like paid search and email. By March 2026, the same traffic was converting 42% better. That’s an 80-percentage-point reversal in twelve months. AI-referred shoppers also generated 37% more revenue per visit than non-AI traffic, spent 48% longer on-site, and browsed 13% more pages per visit. Traffic volume from AI sources grew 393% year over year in Q1 2026 alone.

The reason is behavioral. A human arriving through organic search could be at any stage of a purchase decision. An agent sent to your site has already been assigned a specific task.

It’s this traffic that [WooCommerce stores](https://kinsta.com/blog/woocommerce-tutorial/), membership platforms, and quote or booking forms want to capture:

- **Shoppers researching a plugin** will send an agent to check your pricing and report back with a recommendation.
- **Someone checking service coverage** has an agent fill out your quote form and wait for a reply.
- **Buyers comparing subscription tiers** let an agent complete the signup once the comparison is done.

Each of these tasks can now be completed by an agent end-to-end, if your site lets it.

## Cloudflare splits AI bot blocking into three categories

![Cloudflare's traffic controls showing Search, Agent, and Training as three independently switchable AI categories.](https://kinsta.com/wp-content/uploads/2026/08/block-bots-cloudflare.png)

Cloudflare’s traffic controls showing the category options of Search, Agent, and Training.

Infrastructural layers are starting to catch up. Cloudflare’s current setup replaces the previous single AI-bot switch with three independently controllable categories [available to every customer](https://blog.cloudflare.com/content-independence-day-ai-options/).

- **Search** covers crawlers that index your content so it can be surfaced later in an AI-generated answer, typically sending some traffic back your way.
- **Training** covers crawlers that absorb your content to build or fine-tune a model, with no return traffic or transactional intent.
- **Agent** covers real-time, user-directed traffic acting on a specific person’s behalf, including checkout-completing sessions.

Cloudflare blocks **Training** and **Agent** by default on pages that carry advertising, while **Search** stays enabled. Existing sites will keep the current settings unless you change them. However, multiple-purpose crawlers (including Googlebot) get evaluated against whichever rule is strictest. So, a blanket block of **Training** can end up catching your search visibility along with it.

Kinsta’s [Bot Protection](https://kinsta.com/bot-protection/) already makes this kind of judgment call for you. It currently groups AI crawlers under one switch rather than mirroring a three-way split specific to Cloudflare’s own dashboard. However, you need to know how to work with what you have.

## 3 things that decide whether an agent completes your checkout

Whether an agent finishes its task on your site comes down to three factors, all on the infrastructure side rather than the content side. For much of this, Kinsta’s functionality and infrastructure can be a benefit.

### Pricing and availability need to live in HTML

An agent reads a page’s underlying structure rather than its visual layout. In cases where the price only appears after a click, or your stock count loads via a post-rendering AJAX call, an agent working from the accessibility tree won’t see it.

There are levels to this, however. For instance, a [study testing an AI agent](https://nohacks.co/blog/how-ai-agents-see-your-website) on real-world web tasks found it succeeded in nearly 80% of cases. With keyboard-only interaction (which simulates how a screen reader user would navigate), the success rate dropped to 42%.

The typical culprits are predictable once you know what to look for:

- **Accordion FAQs** hide answers behind a click an agent may never trigger.
- **Tabbed pricing tables** often render only one tab into the page’s initial markup.
- **Stock indicators** loaded through JavaScript may not exist when an agent reads the page.

Google’s proposed [WebMCP standard](https://developer.chrome.com/docs/ai/webmcp) is one attempt to fix this at the browser level. It lets a site expose its checkout and pricing functions directly rather than leaving an agent to infer them from the page. However, it’s still an early-stage trial so semantic HTML is the current dependable fix.

### Your page needs to respond before the agent times out

An agent working through a multi-step task won’t wait out a slow page as a human might. Instead, it will simply drop a stalling page and cost you a conversion.

[Core Web Vitals](https://kinsta.com/blog/core-web-vitals/) thresholds are a reasonable proxy for what an agent will tolerate, even though they were built around a human’s experience of a page. A Largest Contentful Paint under 2.5 seconds gives both a human and an agent enough room to finish a task in the same session.

Also, you can waste all the time you’re trying to save by guessing at slow page fixes. This is where you can use [Kinsta’s APM tool](https://kinsta.com/apm-tool/) to study a checkout or product page, which will narrow the delay down to the specific plugin, database query, or third-party call responsible.

![The Transaction tab of the MyKinsta APM tool with monitoring running against a WordPress website.](https://kinsta.com/wp-content/uploads/2026/08/apm-tool-2.png)

The Transaction tab of the APM tool with monitoring running against a WordPress website.

Once a monitoring window is running, the **Transactions** view shows which page or endpoint is slow. You can then understand which plugin or query sits behind it, fix the right element, and save time to help agents stick around for the right reasons.

### Your Bot Protection settings need to let the converting sessions through

If your bot protection settings treat every automated visitor as a training crawler, the right bots might not even reach your site. These bot sessions can look the same to a system that can’t tell them apart.

This is why [Kinsta’s Bot Protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) gives you four separate controls to make that call:

- **Four protection levels**, ranging from **Block malicious traffic** to **Challenge everyone**, control how aggressively unclassified and likely-bot traffic is challenged across your whole site.
- **A dedicated Block AI crawlers toggle** removes AI crawler traffic at once, including checkout-completing Agent sessions and **Training** crawlers.
- **Allow typical WordPress automations** keeps your REST API, plugin integrations, and background tasks running even at a stricter protection level. This matters for agent sessions hitting your checkout and API endpoints.
- **Always Allow exceptions** (addable by IP, path, or user agent) let you name specific traffic that should never be blocked or challenged regardless of your protection level.

A practical middle ground for a WooCommerce store or booking site is to enable **Allow typical WordPress automations** so checkout and REST API traffic isn’t caught by a stricter protection level. It’s also wise to treat **Block AI crawlers** as a temporary diagnostic tool rather than a setting to leave permanently on.

![The MyKinsta Bot Protection screen showing the four protection levels available to a site.](https://kinsta.com/wp-content/uploads/2026/08/bot-level.png)

The Bot Protection screen showing the four protection levels available.

If you’re trying to stop training crawlers specifically without losing agent-driven purchases, **Always Allow exceptions** for known agent user agents gives you more precision than the toggle can offer on its own.

## Check what’s happening on your own site in MyKinsta

However, before you change any setting, it’s good to confirm what your site’s traffic looks like rather than assuming you already handle agent sessions correctly. MyKinsta gives you a few places to check.

First, the **Sites** > ***[sitename]*** > **Bot protection** screen gives you two sets of insights combined into one graph. The **Request breakdown** shows every request to your site over the past 24 hours with different classifications. This can tell you the proportions and ratios of traffic you’re dealing with.

The **Bot protection results** chart shows how this traffic was handled: either **allowed**, **challenged**, or **blocked**:

![The Request breakdown chart in MyKinsta showing traffic classified by category and the results of the bot protection.](https://kinsta.com/wp-content/uploads/2026/08/request-breakdown.png)

MyKinsta’s Request breakdown showing traffic classified by category.

The **Request breakdown** essentially cross-references itself. For example, if a share of your automated traffic is being challenged or blocked, you can see these ‘join’ with the **AI crawlers** category. However, you can’t tell whether that’s training crawlers or converting agent sessions.

Here, you can look at the timing of any spike in blocked traffic relative to your order or lead volume for the same period; a drop in one alongside a rise in the other suggests legitimate agent sessions are getting caught.

### Test your checkout without JavaScript

An agent working from a page’s underlying structure has a similar experience to that of someone using a screen reader. There are two quick tests that show you where the flow breaks.

First, open your DevTools in the browser, then go to **Settings** > **Debugger**. Next, check **Disable JavaScript**. Then reload the page and try adding an item or going to checkout.

![The browser DevTools open showing the Disable JavaScript setting checked under the Debugger panel.](https://kinsta.com/wp-content/uploads/2026/08/disable-javascript.png)

Browser DevTools showing the checked Debugger > Disable JavaScript setting.

Any glitches or errors are signs the step depends on a script that may never run. For example, an Add to cart button built as a clickable `<div>` often has no fallback behavior without its script.

You can also run an accessibility scanner such as [axe](https://www.deque.com/axe/) or [WAVE](https://wave.webaim.org/) against the same checkout flow. Every missing label, hidden field, or unreachable button here won’t be visible to an agent. Between the two tests, you’ll have a specific list of elements to fix.

### Watch response times under a concurrent load

An agent session that opens several tabs or checks several product pages in quick succession is more like a small burst of concurrent traffic. Many performance checks won’t detect this type of load pattern, so a single-request test will pass cleanly.

Within MyKinsta’s Analytics (**Sites** > `sitename` > **Analytics** > **Performance)**, look at the **Average PHP + MySQL response time.** This (along with the detailed list at the bottom of the screen) can help you find the slowest paths on your site rather than a site-wide average that hides the problem.

![MyKinsta's Performance analytics showing average PHP and MySQL response time for the past two months.](https://kinsta.com/wp-content/uploads/2026/08/kinsta-analytics.png)

MyKinsta’s Performance analytics showing average PHP and MySQL response time.

From there, run the APM Tool and open several sessions against your cart and search endpoints at once. You can then trace where the response time starts to climb.

If the **PHP thread limit** chart in the Performance section of the **Analytics** shows your site hitting its ceiling, it’s something you can fix. Increasing your thread allocation under **Sites** > ***[sitename]*** > **Info** > **PHP performance** > **Change** is a simple way to give your site more room to handle several agent sessions at once.

## Agent traffic is no longer bot noise but a full channel

For training crawlers, blocking and reclaiming the resources is still the right move. It’s not right for AI agents that complete checkouts, so you need to harness all of the tools at your disposal to filter bots correctly.

The fix is to check whether your pricing and stock data render into the page’s initial HTML. Tracing your slowest pages and reviewing your bot protection settings lets you treat existing traffic with precision and keep server resources efficient.

To see how Bot Protection, APM, and Kinsta’s Cloudflare integration work together to keep your infrastructure ready for both kinds of visitor, check out [Kinsta’s managed WordPress hosting](https://kinsta.com/wordpress-hosting/).

Joel Olawanle
[Kinsta](https://kinsta.com/)

Joel is a Frontend developer working at Kinsta as a Technical Editor. He is a passionate teacher with love for open source and has written over 300 technical articles majorly around JavaScript and it's frameworks.

- [Website](https://joelolawanle.com/)
- [LinkedIn](https://www.linkedin.com/in/olawanlejoel/)
- [Twitter](https://twitter.com/olawanle_joel)
- [YouTube](https://www.youtube.com/@joelolawanle)
