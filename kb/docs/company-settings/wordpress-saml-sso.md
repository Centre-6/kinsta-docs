---
url: "https://kinsta.com/docs/company-settings/wordpress-saml-sso/"
title: "SAML Single Sign-On (SSO)"
tier: "docs"
product: "company-settings"
product_label: "MyKinsta Company Settings"
subsection: "wordpress-saml-sso"
section: ["Company Settings"]
kinsta_last_updated: "2026-01-23T10:59:59"
change_signal: "2026-01-23T10:59:59"
fetched_at: "2026-10-07T22:58:17Z"
sha256: "4db6e03b15b047bf25f83536fcee513f2f6e7820029971ce055ab9ecf91a1e7d"
body_chars: 15404
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# SAML Single Sign-On (SSO)

**Section:** Company Settings
**Product:** MyKinsta Company Settings
**Source:** https://kinsta.com/docs/company-settings/wordpress-saml-sso/
**Kinsta last updated:** 2026-01-23T10:59:59

## On this page

- [Set up SAML SSO](#set-up-saml-sso)
  - [Enable SSO in MyKinsta](#enable-sso-in-mykinsta)
  - [Set up the app integration in your IdP](#set-up-the-app-integration-in-your-idp)
  - [Kinsta setup](#kinsta-setup)
    - [Email domain](#email-domain)
    - [Set up Kinsta SAML](#set-up-kinsta-saml)
  - [Test the authentication in MyKinsta](#test-the-authentication-in-mykinsta)
- [Mandatory single sign-on](#mandatory-single-sign-on)
- [Exceptions](#exceptions)
  - [Add a user to exceptions](#add-a-user-to-exceptions)
  - [Remove a user from exceptions](#remove-a-user-from-exceptions)
- [Just-in-time provisioning](#just-in-time-provisioning)
  - [Change default role](#change-default-role)
  - [Enable JIT provisioning](#enable-jit-provisioning)
  - [Disable JIT provisioning](#disable-jit-provisioning)
- [Removing users](#removing-users)
- [Change the session duration](#change-the-session-duration)
- [Disable SSO](#disable-sso)
- [What is the difference between SAML SSO and OAuth SSO?](#what-is-the-difference-between-saml-sso-and-oauth-sso)

---

Security Assertion Markup Language (SAML) Single Sign-On (SSO) allows users to securely access multiple applications using a single set of credentials, typically their company email and password. Instead of creating separate logins for each service, users authenticate once through a company-managed Identity Provider (IdP) such as Okta, OneLogin, Microsoft Entra, or Google Workspace.

The IdP verifies the user’s identity and grants access to all connected applications without requiring additional logins. The organization centrally manages access control, authentication policies, and permissions, providing greater security, compliance, and administrative efficiency.

With SAML SSO, company owners or IT administrators can link their corporate email domain (e.g., `@mycompany.com`) to the organization’s IdP. This ensures that anyone with a company email address is automatically recognized and securely authenticated when accessing approved tools and services.

At Kinsta, SAML SSO lets you connect your company’s IdP directly to MyKinsta. By creating a SAML application in your IdP and adding the connection details to MyKinsta, your team can sign in using their existing company credentials, eliminating the need to create or manage separate MyKinsta passwords. This also gives company owners centralized control over who can access MyKinsta, directly through the IdP.

Kinsta supports all identity providers (IdPs) that use the SAML standard, including Microsoft Entra ID, Okta, OneLogin, Google Workspace, Auth0, Duo, JumpCloud, and more.

## Set up SAML SSO

For detailed step-by-step guides for the most popular IdPs, refer to one of the following:

- [Google Workspace SAML SSO](https://kinsta.com/docs/company-settings/wordpress-saml-sso/google-workspace-saml-sso/)
- [Microsoft Entra SAML SSO](https://kinsta.com/docs/company-settings/wordpress-saml-sso/microsoft-entra-saml-sso/)
- [Okta SAML SSO](https://kinsta.com/docs/company-settings/wordpress-saml-sso/okta-saml-sso)
- [OneLogin SAML SSO](https://kinsta.com/docs/company-settings/wordpress-saml-sso/onelogin-saml-sso)
- [Ping Identity SAML SSO](https://kinsta.com/docs/company-settings/wordpress-saml-sso/ping-identity-saml-sso/)

### Enable SSO in MyKinsta

When you set up SAML SSO, you can click **Save and exit setup** at any stage to store your progress and return later.

In MyKinsta, go to your ***username*** > **Company settings** > **Single sign-on**, and click **Enable**.

![Enable SSO in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-saml-sso-enable.png)

Enable SSO in MyKinsta.

Read through the introduction, which explains how SSO will be set up, and click **Continue**.

![Introduction to the steps required to set up SSO.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-sso-intro.png)

Introduction to the steps required to set up SSO.

### Set up the app integration in your IdP

Use the information provided within **Create SAML app** to set up a SAML app within your identity provider, and then click **Continue**.

- **App name:** Copy and paste this into the Application Name field in your IdP.
- **App description:** Copy and paste this into the Application Description field in your IdP. This field is typically optional.
- **App icon:** Click Download to get the Kinsta icon, then upload it to your IdP application.
- **SSO/ACS URL:** This is the Kinsta endpoint your IdP redirects to after authentication. It processes the SAML response, verifies it, and establishes the user’s session in MyKinsta. Copy and paste this into the **SSO**/**ACS**/**Recipient**/**Single sign-on URL** field in your IdP.
- **Entity ID:** Kinsta’s unique identifier within your IdP, used to recognize Kinsta as the service provider. Copy and paste this into the **Entity ID**/**Audience URI**/**Audience** field in your IdP.
- **Start URL:** The web address for Kinsta’s SSO access portal. This is the entry point users visit to log in using SSO, triggering the SAML authentication request to the IdP. Copy and paste this into the **Start URL**/**Login URL** field in your IdP.
- **Signed Response:** A signed response provides secure digital verification, allowing Kinsta to confirm a user’s identity and grant access without requiring an additional login.
- **Name ID format:** Defines how Kinsta identifies users. This must be set to an email address format in the IdP.
- **Required attributes:** The attributes Kinsta requires from your IdP to complete the login process.

![Information to create the SAML app at your IdP.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-create-saml-app.png)

Information to create the SAML app at your IdP.

### Kinsta setup

#### Email domain

In the **Domain name**, enter the email domain users will use to sign in using SAML SSO, and click **Add domain**.

Only MyKinsta accounts with an email address matching the verified domain can authenticate via SAML. For example, if SAML is enabled for `example.com`, only users with an `@example.com` email address will be able to sign in for that company.

If the domain has already been verified in MyKinsta through DNS management or as a site domain, it will automatically be verified. If it hasn’t, you’ll be prompted to add a TXT record to your DNS management service to confirm domain ownership.

![Add the TXT record to your DNS to verify ownership.](https://kinsta.com/wp-content/uploads/2025/09/kinsta-verify-domain-saml.png)

Add the TXT record to your DNS to verify ownership.

Because DNS changes can take time to propagate, you can click **Save and exit setup** to store your progress and return later.

#### Set up Kinsta SAML

When the domain has been verified, use the information provided from your IdP to complete the **SSO URL**, **Entity ID**, and **Public certificate**, and then click **Continue**.

![Use your IdP details to set up SSO within MyKinsta.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-saml-okta-kinsta-setup.png)

Use your IdP details to set up SSO within MyKinsta.

### Test the authentication in MyKinsta

To check everything is set up correctly, click **Test authentication**.

A notification appears if the test was successful or if the test fails.

If the test fails, click **Back** and check your SAML settings within your IdP and within MyKinsta.

If the test is successful and you want to enable SAML, click **Save and set changes live**.

![Test your SSO set up and set the changes live. ](https://kinsta.com/wp-content/uploads/2025/08/wordpress-sso-test.png)

Test your SSO setup and set the changes live.

Your MyKinsta company users will now be able to sign in with SAML SSO or by entering their username and password. If you want to force users to sign on via SAML, you can enable [Mandatory SSO](#mandatory-single-sign-on). Users who sign in through an IdP are not required to complete Kinsta’s 2FA, as authentication is handled directly by the IdP.

![Sign in to MyKinsta with SAML SSO.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-sign-on-saml-sso.png)

Sign in to MyKinsta with SAML SSO.

## Mandatory single sign-on

To require all users to log in with SSO, enable mandatory SSO. With this setting, all users are prompted to sign in via the identity provider (IdP) rather than their MyKinsta credentials. If a user has already authenticated with SAML elsewhere they’ll automatically be logged in. If a user switches companies to a company that does not have SSO enabled they must enter their MyKinsta credentials.

You can also add Exceptions to allow specific users to log in with a password even when mandatory SSO is enabled. This is useful for 3rd parties that need to access your company but don’t have an email address in your domain, such as developers.

If mandatory SSO is enabled but SAML is **not** enabled, users will be required to log in with their MyKinsta credentials.

![Enable mandatory SSO for all users.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-mandatory-sso-enabled.png)

Enable mandatory SSO for all users.

## Exceptions

If [mandatory SSO](#mandatory-single-sign-on) is enabled, you can add specific users to an exceptions list, allowing them to log in with their MyKinsta credentials instead of SSO. This is useful for 3rd parties that need to access your company but don’t have an email address in your domain, such as, developers.

![Users who can still sign on with a password when mandatory SSO is enabled.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-sso-exceptions.png)

Users who can still sign on with a password when mandatory SSO is enabled.

### Add a user to exceptions

When inviting a user who does not have an existing MyKinsta account, you must first [invite them to your company](https://kinsta.com/docs/company-settings/user-management/#invite-a-user). The user must accept the invitation and create their account. Upon initial login, they will not yet have access to your company. Once the account is created, you can add the user to the exceptions list to allow access without SSO.

To add a user to the exceptions list, click **Add exceptions**. Select the user from the list and click **Add exception**.

![Add a user to the exceptions list.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-sso-add-exceptions.png)

Add a user to the exceptions list.

### Remove a user from exceptions

To remove a user from the exceptions list, click the trash can icon on the user and then click **Remove exception**.

![Remove a user from exceptions.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-sso-exceptions-remove.png)

Remove a user from exceptions.

When you remove the last user from the exceptions list, a warning message will appear. If all users are removed and an issue occurs with the IdP, you may lose access to your MyKinsta company.

![Warning message when you remove the last user from the SSO exceptions. ](https://kinsta.com/wp-content/uploads/2025/09/wordpress-SSO-remove-last-exception.png)

Warning message when you remove the last user from the SSO exceptions.

## Just-in-time provisioning

Just-in-time (JIT) provisioning allows users authorized by your IdP to access your MyKinsta company without requiring an invitation. In most cases, this means anyone with an email address on your domain. When a user signs in to MyKinsta, they are directed through IdP SSO and do not need to create a separate MyKinsta account. By default, users provisioned through JIT are assigned the [**Company Developer**](https://kinsta.com/docs/company-settings/user-management/#company-developer) role. You can adjust each user’s access level after they join, or [update the default role](#change-default-role) to define the access level new JIT-provisioned users receive upon joining. 

### Change default role

When JIT provisioning is enabled, users are assigned the **Company Developer** by default. To change their default access level, click **Change default role**.

![Change the default access level for JIT provisioning.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-sso-jit-change-default.png)

Change the default access level for JIT provisioning.

You can then choose the [access level](https://kinsta.com/docs/company-settings/user-management/) you want to assign to users who join via JIT provisioning, and click **Change default role**.

![Set the default role for users who sign in via JIT provisioning.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-sso-jit-default-role.png)

Set the default role for users who sign in via JIT provisioning.

### Enable JIT provisioning

Once you have set the default role, to enable JIT provisioning, click **Enable**, and then click **Enable JIT provisioning**.

![Enable JIT provisioning in MyKinsta. ](https://kinsta.com/wp-content/uploads/2025/09/wordpress-sso-jit-enable-1.png)

Enable JIT provisioning in MyKinsta.

### Disable JIT provisioning

To disable JIT provisioning, click **Disable**, and then click **Disable JIT provisioning**. If you disable JIT provisioning and SSO, users created through JIT will be prompted to set a password the next time they log in to MyKinsta.

![Disable JIT provisioning in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-sso-jit-disable.png)

Disable JIT provisioning in MyKinsta.

## Removing users

To fully revoke access, users must be removed from both MyKinsta and your identity provider (IdP).

- If SSO and JIT provisioning are enabled, removing a user from MyKinsta alone will not block access. The user can still sign in through your IdP.
- If you remove a user only from your IdP and mandatory SSO is not enabled, the user can still log in with their MyKinsta credentials.

## Change the session duration

Your identity provider (IdP) controls the duration and expiration of your SSO session. Refer to your IdP’s supporting documentation for information about how to change this.

## Disable SSO

If you disable SSO, users will no longer be able to sign in using SAML SSO and must instead log in with their email address and password.

If JIT provisioning was previously enabled, some users may not have an existing MyKinsta password. In this case, they can create one by selecting [**Forgot password**](https://kinsta.com/docs/user-settings/logging-in/#reset-your-mykinsta-password) on the [MyKinsta login page](https://my.kinsta.com/login).

Once SSO is disabled, all users will be required to use [Kinsta’s Two-Factor Authentication (2FA)](https://kinsta.com/docs/user-settings/logging-in/#two-factor-authentication-2-fa).

For security, multiple failed login attempts may [lock the account](https://kinsta.com/docs/user-settings/logging-in/#locked-account). If this happens, Kinsta will send an email containing a temporary login link so the user can regain access to MyKinsta.

To disable SSO, within **Single sign-on**, click **Disable**.

![Disable SAML SSO in MyKinsta. ](https://kinsta.com/wp-content/uploads/2025/10/wordpress-disable-saml-sso.png)

Disable SAML SSO in MyKinsta.

To confirm you want to disable SSO, click **Disable SSO**.

![Confirm you want to disable SSO.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-confirm-disable-saml-sso.png)

Confirm you want to disable SSO.

## What is the difference between SAML SSO and OAuth SSO?

SAML SSO and OAuth SSO both allow single sign-on, but they’re built for different use cases, technologies, and types of identities.

SAML SSO is used by businesses and enterprises to provide employees with secure, company-managed access to internal tools. With SAML, you sign in once using your work email and password, and you’re automatically logged in to all approved apps, such as MyKinsta, Slack, or Salesforce, without needing to remember separate passwords. Usually, your company’s IT team manages access centrally through the Identity Provider (IdP), deciding who can sign in and which tools they can access. This provides greater security, compliance, and easier management for larger teams.

OAuth SSO, on the other hand, is most common for personal use. It lets you sign in to apps or websites using an existing personal account, such as Google, Apple, or Facebook, instead of creating a new one. This is linked to your personal identity rather than your organization, and the company cannot control who accesses which applications. This means that OAuth SSO is less suitable for enterprise-level access management.
