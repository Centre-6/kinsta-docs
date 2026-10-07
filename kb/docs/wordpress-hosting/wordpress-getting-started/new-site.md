---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/new-site/"
title: "Get Started - Add Site"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-getting-started"
section: []
kinsta_last_updated: "October 15, 2025"
sitemap_lastmod: "2025-10-15T10:39:25+00:00"
fetched_at: "2026-10-07T22:38:57Z"
sha256: "e3e3e084719e8254d93aaecce667d17fe2f0ed58820f187e14865bfc71b8ebc1"
body_chars: 8956
extracted_with: "main article"
status: "live"
---

# Get Started - Add Site

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/new-site/
**Kinsta last updated:** October 15, 2025

## On this page

- [Add a new site](#add-a-new-site)
- [Install WordPress](#install-wordpress)
  - [Site name](#site-name)
  - [Data center location](#data-center-location)
  - [WordPress admin email](#wordpress-admin-email)
  - [WordPress admin username](#wordpress-admin-username)
  - [WordPress admin password](#wordpress-admin-password)
  - [WordPress site title](#wordpress-site-title)
  - [Select a language](#select-a-language)
  - [Install WordPress multisite](#install-wordpress-multisite)
- [Empty environment (Without WordPress)](#empty-environment-without-wordpress)
  - [Site name](#site-name)
  - [Data center location](#data-center-location)
- [Clone](#clone)
  - [Environment to clone](#environment-to-clone)
  - [Site name](#site-name)
  - [Data center location](#data-center-location)
- [Completing the process](#completing-the-process)
- [Add a new location](#add-a-new-location)

---

Here at Kinsta, we offer high-performance, enterprise-grade infrastructure to power every Managed WordPress site. Our platform is built on a global network of premium data centers. This means you have access to 30 data centers around the world when launching your WordPress site on Kinsta.

## Add a new site

To add a new Kinsta site, go to **Sites**, then click **Add site** and **Create new site**.

![Create a WordPress site in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-add-site-5.png)

Create a WordPress site in MyKinsta.

Select the type of site you want to create. There are three options.

![Select the site type you want to create at Kinsta.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-add-site-install-wordpress.png)

Select the site type you want to create at Kinsta.

1. **Install WordPress:** This option installs a fully functional WordPress site that is ready for you to use immediately.
2. **Empty environment:** This option installs all the necessary software to run a WordPress site (web server, PHP, MySQL, etc.) but does not install WordPress itself. This is a good option for users [migrating to Kinsta with Duplicator](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrate-wordpress-duplicator-plugin/) or setting up a [Bedrock/Trellis installation](https://kinsta.com/blog/bedrock-trellis/) with a custom file structure.
3. **Clone:** This option allows you to clone an existing staging or live environment to the live environment of a new site.

Make your selection and click **Continue**.

## Install WordPress

The **Install WordPress** option includes several fields to customize your site. Here is what you need to know about each field. Click **Continue** after you complete the fields in each modal.

### Site name

The site name is shown in MyKinsta but isn’t visible to your site’s visitors. It’s also used for the first part of your site’s [temporary domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-temporary-url/) (sitename.kinsta.cloud).

### Data center location

You can select a data center for each of your sites. This is where your data is actually stored and served from. We support 30 locations and recommend [choosing a location](https://kinsta.com/docs/service-information/data-center-locations/) closest to your user base, as this will decrease latency, [TTFB](https://kinsta.com/blog/ttfb/), and load times.

If you have a [dedicated server](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/dedicated-server/), you can choose this from the list of data center locations.

Can’t find the region you’re looking for? If you’re an existing customer, [contact our Account Management team](https://kinsta.com/docs/support/contact-support/#account-management-team-hours). If you’re new to Kinsta or on a free trial, [contact our Sales team](https://kinsta.com/contact-us/).

### WordPress admin email

WordPress uses this email address to send important notifications. It defaults to your Kinsta user’s email address, but you can change it.

### WordPress admin username

You’ll use this to log in to WordPress, and you can add more users later. It defaults to the first part of your email address plus four random characters, but you can change it. For [better security](https://kinsta.com/blog/is-wordpress-secure/), we recommend not using “admin” as your username.

### WordPress admin password

You’ll use this password to log in to WordPress. Strong passwords are enforced automatically. To generate a new one, click the reload icon. You can also [change your WordPress password](https://kinsta.com/blog/change-wordpress-password/) later.

### WordPress site title

Depending on your theme, the site title appears in the browser tab and other places on your site. You can change it in your WordPress settings after the site is created.

### Select a language

Choose the language for your WordPress dashboard. This doesn’t need to match the language of your site’s content.

### Install WordPress multisite

Tick this box if you would like to create a [WordPress Multisite](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/multisite-network/) installation. Once selected, you may choose between a **Subdomain** and **Subdirectory** install.

## Empty environment (Without WordPress)

The **Empty environment** option is helpful for users who need a blank environment for [Duplicator migration](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrate-wordpress-duplicator-plugin/) or custom [Bedrock/Trellis installation](https://kinsta.com/blog/bedrock-trellis/) purposes.

![Add a new site without WordPress (empty environment).](https://kinsta.com/wp-content/uploads/2026/01/wordpress-add-site-empty-environment.png)

Add a new site without WordPress (empty environment).

### Site name

The name of the installation will be shown in MyKinsta but won’t be visible to your site’s visitors. This will also be used for the first part of your site’s [temporary domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-temporary-url/) (sitename.kinsta.cloud).

### Data center location

You can select a data center for each of your sites. This is where your data is actually stored and served from. We support 30 locations and recommend [choosing a location](https://kinsta.com/docs/service-information/data-center-locations/) closest to your user base, as this will decrease latency, [TTFB](https://kinsta.com/blog/ttfb/), and load times.

If you have a [dedicated server](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/dedicated-server/), you can choose this from the list of data center locations.

Can’t find the region you’re looking for? If you’re an existing customer, [contact our Account Management team](https://kinsta.com/docs/support/contact-support/#account-management-team-hours). If you’re new to Kinsta or on a free trial, [contact our Sales team](https://kinsta.com/contact-us/).

## Clone

The **Clone** option allows you to clone a live or staging environment from an existing Kinsta site to a new site. This installation option lets you make a copy of a site without the need for complicated migration plugins.

![Clone an existing Kinsta environment to a new site.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-add-site-clone.png)

Clone an existing Kinsta environment to a new site.

### Environment to clone

Choose an existing live or staging environment to clone.

### Site name

The name of the installation will be shown in MyKinsta but won’t be visible to your site’s visitors. This will also be used for the first part of your site’s [temporary domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-temporary-url/) (sitename.kinsta.cloud).

### Data center location

The **Data center location** field is greyed out for this installation option because cloning is only possible within the same data center location. If you want to host your cloned site in a different data center, open a new chat with our Support team after the cloning process has finished, and we can move the site for you.

## Completing the process

When you reach the final modal, click **Continue**. Creating the new site will take a few minutes, and you will receive a notification in MyKinsta when it is ready.

## Add a new location

You can select a different location for each install/site you add. To do this, go to **Sites**, click **Add site**, and select the preferred data center in the **Data center location** field for your new install/site.

![Data center locations when adding a new site in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-add-site-options.png)

Data center locations when adding a new site in MyKinsta.

At this time, we have 30 global data center locations:

1. Johannesburg, South Africa (af-johannesburg-1)
2. Batam, Indonesia (ap-batam-1)
3. Melbourne, Australia (ap-melbourne-1)
4. Mumbai, India (ap-mumbai-1)
5. Osaka, Japan (ap-osaka-1)
6. Seoul, South Korea (ap-seoul-1)
7. Singapore,Singapore (ap-singapore-1)
8. Sydney, Australia (ap-sydney-1)
9. Tokyo, Japan (ap-tokyo-1)
10. Montreal, Canada (ca-montreal-1)
11. Toronto, Canada (ca-toronto-1)
12. Amsterdam, Netherlands (eu-amsterdam-1)
13. Frankfurt, Germany (eu-frankfurt-1)
14. Madrid, Spain (eu-madrid-1)
15. Milan, Italy (eu-milan-1)
16. Paris, France (eu-paris-1)
17. Stockholm, Sweden (eu-stockholm-1)
18. Zurich, Switzerland (eu-zurich-1)
19. Jerusalem, Israel (il-jerusalem-1)
20. Dubai, United Arab Emirates (me-dubai-1)
21. Riyadh, Saudi Arabia (me-riyadh-1)
22. Monterrey, Mexico (mx-monterrey-1)
23. Bogota, Colombia (sa-bogota-1)
24. Santiago, Chile (sa-santiago-1)
25. Sao Paulo, Brazil (sa-saopaulo-1)
26. London, United Kingdom (uk-london-1)
27. Ashburn, VA (us-ashburn-1)
28. Chicago, IL (us-chicago-1)
29. Phoenix, AZ (us-phoenix-1)
30. San Jose, CA (us-sanjose-1)
