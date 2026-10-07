---
url: "https://api-docs.kinsta.com/pages/wordpress-edge-caching/description/"
title: "WordPress Edge Caching"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-edge-caching"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:55.477Z"
fetched_at: "2026-10-07T22:40:33Z"
sha256: "3626e6e009d4779bf2dac9a9cfa6ff352e5348094dbaf396e076486c41cff3bf"
body_chars: 1273
extracted_with: "main"
status: "live"
---

# WordPress Edge Caching

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/pages/wordpress-edge-caching/description/

---

[Edge caching](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching) saves your site/page cache to Cloudflare’s global network of data centers. With the `edge-caching` endpoint, you can:

- Clear edge caching for your sites.
- Enable or disable edge caching.

You can obtain the `environment_id` using the `GET` request with the [WordPress Site Environments](https://api-docs.kinsta.com/tag/WordPress-Site-Environments#operation/getSiteEnvironments) endpoint.
The `environment_id` is also shown after the `site_id` in the URL in MyKinsta when you access the environment, for example in the URL `https://my.kinsta.com/sites/details/fbab4927-e354-4044-b226-29ac0fbd20ca/c84ce214-69b9-4a32-8e67-880672cf1d38?idCompany=bdd25d71-5706-4890-870f-1adda17c505d`:

- The `site_id` is `fbab4927-e354-4044-b226-29ac0fbd20ca`
- The `environment_id` is `c84ce214-69b9-4a32-8e67-880672cf1d38`
- The `company_id` is `bdd25d71-5706-4890-870f-1adda17c505d`

Most of these edge caching endpoints will trigger **longer tasks** (from a few seconds to around a minute) on your environments. This is why they provide `202 Accepted` response, with an [`operation_id`](https://api-docs.kinsta.com/tag/Operations) in the body. To check the progress, you can use the `/operations` endpoint.
