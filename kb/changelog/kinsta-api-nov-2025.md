---
url: "https://kinsta.com/changelog/kinsta-api-nov-2025/"
title: "Access website analytics with the Kinsta API"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Access website analytics with the Kinsta API"]
kinsta_last_updated: "2026-05-20T20:31:39+00:00"
sitemap_lastmod: "2026-05-20T20:31:39+00:00"
fetched_at: "2026-10-07T22:37:42Z"
sha256: "60faba202a115ee0b24a122d178bf4950d0c1995d879ec0116f00d59799585cc"
body_chars: 6163
extracted_with: "main article"
status: "live"
---

# Access website analytics with the Kinsta API

**Section:** Changelog > Access website analytics with the Kinsta API
**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-nov-2025/
**Kinsta last updated:** 2026-05-20T20:31:39+00:00

## On this page

- [Get site bandwidth data](#get-site-bandwidth-data)
- [Get visits data](#get-visits-data)
  - [Get CDN bandwidth usage](#get-cdn-bandwidth-usage)
- [Get disk space usage](#get-disk-space-usage)
- [Build analytics into your own tools](#build-analytics-into-your-own-tools)

---

Updated
:   May 20, 2026

![](https://kinsta.com/wp-content/uploads/2025/11/new-api-endpoints-1024x536.png)

[Analytics](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/) has always been one of the most-requested features for the [Kinsta API](https://api-docs.kinsta.com/), and it’s finally here.

The first release of analytics endpoints covers [bandwidth](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#bandwidth), [visits](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#visits), [CDN bandwidth](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#cdn-bandwidth), and [disk space](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#disk-space), enabling developers, agencies, and automation tools to monitor resource usage and generate reports programmatically.

Let’s examine these endpoints and how they work.

## Get site bandwidth data

The new [bandwidth endpoint](https://api-docs.kinsta.com/api-reference/analytics/get-server-bandwidth-usage) lets you retrieve total bandwidth usage for a site or environment over a specific time range.

You can define the time span, such as `24_hours`, `7_days`, `30_days`, `60_days`, or specify exact dates for more granular reporting.

For example, here’s how to request data for the last seven days:

```
curl -i -X GET \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bandwidth?company_id={company_id}&time_span=7_days' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

Make sure to replace `{env_id}` and `{company_id}` with your actual environment and company IDs.

For a custom date range, include `from` and `to` parameters in `YYYY-MM-DD` format:

```
curl -i -X GET \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bandwidth?company_id={company_id}&from=2025-10-01&to=2025-10-15' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

The response includes total bandwidth and daily breakdowns over your chosen period, so you can easily visualize trends or integrate the data into dashboards.

```
{
  "analytics": {
    "analytics_response": {
      "key": "bandwidth",
      "data": [
        {
          "name": "bandwidth",
          "total": 1000,
          "dataset": [
            { "key": "2025-10-28T00:00:00", "value": "1000" }
          ]
        }
      ]
    }
  }
}
```

You can find full parameter options and sample queries in the [API documentation for bandwidth analytics](https://api-docs.kinsta.com/api-reference/analytics/get-server-bandwidth-usage).

## Get visits data

You can now fetch total and per-day visit counts for any environment, allowing you to track traffic and user activity programmatically. As with bandwidth, you can define time ranges or specific date intervals.

**Example request:**

```
curl -i -X GET \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/visits?company_id={company_id}&time_span=30_days' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

**Example response:**

```
{
  "analytics": {
    "analytics_response": {
      "key": "uniqueip",
      "data": [
        {
          "name": "uniqueip",
          "total": 1000,
          "dataset": [
            { "key": "2025-10-28T00:00:00", "value": "1000" }
          ]
        }
      ]
    }
  }
}
```

Learn more about available fields and filters in the [API documentation for visits analytics](https://api-docs.kinsta.com/api-reference/analytics/get-visits-usage).

### Get CDN bandwidth usage

If you’re using Kinsta CDN, you can now programmatically monitor total CDN bandwidth for each environment.

The endpoint supports flexible time spans and date filters, allowing you to measure CDN data transfer over time or within custom reporting windows.

**Example request:**

```
curl -i -X GET \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/cdn-bandwidth?company_id={company_id}&time_span=30_days' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

**Example response:**

```
{
  "analytics": {
    "analytics_response": {
      "key": "cdn-bandwidth",
      "data": [
        {
          "name": "cdn-bandwidth",
          "total": 1000,
          "dataset": [
            { "key": "2025-10-28T00:00:00", "value": "1000" }
          ]
        }
      ]
    }
  }
}
```

You can find full query parameters and output examples in the [API documentation for CDN bandwidth analytics](https://api-docs.kinsta.com/api-reference/analytics/get-cdn-bandwidth-usage).

## Get disk space usage

This endpoint enables you to check the total disk space usage for a specific environment, including trends over time. It’s especially helpful for automating capacity checks, setting alerts for storage thresholds, or integrating data into monitoring dashboards.

Like others, you can query by company ID, time span, date range, and timezone to generate precise disk usage analytics.

**Example request:**

```
curl -i -X GET \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/diskspace?company_id={company_id}&time_zone=02:00&time_span=30_days' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

**Example response:**

```
{
  "analytics": {
    "analytics_response": {
      "key": "diskSpaceUsage",
      "data": [
        {
          "name": "diskSpaceUsage",
          "total": 1000,
          "dataset": [
            { "key": "2025-10-28T00:00:00", "value": "1000" }
          ]
        }
      ]
    }
  }
}
```

See all available parameters and response formats in the [API documentation for disk space analytics](https://api-docs.kinsta.com/api-reference/analytics/get-disk-space).

## Build analytics into your own tools

These new analytics endpoints give developers more visibility into their Kinsta-hosted environments directly from their automation and reporting workflows.

Whether you’re tracking bandwidth, visits, or disk space, you can now integrate Kinsta data into your internal dashboards, third-party analytics platforms, or custom billing systems.

You can find all request examples and schema references in the [Kinsta API documentation](https://api-docs.kinsta.com/).
