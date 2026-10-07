---
url: "https://kinsta.com/docs/wordpress-hosting/site-management/configuration-changes/"
title: "Configuration Changes"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "site-management"
section: ["WordPress Hosting", "Site Management"]
kinsta_last_updated: "2025-07-01T15:45:03"
change_signal: "2025-07-01T15:45:03"
fetched_at: "2026-10-07T22:58:21Z"
sha256: "c1c533ea773324062a021573556c17415e912024e4d8a5e376ec087190e10bf3"
body_chars: 2901
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Configuration Changes

**Section:** WordPress Hosting > Site Management
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/site-management/configuration-changes/
**Kinsta last updated:** 2025-07-01T15:45:03

## On this page

- [Set up redirects](#set-up-redirects)
- [Block specific IP addresses](#block-specific-ip-addresses)
- [Password protect your site](#password-protect-your-site)
- [Other rules? Contact our Support team](#other-rules-contact-our-support-team)

---

Because Kinsta uses the newer [Nginx web server](https://kinsta.com/blog/what-is-nginx/) instead of Apache, WordPress sites hosted at Kinsta do **not** have a .htaccess file. Instead, you can use tools in [MyKinsta](https://my.kinsta.com/) to replicate much of the important .htaccess functionality like redirects and IP bans.

For other rules, Nginx also offers its own configuration file where similar rules can be set up, though the syntax is different. Our Support team can help you add additional rules as needed to this Nginx configuration file (the equivalent of Apache’s .htaccess file).

## Set up redirects

To create redirects for your site hosted at Kinsta, you can [use the Redirects tool in MyKinsta](https://kinsta.com/docs/wordpress-hosting/redirect-rules/):

![Add a redirect rule in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-redirects-1024x735.png)

Add a redirect rule in MyKinsta.

## Block specific IP addresses

To stop specific IP addresses from accessing your site at Kinsta, you can [use the IP Deny tool in MyKinsta.](https://kinsta.com/docs/wordpress-hosting/site-management/block-ip-address/)

![Add an IP address to deny in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-IP-deny-3.png)

Add an IP address to deny in MyKinsta.

## Password protect your site

To lock down your entire site, you can use our [password protection (htpasswd) tool](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/htpasswd/) in MyKinsta. You can find it under the **Tools** section on your site. Click **Enable**, choose a username and password, and you’re good to go!

![Enable .htpasswd protection.](https://kinsta.com/wp-content/uploads/2025/06/wordpress-tools-password-protection.png)

Enable .htpasswd protection.

After it’s enabled, your WordPress site will then require authentication to access it. You can change the credentials at any time or disable it when you no longer need it.

![Password protection requires signing in before viewing the site in your browser.](https://kinsta.com/wp-content/uploads/2021/11/htpasswd-authentication-prompt.png "Password protection requires signing in before viewing the site in your browser.")

Password protection requires signing in before viewing the site in your browser.

## Other rules? Contact our Support team

Using the Nginx configuration file, it’s also possible to add other configuration rules – like [password protecting a folder](https://kinsta.com/blog/password-protect-wordpress-site/) at the server level or [disabling image hotlinking](https://kinsta.com/blog/hotlinking/).

By default, you cannot edit the Nginx configuration file yourself at Kinsta. However, if you reach out to our [Support team](https://kinsta.com/docs/support/contact-support/), they’ll be happy to help you and add the relevant rule for you. Note: They cannot convert .htaccess to Nginx rules for you.
