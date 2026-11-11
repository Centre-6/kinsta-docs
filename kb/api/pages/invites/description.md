---
url: "https://api-docs.kinsta.com/pages/invites/description/"
title: "Invites"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "invites"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:50:00.694Z"
fetched_at: "2026-11-11T13:05:11Z"
sha256: "7f7d95c3ec1ad184216fec2bee39f5c7bd00c5048fdc3516a10f138fca09a7c5"
body_chars: 1177
extracted_with: "main"
status: "live"
---

# Invites

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/pages/invites/description/

---

The `invites` endpoint lets you send a `GET` request to retrieve a list of pending invitations, and a `POST` request to invite users to a company or site in MyKinsta.
When you invite a user to a company, you can assign one of the following roles:

- `company-admin`
- `company-developer`
- `company-billing`

When you invite a user to a site, you can assign one of the following roles:

- `site-admin`
- `site-developer`

For more information about each role, refer to [User Management](https://kinsta.com/docs/company-settings/user-management/).
You can find your `company_id` in [MyKinsta](https://my.kinsta.com/) under **username** > **Company settings** > **Billing Details**. The `company_id`, `site_id`, and `environment_id` are also shown in the URL when you open an environment in MyKinsta. For example, in the following URL:
`https://my.kinsta.com/sites/details/fbab4927-e354-4044-b226-29ac0fbd20ca/c84ce214-69b9-4a32-8e67-880672cf1d38?idCompany=bdd25d71-5706-4890-870f-1adda17c505d`

- The `site_id` is `fbab4927-e354-4044-b226-29ac0fbd20ca`
- The `environment_id` is `c84ce214-69b9-4a32-8e67-880672cf1d38`
- The `company_id` is `bdd25d71-5706-4890-870f-1adda17c505d`
