---
url: "https://kinsta.com/changelog/kinsta-api-may-2025/"
title: "Fine-tune CDN, edge cache, and PHP behavior via the Kinsta API"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Fine-tune CDN, edge cache, and PHP behavior via the Kinsta API"]
kinsta_last_updated: "2026-05-20T20:32:09+00:00"
sitemap_lastmod: "2026-05-20T20:32:09+00:00"
fetched_at: "2026-10-07T22:37:45Z"
sha256: "6f3f767773ec19cd2fe928550071a3bebff5a8fa0c29f8beeca344ab12c455e9"
body_chars: 6977
extracted_with: "main article"
status: "live"
---

# Fine-tune CDN, edge cache, and PHP behavior via the Kinsta API

**Section:** Changelog > Fine-tune CDN, edge cache, and PHP behavior via the Kinsta API
**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-may-2025/
**Kinsta last updated:** 2026-05-20T20:32:09+00:00

## On this page

- [Control image optimization](#control-image-optimization)
- [Enable or disable edge caching](#enable-or-disable-edge-caching)
- [Opt out of automatic PHP updates](#opt-out-of-automatic-php-updates)
- [New fields in environment responses](#new-fields-in-environment-responses)
- [Why this matters](#why-this-matters)

---

Updated
:   May 20, 2026

![](https://kinsta.com/wp-content/uploads/2025/05/new-kinsta-api-endpoints-1024x536.png)

[Kinsta’s API](https://kinsta.com/docs/kinsta-api/) just got a fresh set of updates that give developers and site managers more control over how their sites perform at the edge and behind the scenes.

Whether you’re developing automation scripts or [building custom tooling](https://kinsta.com/topic/api/) for your environment, these additions make it easier to precisely manage CDN behavior, cache settings, and PHP version updates.

## Control image optimization

You can now [manage image optimization settings](https://api-docs.kinsta.com/api-reference/wordpress-cdn/update-cdn-image-optimization) for any environment using the Kinsta API. This new endpoint gives developers the flexibility to adjust how Kinsta compresses and serves images without needing to log in to MyKinsta.

This is especially useful if you’re automating deployments or managing multiple environments at scale. Depending on your use case, you can choose one of the following optimization modes:

- `off` — Disables image optimization entirely.
- `lossy` — Applies aggressive compression for smaller file sizes and faster load times, at the cost of some visual fidelity.
- `lossless` — Compresses images without reducing quality, preserving sharpness while still reducing file size.

To update the image optimization setting for an environment, send a `PUT` request to:

```
PUT /sites/cdn/image-optimization
```

Your request body should include the `environment_id` and desired optimization type. Here’s a quick example using `curl` to apply lossy optimization:

```
curl -i -X PUT \
  https://api.kinsta.com/v2/sites/cdn/image-optimization \
  -H 'Authorization: Bearer ' \
  -H 'Content-Type: application/json' \
  -d '{
    "environment_id": "your-environment-id",
    "image_optimization_type": "lossy"
  }'
```

This update gives you more control over how media assets are delivered — ideal for tailoring performance across production, staging, or media-heavy environments.

For more information on how image optimization works at Kinsta, check out our [CDN documentation](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#image-optimization-1).

## Enable or disable edge caching

You can now toggle [Edge Caching](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/) for a specific environment using the Kinsta API. This [new endpoint](https://api-docs.kinsta.com/api-reference/wordpress-edge-caching/update-site-edge-cache-status) allows you to programmatically enable or disable caching at the edge, giving you greater control over how content is served across Kinsta’s global CDN.

This is especially useful during deployments, testing, or troubleshooting scenarios where you need to temporarily bypass or reinstate cached content.

You can send a `PUT` request to:

```
PUT /sites/edge-caching/status
```

Include the `environment_id` and a boolean `enabled` field in the request body. Here’s a sample request using `curl` to enable Edge Caching:

```
curl -i -X PUT \
  https://api.kinsta.com/v2/sites/edge-caching/status \
  -H 'Authorization: Bearer ' \
  -H 'Content-Type: application/json' \
  -d '{
    "environment_id": "your-environment-id",
    "enabled": true
  }'
```

Setting `"enabled"` to `false` disables Edge Caching for that environment. This is helpful if you’re actively pushing updates and want to avoid caching delays.

## Opt out of automatic PHP updates

We’ve added a new level of control to the Kinsta API for [managing PHP versions](https://api-docs.kinsta.com/api-reference/wordpress-site-tools/modify-an-environments-php-version). When modifying an environment’s PHP version, you can now include the optional `is_opt_out_from_automatic_php_update` flag to opt out of future automatic upgrades.

This update is especially helpful for teams that need to maintain version consistency across environments or delay updates to ensure compatibility with custom code, plugins, or legacy dependencies.

Send a `PUT` request to:

```
PUT /sites/tools/modify-php-version
```

The request body should include your environment ID, target PHP version, and the new `is_opt_out_from_automatic_php_update` flag set to `true` or `false`. Here’s a sample `curl` request:

```
curl -i -X PUT \
  https://api.kinsta.com/v2/sites/tools/modify-php-version \
  -H 'Authorization: Bearer ' \
  -H 'Content-Type: application/json' \
  -d '{
    "environment_id": "your-environment-id",
    "php_version": "8.1",
    "is_opt_out_from_automatic_php_update": true
  }'
```

Setting this flag to `true` keeps your environment on the selected PHP version unless you update it manually via the API or in the [MyKinsta dashboard](https://kinsta.com/mykinsta/). If the flag is omitted or set to `false`, the environment follows Kinsta’s default auto-update schedule for supported PHP versions.

For more information, you can review our [PHP management documentation](https://kinsta.com/docs/wordpress-hosting/php/wordpress-restart-update-php/#update-php).

## New fields in environment responses

The `GET /sites/{site_id}/environments` endpoint now returns two additional fields that provide better visibility into how each environment is configured:

- `image_optimization_type` — Displays the current image optimization setting applied via the CDN. This can be `"off"`, `"lossy"`, or `"lossless"`, and helps you confirm optimization levels across environments at a glance.
- `is_opt_out_from_automatic_php_update` — Indicates whether automatic PHP updates are disabled for the environment. If set to `true`, the environment won’t receive scheduled PHP upgrades.

This enhancement makes it easier to audit and manage environment-specific settings programmatically, especially useful for teams working across staging, development, and production instances.

Here’s a simplified example of a response snippet:

```
{
  "id": "your-environment-id",
  "name": "production",
  "image_optimization_type": "lossy",
  "is_opt_out_from_automatic_php_update": true
}
```

You can learn more in our [API reference for environment endpoints](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-site-environments).

## Why this matters

These updates are all about giving you more control, especially if you’re managing multiple environments or automating your workflow.

- Fine-tune image performance without logging into the dashboard.
- Manage Edge Caching behavior directly via API, which is ideal for deployment pipelines.
- Ensure PHP version compatibility by locking environments to a specific version when needed.
- Audit environment settings at scale with new response fields.

Together, these changes make it easier to build with Kinsta on your terms using the tools and automations that already work for your team.

You’ll find full request and response details in the [Kinsta API documentation](https://api-docs.kinsta.com/).
