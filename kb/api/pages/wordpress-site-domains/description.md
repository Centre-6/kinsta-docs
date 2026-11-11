---
url: "https://api-docs.kinsta.com/pages/wordpress-site-domains/description/"
title: "WordPress Site Domains"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-domains"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T09:49:48.573Z"
fetched_at: "2026-11-11T13:05:17Z"
sha256: "b99556e1fd4c53a24a659d9c83fe784aeefe4050eb44a12113bbe015c4e9c556"
body_chars: 1119
extracted_with: "main"
status: "live"
---

# WordPress Site Domains

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/pages/wordpress-site-domains/description/

---

With the `domains` endpoint, you can:

- Use a `POST` request to [add a new domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains) to a WordPress site
- Use a `DEL` request to remove a domain.
- Use a `PUT` request to [change the primary domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/#change-your-primary-domain).
- `GET` a list of verification and pointing records for the site domain.

You can obtain the `environment_id` and `domain_ids` using the `GET` request with the [WordPress Site Environments](https://api-docs.kinsta.com/tag/WordPress-Site-Environments#operation/getSiteEnvironments) endpoint.
The `environment_id` is also shown after the `site_id` in the URL in MyKinsta when you access the environment, for example in the URL `https://my.kinsta.com/sites/details/fbab4927-e354-4044-b226-29ac0fbd20ca/c84ce214-69b9-4a32-8e67-880672cf1d38?idCompany=bdd25d71-5706-4890-870f-1adda17c505d`:

- The `site_id` is `fbab4927-e354-4044-b226-29ac0fbd20ca`
- The `environment_id` is `c84ce214-69b9-4a32-8e67-880672cf1d38`
- The `company_id` is `bdd25d71-5706-4890-870f-1adda17c505d`
