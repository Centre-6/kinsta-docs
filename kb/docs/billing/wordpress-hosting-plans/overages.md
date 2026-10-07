---
url: "https://kinsta.com/docs/billing/wordpress-hosting-plans/overages/"
title: "Overages"
tier: "docs"
product: "billing"
product_label: "Billing"
subsection: "wordpress-hosting-plans"
section: ["Billing", "WordPress Hosting Plans"]
kinsta_last_updated: "2026-03-09T10:55:16"
change_signal: "2026-03-09T10:55:16"
fetched_at: "2026-10-07T22:58:19Z"
sha256: "729d6031e2d9d42f57e48aac3b55579ec5c758affad3d560093144ba6be77c2a"
body_chars: 9322
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Overages

**Section:** Billing > WordPress Hosting Plans
**Product:** Billing
**Source:** https://kinsta.com/docs/billing/wordpress-hosting-plans/overages/
**Kinsta last updated:** 2026-03-09T10:55:16

## On this page

- [Plan limit alerts](#plan-limit-alerts)
- [Visits overage](#visits-overage)
  - [Upgrades are not applied retroactively](#upgrades-are-not-applied-retroactively)
- [Server bandwidth overage](#server-bandwidth-overage)
- [Disk space overage](#disk-space-overage)
  - [Sample disk overage calculation](#sample-disk-overage-calculation)
  - [Check total disk space usage](#check-total-disk-space-usage)
- [CDN bandwidth overage](#cdn-bandwidth-overage)
- [Extreme overages](#extreme-overages)

---

Each Kinsta WordPress Hosting plan includes a set number of monthly visits or server bandwidth, SSD disk space, and CDN bandwidth. If you exceed your plan’s limit, you may incur overage charges. If plan limit alerts are enabled, you’ll receive an email when you reach 80% and 100% of your plan’s usage. For visits overages, you’ll also receive an email when you go over your plan’s usage by 10%.

If you regularly exceed your plan’s limit, you may want to consider upgrading or changing your plan. You can either select a plan with a higher visit allowance or switch to bandwidth-based pricing, which is calculated on your site’s data traffic. We also offer a [disk space add-on](https://kinsta.com/docs/wordpress-hosting/wordpress-add-ons/#disk-space-add-on) so you can increase the storage space of your hosting plan without upgrading.

## Plan limit alerts

[Plan limit alerts](https://kinsta.com/docs/user-settings/notifications) are enabled by default on all accounts, but you can enable/disable them by visiting [User Settings](https://my.kinsta.com/profile).

In [MyKinsta](https://my.kinsta.com/), click on your username in the top right corner and select **User Settings** in the menu that appears.

![MyKinsta user settings.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-user-settings.png)

MyKinsta user settings.

Click **Notifications** in the left navigation. In the **Plan limit alerts** section, toggle the alerts on or off.

![Enable or disable plan limit alerts.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-notifications-plan-limit-alerts.png)

Enable or disable plan limit alerts.

Below, we’ll explore the different types of overages at Kinsta. The **Plan usage** chart can be found on the **Dashboard** page in MyKinsta.

## Visits overage

If you choose a Kinsta Managed WordPress Hosting plan where pricing is based on visits, it will be determined by the **total number of monthly visits to your sites**. The number of visits in a given month is the sum of the unique IP addresses seen within a 24-hour period as recorded in the logs. These visits are shared across your WordPress Hosting plan. We use this data to approximate your plan usage.

![Monthly visits highlighted in the Plan usage chart.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-plan-usage-visits.png)

Monthly visits highlighted in the Plan usage chart.

If you hit your plan’s visitor cap, we’ll keep your sites running but charge you an overage fee ($0.50/1,000 visits) after a specific number of visitors. Don’t worry; we’ll send you a notification at 80% and 100% usage, and when you go over your plan’s usage by 10%. Learn more about [how Kinsta counts visitors](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/counting-visits/).

### Upgrades are not applied retroactively

When you upgrade plans, your new plan is only in force going forward from the moment you make the change. The new upgraded plan is not applied retroactively.

For example, let’s say you register for the Single 35k visits plan ($35 per month / basically $1.17 per day / allows 35k visits). Over the next 30 days, you get 100,000 visits, which results in an overage of 65k visits. On the 30th day, you upgrade to the Single 125k visits plan. We would credit you $1.17 for the remainder of the Single 35k visits plan and charge you $3 for one day on the Single 125k visits plan. So, before considering any overage, the total cost would have been $36.93 ($33.93 for 29 days on the Single 35k visits plan, $3 for one day on the Single 125k visits plan). You would then still be responsible for the one-time overage of 65k visits, which comes out to $32.50 ($0.50 / 1,000 visits).

## Server bandwidth overage

If you choose a Kinsta WordPress Hosting plan where pricing is based on bandwidth, it will be determined by the **total monthly server bandwidth used by your sites**. We allow you to exceed that limitation by paying $0.50/GB. We’ll send you a notification at 80% and 100% usage. Learn more about [how Kinsta calculates server bandwidth](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/wordpress-calculating-bandwidth/). The overage fee (if there is any) will be charged at the end of each month. If you continuously go over month after month, then we’ll reach out and ask you to upgrade your plan. You can easily see your plan usage in [MyKinsta](https://my.kinsta.com/).

As you approach your monthly limit, it will change accordingly.

![Server bandwidth highlighted in Plan usage chart.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-plan-usage-bandwidth.png)

Server bandwidth highlighted in Plan usage chart.

If you exceed your current plan’s server bandwidth by over 250 GB and haven’t upgraded your plan, you will automatically be charged at the end of the first week following the overage. If a 2nd billing attempt fails, we reserve the right to suspend your account until the issue is resolved.

## Disk space overage

Kinsta’s hosting plans come with a specified amount of SSD disk space. If you exceed your plan’s disk space allocation, we charge a modest overage fee. Disk space usage is monitored daily, and any overage charges are calculated on a daily basis, prorated at a rate of **$2 per GB per month**. Overages are only accrued when disk space usage exceeds the plan limit.

Some sites contain many large files, and we want you to have as much flexibility as possible at Kinsta. With our [disk space add-on](https://kinsta.com/docs/wordpress-hosting/wordpress-add-ons/#disk-space-add-on), you can **increase the storage space of your hosting plan** with a few clicks.

### Sample disk overage calculation

If you have 5 GB of disk space overage in a 31-day month, the daily overage calculation would be as follows:

($2 overage rate/31 days) x 5 GB = $0.32/day

In reality, the exact overage in terms of gigabytes will fluctuate daily on a production site, so the exact overage amount will vary slightly from day to day.

You can monitor your disk space usage on your MyKinsta Dashboard. We’ll also send you notifications when your usage reaches 80% and 100%. To avoid overage charges, you can upgrade to a larger plan or purchase our new disk space add-on. You can find and activate it on the same page where you see your plan.

![Disk space highlighted in Plan usage chart.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-plan-usage-disk.png)

Disk space highlighted in Plan usage chart.

### Check total disk space usage

You can quickly check your total disk space usage on the **Plan usage** chart on the **Dashboard** in [MyKinsta](https://my.kinsta.com/login/). To find out which files might be taking up the most space? Check out our blog post on [additional ways to check your disk usage](https://kinsta.com/blog/disk-usage-wordpress/).

![Total disk space usage in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-dashboard-disk-usage.png)

Total disk space usage in MyKinsta.

When you see the “[Upload: Failed to Write File to Disk](https://kinsta.com/blog/wordpress-failed-to-write-file-to-disk/)” error in WordPress, it’s possible that you have used all of your available disk space. If that’s the case, you can remove any unused files from your site, [upgrade your hosting plan](https://kinsta.com/docs/billing/wordpress-hosting-plans/#switch-your-plan), or add a [Disk Space Add-on](https://kinsta.com/docs/wordpress-hosting/wordpress-add-ons/#disk-space-add-on) to your current MyKinsta plan.

## CDN bandwidth overage

Each of our hosting plans comes with a generous amount of free CDN bandwidth for both new and current clients. If you hit your CDN bandwidth limit, we’ll keep your sites running, but we’ll charge you a fee after each additional GB ($0.05 / GB). You can increase your CDN bandwidth by upgrading to a higher hosting plan.

For Single 1.25M visit plans and above, Single 750GB bandwidth plans and above, WP 60 plans and above, Lead plans, or custom plans, we can customize the CDN bandwidth limit for an extra fee. You will need to reach out to our Sales team, as bandwidth upgrades are evaluated on a case-by-case basis.

![CDN bandwidth usage highlighted in the Plan usage chart.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-plan-usage-cdn.png)

CDN bandwidth usage highlighted in the Plan usage chart.

## Extreme overages

Our normal policy is to address overages on your hosting plan’s renewal date. However, in the case of an extreme overage, we may need to take action on the overage prior to your hosting plan’s renewal date.

An **extreme overage** occurs when the amount of your overage is as large or larger than the cost of your hosting plan, or $500, whichever is less.

For example, if you are on our Single 35k visits plan ($35 / month), an extreme overage would be an overage of $35 or more. On our WP 80 plan ($1,050 / month), an extreme overage would be an overage of $500 or more.

When an extreme overage occurs, we may opt to resolve the overage sooner by requiring immediate payment of the overage or requiring that you upgrade to a suitable plan. In addition, in the case of an extreme overage, we reserve the right to temporarily limit access to the site or a resource hosted on our servers until the overage has been acceptably resolved.
