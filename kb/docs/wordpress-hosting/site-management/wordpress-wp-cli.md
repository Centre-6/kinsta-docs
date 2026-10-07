---
url: "https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-wp-cli/"
title: "Site Management - WP-CLI"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "site-management"
section: []
kinsta_last_updated: "August 13, 2025"
sitemap_lastmod: "2025-08-13T07:49:53+00:00"
fetched_at: "2026-10-07T22:38:53Z"
sha256: "fc7ac28d840858555e459cf52d763a665192e1c303b83358ab2df416d480cfcc"
body_chars: 10170
extracted_with: "main article"
status: "live"
---

# Site Management - WP-CLI

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-wp-cli/
**Kinsta last updated:** August 13, 2025

## On this page

- [Access WP-CLI on Kinsta](#access-wp-cli-on-kinsta)
  - [1. Connect to your server with SSH](#1-connect-to-your-server-with-ssh)
    - [Windows](#windows)
    - [Mac/Linux](#maclinux)
  - [2. Navigate to your site’s document root](#2-navigate-to-your-sites-document-root)
- [Useful WP-CLI Commands](#useful-wp-cli-commands)
  - [Useful options](#useful-options)
  - [Plugins](#plugins)
    - [View a list of plugins](#view-a-list-of-plugins)
    - [Activate a plugin](#activate-a-plugin)
    - [Deactivate a plugin](#deactivate-a-plugin)
    - [Update a specific plugin](#update-a-specific-plugin)
    - [Update all plugins](#update-all-plugins)
    - [Roll back a plugin](#roll-back-a-plugin)
  - [URLs](#urls)
    - [Set the home URL](#set-the-home-url)
    - [Set the site URL](#set-the-site-url)
  - [Users](#users)
    - [List all WordPress users](#list-all-wordpress-users)
    - [Create a new user](#create-a-new-user)
    - [Reset a user’s password](#reset-a-users-password)
    - [Update a user’s details](#update-a-users-details)
  - [Cache](#cache)
    - [Clear all cache](#clear-all-cache)
    - [Clear the full-page cache and edge cache](#clear-the-full-page-cache-and-edge-cache)
    - [Clear site cache without clearing edge cache](#clear-site-cache-without-clearing-edge-cache)
    - [Clear the CDN cache](#clear-the-cdn-cache)
    - [Clear Redis cache](#clear-redis-cache)
    - [Flush object cache](#flush-object-cache)
  - [Search and replace](#search-and-replace)
    - [Replace old domain with new domain](#replace-old-domain-with-new-domain)
    - [Replace HTTP with HTTPS](#replace-http-with-https)
- [Troubleshooting](#troubleshooting)

---

WP-CLI (WordPress Command Line Interface) is a powerful tool for managing a WordPress installation directly from the command line or terminal. Instead of using the standard WordPress dashboard, you can execute commands to perform tasks like updating plugins, managing themes, and configuring settings, all from your terminal.

There are a number of benefits to using WP-CLI, including:

- **Speed:** Performing tasks using the command line is often faster than navigating through the WordPress admin interface, especially for repetitive tasks.
- **Automation:** WP-CLI can be integrated into scripts for automated workflows.
- **Remote Management:** WP-CLI allows you to manage WordPress sites remotely.
- **Flexibility:** The ability to execute commands and scripts provides a level of control and customization.

## Access WP-CLI on Kinsta

WP-CLI v2 is installed by default on all of our servers. To access WP-CLI, you must [connect to your server with SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) and navigate to your site’s document root. Kinsta provides SSH access with all of our Managed WordPress Hosting plans.

### 1. Connect to your server with SSH

The easiest method for connecting via SSH is to use a username and password. The steps to connect vary depending on your operating system.

#### Windows

Windows users require a terminal client to connect to SSH. We recommend downloading the [free PuTTY client](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) using the .msi installer.

1. Launch PuTTY and enter your **Host IP Address** and the unique **Port** number (both found in [MyKinsta](https://my.kinsta.com/) > **Sites** > ***sitename*** > **Info** > **SFTP/SSH**). Then click **Open**.
2. If this is your first time connecting, you will most likely see a rsa2 key prompt. Click **Yes**, and this will trust the host in the future.
3. In the terminal screen, enter your Kinsta username (found in [MyKinsta](https://my.kinsta.com/) > **Sites** > ***sitename*** > **Info** > **SFTP/SSH**) and press Enter.
4. Enter your Kinsta password (found in [MyKinsta](https://my.kinsta.com/) > **Sites** > ***sitename*** > **Info** > **SFTP/SSH**) and press Enter again.

You’re now connected via SSH to your WordPress site.

#### Mac/Linux

1. Open a new terminal from **Applications** > **Utilities** > **Terminal**.
2. In MyKinsta, navigate to **Sites** > ***sitename*** > **Info** > **SFTP/SSH**, and on the **SSH terminal command** click **Copy to clipboard.**
3. Paste the **SSH terminal command** into the terminal and press Enter.
4. Enter your Kinsta password (found in [MyKinsta](https://my.kinsta.com/) > **Sites** > ***sitename*** > **Info** > **SFTP/SSH**) and press Enter again.

You’re now connected via SSH to your WordPress site.

### 2. Navigate to your site’s document root

To run WP-CLI commands, you must first navigate to your site’s document root; this is where your WordPress files (such as `wp-config.php`, `wp-content`, `wp-admin`, and `wp-includes`) are located. To navigate to your site’s document root on Kinsta, enter the following command:

Copy

```
cd public
```

You can now use WP-CLI commands on your WordPress installation hosted on Kinsta. For a full list of available WP-CLI commands, refer to the [WordPress developer documentation](https://developer.wordpress.org/cli/commands/).

## Useful WP-CLI Commands

The following is a list of WP-CLI commands you may find helpful. For a full list of available WP-CLI commands, including global parameters and options, refer to the [WordPress developer documentation](https://developer.wordpress.org/cli/commands/).

### Useful options

The following is a list of useful options you can add to the end of your commands:

- `--skip-themes`: This prevents WordPress themes from loading when you execute a WP-CLI command. This is useful if there is an issue in one of the themes that causes conflicts with WP-CLI commands.
- `--skip-plugins`: This prevents WordPress plugins from loading when you execute a WP-CLI command. This is useful if there is an issue in one of the plugins that causes conflicts with WP-CLI commands.
- `--all`: This applies a command to all relevant items. For example, if you want to update all plugins or users.
- `--dry-run`: This can be used to simulate the execution of a command without making any actual changes. It shows you what would happen if the command were executed, but it won’t perform any of the actions. For example, if you run a search and replace, update all plugins, or bulk delete posts.
- `--format=<format>`: Specifies the output format when exporting data. For example, when you run `wp plugin list` or `wp user list` you may want this in `table`, `json`, or `csv` format.

### Plugins

#### View a list of plugins

View a list of installed plugins with the following command:

Copy

```
wp plugin list
```

#### Activate a plugin

To activate a plugin, use the following command, replacing `$plugin` with the name of the plugin from the `wp plugin list`.

Copy

```
wp plugin activate $plugin
```

#### Deactivate a plugin

To deactivate a plugin, use the following command, replacing `$plugin` with the name of the plugin from the `wp plugin list`.

Copy

```
wp plugin deactivate $plugin
```

#### Update a specific plugin

To update a plugin, use the following command, replacing `$plugin` with the name of the plugin from the `wp plugin list`.

Copy

```
wp plugin update $plugin
```

#### Update all plugins

Copy

```
wp plugin update --all
```

#### Roll back a plugin

If you update a plugin that then breaks something on your site, you can roll it back by installing a specific version using the following command, replacing `$plugin` with the name of the plugin from the `wp plugin list` and `$version`with the required version number.

Copy

```
wp plugin update $plugin --version=$version
```

### URLs

#### Set the home URL

To set the URL for your home page, use the following command, replacing `$URL` with the required URL.

Copy

```
wp option update home '$URL'
```

#### Set the site URL

To set the site URL, use the following command, replacing `$URL` with the required URL.

Copy

```
wp option update siteurl '$URL'
```

### Users

#### List all WordPress users

View a list of all WordPress users with the following command:

Copy

```
wp user list
```

#### Create a new user

To create a new user, use the following command, replacing `$username` and `$emailaddress` with the user’s credentials, and `$role` with the role you want to assign the new user to, for example, administrator.

Copy

```
wp user create $username $emailaddress -–role=$role
```

#### Reset a user’s password

To reset a user’s password, use the following command, replacing `$username`with the required username from the `wp user list`.

Copy

```
wp user reset-password $username
```

#### Update a user’s details

To update a user, use the following command, replacing `$user`with the required username from the `wp user list`, `$field` with the field you want to update, and `$value` with the new data you want to enter.

Copy

```
wp user update $user -—$field=$value
```

### Cache

To use the clear cache commands listed below, the [Kinsta Must Use (MU) plugin](https://kinsta.com/docs/wordpress-hosting/kinsta-mu-plugin/) must be installed on the site.

#### Clear all cache

To clear all cache, including site cache, edge cache, CDN cache, and Redis cache, use the following command:

Copy

```
wp kinsta cache purge --all
```

#### Clear the full-page cache and edge cache

To clear the full-page cache and the edge cache, use the following command:

Copy

```
wp kinsta cache purge
```

#### Clear site cache without clearing edge cache

To only clear the site cache, use the following command:

Copy

```
wp kinsta cache purge --site
```

#### Clear the CDN cache

To only clear the CDN cache, use the following command:

Copy

```
wp kinsta cache purge --cdn
```

#### Clear Redis cache

To only clear the Redis cache, use the following command:

Copy

```
wp kinsta cache purge --object
```

#### Flush object cache

Flush your site’s object cache with the following command:

Copy

```
wp cache flush
```

This may lead to a slight increase in load times temporarily as the cache rebuilds.

### Search and replace

When running any search and replace on your WordPress site, we recommend [backing up](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/) and using the `--dry-run` option to see what will be replaced before executing the command.

#### Replace old domain with new domain

To replace an old URL with a new URL, use the following command, replacing `$old-domain` with the URL you want to replace and `$new-domain` with the URL you want to replace it with:

Copy

```
wp search-replace '$old-domain' '$new-domain' --skip-columns=guid
```

`--skip-columns=guid` is recommended to avoid accidentally altering URLs stored as unique identifiers in the database’s `guid` column, which could break post URLs. This command can also be used to replace email address domains.

#### Replace HTTP with HTTPS

To update your URLs from HTTP to HTTPS, use the following command:

Copy

```
wp search-replace 'http://' 'https://' --skip-columns=guid
```

`--skip-columns=guid` is recommended to avoid accidentally altering URLs stored as unique identifiers in the database’s `guid` column, which could lead to issues with media attachments.

## Troubleshooting

If you have issues running commands in WP-CLI, this may be due to a theme or plugin experiencing a fatal error. You can add the following to your WP-CLI command to skip loading themes and plugins:

Copy

```
--skip-themes --skip-plugins
```

For example, to get a list of users and skip the themes and plugins, you can run the following:

Copy

```
wp user list --skip-themes --skip-plugins
```

If you want to skip specific plugins, you can use the following, replacing `$plugin` with the plugin name and using a comma to separate each plugin:

Copy

```
--skip-plugins=$plugin,$plugin
```

For example:

Copy

```
wp user list --skip-plugins=wordpress-seo,wordfence
```
