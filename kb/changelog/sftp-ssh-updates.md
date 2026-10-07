---
url: "https://kinsta.com/changelog/sftp-ssh-updates/"
title: "Kinsta offers more ways to manage SFTP/SSH access to WordPress"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Kinsta offers more ways to manage SFTP/SSH access to WordPress"]
kinsta_last_updated: "2024-05-31T21:43:47+00:00"
sitemap_lastmod: "2024-05-31T21:43:47+00:00"
fetched_at: "2026-10-07T22:36:51Z"
sha256: "4102beda978f224d547e2ab28c70232d8b1031c42af6bd122e9386cb061c758c"
body_chars: 6411
extracted_with: "main article"
status: "live"
---

# Kinsta offers more ways to manage SFTP/SSH access to WordPress

**Section:** Changelog > Kinsta offers more ways to manage SFTP/SSH access to WordPress
**Product:** Changelog
**Source:** https://kinsta.com/changelog/sftp-ssh-updates/
**Kinsta last updated:** 2024-05-31T21:43:47+00:00

## On this page

- [Disabling (and re-enabling) SFTP/SSH access](#disabling-and-re-enabling-sftpssh-access)
- [Setting a password expiration period](#setting-a-password-expiration-period)
- [Changing permitted authentication methods](#changing-permitted-authentication-methods)
- [Downloading SFTP/SSH configuration information](#downloading-sftpssh-configuration-information)
- [We’re serious about security at Kinsta](#were-serious-about-security-at-kinsta)

---

Updated
:   May 31, 2024

![An illustration representing the new SFTP/SSH configuration options in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-wordpress-sftp-ssh-updates-1024x536.png)

We’ve enhanced secure file transfer protocol (SFTP) and secure shell (SSH) configuration options within the [MyKinsta](https://kinsta.com/mykinsta/) dashboard to give [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/) customers more control over site security.

The new features support:

- Disabling SFTP/SSH access (and re-enabling it)
- Auto-expiration of passwords
- Enabling/disabling passwords as an authentication method
- Downloading access configuration information for use in third-party applications

Everything happens on the **Site Information** page in MyKinsta, found under **WordPress Sites** > ***sitename*** > **Info**, in the **SFTP/SSH** panel:

![Screenshot showing the SFTP/SSH panel on the MyKinsta Site Information page.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-sftp-ssh-updates-panel.png)

SFTP/SSH configuration details for a WordPress site on the **Site Information (Info)** page.

These details are unique to each WordPress environment. So, staged website environments will have access details that vary from those of the related live site.

Let’s look at the new configuration options you’ll find here.

## Disabling (and re-enabling) SFTP/SSH access

The most decisive way to secure SFTP/SSH access to your website environment is to turn it off completely. This could be a good move if you rarely use these protocols to work on your website. It’s easy to toggle this setting, so you might even enable SFTP/SSH only when you are using it.

If SFTP/SSH is currently enabled, you’ll see a **Disable** button in the panel’s upper-right corner. Click the button, and you will be prompted to confirm the action:

![Screenshot showing the confirmation prompt for disabling SFTP/SSH access in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-sftp-ssh-updates-disable-access.png)

A user is asked to confirm disabling SFTP/SSH access to a WordPress environment.

When SFTP/SSH is disabled for a website environment, configuration details are not relevant, so the entire SFTP/SSH panel is grayed out, and an **Enable** button repaces the **Disable** button:

![Screenshot showing the SFTP/SSH panel on the Site Information page when access is disabled.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-sftp-ssh-updates-enable-access.png)

With SFTP/SSH disabled, the **Enable** button allows you to reverse that status.

## Setting a password expiration period

By default, passwords created in MyKinsta for SFTP/SSH access do not expire automatically. Click the edit (pencil) icon beside the **Password expiration** label to choose an automatic expiry option:

![Screenshot showing the dialog for selecting an expiration period for SFTP/SSH passwords in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-sftp-ssh-updates-password-expiration.png)

Choosing an expiration period for SFTP/SSH passwords.

When you enable automatic expiry, Kinsta’s system will generate a new password at the end of your chosen period. You can access the new password by revealing it or copying it on the **SFTP/SSH** panel.

## Changing permitted authentication methods

By default, SFTP/SSH access to WordPress environments at Kinsta can be authenticated by passwords and [SSH key pairs](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/#how-to-connect-to-ssh-with-ssh-keys). To disable or re-enable password authentication, click the edit (pencil) icon beside the **Authentication methods** label. You will see this prompt:

![Screenshot showing the dialog for selecting SFTP/SSH authentication methods in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-sftp-ssh-updates-authentication-methods.png)

Choosing whether to allow SFTP/SSH authentication using a password.

Key-based authentication is always available as long as SFTP/SSH is enabled. You can select or deselect the **Password** option and then click the **Save changes** button.

## Downloading SFTP/SSH configuration information

Some SFTP and SSH client software can import connection settings from structured configuration files. You can download your environment’s current SFTP/SSH access settings in multiple file formats.

Click the download icon beside the **FTP client config files** label to download these documents as a ZIP archive. Inside the archive, you’ll find files like these:

![Screenshot showin the list of files found in an SFTP/SSH configuration download ZIP archive.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-sftp-ssh-updates-config-files-download.png)

Contents of a typical client configuration ZIP file.

The file formats above and examples of client software that use them are:

- **.xml** – Supported by [FileZilla](https://filezillapro.com/docs/server/advanced-options/how-to-export-and-import-server-configurations/).
- **.csv** – Used by [Terminus](https://support.termius.com/hc/en-us/articles/4402174294809-Importing-from-CSV).
- **.duck** – These files are pretty much exclusive to [Cyberduck](https://docs.cyberduck.io/cyberduck/connection/)

Below is an image of the FileZilla Site Manager after importing the **acme-sftp-config.xm**l file shown above:

![Screenshot showing the FileZilla Site Manager dialog with data imported from an SFTP/SSH configuration file.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-sftp-ssh-updates-config-files-download-filezilla.png)

FileZilla’s Site Manager with data pre-filled by an SFTP/SSH configuration file.

The client configuration files do not include passwords or shared-key data. You will provide that information within the client before connecting.

## We’re serious about security at Kinsta

Looking for secure cloud hosting? Learn how Kinsta leverages the [Google Cloud](https://kinsta.com/google-cloud-alternative/) and  [Cloudflare](https://kinsta.com/blog/cloudflare-integration/) to provide firewalling, DDoS protection, and free wildcard SSL.

And independent auditors have confirmed our compliance with [System and Organization Controls](https://kinsta.com/docs/service-information/soc-2/) (SOC) security standards. You can request access to Kinsta’s SOC 2 Type II report from our [Trust report page](https://trust.kinsta.com/).
