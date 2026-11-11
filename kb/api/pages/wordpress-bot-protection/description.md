---
url: "https://api-docs.kinsta.com/pages/wordpress-bot-protection/description/"
title: "WordPress Bot Protection"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-bot-protection"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T09:49:48.565Z"
fetched_at: "2026-11-11T13:05:14Z"
sha256: "56b58ef88f10bd934cc45ebb3d938ad73919b48c43a307eeba50eef98eacb670"
body_chars: 1835
extracted_with: "main"
status: "live"
---

# WordPress Bot Protection

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/pages/wordpress-bot-protection/description/

---

[Bot protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) lets you control how different types of traffic are blocked or challenged on your site. With the `bot-protection` endpoints, you can:

- **[Protection level](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#change-the-bot-protection-level):** Retrieve the current level with `GET`, or set a new level with `PUT`.
- **[AI crawlers](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#block-ai-crawlers):** Check whether AI crawlers are blocked with `GET`, or block or unblock them with `PUT`.
- **[WordPress automations](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#allow-typical-wordpress-automations):** Check the **Allow typical WordPress automations** setting with `GET`, or allow or block automations with `PUT`.
- **[Exception rules](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#exceptions):** List rules with `GET`, add a rule with `POST`, or remove a rule with `DELETE`.

You can obtain the `environment_id` using the `GET` request with the [WordPress Site Environments](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-site-environments) endpoint.
The `environment_id` is also shown after the `site_id` in the URL in MyKinsta when you access the environment, for example in the URL `https://my.kinsta.com/sites/details/fbab4927-e354-4044-b226-29ac0fbd20ca/c84ce214-69b9-4a32-8e67-880672cf1d38?idCompany=bdd25d71-5706-4890-870f-1adda17c505d`**:**

- The `site_id` is `fbab4927-e354-4044-b226-29ac0fbd20ca`
- The `environment_id` is `c84ce214-69b9-4a32-8e67-880672cf1d38`
- The `company_id` is `bdd25d71-5706-4890-870f-1adda17c505d`
