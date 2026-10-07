---
url: "https://kinsta.com/changelog/automatic-updates-messaging/"
title: "Improved messaging for Kinsta Automatic Updates"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2025-09-04T14:04:25"
change_signal: "2025-09-04T14:04:25"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "77639e7b660eae6a96b14558206a84b800769a628a0b786a5ca0cae52656a5a6"
body_chars: 2750
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Improved messaging for Kinsta Automatic Updates

**Product:** Changelog
**Source:** https://kinsta.com/changelog/automatic-updates-messaging/
**Kinsta last updated:** 2025-09-04T14:04:25

## On this page

- [New weekly automatic update digests](#new-weekly-automatic-update-digests)
- [Detecting repeated failure of theme and plugin updates](#detecting-repeated-failure-of-theme-and-plugin-updates)
- [Making WordPress management easy](#making-wordpress-management-easy)

---

We’ve added a new option for users of the [Kinsta Automatic Updates](https://kinsta.com/blog/kinsta-automatic-updates/) add-on to manage the alerts they receive when that service works to upgrade plugins and themes on their WordPress sites.

In addition, we are now dialing back on attempts to upgrade individual plugins and themes that repeatedly fail automatic update visual regression testing.

It’s all part of our efforts to help you keep your WordPress sites up and running with minimum fuss, no matter how many you manage.

## New weekly automatic update digests

You can now choose to get email notifications about plugin and theme updates in a single recap every Friday.

To enable weekly messages and control what kind of alerts you need to see, start by clicking on your own name in the upper right corner of the [MyKinsta dashboard](https://kinsta.com/mykinsta/) to reach **User settings** on the dropdown menu. Next, select **Notifications** in the left navigation and scroll down to the **Kinsta Automatic Updates** section:

![A screenshot showing the dialog for managing alerts from Kinsta Automatic Updates.](https://kinsta.com/wp-content/uploads/2025/09/kinsta-automatic-updates-weekly-digest.png)

Enabling a weekly digest for Kinsta Automatic Updates.

Using the controls shown above, you can enable the weekly update option and still choose to be notified immediately of failed or successful updates.

## Detecting repeated failure of theme and plugin updates

As users of Kinsta Automatic Updates know, after an update attempt, the add-on can visually compare before and after images of a site’s homepage and four randomly selected pages (or specific pages you choose) in an effort to detect failure.

If a plugin or theme update fails three times, the add-on will begin a regimen of increasing delays for future attempts, giving you time to [troubleshoot the problem](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-plugins-themes-automatic-updates/#troubleshooting-screenshot-differences).

The update schedule after those repeated failures looks like this:

- Fourth attempt: retry after one day
- Fifth attempt: after two days
- Sixth attempt: after four days
- Seventh attempt: after eight days
- Eighth attempt: after 16 days
- Then every 30 days until the update succeeds

## Making WordPress management easy

We’re fanatical about making [WordPress maintenance](https://kinsta.com/blog/wordpress-maintenance/) simpler for our customers.

If you’re not already one of our customers and are looking for lightning-fast, [secure](https://kinsta.com/wordpress-hosting/security/) WordPress hosting, explore [Kinsta’s plans](https://kinsta.com/pricing/) to find the one that fits your company best.
