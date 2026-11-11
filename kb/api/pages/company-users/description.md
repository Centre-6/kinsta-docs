---
url: "https://api-docs.kinsta.com/pages/company-users/description/"
title: "Company Users"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "company-users"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T09:49:48.563Z"
fetched_at: "2026-11-11T13:05:08Z"
sha256: "82b0a9c37a2e55179e750346d6bfa81f70d45ebf87eb893361a272e02c8244c2"
body_chars: 721
extracted_with: "main"
status: "live"
---

# Company Users

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/pages/company-users/description/

---

The `users` endpoint lets you manage your [company’s users](https://kinsta.com/docs/company-settings/user-management/). You can:

- `GET` a list of all users in your company, including each user’s ID, email address, full name, and profile picture URL.
- `GET` a specific user by their user ID.
- `POST` a request to change a user’s access to your company or to specific sites.

You can obtain the `company_id` from [MyKinsta](https://my.kinsta.com/) > **username** > **Company settings** > **Billing details**.
The `company_id` is also shown in the URL in MyKinsta, for example, in the URL `https://my.kinsta.com/?idCompany=bdd25d71-5706-4890-870f-1adda17c505d` the `company_id` is `bdd25d71-5706-4890-870f-1adda17c505d`.
