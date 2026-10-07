---
url: "https://kinsta.com/docs/wordpress-hosting/site-management/"
title: "Site Management"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "site-management"
section: ["WordPress Hosting"]
kinsta_last_updated: "2026-05-27T16:28:23"
change_signal: "2026-05-27T16:28:23"
fetched_at: "2026-10-07T22:58:21Z"
sha256: "2c93a86f2f01d9f01c0f4ac1e312f2b614d84ab530dad6193e5bba8768cf5da5"
body_chars: 17408
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Site Management

**Section:** WordPress Hosting
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/site-management/
**Kinsta last updated:** 2026-05-27T16:28:23

## On this page

- [Bulk actions](#bulk-actions)
- [Search and filter sites](#search-and-filter-sites)
- [Rename a site in MyKinsta](#rename-a-site-in-mykinsta)
- [Suspend a WordPress site](#suspend-a-wordpress-site)
- [Reset a WordPress site](#reset-a-wordpress-site)
- [Delete a WordPress site](#delete-a-wordpress-site)
- [Change your site’s path](#change-your-sites-path)
- [Export a list of WordPress sites](#export-a-list-of-wordpress-sites)
- [Max upload size for files](#max-upload-size-for-files)
  - [Max upload file size for WordPress](#max-upload-file-size-for-wordpress)
  - [Max upload file size for WordPress multisite](#max-upload-file-size-for-wordpress-multisite)
- [Move an existing site to a new location](#move-an-existing-site-to-a-new-location)

---

You can manage many aspects of your site in [MyKinsta](https://my.kinsta.com/), including [contacting our Support team](https://kinsta.com/docs/support/contact-support/) for assistance with tasks like moving a site to a new location or increasing the max upload file size.

## Bulk actions

To save you the time and effort of updating and changing sites individually, you can use bulk actions to perform multiple actions on multiple sites, including staging sites, simultaneously from the**Sites** list. Within the**Sites** list, select the required sites, click **Actions**, and choose from the following to update all selected sites simultaneously:

- **Caching:**
  - **Clear cache:** This allows you to clear the [server](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/#clear-cache-in-mykinsta), [CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#how-to-disable-or-purge-kinstas-cdn), and [Edge Cache](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/#clear-edge-cache).
  - **Change edge caching:** Use this option to enable or disable [Edge Caching](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/).
  - **Change CDN:**Use this option to enable or disable the [Kinsta CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/).
  - **Change Redis caching:** Use this option to enable or disable the [Redis caching](https://kinsta.com/docs/wordpress-hosting/caching/redis-cache/) add-on.
- **Bot protection:**
  - **Change bot protection level:** Change your [bot protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) level to control how different traffic types are blocked or challenged on your sites.
  - **Change AI crawler block:** Allow or [block all AI crawlers](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#block-ai-crawlers) from your sites, including verified crawlers.
  - **Change WordPress automation allowlist:** Allow or block [typical WordPress automations](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#allow-typical-wordpress-automations) from your sites.
- **Plugins and themes:**
  - **Update plugins:** This shows a list of [plugins](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-manage-plugins-themes/) with available updates so you can select which to update. Only plugins that have available updates are shown.
  - **Update themes:** This shows all of the [themes](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-manage-plugins-themes/) with available updates so you can select which to update. Only themes that have available updates are shown.
  - **Change automatic updates:** This allows you to enable or disable [WordPress auto-updates or Kinsta automatic updates](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-plugins-themes-automatic-updates/) for your plugins and themes.
- **PHP settings:**
  - **Change PHP performance:** Update the [PHP performance](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/) settings.
  - **Change PHP version:** This allows you to change the [PHP version](https://kinsta.com/docs/wordpress-hosting/php/wordpress-restart-update-php/) and enable or disable [Automatic PHP updates](https://kinsta.com/docs/wordpress-hosting/php/wordpress-restart-update-php/).
- **Backups:**
  - **Change external backups:** Enable or disable the [external backups add-on](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#external-backups-add-on).
  - **Change hourly backups:** Enable or disable the [hourly backups add-on](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#hourly-backups-add-on).
- **Export to CSV:** [Exports a list of selected sites](#export-a-list-of-wordpress-sites) to a CSV file.
- **Change labels:**Use this option to update the [site labels](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-labels).

![Perform bulk actions for your WordPress environments from Sites.](https://kinsta.com/wp-content/uploads/2026/09/wordpress-sites-bulk-actions-1.png)

Perform bulk actions for your WordPress environments from Sites.

## Search and filter sites

Within the WordPress sites list, you can search for a specific site, filter by the site label, or filter by plugin and theme updates. The plugin and theme filter allows you to filter by the following:

- **Update available:** Shows all sites that have a plugin or theme update available.
- **Plugin update available:** Shows all sites that have plugin updates available.
- **Theme update available:** Shows all sites that have theme updates available.
- **Vulnerable:**Shows all sites that have [vulnerable plugins or themes](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/#plugin-and-theme-vulnerabilities), which require an update for security purposes.

![Search and filter your sites.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-search-filter.png)

Search and filter your sites.

## Rename a site in MyKinsta

With Kinsta’s site renaming tool, you can change the display name of your Kinsta site in MyKinsta.

This tool is useful if you’ve recently [changed your WordPress site’s domain name](https://kinsta.com/blog/wordpress-change-domain/) or rebranded your business and want the name in MyKinsta to reflect that change.

The site renaming tool is available for the Company Owner, Company Administrator, Company Developer, and Site Administrator ([learn more about user roles in MyKinsta](https://kinsta.com/docs/company-settings/user-management/)).

Here’s how you can use the site renaming tool to rename your Kinsta site.

In [MyKinsta](https://kinsta.com/mykinsta/), navigate to**Sites** > ***sitename*** > **Info**, and click the edit (pencil) icon next to the **Site name**.

![Rename your site in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-rename-site-12.png)

Rename your site in MyKinsta.

You can also rename your site from your**Sites** list by clicking the kebab (three-dot) icon and selecting **Rename site** in the menu that appears.

![Rename your site from the Sites list in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-sites-rename-site.png)

Rename your site from the Sites list in MyKinsta.

Next, enter a new name for your site, and click **Rename site**.

[![Choose a new display name for your Kinsta site.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-rename-site-confirm-1024x300.png)](https://kinsta.com/wp-content/uploads/2023/11/wordpress-rename-site-confirm.png)

Choose a new display name for your Kinsta site.

The name change takes place immediately, and your site’s new name will appear in the MyKinsta top navigation bar and the **WordPress Sites** list.

## Suspend a WordPress site

Company Owners and Company Administrators can suspend a WordPress site’s environment to make it inaccessible to visitors. While suspended, you won’t be charged for bandwidth or visits, though the site will still use disk space on your plan.

When you try to visit the suspended site’s environment, you will receive a **Connection timed out** error. 

To suspend a site’s environment, on the **Info** page, click **Suspend site**. If you have multiple environments, this only suspends the selected environment. For example, if you have a live and staging environment and suspend the live one, the staging environment will still be accessible.

![Suspend a site in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/08/wordpress-suspend-site-1.png)

Suspend a site in MyKinsta.

Enter a reason for the suspension, select the confirmation box, and click **Suspend site**.

![Enter a suspension reason and select the confirmation. ](https://kinsta.com/wp-content/uploads/2026/08/wordpress-suspend-site-reason.png)

Enter a suspension reason and select the confirmation.

When the site is suspended, it is shown at the top of the site’s **Info** page along with the reason for the suspension.

![Site suspended message on your site's Info page.](https://kinsta.com/wp-content/uploads/2026/08/wordpress-site-suspended-1.png)

Site suspended message on your site’s Info page.

To reactivate a suspended site, from the site’s **Info** page, click **Activate site**. Once reactivated, you’ll be charged for visits or bandwidth again. Depending on the environment, it can take anywhere from a few seconds to a few minutes for the environment to be active again.

![Activate a suspended site in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/08/wordpress-activate-site-2.png)

Activate a suspended site in MyKinsta.

## Reset a WordPress site

You can reset your site to reinstall WordPress while keeping some of the site configuration, such as the domains and site options that were set when the site was created. Note that resetting is only available for sites with WordPress installed. If the site is empty (without WordPress), the reset option will not be available. When you reset a site:

- It removes all of the WordPress files, the database, and all standard and premium staging environments and installs a new WordPress.
- The PHP threads and memory per thread within [PHP performance](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/#view-php-performance) are retained, including any add-ons.
- Your [backups](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/) and  [activity log](https://kinsta.com/docs/company-settings/activity-log) are retained.
- Your [domain name(s)](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/) are also retained; therefore, no DNS changes are required unless you change the domain.
- [Redirects](https://kinsta.com/docs/wordpress-hosting/redirect-rules/) are removed and need to be added again if still required.
- You cannot configure the site options that you selected when the site was created. For example, if you selected **Install Yoast SEO** when the site was first created, this option remains enabled when you reset the site and cannot be changed.
- You must set a new WordPress admin password.
- Kinsta performs a system backup before the site reset so you can [restore your site](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/#restore-wordpress-backups) if required.

To reset your site, click**Sites** > ***sitename*** > **Info** > **Reset site**.

![Reset your site from the site's Info page.](https://kinsta.com/wp-content/uploads/2025/03/wordpress-reset-site.png)

Reset your site from the site’s Info page.

Enter a new **WordPress admin password** and click **Continue**.

![Reset your site to install a new WordPress but retain the settings.](https://kinsta.com/wp-content/uploads/2024/01/wordpress-reset-site-992x1024.png)

Reset your site to install a new WordPress, but retain the settings.

Select the acknowledgment checkbox, enter your site name followed by -live, and click **Reset WordPress site**.

![Confirmation screen to reset your site.](https://kinsta.com/wp-content/uploads/2024/01/wordpress-reset-site-confirm-1-1024x553.png)

Confirmation screen to reset your site.

It may take a few minutes to reset the site, and the Resetting WordPress site screen will show until the reset is complete.

![The Resetting WordPress site screen shows until the site reset is complete. ](https://kinsta.com/wp-content/uploads/2024/01/wordpress-resetting-wordpress-site-1024x330.png)

The Resetting WordPress site screen shows until the site reset is complete.

## Delete a WordPress site

If you need to remove a site you’re no longer using or need to start over with a site you’re developing, you can delete your site from within [MyKinsta](https://my.kinsta.com/).

Click on **Sites**, select the site you want to delete, scroll down, and click on the **Delete Site** button.

![Delete your site from the site's Info page.](https://kinsta.com/wp-content/uploads/2025/03/wordpress-delete-site.png)

Delete your site from the site’s Info page.

You’ll get a modal/pop-up asking you to confirm the deletion of your site.

You have to accept the following prompts:

- The files and database for your site will be deleted.
- The files and database in the staging environments for your site will also be deleted.
- Removing the site does not cancel the WordPress Hosting plan. This prompt only appears if the site you are deleting is the only WordPress site on your plan.

Then, enter your site’s name followed by a dash and the word “live” (**sitename-live**) in the field and click **Delete Site**.

![Delete WordPress site confirmation.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-delete-site-confirm-1-1024x563.png)

Delete WordPress site confirmation.

Once the site is deleted, you’ll have an open spot in your plan for a new site. If you also want to cancel your WordPress Plan, you can do this within **Company settings** > **My Plan** > **Cancel plan**; refer to [Cancel WordPress Plan](https://kinsta.com/docs/billing/wordpress-hosting-plans/cancel-wordpress-plan).

## Change your site’s path

The site path is where your WordPress files (such as `wp-config.php`, `wp-content`, `wp-admin`, and `wp-includes`) are located. You can view the site path within **Environment details** on your site’s **Info** page.

The default path for your site is `/www/$site_path/public`. You can customize this path by adding a subfolder using the [Kinsta API](https://api-docs.kinsta.com/#tag/WordPress-Site-Environments/operation/changeEnvironmentWebRootSubfolder), for example: `/www/$site_path/public/site`.

![WordPress site path.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-site-path-4.png)

WordPress site path.

## Export a list of WordPress sites

From the**Sites** list, you can export a list of selected WordPress sites to a CSV file. Select the sites you want to include in the export and click **Actions** > **Export to CSV**.

![Select which sites you want to export to CSV.](https://kinsta.com/wp-content/uploads/2026/09/wordpress-sites-export-1.png)

Select which sites you want to export to CSV.

The CSV export includes the following information about your sites:

- Site name
- Environment name
- Identifier
- Staging type
- Location (data center location)
- Visits
- Bandwidth – In the `.csv` file, this is shown in bytes; in MyKinsta, this is rounded up to MB or GB.
- Disk Usage – In the `.csv` file, this is shown in bytes; in MyKinsta, this is rounded up to MB or GB.
- Force HTTPS (enabled or disabled)
- Domains
- Primary domain
- IP
- Load balancer
- Path
- Port
- Staging port
- Current External IP address
- PHP version
- Create at (date)

## Max upload size for files

At Kinsta, we set the uploaded file size limit to 128MB, which is quite large for a single file.

### Max upload file size for WordPress

If you’re trying to upload a file to your WordPress site and see either of the following error messages, that means that your file is larger than 128MB:

- “The uploaded file exceeds the upload_max_filesize directive in php.ini.”
- “file_name exceeds the maximum upload size for this site.”

To request an increase in the allowed size beyond the default 128 MB limit, you can open a [chat with our Support team](https://kinsta.com/docs/support/contact-support/) in MyKinsta.

### Max upload file size for WordPress multisite

In a [WordPress Multisite Network](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/multisite-network), you can set the max upload file size for the subsites in the WordPress Network Admin. Log in to your WordPress dashboard and go to **Settings** > **Network Settings**. Scroll down to the **Upload Settings** section.

To increase the max upload file size for your network’s subsites beyond the 1500KB (~1.5MB) default, enter the new value in the **Max upload file size** field and click the **Save Changes** button.

## Move an existing site to a new location

If your site needs to be moved to a different data center, that requires some additional steps from our team. Open a new [chat with our Support team](https://kinsta.com/docs/support/contact-support/) in MyKinsta to get that started.

Moving the site to a new [data center](https://kinsta.com/docs/service-information/data-center-locations/) will change the **Host IP** address (used for [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/) and [SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) connections) and may require an [external IP address](https://kinsta.com/docs/wordpress-hosting/site-management/ip-addresses/) change. The external IP address is the one other parties see when your site makes an external connection to an external server. This is sometimes used for integrations with payment processors like PayPal or added to allow lists for some services.

**Note:** The [Site IP](https://kinsta.com/docs/wordpress-hosting/site-management/ip-addresses/) (the IP you point your domain’s A record to) is separate and will not change.

Here at Kinsta, we’re constantly upgrading MyKinsta with new features to make managing your WordPress sites easier. Be sure to [subscribe to our newsletter](https://kinsta.com/wordpress-newsletter/) to stay up to date on our latest features and best articles!
