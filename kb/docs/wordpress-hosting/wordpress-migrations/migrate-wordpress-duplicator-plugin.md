---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrate-wordpress-duplicator-plugin/"
title: "Migrations - Duplicator Migration"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-migrations"
section: []
kinsta_last_updated: "April 20, 2026"
sitemap_lastmod: "2026-04-20T08:34:59+00:00"
fetched_at: "2026-10-07T22:38:33Z"
sha256: "44dc2dad4cb77bba6c227df9f6fb632b8f598b72a75115ebf04e2ce0659372cc"
body_chars: 11934
extracted_with: "main article"
status: "live"
---

# Migrations - Duplicator Migration

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrate-wordpress-duplicator-plugin/
**Kinsta last updated:** April 20, 2026

## On this page

- [Overview of Duplicator migration](#overview-of-duplicator-migration)
- [Preparing for the migration](#preparing-for-the-migration)
  - [Migrating a multisite](#migrating-a-multisite)
  - [Create a backup on your current host](#create-a-backup-on-your-current-host)
  - [Create the site on Kinsta](#create-the-site-on-kinsta)
- [Creating the archive](#creating-the-archive)
  - [Disable caching plugins](#disable-caching-plugins)
  - [Install and activate the Duplicator plugin](#install-and-activate-the-duplicator-plugin)
  - [Create the site archive](#create-the-site-archive)
  - [Download the archive and installer file](#download-the-archive-and-installer-file)
- [Restoring the archive](#restoring-the-archive)
  - [Transfer the archive and installer file to Kinsta](#transfer-the-archive-and-installer-file-to-kinsta)
  - [Restore the archive](#restore-the-archive)
  - [Cleaning up the archive files](#cleaning-up-the-archive-files)
- [Previewing your site before updating DNS](#previewing-your-site-before-updating-dns)
- [Updating DNS](#updating-dns)
- [Install Kinsta MU plugin](#install-kinsta-mu-plugin)

---

Some of you may prefer to [migrate your WordPress site](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/wordpress-manual-migration/) yourself, maybe due to sensitive data, or perhaps you just want to do it immediately rather than coordinating with us. For migrating your site to Kinsta, one of the plugins we recommend is the free version of the [WordPress Duplicator plugin](https://wordpress.org/plugins/duplicator/).

However, please note that Duplicator may not be fully compatible with some WordPress sites. Our Support team is always happy to help with basic migration questions but cannot assist with failed migrations after the fact, as this falls outside of the [scope of our support](https://kinsta.com/docs/support/scope-of-support/managed-wordpress-scope-of-support/).

**Kinsta migrations are free**, so if you’re worried about the integrity of your data, we highly recommend [using our professional migration team](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrating-to-kinsta/).

## Overview of Duplicator migration

Duplicator generates two files: a **zip** file containing an archive of all files and the [database](https://kinsta.com/docs/wordpress-hosting/database-management/) and an **installer.php** file that can be used to restore the site using the archive.

Once you’ve generated the archive file and downloaded both the archive file and the **installer.php** file, you simply upload those two files to your new Kinsta site and then run the **installer.php** file by accessing it using your temporary Kinsta URL.

Duplicator will then walk you through the restoration process. During the restoration process, you will be asked for the new database connection details. You will need to copy and paste the database access details found on the **Info** tab for the site in MyKinsta.

Duplicator will then update your **wp-config.php** file and rewrite the URLs in the database with the temporary Kinsta URL (e.g., example.kinsta.cloud). Rewriting the URLs will allow you to test your site as hosted on Kinsta without actually pointing your live site to Kinsta. (We’ll do that at the end once you’ve confirmed the site was migrated without issue, at which point we’ll also reverse the URL rewriting process to swap the temporary URL with your live URL in the database.)

## Preparing for the migration

### Migrating a multisite

If you’re migrating a [WordPress Multisite](https://kinsta.com/wordpress-hosting/multisite/) network, there are a few things you’ll need to consider. If you’re migrating a subdirectory multisite, you’ll need to [contact our Support team](https://kinsta.com/docs/support/contact-support/) so they can enable the necessary Nginx configuration for subdirectory multisite.

We also recommend reviewing the WordPress Duplicator plugin [documentation](https://snapcreek.com/duplicator/docs/moving-a-multisite-install-with-duplicator-pro/) for migrating WordPress Multisite. Other than the additional steps noted in Duplicator’s documentation, the steps below still apply.

### Create a backup on your current host

If your existing web hosting company offers a way to create a full-site backup, go ahead and do that before proceeding with the migration. The migration process itself should not affect your live site, but it doesn’t hurt to create a backup beforehand, and backups are always a good idea.

If your existing web hosting company does not offer the option to create a full-site backup, you can skip this step.

### Create the site on Kinsta

For this migration, you need to create a [new site](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/new-site/) on [MyKinsta](https://my.kinsta.com/). To do this, go to **Sites** and click **Create new site**. In the modal/pop-up that appears, choose **Empty environment** (we’ll be migrating your existing WordPress site over, so there’s no need to install WordPress).

![Add a new site without WordPress (empty environment).](https://kinsta.com/wp-content/uploads/2023/11/wordpress-add-site-empty-4.png)

Add a new site without WordPress (empty environment).

## Creating the archive

The next step is to create an archive of your current site using the Duplicator plugin. In this section, we’ll install the WordPress Duplicator plugin on your site, build an archive package that includes all your files and database, and download the archive and the **installer.php** file.

### Disable caching plugins

Caching can cause problems during migrations, so it’s best to disable any caching plugins (e.g., [Autoptimize](https://kinsta.com/blog/autoptimize-settings/), [W3 Total Cache](https://kinsta.com/blog/w3-total-cache/), etc.) before creating the archive that you’ll transfer to Kinsta. We have a list of [disallowed plugins](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-banned-incompatible-plugins/) that you’ll also want to review.

### Install and activate the Duplicator plugin

On the WordPress Dashboard for the website you want to migrate, navigate to **Plugins** > **Add New** and search for “Duplicator.” Install and activate “Duplicator – WordPress Migration Plugin.”

![Install the WordPress Duplicator plugin](https://kinsta.com/wp-content/uploads/2023/11/duplicator-install.png)

Install the WordPress Duplicator plugin

### Create the site archive

Once you have activated the Duplicator plugin, go to **Duplicator** > **Backups** and click the **Create New** button to create a new archive package.

Follow the prompts through the three steps to build an archive package. In most cases, you should be able to use the default settings.

![Create a new backup in Duplicator.](https://kinsta.com/wp-content/uploads/2023/11/duplicator-backups-1.png)

Create a new backup in Duplicator.

It’s highly recommended that you enable password protection under the **Installer** option.

![Duplicator enable password protection.](https://kinsta.com/wp-content/uploads/2023/11/duplicator-password-protection-1.png)

Duplicator enable password protection.

### Download the archive and installer file

Once the archive package has been built, download both the Archive file and the Installer file to your local computer. You’ll need to upload these files to your new Kinsta site in the next step.

![Download archive and installer files](https://kinsta.com/wp-content/uploads/2023/11/duplicator-installer-archive-1.png)

Download archive and installer files

## Restoring the archive

### Transfer the archive and installer file to Kinsta

The next step is to upload the archive package and the installer file to your new Kinsta site via SFTP (see [how to use SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/)). Upload both files to the **public/** directory. The **public/** directory should be empty. If it’s not empty, you might already have a WordPress installation on this site, and you should remove that before uploading and restoring the archive.

![Upload archive and installer files to server (via SFTP)](https://kinsta.com/wp-content/uploads/2023/11/duplicator-sftp-1024x554.png)

Upload archive and installer files to server (via SFTP)

### Restore the archive

Once you have uploaded the archive file and the installer file, you can run the Duplicator installer by visiting the **installer.php** file in your browser using the [temporary Kinsta URL](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-temporary-url/). You’ll find the temporary Kinsta URL on the **Domains** tab for your site inMyKinsta.

For example, if the temporary URL is **example.kinsta.cloud**, the URL to the installer file that we need to visit is http://example.kinsta.cloud/installer.php.

![Duplicator deployment after visiting the installer.php link. ](https://kinsta.com/wp-content/uploads/2023/11/duplicator-deployment-1024x707.png)

Duplicator deployment after visiting the installer.php link.

In the **Setup** section of the Duplicator deployment, enter the Database details for your new Kinsta site. You’ll find the **Database access** details for your Kinsta site on the **Info** tab for the site inside MyKinsta.

![Database access credentials in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-database-credentials.png)

Database access credentials in MyKinsta.

Click **Validate** to confirm that you have entered the correct Database details on the Duplicator form.

![WordPress Duplicator plugin: install database](https://kinsta.com/wp-content/uploads/2023/11/duplicator-database-credentials-1024x809.png)

WordPress Duplicator plugin: install database

When the database is validated, accept the terms and notices and click **Next**.

![Accept the terms and notices within the Duplicator deployment. ](https://kinsta.com/wp-content/uploads/2023/11/duplicator-accept-terms-1024x858.png)

Accept the terms and notices within the Duplicator deployment.

In the next step, Duplicator will update the database to use the Kinsta temporary URL. This step ensures that you will be able to log in and test the site when the migration is completed. If your existing site is using SSL (HTTPS), please ensure that the temporary URL in the **URL** field is updated to include **https://**.

![WordPress Duplicator plugin: update data](https://kinsta.com/wp-content/uploads/2023/11/duplicator-install-confirmation-1024x633.png)

WordPress Duplicator plugin: update data

Once the Duplicator process has finished, click the **Admin Login** button to log in to your site.

![WordPress Duplicator plugin: test site](https://kinsta.com/wp-content/uploads/2023/11/duplicator-admin-login-1024x559.png)

WordPress Duplicator plugin: test site

![Login to Kinsta temporary URL](https://kinsta.com/wp-content/uploads/2023/11/duplicator-kinsta-cloud-url-1024x541.png)

Login to Kinsta temporary URL

If everything went OK you should see a message indicating a successful migration upon login.

![Successfully migrated with WordPress Duplicator](https://kinsta.com/wp-content/uploads/2023/11/duplicator-successful-migration.png)

Successfully migrated with WordPress Duplicator

### Cleaning up the archive files

Once you have finished restoring the site on Kinsta, it is recommended that you delete the Duplicator archive and installer files for security purposes. If you’d rather not delete them, you can temporarily move them outside the **public/** directory and into the **private/** directory. The following files should be deleted or moved out of the **public** directory:

- **installer-backup.php**
- **installer.php**
- **database.sql**
- **installer-data.sql**
- ***_archive.zip**

## Previewing your site before updating DNS

At this point in the migration process, you should be able to browse and test your site on Kinsta using the temporary Kinsta URL (e.g., http://example.kinsta.cloud/). If there are references to the live domain in the database or files that give you trouble with that, check out our article on how to [preview your site with our Site Preview tool](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/site-preview/) before updating DNS.

## Updating DNS

When you’re ready to point your domain at Kinsta, you’ll need to update the DNS for your domain to point it at the Kinsta IP address as outlined in our [Add a Domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/) article.

## Install Kinsta MU plugin

Our [Kinsta MU plugin](https://kinsta.com/docs/wordpress-hosting/kinsta-mu-plugin/) is automatically installed on fresh WordPress installations done here at Kinsta. However, since you’ve migrated your site yourself and site files were overwritten (including this plugin), you’ll need to download and install the Kinsta MU plugin manually. This includes our full-page caching and other functionality, such as the ability to deploy [Kinsta’s CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/).
