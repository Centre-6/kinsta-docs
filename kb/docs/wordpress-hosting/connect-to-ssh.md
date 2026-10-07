---
url: "https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/"
title: "WordPress Hosting - SSH"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "connect-to-ssh"
section: []
kinsta_last_updated: "April 20, 2026"
sitemap_lastmod: "2026-04-20T09:39:54+00:00"
fetched_at: "2026-10-07T22:38:37Z"
sha256: "3c5816246841b2bec64b84abcfa59a58f25c6ee79c069a3876567b098b74ab5d"
body_chars: 15372
extracted_with: "main article"
status: "live"
---

# WordPress Hosting - SSH

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/
**Kinsta last updated:** April 20, 2026

## On this page

- [Primary SFTP/SSH user](#primary-sftpssh-user)
  - [Change the primary SFTP/SSH user password](#change-the-primary-sftpssh-user-password)
  - [Set a password expiration for the primary SFTP/SSH user](#set-a-password-expiration-for-the-primary-sftpssh-user)
  - [Authentication methods for primary SFTP/SSH user](#authentication-methods-for-primary-sftpssh-user)
  - [IP allowlist for primary SFTP/SSH user](#ip-allowlist-for-primary-sftpssh-user)
- [How to connect to SSH with a username and password](#how-to-connect-to-ssh-with-a-username-and-password)
  - [Connect to SSH with a username and password on Windows](#connect-to-ssh-with-a-username-and-password-on-windows)
  - [Connect to SSH with a username and password on Mac/Linux](#connect-to-ssh-with-a-username-and-password-on-maclinux)
- [How to connect to SSH with SSH keys](#how-to-connect-to-ssh-with-ssh-keys)
  - [How to generate SSH key pair on Windows](#how-to-generate-ssh-key-pair-on-windows)
  - [How to generate SSH key pair on MAC/Linux](#how-to-generate-ssh-key-pair-on-maclinux)
  - [How to add SSH keys in MyKinsta](#how-to-add-ssh-keys-in-mykinsta)
  - [How to connect to SSH on Windows with SSH keys](#how-to-connect-to-ssh-on-windows-with-ssh-keys)
  - [How to connect to SSH on MAC/Linux with SSH keys](#how-to-connect-to-ssh-on-maclinux-with-ssh-keys)
- [Disable/enable SFTP/SSH access](#disableenable-sftpssh-access)
- [Additional notes](#additional-notes)

---

[SSH](https://kinsta.com/blog/ssh-vs-ssl/#what-is-ssh) is a secure protocol for remote login and other network services over an unsecured network. At Kinsta, SSH access is included with all [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/) plans, allowing you to log into the command line, perform administrative tasks, and execute commands as if you were directly on the server. With SSH, you can use essential tools like Git, Composer, and WP-CLI for efficient site management. If you’re on a Single 1.25M or higher plan or a WP 60 or higher plan, you also get access to additional tools like npm.

SSH is recommended for advanced users only, as running incorrect commands can potentially break your site. If you’re unsure or unfamiliar with SSH, we strongly advise consulting a developer or reaching out to our [Support team](https://kinsta.com/contact-us/) before making any changes.

## Primary SFTP/SSH user

You can connect to SSH using the following information from the **Primary SFTP/SSH user**:

- host/server address (IP address)
- username (SFTP Username, not your email address)
- password
- port (we take security seriously here at Kinsta, each environment uses a different port)

You can find this information under the **Primary SFTP/SSH user** of each site’s **Info** tab within [MyKinsta](https://my.kinsta.com/).

![Primary SFTP and SSH user details in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-ssh-info-1.png)

Primary SFTP and SSH user details in MyKinsta.

You cannot create additional users to connect via SSH; however, you can create [additional SFTP users](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/).

### Change the primary SFTP/SSH user password

If you want to update the primary SFTP/SSH user password for the current environment, hover over the password and click **Generate new SFTP password**.

![Generate a new primary SFTP/SSH user password for your WordPress site.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-new-password.png)

Generate a new primary SFTP/SSH user password for your WordPress site.

To confirm the password change, click **Generate new password**.

![Confirm the password change by clicking Generate new password.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-generate-new-password-1024x324.png)

Confirm the password change by clicking Generate new password.

### Set a password expiration for the primary SFTP/SSH user

If you want the primary STFP/SSH user password to expire and regenerate at regular intervals automatically for the current environment, click the edit icon under **Password expiration**.

![Change the primary STFP/SSH user password expiration time.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-password-expiration-1.png)

Change the primary STFP/SSH user password expiration time.

Choose how often you want the password to expire and regenerate, and click **Save changes**.

![Choose the interval for the password expiration.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-change-password-expiration-1024x488.png)

Choose the interval for the password expiration.

### Authentication methods for primary SFTP/SSH user

To change the primary SFTP/SSH user authentication methods to enable or disable access with a username and password for the current environment, click the edit icon under **Authentication methods**.

![Change the primary SSH user authentication methods.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-authentication-methods.png)

Change the primary SSH user authentication methods.

Select **Password** to enable or disable SSH access with a username and password, and click **Save changes**. You cannot disable access using an SSH key; however, you can [disable all SFTP/SSH access](#disableenable-ftpssh-access).

![Select Password to enable or disable SSH access with a username and password.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-change-authentication-method-1024x500.png)

Select Password to enable or disable SSH access with a username and password.

### IP allowlist for primary SFTP/SSH user

To specify a list of IP addresses that are allowed to access your environment via SFTP/SSH, click the edit icon under **IP allowlist**.

![Specify which IP addresses can access the environment via SFTP/SSH.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-ip-allowlist.png)

Specify which IP addresses can access the environment via SFTP/SSH.

Enter the IP addresses you want to allow access via SFTP/SSH and click **Add**. You can specify multiple addresses separated by a comma, e.g., 1.1.1.1, 2.2.2.2. You can also specify a range of IP addresses using a slash, e.g., 1.1.1.1/32.

![Specify the IP addresses that are allowed to access your environment via SFTP/SSH.](https://kinsta.com/wp-content/uploads/2024/06/wordpress-specify-IP-address-1024x430.png)

Specify the IP addresses that are allowed to access your environment via SFTP/SSH.

Once you have entered all of the required IP addresses, click **Update IP allowlist**.

![Update the IP allowlist for SFTP/SSH.](https://kinsta.com/wp-content/uploads/2024/06/wordpress-sftp-update-ip-allowlist-1024x686.png)

Update the IP allowlist for SFTP/SSH.

## How to connect to SSH with a username and password

The easiest method for connecting via SSH is to use a username and password. To connect with a username and password, you must ensure the [password authentication method](#Authentication-Methods) is enabled. The steps to do that vary depending on your operating system. We’ve outlined the process for each below.

- [Windows](#connect-to-ssh-with-a-username-and-password-on-windows)
- [Mac or Linux](#connect-to-ssh-with-a-username-and-password-on-maclinux)

### Connect to SSH with a username and password on Windows

Windows users require a terminal client to connect to SSH. We recommend downloading the free [PuTTY client](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) using the .msi installer. This also includes PuTTYgen, which you’ll need if you want to use SSH keys.

1. Launch PuTTY and enter your **Host IP Address** and the unique **Port** number (both found in MyKinsta > **Sites** > ***sitename*** > **Info** > **Primary SFTP/SSH user** > **Host**). Then click **Open**.
   ![SSH PuTTY client for Windows.](https://kinsta.com/wp-content/uploads/2015/04/ssh-putty-client.jpg)

   SSH PuTTY client for Windows.
2. If this is your first time connecting, you will most likely see a rsa2 key prompt. Go ahead and click **Yes**, which will trust the host in the future.
   ![PuTTY security alert about rsa2 key.](https://kinsta.com/wp-content/uploads/2015/04/putty-security-alert-rsa2-key.jpg)

   PuTTY security alert about rsa2 key.
3. In the terminal screen, you’ll need to enter your Kinsta username and press Enter/return.
   ![Enter your Kinsta username in PuTTY and press Enter/return.](https://kinsta.com/wp-content/uploads/2015/04/login-putty-username.jpg)

   Enter your Kinsta username in PuTTY and press Enter/return.
4. You’ll then be prompted to enter your password. Press Enter/return again.
   ![Enter your SSH password in PuTTY.](https://kinsta.com/wp-content/uploads/2015/04/ssh-password-login.jpg)

   Enter your SSH password in PuTTY.

You’re now connected via SSH to your WordPress site.

![SSH login successful with PuTTY.](https://kinsta.com/wp-content/uploads/2015/04/login-successful-ssh.jpg)

SSH login successful with PuTTY.

You can run commands such as `ls` or `cd` to list items and navigate throughout your site’s directories. [WP-CLI](https://kinsta.com/blog/wp-cli/) is also installed by default on all sites.

![Running SSH commands in PuTTY.](https://kinsta.com/wp-content/uploads/2015/04/run-ssh-commands.jpg)

Running SSH commands in PuTTY.

### Connect to SSH with a username and password on Mac/Linux

On Mac or Linux, it’s a lot easier to connect to SSH because the operating system (OS) already has a terminal built into it.

1. Open the terminal by going to **Applications** > **Utilities** and double-clicking on **Terminal**.
2. Then enter the command like this (You can copy/paste this command directly from MyKinsta):

Copy

```
ssh username@hostip -p portnumber
```

![SSH terminal command in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-ssh-terminal-command-4.png)

SSH terminal command in MyKinsta.

## How to connect to SSH with SSH keys

Another option for connecting to SSH is to generate an SSH key pair. SSH keys provide a more secure way of logging into a server and eliminate the need for a password. You can also further protect your login by adding a passphrase, but this isn’t required.

### How to generate SSH key pair on Windows

1. Launch PuTTYgen. If you haven’t downloaded it yet, you can [grab it here](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).
2. The default parameters should be fine in most configurations. Click on **Generate**.
   ![Generate a new key in PuTTY Key Generator.](https://kinsta.com/wp-content/uploads/2021/11/putty-key-generator.png)

   Generate a new key in PuTTY Key Generator.
3. Move your mouse around to generate some randomness.
   ![Moving your mouse around to create randomness in PuTTY Key Generator.](https://kinsta.com/wp-content/uploads/2015/04/putty-gen-move-mouse.png)

   Moving your mouse around to create randomness in PuTTY Key Generator.
4. Save both your public (.txt) and private key (.ppk). **Important:** Keep your private key safe and don’t share it with anyone.
   ![Save public and private keys from PuTTY Key Generator.](https://kinsta.com/wp-content/uploads/2015/04/save-public-and-private-keys.png)

   Save public and private keys from PuTTY Key Generator.
5. **Leave the PuTTY window open** and skip down to where you [add your public key to MyKinsta](#how-to-add-ssh-keys-in-mykinsta).

### How to generate SSH key pair on MAC/Linux

Launch the Terminal from **Applications** > **Utilities** > **Terminal** and use the following command to start the key generation:

Copy

```
ssh-keygen -t rsa
```

Choose a location to save your private key. If you leave it blank, it will save it here:

Copy

```
/home/youruser/.ssh/id_rsa
```

The public key (.PUB) will get created in the same location.

Copy

```
/home/youruser/.ssh/id_rsa.pub
```

You will then be prompted to choose a passphrase. You can leave it empty if you don’t want to use a passphrase.

### How to add SSH keys in MyKinsta

Now that you have your SSH keys, you can upload your **public key** to MyKinsta.

1. Click into your user profile in the top-right corner, and click on **User Settings**.
   ![MyKinsta user settings.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-user-settings.png)

   MyKinsta user settings.
2. In the **My Account** tab, click on the **Add SSH key** button.
   ![Add SSH key in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-add-ssh-key.png)

   Add SSH key in MyKinsta.
3. Choose a label and paste your **public** **key**.
   - If you’re running Windows, copy and paste the public key directly from PuTTYgen.
   - If you’re running Mac/Linux, you can copy your public key to your clipboard by using the following command in Terminal:

Copy

```
pbcopy < ~/.ssh/id_rsa.pub
```

4. After you paste your public key, click the **Add SSH key** button.
   ![A valid rsa key in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-add-ssh-key-add-1024x471.png)

   A valid rsa key in MyKinsta.

### How to connect to SSH on Windows with SSH keys

1. Launch [PuTTY](http://www.putty.org/) and enter your **Host IP Address** and the unique **Port** number (both found in MyKinsta > **Sites** > ***sitename*** > **Info** > **Primary** **SFTP/SSH user** > **Host**).
   ![Host Name and Port number in PuTTY client.](https://kinsta.com/wp-content/uploads/2015/04/ssh-putty-client.jpg)

   Host IP and Port number in PuTTY client.
2. Under **Connection** > **Data** enter your Kinsta username in the **Auto-login username** field.
   ![SSH Auto-login username in PuTTY.](https://kinsta.com/wp-content/uploads/2015/04/ssh-auto-login-username.png)

   SSH Auto-login username in PuTTY.
3. Under **Connection** > **SSH** > **Auth** > **Credentials**, click the **Browse** button and select your private key file for authentication.
   ![Add your SSH private key file in PuTTY.](https://kinsta.com/wp-content/uploads/2021/11/putty-ssh-private-key.png)

   Add your SSH private key file in PuTTY.
4. Under **Session**, enter a new **Saved Sessions** name and click on **Save**. Click the **Open** button to start a new session.
   ![Name and save your SSH session in PuTTY.](https://kinsta.com/wp-content/uploads/2015/04/ssh-save-session.png)

   Name and save your SSH session in PuTTY.
5. You’ll most likely see a security alert about a change in keys. Click on **Yes**.
   ![Click Yes in the PuTTY security alert about a change in keys.](https://kinsta.com/wp-content/uploads/2015/04/putty-security-alert.png)

   Click Yes in the PuTTY security alert about a change in keys.
6. If you set up a passphrase, you’ll need to enter that.
   ![Enter passphrase for key, if applicable.](https://kinsta.com/wp-content/uploads/2015/04/ssh-passphrase.png)

   Enter passphrase for key, if applicable.

   Otherwise, you’ll be logged right in.

   ![Logged into the site with an SSH key.](https://kinsta.com/wp-content/uploads/2015/04/kinsta-ssh.png)

   Logged into the site with an SSH key.

### How to connect to SSH on MAC/Linux with SSH keys

1. Launch the Terminal from **Applications** > **Utilities** > **Terminal**.
2. You now need to load your saved private key using the following command:

Copy

```
ssh-add ~/.ssh/id_rsa
```

3. If you set a passphrase for your key, you’ll be prompted to enter that.
4. Enter the command in the following form (You can copy/paste this directly from MyKinsta):

Copy

```
ssh username@hostip -p portnumber
```

![SSH terminal command in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-ssh-terminal-command-4.png)

SSH terminal command in MyKinsta.

## Disable/enable SFTP/SSH access

If you want to disable access so users with the primary SFTP/SSH credentials can’t connect via SFTP/SSH, on your site’s **Info** tab and within **Primary SFTP/SSH user**, click **Disable**.

![Disable SFTP/SSH access.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-disable-1.png)

Disable SFTP/SSH access.

To confirm the changes, click **Disable SFTP/SSH access**.

![Confirm the changes to disable SFTP/SSH access.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-disable-confirm-1024x369.png)

Confirm the changes to disable SFTP/SSH access.

When SFTP/SSH access is disabled, the connection details are no longer shown.

![SFTP/SSH access disabled.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-disabled-1024x152.png)

SFTP/SSH access disabled.

If you want to enable access and show the connection details, click **Enable** > **Enable SFTP/SSH access**.

## Additional notes

If you have trouble connecting, you might need to [change the password](#Change-the-SSH-Password) or [delete entries from your known_hosts file](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/cant-connect-delete-ssh-known-hosts/).
