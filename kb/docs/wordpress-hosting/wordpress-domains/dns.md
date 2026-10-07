---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/"
title: "Domains and DNS"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-domains"
section: []
kinsta_last_updated: "November 5, 2025"
sitemap_lastmod: "2025-11-05T18:29:56+00:00"
fetched_at: "2026-10-07T22:37:41Z"
sha256: "7dee3ac63c3e918e88a185fb4ca5f59c0134685b0cbc902f88fc976b482c1a9e"
body_chars: 34979
extracted_with: "main article"
status: "live"
---

# Domains and DNS

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/
**Kinsta last updated:** November 5, 2025

## On this page

- [The basics of how DNS works](#the-basics-of-how-dns-works)
- [What is Kinsta’s DNS?](#what-is-kinstas-dns)
- [Configure your domain to use Kinsta’s DNS](#configure-your-domain-to-use-kinstas-dns)
  - [1. Add your first domain](#1-add-your-first-domain)
  - [2. Add your domain names](#2-add-your-domain-names)
  - [3. Copy existing DNS records](#3-copy-existing-dns-records)
  - [4. Log in to your domain’s registrar](#4-log-in-to-your-domains-registrar)
  - [5. Update your nameservers](#5-update-your-nameservers)
- [Import DNS records](#import-dns-records)
- [Automatically scan for DNS records](#automatically-scan-for-dns-records)
- [Manually add DNS records](#manually-add-dns-records)
  - [A record](#a-record)
  - [AAAA record](#aaaa-record)
  - [CNAME record](#cname-record)
  - [CAA record](#caa-record)
    - [CAA flag](#caa-flag)
    - [CAA tag](#caa-tag)
    - [CAA value](#caa-value)
    - [Google CAA records](#google-caa-records)
  - [MX record](#mx-record)
    - [Add Gmail MX records on a new domain](#add-gmail-mx-records-on-a-new-domain)
    - [Add Gmail MX records on an existing domain](#add-gmail-mx-records-on-an-existing-domain)
  - [TXT record](#txt-record)
  - [SPF record](#spf-record)
  - [DKIM record](#dkim-record)
  - [DMARC record](#dmarc-record)
  - [SRV record](#srv-record)
  - [NS record](#ns-record)
- [Email authentication](#email-authentication)
  - [How to check if you are using an SPF TXT record](#how-to-check-if-you-are-using-an-spf-txt-record)
  - [How to add an SPF record for MailChannels](#how-to-add-an-spf-record-for-mailchannels)
  - [How to merge an SPF record](#how-to-merge-an-spf-record)
  - [How to add a DMARC record for MailChannels](#how-to-add-a-dmarc-record-for-mailchannels)
- [Add linked WordPress site](#add-linked-wordpress-site)
- [Filter domains](#filter-domains)

---

When you host your WordPress website with Kinsta, you can also use Kinsta’s DNS service to manage your DNS records, including [SPF and DKIM](#email-authentication) records for MailChannels’ service, which we use for transactional email. To take advantage of Kinsta’s DNS service, you must have access to update the name servers on your domain’s registrar. We recommend contacting your DNS provider if you don’t have access to the domain registrar.

This is optional (you can manage your DNS records anywhere you like), but if you’d like to take advantage of our premium DNS service and manage your DNS with Kinsta, follow the instructions below.

## The basics of how DNS works

When someone types in your domain (yourwebsite.com) in their browser, their computer uses the DNS system to look up which name servers it should contact to get DNS information. It will return something like the following:

- ns-155.awsdns-22.com
- ns-326-awsdns-15.net
- ns-1352-awsdns-29.org
- ns-1536-awsdns-08.co-uk

The visitor’s computer then contacts one of those [name servers](https://kinsta.com/blog/what-is-a-nameserver/) to look up the IP address for the domain by checking for the DNS **A record**, which contains the IP address of the server where it’s hosted. In this case, your domain’s A record is pointed to Kinsta’s IP. The visitor’s computer then connects to Kinsta’s IP to load yourwebsite.com.

## What is Kinsta’s DNS?

All [Managed WordPress Hosting plans](https://kinsta.com/wordpress-hosting/) come with Kinsta’s DNS, a premium Anycast DNS service powered by Amazon Route53. Route53 consistently ranks among the fastest DNS services in the world, and it even supports latency and geolocation-based routing to ensure quick response times.

Unlike other WordPress hosts that charge extra for premium DNS, **all Kinsta customers with a Managed WordPress plan can take advantage of Kinsta’s DNS at no additional cost**. The number of domains you can add to Kinsta’s DNS is equal to the number of sites [your plan allows](https://kinsta.com/pricing/).

## Configure your domain to use Kinsta’s DNS

### 1. Add your first domain

In [MyKinsta](https://my.kinsta.com/), click **DNS management** and then click **Add your first domain**. If you already have a domain in Kinsta’s DNS, click **Add domain** instead.

![Add your domain to DNS management in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-dns-management-add-domain.png)

Add your domain to DNS management in MyKinsta.

### 2. Add your domain names

In the **Add domain** modal/pop-up, enter your **Domain name**. If you want to link a WordPress site, select the site to link. When you link a WordPress site to a DNS zone, it shows the DNS zone on the **Domains** page so you can easily access it and gives **Site Administrators** access to manage the DNS records for the site within **DNS management**.

If you’re using Google Workspace for email, you can check the **Add Gmail MX Records** option to add the required MX records automatically. **Note:** This only adds the MX records, and you may still need to add additional CNAME and TXT verification records for Google Workspace later on.

If you have more than one domain to add, click **Add new domain** again and enter your next domain name.

After entering your domain(s), click **Add domains**.

![Enter your domain and linked WordPress site in the Add domain modal and click Add domains to continue.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-add-domain-1-1024x499.png)

Enter your domain and linked WordPress site in the Add domain modal and click Add domains to continue.

### 3. Copy existing DNS records

Before changing your domain’s nameservers, make sure to copy over any existing DNS records. Log in to your current DNS provider (where your nameservers are currently pointed). This might be your domain registrar or another DNS provider.

Copy your site’s DNS records from your current provider to Kinsta DNS. You can do this in one of three ways:

- [Import your DNS records](#import-dns-records) by uploading a zone file (`.txt`) from your domain registrar.
- [Automatically scan your domain’s existing DNS records](#automatically-scan-for-dns-records) to detect commonly used record types and names. Be sure to review these carefully, and manually add any missing records before changing nameservers.
- [Manually add DNS records](#manually-add-dns-records) one by one.

### 4. Log in to your domain’s registrar

Log in to your domain registrar’s management panel. This may not be the same place you currently manage DNS. Your DNS is managed wherever your domain’s nameservers are pointed, but nameservers themselves are always controlled at your domain registrar. Since you need to update the nameservers your domain points to, you must log in to where your domain is registered.

### 5. Update your nameservers

1. Within your domain’s registrar, navigate to the section where nameservers are managed (commonly labeled DNS, Manage Zones, Modify DNS Servers, Custom DNS, or similar). If you can’t find it, check your registrar’s documentation or contact their support team. Depending on your registrar, you may need to remove the existing nameservers first.
2. Add the four nameservers shown in MyKinsta, and make sure they are the only ones listed.
   ![Nameservers in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-dns-nameservers.png)

   Nameservers in MyKinsta.

After updating the name servers at your domain registrar, the changes may take 24-48 hours to propagate across the Internet.

## Import DNS records

Using a `.txt` file, you can import your DNS records for your root domain or subdomains into MyKinsta from your DNS provider.

1. Log in to your DNS provider and download or export your DNS records. For example, in Cloudflare, you can export your DNS records within **DNS** > **Records** > **Import and Export** > **Export**.
2. In MyKinsta, go to **DNS management**, click the domain you want to import DNS records for, and within **Upload zone file**, click **Upload file**. If you’re uploading a zone file for a subdomain, within **DNS records**, click **Upload zone file**.
   ![Upload a .txt file to MyKinsta.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-dns-upload-zone-file.png)

   Upload a .txt file to MyKinsta.
3. Drag and drop the `.txt` file, or **Browse** to the file and click **Open**.
   ![Drag and drop or browse to your .txt file to upload it.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-dns-upload-file.png)

   Drag and drop or browse to your .txt file to upload it.
4. Review the DNS records by comparing these to the records within your DNS provider to ensure they are all correct, deselect any records you do not want to import, and click **Insert DNS records**. NS records are disabled by default, as these are only applicable when you want to delegate a subdomain either to an external DNS provider or to a separate DNS zone within MyKinsta. 
   ![Review and insert the uploaded DNS records.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-dns-insert-uploaded-records.png)

   Review and insert the uploaded DNS records.
5. [Manually add](#manually-add-dns-records) any missing DNS records before changing nameservers.

## Automatically scan for DNS records

You can automatically scan your domain or subdomain’s existing DNS records to identify the most common record types and names.

1. In MyKinsta, go to **DNS management**, click the domain you want to scan DNS records for, and within **Automatic scan**, click **Start scan**. If you want to scan DNS records for a subdomain, within **DNS records**, click **Automatic scan**, enter your subdomain, for example, `shop`, and click **Scan**.
   ![Automatically scan your domain for DNS records.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-dns-start-scan.png)

   Automatically scan your domain for DNS records.
2. Review the DNS records by comparing them to the records within your DNS provider to ensure they are all correct. Deselect any records you do not want to import, and click Insert DNS records. NS records are disabled by default, as they are only applicable when you want to delegate a subdomain either to an external DNS provider or to a separate DNS zone within MyKinsta.
   ![Review and insert your DNS records.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-dns-insert-scan-records.png)

   Review and insert your DNS records.
3. [Manually add](#manually-add-dns-records) any missing DNS records before changing nameservers.

## Manually add DNS records

Kinsta’s DNS supports various DNS record types, including A records, CNAME records, MX records, TXT records, and more. The following shows all supported DNS records and how to configure them in Kinsta’s DNS.

Within MyKinsta, click **DNS management**, click on the domain you want to manage, and within **Add a DNS record**, click **Add record**. If you already have DNS records, click **Add a DNS record**.

![Manually add DNS records in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-dns-manually-add.png)

Manually add DNS records in MyKinsta.

After you add or change the details of a DNS record, click **Add DNS record** or **Change DNS record**.

### A record

An A record maps a domain name to the IPV4 address of a server and is required for a website to be served via a domain name. For specific information on adding and pointing your domain to Kinsta, please refer to our in-depth guide on [Domains and DNS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/).

- **Hostname:** Specify a subdomain if you’re configuring a subdomain. If you are setting up an A record for your root domain, leave the **Hostname** field empty.
- **IPV4 Address:** Enter your [**Site IP Address** (IPv4](https://kinsta.com/docs/wordpress-hosting/site-management/ip-addresses/)).
- **TTL (Time to Live):** We recommend using the default setting of 1 hour.
- **Add DNS record with and without www:** Check this box if you want to automatically add the CNAME record for your www domain at the same time.

![Add an A record in Kinsta's DNS.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-dns-a-record.png)

Add an A record in Kinsta’s DNS.

### AAAA record

An AAAA record maps a domain name to the IPV6 address of a server that supports an IPV6 address.

There may be a couple of situations where you may want to add an AAAA record in Kinsta’s DNS:

- If you have a subdomain you’d like to point to another server that does support IPV6.
- If you’re using Kinsta’s DNS to manage your main domain’s DNS, but you’re pointing the main domain to another server that supports IPV6.

You won’t be able to use this for your site hosted at Kinsta, as we only support IPV4 addresses.

- **Hostname:** Specify the subdomain you’re configuring. If you are setting up an AAAA record for your root domain, leave the **Hostname** field empty.
- **IPV6 Address:** Specify the IPV6 address of the server.
- **TTL (Time to Live):** We recommend using the default setting of 1 hour.
- **Add DNS record with and without www:** Only check this box if you’re creating the AAAA record for your root domain and want to automatically add the CNAME record for your www domain at the same time.

![Add an AAAA record in Kinsta's DNS.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-dns-aaaa-record.png)

Add an AAAA record in Kinsta’s DNS.

### CNAME record

A CNAME record handles the mapping of a domain name to another hostname. CNAMEs are commonly used to map a www domain to a non-www domain (e.g. www.kinstalife.com to kinstalife.com). If you selected the **Add DNS record with and without www** box when adding an A or AAAA record, the CNAME for your www domain has already been added. For specific information on adding and pointing your domain to Kinsta, please refer to our in-depth guide on [Domains and DNS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/).

- **Hostname:** Specify the hostname of your subdomain.
- **Points To:** Specify the hostname you’d like the CNAME to resolve to.
- **TTL (Time to Live):** We recommend using the default setting of 1 hour.

![Add a CNAME record in Kinsta's DNS.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-dns-cname-record.png)

Add a CNAME record in Kinsta’s DNS.

### CAA record

A CAA record is an optional DNS record that lets you specify which certificate authorities (CAs) are allowed to issue SSL certificates for your domain. If a domain has no CAA records, any CA can generate an SSL certificate for it if requested. Setting up a CAA record provides you with an additional layer of security to prevent untrusted CAs from issuing SSL certificates for your domain. The CAA record follows the format below:

Copy

```
your-domain.com CAA <flags> <tag> <value>
```

Let’s take a closer look at each element of the CAA record.

#### CAA flag

A CAA flag specifies whether a CA is allowed to use the information specified in a CAA record. The flag has two values – `0` or `1`

- If the CAA flag is set to `0`, a CA can use the information within the CAA record even if it doesn’t recognize the CAA tag.
- If the CAA flag is set to `1`, a CA is not allowed to use the CAA record unless it recognizes the CAA tag.

#### CAA tag

A CAA tag specifies that allowed behavior for authorized CAs when issuing SSL certificates. The tag is generally one of three values — `issue`, `issuewild`, `iodef` — but custom values specific to certain CAs are supported as well.

- The `issue` tag allows a CA to generate a non-wildcard SSL certificate.
- The `issuewild` tag allows a CA to generate a wildcard SSL certificate.
- The `iodef` tag allows you to receive email alerts if an invalid SSL certificate request is made.

#### CAA value

A CAA value specifies the domain name of a certificate authority (CA). For example, the CAA value for Let’s Encrypt (a popular CA) would be `letsencrypt.org`. If the CAA value is set to `;`, no CA is allowed to issue an SSL certificate for the domain. To add a CAA record in Kinsta’s DNS, you’ll need the hostname, CAA value (the domain name of the CA), CAA flag, and CAA tag. In this example, let’s add the CAA record below.

Copy

```
kinstalife.com. CAA 0 issue “letsencrypt.org”
```

We can add this CAA record in Kinsta’s DNS like so:

![Add a CAA record in Kinsta's DNS.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-dns-caa-record.png)

Add a CAA record in Kinsta’s DNS.

#### Google CAA records

If you use Google Cloud or Google-managed SSL certificates, you must add the following CAA records to your DNS entries to allow Google Trust Services (pki.goog) to issue both standard and wildcard SSL/TLS certificates for your domain, replacing `example.com` with your domain:

Copy

```
example.com. IN CAA 0 issue "pki.goog"
example.com. IN CAA 0 issuewild "pki.goog"
```

### MX record

MX Records are used for email routing, and the specific records will vary based on what your email provider gives you.

- **Hostname:** Specify the hostname of your email address.
- **Points To:** Specify the hostname for your email provider.
- **Priority:** Specify the priority number for the MX record.
- **TTL (Time to Live):** We recommend using the default setting of 1 hour.

For this example, let’s configure MX records for MX Route, a popular email hosting service. Below are the MX records provided by MX Route:

1. echo.mxrouting.net (Priority 10)
2. echo-relay.mxrouting.net (Priority 20)

Add the first MX record like this:

![First MX record for MX Route.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-dns-mx-email-record.png)

First MX record for MX Route.

Next, the second MX record can be added like so (notice the different **Points To** hostname and **Priority**):

![Second MX record for MX Route.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-dns-mx-email-record-2.png)

Second MX record for MX Route.

#### Add Gmail MX records on a new domain

If you’re using [Google Workspace](https://kinsta.com/blog/google-workspace/) for your email service, we make it super easy to add the required MX records. When you’re adding a domain in Kinsta’s DNS, check the **Add Gmail MX Records** box, and the necessary MX records will automatically be added.

![Select the option to Add Gmail MX records in the Add domain modal.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-dna-add-domain-gmail-records-1024x501.png)

Select the option to Add Gmail MX records in the Add domain modal.

#### Add Gmail MX records on an existing domain

Already have a domain added and set up in Kinsta’s DNS? No problem. Click **Add Gmail MX records**.

![Add Gmail MX records on an existing domain in DNS management.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-dna-add-domain-gmail-records-exisiting.png)

Add Gmail MX records on an existing domain in DNS management.

Next, click **Add 5 Records**, and you’re all set!

![Add Gmail MX records in Kinsta DNS.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-dna-add-domain-gmail-records-existing-5-1024x643.png)

Add Gmail MX records in Kinsta DNS.

### TXT record

TXT records are used for a variety of things. Typically they are used for verification. For example, you can [verify your domain name](https://support.google.com/a/answer/2716802?hl=en) with Google Workspace using a TXT record.

- **Hostname:** Specify the hostname for your TXT record.
- **TTL (Time to Live):** We recommend using the default setting of 1 hour.
- **Content:** The body of the TXT record.

Let’s say we need to add the TXT record below to verify the domain kinstalife.com with Google Workspace.

Copy

```
google-site-verification=rXOxyZounnZasA8Z7oaD3c14JdjS9aKSWvsR1EbUSIQ
```

Here’s what that TXT record would look like in Kinsta’s DNS:

![Add a TXT record in Kinsta's DNS.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-dns-txt-record.png)

Add a TXT record in Kinsta’s DNS.

### SPF record

An SPF (Sender Policy Framework) record is a type of DNS record used to prevent email spoofing. It tells mail servers which IP addresses or services are authorized to send email on behalf of your domain. When a receiving mail server checks an incoming message, it looks up the SPF record for the sending domain and verifies whether the sender is allowed. Here’s an example of what an SPF record may look like:

Copy

```
v=spf1 include:servers.mcsv.net ?all
```

When you send an email, the receiving mail server checks the domain in the “envelope from” address and looks up that domain’s DNS records. If an SPF record exists, it contains a list of servers or services that are authorized to send email for the domain. The mail server then compares the sending server’s IP address against this list. If there’s a match, the message passes SPF authentication; if not, the email may be flagged as suspicious or rejected, depending on the domain’s SPF policy.

Third-party email providers and transaction email services might have you set up an SPF record for email authentication purposes. However, SPF records are now obsolete ([RFC 7208](https://tools.ietf.org/html/rfc7208#section-3.1)) and must be entered as TXT records instead.

- **Hostname:** Specify the hostname for the SPF record.
- **TTL (Time to Live):** We recommend using the default setting of 1 hour.
- **Content:** The body of the SPF record (begins with v=spf1).

If you want more details on how to add an SPF record for MailChannels (the service used here at Kinsta to send [transactional emails](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/email/)), see the [email authentication](#email-authentication) steps below.

![Add an SPF record in Kinsta's DNS.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-dns-spf-record.png)

Add an SPF record in Kinsta’s DNS.

### DKIM record

DKIM (DomainKeys Identified Mail) is an email authentication method that helps verify that an email hasn’t been altered after it was sent. It works by adding a cryptographic signature to specific email headers (such as From, To, Date, and Subject). When the receiving mail server gets the email, it uses the sender’s public DKIM key (published in DNS) to check the signature and confirm the message is authentic. The signature itself is stored in a DKIM-Signature header, which includes details such as the sending domain and where to find the public key.

If you’re using [Kinsta’s Transactional Email](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/email/) service to send emails from your WordPress site, you don’t need to configure a DKIM record yourself. Through our MailChannels integration, DKIM is enabled automatically on the server, no manual DNS setup required.

In Kinsta DNS, there isn’t a special record type for DKIM. Instead, DKIM is added using either a TXT record or a CNAME record, depending on the email provider. For example, here’s how you might add a DKIM record for Mailgun.

Keep in mind that TXT records are limited to 255 characters by the DNS protocol (not by Kinsta). If your DKIM record is longer than 255 characters, you’ll need to split it into multiple quoted strings.

![Add a DKIM record with multiple strings in Kinsta's DNS.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-dns-dkim-record.png)

Add a DKIM record with multiple strings in Kinsta’s DNS.

Depending on the method or tool used (the `dig` command or a lookup tool), checking DNS may show the record as a single entry:

Copy

```
"v=DKIM1;  k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUkIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3D"
```

or it may show the record with the double quotes between the strings:

Copy

```
"v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUkIGfMA0GCSqGSIb3DQEBAQUMIGfMA0" "GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3DQEBAQUMIGfMA0GCSqGSIb3D"
```

### DMARC record

Some email providers now enforce stricter authentication requirements for bulk email senders, requiring Domain-based Message Authentication, Reporting, and Conformance (DMARC) alignment. Emails that don’t meet these requirements may be delayed or rejected. At Kinsta, outbound emails sent through the transactional email service do not currently support DMARC alignment. If you require DMARC compliance, we recommend configuring a third-party SMTP service. Many providers offer free plans. For setup guides, see:

- [How to Use a Free SMTP Server for WordPress Emails (Including Gmail SMTP Server)](https://kinsta.com/blog/free-smtp-server/)
- [How to Use the Gmail SMTP Server to Send Emails for Free](https://kinsta.com/blog/gmail-smtp-server/)

DMARC builds on SPF and DKIM to verify that an email truly originates from the domain listed in the header From address (for example, `[email protected]`). The receiving mail server then checks for a DMARC record published at `_dmarc.sitename.com`. The key mechanism in DMARC is alignment, which means the domain in the header From address must match (or closely align with) the domain used in the DKIM signature or the SPF envelope From address. Alignment ensures that unauthorized servers cannot send messages on behalf of your domain.

The policy (p=) defined in your DMARC record tells receiving mail servers how to handle messages that fail DMARC checks. You can choose from the following options:

- `p=none`: Monitoring only. No action is taken, but reports are generated.
- `p=quarantine`: Messages that fail are treated as suspicious (for example, delivered to the spam or junk folder).
- `p=reject`: Messages that fail are rejected and not delivered at all.

To use [Kinsta’s Transactional Email](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/email/) service you must either remove your DKIM record or configure a DMARC record with the policy as `p=none`.

To configure a DMARC record, add a TXT record with the required policy at your DNS provider, for example:

Copy

```
v=DMARC1;p=none
```

If you’re using Kinsta’s DNS, go to your domain’s DNS and click **Add a DNS Record**.

![Add a DNS record in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-dns-add-dns-record-1.png)

Add a DNS record in MyKinsta.

Select the **TXT** record option, in the **Hostname**, enter `_dmarc`, and paste `v=DMARC1;p=none` into the **Content** area. If you’re using a subdomain, be sure to add your subdomain in the **Hostname** field. Click **Add DNS Record** to save the DMARC record.

![Add DMARC TXT record.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-dns-dmarc-record-1.png)

Add DMARC TXT record.

If you’re not using Kinsta’s DNS, you can update the DMARC TXT record where you manage your domain’s DNS. If you’re unsure about how to edit DNS records there, we recommend contacting your DNS provider.

### SRV record

An SRV (service) record is used when a service needs additional information, such as a port number. These are most commonly used with SIP configurations, VOIP, and IM.

- **Hostname:** Prepend the hostname for the SRV record in this format: `_service._protocol`  
  (the hostname is automatically entered, so you only need to add the service and protocol)
- **Target:** The target server for the SRV record.
- **Priority:** The priority level of the target host.
- **Weight:** The weight relative to other SRV records with the same priority number.
- **Port:** The network port for the service.
- **TTL (Time to Live):** We recommend using the default setting of 1 hour.

In this example, we’ll add the [SRV record below for Office 365](https://support.microsoft.com/en-us/help/2566790/troubleshooting-skype-for-business-online-dns-configuration-issues-in) Skype for Business to Kinsta’s DNS.

- Service: _sip
- Protocol: _tls
- Target: sipdir.online.lync.com
- Priority: 100
- Weight: 1
- Port: 443
- TTL: 1 hour

![Add an SRV record in Kinsta's DNS.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-dns-srv-record.png)

Add an SRV record in Kinsta’s DNS.

### NS record

An NS (Name Server) record specifies which name servers are authoritative for a domain or subdomain. In MyKinsta, NS records can be used to delegate a subdomain either to an external DNS provider or to a separate DNS zone within MyKinsta. For example, if you are an agency managing the root domain in MyKinsta, you may want to delegate a subdomain as its own DNS zone. This allows a site administrator to manage DNS records for that subdomain without having access to the root domain.

NS records tell the Internet which servers are responsible for handling DNS queries for the subdomain. When configuring NS records for a subdomain, we recommend adding at least two NS records to ensure high availability and improved performance. This provides a backup if one nameserver becomes unavailable and allows DNS queries to be resolved more efficiently.

- **Subdomain:**Specify which subdomain you want to point to a different DNS service.
- **Value:** Specify the name server you want to point the subdomain to.

In our example, we want Cloudflare to manage DNS for our store at `shop.kinstaexample.com`, so we would add the NS record as follows:

![Add an NS record in Kinsta's DNS.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-dns-ns-record.png)

Add an NS record in Kinsta’s DNS.

This delegates DNS control of only the `shop.kinstaexample.com` subdomain to Cloudflare, while the root domain (`kinstaexample.com`) and any other subdomains can still be managed in MyKinsta.

## Email authentication

To help prevent email spoofing or your legitimate email messages being sent to a Spam/Junk folder, setting up email authentication for your domain is recommended. The most common forms of email authentication DNS records are SPF and DKIM, and can be added to DNS in MyKinsta.

At Kinsta, we utilize MailChannels for [transactional email](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/email/) delivery. This means outgoing emails from your WordPress site are sent through MailChannels’ service. There are two different from addresses when you send emails:

- **Header from:** This is used for identifying the sender to the recipient. It is visible to the recipient and appears in the “From” field of the email message. The header from address is derived from WordPress or a WordPress plugin; by default, it is the site administration email within WordPress Admin > **Settings** > **General** > **Email Address**.
- **Envelope from:** This is used for routing and handling delivery errors. With Kinsta’s transactional email provided by MailChannels, this is set to [[email protected]](https://kinsta.com/cdn-cgi/l/email-protection#e2918b96878c838f87a2918b96878c838f87cc898b8c9196838f838b8e918790948b8187cc818d8f) and cannot be changed. It is part of the email’s metadata, and typically, it is not visible to the email recipient; however, some mail software may show both the header from and envelope from addresses.

If you’re using an SPF TXT record to authorize hostnames for email services on your domain, you’ll need to include MailChannels to ensure reliable email deliverability. To do this, [merge MailChannels](#how-to-merge-an-spf-record) into your existing SPF record. If no SPF record exists, simply [add it to your DNS records](#how-to-add-an-spf-record-for-mailchannels).

### How to check if you are using an SPF TXT record

If you’re using Kinsta’s DNS, log in to [MyKinsta](https://my.kinsta.com), click **DNS management**, and select your site’s domain name. In the **TYPE** column, look for a TXT record. If the value of the TXT record starts with **v=spf1**, it is an SPF TXT record. If you’re not using Kinsta’s DNS, refer to where you manage your domain’s DNS records.

![An SPF TXT record in Kinsta's DNS.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-dns-vspf-1.png)

An SPF TXT record in Kinsta’s DNS.

Alternatively, you can use a service like [whatsmydns.net](https://www.whatsmydns.net/) to check if your domain has SPF TXT records. To do this, input your domain name, select the **TXT** option, and click **Search** to get a list of TXT records for your domain.

![Use whatsmydns.net to check for SPF TXT records.](https://kinsta.com/wp-content/uploads/2020/07/whatsmydns-spf-txt-record.jpg)

Use whatsmydns.net to check for SPF TXT records.

You can only have one SPF record for a domain. If an SPF record already exists, you’ll need to [merge it](#how-to-merge-an-spf-record) to include MailChannels. If no SPF record exists, you’ll need to [create one specifically for MailChannels](#how-to-add-an-spf-record-for-mailchannels).

### How to add an SPF record for MailChannels

To configure an SPF record for MailChannels, add the TXT record below at your DNS provider:

Copy

```
v=spf1 a mx include:relay.kinstamailservice.com ~all
```

If you’re using Kinsta’s DNS, go to your domain’s DNS and click **Add a DNS Record**.

![Add a DNS record in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-dns-add-dns-record-1.png)

Add a DNS record in MyKinsta.

Select the **TXT** record option and paste `v=spf1 a mx include:relay.kinstamailservice.com ~all` into the **Content** area. If you’re using a subdomain, be sure to add your subdomain in the **Hostname** field. Click **Add DNS Record** to save the SPF record.

![Add SPF TXT record for MailChannels.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-dns-spf-mailchannels.png)

Add SPF TXT record for MailChannels.

If you’re not using Kinsta’s DNS, you can update the SPF TXT record where you manage your domain’s DNS. If you’re unsure about how to edit DNS records there, we recommend contacting your DNS provider.

### How to merge an SPF record

A domain can only have one SPF record, so if you have an existing record, you’ll need to merge the MailChannels record to use Kinsta’s transactional email. To merge an SPF DNS record, you combine the rules from multiple SPF configurations into a single valid SPF record, ensuring no mechanisms are repeated.

For example, if your existing SPF record is `v=spf1 include:example.com ~all`. Kinsta’s SPF record should be configured as `v=spf1 a mx include:relay.kinstamailservice.com ~all`. To merge these records, you need to add `a mx include:relay.kinstamailservice.com`. The merged SPF record is therefore `v=spf1 include:example.com a mx include:relay.kinstamailservice.com ~all`.

Your SPF record may already include `a mx`, for example, `v=spf1 a mx include:example.com ~all` in this case, all you need to add is `include:relay.kinstamailservice.com`. The merged SPF record is therefore `v=spf1 a mx include:example.com include:relay.kinstamailservice.com ~all`.

### How to add a DMARC record for MailChannels

To configure a DMARC record for MailChannels, add the TXT record below at your DNS provider:

Copy

```
v=DMARC1;p=none
```

If you’re using Kinsta’s DNS, go to your domain’s DNS and click **Add a DNS Record**.

![Add a DNS record in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-dns-add-dns-record-1.png)

Add a DNS record in MyKinsta.

Select the **TXT** record option, in the **Hostname**, enter `_dmarc`, and paste `v=DMARC1;p=none` into the **Content** area. If you’re using a subdomain, be sure to add your subdomain in the **Hostname** field. Click **Add DNS Record** to save the DMARC record.

![Add DMARC TXT record for MailChannels.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-dns-dmarc-record-1.png)

Add DMARC TXT record for MailChannels.

If you’re not using Kinsta’s DNS, you can update the DMARC TXT record where you manage your domain’s DNS. If you’re unsure about how to edit DNS records there, we recommend contacting your DNS provider.

## Add linked WordPress site

Once you’ve set up your DNS zone, you can link a WordPress site to it. This gives **Site Administrators** access to manage the DNS records for the site. Within **Linked WordPress site**, click **Add site**, choose the WordPress site you want to link to, and click **Add linked site**.

![WordPress sites linked to your DNS zone.](https://kinsta.com/wp-content/uploads/2024/01/dns-linked-wordpress-site-1024x151.png)

WordPress sites linked to your DNS zone.

Click **Change** to change which site the DNS zone is linked to. Click **Remove** to remove the site from the DNS zone.

## Filter domains

Within Kinsta’s DNS you can filter your domains by **Active** or **Inactive**. Click **All statuses** and choose the required option.

![Filter your domains within Kinsta's DNS.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-dns-filter.png)

Filter your domains within Kinsta’s DNS.
