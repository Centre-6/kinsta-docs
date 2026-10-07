---
url: "https://kinsta.com/changelog/kinsta-automatic-updates/"
title: "Kinsta Automatic Updates: Hands-free WordPress plugin and theme management"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2025-03-28T19:16:13"
change_signal: "2025-03-28T19:16:13"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "4dad5a55a36c7048f484802cec00319a9a4b760eea4ae7807bf09b9b72f0f3b7"
body_chars: 8992
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Kinsta Automatic Updates: Hands-free WordPress plugin and theme management

**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-automatic-updates/
**Kinsta last updated:** 2025-03-28T19:16:13

## On this page

- [MyKinsta is home for plugin and theme updates](#mykinsta-is-home-for-plugin-and-theme-updates)
  - [Discovering vulnerable plugins and themes](#discovering-vulnerable-plugins-and-themes)
  - [Managing automatic updates](#managing-automatic-updates)
  - [Configuring automatic updates for individual plugins or themes](#configuring-automatic-updates-for-individual-plugins-or-themes)
  - [Reviewing the results of Kinsta Automatic Updates](#reviewing-the-results-of-kinsta-automatic-updates)
- [Powerfully simple WordPress hosting](#powerfully-simple-wordpress-hosting)

---

Kinsta’s WordPress hosting customers can now automate updates of plugins and themes and be confident that an unexpected update failure won’t leave a site hanging.

Kinsta Automatic Updates can keep plugins and themes current across all your WordPress sites while automatically detecting and recovering from changes that go wrong. By comparing before-and-after-update screenshots of a site’s pages, the feature’s visual regression testing can confirm successful updates and roll back any that fail.

Daniel Pataki, Kinsta’s CTO, says this new feature “is designed to take the hassle out of managing WordPress updates.”

“Keeping sites secure and up to date shouldn’t be a time-consuming task,” Pataki says, “and with Kinsta Automatic Updates, our customers can stay protected with minimal effort. By automating plugin and theme updates while ensuring stability through visual regression testing and rollback protection, we’re making WordPress maintenance easier and more reliable than ever.”

Kinsta Automatic Updates is a premium add-on that costs $3 USD a month for each environment in which it is active. There is no limit to the number of plugins or themes you manage with the add-on within an environment.

## MyKinsta is home for plugin and theme updates

Regular users of the [MyKinsta dashboard](https://kinsta.com/mykinsta/) for managing WordPress sites have seen Kinsta Automatic Updates come together in recent weeks. With the help of feedback from these users, Kinsta has transformed MyKinsta into a comprehensive resource for all things related to plugin and theme updates — from reporting on vulnerable releases to managing the native WordPress auto-update capability across multiple websites to the new Kinsta Automatic Updates feature itself.

### Discovering vulnerable plugins and themes

Nothing confirms the need for automatic updates like finding plugins and themes that are not just out of date but also dangerously vulnerable to security breaches. You can check this in MyKinsta for an individual site environment by navigating to **WordPress sites** > ***sitename/environment*** > **Plugins and themes**.

The detail below from the **Installed plugins** section of that page reveals that the installed version of Yoast SEO (22.2) is not the latest available. What’s more, it’s a release that is known to have possible security vulnerabilities.

![Screenshot showing plugins with updates available, listed in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/03/kinsta-automatic-updates-vulnerability-indicator.png)

Version 22.2 of Yoast SEO is installed and active, but version 24.6 is available.

Here’s another view that spans multiple sites and environments under the **Plugins** tab of the **WordPress sites** page:

![Screenshot showing plugins and update statuses across multiple WordPress environments.](https://kinsta.com/wp-content/uploads/2025/03/kinsta-automatic-updates-vulnerability-indicator-all-sites.png)

A view of plugin statuses across multiple WordPress environments.

Above the “ACME Anvil Co.” has out-of-date versions of the Yoast SEO plugin active in two environments, one of which might be vulnerable. The plugin is up to date in both environments of the second site, with automatic updates being delivered by the WordPress native auto-update functionality.

### Managing automatic updates

To apply automatic update settings for plugins and themes, you can return to **WordPress sites** > ***sitename/environment*** > **Plugins and themes** and then click the **Change** button on the **Automatic updates** card:

![Screenshot showing the Change button that launches the automatic updates settings dialog.](https://kinsta.com/wp-content/uploads/2025/03/kinsta-automatic-updates-change-button.png)

Changing automatic update settings for a WordPress environment.

The subsequent dialog asks you to select one of three update options:

- Manual (no automatic updates)
- WordPress auto-updates
- Kinsta Automatic Updates

![A screenshot showing the dialog for choosing plugin and theme update options within MyKinsta.](https://kinsta.com/wp-content/uploads/2025/03/kinsta-automatic-updates-change-dialog.png)

Selecting the plugin and theme update option in MyKinsta.

If you select the **Manual** option, automatic updates will be disabled (including for any plugins or themes that already had automatic updates enabled). With this setting enabled, you will update plugins and themes individually within the [WordPress admin dashboard](https://kinsta.com/blog/wordpress-admin/) or in MyKinsta (including using its [bulk update](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-manage-plugins-themes/#update-plugins-and-themes) capability).

If you select **WordPress auto-updates**, the CMS’s native update functionality will be enabled for all plugins and themes. This well-known WordPress feature does not offer any safety net when an update creates unexpected problems for your website.

Finally, selecting **Kinsta Automatic Updates** allows you to configure the new advanced update features with scheduling and emergency rollback on errors. Select this option, click **Continue,** and you can edit the settings for Kinsta Automatic Updates:

![Screenshot showing the settings dialog for Kinsta Automatic Updates.](https://kinsta.com/wp-content/uploads/2025/03/kinsta-automatic-updates-settings-dialog.png)

Editing the settings for Kinsta Automatic Updates.

Let’s run through the options in the above settings dialog for Kinsta Automatic Updates:

- **Testing frequency:** You can choose the days of the week on which you want Kinsta Automatic Updates to check for new releases and install any that it finds.
- **Testing time window:** The time of day you want the automatic updates to run.
- **Sensitivity:** The visual regression tests compare the pixels in before-and-after screenshots to determine if an update has changed a page’s presentation. This setting allows you to specify how strict you want that comparison to be. A higher value can detect more subtle changes but can also result in more false positives.
- **Test URLs:** You can add up to five URLs pointing to pages on your website that will be used for the visual regression tests. If you leave the field blank, the test will evaluate the site’s homepage and four random pages.
- **Hide selectors:** Some dynamic content can cause a visual regression test to fail. This option allows you to specify CSS selectors that present that content and hide it from those tests.
- **Enable WordPress maintenance mode:** Select this option to display a maintenance page when the updates are running.

### Configuring automatic updates for individual plugins or themes

You can also enable or disable automatic updates on a per-plugin or per-theme basis. Below, within our list of site plugins, we clicked on the kabob (three-dot menu) beside the Ninja Forms entry:

![Screenshot showing the drop-down menu beside a specific plugin and the option to change its auto-update status.](https://kinsta.com/wp-content/uploads/2025/03/kinsta-automatic-updates-set-individual.png)

Changing automatic updates for a specific plugin.

Choosing **Change automatic updates** in the example above results in the selection dialog we saw earlier, except that it is now targeting a single plugin:

![Screenshot showing the dialog for choosing an update option for an individual plugin within MyKinsta.](https://kinsta.com/wp-content/uploads/2025/03/kinsta-automatic-updates-change-individual.png)

Enabling or disabling automatic updates for a single plugin.

### Reviewing the results of Kinsta Automatic Updates

When an update is identified and installed, it appears within **Plugins and themes** > **Kinsta Automatic Updates**:

![Screenshot showing a log of Kinsta Automatic Updates activity in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/03/kinsta-automatic-updates-report.png)

Viewing the log of Kinsta Automatic Updates activity.

Click **Details** to view information about the plugin or theme update. Click on the plugin or theme name to reveal the screenshots used for the visual regression tests:

![The report of a plugin update, including the screenshots used for regression testing.](https://kinsta.com/wp-content/uploads/2025/03/kinsta-automatic-updates-details.png)

Update details with screenshots used for the visual regression testing.

You can also receive email notifications of Kinsta Automatic Updates activity. Navigate to ***username*** > **User settings** > **Notifications** to enable email notifications for successful and/or failed updates.

## Powerfully simple WordPress hosting

We’re fanatical about making [WordPress maintenance](https://kinsta.com/blog/wordpress-maintenance/) simpler for our customers.

If you’re looking for lightning-fast and [secure](https://kinsta.com/wordpress-hosting/security/) WordPress hosting, explore [Kinsta’s plans](https://kinsta.com/pricing/) to find the one that fits your company best.
