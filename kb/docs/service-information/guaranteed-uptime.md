---
url: "https://kinsta.com/docs/service-information/guaranteed-uptime/"
title: "Service Information - Guaranteed Uptime"
tier: "docs"
product: "service-information"
product_label: "Service Information"
subsection: "guaranteed-uptime"
section: []
kinsta_last_updated: "October 24, 2025"
sitemap_lastmod: "2025-10-24T15:01:47+00:00"
fetched_at: "2026-10-07T22:37:38Z"
sha256: "eb38cf386d6be4bb2a09690aae821c65782a826e36f2e6b4e1ceda7a2a1eceeb"
body_chars: 3389
extracted_with: "main article"
status: "live"
---

# Service Information - Guaranteed Uptime

**Product:** Service Information
**Source:** https://kinsta.com/docs/service-information/guaranteed-uptime/
**Kinsta last updated:** October 24, 2025

---

At Kinsta, whilst we do not offer high availability (HA) hosting, we do offer a Service Level Agreement (SLA)  backed uptime guarantee. At Kinsta, every site on our platform runs in a single Linux container, and the site database runs as a service within the site container, all built on high-performance, enterprise-grade servers. We do not run multiple load-balanced instances of each site infrastructure.

For more details about our infrastructure and architecture, refer to [WordPress Hosting infrastructure](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/wordpress-infrastructure/).

Thanks to the flexibility of container-based infrastructure, proactive load management by our Engineering team, and leading cloud platforms, we are able to offer an [SLA-backed uptime guarantee of up to](https://kinsta.com/legal/service-level-agreement/) [99.9%](https://kinsta.com/legal/service-level-agreement/). For custom plans, we can offer an enhanced uptime guarantee of up to 99.99%. For more information, please [contact our Sales team](https://kinsta.com/talk-to-sales/).

## Maintenance period

Kinsta’s maintenance period is daily, Monday through Sunday, from 2 am to 5 am local time, based on the time zone of the data center where each site is hosted. We do not send monitoring notifications if maintenance is performed during this time. For more information, refer to [Kinsta’s Service Level Agreement](https://kinsta.com/legal/service-level-agreement/).  

## Circumstances that block uptime monitoring

To ensure we meet our uptime guarantee, we monitor every site on our platform. When one of our uptime monitors fails, our Engineers respond immediately and work to restore service to the site. However, there are a few scenarios where our ability to monitor uptime may be limited:

- If you have basic authentication enabled, this will serve a [401 error](https://kinsta.com/blog/401-error/) to all unauthorized requests.
- Cloudflare’s [I’m under attack mode](https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/) has a 5-second wait time to prevent [DDoS attacks](https://kinsta.com/blog/what-is-a-ddos-attack/). This doesn’t apply to HEAD requests, which will return a [503 error](https://kinsta.com/blog/http-error-503/).
- [Reverse proxy](https://kinsta.com/blog/reverse-proxy/) sites where the primary domain isn’t redirecting to the target URL.
- Certain instances of custom caching can cause issues. For example, if you cache Kinsta’s query string HEAD request. Proxy services such as Sucuri and Cloudflare can also sometimes cause issues with caching, depending on the configuration.
- Bot blocking service: Our uptime monitor uses the `kinsta-bot` as a user-agent, so if you block it with a plugin or service (user-agent deny) this can cause our uptime monitoring to fail (this typically results in a [406](https://kinsta.com/blog/406-error/) response code).
- Blocking either our uptime monitor’s IP address(es) or origin country (Geo-block) will impact our monitoring. If you configure these features on Kinsta’s servers, it’s not an issue since we add exceptions.
- If the primary domain doesn’t resolve to the install where it’s added, or it redirects to another domain (listed in the same site’s domain list).
- When a site is in maintenance mode, it might return a [503 response](https://kinsta.com/blog/http-error-503/).
