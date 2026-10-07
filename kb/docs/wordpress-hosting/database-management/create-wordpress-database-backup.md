---
url: "https://kinsta.com/docs/wordpress-hosting/database-management/create-wordpress-database-backup/"
title: "Database Backup"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "database-management"
section: ["WordPress Hosting", "Database Management"]
kinsta_last_updated: "2025-10-15T10:44:15"
change_signal: "2025-10-15T10:44:15"
fetched_at: "2026-10-07T22:58:19Z"
sha256: "1b570b64013a01019b586b927d57bb90352c25e8a6cb18145b4e12a050fd1edb"
body_chars: 4587
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Database Backup

**Section:** WordPress Hosting > Database Management
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/database-management/create-wordpress-database-backup/
**Kinsta last updated:** 2025-10-15T10:44:15

## On this page

- [Download a backup from MyKinsta](#download-a-backup-from-mykinsta)
- [Create a database backup with phpMyAdmin](#create-a-database-backup-with-phpmyadmin)
- [Back up a database with WP-CLI and SFTP](#back-up-a-database-with-wp-cli-and-sftp)
- [Back up a database with the external backups add-on](#back-up-a-database-with-the-external-backups-add-on)

---

At Kinsta, we provide backups that are a [complete snapshot of your WordPress site’s environment](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/) (including files, database, redirects, and Nginx configuration). There may be times you want to back up just your site’s database, and this guide will show you a few different ways to do that.

## Download a backup from MyKinsta

With this option, you’ll extract your site’s database from a backup you download from MyKinsta.

1. If you haven’t already, log in to [MyKinsta](https://my.kinsta.com) and select your site on the **Sites** page.
2. Go to **Backups** > **Download** and click on the **Create backup now** button. This may take a bit of time to complete, depending on the size of your site. We’ll keep you updated with a notification in MyKinsta as well as an email to let you know when it’s ready.

   ![Downloadable backups in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-backups-download.png)

   Downloadable backups in MyKinsta.
3. When your backup is ready to download, click on the “Download the backup now!” link in the email you received or the **Download backup** button in MyKinsta.
4. When the download finishes, you’ll have a .zip file that contains your site files and database. [Unzip](https://kinsta.com/blog/unzip-zip-file/) that file and look for the ***sitename*****.sql** database file.
   ![View the database (.sql) file in the downloadable backup of your WordPress site.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-backup-zip.png)

   View the database (.sql) file in the downloadable backup of your WordPress site.

   **Note:** You can create one downloadable backup **per week.** If you need more database backups during the same week, you’ll need to use one of the other database backup methods in this guide.

## Create a database backup with phpMyAdmin

[phpMyAdmin](https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database-access/) is a database management tool you can use to view, import, and export data in and out of your database.

1. Log in to [MyKinsta](https://my.kinsta.com), go to **Sites**, and select your site in the list.
2. On the **Info** tab, scroll down to **Database access**. Click **Open phpMyAdmin**, which will open phpMyAdmin in a new tab in your browser and automatically log you in using your database credentials.

   ![Open phpMyAdmin from MyKinsta.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-open-phpmyadmin.png)

   Open phpMyAdmin from MyKinsta.
3. Click on the **Export** tab near the top of the page.
4. Select the **Quick** export method, keep the format as **SQL**, and click **Export** to download your database backup (.SQL file).

   ![Exporting a database with the quick export method in phpMyAdmin.](https://kinsta.com/wp-content/uploads/2026/04/phpmyadmin-export.png)

   Exporting a database with the quick export method in phpMyAdmin.

## Back up a database with WP-CLI and SFTP

If you have trouble with the phpMyAdmin interface or just want to use a different method, a slightly longer process is to use WP-CLI to export your database, then connect to the server with SFTP and download the database (.SQL) file.

1. Connect to your server [with SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) and navigate to the public directory:

   ```
   cd public
   ```
2. Export your site’s database (replace db-backup-name with your preferred file name):

   ```
   wp db export db-backup-name.sql
   ```
3. Connect to your site with [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/) and go to the public directory.
4. Download your database (.sql) file.

## Back up a database with the external backups add-on

Our [external backups add-on](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#external-backups-add-on) allows you to set up automatic external backups of your Kinsta site to Amazon S3 or Google Cloud Storage. With this add-on, you have the option to back up your files, your database, or both.

To create an external backup of just your database, select **Database** when setting up your external backup.

![Selecting just the database for an external backup in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-external-backup-choose-files-1024x576.png)

Selecting just the database for an external backup in MyKinsta.

With these methods, you have several ways to get a backup of your website’s database when needed.
