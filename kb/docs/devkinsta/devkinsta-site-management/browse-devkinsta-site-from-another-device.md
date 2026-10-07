---
url: "https://kinsta.com/docs/devkinsta/devkinsta-site-management/browse-devkinsta-site-from-another-device/"
title: "Site Management - Access from Another Device"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-site-management"
section: []
kinsta_last_updated: "July 18, 2024"
sitemap_lastmod: "2024-07-18T08:37:07+00:00"
fetched_at: "2026-10-07T22:38:04Z"
sha256: "c44c389a293ed9838c65a5af0b6deeaf610e6160fc1d45c418c2734c0fc8e9b9"
body_chars: 4783
extracted_with: "main article"
status: "live"
---

# Site Management - Access from Another Device

**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-site-management/browse-devkinsta-site-from-another-device/
**Kinsta last updated:** July 18, 2024

## On this page

- [Find the host device’s network IP address](#find-the-host-devices-network-ip-address)
- [Option 1: Desktops and routers](#option-1-desktops-and-routers)
- [Option 2: Mobile devices](#option-2-mobile-devices)
  - [Update wp-config.php to allow normal navigation using the IP address](#update-wp-configphp-to-allow-normal-navigation-using-the-ip-address)

---

The following instructions are for browsing your [DevKinsta-created site](https://kinsta.com/docs/devkinsta/devkinsta-getting-started/creating-a-site/) on another device on the same network.

**Important notes:**

- This tutorial includes advanced topics, including editing firewall rules and configuration. If you’re not comfortable making these changes or have any trouble loading your local site, we recommend [working with a developer](https://kinsta.com/blog/hire-wordpress-developer/) or IT professional to set this up.
- All involved devices must be connected to the **same private network**.
- For mobile devices, this will only work on **one site at a time**.
- Network Firewall exceptions for the HTTP/HTTPS ports (usually 80/443) may need to be made on the host machine.

## Find the host device’s network IP address

You can find the host device’s IP address [using several methods](https://www.howtogeek.com/236838/how-to-find-any-devices-ip-address-mac-address-and-other-network-connection-details/).

Opening this IP address in your browser on any device on the network should load an Nginx “404 Not Found” page.

If the site doesn’t load, there is likely a [firewall](https://kinsta.com/blog/what-is-a-firewall/) blocking access to HTTP/HTTPS. In this case, new firewall rules will need to be added to open the ports. Here are links to instructions on doing that in Windows, macOS, and Ubuntu:

- [How To Open a Port in Windows Firewall](https://www.configserverfirewall.com/windows-10/open-a-port-in-windows/)
- [Set firewall access for services and apps](https://support.apple.com/guide/mac-help/block-connections-to-your-mac-with-a-firewall-mh34041/mac#mchlp218b2b0) (macOS)
- [Enable or block firewall access](https://help.ubuntu.com/stable/ubuntu-help/net-firewall-on-off.html.en) (Ubuntu)

## Option 1: Desktops and routers

Accessing your DevKinsta sites from another desktop/laptop requires you to map your hostnames to the network IP address found during the previous step. For example, if the hostname of one of your sites is **mysite.local** then you will need to edit your hosts file to point that hostname to the correct IP address:

`192.168.1.7 mysite.local`

For more details on editing your hosts file, see one of the following guides:

- [How to Edit Hosts File on Windows](https://kinsta.com/blog/edit-hosts-file/#option-2--how-to-edit-hosts-file-on-windows)
- [How to Edit Hosts File on Mac](https://kinsta.com/blog/edit-hosts-file/#option-3--how-to-edit-hosts-file-on-mac)

You can point more than one hostname to your DevKinsta host IP when using this option.

Depending on its capabilities/settings, you can also edit the hosts on your network router to allow all devices to map hostnames correctly.

## Option 2: Mobile devices

If you are unable to edit your device/router’s host settings, you will need to access your DevKinsta site using the host device’s IP address.

1. Decide which site you would like to access, then open its Nginx **.conf** file (***sitename.conf***) in **~/DevKinsta/nginx_sites**  
2. Add `localhost` to the `server_name` line:  
`server_name localhost wordpress.local *.wordpress.local;`  
3. After saving the conf file, restart the **devkinsta_nginx** container either through Docker Desktop or using the command line:  
`docker container restart devkinsta_nginx`

You should now be able to access your locally hosted site from a mobile device on the same network by using the DevKinsta host’s IP address. If you want to point to a different site, remove `localhost` from the **.conf** file you added it to, and add it to the different site’s **.conf** file using the steps above.

### Update wp-config.php to allow normal navigation using the IP address

Once the page is loaded, you may notice broken stylesheets/assets or non-working links. This is due to accessing the site with the IP address instead of the **.local** domain. A quick way to get around this is by adding the following snippet in [your site’s wp-config.php file](https://kinsta.com/blog/wp-config-php/) above the “That’s all, stop editing” line:

Copy

```
define( 'WP_HOME', 'https://'.$_SERVER['HTTP_HOST'] );
define( 'WP_SITEURL', 'https://'.$_SERVER['HTTP_HOST'] );
```

In each value, you can replace https with http if needed, depending on how your [local development environment](https://kinsta.com/blog/install-wordpress-locally/) is configured. Remember that if you try to access the IP Address using HTTPS, the site will show as insecure.

Now your site’s stylesheets/assets and links should work as expected when viewing the site on a mobile device on the same network.

![View your DevKinsta site on a different device.](https://kinsta.com/wp-content/uploads/2022/04/Untitled-3.jpg)

View your DevKinsta site on a different device.
