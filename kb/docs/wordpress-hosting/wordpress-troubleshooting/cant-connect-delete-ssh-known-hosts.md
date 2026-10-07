---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/cant-connect-delete-ssh-known-hosts/"
title: "Troubleshooting - SSH and SFTP Connection Errors"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-troubleshooting"
section: []
kinsta_last_updated: "February 18, 2026"
sitemap_lastmod: "2026-02-18T05:53:44+00:00"
fetched_at: "2026-10-07T22:38:08Z"
sha256: "a68275c4716b46d2f0b3bbac8997ae3d7fb6ddf72628089267e6c799f3815f8b"
body_chars: 4683
extracted_with: "main article"
status: "live"
---

# Troubleshooting - SSH and SFTP Connection Errors

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/cant-connect-delete-ssh-known-hosts/
**Kinsta last updated:** February 18, 2026

## On this page

- [Can’t connect via SSH or SFTP – Delete SSH known_hosts](#cant-connect-via-ssh-or-sftp-delete-ssh-known-hosts)
  - [Mac or Linux](#mac-or-linux)
  - [Windows](#windows)
    - [OpenSSH client](#openssh-client)
    - [PuTTY SSH client](#putty-ssh-client)

---

Have issues connecting via [SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) or [SFTP](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/)? If you’re getting an error like the one below, it’s often due to a mismatch in the SSH key fingerprint. This typically happens when the server’s IP address or SSH fingerprint has changed, but your local **known_hosts** file still stores the old one.

For example, if you push one environment to another, such as staging to live, a new SSH key fingerprint is generated. Since the **known_hosts** file is used to verify SSH and SFTP connections, the mismatch can block the connection.

To resolve this, you’ll need to remove the outdated entry from your **known_hosts** file and reconnect to accept the new fingerprint.

Copy

```
[user@hostname ~]$ ssh root@user
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED! @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
xx:xx:xx.
Please contact your system administrator.
Add correct host key in /home/hostname /.ssh/known_hosts to get rid of this message.
Offending RSA key in /var/lib/sss/pubconf/known_hosts:4
RSA host key for user has changed and you have requested strict checking.
Host key verification failed.
```

## Can’t connect via SSH or SFTP – Delete SSH known_hosts

If you’re having trouble connecting, first ensure you are using the correct password. You can always [change your SFTP and or SSH password](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/) from within [MyKinsta](https://my.kinsta.com/).

If the issue persists, follow the directions below to delete entries from your `known_hosts` file.

- [Delete entries from known_hosts file on Mac or Linux](#mac)
- [Delete entries from known_hosts file on Windows](#windows)

### Mac or Linux

1. Open up Terminal and edit your **known_hosts** file in [nano text editor](https://www.nano-editor.org/) with the following command:

Copy

```
nano ~/.ssh/known_hosts
```

1. Remove all entries that start with your site’s Host IP address (found in the SFTP/SSH section on your site’s Info tab in MyKinsta). You can delete each line that you need to remove with Ctrl+k.
2. Then save the document (Ctrl+x). When prompted, answer **Y** for yes and do not change the file name (just hit return when prompted for the file name to confirm and keep the current name).

### Windows

If you are on Windows, there are two different methods for clearing the IP address entries depending on your SSH client.

- If you use the native OpenSSH client built into Windows or Git, you need to delete entries in the `known_hosts` file.
- If you use the PuTTY SSH client or similar, it stores the credentials and IP in the registry.

If you’re not sure which SSH client you’re using, check if the error message contains `known_hosts` in the file path, for example, `C:\Users\Username\.ssh\known_hosts`. If it does, this means you are using an OpenSSH client.

#### OpenSSH client

1. Browse to the file path in the error message, for example, `C:\Users\Username\.ssh\`, and locate the `known_hosts` file. This file may be hidden, so you may need to ensure **Show hidden files, folders, and drives**is selected in your file explorer settings.
2. Identify the IP address and port for the site you are trying to connect to by looking for the specific IP address and port within the error message. You can also find the IP address within the SFTP/SSH section on your site’s Info tab in MyKinsta. For example, `[34.64.255.111]:48129`.
3. Remove all entries that start with your site’s IP address from the `known_hosts` file. You can do this by manually editing the file within a text editor, or by using the `ssh-keygen -R` command, for example:

   Copy

   ```
   ssh-keygen -R [hostname_or_IP]
   ```

   or

   Copy

   ```
   ssh-keygen -R "[IP]:[Port]"
   ```

#### PuTTY SSH client

1. Launch **regedit** from your start menu. The example below is using Windows 10.
   ![regedit](https://kinsta.com/wp-content/uploads/2016/09/regedit-1.png)

   Windows regedit
2. Browse to the following directory:  
   **HKEY_CURRENT_USERSoftWareSimonTathamPuTTYSshHostKeys**![sshhostkeys](https://kinsta.com/wp-content/uploads/2016/09/sshhostkeys-1.png)

   SshHostKeys
3. Remove all entries that end with your site’s Host IP address (found in the SFTP/SSH section on your site’s Info tab in MyKinsta).
