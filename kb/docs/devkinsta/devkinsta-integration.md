---
url: "https://kinsta.com/docs/devkinsta/devkinsta-integration/"
title: "Kinsta Integration"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-integration"
section: ["DevKinsta"]
kinsta_last_updated: "2024-08-19T12:36:52"
change_signal: "2024-08-19T12:36:52"
fetched_at: "2026-10-07T22:58:20Z"
sha256: "82a7577da11b745250b94d08cb167e56d17aea1955ceacd3eac5605d82799efb"
body_chars: 8874
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Kinsta Integration

**Section:** DevKinsta
**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-integration/
**Kinsta last updated:** 2024-08-19T12:36:52

## On this page

- [Pull a site from Kinsta](#pull-a-site-from-kinsta)
- [Push changes to staging](#push-changes-to-staging)
    - [Pushing your changes to staging will:](#pushing-your-changes-to-staging-will)
    - [Won’t change:](#wont-change)
- [Create a site from a backup](#create-a-site-from-a-backup)
  - [Creating a backup](#creating-a-backup)
  - [Creating a site from a backup in DevKinsta](#creating-a-site-from-a-backup-in-devkinsta)
- [Manually import a backup](#manually-import-a-backup)
  - [Creating a backup](#creating-a-backup)
  - [Creating a site in DevKinsta](#creating-a-site-in-devkinsta)
  - [Importing your content](#importing-your-content)
  - [Importing your database](#importing-your-database)
  - [Search and replace](#search-and-replace)

---

This article explains how you can integrate your WordPress sites hosted on MyKinsta into DevKinsta, including how to pull your WordPress site from Kinsta, how to push your changes from DevKinsta to MyKinsta, and how to create a site from a WordPress backup.

## Pull a site from Kinsta

If you have a [Kinsta](https://kinsta.com) account, you can pull your sites into DevKinsta. To import a new site in DevKinsta, see the [Import from MyKinsta section](https://kinsta.com/docs/devkinsta/devkinsta-getting-started/creating-a-site#import-from-mykinsta) of our Creating a Site With DevKinsta guide.

1. Select the site you want to pull to in DevKinsta.
2. Click the **Sync** button and select **Pull from Kinsta** in the dropdown menu.
3. If you are not already logged in to your MyKinsta account in your [DevKinsta settings](https://kinsta.com/docs/devkinsta/settings), you’ll be prompted to log in (and [provide 2FA](https://kinsta.com/docs/user-settings/logging-in/#enable-two-factor-authentication-2-fa) if it’s enabled).
4. Select the environment (Live, [Standard Staging](https://kinsta.com/docs/wordpress-hosting/staging-environment/), or [Premium Staging](https://kinsta.com/docs/wordpress-hosting/staging-environment/#premium-staging-environments)) you want to pull from.
5. You can choose what to pull from your hosted site to your DevKinsta site:
   - only the selected files,
   - only the database,
   - or both.
6. Click **Update local site** to begin the pull process.

As an alternative backup method, when you pull a site into DevKinsta, you can make a local backup of the site using the following command:

```
docker exec -it devkinsta_fpm bash -c "cd /www/kinsta/public/SITENAME && wp db export --allow-root"
```

## Push changes to staging

When pushing changes from DevKinsta to MyKinsta, you can only push to a Standard or Premium Staging Environment; **you can’t push to a live site directly from DevKinsta**. Once you’ve pushed your changes from DevKinsta to a staging environment, you can then [push from staging to live](https://kinsta.com/docs/wordpress-hosting/staging-environment/#push-staging-to-live-1) in MyKinsta.

1. Select the site you want to push from in DevKinsta.
2. Click the **Sync** button and select **Push to Kinsta** in the dropdown menu.
3. If you are not currently logged in to your MyKinsta account in your DevKinsta settings, you’ll be prompted to log in (and [provide 2FA](https://kinsta.com/docs/user-settings/logging-in/#enable-two-factor-authentication-2-fa) if it’s enabled).
4. Select the environment you want to push your changes to.
5. You can choose what to pull from your hosted site to your DevKinsta site:
   - only the selected files,
   - only the database,
   - or both.
6. Click **Push site** to begin pushing your changes.

#### Pushing your changes to staging will:

- Overwrite all files, if selected.
- Overwrite the database, if selected.
- Change the Site URL from local to the primary domain of the staging environment you’re pushing to.
- Push every existing WordPress user from the DevKinsta site if **database** is selected.

#### Won’t change:

- [MySQL (database) password](https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database-access/).
- [MyKinsta redirects](https://kinsta.com/docs/wordpress-hosting/redirect-rules/).
- [PHP version](https://kinsta.com/docs/devkinsta/devkinsta-site-management/php-versions).

## Create a site from a backup

If you have a backup of a WordPress site you’d like to bring into DevKinsta, you can now create a site from a backup file right from within DevKinsta.

Make sure the backup file contains all of your site’s WordPress files and your database (.sql) file. If your backup doesn’t contain a complete WordPress site, follow the steps in our [Manually Import a Backup](#manually-import-a-backup) guide instead.

### Creating a backup

The first thing you’ll need is a backup of the site you want to add in DevKinsta. If the site is hosted at Kinsta, log in to [MyKinsta](https://my.kinsta.com/) and go to**Sites** > ***sitename*** > **Backups** > **Download** to create and [download a backup](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#downloadable-backups) of the site.

### Creating a site from a backup in DevKinsta

Once you have your backup file, [create a custom site](https://kinsta.com/docs/devkinsta/devkinsta-getting-started/creating-a-site) in DevKinsta and select the **Import backup** tab.

![Create a custom site and import your backup in DevKinsta.](https://kinsta.com/wp-content/uploads/2023/11/devkinsta-import-backup.png)

Create a custom site and import your backup in DevKinsta.

Enter your site details and click the **Create site** button. If you do not know the database name, there are a couple of ways you can find that information:

- If your site is hosted at Kinsta, log in to [MyKinsta](https://my.kinsta.com/), go to**Sites** > ***sitename*** > **Info** and look for the database name under **Database access**.
- Unpack the backup file and look for the name of the database (**.sql**) file or look for the database name in the **wp-config.php** file.

A search and replace to update the URLs in the database to your local site’s URL is automatically performed during the site creation. Once the site is created, you’re ready to begin [using your local site](https://kinsta.com/docs/devkinsta/devkinsta-site-management).

## Manually import a backup

If you have an incomplete backup or have any trouble [creating a site from a backup](#create-a-site-from-a-backup), you can use the manual process described below.

### Creating a backup

One of the easiest ways to import a site is to create a downloadable backup. If the site you want to import is hosted with Kinsta, visit the Backups page of your chosen site (**Sites** > ***sitename*** > **Backups**) and head over to the **Download** tab to [create a downloadable backup](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#downloadable-backups). This may take a while if you have a large site, but once the download is ready, you’ll get a message in MyKinsta and an **email with a download link**.

![Download a backup from MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-download-backups.png)

Download a backup from MyKinsta.

Once the backup is downloaded, extract it on your local computer.

### Creating a site in DevKinsta

Create a site in DevKinsta (see our [site creation guide](https://kinsta.com/docs/devkinsta/devkinsta-getting-started/creating-a-site)) as usual. Once created, you’ll see the site path, which you can click to open.

![DevKinsta site information.](https://kinsta.com/wp-content/uploads/2023/11/devkinsta-dashboard.png)

DevKinsta site information.

### Importing your content

Once you open the site path, you’ll see a standard WordPress directory structure. Delete the **wp-content** folder and then move the **wp-content** folder from your extracted backup in its place. This will ensure that the themes, plugins, and media from the imported site are in place.

### Importing your database

In DevKinsta, click the **Database manager** button to open your local database. Make sure the correct database is selected in the top left in Adminer (the database manager). In the main screen that shows the table list, click the checkbox on the left in the top row of the table list. This will select all tables.

![Select all tables in Adminer.](https://kinsta.com/wp-content/uploads/2021/01/site-import-adminer-1024x1020.png "Select all tables in Adminer.")

Select all tables in Adminer.

Click the **Drop** button and confirm to delete all database tables from your local site’s database. Next, click the **Import** button in the sidebar, and in the **File upload** section, select the **mysql-database-backup.sql** (or similar) file from your downloaded backup and click **Execute**. This will import your database.

### Search and replace

Since the database is from a hosted site, there will be a lot of references to your site’s URL within the database. To ensure this doesn’t cause any issues, you’ll need to run a search and replace to update those URLs in your database.

You can do so with any of the following tools:

- [interconnect/it Search Replace DB PHP Script](https://interconnectit.com/search-and-replace-for-wordpress-databases/)
- [WP-CLI](https://kinsta.com/docs/devkinsta/wp-cli)
- a plugin like [Better Find and Replace](https://wordpress.org/plugins/real-time-auto-find-and-replace/)

For more info about using WP-CLI and how to search and replace URLs, check out these guides:

- [WP-CLI v2 – Managing WordPress From the Terminal](https://kinsta.com/blog/wp-cli/)
- [How to Perform a WordPress Search and Replace](https://kinsta.com/blog/wordpress-search-and-replace/)
