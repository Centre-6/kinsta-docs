---
url: "https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/"
title: "SFTP"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "connecting-with-sftp"
section: ["WordPress Hosting"]
kinsta_last_updated: "2026-03-25T10:30:46"
change_signal: "2026-03-25T10:30:46"
fetched_at: "2026-10-07T22:58:18Z"
sha256: "50f15a905b9b07939d020e2714e1cfff1226e3fa40e3c82a9b2aa3aa61f0ee37"
body_chars: 14800
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# SFTP

**Section:** WordPress Hosting
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/
**Kinsta last updated:** 2026-03-25T10:30:46

## On this page

- [SFTP clients](#sftp-clients)
- [Primary SFTP/SSH user](#primary-sftpssh-user)
  - [Download primary SFTP user settings](#download-primary-sftp-user-settings)
  - [Change the primary SFTP/SSH user password](#change-the-primary-sftpssh-user-password)
  - [Set a password expiration for the primary SFTP/SSH user](#set-a-password-expiration-for-the-primary-sftpssh-user)
  - [Authentication methods for primary SFTP/SSH user](#authentication-methods-for-primary-sftpssh-user)
  - [IP allowlist for primary SFTP/SSH user](#ip-allowlist-for-primary-sftpssh-user)
  - [Disable/enable primary SFTP/SSH user access](#disableenable-primary-sftpssh-user-access)
- [Additional SFTP users](#additional-sftp-users)
  - [Important notes](#important-notes)
  - [Edit an SFTP user](#edit-an-sftp-user)
  - [Remove an SFTP user](#remove-an-sftp-user)
  - [Disable/enable additional SFTP users](#disableenable-additional-sftp-users)
- [Client examples](#client-examples)
  - [Cyberduck](#cyberduck)
  - [WinSCP](#winscp)
  - [FileZilla](#filezilla)
  - [Transmit](#transmit)
- [More information](#more-information)

---

To ensure your data remains safe and encrypted, Kinsta only supports SFTP connections. When you’re connected to a WordPress site via SFTP, you gain direct access to the files and folders on the server, allowing you to perform a variety of tasks that can be especially useful for troubleshooting, customizing, or managing your site, such as:

- Upload, download, and edit files.
- Manage your plugins and themes.
- Fix errors and restore access.
- Back up your site.
- Delete files.
- Manage permissions.

MyKinsta includes a [primary SFTP user](#ssh-sftp-superuser) with full access to all files and directories on your WordPress site. You can also create [additional SFTP users](#additional-sftp-users) with customizable permissions, including read-and-write or read-only access. You can also restrict their access to a specific subdirectory, giving you greater control over who can access different parts of your site.

## SFTP clients

If you don’t already have an SFTP client installed on your computer, we recommend one of the following:

- [Cyberduck](https://cyberduck.io/) (Free — macOS or Windows)
- [WinSCP](https://winscp.net/eng/download.php) (Free — Windows)
- [FileZilla](https://filezilla-project.org/) (Free — macOS, Windows, or Linux)
- [Transmit](http://www.panic.com/transmit/) (Premium — macOS)

You can connect via SFTP with your SFTP client using the [primary SFTP/SSH user](#ssh-sftp-superuser) or one of the [Additional SFTP users](#additional-sftp-users).

## Primary SFTP/SSH user

The Primary SFTP/SSH user has full read and write access to all files and folders on your WordPress site. The credentials you need to access your site via SFTP can be found in MyKinsta under **Sites** > ***sitename*** > **Info** > **Primary SFTP/SSH user**.

Kinsta only supports SFTP connections; therefore, you should ensure the connection type is always SFTP. The **Host** may be described as the Address, URL, or Hostname within the SFTP client.

You can also use an [SSH key](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/#how-to-connect-to-ssh-with-ssh-keys) in addition to your username and password.

![Primary SFTP/SSH user details in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-ssh-info-1.png)

Primary SFTP/SSH user details in MyKinsta.

Some SFTP clients may default to FTP as the connection type, so be sure SFTP is selected as the connection type. If you don’t, you might see an error similar to:

> Cannot establish FTP connection to an SFTP server. Please select proper protocol.

### Download primary SFTP user settings

Rather than manually inputting your SFTP settings, you can download a configuration file that contains all of the Primary SFTP user settings required for the SFTP connection for FileZilla, Cyberduck, or Terminus. In MyKinsta, under **Sites** > ***sitename*** > **Info** > **Primary SFTP/SSH user**, click the download icon under **FTP client config files**.

![Download a zip file of your primary SFTP user settings.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-download-ftp-config.png)

Download a zip file of your primary SFTP user settings.

This downloads a zip file that contains the following files:

- **.xml** – This can be used to import the SFTP settings into FileZilla. For support with the import, refer to [FileZilla’s documentation](https://filezillapro.com/docs/server/advanced-options/how-to-export-and-import-server-configurations/).
- **.duck** – This can be used with Cyberduck. If you open the file, it starts the Cyberduck application and creates the connection. If you need further support with this, refer to [Cyberduck’s documentation](https://docs.cyberduck.io/cyberduck/connection/).
- **.csv** – This can be used to import the SFTP settings into Terminus. For support with the import, refer to [Terminus support](https://docs.termius.com/getting-started/import-existing-hosts/).

### Change the primary SFTP/SSH user password

If you want to update the primary SFTP/SSH user password for the current environment, hover over the password and click **Generate new SFTP password**.

![Generate a new SFTP/SSH password for your primary user on your WordPress site.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-new-password.png)

Generate a new SFTP/SSH password for your primary user on your WordPress site.

To confirm the password change, click **Generate new password**.

![Confirm the password change by clicking Generate new password.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-generate-new-password-1024x324.png)

Confirm the password change by clicking Generate new password.

Copy and paste the new password into your [SFTP client](https://kinsta.com/blog/best-ftp-clients/) as needed.

### Set a password expiration for the primary SFTP/SSH user

If you want the primary SFTP/SSH user password to expire and regenerate automatically at regular intervals for the current environment, click the edit icon under **Password expiration**.

![Change the primary STFP/SSH user password expiration time.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-password-expiration-1.png)

Change the primary STFP/SSH user password expiration time.

Choose how often you want the password to expire and regenerate, and click **Save changes**.

![Choose the interval for the password expiration. ](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-change-password-expiration-1024x488.png)

Choose the interval for the password expiration.

### Authentication methods for primary SFTP/SSH user

To change the primary SFTP/SSH user authentication methods to enable or disable access with a username and password for the current environment, click the edit icon under **Authentication methods**.

![Change the primary SFTP/SSH user authentication methods.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-authentication-methods.png)

Change the primary SFTP/SSH user authentication methods.

Select **Password** to enable or disable primary SFTP/SSH user access with a username and password, and click **Save changes**. You cannot disable access using an SSH key; however, you can [disable all SFTP/SSH access](#disableenable-ftpssh-access).

![Select Password to enable or disable access with a username and password.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-change-authentication-method-1024x500.png)

Select Password to enable or disable access with a username and password.

### IP allowlist for primary SFTP/SSH user

To specify a list of IP addresses that are allowed to access your environment with the primary SFTP/SSH user credentials via STFP/SSH, click the edit icon under **IP allowlist**.

![Specify which IP addresses can access the environment via SFTP/SSH.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-ip-allowlist.png)

Specify which IP addresses can access the environment via SFTP/SSH.

Enter the IP addresses you want to allow access via SFTP/SSH and click **Add**. You can specify multiple addresses separated by a comma, e.g., 1.1.1.1, 2.2.2.2. You can also specify a range of IP addresses using a slash, e.g., 1.1.1.1/32.

![Specify the IP addresses that are allowed to access your environment via SFTP/SSH.](https://kinsta.com/wp-content/uploads/2024/06/wordpress-specify-IP-address-1024x430.png)

Specify the IP addresses that are allowed to access your environment via SFTP/SSH.

Once you have entered all of the required IP addresses, click **Update IP allowlist**.

![Update the IP allowlist for SFTP/SSH.](https://kinsta.com/wp-content/uploads/2024/06/wordpress-sftp-update-ip-allowlist-1024x686.png)

Update the IP allowlist for SFTP/SSH.

### Disable/enable primary SFTP/SSH user access

If you want to disable the primary SFTP/SSH user access so users with the primary user credentials cannot connect via SFTP/SSH within **Primary SFTP/SSH user**, click **Disable**.

![Disable primary SFTP/SSH user access.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-disable-1.png)

Disable primary SFTP/SSH user access.

To confirm the changes, click **Disable Primary SFTP/SSH access**.

![Confirm the changes to disable SFTP/SSH access.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-disable-sftp-confirm.png)

Confirm the changes to disable SFTP/SSH access.

When primary SFTP/SSH access is disabled, the connection details are no longer shown.

![Primary SFTP/SSH access disabled.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-disabled-sftp.png)

Primary SFTP/SSH access disabled.

If you want to enable access and show the connection details, click **Enable** > **Enable Primary SFTP/SSH access**.

## Additional SFTP users

In addition to the primary SFTP/SSH user, you can create additional SFTP users with customizable permissions. Additional SFTP users are unique to each environment, and you can limit their access to read and write or read-only and further restrict their access to specific directories within your site. For example, if you want a user to only manage plugins, you can limit their access to the `/wp-content/plugins/` subdirectory. This provides greater control and security when granting access to developers, contractors, or team members.

You can add SFTP users within **Sites** > ***sitename*** > **Info** > **Additional SFTP users** > **Add new user**.

![Add SFTP users.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-add-aftp-user.png)

Add SFTP users.

Complete the new user’s details as follows:

- **Username:** This is unique to the environment; it is case-sensitive and only accepts letters, numbers, underscores (_), and dashes (-).
- **Password:** Enter a password for the user, this must be at least 16 characters.
- **Root directory:** To restrict access to a specific subdirectory, enter the path to the folder here. For example, to limit access to your plugins folder, enter `/plugins/`. The folder must already exist in your directory; if the folder does not exist, when you add the new user, the action will fail. You can create new folders using the Primary SFTP/SSH user.
- **Read, write, or Read only:** Choose the required level of access for the user.

Click **Add new user**.

![Add a new SFTP user.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-add-sftp-user.png)

Add a new SFTP user.

### Important notes

- New SFTP users share the same **Host** as the primary SFTP/SSH user but use a different **Port**.
- When you push an environment to Live or Staging, any additional SFTP users created in the environment you are pushing from are not transferred. Instead, the SFTP users already associated with the environment you are pushing to are retained and remain unchanged.
- When you clone an environment, any additional SFTP users are **not** carried over to the new environment; you’ll need to set them up again manually if needed.
- When you reset an environment, any additional SFTP users are removed.
- The only file you cannot set as the **Root directory** is the `logs` file, as it is owned by the super user. You can assign any other file or directory as the **Root directory** for additional SFTP users.
- If you want to limit access to a specific subdirectory, the folder must already exist in the site’s directory. You can create new folders using the Primary SFTP/SSH user.
- Additional SFTP users do not have SSH access.

### Edit an SFTP user

To change the details of an additional SFTP user, click the kebab (three dots) and click **Edit**.

![Edit an additional SFTP user.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-edit-additional-sftp.png)

Edit an additional SFTP user.

You can change the username, password, subdirectory access, or the level of access they have. If you change the **Root directory** to limit access to a specific subdirectory, the folder must already exist in the `public` directory; if the folder does not exist, when you edit the user, the action will fail. You can create new folders using the Primary SFTP/SSH user.

![Edit an SFTP user.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-edit-sftp-user-1.png)

Edit an SFTP user.

Once you’ve made the changes, click **Edit user**.

### Remove an SFTP user

To remove an SFTP user, click the kebab (three dots) and click **Remove**.

![Remove an additional SFTP user.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-remove-additional-sftp.png)

Remove an additional SFTP user.

To confirm the removal, click **Remove SFTP user**.

![Confirm the removal of an SFTP user.](https://kinsta.com/wp-content/uploads/2025/02/wordpress-remove-sftp-user-1.png)

Confirm the removal of an SFTP user.

### Disable/enable additional SFTP users

To disable additional SFTP users, click **Disable**.

![Disable additional SFTP users.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-disable-additional-sftp-users-1.png)

Disable additional SFTP users.

To confirm you want to disable access for the additional SFTP users, click **Disable Additional SFTP access**. This does not remove the users, if you re-enable additional SFTP access the same users will be retained. If you want to completely remove a user, see [Remove an SFTP user](#remove-an-sftp-user).

![Confirm you want to disable access to additional SFTP users.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-confirm-disable-sftp-users.png)

Confirm you want to disable access to additional SFTP users.

Once disabled, if you want to enable additional SFTP users again, click **Enable**. Any SFTP users that existed prior to disabling will be retained.

![Disabled access for additional SFTP users.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-enable-sftp-users.png)

Disabled access for additional SFTP users.

## Client examples

Here are a few examples of settings in FTP clients.

### Cyberduck

![SFTP details in Cyberduck.](https://kinsta.com/wp-content/uploads/2021/11/cyberduck-connection-settings.jpg "SFTP details in Cyberduck")

SFTP details in Cyberduck.

### WinSCP

![SFTP settings in WinSCP.](https://kinsta.com/wp-content/uploads/2021/11/how-to-use-sftp-winscp-client.png "SFTP settings in WinSCP")

SFTP settings in WinSCP.

### FileZilla

![FileZilla Quick Connect](https://kinsta.com/wp-content/uploads/2022/06/FileZilla-Quick-Connect-1024x138.png)

FileZilla Quick Connect

### Transmit

![SFTP settings in Transmit.](https://kinsta.com/wp-content/uploads/2021/11/transmit-quick-connect.jpg "SFTP settings in Transmit")

SFTP settings in Transmit.

## More information

SFTP is a secure way to connect to your website files and the only supported file transfer protocol at Kinsta. For more details about how SFTP is more secure, be sure to check out the difference between [FTP and SFTP](https://kinsta.com/blog/ftp-vs-sftp/).
