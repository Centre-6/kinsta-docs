---
url: "https://kinsta.com/docs/wordpress-hosting/database-management/restore-import-mysql-database/"
title: "Database Management - Import MySQL Database"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "database-management"
section: []
kinsta_last_updated: "July 1, 2025"
sitemap_lastmod: "2025-07-01T16:24:51+00:00"
fetched_at: "2026-10-07T22:38:46Z"
sha256: "c285ef20b60caae752d940cd2dae9ea396b2e78bcee1afbe0fa3a85a4fd41978"
body_chars: 3790
extracted_with: "main article"
status: "live"
---

# Database Management - Import MySQL Database

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/database-management/restore-import-mysql-database/
**Kinsta last updated:** July 1, 2025

---

In MyKinsta, you can [restore a backup](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#restoring-wordpress-backups-to-staging) that is a complete snapshot of your site’s environment (including files, database, redirects, and Nginx configuration). If you want to restore or import **only** your site’s database, this guide will show you a couple of different ways to do that.

This tutorial assumes you already have a backup or exported *.sql file, which you will be importing. If not, see our guide: [How to Create a Database Backup](https://kinsta.com/docs/wordpress-hosting/database-management/create-wordpress-database-backup/).

These instructions are for importing a database backup of a site hosted at Kinsta. If you’re trying to import a database as part of a migration to Kinsta, check out our guide on [Migrating Your Site to Kinsta](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/).

## Restore a MySQL database using phpMyAdmin

[phpMyAdmin](https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database-access/) is a database management tool you can use to view, import, and export data in and out of your database. Before you import your database, you must ensure the existing database is empty.

1. Log in to [MyKinsta](https://my.kinsta.com), go to **Sites**, and select your site in the list.
2. On the **Info** tab, scroll down to **Database access**. Click **Open phpMyAdmin**, which will open phpMyAdmin in a new tab in your browser and automatically log you in using your database credentials.
   ![Open phpMyAdmin from MyKinsta.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-open-phpmyadmin.png)

   Open phpMyAdmin from MyKinsta.
3. To ensure the existing database is empty, click on your database name, check the box next to **Check all** to select, and in **With selected**, select **Drop**.
   ![Drop tables in phpMyAdmin.](https://kinsta.com/wp-content/uploads/2026/04/phpmyadmin-drop-tables.png)

   Drop tables in phpMyAdmin.
4. On the next page, confirm the `DROP TABLE` query by clicking **Yes**.
   ![Confirm you want to run the query to drop tables in phpMyAdmin.](https://kinsta.com/wp-content/uploads/2026/04/phpmyadmin-confirm-drop.png)

   Confirm you want to run the query to drop tables in phpMyAdmin.
5. Click on the **Import** tab and then click the **Choose file/Browse** button. Select your *.sql file, and click **Import**.
   ![Select your .sql file to import in phpMyAdmin.](https://kinsta.com/wp-content/uploads/2026/04/phpmyadmin-import.png)

   Select your .sql file to import in phpMyAdmin.

## Restore a MySQL database using WP-CLI

If your database file is larger than 134 MB, or you’d prefer to use the command line, you can use WP-CLI to restore your database instead.

1. Connect to your site with [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/) and go to the public directory.
2. Upload your database file.
3. Connect to your server [with SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) and navigate to the public directory:

   Copy

   ```
   cd public
   ```
4. Before importing your database, ensure the existing database is empty to prevent data duplication. The following command does that, so you have an empty database to import to (the `--yes` flag answers the confirmation message without a separate prompt):

   Copy

   ```
   wp db reset --yes
   ```
5. Import your database file (replace **db-backup-name.sql** with the actual file name):

   Copy

   ```
   wp db import db-backup-name.sql
   ```
6. Once your database is imported, delete the database file from the server using either your FTP client or via SSH with this command:

   Copy

   ```
   rm db-backup-name.sql
   ```
