---
url: "https://kinsta.com/docs/devkinsta/devkinsta-troubleshooting/error-codes/"
title: "Error Codes"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-troubleshooting"
section: ["DevKinsta", "Troubleshooting"]
kinsta_last_updated: "2026-02-18T05:53:46"
change_signal: "2026-02-18T05:53:46"
fetched_at: "2026-10-07T22:58:20Z"
sha256: "64dd650090c315f363fa7e460ef281f7aefe608215fba027c179f0f1b2dc713a"
body_chars: 33610
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Error Codes

**Section:** DevKinsta > Troubleshooting
**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-troubleshooting/error-codes/
**Kinsta last updated:** 2026-02-18T05:53:46

## On this page

- [Viewing the application log file](#viewing-the-application-log-file)
  - [Windows](#windows)
  - [Mac](#mac)
  - [Linux](#linux)
- [DK0001](#dk0001)
  - [Description: Not enough free disk space.](#description-not-enough-free-disk-space)
  - [Solution](#solution)
- [DK0002](#dk0002)
  - [Description: There is no internet connection.](#description-there-is-no-internet-connection)
  - [Solution](#solution)
- [DK0003](#dk0003)
  - [Description: Couldn’t install Docker.](#description-couldnt-install-docker)
  - [Solution](#solution)
- [DK0004](#dk0004)
  - [Description: Couldn’t start Docker. Please try to start Docker manually.](#description-couldnt-start-docker-please-try-to-start-docker-manually)
  - [Solution](#solution)
- [DK0005](#dk0005)
  - [Description: Couldn’t create Docker containers.](#description-couldnt-create-docker-containers)
  - [Solution](#solution)
- [DK0006](#dk0006)
  - [Description: Couldn’t download Docker images.](#description-couldnt-download-docker-images)
  - [Solution](#solution)
- [DK0008](#dk0008)
  - [Description: Couldn’t fetch IP.](#description-couldnt-fetch-ip)
  - [Solution](#solution)
- [DK0009](#dk0009)
  - [Description: Can’t start Docker container](#description-cant-start-docker-container)
  - [Solution](#solution)
- [DK0010](#dk0010)
  - [Description: Couldn’t load Docker images.](#description-couldnt-load-docker-images)
  - [Solution](#solution)
- [DK0011](#dk0011)
  - [Description: Unknown server error occurred. Please try it again.](#description-unknown-server-error-occurred-please-try-it-again)
  - [Solution](#solution)
- [DK0012](#dk0012)
  - [Description: Your request timed out. Please try it again.](#description-your-request-timed-out-please-try-it-again)
  - [Solution](#solution)
- [DK0013](#dk0013)
  - [Description: Remote server received wrong data. Please try it again.](#description-remote-server-received-wrong-data-please-try-it-again)
  - [Solution](#solution)
- [DK0014](#dk0014)
  - [Description: You are unauthenticated. Please try to re-login into MyKinsta account.](#description-you-are-unauthenticated-please-try-to-re-login-into-mykinsta-account)
  - [Solution](#solution)
- [DK0015](#dk0015)
  - [Description: You don’t have permission for this action.](#description-you-dont-have-permission-for-this-action)
  - [Solution](#solution)
- [DK0016](#dk0016)
  - [Description: Couldn’t find remote server. Please try it again.](#description-couldnt-find-remote-server-please-try-it-again)
  - [Solution](#solution)
- [DK0017](#dk0017)
  - [Description: You made too many requests. Please try it again a few minutes later.](#description-you-made-too-many-requests-please-try-it-again-a-few-minutes-later)
  - [Solution](#solution)
- [DK0018](#dk0018)
  - [Description: You didn’t grant permission for site deletion.](#description-you-didnt-grant-permission-for-site-deletion)
  - [Solution](#solution)
- [DK0019](#dk0019)
  - [Description: NGINX configuration failed](#description-nginx-configuration-failed)
  - [Solution](#solution)
- [DK0020](#dk0020)
  - [Description: Database creation failed](#description-database-creation-failed)
  - [Solution](#solution)
- [DK0021](#dk0021)
  - [Description: WordPress site setup failed](#description-wordpress-site-setup-failed)
  - [Solution](#solution)
- [DK0022](#dk0022)
  - [Description: Host file update failed](#description-host-file-update-failed)
  - [Solution](#solution)
- [DK0023](#dk0023)
  - [Description: Can’t add certificate to Keychain](#description-cant-add-certificate-to-keychain)
  - [Solution](#solution)
- [DK0024](#dk0024)
  - [Description: Can’t write to Certificate store](#description-cant-write-to-certificate-store)
  - [Solution](#solution)
- [DK0025](#dk0025)
  - [Description: Can’t download site](#description-cant-download-site)
  - [Solution](#solution)
- [DK0026](#dk0026)
  - [Description: Site push failed](#description-site-push-failed)
  - [Solution](#solution)
- [DK0027](#dk0027)
  - [Description: Missing host file entry](#description-missing-host-file-entry)
  - [Solution](#solution)
- [DK0029](#dk0029)
  - [Description: Can’t create mysql dump](#description-cant-create-mysql-dump)
  - [Solution](#solution)
- [DK0030](#dk0030)
  - [Description: OPERATION INTERRUPTED](#description-operation-interrupted)
  - [Solution](#solution)
- [DK0031](#dk0031)
  - [Description: Port 80 or 443 is used.](#description-port-80-or-443-is-used)
  - [Solution](#solution)
    - [find & kill process on macOS](#find-kill-process-on-macos)
    - [find & kill process on Windows](#find-kill-process-on-windows)
- [DK0032](#dk0032)
  - [Description](#description)
  - [Solution](#solution)
- [DK0033](#dk0033)
  - [Description: Can’t connect to database](#description-cant-connect-to-database)
  - [Solution](#solution)
- [DK0034](#dk0034)
  - [Description: Please restart your computer to finish installation.](#description-please-restart-your-computer-to-finish-installation)
  - [Solution](#solution)
- [DK0035](#dk0035)
  - [Description](#description)
  - [Solution](#solution)
- [DK0036](#dk0036)
  - [Description](#description)
  - [Solution](#solution)
- [DK0037](#dk0037)
  - [Description: Container not found](#description-container-not-found)
  - [Solution](#solution)
- [DK0038](#dk0038)
  - [Description: Set WP config](#description-set-wp-config)
  - [Solution](#solution)
- [DK0039](#dk0039)
  - [Description: Docker stops common](#description-docker-stops-common)
  - [Solution](#solution)
- [DK0040](#dk0040)
  - [Description: Could not renew the ssh key.](#description-could-not-renew-the-ssh-key)
  - [Solution](#solution)
- [DK0041](#dk0041)
  - [Description: Invalid TwoFA. Only Authy and TOTP TwoFA are supported.](#description-invalid-twofa-only-authy-and-totp-twofa-are-supported)
  - [Solution](#solution)
- [DK0044](#dk0044)
  - [Description: Can’t write to Certificate store](#description-cant-write-to-certificate-store)
  - [Solution](#solution)
- [DK0045](#dk0045)
  - [Description: Certificate is not verified](#description-certificate-is-not-verified)
  - [Solution](#solution)
- [DK0046](#dk0046)
  - [Description: Failed to install certutil package](#description-failed-to-install-certutil-package)
  - [Solution](#solution)
- [DK0047](#dk0047)
  - [Description: DevKinsta couldn’t overwrite sites.ini. Site creation is failed.](#description-devkinsta-couldnt-overwrite-sitesini-site-creation-is-failed)
  - [Solution](#solution)
- [DK0048](#dk0048)
  - [Description: You don’t have the necessary privileges to start the Docker client. Please set the required permissions and try again.](#description-you-dont-have-the-necessary-privileges-to-start-the-docker-client-please-set-the-required-permissions-and-try-again)
  - [Solution](#solution)
- [DK0049](#dk0049)
  - [Description: Could not delete site’s content.](#description-could-not-delete-sites-content)
  - [Solution](#solution)
- [DK0050](#dk0050)
  - [Description: Could not delete site entry from sites.ini.](#description-could-not-delete-site-entry-from-sitesini)
  - [Solution](#solution)
- [DK0051](#dk0051)
  - [Description: Could not delete the database.](#description-could-not-delete-the-database)
  - [Solution](#solution)
- [DK0052](#dk0052)
  - [Description: Could not save php.ini content](#description-could-not-save-phpini-content)
  - [Solution](#solution)
- [DK0053](#dk0053)
  - [Description: Could not save php.ini content](#description-could-not-save-phpini-content)
  - [Solution](#solution)
- [DK0054](#dk0054)
  - [Description: Could not update sites.ini with the new ports.](#description-could-not-update-sitesini-with-the-new-ports)
  - [Solution](#solution)
- [DK0055](#dk0055)
  - [Description: Could not recreate Nginx container with new ports.](#description-could-not-recreate-nginx-container-with-new-ports)
  - [Solution](#solution)
- [DK0056](#dk0056)
  - [Description: Could not update site URLs with new ports.](#description-could-not-update-site-urls-with-new-ports)
  - [Solution](#solution)
- [DK0058](#dk0058)
  - [Description: Failed to copy the site folder.](#description-failed-to-copy-the-site-folder)
  - [Solution](#solution)
- [DK0059](#dk0059)
  - [Description: Failed to copy the database.](#description-failed-to-copy-the-database)
  - [Solution](#solution)
- [DK0060](#dk0060)
  - [Description: Failed to update the database.](#description-failed-to-update-the-database)
  - [Solution](#solution)
- [DK0061](#dk0061)
  - [Description: Failed to delete the old site’s data.](#description-failed-to-delete-the-old-sites-data)
  - [Solution](#solution)
- [DK0062](#dk0062)
  - [Description: Failed to add certification to the store.](#description-failed-to-add-certification-to-the-store)
  - [Solution](#solution)
- [DK0063](#dk0063)
  - [Description: Failed to restart a Docker container](#description-failed-to-restart-a-docker-container)
  - [Solution](#solution)
- [DK0064](#dk0064)
  - [Description: Couldn’t remove remote files.](#description-couldnt-remove-remote-files)
  - [Solution](#solution)
- [DK0065](#dk0065)
  - [Description: Failed to upload local files](#description-failed-to-upload-local-files)
  - [Solution](#solution)
- [DK0066](#dk0066)
  - [Description: Failed to import database dump](#description-failed-to-import-database-dump)
  - [Solution](#solution)
- [DK0067](#dk0067)
  - [Description: Failed to run search and replace](#description-failed-to-run-search-and-replace)
  - [Solution](#solution)
- [DK0068](#dk0068)
  - [Description: Failed to create site backups when trying to change ports.](#description-failed-to-create-site-backups-when-trying-to-change-ports)
  - [Solution](#solution)
- [DK0070](#dk0070)
  - [Description: Failed to delete DNS record.](#description-failed-to-delete-dns-record)
  - [Solution](#solution)
- [DK0071](#dk0071)
  - [Description: Failed to add DNS record.](#description-failed-to-add-dns-record)
  - [Solution](#solution)
- [DK0072](#dk0072)
  - [Description: Could not delete site config file](#description-could-not-delete-site-config-file)
  - [Solution](#solution)
- [DK0073](#dk0073)
  - [Description: Could not restart Nginx service](#description-could-not-restart-nginx-service)
  - [Solution](#solution)
- [DK0074](#dk0074)
  - [Description: Failed to create site backup.](#description-failed-to-create-site-backup)
  - [Solution](#solution)
- [DK0075](#dk0075)
  - [Description: Failed to restore the site backup.](#description-failed-to-restore-the-site-backup)
  - [Solution](#solution)
- [DK0076](#dk0076)
  - [Description: Couldn’t install WordPress plugin](#description-couldnt-install-wordpress-plugin)
  - [Solution](#solution)
- [DK0077](#dk0077)
  - [Description: Couldn’t remove WordPress plugin](#description-couldnt-remove-wordpress-plugin)
  - [Solution](#solution)
- [DK0078](#dk0078)
  - [Description: Couldn’t update WordPress option](#description-couldnt-update-wordpress-option)
  - [Solution](#solution)
- [DK0081](#dk0081)
  - [Description: Parsing wp-config.php file failed.](#description-parsing-wp-configphp-file-failed)
  - [Solution](#solution)
- [DK0082](#dk0082)
  - [Description: Load remote file system error.](#description-load-remote-file-system-error)
  - [Solution](#solution)
- [DK0083](#dk0083)
  - [Description: Volume path is not supported.](#description-volume-path-is-not-supported)
  - [Solution](#solution)
- [Deprecated error codes](#deprecated-error-codes)
  - [DK0007: Couldn’t download Docker.](#dk0007-couldnt-download-docker)
  - [DK0028: You didn’t grant permission for edit the host file.](#dk0028-you-didnt-grant-permission-for-edit-the-host-file)
  - [DK0057: We cannot display emails on computers with M1 chip.](#dk0057-we-cannot-display-emails-on-computers-with-m1-chip)

---

Below are errors with descriptions and solutions that you may see if an issue occurs in DevKinsta. Give the suggested solutions a try, and if the issue persists, report it to the [DevKinsta Community Forum](https://community.kinsta.com/c/devkinsta/bug-reports/).

## Viewing the application log file

Checking the application log file (main.log) is sometimes recommended for investigating errors. This log file can be accessed from the Help and Support screen in DevKinsta; click the question mark (?) icon in the left sidebar, then click **Reveal log file in File Manager** under the **Support forum** heading. On macOS, you can also go to **Help** > **Reveal log** file in the DevKinsta application menu at the top of the screen.

If you’re unable to start DevKinsta and access the log file through the Help and Support screen, you can open and view the log file manually on your computer. The path to the application log file (main.log) varies slightly between operating systems.

### Windows

```
%userprofile%\AppData\Roaming\DevKinsta\logs
```

### Mac

```
/Users/<yourusername>/Library/Logs/DevKinsta
```

### Linux

```
~/.config/DevKinsta/logs on Ubuntu
```

## DK0001

### Description: Not enough free disk space.

During certain actions (DevKinsta installation, site creation, site import from MyKinsta, etc.), DevKinsta checks the currently available disk space. This error appears when there is not enough disk space on your local machine.

### Solution

Free up disk space on your computer, and repeat the action that caused the initial error.

## DK0002

### Description: There is no internet connection.

During certain actions (DevKinsta installation, site import from MyKinsta, etc.), DevKinsta checks for a stable Internet connection. This error appears if your local machine is not connected to the Internet.

### Solution

Ensure your computer is connected to the Internet, and repeat the action that caused the initial error.

## DK0003

### Description: Couldn’t install Docker.

This error appears when DevKinsta can’t install Docker Desktop; this may be due to insufficient system resources.

### Solution

Ensure your computer aligns with the [system requirements](https://kinsta.com/docs/devkinsta/devkinsta-getting-started/installation) and try to install Docker Desktop manually. For more information about installing Docker Desktop manually, refer to Docker’s installation guides for [Mac](https://docs.docker.com/desktop/install/mac-install/), [Windows](https://docs.docker.com/desktop/install/windows-install/), or [Linux](https://docs.docker.com/desktop/install/linux-install/). When you have installed Docker Desktop, restart DevKinsta.

## DK0004

### Description: Couldn’t start Docker. Please try to start Docker manually.

DevKinsta couldn’t start Docker Desktop.

### Solution

Start Docker Desktop manually and then restart DevKinsta.

## DK0005

### Description: Couldn’t create Docker containers.

DevKinsta couldn’t create the Docker containers.

### Solution

Restart Docker Desktop manually and then restart DevKinsta.

## DK0006

### Description: Couldn’t download Docker images.

DevKinsta couldn’t load the required Docker images; this is usually due to an unstable internet connection.

### Solution

Check your internet connection. If it is stable, restart DevKinsta.

## DK0008

### Description: Couldn’t fetch IP.

DevKinsta couldn’t find Docker’s IP address.

### Solution

Restart Docker Desktop manually and then restart DevKinsta.

## DK0009

### Description: Can’t start Docker container

DevKinsta couldn’t start Docker containers.

### Solution

Stop the DevKinsta-related Docker containers using the following command and then restart DevKinsta.

```
docker kill devkinsta_fpm && docker kill devkinsta_nginx && docker kill devkinsta_adminer && docker kill devkinsta_db && docker kill devkinsta_mailhog
```

## DK0010

### Description: Couldn’t load Docker images.

DevKinsta couldn’t load the required Docker images; this is usually due to an unstable internet connection.

### Solution

Check your internet connection. If it is stable, please try to restart DevKinsta.

## DK0011

### Description: Unknown server error occurred. Please try it again.

You may see this error if DevKinsta cannot access the Kinsta API.

### Solution

Check your Internet connection to see if there are any issues, and check the [Kinsta Status](https://status.kinsta.com/) page to see if there are any issues with the Kinsta API. If the problem still occurs, try again later.

## DK0012

### Description: Your request timed out. Please try it again.

You may see this error if DevKinsta is unable to access the Kinsta API due to a timeout.

### Solution

Check your Internet connection to see if there are any issues, and check the [Kinsta Status](https://status.kinsta.com/) page to see if there are any issues with the Kinsta API. If the problem still occurs, try again later.

## DK0013

### Description: Remote server received wrong data. Please try it again.

You may see this error if DevKinsta receives a bad request error from the Kinsta API.

### Solution

Please report this error to the [DevKinsta Community Forum.](https://community.kinsta.com/c/devkinsta/bug-reports/)

## DK0014

### Description: You are unauthenticated. Please try to re-login into MyKinsta account.

You may see this error if DevKinsta receives an unauthorized request error from the Kinsta API.

### Solution

In DevKinsta, click **Settings**, within **MyKinsta account**, click **Log in to MyKinsta**, enter your credentials to log in, and retry the process.

## DK0015

### Description: You don’t have permission for this action.

You may see this error if DevKinsta encounters a MyKinsta permissions error when accessing the Kinsta API.

### Solution

Go to your [MyKinsta profile](https://my.kinsta.com), and ensure you have the necessary site permissions.

## DK0016

### Description: Couldn’t find remote server. Please try it again.

You may see this error if DevKinsta receives a 404 error from the Kinsta API.

### Solution

Please report this error to the [DevKinsta Community Forum.](https://community.kinsta.com/c/devkinsta/bug-reports/)

## DK0017

### Description: You made too many requests. Please try it again a few minutes later.

You may see this error if DevKinsta encounters a “too many requests” error from the Kinsta API. This error occurs when the Kinsta API is called too frequently.

### Solution

Wait a few minutes, and try the action again.

## DK0018

### Description: You didn’t grant permission for site deletion.

You may see this error if DevKinsta is unable to delete a site due to incorrect permissions to perform the deletion action.

### Solution

| Windows | macOS |
| --- | --- |
| Delete the site again and approve the Windows confirmation dialog. | Delete the site again, and provide your correct password when prompted by macOS. |

## DK0019

### Description: NGINX configuration failed

You may see this error if DevKinsta is unable to update the Nginx configuration file.

### Solution

Restart DevKinsta and recreate the site. If that does not work, check the **sites.ini** file in your **projectFolder/kinsta** folder with a text editor, and remove any duplicate entries.

## DK0020

### Description: Database creation failed

You may see this error if DevKinsta is unable to create the MySQL database due to an invalid database name. The database name is derived from the site name.

### Solution

Recreate the site with a different name. If that does not work, try restarting DevKinsta.

## DK0021

### Description: WordPress site setup failed

You may see this error if DevKinsta is unable to install WordPress.

### Solution

Restart DevKinsta and recreate the site.

## DK0022

### Description: Host file update failed

During site creation, DevKinsta couldn’t update the `hosts` file. You may see this error if DevKinsta is unable to update the computer’s `hosts` file.

### Solution

| Windows | macOS |
| --- | --- |
| Recreate the site and approve the Windows confirmation dialog. | Recreate the site and provide your correct password when prompted by macOS. |

## DK0023

### Description: Can’t add certificate to Keychain

You may see this error if DevKinsta is unable the store the security certificate in the macOS Keychain.

### Solution

Recreate the site and ensure you provide the correct password to the macOS dialog prompt.

## DK0024

### Description: Can’t write to Certificate store

You may see this error if DevKinsta is unable to store the security certificate in the Windows certificate manager.

### Solution

DevKinsta must be run in Administrator mode for the certificate to be created. Recreate the site and ensure you provide the correct password in the Windows confirmation dialog.

## DK0025

### Description: Can’t download site

You may see this error if DevKinsta is unable to pull a site from Kinsta.

### Solution

Restart DevKinsta, click **Settings**, within **MyKinsta account**, click **Log in to MyKinsta**, enter your credentials to log in, and pull the site again.

## DK0026

### Description: Site push failed

You may see this error if DevKinsta is unable to push a site from Kinsta.

### Solution

Restart DevKinsta, click **Settings**, within **MyKinsta account**, click **Log in to MyKinsta**, enter your credentials to log in, and push the site again. If the issue continues, check the application log file (main.log). Search for the error code (DK0026) in the log file to narrow down the search, which may lead to some more detailed information on the root cause.

If the error persists, please report this error to the [DevKinsta Community Forum](https://community.kinsta.com/c/devkinsta/bug-reports/).

## DK0027

### Description: Missing host file entry

You may see this error if there is a missing `hosts` file entry. In this case, you won’t be able to open this site via domain name.

### Solution

Click on the **Fix this** button.

## DK0029

### Description: Can’t create mysql dump

You may see this error if, during site pull, DevKinsta is unable to create a MySQL dump on the remote server.

### Solution

Try it again later. If it still doesn’t help, please report this error to the [DevKinsta Community Forum](https://community.kinsta.com/c/devkinsta/bug-reports/).

## DK0030

### Description: OPERATION INTERRUPTED

You may see this error if you close DevKinsta during site creation.

### Solution

Click on the **Retry** button. If DevKinsta cannot recreate the site, delete and recreate the site.

## DK0031

### Description: Port 80 or 443 is used.

You may see this error if port `80` is used.

### Solution

Close the process using port `80` using one of the following commands:

#### find & kill process on macOS

```
# find & kill processes which are using port 80
sudo lsof -i tcp:80 | grep LISTEN | awk '{print $2}' | xargs kill -9
```

#### find & kill process on Windows

```
# find processes which are using port 80
netstat -ano | findstr :80

# kill process by PID. replace "<PID>" with result from the above command.
taskkill /PID <PID> /F
```

## DK0032

### Description

You may see this error on Windows if WSL2 is not installed or enabled.

### Solution

Restart DevKinsta to initiate the WSL2 installation automatically. If DevKinsta is unable to install WSL2, you can [download it](https://docs.microsoft.com/en-us/windows/wsl/install-win10) directly from Microsoft.

## DK0033

### Description: Can’t connect to database

This error occurs when DevKinsta is unable to connect to the MySQL database.

### Solution

Follow the steps below to resolve this error.

1. Export your site’s database with Adminer. (optional)
2. Close DevKinsta.
3. Run this command in the terminal – `docker container rm devkinsta_db && docker volume rm devkinsta_db_data`.
4. Start DevKinsta.
5. Import the database with Adminer. (optional)

## DK0034

### Description: Please restart your computer to finish installation.

This error occurs when a computer restart is required.

### Solution

Restart the computer and launch DevKinsta.

## DK0035

### Description

This error occurs on Windows if DevKinsta is unable to download WSL2 during the installation process.

### Solution

Restart DevKinsta to initiate the WSL2 download again. If DevKinsta is unable to download and install WSL2, you can [download it](https://docs.microsoft.com/en-us/windows/wsl/install-win10) directly from Microsoft.

## DK0036

### Description

This error occurs if the Windows Subsystem for Linux (WSL2) feature is not enabled.

### Solution

Enable WSL2 by following [Microsoft’s documentation](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

## DK0037

### Description: Container not found

This error can occur because the Docker container doesn’t exist.

### Solution

Follow any instructions provided in the error message. If instructions are not provided or do not resolve the error, restart DevKinsta.

## DK0038

### Description: Set WP config

This error occurs when the wp-config.php file is missing or misconfigured.

### Solution

Click on the **Retry** button shown in DevKinsta.

## DK0039

### Description: Docker stops common

This error appears when Docker stops, and DevKinsta can’t communicate with it.

### Solution

Restart Docker Desktop manually and then restart DevKinsta.

## DK0040

### Description: Could not renew the ssh key.

You may see this error when DevKinsta tries to renew the SSH key during site import.

### Solution

Check your Internet connection to see if there are any issues, and check the [Kinsta Status](https://status.kinsta.com/) page to see if there are any issues with the Kinsta API. If the problem still occurs, try again later.

## DK0041

### Description: Invalid TwoFA. Only Authy and TOTP TwoFA are supported.

This error appears when an incorrect two-factor authentication(2FA) method is used. DevKinsta only supports Authy or Time-based one-time password (TOTP) authentication.

### Solution

Use a supported 2FA method, such as [Authy](https://authy.com/), [Google Authenticator](https://support.google.com/accounts/answer/1066447?hl=en&ref_topic=2954345&sjid=14534610332764139945-EU), or [1Password](https://support.1password.com/one-time-passwords/).

## DK0044

### Description: Can’t write to Certificate store

You may see this error when DevKinsta tries to create a local certificate on the system for your site.

### Solution

Recreate the site and ensure you provide the correct password on the Linux dialog prompt.

## DK0045

### Description: Certificate is not verified

You may see this error when DevKinsta tries to create a local certificate, but the verification process fails due to an already existing certificate in the database.

### Solution

For advanced users: Find and manually delete the corresponding certificates from your database located at “home/yourusername/.pki/nssdb/cert9.db”

## DK0046

### Description: Failed to install certutil package

You may see this error when DevKinsta tries to install missing packages that are necessary to create and manage certificates on your Linux system.

### Solution

Open a terminal window and run `sudo apt update`, then retry the SSL creation in DevKinsta. You can also try to manually install the necessary packages by running `sudo apt install libnss3-tools` or by combining the two commands by running `sudo apt update && apt install libnss3-tools`. To check if the installation was successful, run `certutil` in the terminal and check the output.

## DK0047

### Description: DevKinsta couldn’t overwrite sites.ini. Site creation is failed.

You may see this error when DevKinsta wants to overwrite the **sites.ini** file in your DevKinsta root Folder.

### Solution

Navigate to your root DevKinsta folder, open the **kinsta** folder, delete the **sites.ini** file, and then start DevKinsta.

## DK0048

### Description: You don’t have the necessary privileges to start the Docker client. Please set the required permissions and try again.

You may see this error if you use Linux and the Docker client does not have the necessary privileges or permissions to start on your system.

### Solution

You need to check your user profile to ensure you have the necessary permissions to run the Docker client.

To temporarily give permissions to your user profile (for the current session only), run `sudo chmod 666 /var/run/docker.sock` in the terminal and click **Retry** in DevKinsta to continue the startup process.

If you want to set the permissions permanently (recommended), add your user profile to the Docker group by following the steps below.

1. Make sure the Docker group exists by running `sudo groupadd docker` in the terminal.
2. Run the `groups` command to check if your user is added to the Docker group.
3. If you need to add your user to the Docker group, run `sudo usermod -aG docker $USER`.
4. Run `sudo chmod 666 /var/run/docker.sock` to set the permission.
5. Log in and log out in order for the changes to take effect.

## DK0049

### Description: Could not delete site’s content.

You may see this error if the **devkinsta_nginx** Docker container is not running when you are trying to delete a site’s content.

### Solution

Make sure that **devkinsta_nginx** is running and try again.

## DK0050

### Description: Could not delete site entry from sites.ini.

You may see this error if the **devkinsta_nginx** Docker container is not running when you are trying to delete the site’s entry from the sites.ini file.

### Solution

Make sure that **devkinsta_nginx** is running and try again.

## DK0051

### Description: Could not delete the database.

You may see this error when the site’s database cannot be deleted due to internal problems.

### Solution

You can manually delete the database using the CLI by running the following command in the terminal:

```
docker exec devkinsta_db bin/sh -c 'mysql -u root -p[YOUR_DB_PASSWORD] -e "drop database [YOUR_SITE];"'
```

You can check whether the database has been deleted or not by running the following command in the terminal:

```
docker exec devkinsta_db bin/sh -c 'mysql -u root -p[YOUR_DB_PASSWORD] -e "show databases;"'
```

## DK0052

### Description: Could not save php.ini content

You may see this error if the **devkinsta_fpm** container is not running when trying to save your changes in the php.ini editor.

### Solution

Make sure the **devkinsta_fpm** container is up and running, and try again.

## DK0053

### Description: Could not save php.ini content

You may see this error if the **devkinsta_fpm** container fails to restart after updating the **php.ini** file.

### Solution

Click **Retry**; if this does not resolve the issue, you can start the container manually or restart DevKinsta.

## DK0054

### Description: Could not update sites.ini with the new ports.

You may see this error if the **devkinsta_nginx** container is not running while you are trying to update the **sites.ini** file with the new ports you selected.

### Solution

Make sure that the **devkinsta_nginx** container is running and try again.

## DK0055

### Description: Could not recreate Nginx container with new ports.

You may see this error when DevKinsta is not able to recreate the **devkinsta_nginx** container on the new ports you selected.

### Solution

Click **Retry**; if this does not resolve the issue, relaunch DevKinsta or recreate the **devkinsta_nginx** container yourself using the Docker CLI.

For example, to create the container on ports 80 and 443 on macOS, and Linux, you can run the following command in the terminal, replacing or setting the `${LATEST_IMAGE_VERSION}` variable with the latest version of our DevKinsta Docker image:

```
docker run --network devkinst_network --name devkinsta_nginx \\
-p 80:80 -p 443:443 \\
-v "[YOUR_HOME_PATH]/kinsta:/kinsta" \\
-v "[YOUR_HOME_PATH]/logs:/www/kinsta/logs" \\
-v "[YOUR_HOME_PATH]/private:/www/kinsta/private" \\
-v "[YOUR_HOME_PATH]/public:/www/kinsta/public" \\
-v "[YOUR_HOME_PATH]/ssl:/www/kinsta/ssl" \\
-d kinsta/devkinsta_nginx:${LATEST_IMAGE_VERSION} \\
```

On Windows, you can use the same command without the linebreaks and the `\\` separators.

To get the latest version of our images, run:

```
docker image ls --filter=reference='kinsta/devkinsta_*'
```

## DK0056

### Description: Could not update site URLs with new ports.

You may see this error if **devkinsta_fpm** is not running when you try to rename the site’s URLs after you select the new ports.

### Solution

Make sure that **devkinsta_nginx** and **devkinsta_fpm** containers are up and running.

## DK0058

### Description: Failed to copy the site folder.

When you rename a site in DevKinsta, it copies the site to a new folder with the new name, runs a search and replace on the copied site to update the name within all of the files (for example, the database, PHP files, NGINX configs, etc.), and then deletes the original site that was copied.

This error appears when you rename a site, and DevKinsta cannot copy the files to the new folder.

### Solution

Navigate to the **DevKinsta/public** folder, delete the folder with the new site name and retry the renaming process in DevKinsta.

## DK0059

### Description: Failed to copy the database.

When you rename a site in DevKinsta, it copies the site to a new folder with the new name, runs a search and replace on the copied site to update the name within all of the files (for example, the database, PHP files, NGINX configs, etc.), and then deletes the original site that was copied.

This error appears when DevKinsta cannot copy the database during site renaming.

### Solution

Delete the newly created site’s database and retry the renaming process in DevKinsta.

## DK0060

### Description: Failed to update the database.

When you rename a site in DevKinsta, it copies the site to a new folder with the new name, runs a search and replace on the copied site to update the name within all of the files (for example, the database, PHP files, NGINX configs, etc.), and then deletes the original site that was copied.

This error appears when DevKinsta cannot update the URLs, domains, and emails in the new site database when renaming the site.

### Solution

Check if the database exists. If not, try to create it manually and copy the old site data.

## DK0061

### Description: Failed to delete the old site’s data.

When you rename a site in DevKinsta, it copies the site to a new folder with the new name, runs a search and replace on the copied site to update the name within all of the files (for example, the database, PHP files, NGINX configs, etc.), and then deletes the original site that was copied.

You may see this error when DevKinsta fails to delete the old site’s data when renaming the site.

### Solution

Retry the site renaming and ensure you provide the correct password.

## DK0062

### Description: Failed to add certification to the store.

You may see this error when DevKinsta tries to create a local certificate on the system for your site.

### Solution

Retry the site renaming and ensure you provide the correct password. DevKinsta needs to be in Administrator mode on Windows.

## DK0063

### Description: Failed to restart a Docker container

You may see this error when DevKinsta fails to restart a Docker container.

### Solution

You can restart the container manually in Docker Desktop or in the terminal (replace `<container>` with the container name):

```
docker start <container>
```

## DK0064

### Description: Couldn’t remove remote files.

You may see this error when something changes in your remote environment that makes DevKinsta unable to perform the file deletion command (`rm`) on the remote site’s file system.

Such changes may be:

- Permission changes (DevKinsta does not have permission to remove some files).
- Folder structure changes (the name of the remote site’s root folder has changed since the pull).

### Solution

Pull the remote site again and apply the changes on the new site (e.g. copy and paste the modified files or database), then push again. If that doesn’t resolve the issue, log out and log back in again.

If the error persists, check the application log file (main.log). Search for the error code (DK0064) in the log file to narrow down the search, which may lead to some more detailed information on the root cause.

## DK0065

### Description: Failed to upload local files

This error occurs when there is an issue uploading the local site to the remote server (your MyKinsta environment’s folder). This can be caused by a failed connection to the remote server or unpredictable issues related to the uploaded files.

Note that this step uses `rsync` as a tool to share files with the remote site, so anything that can cause `rsync` to fail can be the root cause of this issue.

### Solution

Log out of MyKinsta in DevKinsta, and then log back in. If it still doesn’t work, pull the remote site again and apply the changes on the new site (e.g. copy and paste the modified files or database), then push again.

If the error persists, check the application log file (main.log). Search for the error code (DK0065) in the log file to narrow down the search, which may lead to some more detailed information on the root cause. If that search doesn’t show any useful information, then try searching for `rsync`.

## DK0066

### Description: Failed to import database dump

This error means that DevKinsta was unable to import the local database dump into your MyKinsta site’s database.

Possible root causes:

- The local database dump was not created (this is unlikely as it would usually fail on the Create MySQL dump step).
- Your remote database does not exist or is down for some reason.

### Solution

Investigate your MyKinsta site’s database and file system to see if your database is working properly. If not, there is an issue on the server side, and our [Support team](https://kinsta.com/docs/support/contact-support/) can help with this.

If your site’s database is working properly, then there was likely an issue on the DevKinsta side. Investigate the application log file (main.log) and search for the error code (DK0066), which may lead to some more detailed information on the root cause.

## DK0067

### Description: Failed to run search and replace

Search and replace is a WP-CLI command (WP-CLI is the command line interface for WordPress) that makes it possible to replace all occurrences of a string in the site’s database. We use it to overwrite the local site’s URL with the remote site’s original URL (to keep the site accessible after the push).

If this error occurs, it may be due to one of the following:

- WP-CLI is unavailable or not working in your site’s folder on the remote server (MyKinsta).
- Your remote database is down.

### Solution

Check if [WP-CLI](https://kinsta.com/docs/devkinsta/wp-cli) is working on your remote (MyKinsta) site. If WP-CLI works but reports database-related issues, then your site is not [connecting to the database properly](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/fix-error-establishing-a-database-connection-in-wordpress). Review the database settings in your site’s **wp-config.php** file and confirm the database details are correct.

If your remote database is down, contact our [Support team](https://kinsta.com/docs/support/contact-support/) to help resolve that issue.

If the solutions suggested above do not resolve the issue, we recommend restoring a recent backup.

## DK0068

### Description: Failed to create site backups when trying to change ports.

We back up sites before we change the port so we can roll back in the event of an error. The error is usually related to zipping or file system issues. The backup is created in the **temp** directory in the “backup” folder.

### Solution

Make sure the **temp** directory and backup folder exist and that you have write permissions.

## DK0070

### Description: Failed to delete DNS record.

Couldn’t delete a site’s URL from the DNS server of the FPM container.

### Solution

You can delete the URL manually with the following command (replace http://example.com with the URL you want to delete):

```
docker exec devkinsta_fpm dns_server delete -d http://example.com
```

## DK0071

### Description: Failed to add DNS record.

Couldn’t add a site’s URL to the DNS server of the FPM container.

### Solution

Restart DevKinsta and click **Retry**. The DNS record should be created during the startup process.

## DK0072

### Description: Could not delete site config file

This error occurs when you try to delete or rename a site, but DevKinsta cannot delete the **sitename.conf** file stored in **DevKinsta/nginx_sites**.

### Solution

The most common reason this happens is due to permission issues, so you may need to delete the file manually.

## DK0073

### Description: Could not restart Nginx service

The Nginx service must be restarted when a site is created, renamed, or deleted. This error appears if the restart fails.

### Solution

To restart the Nginx container manually, open a terminal window and run the following:

```
docker stop devkinsta_nginx
docker start devkinsta_nginx
```

Checking Nginx logs or DevKinsta logs may provide more details as to why the restart failed.

## DK0074

### Description: Failed to create site backup.

The site backup is an archived (zipped) version of a site in the **temp** folder on your local computer. This error is rare and occurs only in edge cases, such as running out of disk space or incorrect permissions on the **temp** folder.

### Solution

Review permissions for your **temp** folder and check to ensure there is enough space on the disk, especially in the case of larger sites.

## DK0075

### Description: Failed to restore the site backup.

Restoration can fail if the site’s folder is not writeable for some reason. Another reason for failure can be that the zip creation was not successful when creating the backup.

### Solution

1. Check if the site backup exists in the **temp** folder.
2. If the backup exists, then it can be manually extracted into the site’s folder.

To help prevent this issue, sync the site regularly to MyKinsta or use a [version control system such as Git](https://kinsta.com/blog/git-vs-github/) to track changes and allow you to restore from previous versions.

## DK0076

### Description: Couldn’t install WordPress plugin

DevKinsta sometimes needs to install plugins, and this error appears when DevKinsta can’t install a WordPress plugin for a given site.

### Solution

This can be fixed by manually installing the plugin via [WP-CLI](https://kinsta.com/docs/devkinsta/wp-cli).

## DK0077

### Description: Couldn’t remove WordPress plugin

DevKinsta sometimes needs to remove plugins, and this error appears when DevKinsta can’t remove a WordPress plugin from a given site.

### Solution

This can be fixed by manually removing the plugin via [WP-CLI](https://kinsta.com/docs/devkinsta/wp-cli).

## DK0078

### Description: Couldn’t update WordPress option

DevKinsta couldn’t update one of the WP options in the site database using a WP-CLI command.

### Solution

This can be fixed by manually updating the option via [WP-CLI](https://kinsta.com/docs/devkinsta/wp-cli).

## DK0081

### Description: Parsing wp-config.php file failed.

You may see this error when importing a site backup file if one of the following happens:

- `wp-config.php not found`  
  This means DevKinsta cannot find **wp-config.php** file in the backup.
- `Invalid database settings. Cannot find DB_NAME variable`  
  This means DevKinsta couldn’t extract the database name out of **wp-config.php**.
- `{dbName}.sql not found`  
  This means **wp-config.php** is okay, but the database backup file cannot be found in the folder or zip file.

### Solution

In any of the above situations, check the site backup file and make sure:

- **wp-config.php** exists in the root folder.
- The `define( 'DB_NAME', '{dbName}' );` line exists in the file.
- A .**sql** file named exactly as mentioned in config file **{dbName}.sql** exists in the root folder.

## DK0082

### Description: Load remote file system error.

This error occurs when DevKinsta fails to load the file system tree of the remote site when doing a selective pull; an SSH key issue usually causes it.

### Solution

Log in again, and if the error persists, remove your “.ssh” folder and try to log in again. If that doesn’t work, contact our [Support team](https://kinsta.com/docs/support/contact-support/) to help resolve that issue.

## DK0083

### Description: Volume path is not supported.

This error only occurs on Windows when Docker uses Windows Subsystem for Linux (WSL2). When using WSL2, DevKinsta creates folders in a location dedicated to the Linux subsystem to improve performance. Different Docker, Windows, and WSL2 versions use different paths for this dedicated part of the file system, and this error can appear when DevKinsta does not support the file system path.

### Solution

Check the paths of the volume on your computer. If the path is not supported, update Windows or Docker to migrate the file system to a new, supported location.

## Deprecated error codes

The following error codes do not occur in the latest version of DevKinsta. If you receive any of the following errors, ensure you [upgrade to the latest version](https://kinsta.com/devkinsta/download/).

### DK0007: Couldn’t download Docker.

### DK0028: You didn’t grant permission for edit the host file.

### DK0057: We cannot display emails on computers with M1 chip.
