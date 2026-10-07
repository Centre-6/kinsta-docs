---
url: "https://kinsta.com/docs/company-settings/wordpress-saml-sso/onelogin-saml-sso/"
title: "SAML Single Sign-On (SSO) - OneLogin SAML SSO"
tier: "docs"
product: "company-settings"
product_label: "MyKinsta Company Settings"
subsection: "wordpress-saml-sso"
section: []
kinsta_last_updated: "January 16, 2026"
sitemap_lastmod: "2026-01-16T16:29:41+00:00"
fetched_at: "2026-10-07T22:37:51Z"
sha256: "7142025e26a0b3f8be788a88ae1fdf6c5d862d41d3df9e944cd12e7310d9b2d0"
body_chars: 10553
extracted_with: "main article"
status: "live"
---

# SAML Single Sign-On (SSO) - OneLogin SAML SSO

**Product:** MyKinsta Company Settings
**Source:** https://kinsta.com/docs/company-settings/wordpress-saml-sso/onelogin-saml-sso/
**Kinsta last updated:** January 16, 2026

## On this page

- [Enable SSO in MyKinsta](#enable-sso-in-mykinsta)
- [Set up the app integration in OneLogin](#set-up-the-app-integration-in-onelogin)
- [Map your OneLogin attributes](#map-your-onelogin-attributes)
- [Assign users to the OneLogin app](#assign-users-to-the-onelogin-app)
- [Kinsta setup](#kinsta-setup)
  - [Email domain](#email-domain)
  - [Set up Kinsta SAML](#set-up-kinsta-saml)
- [Test the authentication in MyKinsta](#test-the-authentication-in-mykinsta)
- [Change the session duration](#change-the-session-duration)

---

[OneLogin](https://www.onelogin.com/) is an Identity Provider (IdP) that enables secure single sign-on (SSO), allowing your company’s users to access multiple applications with one login.

With Security Assertion Markup Language (SAML) SSO, employees sign in once using their company credentials (typically email and password). The IdP, such as OneLogin, verifies their identity and grants seamless, secure access to all connected services, without requiring separate logins for each application.

Company owners or IT administrators can link their organization’s email domain (e.g., @mycompany.com) to the IdP so that anyone with a company email address is automatically recognized and can securely sign in to SAML-enabled tools.

Using Kinsta SAML SSO, you can connect OneLogin to MyKinsta by creating a SAML application within OneLogin, verifying your company’s email domain, and adding the required OneLogin details in MyKinsta. This allows your team to log in with their existing company credentials, eliminating the need to create or manage separate MyKinsta accounts.

## Enable SSO in MyKinsta

When you set up SAML SSO, you can click **Save and exit setup** at any stage to store your progress and return later.

In MyKinsta, go to your ***username*** > **Company settings** > **Single sign-on**, and click **Enable**.

![Enable SSO in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-saml-sso-enable.png)

Enable SSO in MyKinsta.

Read through the introduction, which explains how SSO will be set up, and click **Continue**.

![Introduction to the steps required to set up SSO.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-sso-intro.png)

Introduction to the steps required to set up SSO.

The next page provides all the information you need to set up your SAML app within OneLogin.

## Set up the app integration in OneLogin

In MyKinsta, the **Create SAML app** tab provides all the information you need to set up your SAML app within OneLogin. The following steps explain where to add this information.

![Information to create the SAML app at OneLogin.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-create-saml-app.png)

Information to create the SAML app at OneLogin.

Log in to OneLogin as a user with admin access, and within **Administration**, click **Applications** > **Applications** > **Add App**.

![Add an application in OneLogin.](https://kinsta.com/wp-content/uploads/2025/09/onelogin-add-app.png)

Add an application in OneLogin.

Search for ‘saml custom connector’ and select **SAML Custom Connector (Advanced)**.

![Search for the SAML custom connector app in OneLogin.](https://kinsta.com/wp-content/uploads/2025/09/onelogin-search-saml.png)

Search for the SAML custom connector app in OneLogin.

In the Display Name, enter the **App name** from MyKinsta. You can also download the **App icon** from MyKinsta and upload this to the **Square Icon**, and add a **Description** if required. Click **Save**.

![Add the app name in OneLogin.](https://kinsta.com/wp-content/uploads/2025/09/onelogin-app-name.png)

Add the app name in OneLogin.

Click **Configuration** and complete as follows:

- **Audience (EntityID):** Copy and paste the **Entity ID** from MyKinsta.
- **Recipient:** Copy and paste the **SSO/ACS URL** from MyKinsta.
- **ACS (Consumer) URL Validator:** Copy and paste the **SSO/ACS URL** from MyKinsta.
- **ACS (Consumer) URL:**Copy and paste the **SSO/ACS URL** from MyKinsta.
- **Login URL:** Copy and paste the **Start URL** from MyKinsta.
- **SAML initiator:** Select **Service Provider**.
- **SAML nameID format:** Select **Email**.
- **SAML issuer type:** Select **Specific**.
- **SAML signature element:** Select **Assertion**.
- **Sign SLO Response:** Select this option.
- **Sign SLO Request:** Select this option.

Leave all other fields as default and click **Save**.

![Configuration of the SAML app in OneLogin.](https://kinsta.com/wp-content/uploads/2025/09/onelogin-configuration.png)

Configuration of the SAML app in OneLogin.

Click **SSO**, and within **SAML Signature Algorithm** select **SHA-256**, and click **Save**.

![Change the SAML signature algorithm in OneLogin.](https://kinsta.com/wp-content/uploads/2025/09/onelogin-sso-signature.png)

Change the SAML signature algorithm in OneLogin.

## Map your OneLogin attributes

Within OneLogin, you must map the firstName, lastName, and email attributes from MyKinsta to the correct fields within OneLogin. For more information about how to do this, refer to the [OneLogin documentation](https://onelogin.service-now.com/support?id=kb_article&sys_id=c1e4255a9758ea900f94b86ef053af1a&kb_category=566ffd6887332910695f0f66cebb3556).

## Assign users to the OneLogin app

In OneLogin, you can assign a policy to the application to allow all users using the policy to log in to the app. Go to **Applications** > **Applications**, select the application you set up for the MyKinsta Dashboard, click **Access**, choose the policy you want to assign, and click **Save**. For more information about security policies, refer to [OneLogin’s documentation](https://onelogin.service-now.com/support?id=kb_article&sys_id=1510ecd787dee610f7b8a7dd3fbb35d9&kb_category=95c6573887772910763a0ed7dabb3538).

You can also assign individual users to the application. In OneLogin, click **Users** > **Users**, select the user you want to assign, click **Applications**, and click the plus icon.

![Add a user to an application in OneLogin.](https://kinsta.com/wp-content/uploads/2025/09/onelogin-add-user-to-app.png)

Add a user to an application in OneLogin.

From the **Select application** dropdown, select the MyKinsta application, and click **Continue**.

![Assign an application to a user in OneLogin.](https://kinsta.com/wp-content/uploads/2025/09/onelogin-assign-app-user.png)

Assign an application to a user in OneLogin.

Select **Allow the user to sign in**, ensure the credentials are correct, and click **Save**.

![Save the app allocation for the user. ](https://kinsta.com/wp-content/uploads/2025/09/onelogin-save-app-user-assign.png)

Save the app allocation for the user.

To test authentication, make sure the MyKinsta user account you’re signed in with is assigned.

## Kinsta setup

In MyKinsta, on **Create SAML app**, click **Continue** so that you are on the **Kinsta setup** page.

### Email domain

In the **Domain name**, enter the email domain users will use to sign in using SAML SSO, and click **Add domain**.

Only MyKinsta accounts with an email address matching the verified domain can authenticate via SAML. For example, if SAML is enabled for `example.com`, only users with an `@example.com` email address will be able to sign in for that company.

If the domain has already been verified in MyKinsta through DNS management or as a site domain, it will automatically be verified. If it hasn’t, you’ll be prompted to add a TXT record to your DNS management service to confirm domain ownership.

![Add the TXT record to your DNS to verify ownership.](https://kinsta.com/wp-content/uploads/2025/09/kinsta-verify-domain-saml.png)

Add the TXT record to your DNS to verify ownership.

Because DNS changes can take time to propagate, you can click **Save and exit setup** to store your progress and return later.

### Set up Kinsta SAML

In OneLogin, go to **Applications** > **Applications**, select the application you set up for the MyKinsta Dashboard, and click **SSO**.

This page provides all the information you need to set up SAML in MyKinsta.

![OneLogin SAML information for MyKinsta setup.](https://kinsta.com/wp-content/uploads/2025/09/onelogin-saml-details.png)

OneLogin SAML information for MyKinsta setup.

In MyKinsta, within the Single sign-on **Kinsta setup** tab, complete the fields as follows:

- **SSO URL:** Copy and paste the **SAML 2.0 Endpoint (HTTP)** from OneLogin.
- **Entity ID:** Copy and paste the **Issuer URL** from OneLogin.
- **Public certificate:** In OneLogin, on the **X.509 Certificate**, click **View Details**, copy and paste the contents of the **X.509 Certificate**.

Click **Continue**.

![Enter the required information from the IdP to set up Kinsta SAML.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-kinsta-setup-onelogin.png)

Enter the required information from the IdP to set up Kinsta SAML.

## Test the authentication in MyKinsta

You cannot enable SAML SSO within MyKinsta without first testing the authentication.

In MyKinsta, within the Single sign-on **Test and finish** tab, click **Test authentication**.

![Test the SAML authentication within MyKinsta.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-saml-test-authentication.png)

Test the SAML authentication within MyKinsta.

A notification appears if the test was successful or if the test fails.

If the test fails, click **Back** and check your SAML settings within OneLogin and within MyKinsta.

If the test is successful and you want to enable SAML, click **Save and set changes live**.

Your MyKinsta company users will now be able to sign in with SAML SSO or by entering their username and password. Users who sign in through an IdP are not required to complete Kinsta’s 2FA, as authentication is handled directly by the IdP.

If you want to force users to sign on via SAML, you can enable [Mandatory SSO](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#mandatory-single-sign-on) and add [Exceptions](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#exceptions). You can also enable [JIT provisioning](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#just-in-time-provisioning) to allow users authorized by your IdP to access your MyKinsta company without requiring an invitation.

![Sign in to MyKinsta with SAML SSO.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-sign-on-saml-sso.png)

Sign in to MyKinsta with SAML SSO.

## Change the session duration

Your Identity Provider (IdP) determines how long your SSO session remains active and when it expires. If your IdP doesn’t specify a session duration, MyKinsta defaults to a 24-hour session.

When your SSO session expires, you’ll be logged out of SSO. If you’re working within a company that uses SSO, you’ll be prompted to reauthenticate. If you have access to multiple companies in MyKinsta, you’ll remain logged in overall but will need to reauthenticate before accessing any company that requires SSO.

For details on adjusting session duration, refer to the [OneLogin Knowledge Base](https://support.onelogin.com/kb/4271392/user-policies).
