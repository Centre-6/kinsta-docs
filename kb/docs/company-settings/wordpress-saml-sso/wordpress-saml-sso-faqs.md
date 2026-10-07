---
url: "https://kinsta.com/docs/company-settings/wordpress-saml-sso/wordpress-saml-sso-faqs/"
title: "SAML SSO FAQs"
tier: "docs"
product: "company-settings"
product_label: "MyKinsta Company Settings"
subsection: "wordpress-saml-sso"
section: ["Company Settings", "SAML Single Sign-On (SSO)"]
kinsta_last_updated: "2025-10-27T11:05:21"
change_signal: "2025-10-27T11:05:21"
fetched_at: "2026-10-07T22:58:17Z"
sha256: "f9012da2039733a4de38989c0e303b2e5a41aa58bcb14e63edd52ac931ab0311"
body_chars: 3244
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# SAML SSO FAQs

**Section:** Company Settings > SAML Single Sign-On (SSO)
**Product:** MyKinsta Company Settings
**Source:** https://kinsta.com/docs/company-settings/wordpress-saml-sso/wordpress-saml-sso-faqs/
**Kinsta last updated:** 2025-10-27T11:05:21

## On this page

- [What is the difference between SAML SSO and OAuth SSO?](#what-is-the-difference-between-saml-sso-and-oauth-sso)
- [Can I log in to MyKinsta through my Identity Provider (IdP)?](#can-i-log-in-to-mykinsta-through-my-identity-provider-idp)
- [Why can I still log in to MyKinsta with my username and password when SSO is mandatory?](#why-can-i-still-log-in-to-mykinsta-with-my-username-and-password-when-sso-is-mandatory)
- [How long is the session duration?](#how-long-is-the-session-duration)
- [Can I add multiple domains to the SSO configuration?](#can-i-add-multiple-domains-to-the-sso-configuration)

---

Below, we’ve compiled all the **most common SAML SSO****questions** in one place.

## What is the difference between SAML SSO and OAuth SSO?

SAML SSO and OAuth SSO both allow single sign-on, but they’re built for different use cases, technologies, and types of identities.

SAML SSO is used by businesses and enterprises to provide employees with secure, company-managed access to internal tools. With SAML, you sign in once using your work email and password, and you’re automatically logged in to all approved apps, such as MyKinsta, Slack, or Salesforce, without needing to remember separate passwords. Usually, your company’s IT team manages access centrally through the Identity Provider (IdP), deciding who can sign in and which tools they can access. This provides greater security, compliance, and easier management for larger teams.

OAuth SSO, on the other hand, is most common for personal use. It lets you sign in to apps or websites using an existing personal account, such as Google, Apple, or Facebook, instead of creating a new one. This is linked to your personal identity rather than your organization, and the company cannot control who accesses which applications. This means that OAuth SSO is less suitable for enterprise-level access management.

## Can I log in to MyKinsta through my Identity Provider (IdP)?

No, you can’t log in to MyKinsta directly from your Identity Provider. For security reasons, all logins must start from the MyKinsta login page. This ensures that your authentication request is properly verified and prevents potential security issues, such as unauthorized or invalid login attempts. Logging in through MyKinsta provides a more secure and reliable sign-in process for your account. For more information about this, refer to IdentityServer’s article [The Dangers of SAML IdP-Initiated SSO](https://www.identityserver.com/articles/the-dangers-of-saml-idp-initiated-sso).

## Why can I still log in to MyKinsta with my username and password when SSO is mandatory?

Mandatory SSO applies only to the specific company where it has been enabled. If you have access to multiple companies in MyKinsta, you can still log in with your username and password. However, you won’t be able to access any company that requires mandatory SSO unless you sign in using that company’s SSO method or your username has been added to the [exceptions list](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#exceptions).

## How long is the session duration?

Your Identity Provider (IdP) determines how long your SSO session remains active and when it expires. If your IdP doesn’t specify a session duration, MyKinsta defaults to a 24-hour session.

When your SSO session expires, you’ll be logged out of SSO. If you’re working within a company that uses SSO, you’ll be prompted to reauthenticate. If you have access to multiple companies in MyKinsta, you’ll remain logged in overall but will need to reauthenticate before accessing any company that requires SSO.

For details on adjusting session duration, refer to your IdP’s documentation.

## Can I add multiple domains to the SSO configuration?

No, SSO is configured at the company level, and each company can have only one associated domain for SSO.
