---
url: "https://kinsta.com/changelog/kinsta-api-nov-21-2025/"
title: "Generate phpMyAdmin login link and view API activity with the Kinsta API"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Generate phpMyAdmin login link and view API activity with the Kinsta API"]
kinsta_last_updated: "2026-05-20T20:31:36+00:00"
sitemap_lastmod: "2026-05-20T20:31:36+00:00"
fetched_at: "2026-10-07T22:37:41Z"
sha256: "40a2cbc37f9c5b1dd804fb20802491a8fdcdd3b5a6714baf989cb46357a33433"
body_chars: 6272
extracted_with: "main article"
status: "live"
---

# Generate phpMyAdmin login link and view API activity with the Kinsta API

**Section:** Changelog > Generate phpMyAdmin login link and view API activity with the Kinsta API
**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-nov-21-2025/
**Kinsta last updated:** 2026-05-20T20:31:36+00:00

## On this page

- [Generate phpMyAdmin login link](#generate-phpmyadmin-login-link)
- [Retrieve company API keys](#retrieve-company-api-keys)
- [Access company activity logs](#access-company-activity-logs)
- [View and filter API key activity in MyKinsta](#view-and-filter-api-key-activity-in-mykinsta)
- [Build visibility and security into your workflow](#build-visibility-and-security-into-your-workflow)

---

Updated
:   May 20, 2026

![An illustration with an image of the MyKinsta dashboard and the words 'Kinsta product update.'](https://kinsta.com/wp-content/uploads/2024/04/kinsta-product-update-changelog-1024x536.png)

We have introduced an API endpoint that generates short-lived phpMyAdmin login links, making database access faster and easier to automate.

This update also includes new endpoints for listing company API keys and retrieving activity logs, along with MyKinsta additions that improve visibility and allow filtering activity by specific keys.

Let’s go through these updates in detail.

## Generate phpMyAdmin login link

You can now [generate a temporary phpMyAdmin login link](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/generate-phpmyadmin-login-link) for any WordPress environment directly through the Kinsta API. This creates a secure, one-time login URL that gives you instant access to your database without using stored credentials outside of the MyKinsta dashboard.

This feature mirrors the [one-click login to phpMyAdmin](https://kinsta.com/changelog/phpmyadmin-one-click/) now available in MyKinsta.

Each link generated via the API is valid for five minutes from the moment it’s created, ensuring access remains both fast and secure.

**Example request:**

```
curl -i -X POST \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/pma-login-token' \
  -H 'Authorization: Bearer '
```

Replace `{env_id}` with the environment you want to access, and the API will return a fresh login link. Here is an example response:

```
{
  "url": "https://mysqleditor-mysite.kinsta.cloud?app-key=4e8d3c9e7b9f4d2a87f1e27c0f61b2fa8f4a15de4e25c9f1f81ad0b2d0ef3c1a",
  "expires_at": 1736914230000
}
```

You can find other details in the [API documentation for phpMyAdmin login links](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/generate-phpmyadmin-login-link).

## Retrieve company API keys

The new [Get list of company API Keys](https://api-docs.kinsta.com/api-reference/api-keys/get-list-of-company-api-keys) endpoint lets you retrieve a full list of your company’s API keys directly through the Kinsta API.

This makes it easier to audit which keys exist, check their status, and confirm expiration dates, especially for larger teams managing multiple automations or integrations.

**Example request:**

```
curl -i -X GET \
  'https://api.kinsta.com/v2/company/{company_id}/api-keys' \
  -H 'Authorization: Bearer '
```

Replace `{company_id}` with your company’s ID, and the response will include each key’s name, status, and expiration timestamp:

```
{
  "api_keys": [
    {
      "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
      "name": "Public API Key",
      "status": "active",
      "expires_at": "2028-08-21T08:15:21.872Z"
    }
  ]
}
```

You can find full parameter details in the [API documentation for company API keys](https://api-docs.kinsta.com/api-reference/api-keys/get-list-of-company-api-keys).

## Access company activity logs

The Kinsta API now provides access to [company-level activity logs](https://api-docs.kinsta.com/api-reference/activity-logs/get-list-of-company-activity-logs), allowing administrators to track events, user actions, and API key usage programmatically.

The endpoint supports filters such as **category**, **site ID**, the **API key** used, or the **user** who initiated the action, making it especially useful for teams with multiple contributors or automated services.

**Example request:**

```
curl -i -X GET \
  'https://api.kinsta.com/v2/company/{company_id}/activity-logs?limit=10&offset=0&category=siteActions' \
  -H 'Authorization: Bearer '
```

You can adjust the query parameters (like `limit`, `offset`, or `category`) depending on how much detail you want to retrieve.

**Example response:**

```
{
  "company": {
    "activity_logs": {
      "items": [
        {
          "id": 34181968,
          "site_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
          "created_at": 1665382600770,
          "is_done": true,
          "has_failed": false,
          "has_warning": false,
          "type": "deleteSite",
          "public_error": "The environment is blocked by another process. Please try again a bit later.",
          "ip_address": "203.0.113.42",
          "initiated_by": {
            "id": "admin-user",
            "role": "admin",
            "full_name": "Jane",
            "first_name": "Smith"
          },
          "user_agent_info": {
            "browser_name": "Chrome",
            "browser_version": "126.0.0",
            "os_name": "macOS"
          },
          "api_key_info": {
            "id": "cf5b98a0-6fdd-4997-9c1f-e73d566533be",
            "name": "Public API Key"
          },
          "descriptions": [
            "Delete site \"Test ABC\""
          ]
        }
      ],
      "total": 42
    }
  }
}
```

See all available parameters and a detailed response example in the [API documentation for company activity logs](https://api-docs.kinsta.com/api-reference/activity-logs/get-list-of-company-activity-logs).

## View and filter API key activity in MyKinsta

MyKinsta now lets companies view details for each API key and filter the **User activity** tab by a specific key.

![API details page in MyKinsta showing user activity logs.](https://kinsta.com/wp-content/uploads/2025/11/api-details-user-activity.png)

API details page in MyKinsta showing user activity logs.

You can quickly see:

- The name and status of each API key
- Which actions were triggered by a particular key
- When and from where requests were made

This added visibility helps teams stay organized and maintain tighter security, especially when multiple developers, tools, or external integrations depend on API access.

## Build visibility and security into your workflow

These updates give developers and administrators better tools to manage access and track activity across their environments.

Whether generating temporary phpMyAdmin login links, reviewing API key usage, or auditing company actions, the Kinsta API continues to expand to support advanced automation and secure management.

Explore all request examples and schema references in the [Kinsta API documentation](https://api-docs.kinsta.com/).
