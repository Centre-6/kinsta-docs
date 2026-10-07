---
url: "https://kinsta.com/docs/service-information/files-and-database-storage/"
title: "Service Information - Files and Database Storage"
tier: "docs"
product: "service-information"
product_label: "Service Information"
subsection: "files-and-database-storage"
section: []
kinsta_last_updated: "June 15, 2026"
sitemap_lastmod: "2026-06-15T09:47:49+00:00"
fetched_at: "2026-10-07T22:39:10Z"
sha256: "7b19ad0f939935395c060f691bccb7e2a0e89f8a362e3503eed9e7ca92832799"
body_chars: 4040
extracted_with: "main article"
status: "live"
---

# Service Information - Files and Database Storage

**Product:** Service Information
**Source:** https://kinsta.com/docs/service-information/files-and-database-storage/
**Kinsta last updated:** June 15, 2026

## On this page

- [Website access logs](#website-access-logs)
- [MyKinsta tools](#mykinsta-tools)
- [Communication tools](#communication-tools)
- [Kinsta’s CDN and edge caching](#kinstas-cdn-and-edge-caching)
- [Summary](#summary)

---

When you [host a site with Kinsta](https://kinsta.com/why-us/), you choose the [data center](https://kinsta.com/docs/service-information/data-center-locations/) where your site is hosted. Your site’s [files](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-file-manager/) and [database](https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database/) are stored in that data center. Backups may be stored in a different data center within the same geographic region or zone to improve resilience and reliability.

To provide certain features and services, some data related to your site may be securely transferred outside of the selected data center. This article explains when that happens and what data may be involved.

## Website access logs

Kinsta’s hosting platform includes analytics and [security](https://kinsta.com/wordpress-hosting/security/) systems that help us monitor website performance, track usage metrics, and identify potentially malicious activity, such as suspicious login attempts.

To support these functions, information from your website access logs, including visitor IP addresses, is securely transmitted to our analytics infrastructure. This data is retained for up to 30 days as part of our analytics dataset and is then automatically deleted.

## MyKinsta tools

Some tools available in MyKinsta process information related to your site. Depending on the tool, this may include:

- Data from access and error logs
- Visitor IP addresses
- Information retrieved from your database (for example, when using Search and Replace)

To provide these features, the data may be temporarily processed or stored on the infrastructure that powers MyKinsta, which may be located outside your site’s hosting data center.

In some cases, third-party services are involved. For example, when you enable Kinsta’s CDN, your site’s static assets are delivered through Cloudflare’s network. As visitors access those assets, Cloudflare processes and logs requests as part of providing CDN services.

## Communication tools

Kinsta uses various communication systems to provide support and platform services, including live chat, email, and email delivery services.

If you share information with our Support team through chat, email, or other communication channels, that information is stored and processed by the providers that power those services. The same applies to any third-party communication tools used to deliver support or operate our platform.

## Kinsta’s CDN and edge caching

When [Kinsta’s CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/) is enabled, copies of your website’s static assets, such as images, JavaScript, CSS, and other media files, are stored on Cloudflare’s global network to improve performance and availability.

If [Edge Caching](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/) is also enabled, cached HTML versions of your site’s pages are stored on Cloudflare’s network as visitors access them.

We strongly recommend enabling both Kinsta’s CDN and Edge Caching whenever they are compatible with your site. These features can significantly improve performance, reduce latency, and enhance reliability.

If you prefer not to have static assets or cached HTML content stored on Cloudflare’s network, you can disable the CDN (**Sites** > ***sitename*** > **Caching** > **CDN**) or turn off Edge Caching (**Sites** > ***sitename*** > **Caching** > **Edge Caching**).

## Summary

The files and database for your site are stored in the data center you select when creating your site. However, some limited categories of data may be transferred, processed, or stored outside that data center to provide core platform features such as analytics, security monitoring, support services, and content delivery.

If you have questions about how Kinsta processes and stores data, please refer to our [Terms of Service](https://kinsta.com/legal/terms-service/) and [Privacy Policy](https://kinsta.com/legal/privacy-policy/).
