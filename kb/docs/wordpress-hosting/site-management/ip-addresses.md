---
url: "https://kinsta.com/docs/wordpress-hosting/site-management/ip-addresses/"
title: "Site Management - IP Addresses"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "site-management"
section: []
kinsta_last_updated: "March 27, 2026"
sitemap_lastmod: "2026-03-27T09:27:32+00:00"
fetched_at: "2026-10-07T22:39:49Z"
sha256: "c4583b7ae4c0bb85202b4c199219ba379951907d671d64f91b9ed50e25609cc1"
body_chars: 2557
extracted_with: "main article"
status: "live"
---

# Site Management - IP Addresses

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/site-management/ip-addresses/
**Kinsta last updated:** March 27, 2026

## On this page

- [Site IP address (IPv4)](#site-ip-address-ipv4)
  - [IP address info](#ip-address-info)
- [External IP address](#external-ip-address)
- [Dedicated IP address](#dedicated-ip-address)

---

## Site IP address (IPv4)

Your Site IP address (IPv4) can be found in [MyKinsta](https://my.kinsta.com/) under your site’s **Info** tab. This is the IP address you’ll need to point your domain to at your DNS provider.

![Site IP Address in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-site-ip-address-2.png)

Site IP Address in MyKinsta.

### IP address info

We use [Cloudflare](https://kinsta.com/cloudflare-integration/) to secure our hosting infrastructure, so the corresponding IP you see for your site is a Cloudflare IP address. This means the owner of the IP address is Cloudflare, Inc., located in the United States of America.

Certain pieces of data related to your website’s visitors, files, and database will necessarily [leave that data center in a few scenarios](https://kinsta.com/docs/service-information/files-and-database-storage/).

## External IP address

The **IP address for external connections** to your WordPress site can be found in [MyKinsta](https://my.kinsta.com) under your site’s **Info** tab.

This is the IP address that other parties see when your site connects to another server. For example, if your site connects to a third-party payment processor like PayPal, you might need to provide PayPal with the external IP address so that they can add the IP to their allowlist on their end.

**The IP address for external connections is different from your Site IP address**. Your [Site IP address](#site-ip-address-ipv4) is the IP address that your domain should be pointed to.

![The IP address for external connections.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-external-site-ip-address.png)

The IP address for external connections.

## Dedicated IP address

We do not offer dedicated IP addresses because they aren’t necessary for most configurations. Since our infrastructure is secured by Cloudflare, sites hosted on Kinsta use a range of [shared IP addresses](https://kinsta.com/docs/wordpress-hosting/wordpress-reference/technical-faq/#do-my-sites-get-a-dedicated-ip) provided by Cloudflare. Our Cloudflare IP addresses are reserved for Kinsta customers only, so you won’t share an IP address with spam or adult sites hosted elsewhere.

If you’re looking for a dedicated IP because you need to add a single IP to an allowlist for a third-party service (maybe a payment processor like PayPal or similar), you’ll want to use your site’s [external IP](#external-ip-address) for that. The external IP address is the one other servers see when your site connects to that other server.
