---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/fix-error-establishing-a-database-connection-in-wordpress/"
title: "Troubleshooting - Database Connection Errors"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-troubleshooting"
section: []
kinsta_last_updated: "August 13, 2024"
sitemap_lastmod: "2024-08-13T10:31:40+00:00"
fetched_at: "2026-10-07T22:36:53Z"
sha256: "22c37750dc618429f1f74ac2add08c127f71a8793e350c04e28879677904a093"
body_chars: 7531
extracted_with: "main article"
status: "live"
---

# Troubleshooting - Database Connection Errors

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/fix-error-establishing-a-database-connection-in-wordpress/
**Kinsta last updated:** August 13, 2024

## On this page

- [Error Establishing a Database Connection causes](#error-establishing-a-database-connection-causes)
- [Fixing Error Establishing a Database Connection](#fixing-error-establishing-a-database-connection)
  - [Check that your DNS is pointed to Kinsta](#check-that-your-dns-is-pointed-to-kinsta)
  - [Check your database credentials](#check-your-database-credentials)
    - [Database name](#database-name)
    - [MySQL database username](#mysql-database-username)
    - [MySQL database password](#mysql-database-password)
    - [MySQL hostname (server)](#mysql-hostname-server)
  - [Repair a corrupt database](#repair-a-corrupt-database)
    - [Repairing a database with WordPress](#repairing-a-database-with-wordpress)
    - [Repairing a database with phpMyAdmin](#repairing-a-database-with-phpmyadmin)
    - [Repairing a database with WP-CLI](#repairing-a-database-with-wp-cli)
  - [Fix corrupt files](#fix-corrupt-files)
    - [Reinstall WordPress core with SFTP](#reinstall-wordpress-core-with-sftp)
    - [Reinstall WordPress core with WP-CLI](#reinstall-wordpress-core-with-wp-cli)
  - [Restore your latest working backup](#restore-your-latest-working-backup)
  - [Contact support](#contact-support)

---

When your WordPress site can’t connect to the site’s database, it displays this error:

> Error Establishing a Database Connection

## Error Establishing a Database Connection causes

There are a few scenarios that can lead to this error:

- Your DNS is not pointed to Kinsta.
- The database credentials in wp-config.php are incorrect. This is fairly common when manually migrating or installing a WordPress site.
- Your website’s database is corrupted. While this isn’t as common, it can happen, and if your database credentials check out, this would be the next thing to investigate.
- There may be corrupted files in your WordPress installation. Another situation that isn’t common but can happen sometimes due to a hack or an issue when copying or uploading the files.

## Fixing Error Establishing a Database Connection

Head to the **Backups** tab for your site in [MyKinsta](https://my.kinsta.com/) and click the **Back up now** button to make a backup of your site.

### Check that your DNS is pointed to Kinsta

If your domain’s DNS has not been pointed to Kinsta, requests reach Kinsta’s infrastructure, but the server may not correctly match your hostname to your site’s environment and its database credentials, resulting in this error.

To check this, go to your site’s **Domains** list and confirm your domain is added, correctly pointed, and set as your primary domain. If it isn’t, follow the steps in [Add a domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/) to complete the setup.

### Check your database credentials

To check your site’s database credentials, begin by heading over to your site’s **Info** tab in MyKinsta. Under the **Database access** section, you’ll find your database name, username, and password. Next, view your site’s **wp-config.php** file using either [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/) or [SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) and compare the database details:

#### Database name

Copy

```
// ** MySQL settings ** //
/** The name of the database for WordPress */
define('DB_NAME', 'xxxxxx');
```

#### MySQL database username

Copy

```
/** MySQL database username */
define('DB_USER', 'xxxxxx');
```

#### MySQL database password

Copy

```
/** MySQL database password */
define('DB_PASSWORD', 'xxxxxx');
```

#### MySQL hostname (server)

Copy

```
/** MySQL hostname */
define('DB_HOST', 'localhost');
```

If any of those details do not match, update your wp-config.php with the correct information and save your changes. If you’re viewing and editing the file on your local machine after downloading it with SFTP, be sure to upload the updated file to the server, overwriting the old **wp-config.php** file.

If all of the details match but the error persists, continue on to the next section.

### Repair a corrupt database

As mentioned earlier, this isn’t as common but can happen over time as database tables are added, removed, or altered by plugins and themes. If you try logging into your WordPress dashboard and see the following error, this indicates the database is corrupted and will need to be repaired:

> One or more database tables are unavailable. The database may need to be repaired.

To repair your database, you have a few options, which we explain below: with WordPress, in phpMyAdmin, or using WP-CLI.

#### Repairing a database with WordPress

Fortunately, WordPress has a database repair mode which you can initiate by adding the following code snippet to the bottom of your **wp-config.php** file.

Copy

```
define('WP_ALLOW_REPAIR', true);
```

After saving that change, go to https://yourdomain.com/wp-admin/maint/repair.php in your browser to open the interface for repairing your site’s database:

![WordPress repair database](https://kinsta.com/wp-content/uploads/2017/06/wordpress-repair-database.png)

WordPress repair database

The **Repair Database** option is quicker than the **Repair and Optimize Database** option. If this is a live site you’re working to get back up and running, we recommend going with the **Repair Database** option.

#### Repairing a database with phpMyAdmin

[Log in to phpMyAdmin](https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database-access/), click on your database, and select all the tables. From the dropdown menu near the bottom of the page, select **Repair table**. This does the same thing as running the [REPAIR TABLE](https://dev.mysql.com/doc/refman/5.7/en/repair-table.html) MySQL statement.

![Repair database tables in phpMyAdmin.](https://kinsta.com/wp-content/uploads/2021/12/phpmyadmin-repair-all-tables.jpg)

Repair database tables in phpMyAdmin.

#### Repairing a database with WP-CLI

To repair your database with WP-CLI, run the following command:

Copy

```
wp db repair
```

Once it’s finished, you’ll see the following success message:

Copy

```
Success: Database repaired.
```

### Fix corrupt files

Another less common cause of a database connection error is corrupted WordPress core files. To test and fix this, you’ll need to replace your WordPress core files via [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/) or WP-CLI.

#### Reinstall WordPress core with SFTP

Begin by downloading a fresh copy of WordPress from WordPress.org. Be sure to download the same version you’re running on your site.

Unzip the downloaded file on your local computer, then delete the **wp-content** folder and the **wp-config-sample.php** file.

Connect to your site with SFTP and upload the remaining WordPress files to your site, overwriting the existing files.

Once the upload is complete, [empty your site’s cache](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/) and test the site to see if the error is cleared.

#### Reinstall WordPress core with WP-CLI

To reinstall WordPress without overwriting the **wp-content** directory (where your theme, plugins, and media are stored), run the following command:

Copy

```
wp core download --skip-content --force
```

Once the reinstall is complete, [empty your site’s cache](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/) and test the site to see if the error is cleared.

### Restore your latest working backup

If all else fails, you can try [restoring your latest working backup](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#restore-wordpress-backups). Note: this may not be your most recent backup if the error has been going on for some time.

In MyKinsta, go to your site’s **Backups** tab and choose the backup you want to restore. If you want to [test the backup in staging](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#restoring-wordpress-backups-to-staging) before restoring it to your live site, click the **Restore to** button, and in the dropdown menu, select the **Staging** environment you want to restore the backup to.

![Restore a backup to Staging](https://kinsta.com/wp-content/uploads/2023/11/wordpress-restore-backup-1024x268.png)

Restore a backup to Staging

Once you’re sure you want to restore the backup to your live site, click the **Restore to** button next to the backup, then choose **Live** from the dropdown menu.

### Contact support

If you’ve followed the troubleshooting steps above, but this error persists, our knowledgeable [Support team is here to help 24/7](https://kinsta.com/docs/support/contact-support/).
