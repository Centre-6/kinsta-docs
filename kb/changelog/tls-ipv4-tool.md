---
url: "https://kinsta.com/changelog/tls-ipv4-tool/"
title: "TLS 1.3, Public IPv4 Tool, Better Status Notifications, and MyKinsta Updates"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2025-09-19T06:37:31"
change_signal: "2025-09-19T06:37:31"
fetched_at: "2026-10-07T22:58:23Z"
sha256: "9a0ee097f29e9db3a29b94b27fa0be10f1fde03a588435d61802ceffd69b1ce7"
body_chars: 9462
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# TLS 1.3, Public IPv4 Tool, Better Status Notifications, and MyKinsta Updates

**Product:** Changelog
**Source:** https://kinsta.com/changelog/tls-ipv4-tool/
**Kinsta last updated:** 2025-09-19T06:37:31

## On this page

- [TLS 1.3 Support on All Servers](#tls-13-support-on-all-servers)
- [New Public IPv4 Checker Tool](#new-public-ipv4-checker-tool)
- [Reverting Error Pages Back to Non-Branded](#reverting-error-pages-back-to-non-branded)
- [Better Status Page Subscription Options](#better-status-page-subscription-options)
- [MyKinsta Updates](#mykinsta-updates)
  - [Free Basic Migrations are Now Available in MyKinsta](#free-basic-migrations-are-now-available-in-mykinsta)
  - [Knowledge Base Articles in MyKinsta](#knowledge-base-articles-in-mykinsta)
  - [Edit Your Avatar Link](#edit-your-avatar-link)
  - [MyKinsta Login Redirects Are Now Deep-Linked](#mykinsta-login-redirects-are-now-deep-linked)
  - [Revamped UI for Payment Methods Page](#revamped-ui-for-payment-methods-page)

---

Our favorite time of the month; another **feature update roundup!** 🤗 While it might be August, our developer and sysadmin teams have been working around the clock to push out new improvements, features, and even new tools. Today we’ll dive into a few you’ll want to know about.

## TLS 1.3 Support on All Servers

[TLS 1.3](https://kinsta.com/blog/tls-1-3/) is the latest encryption protocol update that is both faster (reducing HTTPS overhead) and more secure than TLS 1.2. **Kinsta now supports TLS 1.3 on all of our servers and via our Kinsta CDN.**

According to [Caniuse](https://caniuse.com/#feat=tls1-3), browser support for TLS 1.3 as of August 2019 sits at a little over 77%. But don’t worry, TLS 1.3 also allows a connection to negotiate back down to TLS 1.2 where either side does not support TLS 1.3. This ensures backward compatibility.

If you’re curious whether or not your server or host supports TLS 1.3 yet you can use the [SSL Server Test](https://www.ssllabs.com/ssltest/) tool. Simply scan your domain and scroll down to the “Protocol Features” section. It will say either yes or no next to the supported TLS version running on the server. Below is a WordPress site scanned at Kinsta.

![TLS 1.3 server support](https://kinsta.com/wp-content/uploads/2019/08/tls-1.3-server-support.png)

TLS 1.3 server support (Kinsta WordPress site)

## New Public IPv4 Checker Tool

There are a lot of different reasons you might need to look up your public IP address. Perhaps you accidentally got blocked from a firewall rule and need our support team to whitelist you. Or maybe you want to lock down access to only your IP. To easily find your public IP, we’ve released a new [simple IPv4 lookup tool](https://kinsta.com/tools/what-is-my-ip/).

One-click copy your IP address to your clipboard!

[![Kinsta Public IP lookup tool](https://kinsta.com/wp-content/uploads/2019/08/public-ip-lookup-tool-1.png)](https://kinsta.com/tools/what-is-my-ip/)

Kinsta Public IP lookup tool

## Reverting Error Pages Back to Non-Branded

We aren’t afraid to change a feature if we see it’s not working for you. 👍 We heard your feedback and have reverted the way we do error pages. Previously we showed a custom Kinsta branded page for 500 errors, [502 errors](https://kinsta.com/blog/502-bad-gateway/), etc. (see example below).

![Kinsta branded 500 error page](https://kinsta.com/wp-content/uploads/2019/08/kinsta-branded-500-error-page.jpg)

Kinsta branded 500 error page

While the above page might be helpful, we heard from a lot of you that you didn’t want your visitors seeing the Kinsta brand. Especially those of you working with clients or reselling Kinsta hosting services. We totally understand! Therefore, we’ve reverted these back to the classic error pages you were most likely used to before (see example below).

![500 internal server error in WordPress](https://kinsta.com/wp-content/uploads/2017/12/500-internal-server-error-in-wordpress.png)

500 internal server error in WordPress

We’ve seen that most of you will reach out to our support team anyways for help. And those of you already familiar with say debugging a PHP code error, we probably won’t hear from.

Don’t forget, we have a lot of helpful tutorials on our site on [how to troubleshoot errors](https://kinsta.com/?s=error) like these.

## Better Status Page Subscription Options

Back in September 2018, we released our new [status page](https://kinsta.com/changelog/status-page/). However, up until this month, you couldn’t subscribe to individual data center notifications. This means some of you might have received a lot of our regular ongoing maintenance messages in your inboxes. Great news, you can now subscribe to **only get updates about the data center where your site is hosted**.

If you’ve already subscribed to our notifications, you can modify your subscription in two ways:

1. Click the “manage your subscription” at the bottom of an email you’ve received.
2. Visit [status.kinsta.com](https://status.kinsta.com/) and re-subscribe using the same email address via the purple button at the top of the page.

![Kinsta status messages subscription](https://kinsta.com/wp-content/uploads/2019/08/subscribe-kinsta-status-messages.png)

Kinsta status messages subscription

On the subscription management page, you can deselect any areas of the Kinsta platform or data centers for which you don’t want to receive notifications. If you haven’t yet signed up, simply enter your email and you’ll be able to choose which ones you want to subscribe to.

![Choose Kinsta status page subscriptions](https://kinsta.com/wp-content/uploads/2019/08/choose-kinsta-status-subscriptions-1.png)

Choose Kinsta status page subscriptions

If you don’t remember the name of your data center, you can find it within the “Info” screen of your site in the MyKinsta dashboard.

![MyKinsta data center](https://kinsta.com/wp-content/uploads/2019/08/mykinsta-data-center.png)

MyKinsta data center

## MyKinsta Updates

Many of our **MyKinsta dashboard improvements come directly from your feedback!** We can’t thank you enough for always sharing your positive and negative feedback with us. So keep the ideas coming. 😄

Here are just a few changes and updates we’ve implemented over the past couple weeks.

### Free Basic Migrations are Now Available in MyKinsta

Previously only our premium migrations were available in our migration form in the MyKinsta dashboard.

We are now offering unlimited free basic migrations from select hosts such as [WP Engine](https://kinsta.com/wp-engine-alternative/), [Flywheel](https://kinsta.com/flywheel-hosting-alternative/), [SiteGround](https://kinsta.com/siteground-alternative/), [Pagely](https://kinsta.com/pagely-alternative/), [Pantheon](https://kinsta.com/pantheon-alternative/), [Cloudways](https://kinsta.com/cloudways-alternative/), [GoDaddy](https://kinsta.com/godaddy-alternative/), [DreamHost](https://kinsta.com/dreamhost-alternative/), [A2 Hosting](https://kinsta.com/a2-hosting-alternative/), and tsoHost.

**Both types of migrations are now available in our migration form**. No more having to reach out to our support team when bulk migrating sites from another host. Simply fill out the information, schedule a time that works for you, and our migration team will start moving your sites over to Kinsta. 👏

Read more about [how free migrations work at Kinsta](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrating-to-kinsta/#request-a-free-basic-migration).

![MyKinsta basic migrations](https://kinsta.com/wp-content/uploads/2019/08/mykinsta-basic-migrations.png)

MyKinsta basic migrations

We’ve also added more logic into our migration form area so it’s easier to understand why a migration might not be available.

### Knowledge Base Articles in MyKinsta

As many of you know, we spend a lot of time producing content and documentation. We’ve now released the first phase of our knowledge base integration with MyKinsta.

This means that many of the tooltips now pull up a simplified version of our **knowledge base article right within the MyKinsta dashboard!**How cool is that? The aim here is to help save you time from bouncing around between the dashboard and our main site. Find what you need fast!

![Knowledge Base in MyKinsta](https://kinsta.com/wp-content/uploads/2019/08/knowledge-base-in-mykinsta.png)

Knowledge Base in MyKinsta

You can expect to see more improvements to this new feature.

### Edit Your Avatar Link

Want to change your avatar that shows up in the MyKinsta dashboard? This is actually automatically pulled from [Gravatar.com](https://en.gravatar.com/). Gravatar is a free service for site owners, developers, and users. It is run and supported by Automattic. We’ve now added a handy link so that you can go edit it on their website.

![MyKinsta Gravatar link](https://kinsta.com/wp-content/uploads/2019/08/mykinsta-gravatar-link.png)

MyKinsta Gravatar link

### MyKinsta Login Redirects Are Now Deep-Linked

MyKinsta just got a little smarter. 🧠 We now support deep links. What this means is that MyKinsta won’t forget where you wanted to go initially if you have to login first. This usually happens if no session exists or your current session has expired.

### Revamped UI for Payment Methods Page

We’ve completely rebuilt our “Payment Methods” screen.

You can now **see your Kinsta account balance**. This is the amount of credit available in your account. It will be applied to your next invoice. Account credits are created automatically when you downgrade your plan or when our team adds credits to your account.

You can also **see how many premium migration credits you have available**. One premium migration credit allows you to request one premium migration free of charge.

![New UI on payment methods page](https://kinsta.com/wp-content/uploads/2019/08/ui-payment-methods-mykinsta-dashboard.png)

New UI on payment methods page

A few other updates that relate to payments we’ve pushed out include:

- Better messaging and workflow for card payment failures.
- Updates to invoices.
- The “Billing” menu item in MyKinsta will have a red dot notification next to if you have an overdue invoice.
- Yearly to yearly upgrades (e.g. Single 35k yearly to Single 125k yearly) are now charged automatically and prorated.

We are already busy working on new features for our next update! As always, if you have any feedback (positive or negative), we would love to hear it!
