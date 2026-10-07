---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-plugins-themes-faqs/"
title: "Plugins and Themes FAQs"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-plugins-themes"
section: ["WordPress Hosting", "Plugins and Themes"]
kinsta_last_updated: "2025-03-12T10:58:55"
change_signal: "2025-03-12T10:58:55"
fetched_at: "2026-10-07T22:58:17Z"
sha256: "ee41cdc121ba1d065f229f363b2d5379e12269999aad677061db3a39845a47dc"
body_chars: 2397
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Plugins and Themes FAQs

**Section:** WordPress Hosting > Plugins and Themes
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-plugins-themes-faqs/
**Kinsta last updated:** 2025-03-12T10:58:55

## On this page

- [Can I update plugins and themes on multiple sites at the same time?](#can-i-update-plugins-and-themes-on-multiple-sites-at-the-same-time)
- [Can I choose which version of a plugin or theme to update to?](#can-i-choose-which-version-of-a-plugin-or-theme-to-update-to)
- [Can I downgrade a plugin or theme?](#can-i-downgrade-a-plugin-or-theme)
- [What if there’s an issue with an update? Can I undo the change?](#what-if-theres-an-issue-with-an-update-can-i-undo-the-change)
- [Can I still manage my plugins and themes in my WordPress dashboard?](#can-i-still-manage-my-plugins-and-themes-in-my-wordpress-dashboard)
- [Can I manage my plugins and themes for any site?](#can-i-manage-my-plugins-and-themes-for-any-site)

---

Below, we’ve compiled all the **most common plugin and theme questions** in one place. If you have any other questions we’ve perhaps missed, make sure to feedback using the options at the bottom of the article, or you can always [open a chat with our Support team](https://kinsta.com/docs/support/contact-support/).

## Can I update plugins and themes on multiple sites at the same time?

Yes, you can [update plugins and themes](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-manage-plugins-themes/) for multiple sites, including staging sites, simultaneously from the **WordPress Sites** page.

## Can I choose which version of a plugin or theme to update to?

No, you can only update to the latest version of a plugin or theme.

## Can I downgrade a plugin or theme?

No, you can only update to the latest version of a plugin or theme. You cannot go back to a previous version.

## What if there’s an issue with an update? Can I undo the change?

While there isn’t a built-in way to undo an update, we take a backup of the environment just before the update, which you can restore. **Note:** Backups created before a plugin or theme update are only available for two hours.

[Kinsta Automatic Updates](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-plugins-themes-automatic-updates/) performs a visual regression test on your site to detect any significant changes before and after updates. If an issue is identified, Kinsta automatically restores a backup taken prior to the update, ensuring your site remains stable and secure. These backups are available for three days.

## Can I still manage my plugins and themes in my WordPress dashboard?

Yes, you can continue to handle plugins and themes through WordPress.

## Can I manage my plugins and themes for any site?

Not quite. While the feature will work just fine on most sites, there are some situations that will prevent this feature from working:

- Issues that prevent us from running [WP-CLI](https://kinsta.com/docs/devkinsta/wp-cli).
- Premium (payment required) and custom (built by you or your developer) plugins or themes may not have a publicly available update endpoint, so they cannot be updated from MyKinsta. In some cases, we may detect that a new version is available, but the update process fails due to not being available via the standard WordPress endpoint.
