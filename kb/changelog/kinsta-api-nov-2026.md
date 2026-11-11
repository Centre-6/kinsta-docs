---
url: "https://kinsta.com/changelog/kinsta-api-nov-2026/"
title: "Manage bot protection and analyze bot traffic with the Kinsta API"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-11-04T20:26:02"
change_signal: "2026-11-04T20:26:02"
fetched_at: "2026-11-11T13:03:01Z"
sha256: "2821663f60b1b0323f5b717acbcabcbe0105831219874b5058c2621cb4f56080"
body_chars: 13859
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Manage bot protection and analyze bot traffic with the Kinsta API

**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-nov-2026/
**Kinsta last updated:** 2026-11-04T20:26:02

## On this page

- [Check and change bot protection levels](#check-and-change-bot-protection-levels)
- [Block or unblock AI crawlers](#block-or-unblock-ai-crawlers)
- [Control WordPress automations](#control-wordpress-automations)
- [Add, retrieve, and remove bot protection exceptions](#add-retrieve-and-remove-bot-protection-exceptions)
- [Analyze bot traffic through the API](#analyze-bot-traffic-through-the-api)
  - [See how bot protection handles incoming traffic](#see-how-bot-protection-handles-incoming-traffic)
  - [**Track bot traffic and protection results over time**](#track-bot-traffic-and-protection-results-over-time)
  - [Identify the top sources of bot traffic](#identify-the-top-sources-of-bot-traffic)
- [Bring bot protection into your site management workflows](#bring-bot-protection-into-your-site-management-workflows)

---

You can now configure [Kinsta’s Bot Protection](https://kinsta.com/bot-protection/) and retrieve detailed bot traffic analytics through the Kinsta API.

We’ve added 13 new endpoints that let you check and change protection levels, block AI crawlers, manage WordPress automation settings, and create custom exception rules. You can also retrieve analytics showing how traffic is classified, how requests are handled, and which sources account for the most activity.

These additions let you include bot protection in your site management tools, monitoring systems, and automated workflows.

## Check and change bot protection levels

Two new endpoints let you retrieve and change the bot protection level for a WordPress environment.

The [Get bot protection level](https://api-docs.kinsta.com/api-reference/wordpress-bot-protection/get-the-bot-protection-level-of-an-environment) endpoint returns the environment’s current configuration:

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level \
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

For example, the response below shows that the environment is configured to block automated traffic:

```
{
  "bot_protection": {
    "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "level": "block-automations"
  }
}
```

You can use the new [Set bot protection level](https://api-docs.kinsta.com/api-reference/wordpress-bot-protection/set-the-bot-protection-level-of-an-environment) endpoint to switch between four supported levels:

- `block-malicious-traffic` blocks known malicious traffic as part of Kinsta’s baseline protection.
- `block-automations` blocks automated and malicious traffic.
- `challenge-bots` also challenges likely bots and unclassified traffic.
- `challenge-everyone` applies challenges to all unverified traffic, including likely human visitors.

For example, if a site experiences increased scraping or suspicious automated requests, you can switch to Challenge bots:

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level \
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  --header 'Content-Type: application/json' \
  --data '{
    "level": "challenge-bots"
  }'
```

The API returns a `202` response with an operation ID:

```
{
  "message": "Setting a bot protection level in progress. Use the operation_id to check the status.",
  "status": 202,
  "operation_id": "environment:set-bot-protection-level-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
}
```

You can use the returned `operation_id` to track the request until the change is complete.

Higher protection levels can affect legitimate automated requests and, at the strictest level, introduce challenges for visitors. Check how the [selected level affects](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#when-to-enable-a-higher-level-of-kinstas-bot-protection) your site’s normal traffic before applying it more widely.

## Block or unblock AI crawlers

The API also provides two endpoints for managing the Block AI crawlers setting. You can use the [Get AI crawler block status](https://api-docs.kinsta.com/api-reference/wordpress-bot-protection/get-the-ai-crawler-block-status-of-an-environment) endpoint to check whether blocking is enabled:

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/ai-crawlers \
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

The response includes the `ai_crawlers_blocking` field, which indicates whether the setting is `enabled` or `disabled`.

To change the setting, send a PUT request to the same path:

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/ai-crawlers \
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  --header 'Content-Type: application/json' \
  --data '{
    "status": "enabled"
  }'
```

Setting `status` to `enabled` blocks AI crawlers, including verified crawlers that collect website content for AI training and related purposes. Use `disabled` to turn off this specific restriction.

Kinsta’s Block AI crawlers setting doesn’t block traditional search engine crawlers such as Googlebot and Bingbot, AI search crawlers such as `OAI-SearchBot`, or user-initiated AI agents such as `ChatGPT-User`. However, requests from these sources may still be challenged under stricter protection levels if they exhibit excessive behavior.

This gives you a separate control for automated AI content collection without changing your site’s overall protection level.

See the [Block or unblock AI crawlers API documentation](https://api-docs.kinsta.com/api-reference/wordpress-bot-protection/block-or-unblock-ai-crawlers-for-an-environment) for the full request and response details.

## Control WordPress automations

Some WordPress features and integrations rely on automated requests to your site. These can include external services accessing the [WordPress REST API](https://kinsta.com/blog/wordpress-rest-api/), plugins exchanging data with third-party services, or automation platforms sending webhooks.

Two new endpoints let you check and control whether typical WordPress automations are allowed through bot protection.

The [Get WP automations allow status](https://api-docs.kinsta.com/api-reference/wordpress-bot-protection/get-the-wp-automations-allow-status-of-an-environment) endpoint returns the current setting:

```
{
  "bot_protection": {
    "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "wp_automations": "enabled"
  }
}
```

You can then use the [Allow or block WP automations](https://api-docs.kinsta.com/api-reference/wordpress-bot-protection/allow-or-block-wp-automations-for-an-environment) endpoint to change it. For example, the following request enables the allowance for typical WordPress automations:

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/wp-automations \
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  --header 'Content-Type: application/json' \
  --data '{
    "status": "enabled"
  }'
```

The request returns an operation ID that you can use to track the change. This setting uses a Kinsta-managed allowlist of common WordPress endpoints and services. It can help when stricter bot protection interferes with an external integration or automated process your site depends on.

Requests originating from within the site’s own container or Kinsta-managed internal infrastructure are already allowed, so normal internal WordPress tasks aren’t affected by this setting.

## Add, retrieve, and remove bot protection exceptions

Sometimes you need more specific rules than a general protection level provides. For example, you may want to allow requests from a trusted monitoring service while still challenging other automated traffic.

Three new endpoints let you manage bot protection exceptions for individual WordPress environments.

You can create an exception using the [Add bot protection exception rule](https://api-docs.kinsta.com/api-reference/wordpress-bot-protection/add-a-bot-protection-exception-rule-to-an-environment) endpoint. Each rule has three required fields:

- `type` identifies what to match: `ip`, `path`, `user_agent`, or `country`.
- `action` determines what happens to matching traffic: `skip`, `challenge`, or `block`.
- `value` contains the IP address, path, user agent, or country to match.

For example, the following request adds an exception that allows requests from a trusted IP address to bypass bot protection rules:

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules \
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  --header 'Content-Type: application/json' \
  --data '{
    "type": "ip",
    "action": "skip",
    "value": "192.0.2.1"
  }'
```

The API returns an operation ID when it accepts the request. To inspect the configured exceptions, use the [Get bot protection exception rules](https://api-docs.kinsta.com/api-reference/wordpress-bot-protection/get-the-bot-protection-exception-rules-of-an-environment) endpoint:

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules \
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

The response lists the rules, including their IDs, matching values, and actions:

```
{
  "bot_protection": {
    "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "exception_rules": [
      {
        "id": "ip:skip:192.0.2.1",
        "type": "ip",
        "action": "skip",
        "value": "192.0.2.1"
      }
    ],
    "has_custom_waf_rules": false
  }
}
```

You can use the rule ID with the new [Remove bot protection exception rule](https://api-docs.kinsta.com/api-reference/wordpress-bot-protection/remove-a-bot-protection-exception-rule-from-an-environment) endpoint:

```
curl --request DELETE \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules \
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  --header 'Content-Type: application/json' \
  --data '{
    "exception_rule_id": "ip:skip:192.0.2.1"
  }'
```

Exceptions apply to individual environments, so a rule created for a staging environment doesn’t automatically apply to production.

The `skip` action bypasses bot protection rules, but it doesn’t override Kinsta’s underlying platform security or vulnerability protection.

## Analyze bot traffic through the API

Alongside the nine bot protection management endpoints, we’ve added four endpoints to the Analytics section.

These provide data about the requests reaching your site, how Kinsta classifies that traffic, and what happens to those requests after bot protection evaluates them.

### See how bot protection handles incoming traffic

The new [Get bot traffic flow](https://api-docs.kinsta.com/api-reference/analytics/get-bot-traffic-flow) endpoint returns request totals by traffic classification and protection result.

You can use it to see how many requests were classified as likely humans, likely bots, AI crawlers, or other traffic types, and how many were allowed, challenged, or blocked.

For example, the following request retrieves data for the last 30 days:

```
curl --request GET \
  --url 'https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bot-protection/traffic-flow?company_id={company_id}&time_span=30_days' \
  --header 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

The response contains three main sections within `traffic_flow`: `traffic_types`, `results`, and `flows`. The `flows` object connects each traffic classification to its protection outcomes.

This lets you see what happened to the traffic instead of looking only at an overall blocked-request count.

### **Track bot traffic and protection results over time**

Two additional endpoints provide time-series analytics:

- [Get bot traffic requests over time](https://api-docs.kinsta.com/api-reference/analytics/get-bot-traffic-requests-over-time) returns request counts grouped by traffic classification.
- [Get bot protection results over time](https://api-docs.kinsta.com/api-reference/analytics/get-bot-protection-results-over-time) returns the number of requests allowed, challenged, or blocked over the selected period.

Both return hourly data when `time_span` is set to `24_hours` and daily data for longer periods.

For example, the requests-over-time endpoint returns data in this format:

```
{
  "analytics": {
    "requests_over_time": [
      {
        "traffic_type": "likely_humans",
        "label": "Likely humans",
        "total": 10572,
        "timeline": [
          {
            "date": "2026-09-14T00:00:00.000Z",
            "requests": 5286
          }
        ]
      }
    ]
  }
}
```

This data can help you investigate unusual traffic increases and see whether changes to bot protection settings affect the number of requests being challenged or blocked.

### Identify the top sources of bot traffic

The new [Get bot traffic top breakdown](https://api-docs.kinsta.com/api-reference/analytics/get-bot-traffic-top-breakdown) endpoint provides more detail about the sources behind each traffic classification. It returns the top requested paths, user agents, countries, and IP addresses, along with their request counts.

For example, if your site has a sudden increase in automated requests, you can check whether those requests are concentrated on `/wp-login.php`, a particular API path, or from specific IP addresses.

The endpoint returns the information under `analytics.top_requests_breakdown`, with separate `top_paths`, `top_user_agents`, `top_countries`, and `top_ips` arrays for each traffic category.

All four new analytics endpoints support `24_hours`, `7_days`, `30_days`, and `60_days`, with `7_days` as the default. You can also use the optional `from` and `to` parameters to request a custom date range. Each request requires a `company_id` query parameter.

## Bring bot protection into your site management workflows

With these endpoints, you can include bot protection settings alongside other tasks managed through the Kinsta API.

For example, a monitoring tool can retrieve bot traffic analytics during a traffic spike, while an internal management system can check an environment’s current protection level and apply a different setting when needed. You can also manage exceptions for trusted services without configuring each environment manually.

Find the complete request and response formats in the [WordPress Bot Protection API reference](https://api-docs.kinsta.com/pages/wordpress-bot-protection/description) and the [Kinsta API Analytics documentation](https://api-docs.kinsta.com/api-reference/analytics/get-bot-traffic-flow).
