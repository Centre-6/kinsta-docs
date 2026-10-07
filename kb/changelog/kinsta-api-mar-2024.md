---
url: "https://kinsta.com/changelog/kinsta-api-mar-2024/"
title: "3 new Kinsta API endpoints for Application Hosting (CDN, Edge Caching, & clear cache)"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-05-06T15:15:29"
change_signal: "2026-05-06T15:15:29"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "57c265010cc7e20ccbd31d02e61320d2c0a9630b6981ad696d137862889d24a9"
body_chars: 5650
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# 3 new Kinsta API endpoints for Application Hosting (CDN, Edge Caching, & clear cache)

**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-mar-2024/
**Kinsta last updated:** 2026-05-06T15:15:29

## On this page

- [1. Application CDN](#1-application-cdn)
  - [CDN activation/deactivation](#cdn-activationdeactivation)
- [2. Application Edge Cache](#2-application-edge-cache)
  - [Edge Cache activation/deactivation](#edge-cache-activationdeactivation)
- [3. Clear application cache](#3-clear-application-cache)
  - [Clear cache activation](#clear-cache-activation)
- [Get started with Kinsta API today](#get-started-with-kinsta-api-today)

---

We are excited to announce the addition of three new endpoints to the [Kinsta API](https://kinsta.com/docs/kinsta-api/) for our [Application Hosting](https://sevalla.com/application-hosting/) service.

These endpoints are designed to enhance your ability to manage content delivery and caching strategies directly through our API, providing more control and flexibility over your application’s performance and response times.

## 1. Application CDN

Kinsta’s Application Hosting offers a premium [CDN](https://docs.sevalla.com/applications/cdn) service powered by Cloudflare at **no extra cost.** The CDN enhances security with an enterprise-level firewall and DDoS protection while leveraging Cloudflare’s expansive global network across 300+ locations in over 100 countries.

This allows for the efficient distribution of static assets, improving application performance. It caches files based on their extension, excluding files accessed with an Authorization header, and supports a wide range of file types.

The CDN is not enabled by default and requires activation/deactivation via a `POST` request to the [CDN API endpoint](https://api-docs.kinsta.com/tag/Application-CDN).

### CDN activation/deactivation

To use this endpoint, you need your application’s unique ID. You can obtain this programmatically by [listing all applications](https://api-docs.kinsta.com/tag/Applications#operation/getApplications) associated with your Kinsta company, which provides essential details about each application.

With the application ID in hand, You can send a `POST` request to `/applications/${application_id}/cdn/toggle-status`, and it toggles the feature:

```
curl -i -X POST \
 'https://api.kinsta.com/v2/applications/{application_id}/cdn/toggle-status' \
 -H 'Authorization: Bearer '
```

Ensure you replace `<YOUR_TOKEN_HERE>` with your actual [API key](https://kinsta.com/blog/kinsta-api-key/) and `{application_id}` with the specific application ID.

## 2. Application Edge Cache

The [Edge Caching](https://docs.sevalla.com/applications/edge-caching) feature for Kinsta Application Hosting enhances your application’s performance and speed by caching your application’s web pages across Cloudflare’s global network. This ensures cached responses are delivered from the closest location to your visitors.

Edge Caching does not handle static assets like image, [JavaScript](https://kinsta.com/blog/what-is-javascript/), and [CSS](https://kinsta.com/blog/css-best-practices/) files; these can be served through Kinsta’s CDN, which operates independently and provides an additional caching layer.

By default, Edge Caching is not enabled. To enable or disable Edge Caching for applications, send a `POST` request to the [edge-cache API endpoint](https://api-docs.kinsta.com/tag/Application-Edge-Caching).

### Edge Cache activation/deactivation

As with the CDN endpoint, you need an application ID to send this request. With the application ID in hand, send a `POST` request to `/applications/${application_id}/edge-cache/toggle-status`, and it toggles the feature:

```
curl -i -X POST \
 'https://api.kinsta.com/v2/applications/{application_id}/edge-cache/toggle-status' \
 -H 'Authorization: Bearer '
```

Ensure you replace `<YOUR_TOKEN_HERE>` with your actual [API key](https://kinsta.com/blog/kinsta-api-key/) and `{application_id}` with the specific application ID.

## 3. Clear application cache

The [clear-cache API endpoint](https://api-docs.kinsta.com/tag/Application-Clear-Cache) allows for the clearing of both CDN and Edge Cache, ensuring that any updates to your application are promptly reflected across all caching layers. This functionality is crucial for maintaining the freshness of your content, especially after making significant changes.

The process of clearing the CDN Cache and Edge Cache is integrated, meaning a single request will clear both caches if they are enabled. It can take two to five minutes to completely clear the cache across all data centers.

### Clear cache activation

As with the CDN and Edge cache endpoints, you need an application ID to send this request. With the application ID in hand, You can send a `POST` request to `/applications/${application_id}/clear-cache`:

```
curl -i -X POST \
 'https://api.kinsta.com/v2/applications/{application_id}/clear-cache' \
 -H 'Authorization: Bearer '
```

Ensure you replace `<YOUR_TOKEN_HERE>` with your actual [API key](https://kinsta.com/blog/kinsta-api-key/) and `{application_id}` with the specific application ID.

## Get started with Kinsta API today

You can do a lot with the Kinsta API, and the Kinsta team is actively adding new endpoints. Kristof Siket, our Development Team Lead for the Kinsta API, notes:

> User feedback drives the prioritization of feature exposure. If you believe a specific tool or endpoint should be included in the Kinsta API, feel free to [send in your feedback](https://kinsta.com/docs/service-information/kinsta-research-program/#how-to-join).

Check out previously published changelogs for the Kinsta API to understand what’s possible, how to get started, and the various permission levels and limits of the API:

- [Introducing Kinsta API: The Power of Automation for Site Management](https://kinsta.com/changelog/kinsta-api/)
- [Introducing New Kinsta API Endpoints: Environment CRUD, Edge Caching, Application Deployment](https://kinsta.com/changelog/kinsta-api-aug-2023/)
- [New Kinsta API Endpoints: Clear CDN Cache and Push Environment](https://kinsta.com/changelog/kinsta-api-sept-2023/)
- [New Kinsta API endpoints enhance WordPress site management](https://kinsta.com/changelog/kinsta-api-feb-2024/)
