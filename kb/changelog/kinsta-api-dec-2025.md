---
url: "https://kinsta.com/changelog/kinsta-api-dec-2025/"
title: "Track monthly usage and run WP-CLI commands with the Kinsta API"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-05-20T20:31:33"
change_signal: "2026-05-20T20:31:33"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "154a1bcb879993880cc4b4a0b92a4840c238639d3d32fec012738b1612d4507f"
body_chars: 3243
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Track monthly usage and run WP-CLI commands with the Kinsta API

**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-dec-2025/
**Kinsta last updated:** 2026-05-20T20:31:33

## On this page

- [Check current-month visits, bandwidth, and CDN usage](#check-current-month-visits-bandwidth-and-cdn-usage)
- [Run WP-CLI commands programmatically](#run-wp-cli-commands-programmatically)
- [Build on your workflows with the latest Kinsta API additions](#build-on-your-workflows-with-the-latest-kinsta-api-additions)

---

Tracking your website’s resource usage and automating WordPress operations just got easier. This update introduces new endpoints for retrieving current-month usage metrics and running WP-CLI commands directly through the [Kinsta API](https://api-docs.kinsta.com/).

These additions give you clearer visibility into consumption and more flexibility to automate routine WordPress tasks across your sites.

## Check current-month visits, bandwidth, and CDN usage

You can now retrieve **visits**, **server bandwidth**, and **CDN bandwidth** usage metrics for the current billing month. These endpoints make it easy to monitor consumption, power internal dashboards, or trigger alerts when usage approaches plan limits.

Each endpoint returns a simple object containing the site ID and its usage totals for the month.

Here is an example request to get current-month visits:

```
curl -i -X GET \
  'https://api.kinsta.com/v2/sites/{site_id}/usage/visits/this-month' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

Example response:

```
{
  "site": {
    "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "this_month_usage": {
      "visits": 100
    }
  }
}
```

To retrieve **server bandwidth** or **CDN bandwidth**, replace visits with bandwidth or cdn-bandwidth in the endpoint URL.

You can learn more about each usage endpoint in the API documentation for [visits](https://api-docs.kinsta.com/api-reference/analytics/get-visits-usage), [server bandwidth](https://api-docs.kinsta.com/api-reference/analytics/get-server-bandwidth-usage), and [CDN bandwidth](https://api-docs.kinsta.com/api-reference/analytics/get-cdn-bandwidth-usage).

## Run WP-CLI commands programmatically

We now also have a `/run-wp-cli-command` endpoint that lets you execute [WP-CLI commands](https://developer.wordpress.org/cli/commands/) on any environment through the Kinsta API.

This opens the door to automating routine WordPress tasks such as checking the core version, clearing caches, inspecting plugins, or retrieving site details.

Example request:

```
curl -i -X POST \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/run-wp-cli-command' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  -H 'Content-Type: application/json' \
  -d '{
    "wp_command": "wp core version"
  }'
```

After sending the request, the API returns a `202` response, which confirms the command is queued. Any other status code reflects a validation, authentication, or execution issue.

You can test this directly in the [API documentation](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/run-a-wp-cli-command) using the **Try it** button.

## Build on your workflows with the latest Kinsta API additions

These usage and WP-CLI endpoints continue our ongoing expansion of the Kinsta API, following earlier releases of [detailed analytics](https://kinsta.com/changelog/kinsta-api-nov-2025/) and [environment-level controls](https://kinsta.com/changelog/kinsta-api-oct-2025/). Together, they make it easier to automate tasks, monitor resource consumption, and integrate Kinsta more deeply into your internal tools.

You can explore full request and response formats for each endpoint in the [API documentation](https://api-docs.kinsta.com/).
