---
url: "https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-users/"
title: "WordPress Users"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "site-management"
section: ["WordPress Hosting", "Site Management"]
kinsta_last_updated: "2026-10-22T13:48:55"
change_signal: "2026-10-22T13:48:55"
fetched_at: "2026-11-11T13:03:01Z"
sha256: "28dc754bc6a755c2e5b7743a270e02f7e5b534949964d943fffdbd22eb645e2c"
body_chars: 17527
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# WordPress Users

**Section:** WordPress Hosting > Site Management
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-users/
**Kinsta last updated:** 2026-10-22T13:48:55

## On this page

- [User roles and capabilities](#user-roles-and-capabilities)
- [Add a user](#add-a-user)
  - [Add a user in WP Admin](#add-a-user-in-wp-admin)
  - [Add a user in the database manager](#add-a-user-in-the-database-manager)
  - [Add a user in phpMyAdmin](#add-a-user-in-phpmyadmin)
  - [Add a user in WP-CLI](#add-a-user-in-wp-cli)
- [Manage users](#manage-users)
  - [Manage a user in WP Admin](#manage-a-user-in-wp-admin)
  - [Manage a user in the database manager](#manage-a-user-in-the-database-manager)
  - [Manage a user in phpMyAdmin](#manage-a-user-in-phpmyadmin)
  - [Manage a user in WP-CLI](#manage-a-user-in-wp-cli)
- [Delete a user](#delete-a-user)
  - [Delete a user in WP Admin](#delete-a-user-in-wp-admin)
  - [Delete a user in the database manager](#delete-a-user-in-the-database-manager)
  - [Delete a user in phpMyAdmin](#delete-a-user-in-phpmyadmin)
  - [Delete a user in WP-CLI](#delete-a-user-in-wp-cli)
- [Two-factor authentication](#two-factor-authentication)
  - [Choose a 2FA plugin](#choose-a-2fa-plugin)
  - [Set up 2FA with Google Authenticator](#set-up-2fa-with-google-authenticator)
  - [Regain access if you’re locked out](#regain-access-if-youre-locked-out)

---

[Kinsta’s user roles](https://kinsta.com/docs/company-settings/user-management/) allow you to manage what users have access to within MyKinsta. WordPress user roles allow you to manage what users can do on your WordPress site, such as adding new posts or pages, moderating comments, installing plugins, etc. For a full guide on how WordPress user roles and capabilities work, refer to [The Ultimate Guide to WordPress User Roles and Capabilities](https://kinsta.com/blog/wordpress-user-roles/).

## User roles and capabilities

Capabilities are the actions that users can perform within WordPress, such as:

- Read posts ([read](https://wordpress.org/support/article/roles-and-capabilities/#read))
- Write and edit posts ([edit_posts](https://wordpress.org/support/article/roles-and-capabilities/#edit_posts))
- Publish posts ([publish_posts](https://wordpress.org/support/article/roles-and-capabilities/#publish_posts))
- Install plugins ([install_plugins](https://wordpress.org/support/article/roles-and-capabilities/#install_plugins))
- Delete themes ([delete_themes](https://wordpress.org/support/article/roles-and-capabilities/#delete_themes))
- Create users ([create_users](https://wordpress.org/support/article/roles-and-capabilities/#create_users))
- Moderate comments ([moderate_comments](https://wordpress.org/support/article/roles-and-capabilities/#moderate_comments))

Roles are a predefined set of capabilities; when you add a new user to WordPress, you must assign them to a role. By default, WordPress includes 5 predefined user roles:

- **Administrator:** This is the highest level of access and allows users to perform actions such as, create and delete users, reset passwords, install and manage themes and plugins.
- **Editor:**This role is for users who manage your site’s content; it allows them to create, modify, publish, and delete posts and pages.
- **Author:** Users assigned to this role can create, edit, and publish posts, upload media files, and delete their own posts. They cannot create new pages or delete other users’ posts.
- **Contributor:**Users assigned to this role can create draft posts and delete their own drafts, but they cannot publish posts.
- **Subscriber:** This is the lowest level of access and allows users to manage their WordPress profile and read all of the posts on your site.

For a full list of roles and capabilities, refer to the [WordPress Roles and Capabilities page](https://wordpress.org/documentation/article/roles-and-capabilities).

## Add a user

### Add a user in WP Admin

1. Open WP Admin from [MyKinsta](https://my.kinsta.com/), click**Sites** > ***sitename*** > **Info** > **Open WP Admin**.
2. Within WP Admin, click **Users** > **Add New User**, complete the fields as required, choose a user **Role**, and click **Add New User**.

   ![Add a new WordPress user in WP Admin. ](https://kinsta.com/wp-content/uploads/2024/05/wordpress-add-user-987x1024.png)

   Add a new WordPress user in WP Admin.

### Add a user in the database manager

This method requires directly editing your WordPress site’s database, so we only recommend it if you are comfortable using the [database manager](https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database-access/#database-manager). We also recommend [backing up your database](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/) before making any changes.

1. In MyKinsta, go to **Sites** > ***sitename*** > **Database** > **Open database**, and then click the `wp_users` table.

   ![wp_users table in the database manager.](https://kinsta.com/wp-content/uploads/2024/05/wordpress-database-wp-users.png)

   wp_users table in the database manager.
2. Click **SQL console** and enter the following command, replacing the `VALUES` with the new user details:

   ```
   INSERT INTO `wp_users` (`user_login`, `user_pass`, `user_nicename`, `user_email`, `user_status`) VALUES ('your username', MD5('your password'), 'your firstname & your lastname', 'your email', '0')
   ```
3. Click **Run**, and then enter the following commands; this gives the user administrator privileges. You can change this after the user is created within WP Admin:

   ```
   INSERT INTO `wp_usermeta` (`umeta_id`, `user_id`, `meta_key`, `meta_value`) VALUES (NULL, (Select max(id) FROM wp_users), 'wp_capabilities', 'a:1:{s:13:"administrator";s:1:"1";}');

   INSERT INTO `wp_usermeta` (`umeta_id`, `user_id`, `meta_key`, `meta_value`) VALUES (NULL, (Select max(id) FROM wp_users), 'wp_user_level', '10');
   ```

### Add a user in phpMyAdmin

This method requires directly editing your WordPress site’s database, so we only recommend it if you are comfortable [working with phpMyAdmin](https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database-access/). We also recommend [backing up your database](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/) before making any changes. 

1. Open phpMyAdmin from [MyKinsta](https://my.kinsta.com/), click**Sites** > ***sitename*** > **Info**, and within **Database access**, click **Open phpMyAdmin**. If you are prompted for a username and password, use your **Database username** and **Database password** from MyKinsta to log in.
2. Within phpMyAdmin, click your ***sitename*** and then click the `wp_users` table.

   ![Select the wp_users table within phpMyAdmin. ](https://kinsta.com/wp-content/uploads/2024/05/phpmyadmin-wp_users.png)

   Select the wp_users table within phpMyAdmin.
3. Click **SQL** and enter the following command, replacing the `VALUES` with the new user details:

   ```
   INSERT INTO `wp_users` (`user_login`, `user_pass`, `user_nicename`, `user_email`, `user_status`) VALUES ('your username', MD5('your password'), 'your firstname & your lastname', 'your email', '0')
   ```
4. Click **Go**, click back to the **SQL** tab, and enter the following commands; this gives the user administrator privileges. You can change this after the user is created within WP Admin:

   ```
   INSERT INTO `wp_usermeta` (`umeta_id`, `user_id`, `meta_key`, `meta_value`) VALUES (NULL, (Select max(id) FROM wp_users), 'wp_capabilities', 'a:1:{s:13:"administrator";s:1:"1";}');

   INSERT INTO `wp_usermeta` (`umeta_id`, `user_id`, `meta_key`, `meta_value`) VALUES (NULL, (Select max(id) FROM wp_users), 'wp_user_level', '10');
   ```

### Add a user in WP-CLI

This method requires directly editing your WordPress site’s database, so we recommend it only if you are comfortable working with the command line. We also recommend [backing up your database](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/) before making any changes. 

1. Connect to your server [with SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) and navigate to the public directory:

   ```
   cd public
   ```
2. Run the following command, replacing the `$username` and `$emailaddress` with the new user details and `$role` with the role you want to assign the new user to, for example, administrator:

   ```
   wp user create $username $emailaddress --role=$role
   ```

   For example:

   ```
   wp user create newuser user@example.com --role=administrator
   ```

   When the command completes, it returns a password for the new user.

## Manage users

When you add users, they are stored in your [WordPress database](https://kinsta.com/docs/wordpress-hosting/database-management). A user with administrator access can edit all of the user fields within WP Admin, with the exception of the username. You can delete a user and create a new one to change the username, or if you want to edit the username, you must do this directly within the database with phpMyAdmin.

### Manage a user in WP Admin

1. Open WP Admin from [MyKinsta](https://my.kinsta.com/), click**Sites** > ***sitename*** > **Info** > **Open WP Admin**.
2. Within WP Admin, click **Users**, hover over the user you want to edit, and click **Edit.**

   ![Edit a WordPress user in WP Admin.](https://kinsta.com/wp-content/uploads/2024/05/wordpress-edit-users-1024x319.png)

   Edit a WordPress user in WP Admin.

### Manage a user in the database manager

This method requires directly editing your WordPress site’s database, so we only recommend it if you are comfortable using the [database manager](https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database-access/#database-manager). We also recommend [backing up your database](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/) before making any changes.

1. In MyKinsta, go to **Sites** > ***sitename*** > **Database** > **Open database**, and then click the `wp_users` table.

   ![wp_users table in the database manager.](https://kinsta.com/wp-content/uploads/2024/05/wordpress-database-wp-users.png)

   wp_users table in the database manager.
2. Double-click the field you want to change. When you have made the changes, press Enter, and then click **Save**.

   ![Save your changes to the database. ](https://kinsta.com/wp-content/uploads/2024/05/wordpress-save-changes-database.png)

   Save your changes to the database.

### Manage a user in phpMyAdmin

This method requires directly editing your WordPress site’s database, so we only recommend it if you are comfortable [working with phpMyAdmin](https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database-access/). We also recommend [backing up your database](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/) before making any changes. 

1. Open phpMyAdmin from [MyKinsta](https://my.kinsta.com/), click **Sites** > ***sitename*** > **Info;** within **Database access**, click **Open phpMyAdmin**. If you are prompted for a username and password, use your **Database username** and **Database password** from MyKinsta to log in.
2. Within phpMyAdmin, click your ***sitename*** and then click the `wp_users` table.

   ![Select the wp_users table within phpMyAdmin. ](https://kinsta.com/wp-content/uploads/2024/05/phpmyadmin-wp_users.png)

   Select the wp_users table within phpMyAdmin.
3. Click **Edit** on the user you want to change, or double-click the field you want to change.

   ![Edit a user within the wp_users table in phpMyAdmin. ](https://kinsta.com/wp-content/uploads/2024/05/phpmyadmin-edit-user.png)

   Edit a user within the wp_users table in phpMyAdmin.

### Manage a user in WP-CLI

This method requires directly editing your WordPress site’s database, so we recommend it only if you are comfortable working with the command line. We also recommend [backing up your database](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/) before making any changes. 

1. Connect to your server [with SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) and navigate to the public directory:

   ```
   cd public
   ```
2. Run the following command, replacing `$user` with the username, `$field` with the field you want to update, `$value` with the new data you want to enter:

   ```
   wp user update $user -—$field=$value
   ```

   For example, to replace the email on the Kinsta user with example@kinsta.com, you would use the following:

   ```
   wp user update Kinsta -—user_email=example@kinsta.com
   ```

## Delete a user

### Delete a user in WP Admin

1. Open WP Admin from [MyKinsta](https://my.kinsta.com/), click **Sites** > ***sitename*** > **Info** > **Open WP Admin**.
2. Within WP Admin, click **Users**, hover over the user you want to remove, and click **Delete.**

   ![Delete a WordPress user in WP Admin. ](https://kinsta.com/wp-content/uploads/2024/05/wordpress-delete-users-1024x319.png)

   Delete a WordPress user in WP Admin.

### Delete a user in the database manager

This method requires directly editing your WordPress site’s database, so we only recommend it if you are comfortable using the [database manager](https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database-access/#database-manager). We also recommend [backing up your database](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/) before making any changes.

1. In MyKinsta, go to **Sites** > ***sitename*** > **Database** > **Open database**, and then click the `wp_users` table.

   ![wp_users table in the database manager.](https://kinsta.com/wp-content/uploads/2024/05/wordpress-database-wp-users.png)

   wp_users table in the database manager.
2. Select the user you want to delete and click **Delete record**.

   ![Delete a record in the database manager.](https://kinsta.com/wp-content/uploads/2024/05/wordpress-delete-database.png)

   Delete a record in the database manager.

### Delete a user in phpMyAdmin

This method requires directly editing your WordPress site’s database, so we only recommend it if you are comfortable [working with phpMyAdmin](https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database-access/). We also recommend [backing up your database](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/) before making any changes. 

1. Open phpMyAdmin from [MyKinsta](https://my.kinsta.com/), click**Sites** > ***sitename*** > **Info;** within **Database access**, click **Open phpMyAdmin**. If you are prompted for a username and password, use your **Database username** and **Database password** from MyKinsta to log in.
2. Within phpMyAdmin, click your ***sitename*** and then click the `wp_users` table.

   ![Select the wp_users table within phpMyAdmin. ](https://kinsta.com/wp-content/uploads/2024/05/phpmyadmin-wp_users.png)

   Select the wp_users table within phpMyAdmin.
3. Click **Delete** on the user you want to remove.

   ![Delete a user within the wp_users table in phpMyAdmin.](https://kinsta.com/wp-content/uploads/2024/05/phpmyadmin-delete-user.png)

   Delete a user within the wp_users table in phpMyAdmin.

### Delete a user in WP-CLI

This method requires directly editing your WordPress site’s database, so we recommend it only if you are comfortable working with the command line. We also recommend [backing up your database](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/) before making any changes.

1. Connect to your server [with SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) and navigate to the public directory:

   ```
   cd public
   ```
2. Run the following command, replacing `$username` with the username you want to delete:

   ```
   wp user delete $username
   ```

   This also deletes all of their posts. If you want to remove the user and reassign the posts to another user, use the following command, replacing `$username` with the username you want to delete and `$anotherusername` with the username you want to assign the posts to:

   ```
   wp user delete $username --reassign=$anotherusername
   ```

## Two-factor authentication

Two-factor authentication (2FA) adds a second step when users log in to WP Admin. After entering their password, they must enter a time-based code from an authenticator app on their phone. WordPress doesn’t include 2FA by default, so you need a plugin.

This is separate from 2FA for your MyKinsta account. For details, refer to [Logging In](https://kinsta.com/docs/user-settings/logging-in/).

### Choose a 2FA plugin

We recommend one of the following plugins:

- **[Two Factor Authentication](https://wordpress.org/plugins/two-factor-authentication/):** Supports TOTP and HOTP, so it works with apps such as Google Authenticator and Authy. It works with WooCommerce and Affiliates-WP login forms, and with [WordPress Multisite](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/multisite-network/) when network activated. The premium version adds emergency codes.
- **[WP 2FA](https://wordpress.org/plugins/wp-2fa/):** The free version lets you require 2FA for users, provides backup codes to prevent lockouts, and works with third-party plugins and themes. Premium and Enterprise versions add 2FA policies by user role, YubiKey authentication, trusted devices, and white labeling.
- **[Google Authenticator](https://wordpress.org/plugins/google-authenticator/):** A free, lightweight plugin with no user limits. You can enable 2FA per user, for example, for administrators only. It doesn’t support backup codes.

### Set up 2FA with Google Authenticator

1. Open WP Admin from [MyKinsta](https://my.kinsta.com/), click **Sites** > ***sitename*** > **Info** > **Open WP Admin**.
2. Within WP Admin, click **Plugins** > **Add New Plugin**, search for **Google Authenticator**, click **Install Now**, and then click **Activate**.
3. Click **Users** > **Profile**, scroll to the **Google Authenticator Settings** section, and select **Active**.
4. Enter a **Description** to identify the site in your authenticator app. Then scan the QR code with an authenticator app, such as Google Authenticator for Android or iOS, or enter the secret key manually.
5. Click **Update Profile**.

The next time you log in, the WordPress login page shows an extra field for the code from your authenticator app. Each user must complete these steps from their own profile.

### Regain access if you’re locked out

If you can’t log in because you’ve lost access to your authenticator app, disable the plugin by renaming or deleting its folder in wp-content/plugins/. You can do this with [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/) or the [File Manager](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-file-manager/). You can then log in with your username and password and set up 2FA again.
