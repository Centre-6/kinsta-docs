---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-domains/google-mx-records/"
title: "Domains and DNS - Google MX Records"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-domains"
section: []
kinsta_last_updated: "August 13, 2024"
sitemap_lastmod: "2024-08-13T09:28:18+00:00"
fetched_at: "2026-10-07T22:38:10Z"
sha256: "59fc158b40185713f30d76a18b5f61fe94621e20c9ac8608d015db58a4a67010"
body_chars: 3416
extracted_with: "main article"
status: "live"
---

# Domains and DNS - Google MX Records

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-domains/google-mx-records/
**Kinsta last updated:** August 13, 2024

## On this page

- [Set up Google MX records for Google Workspace (G Suite)](#set-up-google-mx-records-for-google-workspace-g-suite)
  - [Google MX records](#google-mx-records)
  - [How to add Gmail MX records to a new domain](#how-to-add-gmail-mx-records-to-a-new-domain)
  - [How to add Gmail MX records to an existing domain](#how-to-add-gmail-mx-records-to-an-existing-domain)
- [Email authentication](#email-authentication)

---

## Set up Google MX records for Google Workspace (G Suite)

[Google Workspace](https://kinsta.com/blog/google-workspace/) (formerly G Suite) is designed for businesses that need their email routed through Gmail. It also includes other software with premium storage, such as Google Drive, Google Docs (check out on our blog how you can [import Google Docs into WordPress](https://kinsta.com/blog/google-docs-to-wordpress/)), etc. We’re big fans of Google Workspace and even use it ourselves.

For your business email to work with Google Workspace, Google MX records have to be set up and configured for your domain. If you use Kinsta’s DNS, we’ve made adding your Google MX records as easy as possible

### Google MX records

Google MX records are as follows:

- aspmx.l.google.com / priority 1
- alt1.aspmx.l.google.com / priority 5
- alt2.aspmx.l.google.com / priority 5
- alt3.aspmx.l.google.com / priority 10
- alt4.aspmx.l.google.com / priority 10

For TTL, use 3600 seconds (1 hour).

We’ve completely streamlined this process, so now **you can add your Gmail MX records with a few clicks in Kinsta’s DNS**. No more copy/pasting DNS records.

- [How to Add Gmail MX Records to a New Domain](#new-domain)
- [How to Add Gmail MX Records to an Existing Domain](#existing-domain)

### How to add Gmail MX records to a new domain

If you’re adding your domain for the first time in Kinsta’s DNS, select the **Add Gmail MX records** checkbox, and you’re done! The 5 Gmail MX records are added along with your domain.

If you want to link a WordPress site, select the site to link within **Link WordPress site**. When you link a WordPress site to a DNS zone, it shows the DNS zone on the **Domains** page so you can easily access it, and it gives **Site Administrators** access to manage the site’s DNS records within **DNS management**.

![Add Gmail MX records to a new domain.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-dns-add-gmail-mx-records.png)

Add Gmail MX records to a new domain.

### How to add Gmail MX records to an existing domain

Already have a domain added and set up in Kinsta’s DNS? No problem. Edit your domain’s DNS and click **Add Gmail MX records** at the top of the page.

![Add Gmail MX records to an existing domain in Kinsta's DNS.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-dna-add-domain-gmail-records-exisiting.png)

Add Gmail MX records to an existing domain in Kinsta’s DNS.

In the modal/pop-up that appears, click on **Add 5 records**, and you’re done.

![Add Gmail MX records in KinstaDNS.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-dna-add-domain-gmail-records-existing-5-1024x643.png)

Add Gmail MX records in KinstaDNS.

Here is an example of what they will look like after they are added.

![Google MX records for Google Workspace.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-dna-add-domain-gmail-records-example.png)

Google MX records for Google Workspace.

## Email authentication

To help prevent email spoofing or your legitimate email messages being sent to a Spam/Junk folder, setting up email authentication for your domain is recommended. The two most common forms of email authentication DNS records are [SPF](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/#spf-record) and [DKIM](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/#dkim-record), and can be added to DNS in MyKinsta.
