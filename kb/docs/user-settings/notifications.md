---
url: "https://kinsta.com/docs/user-settings/notifications/"
title: "Notifications"
tier: "docs"
product: "user-settings"
product_label: "MyKinsta User Settings"
subsection: "notifications"
section: ["User Settings"]
kinsta_last_updated: "2026-04-27T10:02:14"
change_signal: "2026-04-27T10:02:14"
fetched_at: "2026-10-07T22:58:20Z"
sha256: "e24f8d65ee45fb3a83930cf57561c63582567d89580ee1c814cb643249518e9d"
body_chars: 8576
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Notifications

**Section:** User Settings
**Product:** MyKinsta User Settings
**Source:** https://kinsta.com/docs/user-settings/notifications/
**Kinsta last updated:** 2026-04-27T10:02:14

## On this page

- [View notifications](#view-notifications)
- [Enable or disable notifications](#enable-or-disable-notifications)
- [Notification types](#notification-types)
  - [Plan limit alerts](#plan-limit-alerts)
  - [Newsletter](#newsletter)
  - [Feature update newsletter](#feature-update-newsletter)
  - [Invoice in email](#invoice-in-email)
  - [Research invitations](#research-invitations)
  - [WordPress site monitoring](#wordpress-site-monitoring)
  - [Kinsta Automatic Updates](#kinsta-automatic-updates)
  - [Vulnerability notifications](#vulnerability-notifications)
  - [Monthly vulnerability digest](#monthly-vulnerability-digest)
- [Summary](#summary)

---

MyKinsta has several useful notification-related options to help make managing your account and services easier, such as plan limit alerts, newsletters, and invoices. You can also configure MyKinsta to send critical site monitoring alerts in response to errors on your site.

There are also mandatory system messages that include information about important changes or updates, for example, PHP deprecation notices. These notifications are delivered by email and cannot be opted out of; they are sent to Company Owners, Company Administrators, Company Developers, Site Developers, and Site Administrators.

## View notifications

You can view your notifications on the **Dashboard** or by clicking the **Notifications** icon.

![Notifications in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/04/wordpress-notifications.png)

Notifications in MyKinsta.

You can click on an individual notification to view more information and click **Ask Support** to initiate a chat with our support team about that notification.

![Notification details. ](https://kinsta.com/wp-content/uploads/2026/04/wordpress-notification-details.png)

Notification details.

## Enable or disable notifications

To enable or disable notifications:

1. Log in to [MyKinsta](https://kinsta.com/mykinsta/), click your username in the upper-right corner.
2. Select **User Settings** from the dropdown menu.
3. Toggle notifications on and off or subscribe and unsubscribe as needed for each notification type.

![Notification settings in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-user-settings-notifications.png)

Notification settings in MyKinsta.

## Notification types

### Plan limit alerts

All Kinsta [WordPress hosting plans](https://kinsta.com/pricing/) include a predetermined amount of resources. If you go over your limits, we have a few different types of [overages](https://kinsta.com/docs/billing/wordpress-hosting-plans/overages/) in place.

If you regularly exceed your plan’s limit, you may want to consider upgrading or changing your plan. You can either select a plan with a higher visit allowance or switch to bandwidth-based pricing, which is calculated on your site’s data traffic. You can [upgrade your plan in MyKinsta](https://kinsta.com/docs/billing/wordpress-hosting-plans/#switch-your-plan).

If you want to be alerted before a potential overage, we recommend enabling plan limit alerts in MyKinsta. When these alerts are enabled, we’ll send you a notification at 80% and 100% of your plan usage. For visits overages, you’ll also receive an email when you exceed your plan’s usage by 10%.

By default, plan limit alerts are enabled on all accounts. These alerts are available for the **Company Owner**, **Company Administrator**, and **Company Billing**  [user roles](https://kinsta.com/docs/company-settings/user-management/). If you would like to send plan limit alerts to someone who does not require site access, you can [invite them to your company](https://kinsta.com/docs/company-settings/user-management/#invite-a-user-to-your-company) in MyKinsta with the “Company Billing” role.

### Newsletter

Here, you can manage your subscription to our monthly [jam-packed WordPress newsletter](https://kinsta.com/wordpress-newsletter/), delivered to over 165,000 subscribers around the world. Our WordPress newsletter is perfect for bloggers, [WordPress agencies](https://kinsta.com/wordpress-hosting/agencies/), content marketers, and other enthusiasts who want to stay updated on the latest industry trends. To change the newsletter’s language, click **Change language** and select the required option.

### Feature update newsletter

This is where you can manage your subscription to our monthly updates about new feature releases, data centers, add-ons, and more useful information to get the most out of your hosting. To change the newsletter’s language, click **Change language** and select the required option.

### Invoice in email

PDF versions of your Kinsta invoices are always available in MyKinsta under **Company** > **Billing**. If you also want to receive PDF invoices via email, you can enable the **Invoice in Email** option. This option is only available for the Company Administrator, Company Billing, and Company Owner [MyKinsta user roles](https://kinsta.com/docs/company-settings/user-management/).

Company Administrator, Company Billing, and Company Owner roles can also add email addresses to send invoices to within the **Invoices** > [**Invoice in email**](https://kinsta.com/docs/billing/invoices/) option.

### Research invitations

When this notification is enabled, you’ll receive occasional invitations to participate in surveys, usability tests, interviews, and beta tests of new features in exchange for monetary rewards or swag. Being a part of the [Kinsta Research Program](https://kinsta.com/docs/service-information/kinsta-research-program/) means you’ll have an impact on how MyKinsta evolves over time!

### WordPress site monitoring

A modern WordPress site has many moving parts. Whether it’s DNS issues, [site downtime](https://kinsta.com/blog/wordpress-errors/#500-errors), SSL errors, or [domain name](https://kinsta.com/blog/choose-domain-name/) expiration notices, there are a lot of things to pay attention to!

Kinsta’s site monitoring feature for WordPress helps you out by notifying you when your site needs critical attention.

When site monitoring is enabled, we check your site every 3 minutes. If one of the errors below is detected on your WordPress site, we’ll send you an email alert:

- **Site Errors** – We utilize a custom-built tool for monitoring our infrastructure. If we detect errors or issues on your site, we’ll send you an email notification to let you know.
- **SSL Errors** – If there’s a configuration issue with your domain and the SSL certificate expires, we’ll notify you. If you’re using Kinsta’s free SSL certifications you’ll receive an email message and a notification in [MyKinsta](https://my.kinsta.com/) 30 days before your SSL expires. However, if you’re using a custom SSL certificate, we **do not** send expiration notifications. You should check with your SSL provider for expiration details.
- **Domain Expiration** – If we detect an expired domain assigned to your Kinsta site, we’ll send you an alert.
- **Domain Resolution** – If we detect that a domain cannot be resolved due to incorrect DNS configuration, misconfigured nameservers, or temporary DNS resolution failures, we’ll email you to let you know.

### Kinsta Automatic Updates

[Kinsta Automatic Updates](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-plugins-themes-automatic-updates/) installs daily updates for your plugins and themes for $3 per environment per month. If you enable Kinsta Automatic Updates, you can set up email notifications for weekly updates, successful updates, and failed updates.

### Vulnerability notifications

Select this option to receive email notifications when high-severity [vulnerabilities](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/#plugin-and-theme-vulnerabilities) (severity score of 7 or higher) are detected in your plugins or themes. These notifications focus only on high-severity issues, while the monthly vulnerability digest includes both high and lower-severity vulnerabilities.

WPScan provides vulnerability data. It maintains a comprehensive database of [plugin](https://wpscan.com/plugins/) and [theme](https://wpscan.com/themes/) security issues, including technical details and disclosure dates.

These notifications are available to Company Owners, Company Administrators, Company Developers, Site Administrators, and Site Developers.

### Monthly vulnerability digest

MyKinsta scans each plugin and theme daily to identify [security vulnerabilities](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/#plugin-and-theme-vulnerabilities). You can set up email notifications to receive a monthly summary of all vulnerable plugins and themes installed on your sites. WPScan provides vulnerability data. It maintains a comprehensive database of [plugin](https://wpscan.com/plugins/) and [theme](https://wpscan.com/themes/) security issues, including technical details and disclosure dates.

## Summary

At Kinsta, we try to make managing your account and services as stress-free as possible. With our various notification options, including overage and site monitoring alerts, you’ll be able to spend more time working on your business and less time checking up on your site.
