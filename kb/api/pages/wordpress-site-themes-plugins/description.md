---
url: "https://api-docs.kinsta.com/pages/wordpress-site-themes-plugins/description/"
title: "WordPress Site Themes & Plugins"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-themes-plugins"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:55.463Z"
fetched_at: "2026-10-07T22:41:53Z"
sha256: "f9966c627429a927470e96f979bd991c6be9039c043bbfbe4918af8f42867b87"
body_chars: 957
extracted_with: "main"
status: "live"
---

# WordPress Site Themes & Plugins

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/pages/wordpress-site-themes-plugins/description/

---

With the site `plugins` and `themes` endpoints, you can get a list of your site’s [plugins and themes](https://kinsta.com/docs/wordpress-hosting/site-management/plugins-themes). You can also send a `PUT` request to update your plugins or themes individually or as a bulk update.
You can obtain the `environment_id` using the `GET` request with the [WordPress Site Environments](https://api-docs.kinsta.com/tag/WordPress-Site-Environments#operation/getSiteEnvironments) endpoint.
The `environment_id` is also shown after the `site_id` in the URL in MyKinsta when you access the environment, for example in the URL `https://my.kinsta.com/sites/details/fbab4927-e354-4044-b226-29ac0fbd20ca/c84ce214-69b9-4a32-8e67-880672cf1d38?idCompany=bdd25d71-5706-4890-870f-1adda17c505d`:

- The `site_id` is `fbab4927-e354-4044-b226-29ac0fbd20ca`
- The `environment_id` is `c84ce214-69b9-4a32-8e67-880672cf1d38`
- The `company_id` is `bdd25d71-5706-4890-870f-1adda17c505d`
