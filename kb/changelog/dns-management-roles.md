---
url: "https://kinsta.com/changelog/dns-management-roles/"
title: "A new option for sharing the management of DNS in MyKinsta"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2024-04-09T13:50:54"
change_signal: "2024-04-09T13:50:54"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "ab4bc765714038c7c6eb82a8379649bc2897a16dd3c403b06b3e8b2d744ad623"
body_chars: 3927
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# A new option for sharing the management of DNS in MyKinsta

**Product:** Changelog
**Source:** https://kinsta.com/changelog/dns-management-roles/
**Kinsta last updated:** 2024-04-09T13:50:54

---

Kinsta’s [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/) customers now have increased flexibility when managing [DNS](https://kinsta.com/blog/what-is-dns/) records associated with their website domains.

Previously, access to settings for those using our free Kinsta DNS service required a company-level role for users (Company Owner, Company Administrator, or Company Developer). Customers now have the option of assigning [management of DNS records](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/) to site-specific administrators.

This change should be helpful to organizations that need to share responsibility for DNS management across larger teams and to agencies that hand off that task to their own customers.

While our customers can choose any DNS provider for websites hosted with Kinsta, our free service is built on the [Amazon Route 53](https://aws.amazon.com/route53/) network of DNS servers.

With our latest update to DNS management within the [MyKinsta dashboard](https://kinsta.com/mykinsta/), customers can assign access to DNS records to individuals with the role of Site Administrator. You can do this when adding a domain to Kinsta’s DNS service or later when settings for an existing domain are updated.

## How to give Site Administrators access to DNS records

When first adding a domain to DNS Management within MyKinsta, you will see an option to **Link WordPress site** within the **Add domain** dialog:

![Screenshot of the dialog for linking a WordPress site to a domain name.](https://kinsta.com/wp-content/uploads/2024/04/link-site-while-adding-domain-mykinsta.png)

Linking a WordPress site to a domain name.

When a website is linked to a domain in this way, any individual assigned to the site as a Site Administrator can edit the domain’s DNS records.

Alternatively, you can set up this relationship later by choosing **DNS** in MyKinsta’s main menu and then clicking on the name of the domain you want to update. That will invoke the **DNS Management** page, on which you can click the **Add site** button in the **Linked WordPress site** block:

![Screenshot showing a website being linked to an existing domain.](https://kinsta.com/wp-content/uploads/2024/04/link-site-existing-domain-mykinsta.png)

Linking a WordPress site to an existing domain under **DNS Management**.

Linking a site to a domain here also gives any associated Site Administrator access to its DNS records.

When a website is linked to a domain supported by Kinsta DNS, its Site Administrators will see **DNS** as a menu entry in MyKinsta and can add and edit individual DNS records using the dialog shown below:

![Screenshot of the dialog used to add and edit DNS records in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/04/add-record-site-administrator-mykinsta.png)

The dialog for managing DNS records in MyKinsta.

## How Kinsta helps websites stand out

Amazon’s Route 53 DNS hosting is just one example of the premium services Kinsta harnesses to bring our customers’ websites up to speed without additional fees.

We also choose the [fastest servers](https://kinsta.com/changelog/google-c3d-machines/) available in each data center behind the [Google Cloud Platform](https://kinsta.com/blog/cloud-platform-for-developers/). Then we [integrate with Cloudlfare](https://kinsta.com/blog/cloudflare-integration/) to optimize performances further with a [global CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/), [edge caching](https://kinsta.com/changelog/edge-caching/), [early hints](https://kinsta.com/changelog/early-hints/), and [image optimization](https://kinsta.com/changelog/wordpress-image-optimization/).

Add 24/7/365 support from real humans and options like a [REST API](https://kinsta.com/docs/kinsta-api/) for more flexible site management and it’s clear that Kinsta is ready to power the most demanding WordPress properties.
