---
url: "https://kinsta.com/docs/devkinsta/devkinsta-reference/faq/"
title: "Reference - FAQs"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-reference"
section: []
kinsta_last_updated: "August 19, 2024"
sitemap_lastmod: "2024-08-19T12:45:05+00:00"
fetched_at: "2026-10-07T22:38:20Z"
sha256: "3250c6930c9278fe301c2c0dd3cc5420d0ef57e9fc9ecfda414966371ce83ace"
body_chars: 7023
extracted_with: "main article"
status: "live"
---

# Reference - FAQs

**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-reference/faq/
**Kinsta last updated:** August 19, 2024

## On this page

- [Why should I use DevKinsta?](#why-should-i-use-devkinsta)
- [What operating systems does DevKinsta support? What are the minimum system requirements to run DevKinsta?](#what-operating-systems-does-devkinsta-support-what-are-the-minimum-system-requirements-to-run-devkinsta)
  - [Windows](#windows)
  - [Mac](#mac)
  - [Linux](#linux)
- [Where can I download DevKinsta?](#where-can-i-download-devkinsta)
- [How do I install DevKinsta?](#how-do-i-install-devkinsta)
- [Where can I ask for help?](#where-can-i-ask-for-help)
- [Where do I report bugs?](#where-do-i-report-bugs)
- [Where can I make a feature request?](#where-can-i-make-a-feature-request)
- [Can I publish or download my live site using DevKinsta?](#can-i-publish-or-download-my-live-site-using-devkinsta)
- [Can I use DevKinsta for non-WordPress sites?](#can-i-use-devkinsta-for-non-wordpress-sites)
- [How do I update DevKinsta?](#how-do-i-update-devkinsta)
- [How do I use the email features within DevKinsta?](#how-do-i-use-the-email-features-within-devkinsta)
- [How do I access the database?](#how-do-i-access-the-database)
- [What should I do if I get an error when launching DevKinsta?](#what-should-i-do-if-i-get-an-error-when-launching-devkinsta)
- [Why can’t I change some fields in the DevKinsta UI?](#why-cant-i-change-some-fields-in-the-devkinsta-ui)
- [How do I access phpMyAdmin?](#how-do-i-access-phpmyadmin)
- [Can I use third-party database tools like Sequel Pro or TablePlus?](#can-i-use-third-party-database-tools-like-sequel-pro-or-tableplus)

---

This page addresses some common questions you may have while using DevKinsta.

## Why should I use DevKinsta?

DevKinsta makes it easy to develop WordPress sites locally and push the site directly to Kinsta’s servers. You can also download an existing website hosted on Kinsta to your local environment.

## What operating systems does DevKinsta support? What are the minimum system requirements to run DevKinsta?

For detailed instructions, refer to [DevKinsta Installation](https://kinsta.com/docs/devkinsta/devkinsta-getting-started/installation/) or the [Docker Desktop documentation](https://docs.docker.com/desktop/). DevKinsta is available for the following operating systems:

### Windows

- Windows 10 64-bit: Pro, Enterprise, or Education (Build 16299 or later)
- Windows 10 Home (version 1903 or higher)

For more information, see the [requirements and installation instructions for Windows](https://kinsta.com/docs/devkinsta/devkinsta-getting-started/installation/#windows).

### Mac

- **macOS 10.14 or newer.** We recommend using the latest version of macOS.
- Mac hardware must be a 2010 or a newer model, with either:
  - Intel’s hardware support for memory management unit (MMU) virtualization, including Extended Page Tables (EPT) and Unrestricted Mode.
  - Or Apple silicon’s Virtualization Extensions.

For more information, see the [requirements and installation instructions for Mac](https://kinsta.com/docs/devkinsta/devkinsta-getting-started/installation/#mac).

### Linux

- Ubuntu 20.04 LTS (or later)

For more information, see the [requirements and installation instructions for Linux](https://kinsta.com/docs/devkinsta/devkinsta-getting-started/installation/#linux).

Officially, DevKinsta is only supported for Ubuntu. You’re free to try it on any other Debian-based distro, but they’re not supported officially as of yet.

## Where can I download DevKinsta?

Visit the [DevKinsta Download](https://kinsta.com/devkinsta/download/) page and click the download button for your operating system and hardware.

## How do I install DevKinsta?

See our guide for instructions on [how to install DevKinsta on Windows, macOS, or Linux](https://kinsta.com/docs/devkinsta/devkinsta-getting-started/installation/). Alternatively, you can [watch our video](https://kinsta.com/webinars/install-and-use-devkinsta/) to learn how to install and use DevKinsta.

## Where can I ask for help?

Support for DevKinsta is handled on our [community forum](https://community.kinsta.com/c/devkinsta/), where you can ask for help or search through existing discussions.

Traditional live chat support is not provided for DevKinsta. However, if you are experiencing an issue with a site that has been uploaded to MyKinsta or an existing site on our platform, please [reach out to our Support team via MyKinsta for assistance](https://kinsta.com/docs/support/contact-support/).

## Where do I report bugs?

[Bug reports](https://community.kinsta.com/c/devkinsta/bug-reports/) are tracked and submitted through our community forum. We’ll get back to you as soon as possible on the bug report.

## Where can I make a feature request?

Feature requests can be made through our [community forum](https://community.kinsta.com/c/devkinsta/feature-requests). If it is implemented, we will update the thread. While we can’t guarantee when or if a feature will be implemented, we take user requests very seriously and use them to prioritize which features we implement next. Thanks for helping us improve DevKinsta!

## Can I publish or download my live site using DevKinsta?

When pushing changes from DevKinsta to MyKinsta, you can only push to a Standard or Premium Staging Environment; you can’t push to a live site directly from DevKinsta. Learn more about [how to import a site](https://kinsta.com/docs/devkinsta/devkinsta-getting-started/creating-a-site/#import-from-mykinsta) from MyKinsta and how to [publish a site](https://kinsta.com/docs/devkinsta/devkinsta-integration/#push-changes-to-staging) in our documentation.

## Can I use DevKinsta for non-WordPress sites?

At this time, DevKinsta only supports WordPress. If you have any requests for other platforms, please submit them as a feature request.

## How do I update DevKinsta?

DevKinsta will automatically update. You can configure auto-updates by going to **Settings** in DevKinsta. If **Download new updates automatically** deselected, you can click **Check Now** and install any available update.

## How do I use the email features within DevKinsta?

We’ve implemented a local email application called MailHog within DevKinsta so you can test if emails are sent from the site. Emails will not be sent externally and will only appear within DevKinsta. [More information on how to use MailHog can be found here](https://kinsta.com/docs/devkinsta/devkinsta-site-management/email-inbox/).

## How do I access the database?

You can view the database by accessing Adminer for each site. Adminer is a user interface for managing your database. It is very similar to phpMyAdmin, but has a reduced footprint and is snappier to work with. [More information on how to use Adminer can be found here](https://kinsta.com/docs/devkinsta/devkinsta-database/database-manager/).

## What should I do if I get an error when launching DevKinsta?

In macOS, when you first launch DevKinsta, you may see an error that reads:

> DevKinsta can’t be opened because Apple cannot check it for malicious software.

This is due to strict permissions on macOS and can be resolved by adding an exception for DevKinsta in your security settings. Check out this [macOS user guide](https://support.apple.com/guide/mac-help/apple-cant-check-app-for-malicious-software-mchleab3a043/mac) for more information on how to resolve this error.

If you encounter a different error message, please let us know via the [DevKinsta Community Forum](https://community.devkinsta.com/).

## Why can’t I change some fields in the DevKinsta UI?

DevKinsta is in active development, and some fields reflect features and settings that we anticipate implementing in the future. At this time, the following fields can not be changed in DevKinsta.

- [Second-level domain](https://kinsta.com/blog/what-is-a-tld/#what-is-a-tld-explained-in-more-detail) (the part of your site’s domain before .local)
- Web Server type
- Database type

## How do I access phpMyAdmin?

DevKinsta uses Adminer instead of phpMyAdmin. Adminer is a lightweight alternative to phpMyAdmin that includes all of the necessary features for local WordPress development. To learn all about Adminer, take a look at our [Adminer documentation](https://kinsta.com/docs/devkinsta/devkinsta-database/database-manager/).

## Can I use third-party database tools like Sequel Pro or TablePlus?

Yes, third-party database management tools are supported. To learn more about how to connect third-party database tools to DevKinsta sites, check out our [database tools documentation](https://kinsta.com/docs/devkinsta/devkinsta-database/database-tools/).
