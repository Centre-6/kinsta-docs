---
url: "https://kinsta.com/docs/devkinsta/devkinsta-troubleshooting/xdebug-support/"
title: "Troubleshooting - Xdebug Support"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-troubleshooting"
section: []
kinsta_last_updated: "July 18, 2024"
sitemap_lastmod: "2024-07-18T08:40:53+00:00"
fetched_at: "2026-10-07T22:36:46Z"
sha256: "aac1c4ceecb0f3be706badc2724e766b0102649f862c86cdc71cbe12ded251ec"
body_chars: 1750
extracted_with: "main article"
status: "live"
---

# Troubleshooting - Xdebug Support

**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-troubleshooting/xdebug-support/
**Kinsta last updated:** July 18, 2024

## On this page

- [Finding your IP address](#finding-your-ip-address)
  - [Mac](#mac)
  - [Windows](#windows)
  - [Linux](#linux)
- [Configure Xdebug with DevKinsta](#configure-xdebug-with-devkinsta)
- [Configure Xdebug with your IDE or editor](#configure-xdebug-with-your-ide-or-editor)

---

[Xdebug](https://xdebug.org/) is a popular general debugging extension for PHP. As a PHP extension, it needs to be installed in DevKinsta’s FPM container, which provides PHP. Starting with DevKinsta 2.8.0, Xdebug is included with the FPM Docker image for DevKinsta.

## Finding your IP address

In order to make the necessary changes to configure Xdebug with your site in DevKinsta, one of the things you’ll need is your IP address.

### Mac

Copy

```
ifconfig -l | xargs -n1 ipconfig getifaddr
```

If that doesn’t return your IP address, try the following:

Copy

```
ipconfig getifaddr en0
```

or

Copy

```
ipconfig getifaddr en1
```

### Windows

Run this command in WSL:

Copy

```
grep nameserver /etc/resolv.conf | cut -d ' ' -f2
```

### Linux

Copy

```
hostname -I | cut -d ' ' -f1
```

## Configure Xdebug with DevKinsta

1. Open DevKinsta and navigate to the Site configurations screen for the site where you want to enable Xdebug.
2. Scroll down to **PHP.ini Editor**, add the following, replacing <youripaddress> with your actual IP address, and click the **Save changes** button:

   Copy

   ```
   xdebug.client_host = <youripaddress>
   ```

## Configure Xdebug with your IDE or editor

In your preferred IDE or code editor, open your site and edit your debugging configuration.

In this example, we’re using Visual Studio Code (aka VS Code), so we’ll edit the **launch.json** file and configure the path to our site. Replace SITE_NAME with the actual folder name of your site.

Copy

```
{
"name": "Listen for Xdebug",
"type": "php",
"request": "launch",
"port": 9000,
"pathMappings": {
"/www/kinsta/public/SITE_NAME": "${workspaceRoot}"
}
}
```

Breakpoints should now work, and you can begin debugging with your IDE or editor.
