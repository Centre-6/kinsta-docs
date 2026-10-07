---
url: "https://api-docs.kinsta.com/pages/additional-sftp-users/description/"
title: "Additional SFTP Users"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "additional-sftp-users"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:55.465Z"
fetched_at: "2026-10-07T22:41:44Z"
sha256: "b16acc5adfcba0471eb8dbac8fca1ef26738999e21ddd445ba222bf51c6ee63f"
body_chars: 1250
extracted_with: "main"
status: "live"
---

# Additional SFTP Users

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/pages/additional-sftp-users/description/

---

You can use the `additional SFTP users` endpoint to:

- [Enable or disable additional SFTP accounts](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/#disable-enable-additional-sftp-users).
- [Add additional SFTP accounts](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/#additional-sftp-users).
- Get a list of additional SFTP accounts.
- [Remove additional SFTP accounts](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/#remove-an-sftp-user).

You can obtain the `environment_id` using the `GET` request with the [WordPress Site Environments](https://api-docs.kinsta.com/tag/WordPress-Site-Environments#operation/getSiteEnvironments) endpoint.
The `environment_id` is also shown after the `site_id` in the URL in MyKinsta when you access the environment, for example in the URL `https://my.kinsta.com/sites/details/fbab4927-e354-4044-b226-29ac0fbd20ca/c84ce214-69b9-4a32-8e67-880672cf1d38?idCompany=bdd25d71-5706-4890-870f-1adda17c505d`:

- The `site_id` is `fbab4927-e354-4044-b226-29ac0fbd20ca`
- The `environment_id` is `c84ce214-69b9-4a32-8e67-880672cf1d38`
- The `company_id` is `bdd25d71-5706-4890-870f-1adda17c505d`

The `sftp_account_id` is shown when you `GET` the list of additional SFTP users.
