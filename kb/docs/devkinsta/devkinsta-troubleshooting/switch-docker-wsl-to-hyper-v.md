---
url: "https://kinsta.com/docs/devkinsta/devkinsta-troubleshooting/switch-docker-wsl-to-hyper-v/"
title: "Troubleshooting - Windows Issues"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-troubleshooting"
section: []
kinsta_last_updated: "July 18, 2024"
sitemap_lastmod: "2024-07-18T08:42:27+00:00"
fetched_at: "2026-10-07T22:36:47Z"
sha256: "57b6ad34993c136a637d15971830c446a41434911c5368e3344717010fca5eef"
body_chars: 2873
extracted_with: "main article"
status: "live"
---

# Troubleshooting - Windows Issues

**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-troubleshooting/switch-docker-wsl-to-hyper-v/
**Kinsta last updated:** July 18, 2024

## On this page

- [Preparing to switch](#preparing-to-switch)
  - [Option 1](#option-1)
  - [Option 2](#option-2)
  - [Option 3](#option-3)
- [Making the switch to Hyper-V](#making-the-switch-to-hyper-v)

---

A common issue for Windows users is slowness due to Docker using WSL instead of Hyper-V. If you have Windows 10 64-bit: Pro, Enterprise, or Education (Build 16299 or later) — you have the option to use Hyper-V, which is the most reliable way to speed up DevKinsta on Windows.

If Hyper-V isn’t an option in **Turn Windows features on or off** (**Control Panel** > **Programs** > **Programs and Features** > **Turn Windows features on or off**), you’ll need to upgrade Windows to Pro or another version that supports Hyper-V.

## Preparing to switch

Because Docker keeps the WSL and Hyper-V database volumes separate, any databases created when WSL is enabled are not accessible once you switch to Hyper-V. To work around this, you have a couple of options:

### Option 1

1. Export the database(s) of your local site(s) in DevKinsta before switching to Hyper-V.
2. After switching to Hyper-V, import the database(s).

### Option 2

1. [Push any site(s) you have in DevKinsta to Staging](https://kinsta.com/docs/devkinsta/devkinsta-integration/#push-changes-to-staging) (or make backups) before switching to Hyper-V.
2. Reset Docker and completely [uninstall DevKinsta](https://kinsta.com/docs/devkinsta/devkinsta-reference/uninstall-devkinsta/) so that you start fresh.
3. Make sure Hyper-V and Containers Windows features are enabled before reinstalling DevKinsta.
4. [Pull your site(s) from Staging to DevKinsta](https://kinsta.com/docs/devkinsta/devkinsta-integration/#pull-a-site-from-kinsta) (or restore from a backup). Note: When pulling a site from Kinsta, you can choose to pull from any environment, so make sure you’re pulling from the same Staging environment you pushed to above.

### Option 3

This option is only recommended if you haven’t made any changes to your local site(s)

1. Delete your site(s) in DevKinsta before switching to Hyper-V.
2. After switching to Hyper-V, create your site(s) again in DevKinsta.

## Making the switch to Hyper-V

There are several options for enabling Hyper-V on Windows. We’ll walk you through a common method here. For more details and other methods of enabling Hyper-V, see Microsoft’s documentation for [enabling Hyper-V on Windows](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v).

1. Make sure DevKinsta is not running.
2. If your version of Windows doesn’t support Hyper-V, upgrade to Windows Pro or another version that supports Hyper-V.
3. Go to **Control Panel** > **Programs** > **Programs and Features** > **Turn Windows features on or off** and enable the **Hyper-V** and **Container** options.
4. In Docker, go to **Settings** > **General**, disable the **Use the WSL 2 based engine** option, then click **Apply & Restart**.
5. Start DevKinsta (or reinstall if you chose Option 2 above) and let it create and update containers for the new Hyper-V environment.
