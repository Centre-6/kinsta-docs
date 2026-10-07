---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migration-source-details/"
title: "Migrations - Source Details by Hosting Provider"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-migrations"
section: []
kinsta_last_updated: "April 21, 2026"
sitemap_lastmod: "2026-04-21T09:20:57+00:00"
fetched_at: "2026-10-07T22:40:03Z"
sha256: "d191ca1d74af69c00cbae078e1508edc8df993bf6f334993a282622182213242"
body_chars: 33978
extracted_with: "main article"
status: "live"
---

# Migrations - Source Details by Hosting Provider

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migration-source-details/
**Kinsta last updated:** April 21, 2026

## On this page

- [Other](#other)
- [A2 Hosting](#a2-hosting)
- [Amazon AWS](#amazon-aws)
  - [Option 1: Your public SSH key](#option-1-your-public-ssh-key)
  - [Option 2: Add Kinsta public SSH key to AWS](#option-2-add-kinsta-public-ssh-key-to-aws)
- [Bluehost](#bluehost)
- [Cloudways](#cloudways)
  - [Option 1: Add Kinsta to your account](#option-1-add-kinsta-to-your-account)
  - [Option 2: Cloudways platform](#option-2-cloudways-platform)
- [DreamHost](#dreamhost)
- [DigitalOcean](#digitalocean)
- [Flywheel](#flywheel)
- [GoDaddy](#godaddy)
  - [Option 1: Add Kinsta to your account](#option-1-add-kinsta-to-your-account)
  - [Option 2: GoDaddy Control Panel](#option-2-godaddy-control-panel)
  - [Option 3: cPanel](#option-3-cpanel)
- [Google Cloud](#google-cloud)
  - [Option 1: Google Cloud Account](#option-1-google-cloud-account)
  - [Option 2: Your public SSH key](#option-2-your-public-ssh-key)
- [HostGator](#hostgator)
  - [Option 1: HostGator Portal](#option-1-hostgator-portal)
  - [Option 2: cPanel](#option-2-cpanel)
  - [Option 3: SFTP](#option-3-sftp)
- [Ionos](#ionos)
- [Linode (Akamai Cloud)](#linode-akamai-cloud)
- [Liquid Web](#liquid-web)
- [Media Temple](#media-temple)
- [Pagely](#pagely)
- [Pantheon](#pantheon)
- [Pressable](#pressable)
- [Savvii](#savvii)
- [SiteGround](#siteground)
  - [Option 1: Add Kinsta to your account](#option-1-add-kinsta-to-your-account)
  - [Option 2: Hosting panel credentials](#option-2-hosting-panel-credentials)
- [tsoHost](#tsohost)
- [Vultr](#vultr)
- [WP Engine](#wp-engine)
  - [Add Kinsta to your account](#add-kinsta-to-your-account)
  - [WP Engine User Portal](#wp-engine-user-portal)
- [WPX Hosting](#wpx-hosting)

---

When you request a migration from your existing host, Kinsta needs access credentials to connect to your site and transfer it to our infrastructure. The details we ask for typically include your hostname, username, password, and SFTP connection details, though some hosts require additional credentials such as hosting panel access.  
Where to find these details varies depending on your provider. Use the sections below to locate the required information for your host.

## Other

If your hosting provider is not listed, choose this option and consult your hosting provider for the required information.

## A2 Hosting

A2 Hosting uses cPanel, so most of the credentials are available in the **A2 Hosting Customer Portal** at [my.a2hosting.com](https://my.a2hosting.com). Log in, go to **Services** > **My Services**, locate your hosting account, and click **Manage**.

- **A2 Hosting username:** Your shared hosting username is shown in the Customer Portal under **Connection Details**. This username is also your cPanel username.
- **A2 Hosting password:** Your password is also shown within the **Connection Details** section. Click the eye icon next to the password to reveal it.
- **Server address:** Use your website’s domain name, for example, `yourdomain.com`. If you are using Cloudflare, use your server hostname instead, which looks like `server123.a2hosting.com` where the number corresponds to the specific server your account is on. You can find your server number in your A2 Hosting welcome email.
- **Port:** Enter `7822`. A2 Hosting uses this non-standard port for all SFTP connections instead of the default port 22.
- **SFTP Username:** This is the same as your **A2 Hosting username** found in the Customer Portal above.
- **SFTP Password:** This is the same as your **A2 Hosting password** found in the Customer Portal above.
- **WordPress site path:** This is where your WordPress files are located. On A2 Hosting, this is `/home/username/public_html`, where `username` is your cPanel username.

## Amazon AWS

There are two options for giving the migrations team access to your AWS site. Option 1 (providing the `.pem` file) is simpler for most users, and Option 2 is better suited to those comfortable with the command line.

The following details apply to both options:

- **Server address:** Log in to the AWS Management Console, navigate to your EC2 dashboard, select your instance, and look for the **Public IPv4 address** or **Public DNS (IPv4)**. Either can be used as the server address.
- **Port:** Enter `22`. This is the standard SSH/SFTP port for EC2 unless your server has been configured to use a different SSH port. If you’re unsure, check with whoever set up the server.
- **Username:** The default username depends on the Amazon Machine Image (AMI) you used when launching the instance. Common defaults are:
  - - Amazon Linux or Amazon Linux 2: `ec2-user`.
    - Ubuntu: `ubuntu`.
    - Debian: `admin`
    - CentOS: `centos`
    - Bitnami: `bitnami`

  If your instance was set up by a developer or uses a custom AMI, the username may differ; check with whoever configured the server. If you’re unsure, you can find your AMI name in the EC2 dashboard under your instance’s **Description** tab, then cross-reference it with the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-users.html).

### Option 1: Your public SSH key

- **SSH key:** The SSH key is the `.pem` file that was downloaded when you first deployed the instance. If you’re unsure of its name, it was specified during the instance launch process and is typically found in your Downloads folder. This file cannot be downloaded again after the initial launch; if it has been lost, a new key pair will need to be generated and assigned to the instance. To check existing key pairs or create a new one, go to **EC2** > **Network & Security** > **Key Pairs**.

### Option 2: Add Kinsta public SSH key to AWS

When you complete the migration request, the migrations team will supply you with the Kinsta public SSH key. Once you have this, you need to add it to your EC2 instance via SSH.

1. Connect to your EC2 instance via SSH using your existing `.pem` key and the username for your AMI (see above).
2. Once connected, open the authorized keys file with a text editor:

   Copy

   ```
   nano ~/.ssh/authorized_keys
   ```
3. On a new line at the end of the file, paste Kinsta’s public SSH key.
4. Save and close the file.
5. Disconnect from the instance.

For step-by-step instructions, see [Add or replace a public key on your Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/replacing-key-pair.html) in the AWS documentation.

## Bluehost

Bluehost currently uses cPanel, so most credentials are found in the **Bluehost Portal**. Log in at [bluehost.com](https://www.bluehost.com/my-account/login/), click **Hosting**, then click the **Advanced** tab to access your account details and cPanel. Bluehost is in the process of upgrading its interface. If you are on the new interface, your credentials are located within **Websites** > **Manage** > **Files & Access** > **Manage**.

- **Bluehost username:** Your username is your Bluehost Portal login email or user ID, the one you use to log in at [bluehost.com](https://www.bluehost.com/my-account/login/). You can also find it in the original “Welcome to Bluehost” email you received when signing up.
- **Bluehost password:** This is the password you use to log in to your Bluehost Portal.
- **Server address:** Your main domain and IP address can also be found in the **General Information** section of your control panel under the **Advanced** tab. In the new portal, go to **Websites** > **Manage** > **Advanced**. Scroll to the Name Servers & IP Address section and copy the IP address. You can use either your domain name (e.g., `yourdomain.com`) or the server IP address.
- **Port:** Enter `21`. This is the standard for FTP connections.
- **FTP Username:** This is the same as your Bluehost username above. If you have created a separate FTP account, you can find its details in the Bluehost Portal within **FTP Management**, click the ellipsis next to the **FTP account**, and select **View**. If you are on the new interface, click **Websites > Manage** > **Files & Access** > **Manage** under the FTP card. On the FTP Management panel, click the ellipsis next to the **FTP account** and select **View**.
- **FTP Password:**This is the same as your Bluehost password above. If you have created a separate FTP account, you can find its details in the Bluehost Portal within **FTP Management**, click the ellipsis next to the **FTP account**, and select **View**. If you are on the new interface, click **Websites > Manage** > **Files & Access** > **Manage** under the FTP card. On the FTP Management panel, click the ellipsis next to the **FTP account** and select **View**.
- **WordPress site path:** Your WordPress files are located at `/public_html/` or `/public_html/yourfoldername/` if WordPress was installed in a subdirectory.

## Cloudways

### Option 1: Add Kinsta to your account

This is the preferred method as it allows the migrations team to log in directly and obtain a copy of your site without requiring your personal account credentials.

Log in to the [Cloudways Platform](https://unified.cloudways.com/login/), select **Team** from the side menu, and click **Add Member**. Complete the fields as follows:

- **Email:** [[email protected]](https://kinsta.com/cdn-cgi/l/email-protection)
- **Member Name:** Kinsta migrations
- **Job Title:** Migrations
- **Status:** Active

You also need to set the permissions, select **Flexible** > **Limited Access**, choose the server your site is on, enable **View Master Credentials**, and select the website you want to migrate.

For permissions, select **Flexible > Limited Access**, then:

- Choose the server your site is on.
- Enable **View Master Credentials**.
- Select the application (website) you want to migrate.

Once done, click **Add Member**. The Kinsta team will receive an activation email automatically.

Also, provide us with the following so we can identify the correct account:

- **Customer email address:** The email address you use to log in to Cloudways.

### Option 2: Cloudways platform

If you’re unable to add a team member, you can provide your Cloudways login credentials directly.

If you choose this option, you must disable two-factor authentication before submitting your migration request so the migrations team can log in without additional security checks. To do so, log in to your [Cloudways dashboard](https://unified.cloudways.com/login/), click **Account** > **Security** > **Deactivate TFA**.

- **Cloudways username:** The username you use to log in to Cloudways.
- **Cloudways password:**The password you use to log in to Cloudways.

## DreamHost

To enable the migrations team to access your site, SSH access must be specifically enabled for your user. To enable it, go to **SFTP Users & Files**, click **Login info** next to your user, and toggle on **Secure Shell Access (SSH)**.

- **DreamHost username:** This is your DreamHost panel login, the email address you use to log in at [panel.dreamhost.com](https://panel.dreamhost.com).
- **DreamHost password:** The password you use to log in to the DreamHost panel.
- **Server address:** There are two hostnames you can use. Your domain name (e.g., `yourdomain.com`) can be used if your DNS is already pointing to DreamHost. If it isn’t pointed to DreamHost yet, use your server hostname instead, which follows the format `servername.dreamhost.com`. Both are visible on the **Login info** page under **SFTP Users & Files**.
- **Port:** Enter `22`. This applies to all DreamHost accounts.
- **SSH Username:** In your panel, go to **SFTP Users & Files**, click **Login info** next to your user; this displays your username, host, and port. Your SSH username is the same as your SFTP username.
- **SSH Password:** Your SSH password is the same as your SFTP password. If you don’t remember your password, you can reset it in **Manage Websites** > **Manage** > **Content** > **Show Login Info** > **Reset Password**.
- **WordPress site path:** Your WordPress files are located at `/home/username/yourdomain.com/`, where `username` is your SFTP/SSH username and `yourdomain.com` is your domain name.

## DigitalOcean

- **Server address:** After your Droplet is created, its IP address is displayed in the [DigitalOcean Control Panel](https://cloud.digitalocean.com/login). You’ll see it listed in the **IP Address** column on the **Droplets** page, or at the top of the Droplet’s detail page.
- **Port:** Enter `22` unless your server has been configured to use a different SSH port. If you’re unsure, check with whoever set up the server.
- **SSH Username:** The default is `root` but if the server has been hardened or set up by a developer, a different user may have been created. If you’re unsure, check with whoever set up the server or check under **Settings** in your Droplet’s detail page.
- **SSH Password:** If you created the Droplet without adding an SSH key, DigitalOcean will have emailed you a temporary root password when the Droplet was created. If you no longer have this, you can reset it from the DigitalOcean dashboard, navigate to your Droplet’s detail page, select **Access**, and click **Reset Root Password**. If you set up your DigitalOcean Droplet with SSH key authentication, you will need to provide the private SSH key instead of a password.
- **WordPress site path:** For Droplets created using DigitalOcean’s WordPress 1-Click App, the web root is `/var/www/html`. If WordPress was installed manually or using a different stack, the path may differ — `/var/www/` is the most common alternative. If you’re unsure, check with whoever set up the server.

## Flywheel

You must add [[email protected]](https://kinsta.com/cdn-cgi/l/email-protection) to your Flywheel account. This allows the migrations team to log in directly and obtain a copy of your site without requiring your personal account credentials.

To add the Kinsta migrations team to an individual site, log in to your [Flywheel dashboard](https://app.getflywheel.com/login), click on the site you want to migrate, click **Add Collaborators**, and enter `[email protected]`.

If you want to migrate more than one site, you can give the migrations team access to your organization so they can access all sites at once. Log in to your [Flywheel dashboard](https://app.getflywheel.com/login), navigate to your **Organization**, click **Members**, click **Add Members**, and enter `[email protected]`.

The migrations team will then receive an email letting them know they’ve been invited to collaborate.

## GoDaddy

### Option 1: Add Kinsta to your account

This is the preferred method as it allows the migrations team to log in directly and obtain a copy of your site without requiring your personal account credentials.

1. Sign in to your [GoDaddy account](https://sso.godaddy.com/), click your username, select **Account Settings**, and then **Delegate Access**.
2. Click **Invite to Access**, and complete the fields as follows:
   - **Name:**Kinsta Migrations
   - **Email:**[[email protected]](https://kinsta.com/cdn-cgi/l/email-protection)
   - **Access level:** Products & Domains
3. Click **Invite**. GoDaddy will send an email invitation to the migrations team and notify you once it has been accepted.

Also, provide us with the following so we can identify the correct account:

- **GoDaddy account name:**  The email address or customer number you use to log in to GoDaddy.

### Option 2: GoDaddy Control Panel

If you’re unable to add a user, you can provide your GoDaddy login credentials directly.

If you choose this option, you must disable two-factor authentication before submitting your migration request so the migrations team can log in without additional security checks. To do so, sign in to your [GoDaddy Login & PIN page](https://account.godaddy.com/security), and enter your verification code when prompted. Under **2-Step Verification**, select **Edit**, then **Delete** next to your authentication method, and confirm by clicking **Remove**.

- **GoDaddy username:** The email address you use to log in to GoDaddy.
- **GoDaddy password:** The password you use to log in to GoDaddy.

### Option 3: cPanel

If you are unable to use Option 1 or Option 2, you can provide your cPanel credentials. To access cPanel, you must first [enable SSH access](https://www.godaddy.com/en-uk/help/enable-ssh-for-my-web-hosting-cpanel-account-16102). To find the credentials, log in to your [GoDaddy account](https://sso.godaddy.com/) and go to **My Products > Web Hosting > Manage**.

- **cPanel URL:** Click **cPanel Admin**. The URL that opens in your browser is your cPanel URL. It will usually follow the format `https://yourdomain.com/cpanel`.
- **cPanel username:** The cPanel username is the **cPanel login** in **Settings**.
- **cPanel password:** You cannot view the cPanel password for security reasons. If you don’t know it, click **Change** next to the password field in **Settings** to reset it.

## Google Cloud

### Option 1: Google Cloud Account

If you choose this option, it is subject to additional security checks, including multi-factor authentication. This means the migrations team will need to contact you for this information.

- **Google Cloud username:** The username or email you use to log in to Google Cloud.
- **Google Cloud password:** The password you use to log in to Google Cloud.

### Option 2: Your public SSH key

The following credentials can be found within the [Google Cloud Console](https://console.cloud.google.com/). Click **Compute Engine** > **VM Instances** and then click on the name of your VM instance. If your site was set up by a developer, you should check with the developer for this information.

- **Server address:** In the Google Cloud Console, go to **VM Instances** and find the **External IP address** in the IP address column of the VM you want to connect to.
- **Port:** Enter `22` unless your server has been configured to use a different SSH port. If you’re unsure, check with whoever set up the server.
- **Username:** The username depends on how SSH keys are managed on your instance. If you manage SSH keys in metadata, the username is what was specified when the SSH key was created. For OS Login accounts, the username is derived from your Google profile. For example, if your Google account email is `[email protected]`, your username would be `yourname`. If your server was set up by a developer, check with them for the correct username.
- **SSH Key:** Google Cloud uses key-based SSH authentication. Your private SSH key is stored on your local machine, while the public key is stored in your VM’s instance metadata or project metadata. To find or manage your SSH keys, go to **Compute Engine** > **VM Instances**, click the name of your instance, click **Edit**, and scroll to **SSH Keys**. Your private key file is typically found in the `~/.ssh/` directory on your local machine.

## HostGator

### Option 1: HostGator Portal

If you choose this option, it is subject to additional security checks, including multi-factor authentication. This means the migrations team will need to contact you for this information.

- **HostGator Portal username:** The username or email you use to log in to HostGator.
- **HostGator Portal password:** The password you use to log in to HostGator.

### Option 2: cPanel

Your cPanel credentials are different from your HostGator Portal login. When you signed up with HostGator, your Welcome Email contained your cPanel URL, username, and password. If you no longer have that email, log in to your [Customer Portal](https://www.hostgator.com/my-account/login/), click **Hosting**, then click **Manage** next to your hosting package. The credentials can be found as follows:

- **cPanel URL:** Click **Settings**, and the server hostname is shown under the **Server** section. The cPanel URL follows the format `https://yourhostname/cpanel`. You can also use your domain name: `https://yourdomain.com/cpanel`.
- **cPanel username:** Shown in the **Server Information** section. You can also find it within cPanel itself, in **Current User** in the **General Information** section.
- **cPanel password:** You cannot view the password in your customer portal. If you don’t know it, you can reset it within **Hosting** > **Manage > Reset Password** in the **Server Information** section. After resetting your cPanel password, it can take up to 24 hours for the new password to sync with your SFTP account.

### Option 3: SFTP

SFTP is not available on Optimized WordPress plans or Windows shared hosting plans. If you are on one of these plans, you will need to use Option 1 or Option 2.

Most of the information required for SFTP can be found within the **Customer Portal** or **cPanel’s General Information** section.

- **Server address:** Use your domain name or your **Shared IP Address** as the server address. Both can be found in your **Customer Portal** or in **cPanel’s General Information** section.
- **Port:** The port is `2222` for shared and reseller hosting, and `22` for VPS and Dedicated hosting.
- **SFTP Username:** This is the same as your cPanel username. Your cPanel username is shown in the **Server Information** section. You can also find it within cPanel itself, in **Current User** in the **General Information** section.
- **SFTP Password:**This is the same as your cPanel password. You cannot view the password in your customer portal. If you don’t know it, you can reset it within **Hosting** > **Manage > Reset Password** in the **Server Information** section. After resetting your cPanel password, it can take up to 24 hours for the new password to sync with your SFTP account.
- **WordPress site path:** Your WordPress files are located at `/public_html/` for the primary domain, or `/public_html/yourdirectory/` if WordPress was installed in a subdirectory.

## Ionos

You must disable two-factor authentication before submitting your migration request so the migrations team can log in without additional security checks. To do so, log in to your [IONOS account](https://login.ionos.com/), click **Menu** > **My account**, then **Login & account security**. Click **Manage two-factor authentication** and then click **Deactivate**.

- **Ionos username:** The username you use to log in to Ionos.
- **Ionos password:** The password you use to log in to Ionos.

The protocol you use (FTP/SFTP) depends on your hosting plan. Linux hosting uses SFTP, and Windows/ASP.NET hosting uses FTPS. If you’re unsure which plan you have, log in to your IONOS account and check whether the **SFTP & SSH** tile or the **FTPS** tile appears under your hosting settings. Once you know which plan you are using, within the Kinsta migration Source details, select SFTP for Linux hosting or FTP for Windows hosting.

For the FTP/SFTP credentials, log in to your [IONOS account](https://login.ionos.com/), click **Menu > Hosting**, select your hosting contract if you have more than one, then click **Manage** in the **SFTP & SSH** or **FTPS** section, then click on your username to view your connection details.

- **Server address:** Shown in your connection details. It follows the format `home12345678.1and1-data.host` or `access12345678.webspace-data.io`.
- **Port:** Port `22` for SFTP (Linux hosting) or `990` for FTPS (Windows hosting).
- **SFTP/FTP Username:** Your username is set by IONOS. For SFTP, it typically starts with `u` or `p`, for example, `u12345678`. For FTPS, it typically starts with `ftp`, for example, `ftp12345678`.
- **SFTP/FTP Password:** The password is not displayed for security reasons. If you don’t know it, click on your username in the **SFTP & SSH** or **FTPS** section and enter a new one.
- **WordPress site path:** From your main IONOS dashboard, click **Use Webspace**. Expand the folders until you find the folder that contains the `wp-admin` folder. The full path to that folder is your WordPress site path.

## Linode (Akamai Cloud)

All credentials are found in the [Linode Cloud Manager](https://login.linode.com/). Click **Linodes** and select your Linode from the list.

- **Server address:** Your primary IPv4 address is shown in the top **Summary** section of your Linode’s dashboard. To view all IP addresses, go to **Network** > **IP Addresses**.
- **Port:** The default SSH port is `22`. However, if a developer configured your server, you should check with them.
- **SSH Username:** The default username is `root`. If a limited user account was set up on the server, that username can be used instead. If the server was configured by a developer, check with them, as `root` login may have been disabled for security reasons.
- **SSH Password:** The password is the root password that was set when the Linode was first deployed. If you don’t know it, you can reset it in Cloud Manager, select your Linode, go to **Settings** > **Reset Root Password**, select your primary disk, enter a new password, and click **Save**.
- **WordPress site path:** Linode is a cloud VPS provider, so the WordPress file path depends on how the server was configured. For a standard LAMP stack setup, the path is typically `/var/www/html/`. If WordPress was installed using a different stack or by a developer, the path may differ; check with whoever set up the server.

## Liquid Web

You must disable two-factor authentication before submitting your migration request so the migrations team can log in without additional security checks. To do so, log in to [my.liquidweb.com](https://my.liquidweb.com), click **Account**, then **Users**. Click your username, at the bottom of the **User Profile**, and click **Disable Two-Factor**.

- **Liquid Web username:** The username you use to log in to Liquid Web.
- **Liquid Web password:** The password you use to log in to Liquid Web.

On Liquid Web, SFTP and SSH use the same server address, port, username, and password. SFTP is used for file transfers via an FTP client; SSH is used for command-line access. Both sets of credentials are found in the [Liquid Web account portal](https://login.liquidweb.com/). Click **My Servers**, then click the name of your server to open the **Server details** page.

- **Server address:** The primary IP address of each server is shown next to the server name on **My Servers** or in the **Server details** page.
- **Port:** `22` is the default port for both SFTP and SSH. On InterWorx-based hosting, SFTP via mod_sftp uses port `24`. If you’re unsure which applies, check the **Network** **info** block on your **Server details** page.
- **SFTP Username:** Shown in Server Credentials.
- **SFTP Password:** Shown in Server Credentials.
- **WordPress site path:** This depends on how the server was configured. For a standard cPanel setup, the path is typically `/home/username/public_html/`. For VPS or dedicated servers without cPanel, it is commonly `/var/www/html/`. If you’re unsure, check with whoever set up the server.

## Media Temple

Media Temple was retired in February 2023, and all accounts were migrated to GoDaddy. If your site was previously hosted with Media Temple, your hosting is now managed through GoDaddy. Please refer to the [GoDaddy](#godaddy) section for instructions on finding your credentials.

## Pagely

You must disable two-factor authentication before submitting your migration request so the migrations team can log in without additional security checks. To do so, log in to your [Atomic control panel](https://atomic.pagely.com/login), click **My Settings** > **Security** > **Disable MFA**, enter your MFA code, and click **Verify and Disable**.

- **Pagely username:** The username you use to log in to Pagely.
- **Pagely password:** The password you use to log in to Pagely.

## Pantheon

You must disable two-factor authentication before submitting your migration request so the migrations team can log in without additional security checks. To do so, log in to the [Pantheon dashboard](https://dashboard.pantheon.io/login), click your avatar, select **User Settings** > **Security**, and click **Disable multi-factor authentication**. Confirm when prompted, you will be logged out and can log back in without MFA.

- **Pantheon username:** The username you use to log in to Pantheon.
- **Pantheon password:** The password you use to log in to Pantheon.

## Pressable

You must disable two-factor authentication before submitting your migration request so the migrations team can log in without additional security checks. To do so, go to [my.pressable.com/settings/security](https://my.pressable.com/settings/security). In **Two-Factor Authentication**, click **Disable**. For security, you will be prompted to enter your account password to confirm.

- **Pressable username:** The username you use to log in to Pressable.
- **Pressable password:** The password you use to log in to Pressable.

All SFTP credentials are found in the [Pressable dashboard](https://my.pressable.com/login/). Click **Sites**, select your site, and go to **Collaborators**.

- **Server address:** `sftp.pressable.com`.
- **Port:** `22`
- **SFTP Username:** Shown in **Collaborators**. This is different from the username you use to log in to Pressable.
- **SFTP Password:** This is not stored in the dashboard. If you don’t know it, click **Reset** to generate a new one. Once generated, store it securely as it cannot be viewed again.
- **WordPress site path:** WordPress files on Pressable are located at `/srv/htdocs/`.

## Savvii

Savvii may be subject to additional security checks, including multi-factor authentication. This means the migrations team will need to contact you for this information.

- **Savvii username:** The username you use to log in to Savvii.
- **Savvii password:**The password you use to log in to Savvii.

All credentials are found in the [Savvii portal](https://portal.savii.ai/login). Click **Manage** next to your site, then go to **Access**.

- **Server address:** The server hostname assigned to your site, shown in **Access** or in the email you received when the site was provisioned.
- **Port:** `22`.
- **SFTP Username:** Shown in **Access**. This is different from the username you use to log in to Savvii.
- **SFTP Password:** Sent by email when the site was delivered. If you no longer have it, go to **Manage** > **User** > **Reset password** to generate a new one.
- **WordPress site path:** `/wordpress/current/`.

## SiteGround

### Option 1: Add Kinsta to your account

This is the preferred method as it allows the migrations team to log in directly and obtain a copy of your site without requiring your personal account credentials. To add the migrations team as a collaborator:

1. Log in to your [SiteGround Client Area](https://login.siteground.com/), click your profile icon, and select **Manage Users**.
2. Go to **Collaborators** and click **Add New Collaborator**.
3. Select **Website**, choose the site you want to migrate, and enter the following details:
   - **Name:** Kinsta Migrations
   - **Email:** [[email protected]](https://kinsta.com/cdn-cgi/l/email-protection)
4. Click **Add**. The Kinsta migrations team will receive an email invitation.

Also, provide us with the following so we can identify the correct account:

- **Company name:** Your company name in SiteGround.

### Option 2: Hosting panel credentials

If you’re unable to add a user, you can provide your SiteGround login credentials directly.

If you choose this option, you must disable two-factor authentication before submitting your migration request so the migrations team can log in without additional security checks. To do so, log in to your [SiteGround Client Area](https://login.siteground.com/), click your profile icon, and go to **Login & Profile** > **Security** > **2-Step Verification**. Click **Disable** and enter the SMS verification code sent to your backup phone number to confirm.

- **SiteGround username:**The username you use to log in to SiteGround.
- **SiteGround password:**The password you use to log in to SiteGround.

## tsoHost

tsoHost accounts are currently being migrated to GoDaddy. Please refer to the [GoDaddy](#godaddy) section for instructions on finding your credentials.

## Vultr

All SSH credentials are found in the [Vultr Console](https://console.vultr.com/). Go to **Products**, then click your server name to open the server information page.

- **Server address:** The server IP address shown on the server information page.
- **Port:**The default SSH port is `22`. However, if a developer configured your server, you should check with them.
- **SSH Username:** The username is shown on the server information page. The default username on most Vultr Linux instances is `root`, though a limited user may have been created; check with whoever manages the server.
- **SSH Password:** The password is shown on the server information page; click the eye icon to reveal it.
- **WordPress site path:** The path depends on how the server was configured. For a standard LAMP stack, it is typically `/var/www/html/`. If WordPress was installed differently or by a developer, the path may vary; check with whoever set up the server.

## WP Engine

### Add Kinsta to your account

This is the preferred method as it allows the migrations team to log in directly and obtain a copy of your site without requiring your personal account credentials. To add the migrations team as a user:

1. Log in to your [WP Engine portal](https://identity.wpengine.com/), click **Users**, then **Account Users**.
2. Click **Invite account user** and enter the following:
   - **Name:** Kinsta Migrations
   - **Email:** [[email protected]](https://kinsta.com/cdn-cgi/l/email-protection)
   - **Role:** Full (no billing)
3. Click **Send Invitation**. The Kinsta migrations team will receive an email invitation.

Also, provide us with the following so we can identify the correct account:

- **Company name:** Your company name in WP Engine.

### WP Engine User Portal

If you’re unable to add a user, you can provide your WP Engine login credentials directly.

If you choose this option, it is subject to additional security checks, including multi-factor authentication. This means the migration process may take longer as the migrations team will need to contact you for this information.

- **WP Engine User Portal username:** The username you use to log in to WP Engine.
- **WP Engine User Portal password:** The password you use to log in to WP Engine.

## WPX Hosting

You must disable two-factor authentication before submitting your migration request so the migrations team can log in without additional security checks. To do so, log in to your [WPX account](https://wpx.net/clientarea), go to **Security**, and select the option to disable 2FA.

- **WPX Hosting username:** The username you use to log in to WPX Hosting.
- **WPX Hosting password:** The password you use to log in to WPX Hosting.

All FTP credentials are found in the [WPX Control Panel](https://wpx.net/clientarea). Locate your hosting plan, click **Control Panel**, then **FTP Users & Files**. You must create an FTP user before you can provide FTP credentials. Create a new FTP user for the site you want to migrate. Once created, the username, password, and server address will be displayed in the same section.

- **Server address:** Shown in **FTP Users & Files**. It follows the format `sftp://s24.wpx.net`, the number will vary depending on which server your account is on.
- **Port:** `21`.
- **FTP Username:** Shown in **FTP Users & Files**.
- **FTP Password:**Shown in **FTP Users & Files**.
- **WordPress site path:** Your main WordPress files are stored in the `public_html` folder. Any additional sites or subdomains are stored inside the `/domains` directory, each with its own `public_html` folder.
