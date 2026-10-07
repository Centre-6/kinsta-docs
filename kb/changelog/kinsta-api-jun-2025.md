---
url: "https://kinsta.com/changelog/kinsta-api-jun-2025/"
title: "Fetch files and target specific paths with the Kinsta API"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Fetch files and target specific paths with the Kinsta API"]
kinsta_last_updated: "2026-05-20T20:32:08+00:00"
sitemap_lastmod: "2026-05-20T20:32:08+00:00"
fetched_at: "2026-10-07T22:37:44Z"
sha256: "881a53d0bcdb4cb0980962302f314f4ac1c74f7b47c88230031998f03533ea42"
body_chars: 5032
extracted_with: "main article"
status: "live"
---

# Fetch files and target specific paths with the Kinsta API

**Section:** Changelog > Fetch files and target specific paths with the Kinsta API
**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-jun-2025/
**Kinsta last updated:** 2026-05-20T20:32:08+00:00

## On this page

- [Get file list for an environment](#get-file-list-for-an-environment)
- [Selective file push between environments](#selective-file-push-between-environments)
- [List sites and their environments in one call](#list-sites-and-their-environments-in-one-call)
- [Kinsta API: Built for teams managing at scale](#kinsta-api-built-for-teams-managing-at-scale)

---

Updated
:   May 20, 2026

![](https://kinsta.com/wp-content/uploads/2025/06/new-api-enhancements-1024x536.png)

Working with environments just got easier. This Kinsta API update introduces new ways to fetch file structure data, perform [selective file pushes between environments](https://kinsta.com/docs/wordpress-hosting/staging-environment/#push-environment-to-live-or-staging), and retrieve all environments in a single request when listing sites.

These additions are designed to reduce the number of calls you need to make, so your deployments and dev tools are faster and more efficient.

## Get file list for an environment

You can now [retrieve the full directory structure](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-list-of-files-for-environment) of a WordPress environment using the Kinsta API. This new endpoint returns a recursive list of folders and subfolders, giving you a clear view of what’s inside each environment — no [SSH](https://kinsta.com/blog/how-to-use-ssh/) logins required.

This is especially useful when building internal tools, validating file paths before selective deployments, or automating environment tasks with precision.

You can send a `GET` request to:

```
GET /sites/environments/{env_id}/file-list
```

Here’s a sample request using `curl`:

```
curl -i -X GET \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/file-list' \
  -H 'Authorization: Bearer '
```

The response includes nested objects representing directories like:

- `wp-content/`
- `wp-content/plugins/`
- `wp-content/themes/`
- `wp-content/uploads/`

Each folder contains its name, path, and any children, making it easy to map or visualize.

## Selective file push between environments

The existing `Push Environment` endpoint now supports a more flexible way to manage file transfers. With two new optional fields, you can push either the full environment or target specific directories — perfect for workflows where you don’t want to sync everything.

You can send a `PUT` request to:

```
PUT /sites/{site_id}/environments
```

Use the following fields to control which files are included:

- `push_files_option`: Choose between `"ALL_FILES"` or `"SPECIFIC_FILES"`
- `file_list`: Provide a list of directory paths you want to push

Here’s an example using `curl` to push only selected folders from one environment to another:

```
curl -i -X PUT \
  'https://api.kinsta.com/v2/sites/{site_id}/environments' \
  -H 'Authorization: Bearer ' \
  -H 'Content-Type: application/json' \
  -d '{
    "source_env_id": "your-source-env-id",
    "target_env_id": "your-target-env-id",
    "push_db": true,
    "push_files": true,
    "run_search_and_replace": true,
    "push_files_option": "SPECIFIC_FILES",
    "file_list": [
      "wp-content/plugins",
      "wp-content/themes",
      "wp-content/uploads"
    ]
  }'
```

This selective approach helps:

- Reduce deployment time by syncing only what has changed
- Avoid overwriting other assets or uploads
- Improve control when pushing changes from staging to production

If you don’t include `push_files_option`, it defaults to `"ALL_FILES"`, maintaining backward compatibility.

## List sites and their environments in one call

You can now [fetch all of a company’s sites](https://api-docs.kinsta.com/api-reference/wordpress-sites/get-list-of-company-sites) **[and](https://api-docs.kinsta.com/api-reference/wordpress-sites/get-list-of-company-sites)**[their environments](https://api-docs.kinsta.com/api-reference/wordpress-sites/get-list-of-company-sites) with a single API call. By adding the `include_environments=true` query parameter to the `GET /sites` endpoint, the response includes each site’s associated environments — no need for separate follow-up requests.

This is especially useful for agencies or teams managing a large number of sites, where minimizing API calls and speeding up environment audits can make a big difference.

```
GET /sites?company=your-company-id&include_environments=true
```

Here’s a sample `curl` request:

```
curl -i -X GET \
'https://api.kinsta.com/v2/sites?company=your-company-id&include_environments=true' \
  -H 'Authorization: Bearer '
```

The response includes site metadata (name, ID, etc.) and a nested list of environments (`staging`, `production`, etc.).

## Kinsta API: Built for teams managing at scale

These API enhancements are designed to save time and reduce complexity, especially for developers and agencies managing dozens (or hundreds) of WordPress sites.

Whether you’re syncing selected plugin files, [building internal tools](https://kinsta.com/topic/api/), or auditing environments across a portfolio, these improvements help streamline the work you’d otherwise have to do manually in the dashboard.

You can explore these new capabilities in the [Kinsta API documentation](https://api-docs.kinsta.com/) or jump straight into [MyKinsta](https://my.kinsta.com/login/) to [generate your access token](https://kinsta.com/blog/kinsta-api-key/) and start building.
