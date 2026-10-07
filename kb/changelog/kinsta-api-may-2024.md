---
url: "https://kinsta.com/changelog/kinsta-api-may-2024/"
title: "Access application metrics and company user data with Kinsta API"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Access application metrics and company user data with Kinsta API"]
kinsta_last_updated: "2026-05-06T15:09:06+00:00"
sitemap_lastmod: "2026-05-06T15:09:06+00:00"
fetched_at: "2026-10-07T22:37:27Z"
sha256: "b7eb2cdc56b88ac61b7659e544e46bc50341908692417ad0755e855f0170cbdb"
body_chars: 10606
extracted_with: "main article"
status: "live"
---

# Access application metrics and company user data with Kinsta API

**Section:** Changelog > Access application metrics and company user data with Kinsta API
**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-may-2024/
**Kinsta last updated:** 2026-05-06T15:09:06+00:00

## On this page

- [New metrics endpoints for your applications](#new-metrics-endpoints-for-your-applications)
- [Access company users with Kinsta API](#access-company-users-with-kinsta-api)
- [Get started with Kinsta API today](#get-started-with-kinsta-api-today)

---

Updated
:   May 6, 2026

![](https://kinsta.com/wp-content/uploads/2024/04/2024-04-kinsta-changelog-new-Kinsta-API-endpoints-1024x536.png)

We’re excited to announce the release of new endpoints on the [Kinsta API](https://kinsta.com/docs/kinsta-api/) that allow you to [access detailed analytics about your applications](https://api-docs.kinsta.com/tag/Application-Metrics) and [retrieve information about your company users](https://api-docs.kinsta.com/api-reference/company-users/get-list-of-company-users) on Kinsta.

Since launching our [Application Hosting](https://sevalla.com/application-hosting/) service, we have provided application-level analytics that detail your application’s bandwidth, build time, runtime, CPU and memory usage, average response time, HTTP requests, and slowest requests via the [MyKinsta](https://my.kinsta.com/) dashboard (**Applications** > **appname** > **Analytics**).

![Access analytics information for each application in MyKinsta dashboard](https://kinsta.com/wp-content/uploads/2024/04/application-analytics.png)

Access analytics information for each application in the MyKinsta dashboard.

Now, these metrics can be accessed programmatically via the Kinsta API.

## New metrics endpoints for your applications

You can now access the following analytics information via the Kinsta API:

- [Bandwidth](https://api-docs.kinsta.com/tag/Application-Metrics#operation/getApplicationBandwidth) — Total data transmitted in the selected time period.
- [Build time](https://api-docs.kinsta.com/tag/Application-Metrics#operation/getApplicationBuildTime) — Total time it took to build your application.
- [Run time](https://api-docs.kinsta.com/tag/Application-Metrics#operation/getApplicationRunTime) — Total time the application runs after being built and deployed.
- [HTTP requests per minute](https://api-docs.kinsta.com/tag/Application-Metrics#operation/getApplicationHttpRequests) — Total average requests per minute.
- [Average response time](https://api-docs.kinsta.com/tag/Application-Metrics#operation/getApplicationAverageResponseTime) — The average request response time. (If the response time query includes the `percent` parameter with values of 95 or 50, the [P95 latency](https://docs.sevalla.com/applications/analytics#http-p-95-latency) or [P50 latency](https://docs.sevalla.com/applications/analytics#http-p-50-latency) response times will be returned).
- [Slowest requests](https://api-docs.kinsta.com/tag/Application-Metrics#operation/getApplicationSlowestRequests) — This shows you exactly which responses are the slowest within your application.
- [CPU usage](https://api-docs.kinsta.com/tag/Application-Metrics#operation/getApplicationCpuUsage) —The average of the total CPU usage for the selected time period, as a percentage of the instance’s CPU resources.
- [Memory usage](https://api-docs.kinsta.com/tag/Application-Metrics#operation/getApplicationMemoryUsage) — An average of the total memory (RAM) usage for the selected time period.

The [Kinsta API documentation](https://api-docs.kinsta.com/tag/Application-Metrics) provides the necessary path and query parameters for accessing these metrics. For example, to retrieve daily bandwidth usage data, send a GET request to:

```
https://api.kinsta.com/v2/applications/{id}/metrics/bandwidth
```

![Kinsta API documentation showing various parameters to retrieve bandwidth metrics information](https://kinsta.com/wp-content/uploads/2024/04/bandwidth-kinsta-api.png)

Kinsta API documentation showing various parameters to retrieve bandwidth metrics information.

This request will require the following parameters:

- **Path parameter:**
  - `id` — This is the application ID and will be added to the API URL.

- **Query parameters:**
  - `interval_in_seconds` — This is required and measured in seconds, If you want the interval between the returned values to be 24 hours, then you’d convert 24 hours to seconds, which is 86400.
  - `timeframe_start` and `timeframe_end` — These parameters are required, and the ISO 8601 date time format is used. It has a general format of `YYYY-MM-DDThh:mm:ss.sssZ`.

Here’s a detailed breakdown of the ISO 8601 date and time format:

- **YYYY-MM-DD** — Represents the date:
  - **YYYY** — Four-digit year
  - **MM** — Two-digit month (01 to 12)
  - **DD** — Two-digit day of the month (01 to 31)

- **T** — The letter T is used as a separator to distinguish clearly between the date and time parts.
- **hh:mm:ss.sss** — Represents the time:
  - **hh** — Two-digit hour (00 to 23)
  - **mm** — Two-digit minute (00 to 59)
  - **ss** — Two-digit second (00 to 59)
  - **.sss** — Milliseconds, which can be one to three digits, representing a fractional part of a second

- **Z** — Indicates that the time is set to UTC (Coordinated Universal Time). If the time is not in UTC, a time offset can also be included in place of “Z,” formatted as ±hh:mm, where “hh” represents the hour difference and “mm” represents the minute difference from UTC.

Back to our example, you can send a GET request to retrieve daily data between April 20, 2024, and April 28, 2024:

```
curl -i -X GET \
'https://api.kinsta.com/v2/applications/{application_id}/metrics/bandwidth?interval_in_seconds=86400&timeframe_start=2024-04-20T18%3A10%3A45.511Z&timeframe_end=2024-04-28T18%3A10%3A45.511Z' \
  -H 'Authorization: Bearer '
```

Replace `{application_id}` and `<YOUR_TOKEN_HERE>` with your application ID and API token, respectively. When you send this request, the following data format is returned:

```
{
  "app": {
    "id": "MY_APP_ID",
    "display_name": "Kinsta-developer-portfolio",
    "metrics": {
      "timeframe": {
        "start": "1713571200000",
        "end": "1714262400000"
      },
      "bandwidth": [
        {
          "time": "1713571200000",
          "value": "18205"
        },
        {
          "time": "1713657600000",
          "value": "834750"
        },
        {
          "time": "1713744000000",
          "value": "146959"
        },
        {
          "time": "1713830400000",
          "value": "142413"
        },
        {
          "time": "1713916800000",
          "value": "165352"
        },
        {
          "time": "1714089600000",
          "value": "109015"
        },
        {
          "time": "1714176000000",
          "value": "628641"
        }
      ]
    }
  }
}
```

The response specifies the timeframe’s start and end based on what was sent via the request. If you put it into the `new Date()` constructor, you get the date/time object. Also, the bandwidth returns an array of objects containing the time (timestamp given for each day — based on the interval set) and the value in bytes.

When you convert each of these data accordingly, it means the following:

**Timeframe**

- Start: 2024-04-20 00:00:00
- End: 2024-04-29 00:00:00

**Bandwidth (converted to MB)**

- Time: 2024-04-20 00:00:00, Value: 0.0174 MB
- Time: 2024-04-21 00:00:00, Value: 0.7961 MB
- Time: 2024-04-22 00:00:00, Value: 0.1402 MB
- Time: 2024-04-23 00:00:00, Value: 0.1358 MB
- Time: 2024-04-24 00:00:00, Value: 0.1577 MB
- Time: 2024-04-26 00:00:00, Value: 0.1040 MB
- Time: 2024-04-27 00:00:00, Value: 0.5995 MB
- Time: 2024-04-28 00:00:00, Value: 5.8086 MB

This means you can programmatically get information about each of these analytic information into another platform without needing to navigate the MyKinsta dashboard for each application.

For example, you can [create a Slackbot that uses Slack’s Slash command](https://kinsta.com/blog/create-slackbot-site-management/) to access this information from Slack or create a reminder to inform you when the daily bandwidth, CPU, or memory usage crosses a particular threshold.

## Access company users with Kinsta API

In response to client requests, we’ve added an endpoint for retrieving details about Kinsta account company users, including their full name, email, and gravatar image URL.

This aligns with our commitment to prioritize features based on user feedback. If you believe a specific tool or endpoint should be included in the Kinsta API, feel free to [send your feedback](https://kinsta.com/docs/service-information/kinsta-research-program/#how-to-join).

To access this data, send a GET request to: `https://api.kinsta.com/v2/company/{company_id}/users`. Ensure to replace `{company_id}` with your company ID. This will return a response like:

```
{
  "company": {
    "users": [
      {
        "user": {
          "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
          "email": "[email protected]",
          "image": "https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
          "full_name": "John Doe"
        }
      }
    ]
  }
}
```

## Get started with Kinsta API today

To use the Kinsta API, you need an active Kinsta account with at least one WordPress site, application, or database in MyKinsta. Here’s how to generate an API key:

1. Go to your [MyKinsta](https://my.kinsta.com/) dashboard.
2. Navigate to the API Keys page (**Your name** > **Company settings** > **API Keys**).
3. Click **Create API Key**.
4. Choose an expiration or set a custom start date and number of hours for the key to expire.
5. Give the key a unique name.
6. Click Generate.

When the API key is created, make sure you copy it and store it somewhere safe, as this is the only time you can see it. We recommend using a [password manager](https://kinsta.com/blog/password-managers/) like 1Password to share it securely.

There is a lot that can be done with the Kinsta API. Feel free to check out our [documentation](https://kinsta.com/docs/kinsta-api/) to understand [what’s possible](https://kinsta.com/docs/kinsta-api/#common-use-cases) with the API, how to get started, and the various [permission levels](https://kinsta.com/docs/kinsta-api/#authentication-and-user-access) and [limits to the API](https://kinsta.com/docs/kinsta-api/#rate-limit).

You can also check out our previous changelogs for the Kinsta API:

- [Introducing Kinsta API: The Power of Automation for Site Management](https://kinsta.com/changelog/kinsta-api/)
- [Introducing New Kinsta API Endpoints: Environment CRUD, Edge Caching, Application Deployment](https://kinsta.com/changelog/kinsta-api-aug-2023/)
- [New Kinsta API Endpoints: Clear CDN Cache and Push Environment](https://kinsta.com/changelog/kinsta-api-sept-2023/)
- [New Kinsta API endpoints enhance WordPress site management](https://kinsta.com/changelog/kinsta-api-feb-2024/)
- [3 new Kinsta API endpoints for Application Hosting (CDN, Edge Caching, & clear cache)](https://kinsta.com/changelog/kinsta-api-mar-2024/)
