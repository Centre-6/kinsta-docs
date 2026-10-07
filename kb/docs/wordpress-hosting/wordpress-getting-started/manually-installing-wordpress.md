---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/manually-installing-wordpress/"
title: "Manual Install"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-getting-started"
section: ["WordPress Hosting", "Get Started"]
kinsta_last_updated: "2025-06-30T13:23:40"
change_signal: "2025-06-30T13:23:40"
fetched_at: "2026-10-07T22:58:21Z"
sha256: "8a941c0c63f22eb8117da2eab76058f5c7880fa1ff3b4f76a37e439f7533bc85"
body_chars: 7447
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Manual Install

**Section:** WordPress Hosting > Get Started
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/manually-installing-wordpress/
**Kinsta last updated:** 2025-06-30T13:23:40

## On this page

- [Install WordPress using WP-CLI](#install-wordpress-using-wp-cli)
- [Install WordPress using SFTP](#install-wordpress-using-sftp)
- [Replace temporary URL with a custom domain](#replace-temporary-url-with-a-custom-domain)

---

If you choose the option to not install WordPress (empty environment) when [adding a site](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/new-site/), you can install WordPress manually. This is helpful if you want to run an older version of WordPress to test something like a plugin or theme.

## Install WordPress using WP-CLI

1. Connect to your site’s server [with SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) and navigate to the site’s document root:

   ```
   cd public
   ```
2. Download the latest version of WordPress with:

   ```
   wp core download
   ```
3. Before we can install WordPress, we need to create the **wp-config.php** file and configure the database settings in it. For that, we’ll need the database name, database username, and database password. These details can be found in your site’s **Info** tab in MyKinsta.
   ![Database access credentials in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-database-credentials.png)

   Database access credentials in MyKinsta.

   The following command will prompt you for the database password (more secure than it possibly being stored in bash history). Replace “yourdbname” and “yourdbuser” with your site’s database name and database username from MyKinsta:

   ```
   wp config create --dbname=yourdbname --dbuser=yourdbuser --prompt=dbpass
   ```

   When prompted, enter the database password, and your **wp-config.php** file will be generated.
4. Now you’re ready to install WordPress. Update the following command with your site’s domain (or [temporary URL](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-temporary-url/) if you haven’t added a custom domain yet), title, your preferred admin username, and admin email address. When prompted for the password, enter a unique and strong password.

   ```
   wp core install --url=example.com --title="Your New WordPress Site" --admin_user=youruser --prompt=admin_password --admin_email=yourname@yourdomain.com
   ```
5. **Optional**: The core install command installs the latest version of WordPress. If you’d like to downgrade WordPress for testing, use this command, replacing the version number with your desired version:

   ```
   wp core update --version=5.7.3 --force
   ```
6. You can now head to your WordPress login page (/wp-admin) and log in.
7. Because WordPress was installed manually, the last step you’ll need to complete is installing the [Kinsta MU plugin](https://kinsta.com/docs/wordpress-hosting/kinsta-mu-plugin#install-the-kinsta-mu-plugin) to ensure your site runs smoothly in our environment.

## Install WordPress using SFTP

1. [Download the version of WordPress](https://wordpress.org/download/releases/) you want to install from WordPress.org, saving it where you can easily find it on your computer.
2. After your download completes, extract the files from the download.

   ![Viewing extracted WordPress core files.](https://kinsta.com/wp-content/uploads/2021/11/wordpress-files.png "Viewing extracted WordPress core files.")

   Viewing extracted WordPress core files.
3. Inside the **wordpress** folder, rename **wp-config-sample.php** to **wp-config.php** and open it with your preferred [text editor](https://kinsta.com/blog/best-text-editors/).
4. To update the file, we need to first copy the database name, database username, and database password from the site’s **Info** tab in MyKinsta.

   ![Database access credentials in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-database-credentials.png)

   Database access credentials in MyKinsta.
5. Update the MySQL settings in **wp-config.php** with those details. Leave the other MySQL settings unchanged.

   ![Updating wp-config.php with database details.](https://kinsta.com/wp-content/uploads/2021/11/mysql-settings-wp-config.png "Updating wp-config.php with database details")

   Updating wp-config.php with database details.
6. Next, generate unique [WordPress salts](https://kinsta.com/blog/wordpress-salts/) with the [WordPress.org secret-key tool](https://api.wordpress.org/secret-key/1.1/salt/) and update your **wp-config.php** file with the new salts and save the file.

   ![New WordPress salts in wp-config.php](https://kinsta.com/wp-content/uploads/2021/11/wordpress-authentication-keys-salts.jpg "New WordPress salts in wp-config.php")

   New WordPress salts in wp-config.php
7. Now, it’s time to upload your WordPress files to your site’s server. To do this, you’ll need to connect to your site [with SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/). Once you’re connected, navigate into the **public** folder/directory. Upload the contents of the **wordpress** folder (but not the folder itself) from your local computer into **public** on the server. Note: You can skip or delete the **readme.html** and **license.txt** files, as these aren’t needed. The upload may take several minutes, depending on the speed of your internet connection.
8. To run the WordPress installer, you’ll need to visit your site. From your site’s **Domains** list in MyKinsta, click **Open URL** next to your Primary Domain.

   ![Open URL link in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-domains-open-url.png)

   Open URL link in MyKinsta.
9. Visiting your site will show the WordPress installer where you can choose the language for your site and click **Continue**.

   ![WordPress installer on website.](https://kinsta.com/wp-content/uploads/2021/11/wordpress-installer-language.jpg "WordPress installer on website")

   WordPress installer on website.
10. Enter your **Site Title**, **Username**, **Password**, **email address**, and choose whether you want to discourage search engines from indexing your site.
    ![Entering site details in WordPress installer.](https://kinsta.com/wp-content/uploads/2021/11/wp-manual-install.jpg "Entering site details in WordPress installer")

    Entering site details in WordPress installer.

    A success message will appear, and you’ll also receive an email with your login URL and username.

    ![Success message from WordPress installer.](https://kinsta.com/wp-content/uploads/2021/11/wp-manual-install-success.jpg "Success message from WordPress installer")

    Success message from WordPress installer.
11. You can now head to your WordPress login page (wp-admin) and log in.
12. The last step you’ll need to complete is installing the [Kinsta MU plugin](https://kinsta.com/docs/wordpress-hosting/kinsta-mu-plugin) to ensure your site runs smoothly in our environment.

## Replace temporary URL with a custom domain

If you install WordPress on the [Kinsta temporary URL](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-temporary-url/) (https://yoursite.kinsta.cloud), you’ll need to update it with your own custom domain.

1. Follow the steps in [Add a domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/) to add and point your domain
2. [Set it as your primary domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/#3-set-your-domain-as-primary) and enable the **Run search and replace** option to update any temporary domain references in your WordPress database.
3. We also recommend forcing your site to [load over HTTPS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/#force-https-optional) for added security.
