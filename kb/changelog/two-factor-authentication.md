---
url: "https://kinsta.com/changelog/two-factor-authentication/"
title: "Two-factor authentication is now required for MyKinsta logins"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-01-14T17:34:13"
change_signal: "2026-01-14T17:34:13"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "9a04164ea93e5676002cdcef69ec7daba1cbaa7bbfff5522cdbd8143238b8b39"
body_chars: 5600
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Two-factor authentication is now required for MyKinsta logins

**Product:** Changelog
**Source:** https://kinsta.com/changelog/two-factor-authentication/
**Kinsta last updated:** 2026-01-14T17:34:13

## On this page

- [How 2FA works in MyKinsta](#how-2fa-works-in-mykinsta)
- [Enabling an authenticator application](#enabling-an-authenticator-application)
- [Delaying repeat 2FA authentication](#delaying-repeat-2fa-authentication)
- [MyKinsta 2FA and Git-provider SSO](#mykinsta-2fa-and-git-provider-sso)
- [Kinsta: Focused on security](#kinsta-focused-on-security)

---

Kinsta now requires two-factor authentication (2FA) for access to the [MyKinsta dashboard](https://kinsta.com/mykinsta/).

While 2FA using authenticator applications like Google Authenticator and Authy has been an option in MyKinsta for some time, the move to make this extra step mandatory reflects the proven security enhancements provided by combining [multiple authentication methods](https://kinsta.com/blog/benefits-of-two-factor-authentication/).

The change also highlights the fact that customers’ MyKinsta dashboards are the first line of defence for the properties they host here — something hackers would love to exploit.

## How 2FA works in MyKinsta

If you have already enabled 2FA using an authenticator app or are using a Git service provider for single sign-on (SSO), there are no changes to your MyKinsta login flow. Otherwise, as the next step after you submit your login credentials (email and password), Kinsta sends a unique code via email to the address associated with your account.

It looks something like this:

![A screenshot of the email send to confirm two-factor authentication in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/05/mykinsta-2fa-authentication-email.png)

An example of the email and authentication code customers will receive for 2FA.

After receiving the email, you can flip back to your MyKinsta login to enter your authorization code and complete your login by clicking the **Verify** button:

![A screenshot of a MyKinsta login with a 2FA authorization code being provided.](https://kinsta.com/wp-content/uploads/2025/05/mykinsta-2fa-authentication-verify.png)

Verifying your 2FA login in MyKinsta.

## Enabling an authenticator application

Receiving an authentication code via email will be the ongoing procedure for your MyKinsta access unless you choose to use Git-provider SSO or an authenticator application, like [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2), [Authy](https://www.authy.com/), [2FAS](https://2fas.com/), [Duo](https://duo.com/), [Aegis Authenticator](https://getaegis.app/), or a password manager with built-in 2FA support like [1Password](https://kinsta.com/docs/user-settings/logging-in/#how-to-add-mykinsta-2-fa-to-1-password).

You can enable an authenticator application by clicking on your username in the top right corner of the MyKinsta dashboard and selecting **User settings**. On the resulting **My account** page, find the **Authenticator app** section and click the **Enable** button:

![A screen shot of the My Accounts page in MyKinsta where an authenticator application can be enabled.](https://kinsta.com/wp-content/uploads/2025/05/mykinsta-2fa-authenticator-app-status.png)

Beginning the process to enable an authenticator app for MyKinsta access.

You will be prompted to scan a QR code with your authenticator application. If you have problems scanning the image, you can enter the 16-digit code displayed under the QR code. You can then enter the six-digit code initially displayed by your authenticator application and click the **Verify** button:

![A screenshot showing a QR code used to connect MyKista to an authenticator app for 2FA.](https://kinsta.com/wp-content/uploads/2025/05/mykinsta-2fa-authenticator-app-enable.png)

Adding MyKinsta to an authenticator application.

## Delaying repeat 2FA authentication

You can reduce the number of times MyKinsta requests authentication by selecting **Don’t ask for a code on this device** while logging in:

![A screenshot of the MyKinsta login dialog with the option to reduce 2FA requests selected.](https://kinsta.com/wp-content/uploads/2025/05/mykinsta-2fa-authentication-do-not-ask.png)

Asking to delay requests for two-factor authentication.

After logging in with this option enabled, MyKinsta wil wait 30 days before asking for re-authentication on the same device connecting via the same IP address.

## MyKinsta 2FA and Git-provider SSO

You may already be using [SSO access to MyKinsta](https://kinsta.com/docs/user-settings/logging-in/#single-sign-on-sso) supported by the Git service providers [GitHub](https://kinsta.com/blog/what-is-github/), [GitLab](https://kinsta.com/blog/gitlab-vs-github/), or [Bitbucket](https://kinsta.com/blog/bitbucket-vs-github/). If so, your login process will not change, and you will use any 2FA configured for your preferred Git service provider.

If you want to add one of these SSO options, you can do so on the **My account** page by scrolling to the **Connect with Git service** section, selecting your provider, and then logging in to that service:

![Screenshot of the area on the My Account page in MyKista were SSO using a Git service provider is enabled.](https://kinsta.com/wp-content/uploads/2025/05/mykinsta-connect-git-service.png)

Choosing a Git service for SSO.

## Kinsta: Focused on security

At Kinsta, we’re dedicated to [protecting customer websites](https://kinsta.com/blog/web-hosting-security/) and their data. Our [ISO 27001-certified](https://kinsta.com/blog/iso-27001-certification/) and [SOC 2-compliant](https://kinsta.com/blog/soc-2-compliance/) information security procedures reflect our investment in earning customer trust. It’s also evident in our free tools to safeguard websites with [firewalling](https://kinsta.com/blog/what-is-a-firewall/), [DDoS protection](https://kinsta.com/blog/prevent-ddos-attacks/), and [wildcard SSL](https://kinsta.com/blog/wildcard-ssl/).

Visit Kinsta’s [Trust Center](https://trust.kinsta.com/) for information on the company’s ongoing security-protection efforts.
