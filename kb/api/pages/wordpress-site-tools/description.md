---
url: "https://api-docs.kinsta.com/pages/wordpress-site-tools/description/"
title: "WordPress Site Tools"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-tools"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T09:49:48.558Z"
fetched_at: "2026-11-11T13:05:20Z"
sha256: "d292ae0904b68ea6865951b4bec1fcab9eb96e09bb250b2d49c01f9ac3dfa480"
body_chars: 1718
extracted_with: "main"
status: "live"
---

# WordPress Site Tools

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/pages/wordpress-site-tools/description/

---

With the `tools` endpoint, you can perform actions on sites like:

- [Clear site cache](https://kinsta.com/docs/wordpress-hosting/caching/site-caching#clear-cache-in-mykinsta).
- [Restart PHP](https://kinsta.com/docs/wordpress-hosting/site-management/php#restart-php).
- [Modify PHP version](https://kinsta.com/docs/wordpress-hosting/site-management/php#updating-php).
- Get and update a list of [denied IP addresses](https://kinsta.com/docs/wordpress-hosting/site-management/block-ip-address).
- [Update the Force HTTPS status](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/#force-https).
- [Search and replace content](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/mykinsta-search-replace-tool/).

You can obtain the `environment_id` using the `GET` request with the [WordPress Site Environments](https://api-docs.kinsta.com/tag/WordPress-Site-Environments#operation/getSiteEnvironments) endpoint.
The `environment_id` is also shown after the `site_id` in the URL in MyKinsta when you access the environment, for example in the URL `https://my.kinsta.com/sites/details/fbab4927-e354-4044-b226-29ac0fbd20ca/c84ce214-69b9-4a32-8e67-880672cf1d38?idCompany=bdd25d71-5706-4890-870f-1adda17c505d`:

- The `site_id` is `fbab4927-e354-4044-b226-29ac0fbd20ca`
- The `environment_id` is `c84ce214-69b9-4a32-8e67-880672cf1d38`
- The `company_id` is `bdd25d71-5706-4890-870f-1adda17c505d`

Most of these tool endpoints will trigger **longer tasks** (from a few seconds to around a minute) on your environments. This is why they provide `202 Accepted` response, with an [`operation_id`](https://api-docs.kinsta.com/tag/Operations/) in the body. To check the progress, you can use the `/operations` endpoint.
