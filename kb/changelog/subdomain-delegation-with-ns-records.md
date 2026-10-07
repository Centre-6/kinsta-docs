---
url: "https://kinsta.com/changelog/subdomain-delegation-with-ns-records/"
title: "Subdomain delegation with NS records now available in Kinsta DNS"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-04-20T09:30:51"
change_signal: "2026-04-20T09:30:51"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "b5e1ba32c87c440966e6f68e33d343aa6321d1773a6ee76123dee7dd1efd6f5b"
body_chars: 2178
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Subdomain delegation with NS records now available in Kinsta DNS

**Product:** Changelog
**Source:** https://kinsta.com/changelog/subdomain-delegation-with-ns-records/
**Kinsta last updated:** 2026-04-20T09:30:51

---

We’ve added support for creating [NS records](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/#ns-record) for subdomains in [Kinsta DNS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/).

This new feature lets you delegate DNS management for specific subdomains to another DNS provider or even to a separate DNS zone within [MyKinsta](https://kinsta.com/mykinsta/), while keeping your root domain records managed in one place.

## How it works

To create an NS record, head to the **DNS section** of MyKinsta from the left sidebar and choose the domain you want to manage.

![Accessing DNS management section in the MyKinsta dashboard.](https://kinsta.com/wp-content/uploads/2025/09/dns-management.png)

Accessing DNS management section in the MyKinsta dashboard.

On the DNS management page, you’ll see your existing records and the option to add new ones by clicking the **Add a DNS record** button.

![DNS records overview in MyKinsta showing existing entries.](https://kinsta.com/wp-content/uploads/2025/09/dns-records.png)

DNS records overview in MyKinsta.

Choose **NS** from the record type tab. From there, you can enter the subdomain you want to delegate, add the authoritative nameservers, and set your preferred TTL.

For example, in the screenshot below, we delegate `shop.happyavocados.com` to Cloudflare:

![Form for adding a new NS record in MyKinsta DNS settings.](https://kinsta.com/wp-content/uploads/2025/09/add-ns-record.png)

Form for adding a new NS record in MyKinsta DNS settings.

This setup allows Cloudflare to manage all DNS records under `shop.happyavocados.com`, while the root domain and other subdomains remain in Kinsta DNS.

## Reliable hosting, simpler management

At Kinsta, we’re always working to improve your hosting experience and make it easier to manage. The addition of NS records for subdomains is one more way we’re giving you the flexibility to run complex projects without the complexity.

If you’re not already a Kinsta customer and want powerful hosting with built-in DNS management, [explore our plans](https://kinsta.com/pricing/) to see how Kinsta can help you manage everything in one place.
