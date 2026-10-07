---
url: "https://kinsta.com/docs/devkinsta/devkinsta-getting-started/installation/"
title: "Get Started - Installation"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-getting-started"
section: []
kinsta_last_updated: "August 19, 2024"
sitemap_lastmod: "2024-08-19T12:02:13+00:00"
fetched_at: "2026-10-07T22:36:56Z"
sha256: "f8448b5a16795df2e26a8f8ea3c69eecc2db083f4d3030144d0168e06e2d5783"
body_chars: 5930
extracted_with: "main article"
status: "live"
---

# Get Started - Installation

**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-getting-started/installation/
**Kinsta last updated:** August 19, 2024

## On this page

- [Download DevKinsta](#download-devkinsta)
- [DevKinsta requirements and installation](#devkinsta-requirements-and-installation)
  - [Windows](#windows)
    - [Windows 10 64-bit: Pro, Enterprise, or Education (build 16299 or later)](#windows-10-64-bit-pro-enterprise-or-education-build-16299-or-later)
    - [Windows 10 Home (version 1903 or higher)](#windows-10-home-version-1903-or-higher)
    - [Installing on Windows](#installing-on-windows)
  - [Mac](#mac)
    - [Installing on macOS](#installing-on-macos)
  - [Linux](#linux)
    - [Ubuntu 20.04 LTS (or later)](#ubuntu-2004-lts-or-later)
    - [Installing on Linux](#installing-on-linux)
    - [Setting Docker context to Engine](#setting-docker-context-to-engine)

---

Follow the instructions given below to get started with DevKinsta. Alternatively, you can [watch our video](https://kinsta.com/webinars/install-and-use-devkinsta/) to learn how to install and use DevKinsta.

## Download DevKinsta

First, visit the DevKinsta [download page](https://kinsta.com/devkinsta/download/). You’ll need to enter your name and email address to begin the download.

For Mac, choose the installation file for your hardware:

- For Apple silicon Macs: **DevKinsta_arm64.dmg**
- For Intel Macs: **DevKinsta_x64.dmg**

## DevKinsta requirements and installation

Depending on your operating system, follow the instructions outlined below.

### Windows

|  | Minimum | Preferred | Note |
| --- | --- | --- | --- |
| Disk space | 5GB | 10GB |  |
| Memory | 2GB | 4GB |  |
| Docker Desktop | v2.0.0 | >=v4.17.0 | Install or update to the latest version. |

#### Windows 10 64-bit: Pro, Enterprise, or Education (build 16299 or later)

- Enabling the Hyper-V and Containers Windows features is recommended.
- The following hardware prerequisites are required to run Client Hyper-V on Windows 10 successfully:
  - 64-bit processor with Second Level Address Translation (SLAT)
  - 4GB system RAM
  - BIOS-level hardware virtualization support must be enabled in the BIOS settings.

#### Windows 10 Home (version 1903 or higher)

- Enable the WSL 2 feature on Windows. For detailed instructions, refer to the [Microsoft documentation](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
- The following hardware prerequisites are required to run WSL 2 on Windows 10 Home successfully:
  - 64-bit processor with Second Level Address Translation (SLAT)
  - 4GB system RAM
  - BIOS-level hardware virtualization support must be enabled in the BIOS settings.

#### Installing on Windows

1. Double-click on the downloaded file to launch the installer, which will guide you through the setup process. We suggest running the installation with Administrator mode (all users) as it’s needed for permissions to write to the host file and SSL generator.
2. If prompted, download and install Docker Desktop.
3. When you launch the app for the first time, it will need 5-10 minutes (depending on your connection speed) to download dependencies and other items it requires to function. This only needs to be done once, though; any time you re-launch DevKinsta, it’ll take you straight to your site list.
4. Choose **Yes** when Windows requests: **Do you want to allow this app to make changes to your device?**
5. Once installation is complete, feel free to delete the **installer.exe** file.

### Mac

|  | Minimum | Preferred | Note |
| --- | --- | --- | --- |
| Disk space | 5GB | 10GB |  |
| Memory | 2GB | 4GB |  |
| Docker Desktop | v2.0.0 | >=v4.17.0 | Install or update to the latest version. |

- Mac hardware must be a 2010 or a newer model, with either:
  - Intel’s hardware support for memory management unit (MMU) virtualization, including Extended Page Tables (EPT) and Unrestricted Mode.
  - Or Apple silicon’s Virtualization Extensions.

  You can check to see if your machine has this support by running the following command in a terminal:

  Copy

  ```
  sysctl kern.hv_support
  ```

  If your Mac supports the Hypervisor framework, the command prints:  
  `kern.hv_support: 1`
- **macOS must be version 12.0 or newer.** We recommend using the latest version of macOS.

#### Installing on macOS

1. Double-click on the downloaded DMG file. This will create an icon for the installer application and will open it right away.
2. Drag the DevKinsta application in the opened window into the **Applications** folder.
3. You can now launch DevKinsta from your applications. You can also hit **Command + Space** to open Spotlight search and start typing “DevKinsta,” and hit return/Enter once it pops up.
4. If prompted, download and install Docker Desktop.
5. When you launch the app for the first time, it will need 5-10 minutes (depending on your connection speed) to download dependencies and other required items. This only needs to be done once, though; any time you re-launch DevKinsta, it’ll take you straight to your site list.
6. Enter your password when asked.
7. Once done, close the window and delete the DMG file and the installer created.

### Linux

|  | Minimum | Preferred | Note |
| --- | --- | --- | --- |
| Disk space | 5GB | 10GB |  |
| Memory | 2GB | 4GB |  |
| Docker Engine | v2.0.0 | >=v2.5.0 |  |

#### Ubuntu 20.04 LTS (or later)

- Officially, DevKinsta is only supported for Ubuntu.
- You’re free to try it on any other Debian-based distro, but they’re not supported officially as of yet.

#### Installing on Linux

1. Double-click on the downloaded DevKinsta installer file. This will open the installer right away.
2. Proceed with the installation by following the instructions.
3. If prompted, download and install Docker Engine.
4. When you launch the app for the first time, it’ll take 5-10 minutes (depending on your connection speed) to download dependencies and other required items. This only happens the first time you launch DevKinsta. Subsequent launches will take you straight to your site list.
5. Enter your password when asked.
6. Once done, close the window and delete any installation files created.

#### Setting Docker context to Engine

If Docker Desktop and Docker Engine are both installed on Ubuntu, you can only access one of them at a time. Docker context determines which one your Docker client is connected to.

Check which context is currently in use with `docker context list` or `docker context ls`, which will return a list of contexts. The active context is indicated with an asterisk (*).

![A list of Docker contexts, with the active context indicated with an asterisk (*).](https://kinsta.com/wp-content/uploads/2023/03/devkinsta-docker-context-list.png)

To switch the context to Docker Engine, run:

Copy

```
docker context use default
```
