---
url: "https://kinsta.com/changelog/kinsta-api-jul-2025/"
title: "Reset sites, manage DNS records, and more with Kinsta API"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Reset sites, manage DNS records, and more with Kinsta API"]
kinsta_last_updated: "2026-05-20T20:31:55+00:00"
sitemap_lastmod: "2026-05-20T20:31:55+00:00"
fetched_at: "2026-10-07T22:36:23Z"
sha256: "c05ee157989d554eed203ca47803a18af97d73ab5d4fafb8298c6248ab88cdac"
body_chars: 8400
extracted_with: "main article"
status: "live"
---

# Reset sites, manage DNS records, and more with Kinsta API

**Section:** Changelog > Reset sites, manage DNS records, and more with Kinsta API
**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-jul-2025/
**Kinsta last updated:** 2026-05-20T20:31:55+00:00

## On this page

- [Reset a site](#reset-a-site)
- [Fetch verification and pointing records for a domain](#fetch-verification-and-pointing-records-for-a-domain)
- [Manage DNS records programmatically](#manage-dns-records-programmatically)
- [Set PHP thread allocation](#set-php-thread-allocation)
- [Environment listings now show WordPress version](#environment-listings-now-show-wordpress-version)
- [Get a list of available regions](#get-a-list-of-available-regions)
- [More flexibility for your workflows](#more-flexibility-for-your-workflows)

---

Updated
:   May 20, 2026

![](https://kinsta.com/wp-content/uploads/2025/07/new-kinsta-api-endpoints-1024x536.png)

We’ve rolled out a new set of [API](https://api-docs.kinsta.com/) endpoints and enhancements focused on giving WordPress developers more control over site operations, DNS configuration, and resource settings.

You can now automate tasks ranging from resetting WordPress sites to managing domain verification records and DNS entries, especially at scale.

Here’s what’s new:

## Reset a site

As with the [MyKinsta](https://kinsta.com/mykinsta/) dashboard, you can now reset a WordPress site using the API’s new `/reset-site` endpoint. This action resets the site’s file system and database, restoring it to a clean WordPress installation.

This is ideal for scripted setups, provisioning templates, or quickly starting fresh during development.

To use it, send a `POST` request with the site ID and your **admin password**:

```
curl -i -X POST \
  'https://api.kinsta.com/v2/sites/{site_id}/reset-site' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  -H 'Content-Type: application/json' \
  -d '{
    "admin_password": "your-admin-password"
  }'
```

## Fetch verification and pointing records for a domain

We have also introduced the `/verification-records` endpoint, which allows you to fetch both verification and pointing records for any domain connected to a WordPress environment.

This is helpful when setting up custom domains and confirming they’re pointing correctly. It’s also helpful if you want to automate domain verification as part of [CI/CD](https://kinsta.com/blog/how-to-setup-ci-cd-pipeline/) or provisioning workflows.

Here’s an example request:

```
curl -i -X GET \
  'https://api.kinsta.com/v2/sites/environments/domains/{site_domain_id}/verification-records' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

The response includes DNS-related records like `CNAME` or `TXT` entries needed for domain validation and edge network configuration:

```
{
  "site_domain": {
    "verification_records": [
      {
        "name": "_acme-challenge.staging.example-site.io",
        "value": "staging.example-site.io.kinstavalidation.app",
        "type": "CNAME"
      }
    ],
    "pointing_records": [
      {
        "name": "staging.example-site.io",
        "value": "192.0.2.10",
        "type": "A"
      },
      {
        "name": "www",
        "value": "staging.example-site.io",
        "type": "CNAME"
      }
    ]
  }
}
```

## Manage DNS records programmatically

You can now programmatically manage domains and [DNS](https://kinsta.com/blog/what-is-dns/) records using the Kinsta API (similar to the functionality available in MyKinsta under Kinsta’s DNS).

This includes:

- [Listing domains for a company](https://api-docs.kinsta.com/api-reference/domains/get-list-of-domains-by-company-id)
- [Retrieving DNS records for a domain](https://api-docs.kinsta.com/api-reference/domains/get-list-of-domain-dns-records-by-domain-id)
- [Creating records](https://api-docs.kinsta.com/api-reference/domains/create-a-domain-dns-record), including A, AAAA, CNAME, MX, TXT, CAA, SRV, and more
- [Updating DNS records](https://api-docs.kinsta.com/api-reference/domains/update-a-domain-dns-record) by modifying resource values or TTLs
- [Deleting records](https://api-docs.kinsta.com/api-reference/domains/delete-domain-dns-record) from a domain zone

This API support mirrors what you can do in MyKinsta when managing zones linked to Kinsta’s DNS, powered by Amazon Route53.

For instance, if you want to add an A record for a subdomain, here’s how you’d do it:

```
curl -X POST \
  'https://api.kinsta.com/v2/domains/{domain_id}/dns-records' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  -H 'Content-Type: application/json' \
  -d '{
    "type": "A",
    "name": "staging.mydomain.com",
    "ttl": 3600,
    "resource_records": [
      { "value": "1.1.1.1" }
    ]
  }'
```

This is useful when provisioning domains dynamically or syncing DNS changes from your CI/CD pipeline, especially for multisite agencies or staging-heavy workflows.

For supported record types and DNS behavior, refer to [Kinsta’s DNS docs](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/#how-to-add-dns-records).

## Set PHP thread allocation

The [PHP performance add-on](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/) is one of the most used add-ons at Kinsta, as it helps sites handle more traffic and heavy processing without breaking a sweat.

It made sense to bring that control into the API, and so earlier this year, we introduced two endpoints to manage PHP performance programmatically:

- [Change PHP allocation for premium staging environments](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/change-php-allocation-settings-for-a-premium-staging-environment)
- [Change PHP allocation for live and standard staging environments](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/change-php-allocation-settings-for-a-sites-live-and-standard-staging-environments)

These endpoints originally accepted `worker_number` and `worker_memory`, but in line with our [company-wide switch](https://kinsta.com/changelog/workers-now-threads/) from “PHP workers” to “threads” (which better reflects how PHP actually works), we’ve now deprecated those old fields.

![Deprecated PHP fields](https://kinsta.com/wp-content/uploads/2025/07/image1.png)

Deprecated fields.

By the end of August 2025, only `thread_count` and `thread_memory` will be supported. If you’re using these endpoints already, now’s the time to update your requests.

Here’s what a thread configuration request looks like using the updated fields:

```
curl -i -X POST \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/change-environment-php-allocation' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  -H 'Content-Type: application/json' \
  -d '{
    "thread_count": 2,
    "thread_memory": 256
  }'
```

The above sets two PHP threads for that environment, each with 256MB of memory. This matches the same control you find in MyKinsta.

## Environment listings now show WordPress version

When managing multiple sites, it’s helpful to know exactly which version of WordPress each environment is running, especially if your team has different update schedules across clients or stages.

We’ve added a new `wordpress_version` field to these endpoints:

- [Get site environments](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-site-environments)
- [Get a list of company sites](https://api-docs.kinsta.com/api-reference/wordpress-sites/get-list-of-company-sites)

Now, when you fetch environment data, the WordPress version is included. This makes it easier to spot outdated installs or confirm updates were applied successfully without manually logging into each site.

Here’s an example of what the response looks like:

```
{
  "site": {
    "environments": [
      {
        "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
        "name": "live",
        "display_name": "Live",
        "wordpress_version": "6.3.1",
        "is_premium": false,
        "is_additional_sftp_accounts_enabled": false,
        ...
      }
    ]
  }
}
```

## Get a list of available regions

Let’s say you need to spin up new environments in a specific location. With the new `/available-regions` endpoint, you can now retrieve the list of available regions tied to your company.

This helps you programmatically confirm which data center locations are available for deployments and is useful if you’re managing multiple clients or scaling across different regions.

Here’s a sample response:

```
{
  "company": {
    "available_regions": [
      {
        "name": "Dallas US (us-south1)",
        "region": "us-south1"
      }
    ]
  }
}
```

## More flexibility for your workflows

This batch of updates gives you more programmatic control over environments, domains, DNS records, PHP performance, and regional deployments.

Whether you’re fine-tuning threads and memory, managing domains at scale, or syncing WordPress versions across sites, the Kinsta API continues to grow with modern teams in mind.

Do you need proof that it scales? We recently published a case study on how [Sod manages 400+ sites](https://kinsta.com/case-studies/sod/) with custom automation built on the Kinsta API.
