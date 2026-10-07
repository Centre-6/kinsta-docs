---
url: "https://kinsta.com/docs/company-settings/wordpress-saml-sso/okta-saml-sso/"
title: "SAML Single Sign-On (SSO) - Okta SAML SSO"
tier: "docs"
product: "company-settings"
product_label: "MyKinsta Company Settings"
subsection: "wordpress-saml-sso"
section: []
kinsta_last_updated: "November 14, 2025"
sitemap_lastmod: "2025-11-14T17:51:30+00:00"
fetched_at: "2026-10-07T22:39:05Z"
sha256: "003b7fcf3813bb0bfd38cc1b70f000a75290c0b49d50622c1586d8a7e2b3e130"
body_chars: 9455
extracted_with: "main article"
status: "live"
---

# SAML Single Sign-On (SSO) - Okta SAML SSO

**Product:** MyKinsta Company Settings
**Source:** https://kinsta.com/docs/company-settings/wordpress-saml-sso/okta-saml-sso/
**Kinsta last updated:** November 14, 2025

## On this page

- [Enable SSO in MyKinsta](#enable-sso-in-mykinsta)
- [Set up the app integration in Okta](#set-up-the-app-integration-in-okta)
- [Map your Okta attributes](#map-your-okta-attributes)
- [Assign users to the Okta app](#assign-users-to-the-okta-app)
- [Kinsta setup](#kinsta-setup)
  - [Email domain](#email-domain)
  - [Set up Kinsta SAML](#set-up-kinsta-saml)
- [Test the authentication in MyKinsta](#test-the-authentication-in-mykinsta)
- [Change the session duration](#change-the-session-duration)

---

[Okta](https://www.okta.com/) is an Identity Provider (IdP) that enables secure single sign-on (SSO), allowing your company’s users to access multiple applications with one login.

With Security Assertion Markup Language (SAML) SSO, employees sign in once using their company credentials (typically email and password). The IdP, such as Okta, verifies their identity and grants seamless, secure access to all connected services, without requiring separate logins for each application.

Company owners or IT administrators can link their organization’s email domain (e.g., @mycompany.com) to the IdP so that anyone with a company email address is automatically recognized and can securely sign in to SAML-enabled tools.

Using Kinsta SAML SSO, you can connect Okta to MyKinsta by creating a SAML application within Okta, verifying your company’s email domain, and adding the required Okta details in MyKinsta. This allows your team to log in with their existing company credentials, eliminating the need to create or manage separate MyKinsta accounts.

## Enable SSO in MyKinsta

When you set up SAML SSO, you can click **Save and exit setup** at any stage to store your progress and return later.

In MyKinsta, go to your ***username*** > **Company settings** > **Single sign-on**, and click **Enable**.

![Enable SSO in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-saml-sso-enable.png)

Enable SSO in MyKinsta.

Read through the introduction, which explains how SSO will be set up, and click **Continue**.

![Introduction to the steps required to set up SSO.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-sso-intro.png)

Introduction to the steps required to set up SSO.

The next page provides all the information you need to set up your SAML app within Okta.

## Set up the app integration in Okta

In MyKinsta, the **Create SAML app** tab provides all the information you need to set up your SAML app within Okta. The following steps explain where to add this information.

![Information to create the SAML app at Okta.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-create-saml-app.png)

Information to create the SAML app at Okta.

Log in to Okta as a user with admin access, and within the Admin Dashboard, click **Applications** > **Create App Integration**.

![Create the app integration within Okta.](https://kinsta.com/wp-content/uploads/2025/09/okta-create-ap-integration.png)

Create the app integration within Okta.

Select **SAML 2.0** as the sign-in method and click **Next**.

![Select SAML 2.0 as the sign-in method in Okta.](https://kinsta.com/wp-content/uploads/2025/09/okta-app-saml-2.png)

Select SAML 2.0 as the sign-in method in Okta.

Enter the **App name** from MyKinsta. You can also download the **App icon** from MyKinsta and upload this to the **App logo**, if required. Click **Next**.

![Enter the SAML app name in Okta.](https://kinsta.com/wp-content/uploads/2025/09/okta-app-name-1.png)

Enter the SAML app name in Okta.

Complete the **Configure SAML** in Okta as follows:

- **Single sign-on URL:** Copy and paste the **SSO/ACS URL** from MyKinsta.
- **Audience URI (SP Entity ID):** Copy and paste the **Entity ID** from MyKinsta.
- **Name ID format:** EmailAddress
- **Application username:** Email
- **Update application username on:** Create and update

Leave all other fields as default and click **Next**.

![Configure your SAML app in Okta.](https://kinsta.com/wp-content/uploads/2025/09/okta-configure-saml.png)

Configure your SAML app in Okta.

On the **Feedback** tab, select **This is an internal app that we have created** and then click **Finish**.

![Finish setting up the app integration in Okta.](https://kinsta.com/wp-content/uploads/2025/09/okta-feedback-finish.png)

Finish setting up the app integration in Okta.

You now need to set up the SAML app within MyKinsta.

## Map your Okta attributes

Within Okta, you must map the firstName, lastName, and email attributes from MyKinsta to the correct fields within Okta. For more information about how to do this, refer to the [Okta docs](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-map-attributes.htm).

## Assign users to the Okta app

In Okta, go to **Applications**, select the application you set up for the MyKinsta Dashboard, and click **Assignments**.

![Okta assignments.](https://kinsta.com/wp-content/uploads/2025/09/okta-assignments.png)

Okta assignments.

Click **Assign** and then click **Assign to People**. If you have your users set up in groups, click **Assign to Groups**. Click **Assign** on each user or group you want to assign to the Kinsta SAML SSO application and then click **Done**.

To test authentication, make sure the MyKinsta user account you’re signed in with is assigned.

![Assign users to the MyKinsta SAML application in Okta.](https://kinsta.com/wp-content/uploads/2025/09/okta-assign-users.png)

Assign users to the MyKinsta SAML application in Okta.

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

In Okta, go to **Applications**, select the application you set up for the MyKinsta Dashboard, click **Sign On**, and then click **View SAML setup instructions**.

![View SAML setup instructions within Okta.](https://kinsta.com/wp-content/uploads/2025/09/okta-sign-on-details-1.png)

View SAML setup instructions within Okta.

This page provides all the information you need to set up SAML in MyKinsta.

![SAML configuration details in Okta.](https://kinsta.com/wp-content/uploads/2025/09/okta-saml-details-1.png)

SAML configuration details in Okta.

In MyKinsta, within the Single sign-on **Kinsta setup** tab, complete the fields as follows:

- **SSO URL:** Copy and paste the **Identity Provider Single Sign-On URL** from Okta.
- **Entity ID:** Copy and paste the **Identity Provider Issuer** from Okta.
- **Public certificate:** Copy and paste the **X.509 Certificate** from Okta.

Click **Continue**.

![Enter the required information from the IdP to set up Kinsta SAML.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-saml-okta-kinsta-setup.png)

Enter the required information from the IdP to set up Kinsta SAML.

## Test the authentication in MyKinsta

You cannot enable SAML SSO within MyKinsta without first testing the authentication.

In MyKinsta, within the Single sign-on **Test and finish** tab, click **Test authentication**.

![Test the SAML authentication within MyKinsta.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-saml-test-authentication.png)

Test the SAML authentication within MyKinsta.

A notification appears if the test was successful or if the test fails.

If the test fails, click **Back** and check your SAML settings within Okta and within MyKinsta.

If the test is successful and you want to enable SAML, click **Save and set changes live**.

Your MyKinsta company users will now be able to sign in with SAML SSO or by entering their username and password. Users who sign in through an IdP are not required to complete Kinsta’s 2FA, as authentication is handled directly by the IdP.

If you want to force users to sign on via SAML, you can enable [Mandatory SSO](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#mandatory-single-sign-on) and add [Exceptions](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#exceptions). You can also enable [JIT provisioning](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#just-in-time-provisioning) to allow users authorized by your IdP to access your MyKinsta company without requiring an invitation.

![Sign in to MyKinsta with SAML SSO.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-sign-on-saml-sso.png)

Sign in to MyKinsta with SAML SSO.

## Change the session duration

Your Identity Provider (IdP) determines how long your SSO session remains active and when it expires. If your IdP doesn’t specify a session duration, MyKinsta defaults to a 24-hour session.

When your SSO session expires, you’ll be logged out of SSO. If you’re working within a company that uses SSO, you’ll be prompted to reauthenticate. If you have access to multiple companies in MyKinsta, you’ll remain logged in overall but will need to reauthenticate before accessing any company that requires SSO.

For details on adjusting session duration, refer to the [Okta Help Center](https://support.okta.com/help/s/article/How-to-Adjust-Session-Lifetime-and-Idle-Value-for-Users?language=en_US).
