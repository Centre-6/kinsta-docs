---
url: "https://kinsta.com/changelog/wp_debug-tool/"
title: "New WP_DEBUG Tool, Search and Replace 2.0, and MyKinsta Improvements"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2024-08-23T14:40:14"
change_signal: "2024-08-23T14:40:14"
fetched_at: "2026-10-07T22:58:23Z"
sha256: "7348a41b4b92a7c702fc243519b3c84580a67072e213a78101f8bac84145df34"
body_chars: 7939
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# New WP_DEBUG Tool, Search and Replace 2.0, and MyKinsta Improvements

**Product:** Changelog
**Source:** https://kinsta.com/changelog/wp_debug-tool/
**Kinsta last updated:** 2024-08-23T14:40:14

## On this page

- [New WP_DEBUG Tool](#new-wp-debug-tool)
  - [How to Enable the WP_DEBUG Tool](#how-to-enable-the-wp-debug-tool)
- [Redesigned Search and Replace Tool](#redesigned-search-and-replace-tool)
- [CDN Indicator on Sites List](#cdn-indicator-on-sites-list)
- [Join the Kinsta Research Program](#join-the-kinsta-research-program)
- [Updated Backup Restoration Workflow](#updated-backup-restoration-workflow)
- [Miscellaneous Improvements and Changes](#miscellaneous-improvements-and-changes)
  - [Kinsta DNS and “@”](#kinsta-dns-and)
  - [Reorganizing SFTP/SSH and Database Access](#reorganizing-sftpssh-and-database-access)
  - [Name Changes](#name-changes)

---

The holidays are quickly approaching, but our teams are still busy at work. We have a lot of new features and updates coming out before the end of the year that you’re not going to want to miss.

Today we are excited to release our new [**WP_DEBUG tool**](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/wordpress-debugging/#enable-wp-debug). This tool lets you easily see warnings, errors, and notices on your WordPress site. It’s **already available in the MyKinsta dashboard**. **🙌**

We also have a few other updates and improvements to our MyKinsta dashboard which we’ll dive into below. Many come directly from your own requests! So thank you, and keep the feedback coming. We mean it. We want to know your struggles and pain points so that we can help fix them.

## New WP_DEBUG Tool

Many of you do a lot of troubleshooting and debugging in your daily workflows, especially those of you working with clients or writing custom code.

Typically whenever you’re trying to investigate an error or warning in WordPress, one of the first things thing to do is to enable [WP_DEBUG](https://wordpress.org/support/article/debugging-in-wordpress/). This is a PHP constant (a permanent global variable) that can be used to trigger the debug mode throughout your site.

Whether it’s an out of date plugin or PHP function causing problems, you simply need more data to determine what’s going on. This usually requires connecting to your site via SFTP, and dropping a line of code into your `wp-config.php` file. However, this isn’t very convenient. Many of you just need to see the warning or error and where it’s happening to quickly fix it.

Our new WP_DEBUG tool makes that a little easier!

### How to Enable the WP_DEBUG Tool

Log in to MyKinsta and click into “Tools” under your WordPress site. You will now see a new tool called “WordPress debugging.” Simply click “Enable.”

![WP_Debug tool](https://kinsta.com/wp-content/uploads/2019/11/wp_debug-tool-mykinsta.png)

WP_DEBUG tool

And that’s it! Behind the scenes, our platform is setting the WP_DEBUG constant to `true` in your `wp-config.php` file. You will then be able to see warnings, errors, and notices on your WordPress site (both on the frontend and the WordPress admin dashboard).

An example would be like the one below. It’s a notice complaining about an undefined property. With WP_DEBUG turned off you would never see this message.

![WP_DEBUG example of error on WordPress site](https://kinsta.com/wp-content/uploads/2019/11/wp_debug-error-on-wordpress-site.png)

WP_DEBUG example of error on WordPress site

Don’t forget to turn off debugging when you’re all done!

## Redesigned Search and Replace Tool

We’ve redesigned our [Search and Replace tool](https://kinsta.com/blog/wordpress-search-and-replace/) in MyKinsta so that it’s easier to use. This has become a very popular tool and many are doing replacements on a regular basis. The whole idea is that you no longer have to bother installing a plugin or going to phpmyadmin to perform what in most cases should be a simple and quick task.

Previously the tool was found at the bottom of the tools page. We’ve now given the Search and Replace tool it’s own section as we’ll keep adding improvements to it as we move forward.

![Search and Replace tool](https://kinsta.com/wp-content/uploads/2019/11/search-and-replace-tool.png)

Search and Replace tool

The UI for the tool has been redesigned and is much easier to use, especially for those that aren’t used to regularly doing these types of operations. Our platform will automatically take a backup before doing the replacement in your database and you can have it automatically clear your site cache.

![New Search and Replace tool](https://kinsta.com/wp-content/uploads/2019/11/search-and-replace-tool-new-1.png)

New Search and Replace tool

## CDN Indicator on Sites List

While it’s a minor change, it’s one that we got a lot of feedback about. We’ve added a new CDN indicator on the Sites list page. You can now easily see if you have the [Kinsta CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#kinstas-cdn) enabled on a site without having to dig down into the CDN page.

![CDN indicator on sites list](https://kinsta.com/wp-content/uploads/2019/11/cdn-enabled-indicator-mykinsta-1.png)

CDN indicator on sites list

## Join the Kinsta Research Program

It would be awesome if we could ask a few questions or show you some new features before they go live so that we can hear your first impressions and collect feedback. This way, you can have a real impact on how certain features might look or work in MyKinsta.

Want to join [Kinsta’s Research Program](https://kinsta.com/docs/service-information/kinsta-research-program/)?

If you are a Kinsta customer, you can enable or disable research invitations from your **User Settings** in MyKinsta. To find the toggle for this setting, click on your user icon in the upper-right corner of MyKinsta, then click **User Settings**.

On the **User Settings** page, click on **Notifications** in the left side menu and scroll down. Enable the toggle in the **Research invitations** section to be contacted about upcoming research opportunities. If you decide you no longer want to receive invitations in the future, disable the same toggle.

![](https://kinsta.com/wp-content/uploads/2019/11/mykinsta-research-invitations-enabled_720.png)

## Updated Backup Restoration Workflow

Backups are very important to us at Kinsta. In fact, we offer [6 different types of backups](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/#wordpress-backups). This includes automatic backups, manual backups, system-generated backups, downloadable backups, hourly backups, and more.

We’ve updated and improved our backup restoration workflow screens to include additional information. This way you’ll know exactly what is going to happen before restoring a backup to live or staging.

![Backup restoration workflow](https://kinsta.com/wp-content/uploads/2019/11/backup-restoration-workflow.png)

Backup restoration workflow

## Miscellaneous Improvements and Changes

Below are a few additional improvements and changes we’ve made over the past couple of weeks.

### Kinsta DNS and “@”

If you’re using [Kinsta DNS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/), you’ll be happy to know we’ve made a small change in how we treat the “@” symbol in regards to our DNS records. Typically most providers associate the “@” with the domain itself, so we have followed suit.

You can now leave the “@” symbol as the value, which will designate the domain. In the example below, leaving “@” would simply mean `asdf.com` is pointing to `123.23.123.1`.

![Kinsta DNS example](https://kinsta.com/wp-content/uploads/2019/11/kinsta-dns-example.png)

Kinsta DNS example

### Reorganizing SFTP/SSH and Database Access

Previously there were three sections under the Info page regarding your connections:

- SFTP/SSH
- SSH Connections
- Database Access

We discovered that this was more confusing than it was helpful since the credentials for SFTP/SSH are the same. Therefore, we’ve combined these down into two simple sections.

- SFTP/SSH
- Database access

![MyKinsta SFTP/SSH and database](https://kinsta.com/wp-content/uploads/2019/11/mykinsta-sftp-ssh-database.png)

MyKinsta SFTP/SSH and database

### Name Changes

- “IPv4 Address” is now referred to as “[Site IP address](https://kinsta.com/docs/wordpress-hosting/site-management/ip-addresses/#site-ip-address-ipv-4).” This is simply easier for everyone to understand.
- What was previously “Billing” on the left-hand side navigation is now “Company.” Everything underneath this navigation item remains unchanged.

We hope all of these changes will help improve your daily workflow using MyKinsta. As always, please let us know if you have any suggestions or feedback. Stay tuned for the next feature update. 🤟
