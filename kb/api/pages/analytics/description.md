---
url: "https://api-docs.kinsta.com/pages/analytics/description/"
title: "Analytics"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "analytics"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T09:49:48.559Z"
fetched_at: "2026-11-11T13:05:03Z"
sha256: "b75111c8b0e186caa5f442a3a8b4b68eed190dca9b42204ced83f6ffb5e38d40"
body_chars: 3129
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
- [Top ASNs requests](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#top-asn)
- [Top browser requests](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#top-browsers)
- [Top hosts requests](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#top-hosts)
- [Top referrers requests](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#top-referrers)
- [Top user agents requests](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#top-user-agents)
- [Visit Dispersion](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#dispersion)
- [Response Code Breakdown](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#response-code-breakdown)
- [Bot traffic flow](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#requests)
- [Bot traffic requests](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#request-breakdown)
- [Bot protection results](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#bot-protection-results)
- [Bot traffic top breakdown](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#top-traffic)

The bot traffic reports return the number of requests to your site, broken down by traffic type and by whether [bot protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) allowed, challenged, or blocked them.
You can obtain the `environment_id` using the `GET` request with the [WordPress Site Environments](https://api-docs.kinsta.com/tag/WordPress-Site-Environments#operation/getSiteEnvironments) endpoint.
The `environment_id` is also shown after the `site_id` in the URL in MyKinsta when you access the environment, for example, in the URL `https://my.kinsta.com/sites/details/fbab4927-e354-4044-b226-29ac0fbd20ca/c84ce214-69b9-4a32-8e67-880672cf1d38?idCompany=bdd25d71-5706-4890-870f-1adda17c505d`:

- The `site_id` is `fbab4927-e354-4044-b226-29ac0fbd20ca`
- The `environment_id` is `c84ce214-69b9-4a32-8e67-880672cf1d38`
- The `company_id` is `bdd25d71-5706-4890-870f-1adda17c505d`
