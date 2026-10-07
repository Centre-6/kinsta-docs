---
url: "https://kinsta.com/docs/devkinsta/devkinsta-troubleshooting/devkinsta-docker-issues/"
title: "Docker Issues"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-troubleshooting"
section: ["DevKinsta", "Troubleshooting"]
kinsta_last_updated: "2025-04-07T15:17:36"
change_signal: "2025-04-07T15:17:36"
fetched_at: "2026-10-07T22:58:17Z"
sha256: "dff07016257815f23fae85bbb44bdc78f6b2a42df89366184c9e0e82a04c33a5"
body_chars: 2241
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Docker Issues

**Section:** DevKinsta > Troubleshooting
**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-troubleshooting/devkinsta-docker-issues/
**Kinsta last updated:** 2025-04-07T15:17:36

## On this page

- [Check Docker settings](#check-docker-settings)
- [Create the Docker socket symlink](#create-the-docker-socket-symlink)
- [Check for warnings or notifications in Docker Desktop](#check-for-warnings-or-notifications-in-docker-desktop)
- [Remove DevKinsta and Docker and reinstall](#remove-devkinsta-and-docker-and-reinstall)

---

DevKinsta requires Docker to power the web technologies needed for your WordPress site to run locally (Nginx, PHP, etc.). DevKinsta will prompt you to download and install Docker as part of the installation process if you do not already have it installed. 

In some cases, Docker may be installed on your system, but DevKinsta is unable to detect it and prompts you to install Docker when launched. If this occurs, follow the steps below to resolve the issue.

## Check Docker settings

Close DevKinsta, open Docker Desktop, click **Settings** > **Advanced**, and select **Allow the default Docker socket to be used (requires password)**.

![Check the Docker Desktop settings. ](https://kinsta.com/wp-content/uploads/2025/04/docker-desktop-settings-1024x643.png)

Check the Docker Desktop settings.

Close Docker Desktop and open DevKinsta again.

## Create the Docker socket symlink

To ensure the proper symlink is set up for the Docker socket file, run the following command:

```
sudo ln -s “$HOME/.docker/run/docker.sock” /var/run/docker.sock
```

Enter the administrator password, or if your user is an administrator, enter your password. Once this is complete, close and reopen DevKinsta.

## Check for warnings or notifications in Docker Desktop

Within Docker Desktop, check the notifications for any warnings, if there are any, click **Repair**.

If there you have any warnings in the banner across the top of Docker Desktop, click **Re-apply configuration**.

## Remove DevKinsta and Docker and reinstall

To remove DevKinsta and Docker, follow the steps in [Uninstall DevKinsta,](https://kinsta.com/docs/devkinsta/devkinsta-reference/uninstall-devkinsta/) including the steps to clean up after removal.

After uninstalling both DevKinsta and Docker, restart your computer. Then, download and install the latest version of Docker Desktop from the [Docker documentation](https://docs.docker.com/desktop/setup/install/mac-install/). During installation, use the default and recommended settings. You may be prompted to enter your administrator password to allow Docker Desktop to configure properly.

Once Docker Desktop is installed, [reinstall DevKinsta](https://kinsta.com/docs/devkinsta/devkinsta-getting-started/installation/).
