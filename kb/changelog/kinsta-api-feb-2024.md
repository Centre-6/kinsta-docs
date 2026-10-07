---
url: "https://kinsta.com/changelog/kinsta-api-feb-2024/"
title: "New Kinsta API endpoints enhance WordPress site management"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-05-06T12:08:53"
change_signal: "2026-05-06T12:08:53"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "2c6f1cd336114cc11e006259da4d010d72895021a0e46c943e4f7baaa69ed30b"
body_chars: 9564
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# New Kinsta API endpoints enhance WordPress site management

**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-feb-2024/
**Kinsta last updated:** 2026-05-06T12:08:53

## On this page

- [What’s new in Kinsta API](#whats-new-in-kinsta-api)
  - [1. Managing WordPress site themes and plugins](#1-managing-wordpress-site-themes-and-plugins)
  - [2. Add and delete WordPress site domain(s)](#2-add-and-delete-wordpress-site-domains)
  - [3. Retrieve, add, restore, and remove backups in WordPress sites](#3-retrieve-add-restore-and-remove-backups-in-wordpress-sites)
  - [4. Retrieve site logs](#4-retrieve-site-logs)
- [Get started with Kinsta API today](#get-started-with-kinsta-api-today)

---

Agencies are always looking for ways to improve how they manage multiple sites.

Kinsta provides a [user-friendly dashboard](https://my.kinsta.com/) equipped with a comprehensive suite of tools designed to simplify site management. This includes access to [various tools](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/), [themes, and plugins](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/) alongside features like [analytics](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/), [CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/), [edge caching](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/), and [Kinsta APM](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/).

In our continuous effort to empower users, we launched the [Kinsta API](https://kinsta.com/changelog/kinsta-api/), opening up new avenues for agencies and users to manage their sites programmatically through a range of available endpoints.

## What’s new in Kinsta API

Since the introduction of the [Kinsta API](https://kinsta.com/docs/kinsta-api/), we’ve regularly added new endpoints — developments we’ve highlighted through changelogs and blog posts. To date, these endpoints have supported a wide range of tasks, including the ability to:

- [Retrieve, clone, create, and delete WordPress sites](https://api-docs.kinsta.com/pages/wordpress-sites/description)
- [Manage site environments](https://api-docs.kinsta.com/pages/wordpress-site-environments/description)
- Use tools for [clearing site cache](https://api-docs.kinsta.com/api-reference/wordpress-site-tools/clear-site-cache), [restarting the PHP engine](https://api-docs.kinsta.com/api-reference/wordpress-site-tools/restart-an-environments-php-engine), [modifying the PHP version of environments](https://api-docs.kinsta.com/api-reference/wordpress-site-tools/modify-an-environments-php-version), and [managing denied IP lists](https://api-docs.kinsta.com/api-reference/wordpress-site-tools/get-list-of-denied-ips)
- [Clear edge](https://api-docs.kinsta.com/pages/wordpress-edge-caching/description) and [site CDN caches](https://api-docs.kinsta.com/pages/wordpress-cdn/description)

However, we’re not stopping there. New endpoints are being added continuously to enhance your site management capabilities further. As Kristof Siket, our Development Team Lead for the Kinsta API, notes:

“User feedback drives the prioritization of feature exposure. If you believe a specific tool or endpoint should be included in the Kinsta API, feel free to send in your feedback.”

In this update, we’re excited to introduce the latest endpoints added to the Kinsta API, designed to enrich the WordPress site management experience. Let’s explore these new additions and how they can benefit your site management processes.

### 1. Managing WordPress site themes and plugins

[Themes](https://kinsta.com/blog/fastest-wordpress-theme/) and [plugins](https://kinsta.com/blog/wordpress-plugin/) are crucial components of the WordPress ecosystem, serving as the backbone for customizing and enhancing websites built on this platform.

Like WordPress, themes and plugins receive regular updates to add new features, patch a security hole, increase compatibility, and more. That’s why we included [Plugin and Theme Management](https://kinsta.com/changelog/plugin-and-theme-management/) among the tools available within MyKinsta for each of your sites.

Now, the new [site themes and plugins API endpoint](https://api-docs.kinsta.com/pages/wordpress-site-themes-plugins/description) can return a list of your site’s plugins and themes programmatically. You can also send a `PUT` request to update your plugins or themes individually or in bulk.

Agencies can develop custom tools using these endpoints to make the task of updating themes and plugins across all sites easier.

Imagine creating a tool that iterates through each site in your Kinsta company account, retrieves the themes and plugins, and then updates all outdated components in one fell swoop — without the need to log into each site individually. The potential for efficiency gains here is enormous.

Moreover, these endpoints can be integrated into bots — such as a Discord bot or Slackbot — to execute updates directly from another preferred workspace tool, adding a layer of convenience to your workflow.

### 2. Add and delete WordPress site domain(s)

A [domain](https://kinsta.com/blog/how-to-buy-a-domain-name/) is a unique, easy-to-remember address used to access websites. The MyKinsta dashboard makes it easy to [add, remove, and configure domains in your sites](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/).

With the API’s newly added [site domains endpoint](https://api-docs.kinsta.com/pages/wordpress-site-domains/description), you can now [add a domain to your WordPress site](https://api-docs.kinsta.com/api-reference/wordpress-site-domains/add-new-site-domain) programmatically using the site’s environment ID with the option of passing a custom SSL key and certificate.

You can also [delete domains](https://api-docs.kinsta.com/api-reference/wordpress-site-domains/delete-one-or-more-site-domains) by specifying their IDs, which you can access programmatically from the [details of your site environments](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-site-environments).

As an agency, you can make this process suit your taste by leveraging a custom dashboard or workspace environment to perform operations like this.

Kristof also noted the potential benefits of integrating DNS management into these endpoints. While this feature is not yet available, it’s a development goal we’re actively working towards

### 3. Retrieve, add, restore, and remove backups in WordPress sites

[Backups](https://kinsta.com/blog/backup-wordpress-site/) offer website owners a safety net in case of mishaps. Users of Kinsta’s [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/) service benefit from [six types of backups](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/): automatic daily, optional hourly, manual, system-generated, downloadable, and external backups sent automatically to your Amazon S3 or Google Cloud Storage.

Managing these backups is a breeze in the [MyKinsta](https://my.kinsta.com/) dashboard. And now the Kinsta API opens the door for **your approach** to working with WordPress sites and their backups. With the backups endpoint, you can manage every action around backups programmatically, such as:

- [List manual, scheduled, and system-generated backups](https://api-docs.kinsta.com/api-reference/backups/get-manual-schedule-and-system-generated-backups)
- [List downloadable backups](https://api-docs.kinsta.com/api-reference/backups/get-downloadable-backups)
- [Restore a scheduled, manual, or system-generated backup](https://api-docs.kinsta.com/api-reference/backups/restore-a-scheduled-or-manual-or-system-generated-backup-to-an-environment)
- [Create a manual backup for a specific environment](https://api-docs.kinsta.com/api-reference/backups/add-a-manual-backup-to-an-environment)
- [Remove a WordPress site environment backup](https://api-docs.kinsta.com/api-reference/backups/remove-a-wp-site-environment-backup)

This functionality is particularly beneficial for agencies, enabling the integration of these [backup management capabilities with tools like Slack](https://kinsta.com/blog/wordpress-backups-api/). This means tasks like restoring or downloading backups can be executed programmatically through familiar tools without the need to navigate the dashboard for each site.

### 4. Retrieve site logs

Logs are very helpful for troubleshooting and debugging issues on your WordPress sites. At Kinsta, you can access [three types of logs](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/): error logs, kinsta-cache-perf (cache performance) logs, and access logs.

Accessing logs through the MyKinsta dashboard is straightforward: navigate to **WordPress Sites**, select the desired site, and click the **Logs** tab to open the **Log viewer** page.

Now, the Kinsta API lets you access these logs programmatically by specifying your site’s environment ID, the log file you need, and the number of log lines you want to retrieve.

This feature is particularly beneficial for agencies and larger teams, enabling the development of custom interfaces for log access. For instance, teams can [leverage Slack to create a custom Slackbot](https://kinsta.com/blog/api-server-logs/), making log retrieval as simple as executing a slash command like:

```
/get_site_logs [environment_ID] [log_file] [lines]
```

## Get started with Kinsta API today

There is a lot that can be done with the Kinsta API. Feel free to check out the following to understand what’s possible with the API, how to get started, and the various permission levels and limits of the API:

- [Kinsta API Documentation](https://kinsta.com/docs/kinsta-api/)
- [Changelog — Introducing Kinsta API: The Power of Automation for Site Management](https://kinsta.com/changelog/kinsta-api/)
- [Changelog — Introducing New Kinsta API Endpoints: Environment CRUD, Edge Caching, Application Deployment](https://kinsta.com/changelog/kinsta-api-aug-2023/)
- [Changelog — New Kinsta API Endpoints: Clear CDN Cache and Push Environment](https://kinsta.com/changelog/kinsta-api-sept-2023/)

Embrace the opportunities our API offers to automate your site management experience.
