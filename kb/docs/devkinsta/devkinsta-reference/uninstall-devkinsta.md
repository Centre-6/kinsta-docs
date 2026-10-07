---
url: "https://kinsta.com/docs/devkinsta/devkinsta-reference/uninstall-devkinsta/"
title: "Reference - Uninstall DevKinsta"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-reference"
section: []
kinsta_last_updated: "February 18, 2026"
sitemap_lastmod: "2026-02-18T05:53:47+00:00"
fetched_at: "2026-10-07T22:39:32Z"
sha256: "0a8e704c553bc1bfa3e2192a1dd79e440df688ad3ad5ff44e6985f6fe3b61471"
body_chars: 1636
extracted_with: "main article"
status: "live"
---

# Reference - Uninstall DevKinsta

**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-reference/uninstall-devkinsta/
**Kinsta last updated:** February 18, 2026

## On this page

- [DevKinsta removal](#devkinsta-removal)
  - [Windows](#windows)
  - [Mac](#mac)
  - [Linux](#linux)
- [Clean up after removal](#clean-up-after-removal)
  - [Docker](#docker)
  - [Hosts file](#hosts-file)
  - [Mac](#mac)
  - [Windows](#windows)
  - [Linux](#linux)

---

Follow the instructions given below to uninstall DevKinsta for a fresh start.

## DevKinsta removal

### Windows

Go to **Settings** > **Apps**, search for DevKinsta, and remove it.

### Mac

Open **Finder** and click on **Applications** in the sidebar. Drag and drop the DevKinsta icon into the Trash, or right-click on the DevKinsta icon and choose **File** > **Move to Trash** from the menu that appears.

### Linux

In terminal/command-line, remove the DevKinsta application with:

Copy

```
sudo rm /usr/share/applications/dev-kinsta.desktop
```

## Clean up after removal

There are some folders and Docker containers that require a bit of additional clean-up.

### Docker

On all OS, Docker containers, volumes, and networks starting with **devkinsta_** should be removed.

If you do not need Docker for other applications and wish to remove it too, in Docker Desktop go to **Preferences** > **Troubleshoot** > **Uninstall**.

On Linux, you can also remove Docker with:

Copy

```
sudo apt-get purge docker-ce docker-ce-cli containerd.io
```

### Hosts file

You may also want to remove the entries added to your hosts file by DevKinsta. This will be everything between the `START DEVKINSTA` entries and `END DEVKINSTA` entries in your hosts file.

### Mac

Remove the following folders:

- **User/Library/Application Support/DevKinsta** (application config)
- **User/DevKinsta** (site files)

### Windows

Remove the following folders:

- **User\DevKinsta**
- **User\AppData\Roaming\DevKinsta**
- **User\AppData\Local\dev-kinsta-updater**

### Linux

Remove the following folders:

- **/opt/DevKinsta**
- **~/.config/DevKinsta**
