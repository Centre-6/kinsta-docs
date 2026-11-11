---
url: "https://api-docs.kinsta.com/pages/logs/description/"
title: "Logs"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "logs"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T09:49:48.561Z"
fetched_at: "2026-11-11T13:05:12Z"
sha256: "c2e4c26dafdc1b8bb11fad9705941868a8cae264e857441c606298d9ef3bbd9e"
body_chars: 939
extracted_with: "main"
status: "live"
---

# Logs

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/pages/logs/description/

---

Use the `logs` endpoint to get your site’s [log files](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs), including the `error.log`, `kinsta-cache-perf.log`, and `access.log`. This has a rate limit of 35 requests per minute.
You can obtain the `environment_id` using the `GET` request with the [WordPress Site Environments](https://api-docs.kinsta.com/tag/WordPress-Site-Environments#operation/getSiteEnvironments) endpoint.
The `environment_id` is also shown after the `site_id` in the URL in MyKinsta when you access the environment, for example in the URL `https://my.kinsta.com/sites/details/fbab4927-e354-4044-b226-29ac0fbd20ca/c84ce214-69b9-4a32-8e67-880672cf1d38?idCompany=bdd25d71-5706-4890-870f-1adda17c505d`:

- The `site_id` is `fbab4927-e354-4044-b226-29ac0fbd20ca`
- The `environment_id` is `c84ce214-69b9-4a32-8e67-880672cf1d38`
- The `company_id` is `bdd25d71-5706-4890-870f-1adda17c505d`
