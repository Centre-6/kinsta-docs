---
url: "https://api-docs.kinsta.com/pages/analytics/description/"
title: "Analytics"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "analytics"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:55.467Z"
fetched_at: "2026-10-07T22:41:45Z"
sha256: "a068b40e17d2c315905c2df22da6d75f527cda2b7f0395705cbb0d112d44f7ff"
body_chars: 1846
extracted_with: "main"
status: "live"
---

# Analytics

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/pages/analytics/description/

---

With the `Analytics` endpoint, you can `GET` the following analytics data:

- [Visits, server bandwidth, and CDN bandwidth usage](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#plan-usage-distribution).
- [CDN bandwidth](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#cdn-bandwidth)
- [Visits](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#visits)
- [Sever bandwidth](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#bandwidth)
- [Disk space](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#disk-space)
- [Top Countries](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#top-countries)
- [Top Cities](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#top-cities)
- [Top Client IPs](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#top-client-ips)
- [Visit Dispersion](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#dispersion)
- [Response Code Breakdown](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#response-code-breakdown)

You can obtain the `environment_id` using the `GET` request with the [WordPress Site Environments](https://api-docs.kinsta.com/tag/WordPress-Site-Environments#operation/getSiteEnvironments) endpoint.
The `environment_id` is also shown after the `site_id` in the URL in MyKinsta when you access the environment, for example in the URL `https://my.kinsta.com/sites/details/fbab4927-e354-4044-b226-29ac0fbd20ca/c84ce214-69b9-4a32-8e67-880672cf1d38?idCompany=bdd25d71-5706-4890-870f-1adda17c505d`:

- The `site_id` is `fbab4927-e354-4044-b226-29ac0fbd20ca`
- The `environment_id` is `c84ce214-69b9-4a32-8e67-880672cf1d38`
- The `company_id` is `bdd25d71-5706-4890-870f-1adda17c505d`
