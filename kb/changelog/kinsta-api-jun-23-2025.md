---
url: "https://kinsta.com/changelog/kinsta-api-jun-23-2025/"
title: "Change primary domains and manage SFTP access with Kinsta API"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-05-20T20:32:03"
change_signal: "2026-05-20T20:32:03"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "66b95deb4fd45184813d9038c037ddda16101f8292278d0096589ec447e5c23e"
body_chars: 5821
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Change primary domains and manage SFTP access with Kinsta API

**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-jun-23-2025/
**Kinsta last updated:** 2026-05-20T20:32:03

## On this page

- [Change the primary domain of an environment](#change-the-primary-domain-of-an-environment)
- [Full support for managing additional SFTP accounts](#full-support-for-managing-additional-sftp-accounts)
  - [Enable or disable access](#enable-or-disable-access)
  - [Add a new SFTP user](#add-a-new-sftp-user)
  - [List and remove users](#list-and-remove-users)
  - [New metadata in environment listings](#new-metadata-in-environment-listings)
- [More control for modern teams](#more-control-for-modern-teams)

---

We’ve expanded the [Kinsta API](https://kinsta.com/docs/kinsta-api/) with new domain and user management capabilities, giving teams even more control over their environments, without needing to log in to [MyKinsta](https://kinsta.com/mykinsta/).

With these updates, you can now programmatically change the primary domain of a WordPress environment and fully manage additional SFTP accounts via the Kinsta API.

## Change the primary domain of an environment

Previously, the Kinsta API allowed you to [add](https://api-docs.kinsta.com/api-reference/wordpress-site-domains/add-new-site-domain) or [remove domains](https://api-docs.kinsta.com/api-reference/wordpress-site-domains/delete-one-or-more-site-domains) from your site, which was great for setup and cleanup. But you couldn’t change which domain was set as primary for an environment.

With this new release, you can now set an existing domain as the [new primary domain](https://api-docs.kinsta.com/api-reference/wordpress-site-domains/change-primary-domain-of-an-environment) for a specific environment using the following endpoint:

```
PUT /sites/environments/{env_id}/change-primary-domain
```

To use the endpoint, you need the `domain_id` of the domain you want to set as primary. This must be one of the domains already associated with the environment.

You can find the `domain_id` using the `Get Site by ID` or `Get Site Environments` endpoints. It looks something like this in the response:

```
"domains": [
  {
    "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "name": "example.com",
    "type": "live"
  }
]
```

You also need to set the `run_search_and_replace` field. When set to `true`, it triggers a search and replace across the site’s database to update URLs referencing the domain.

Here’s an example using `curl`:

```
curl -i -X PUT \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/change-primary-domain' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  -H 'Content-Type: application/json' \
  -d '{
    "domain_id": "your-domain-id",
    "run_search_and_replace": true
  }'
```

## Full support for managing additional SFTP accounts

In April, we added the [ability to create and manage multiple SFTP user](https://kinsta.com/changelog/additional-sftp-users/) accounts directly in the MyKinsta dashboard. Now, you can do all of that using the Kinsta API.

This gives you full programmatic control over additional SFTP users in each environment. You can enable access, add new users, list existing ones, or remove them entirely.

### Enable or disable access

Before adding any users, additional SFTP access must be enabled for the environment. You can do that with:

```
PUT /sites/environments/{env_id}/additional-sftp-accounts/toggle-status
```

Here’s an example using `curl`:

```
curl -i -X PUT \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts/toggle-status' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  -H 'Content-Type: application/json' \
  -d '{
    "enabled": true
  }'
```

This can be reversed at any time by setting `"enabled": false`.

### Add a new SFTP user

Once enabled, you can [add users](https://api-docs.kinsta.com/api-reference/additional-sftp-users/add-additional-sftp-account) with this endpoint:

```
POST /sites/environments/{env_id}/additional-sftp-accounts
```

The request lets you define a username, secure password (minimum 16 characters), root directory, and permission level (`read` or `write`).

```
curl -i -X POST \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "dev-user",
    "password": "R8zXwT@#bV!kJq9^",
    "root_directory": "/wp-content/themes",
    "permission": "write"
  }'
```

This mirrors the same controls you’d find in MyKinsta, including the ability to restrict access to specific directories or assign read-only permissions.

### List and remove users

You can [retrieve a list of additional SFTP accounts](https://api-docs.kinsta.com/api-reference/additional-sftp-users/get-list-of-additional-sftp-accounts) like this:

```
GET /sites/environments/{env_id}/additional-sftp-accounts
```

To [delete one](https://api-docs.kinsta.com/api-reference/additional-sftp-users/remove-additional-sftp-account):

```
DELETE /sites/environments/additional-sftp-accounts/{sftp_account_id}
```

This gives you full flexibility to automate account rotation, grant limited access to collaborators, or revoke credentials after a deployment.

### New metadata in environment listings

To support these new capabilities, we added the field `is_additional_sftp_accounts_enabled` to the following endpoints:

- [GET /sites/{site_id}/environments](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-site-environments)
- [GET /sites](https://api-docs.kinsta.com/api-reference/wordpress-sites/get-list-of-company-sites) (when using the `include_environments=true` query parameter)

This makes it easier to audit which environments have additional SFTP access enabled, especially if you’re managing many across your platform or client accounts.

## More control for modern teams

These new API features give you deeper control over your infrastructure, whether you’re automating staging workflows, rotating SFTP credentials, or programmatically switching site URLs.

You can find all request/response details in the[Kinsta API documentation](https://api-docs.kinsta.com/). There’s a lot you can do with the Kinsta API, and many agencies and developers already rely on it to manage hundreds of sites efficiently.

Ready to get started? Head to [MyKinsta](https://my.kinsta.com/login/) to [generate your API token](https://kinsta.com/blog/kinsta-api-key/) and start building.
