---
url: "https://kinsta.com/blog/php2shell-kinsta-wordpress/"
title: "PHP2Shell: How Kinsta protected WordPress sites"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: []
kinsta_last_updated: "2026-10-23T15:28:05"
change_signal: "2026-10-23T15:28:05"
fetched_at: "2026-11-11T13:03:02Z"
sha256: "2a15c9caad283cbdb419b3a99be62d0a32dbd12d27fe7aec9d0810a60452150a"
body_chars: 6256
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# PHP2Shell: How Kinsta protected WordPress sites

**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/php2shell-kinsta-wordpress/
**Kinsta last updated:** 2026-10-23T15:28:05

## On this page

- [What is PHP2Shell?](#what-is-php2shell)
- [How Kinsta responded to PHP2Shell](#how-kinsta-responded-to-php2shell)
  - [Blocking exploit attempts with Cloudflare](#blocking-exploit-attempts-with-cloudflare)
  - [Applying the PHP security updates](#applying-the-php-security-updates)
- [Do Kinsta customers need to take any action?](#do-kinsta-customers-need-to-take-any-action)
- [Where to find updates and get help](#where-to-find-updates-and-get-help)

---

On October 21, 2026, two critical PHP vulnerabilities, collectively known as [PHP2Shell](https://en.wikipedia.org/wiki/PHP2Shell), were publicly disclosed. These vulnerabilities could allow attackers to execute malicious code on affected servers without authentication. The PHP development team [released emergency security updates](https://www.php.net/archive/2026.php#2026-10-21-5) the same day to address them.

**If your WordPress site is hosted on Kinsta, it’s protected against PHP2Shell.** Our engineering and security teams deployed the necessary PHP security updates across our hosting platform, including live and [staging environments](https://kinsta.com/docs/wordpress-hosting/staging-environment/). We found no evidence of breaches related to these vulnerabilities.

Here’s what you should know about PHP2Shell, how we handled the vulnerabilities, and how to check your site’s PHP settings.

## What is PHP2Shell?

PHP2Shell refers to two PHP vulnerabilities, identified as [CVE-2026-109618](https://www.cve.org/CVERecord?id=CVE-2026-109618) and [CVE-2026-109619](https://www.cve.org/CVERecord?id=CVE-2026-109619). Both received a critical severity rating of 9.2 under [CVSS 4.0](https://www.first.org/cvss/).

The vulnerabilities affect how PHP handles memory when processing requests. If exploited, an attacker could run malicious code on a server, potentially compromising the websites and data hosted there.

Since WordPress runs on PHP, these vulnerabilities also presented a risk to WordPress websites using affected PHP versions.

Unlike vulnerabilities found in a WordPress plugin, theme, or WordPress core, PHP2Shell affects the PHP runtime itself. This means updating WordPress or its plugins wouldn’t resolve the issue. The server’s PHP software needed to be patched.

The PHP team released fixes for PHP 8.2, 8.3, 8.4, and 8.5 on October 21. Older PHP versions received security fixes from third-party maintainers.

For Kinsta customers, we handled these updates at the hosting level rather than requiring changes to individual WordPress installations.

## How Kinsta responded to PHP2Shell

Our engineering and security teams began preparing for PHP2Shell before the official security patches became available. The response involved adding protections to reduce the risk of exploitation, then deploying patched PHP versions as they were released.

### Blocking exploit attempts with Cloudflare

One of our first priorities was protecting websites while we prepared the PHP fixes. Kinsta uses [Cloudflare’s Web Application Firewall (WAF)](https://kinsta.com/cloudflare-integration/) to help identify and block malicious requests before they reach websites hosted on our platform.

Before the PHP2Shell disclosure, [Cloudflare deployed new firewall protections](https://blog.cloudflare.com/php-vulnerabilities-waf-protection/) designed to detect attempts to exploit these vulnerabilities. Our team enabled the relevant protections across our hosting infrastructure.

As a result, our edge-level firewalls were already blocking PHP2Shell exploitation attempts while we waited for the PHP patches and during their deployment.

We also applied additional PHP configuration changes across our hosting environments to reduce potential exposure. Throughout the incident, we stayed in close contact with our [Vulnerability Protection](https://kinsta.com/vulnerability-protection/) partner, [Patchstack](https://patchstack.com/), sharing information about the threats and attack patterns we observed.

These measures helped protect websites while we prepared updates, but they weren’t a replacement for patching PHP itself.

### Applying the PHP security updates

Once the PHP team released the fixes, our engineering team began validating and deploying the patched PHP packages across the platform.

We deployed security updates for PHP 7.4 through PHP 8.5, including patches for older versions supplied by Freexian, our PHP package provider.

Because we manage PHP at the platform level, customers didn’t need to install the fixes or manually change their PHP versions. Our team handled the updates across the hosting infrastructure while keeping the additional Cloudflare protections in place.

On October 22, 2026, at 08:26 UTC, we marked the incident resolved on our public status page, confirming that all sites were protected and the security updates had been rolled out across the platform.

Throughout the incident, our team monitored suspicious activity, manually checked sites that appeared to be targeted, and continued spot-checking hosting environments for signs of compromise. We found no evidence of successful breaches related to PHP2Shell.

You can read the updates published throughout the response on our [PHP security incident status page](https://status.kinsta.com/incidents/c0c6xl1ghpb2).

## Do Kinsta customers need to take any action?

No. If your WordPress website is hosted on Kinsta, we’ve already applied the necessary security updates.

You don’t need to change your PHP version, install a separate patch, or take your website offline because of PHP2Shell. The protections also cover your staging environments.

If you suspended any environments as a precaution while we addressed the vulnerabilities, you can reactivate them now. Our team also performed the relevant security updates on suspended environments.

You should still keep your WordPress installation, plugins, and themes updated as part of your normal website maintenance. However, those updates are separate from the PHP2Shell fixes, which we’ve already applied at the hosting level.

## Where to find updates and get help

If you manage WordPress websites for clients, you can share our [official PHP security incident report](https://status.kinsta.com/incidents/c0c6xl1ghpb2) with them. It documents the updates we made as patched PHP versions became available and confirms the incident’s resolution.

If you have questions about a particular website or want to confirm its security status, you can contact [our support team](https://kinsta.com/kinsta-support/) directly through MyKinsta. Our team is available 24/7 to help.

For more information, see our [guide to contacting Kinsta Support](https://kinsta.com/docs/support/contact-support/).
