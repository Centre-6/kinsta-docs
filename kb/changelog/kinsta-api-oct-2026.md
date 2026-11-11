---
url: "https://kinsta.com/changelog/kinsta-api-oct-2026/"
title: "Manage company users and permissions with the Kinsta API"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-10-21T18:05:36"
change_signal: "2026-10-21T18:05:36"
fetched_at: "2026-11-11T13:03:01Z"
sha256: "b1b23fa95a3cf0d071e26b5595cfd89400ffcb534296c7b6711449eb79966e4d"
body_chars: 8806
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Manage company users and permissions with the Kinsta API

**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-oct-2026/
**Kinsta last updated:** 2026-10-21T18:05:36

## On this page

- [Retrieve company users with their roles and 2FA details](#retrieve-company-users-with-their-roles-and-2fa-details)
  - [Get a specific company user by ID](#get-a-specific-company-user-by-id)
- [Change a user’s company role](#change-a-users-company-role)
- [Update permissions for users on individual sites](#update-permissions-for-users-on-individual-sites)
- [Troubleshoot API operations with a new support reference ID](#troubleshoot-api-operations-with-a-new-support-reference-id)
- [Manage user access through your own tools](#manage-user-access-through-your-own-tools)

---

You can now manage who has access to your WordPress sites through the [Kinsta API](https://kinsta.com/docs/kinsta-api/).

We’ve added three endpoints that let you retrieve a specific company user’s details and update their permissions at the company or site level. The existing endpoint for listing company users also returns more information about each person’s role and two-factor authentication (2FA) method.

This release also introduces a new reference ID that makes it easier to get help when an API operation fails.

## Retrieve company users with their roles and 2FA details

The existing [Get list of company users](https://api-docs.kinsta.com/api-reference/company-users/get-list-of-company-users) endpoint has been extended to return more information about each user.

Previously, you could retrieve basic details such as a user’s name, email address, and profile image. The response now includes a `capabilities` array describing the user’s company and site roles, along with a `type_2fa` field indicating their configured authentication method.

To retrieve your company’s users, send a GET request:

```
curl --request GET \
  --url https://api.kinsta.com/v2/company/{company_id}/users \
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

The response now includes the additional fields:

```
{
  "company": {
    "users": [
      {
        "user": {
          "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
          "email": "john@example.com",
          "image": "https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
          "full_name": "John Doe",
          "type_2fa": "email"
        },
        "capabilities": [
          {
            "id": "9c1f7b2e-3d4a-4f5b-8c6d-1e2f3a4b5c6d",
            "type": "company",
            "role": "company-admin",
            "company_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
            "site_id": null
          }
        ]
      }
    ]
  }
}
```

Each capability identifies the assigned role and the associated company or site. The `type_2fa` field can contain a configured authentication method or `null`.

This additional information helps when reviewing team access, checking assigned roles, or building internal tools that show who can access specific resources.

### Get a specific company user by ID

A new [Get a company user by ID](https://api-docs.kinsta.com/api-reference/company-users/get-a-company-user-by-id) endpoint lets you retrieve one person’s details without fetching the entire company user list.

Pass the company ID and user ID in the request:

```
curl --request GET \
  --url https://api.kinsta.com/v2/company/{id}/users/{id_user} \
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

The response contains the person’s basic information, 2FA method, and assigned capabilities:

```
{
  "company": {
    "user_by_id": {
      "user": {
        "id": "9c1e4d2a-1b3c-4f5a-8d6e-7f8a9b0c1d2e",
        "email": "john@example.com",
        "full_name": "John Doe",
        "type_2fa": "email"
      },
      "capabilities": [
        {
          "role": "company-developer",
          "id_company": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
          "id_site": null
        }
      ]
    }
  }
}
```

You can use this endpoint to check an individual’s current access before changing their role or including their permissions in an internal access report.

## Change a user’s company role

The new [Edit user capabilities for the company](https://api-docs.kinsta.com/api-reference/company-users/edit-user-capabilities-for-the-company) endpoint let you change an existing user’s company-level role.

It supports three roles:

- `company-admin`, which provides company-wide administrative access.
- `company-developer`, which provides access to manage sites and development-related resources without billing permissions.
- `company-billing`, which provides access to billing information without access to WordPress sites.

For example, the following request changes an existing user’s role to Company Developer:

```
curl --request POST \
  --url https://api.kinsta.com/v2/company/{company_id}/users/company-capabilities \
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  --header 'Content-Type: application/json' \
  --data '{
    "user_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "role": "company-developer"
  }'
```

When the request is accepted, the response includes an operation ID:

```
{
  "message": "User capabilities updated for the company",
  "status": 202,
  "operation_id": "company:set-company-user-capabilities-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
}
```

You can use the returned `operation_id` to check the operation’s status.

Company-level roles determine which resources a person can access, so changing a role may grant or remove access to sites, billing, or company settings. See the [user roles and permissions documentation](https://kinsta.com/docs/company-settings/user-management/) for the access associated with each role.

## Update permissions for users on individual sites

You can also manage site-level access with the new [Edit users capabilities for the site](https://api-docs.kinsta.com/api-reference/company-users/edit-users-capabilities-for-the-site) endpoint.

Unlike company-level permissions, site capabilities apply to specific WordPress sites. This is useful when you want a developer or client to have access to one site without granting access across the entire company.

The endpoint accepts a `user_ids` array and a `site_capabilities` array, so you can specify multiple users and site assignments in a single request.

Each site assignment supports two roles:

- `site-admin`, which gives a user administrative access to the assigned site and its environments, subject to the role’s restrictions.
- `site-developer`, which provides access to the site’s staging environments, with limited permissions.

For example, this request assigns a user the Site Developer role:

```
curl --request POST \
  --url https://api.kinsta.com/v2/company/{company_id}/users/site-capabilities \
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  --header 'Content-Type: application/json' \
  --data '{
    "user_ids": [
      "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
    ],
    "site_capabilities": [
      {
        "site_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
        "role": "site-developer"
      }
    ]
  }'
```

The response includes an operation ID that can be used to track the update:

```
{
  "message": "Users capabilities updated for the site",
  "status": 202,
  "operation_id": "company:set-site-user-capabilities-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
}
```

For teams managing multiple client websites, this endpoint lets you assign site permissions from an onboarding script or internal management system.

## Troubleshoot API operations with a new support reference ID

We’ve also added an optional `support_reference_id` field to responses from API endpoints that trigger actions in MyKinsta.

Previously, these requests returned an `operation_id` you could use to check the operation’s progress. However, because operation IDs are temporarily cached, it can be difficult to identify the underlying action when investigating a failed request.

The new `support_reference_id` identifies the original action, giving Kinsta Support a more direct way to investigate what happened.

The field can appear in the initial API response and when checking the operation through the existing [Get operation status](https://api-docs.kinsta.com/api-reference/operations/get-the-status-information-of-an-operation) endpoint:

```
curl --request GET \
  --url https://api.kinsta.com/v2/operations/{operation_id} \
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

For example, an operation that’s still running can return:

```
{
  "status": 202,
  "message": "Operation in progress",
  "support_reference_id": 12345,
  "data": null
}
```

If an API action fails, you can provide the support reference ID to our [Support team](https://kinsta.com/kinsta-support/) to help them locate and investigate the corresponding action.

Because the field is optional, integrations should continue to use `operation_id` for tracking progress and retain `support_reference_id` when it’s available.

## Manage user access through your own tools

These additions let you build more complete user access workflows with the Kinsta API. You can retrieve a person’s current permissions, change their company role, or assign site-level access without handling each change individually in the dashboard.

The new support reference ID also gives teams a useful identifier to retain when logging API operations and investigating failures.

Explore the available endpoints and request formats in the [Kinsta API documentation](https://api-docs.kinsta.com/).
