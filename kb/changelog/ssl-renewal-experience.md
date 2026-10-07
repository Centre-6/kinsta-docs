---
url: "https://kinsta.com/changelog/ssl-renewal-experience/"
title: "Introducing a Pain-Free SSL Renewal Experience"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2023-11-24T13:34:42"
change_signal: "2023-11-24T13:34:42"
fetched_at: "2026-10-07T22:58:23Z"
sha256: "621273910d339938c1fb3b4e06495e50ff69899037a28939f2005a3021c9285b"
body_chars: 6214
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Introducing a Pain-Free SSL Renewal Experience

**Product:** Changelog
**Source:** https://kinsta.com/changelog/ssl-renewal-experience/
**Kinsta last updated:** 2023-11-24T13:34:42

## On this page

- [Kinsta’s Improved SSL Renewal Process](#kinstas-improved-ssl-renewal-process)
- [Why Use Kinsta’s SSL Certificates?](#why-use-kinstas-ssl-certificates)
- [Simplifying Site Management at Kinsta](#simplifying-site-management-at-kinsta)

---

There are always loads of details to keep track of when managing and maintaining a website. Necessary tasks like SSL renewals never seem to come at a convenient time, and following up on them can be time-consuming and frustrating, especially when you’re required to drop what you’re doing to make changes to your site or its files.

That’s why we’re excited to announce a major improvement to our [SSL certificate renewal process](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/#renew-free-cloudflare-ssl-certificate).

Most recently, Kinsta customers have been required to add a new DNS record to their domain each year before their wildcard SSL certificates can be renewed. While this process was necessary, it could also be inconvenient and time-intensive.

But we’re pleased to say that we’ve lifted this requirement for most Kinsta customers.

Now, SSL certificates issued through [Kinsta’s Cloudflare integration](https://kinsta.com/cloudflare-integration/) will be **renewed automatically** in most cases, without the need for you to repeatedly add new records or make changes to your DNS setup. This means a faster renewal process that’s more streamlined for our customers, yet still just as secure as before.

Let’s take a look at why we’ve introduced this change and how the renewal process now works.

## Kinsta’s Improved SSL Renewal Process

Due to an industry-wide [shift in requirements for SSL certificate renewal](https://www.ssls.com/blog/upcoming-changes-to-http-domain-control-validation/), renewal processes are changing for hosting providers across the web. Although Kinsta supports both [wildcard](https://kinsta.com/blog/wildcard-ssl/) and [non-wildcard domains](https://kinsta.com/blog/types-of-ssl-certificates/#types-of-ssl-certificates), this change will mostly affect how **wildcard domains** are treated during renewal.

Luckily, we’ve worked to turn this change into a positive for our users rather than a negative by introducing automatic renewal.

Depending on whether your domain utilizes Kinsta’s DNS or third-party nameservers, the renewal process could look a little different. Here’s an overview of the updated SSL renewal process for new and existing domains at Kinsta:

- **Kinsta’s DNS:** If your website uses [Kinsta’s DNS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/#what-is-kinstas-dns) along with one of our [free Cloudflare SSL certificates](https://kinsta.com/blog/free-ssl-certificate/), you’re already set up for automatic renewal! You won’t need to take any action to renew your certificate for as long as your domain uses Kinsta’s DNS.
- **Custom SSL:** Kinsta supports [custom SSL certificates](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/#step-2-install-custom-ssl-certificate) as well. However, to renew an SSL certificate purchased through a third-party service, you’ll need to work outside of Kinsta. In most cases, this means referring back to your SSL provider and their documentation.
- **Third-Party Nameservers:** If you use a third-party DNS server alongside Kinsta’s Cloudflare SSL, you’ll need to add a one-time `CNAME` record that allows us to update the `TXT` record when needed for SSL validation. After this, your domain’s SSL renewal will be automatic.

As is often the case, the best option is the simplest: By pairing Kinsta’s built-in DNS features with a free Cloudflare wildcard SSL, the pain of SSL renewals will be a thing of the past.

![Adding a CNAME record to verify a third-party domain and renew SSL via MyKinsta.](https://kinsta.com/wp-content/uploads/2023/01/domain-ssl-renewal-txt.png)

Adding a CNAME record to verify a third-party domain and renew SSL via MyKinsta.

## Why Use Kinsta’s SSL Certificates?

[Kinsta’s Cloudflare integration](https://kinsta.com/cloudflare-integration/) includes [automatic and free SSL certificates](https://kinsta.com/blog/free-ssl-certificate/) for all WordPress sites hosted on our platform. What’s more, our free SSLs are also completely safe. [Cloudflare is one of the world’s leading web security companies](https://kinsta.com/blog/cloudflare-integration/), and they safely handle SSL termination for many millions of websites across the globe.

This access to Cloudflare-secured SSL with automatic renewal means customers no longer have to deal with the confusing process of obtaining their own certificate keys and private keys, debugging their intermediate certificate, generating a CSR, or installing their own SSL certificate.

Once your WordPress site’s domain is pointed at Kinsta, SSL starts working automatically. **No additional steps are needed — not even for renewal.**

[Switching is easy](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/#renew-free-cloudflare-ssl-certificate), but you’ll need to confirm your current setup first. If you’re a Kinsta customer but aren’t sure what kind of SSL certificate you have, you can [check via MyKinsta](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/#check-your-ssl-certificate).

## Simplifying Site Management at Kinsta

At Kinsta, we understand that both speed and [security are of the utmost importance](https://kinsta.com/blog/cloud-security/) to our customers, which is why we’re constantly looking for ways to improve our services.

The average SSL certificate renewal process may not seem like big deal, but it can often take longer than anticipated, especially if your registrar or hosting provider has complicated their dashboard interface or renewal processes since you last used them.

The whole operation inevitably takes time — and as every site owner knows, those small chunks of time can quickly add up.

By simplifying the SSL certificate renewal process, we’re making it easier for our customers to [keep their websites secure](https://kinsta.com/blog/website-security-check/) and protect their online assets. We’re also saving them valuable time that can be better spent creating and managing their sites.

Just one more of the many reasons to switch to Kinsta for your [WordPress hosting needs](https://kinsta.com/wordpress-hosting/).
