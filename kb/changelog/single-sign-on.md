---
url: "https://kinsta.com/changelog/single-sign-on/"
title: "Simplify secure access to MyKinsta with SAML single sign-on"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Simplify secure access to MyKinsta with SAML single sign-on"]
kinsta_last_updated: "2025-11-13T18:01:00+00:00"
sitemap_lastmod: "2025-11-13T18:01:00+00:00"
fetched_at: "2026-10-07T22:37:10Z"
sha256: "d686567a8fd141c92c84a22f16cc4203ccd9892d1e5170a2ea21fafce43fa419"
body_chars: 5676
extracted_with: "main article"
status: "live"
---

# Simplify secure access to MyKinsta with SAML single sign-on

**Section:** Changelog > Simplify secure access to MyKinsta with SAML single sign-on
**Product:** Changelog
**Source:** https://kinsta.com/changelog/single-sign-on/
**Kinsta last updated:** 2025-11-13T18:01:00+00:00

## On this page

- [Enabling SAML SSO in My Kinsta](#enabling-saml-sso-in-my-kinsta)
- [MyKinsta SSO and your team](#mykinsta-sso-and-your-team)
  - [Just-in-time provisioning of SSO](#just-in-time-provisioning-of-sso)
  - [Mandatory SSO and exceptions](#mandatory-sso-and-exceptions)
- [Secure WordPress management for organizations](#secure-wordpress-management-for-organizations)

---

Published
:   November 13, 2025

![An illustration representing the user interface for SAML Single-Sign-On in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/11/mykinsta-single-sign-on-changelog-1024x536.png)

Organizations can now manage access to the MyKinsta dashboard using Security Assertion Markup Language (SAML) protocols, enabling secure single sign-on (SSO) for their team members.

With SAML-based SSO enabled in MyKinsta, companies can grant users access to the dashboard using the same centralized identity provider (IdP) they might be using to mediate access to other enterprise applications.

Those providers might include popular services like Microsoft Entra ID, Okta, OneLogin, Google Workspace, Auth0, Duo, and JumpCloud, but any IdP that supports SAML will work with MyKinsta.

## Enabling SAML SSO in My Kinsta

The first step to enabling SAML SSO for your organization’s MyKinsta access is to review our extensive documentation for this new feature. In addition to instructions [common to all SAML SSO configurations](https://kinsta.com/docs/company-settings/wordpress-saml-sso/), we’ve documented configurations for a list of providers that, so far, includes:

- [Google Workspace](https://kinsta.com/docs/company-settings/wordpress-saml-sso/google-workspace-saml-sso/)
- [Okta](https://kinsta.com/docs/company-settings/wordpress-saml-sso/okta-saml-sso/)
- [OneLogin](https://kinsta.com/docs/company-settings/wordpress-saml-sso/onelogin-saml-sso/)

It all begins on the MyKinsta side by navigating to ***username*** > **Company settings** > **Single sign-on**, and clicking **Enable**:

![A screenshot showing the first step to enabling single sign-on in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-enable-sso.png)

Getting started with SSO in MyKinsta.

You will be configuring a SAML app in MyKinsta, the particulars of which you will provide to your IdP.

![A screenshot of the interface for providing SAML app details within MyKinsta.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-create-saml-app.png)

Configuring a SAML app in MyKinsta.

There’s a good chance you will find yourself jumping back and forth between the SAML configuration in MyKinsta and your IdP’s dashboard, so MyKinsta allows you to save your work there as you go.

## MyKinsta SSO and your team

Organizations that adopt SAML for SSO typically seek to simplify user access management across multiple applications while also enhancing security. SAML supports the kind of secure authentication many companies demand, while IdP platforms enable centralized user management.

When enabled in MyKinsta, SAML SSO allows organizations to avoid creating multiple user accounts in our dashboard to support their team. Instead, they can grant access to the Kinsta “SAML app” in their IdP platform.

For example, users of the Okta IdP would see something like this within that platform’s dashboard:

![A screenshot hoswing user-management on the IdP Okta.](https://kinsta.com/wp-content/uploads/2025/09/okta-assign-users.png)

Assigning users to the MyKinsta SAML application in Okta.

Users who sign in to MyKinsta using SAML SSO are not required to complete Kinsta’s two-factor authentication (2FA) steps, since authentication is handled directly by the IdP (which may use multi-factor authentication itself).

### Just-in-time provisioning of SSO

Kinsta supports Just-in-time (JIT) provisioning of SSO in MyKinsta, usually enabling any user authorized by your IdP to log in to the dashboard without an invitation. This allows your team to manage access requirements entirely within your IdP’s platform.

![Screenshot showing the interface in MyKinsta for initiating JIT provisioning or changing the default JIT role.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-sso-jit-change-default.png)

Enabling JIT provisioning or changing the default role.

By default, users provisioned through JIT are assigned the **Company Developer** role in MyKinsta. You can edit a user’s access level in MyKinsta after they join, or [update the default role for JiT](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#change-default-role) for newly provisioned users.

### Mandatory SSO and exceptions

A key feature of SAML SSO in MyKinsta is the ability to make such authentication mandatory:

![A screenshot showing the interface for enabling SSO mandatory in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-sso-mandatory.png)

SSO set to mandatory in MyKinsta.

When SSO is declared mandatory, organizations can create exceptions to that rule, allowing some users to log in with their MyKinsta passwords. This feature is particularly useful when dashboard access is granted to a user whose account is not managed in a SAML-based IdP.

![Screenshot showing an example of setting an exception to mandatory SSO in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-sso-exceptions.png)

An exception to mandatory SSO in MyKinsta.

## Secure WordPress management for organizations

The addition of SAML-based SSO is the latest enhancement to MyKinsta, supporting the security requirements of teams like yours.

Security is built into every part of the Kinsta platform. From [ISO 27001 certification](https://kinsta.com/blog/iso-27001-certification/) and [SOC 2 compliance](https://kinsta.com/blog/soc-2-compliance/) to built-in [firewalling](https://kinsta.com/blog/what-is-a-firewall/), [DDoS protection](https://kinsta.com/blog/prevent-ddos-attacks/), and [wildcard SSL](https://kinsta.com/blog/wildcard-ssl/), we’re committed to [keeping customer data](https://kinsta.com/blog/web-hosting-security/) safe.
