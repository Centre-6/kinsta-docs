---
url: "https://api-docs.kinsta.com/pages/wordpress-cdn/description/"
title: "WordPress CDN"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-cdn"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T09:49:48.571Z"
fetched_at: "2026-11-11T13:05:15Z"
sha256: "616ca50a61bd14b7a51f30992228bef2930479073125dd5fd02fb3a5a29483d9"
body_chars: 1549
extracted_with: "main"
status: "live"
---

# WordPress CDN

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/pages/wordpress-cdn/description/

---

[Kinsta’s premium CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn) powered by Cloudflare helps to maximize the performance of your site. With the `cdn` endpoint you can:

- Clear the CDN cache for your sites.
- Change the [image optimization settings](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#image-optimization-1).

You can obtain the `environment_id` using the `GET` request with the [WordPress Site Environments](https://api-docs.kinsta.com/tag/WordPress-Site-Environments#operation/getSiteEnvironments) endpoint.
The `environment_id` is also shown after the `site_id` in the URL in MyKinsta when you access the environment, for example in the URL `https://my.kinsta.com/sites/details/fbab4927-e354-4044-b226-29ac0fbd20ca/c84ce214-69b9-4a32-8e67-880672cf1d38?idCompany=bdd25d71-5706-4890-870f-1adda17c505d`:

- The `site_id` is `fbab4927-e354-4044-b226-29ac0fbd20ca`
- The `environment_id` is `c84ce214-69b9-4a32-8e67-880672cf1d38`
- The `company_id` is `bdd25d71-5706-4890-870f-1adda17c505d`

You can obtain the `cdn_cache_id` using the `GET` request with the [WordPress Site Environments](https://api-docs.kinsta.com/tag/WordPress-Site-Environments#operation/getSiteEnvironments) endpoint.
The CDN endpoints may trigger **longer tasks** (from a few seconds to around a minute) on your environments. This is why they provide `202 Accepted` response, with an [`operation_id`](https://api-docs.kinsta.com/tag/Operations) in the body. To check the progress, you can use the `/operations` endpoint.
