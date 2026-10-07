---
url: "https://api-docs.kinsta.com/pages/wordpress-sites/description/"
title: "WordPress Sites"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-sites"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:55.469Z"
fetched_at: "2026-10-07T22:41:54Z"
sha256: "11d881e8de9bf2d36c0114c7dca60fb5c7b0523b54b6ff32e9b7f14c3fa4178e"
body_chars: 2707
extracted_with: "main"
status: "live"
---

# WordPress Sites

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/pages/wordpress-sites/description/

---

With the `sites` endpoint, you can get a list of your company’s WordPress sites, details for a specific site, and details about a site’s environment ([live](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/new-site), [staging](https://kinsta.com/docs/wordpress-hosting/staging-environment), and/or [premium staging](https://kinsta.com/docs/wordpress-hosting/staging-environment#premium-staging-environments)). You can also perform actions like:

- [Create a new site](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/new-site#option-1-install-wordpress).
- [Clone an existing site](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/new-site#option-3-clone-an-existing-environment).
- [Create a plain site without WordPress (empty environment)](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/new-site#option-2-dont-install-wordpress-empty-environment).
- [Delete a site](https://kinsta.com/docs/wordpress-hosting/site-management#delete-a-wordpress-site).
- [Reset a site](https://kinsta.com/docs/wordpress-hosting/site-management/#reset-a-wordpress-site).

You can also `GET` the following [Analytics](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/) data for each site:

- [Visits](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#visits)
- [Bandwidth](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#bandwidth)
- [CDN bandwidth](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#cdn-bandwidth)

Depending on the parameters, **site creation** might take around one to a few minutes. This is why this endpoint responds with `202 Accepted` with an `operation_id` in the body, which you can use with the `/operations` endpoint to check the progress.
You can obtain the `company_id` from [MyKinsta](https://my.kinsta.com/) > **username** > **Company settings** > **Billing details**.
The `company_id`, `site_id` and `environment_id` are shown in the URL in MyKinsta when you access an environment, for example in the URL `https://my.kinsta.com/sites/details/fbab4927-e354-4044-b226-29ac0fbd20ca/c84ce214-69b9-4a32-8e67-880672cf1d38?idCompany=bdd25d71-5706-4890-870f-1adda17c505d`:

- The `site_id` is `fbab4927-e354-4044-b226-29ac0fbd20ca`
- The `environment_id` is `c84ce214-69b9-4a32-8e67-880672cf1d38`
- The `company_id` is `bdd25d71-5706-4890-870f-1adda17c505d`

**Important**: due to a delay in the operation initialization process, the site creation operation can return `404 Not Found` in the first few seconds. So, when you integrate it into your script or application, please consider this delay when polling the `operation` status.
