---
url: "https://kinsta.com/docs/devkinsta/devkinsta-reference/uninstall-devkinsta/"
title: "Uninstall DevKinsta"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-reference"
section: ["DevKinsta", "Reference"]
kinsta_last_updated: "2026-02-18T05:53:47"
change_signal: "2026-02-18T05:53:47"
fetched_at: "2026-10-07T22:58:20Z"
sha256: "d6cf0afda082954331d7910454205885081f9ac54d6da3a5ea0108f1a33ea08a"
body_chars: 1624
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Uninstall DevKinsta

**Section:** DevKinsta > Reference
**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-reference/uninstall-devkinsta/
**Kinsta last updated:** 2026-02-18T05:53:47

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

```
sudo rm /usr/share/applications/dev-kinsta.desktop
```

## Clean up after removal

There are some folders and Docker containers that require a bit of additional clean-up.

### Docker

On all OS, Docker containers, volumes, and networks starting with **devkinsta_** should be removed.

If you do not need Docker for other applications and wish to remove it too, in Docker Desktop go to **Preferences** > **Troubleshoot** > **Uninstall**.

On Linux, you can also remove Docker with:

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
