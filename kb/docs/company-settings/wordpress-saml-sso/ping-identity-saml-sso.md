---
url: "https://kinsta.com/docs/company-settings/wordpress-saml-sso/ping-identity-saml-sso/"
title: "Ping Identity SAML SSO"
tier: "docs"
product: "company-settings"
product_label: "MyKinsta Company Settings"
subsection: "wordpress-saml-sso"
section: ["Company Settings", "SAML Single Sign-On (SSO)"]
kinsta_last_updated: "2025-11-14T17:52:41"
change_signal: "2025-11-14T17:52:41"
fetched_at: "2026-10-07T22:58:17Z"
sha256: "cb3dd236593aa883b6cd450a18adb7bf4a3286226a08dc9dd1d5c2405fb2c9e6"
body_chars: 9692
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Ping Identity SAML SSO

**Section:** Company Settings > SAML Single Sign-On (SSO)
**Product:** MyKinsta Company Settings
**Source:** https://kinsta.com/docs/company-settings/wordpress-saml-sso/ping-identity-saml-sso/
**Kinsta last updated:** 2025-11-14T17:52:41

## On this page

- [Enable SSO in MyKinsta](#enable-sso-in-mykinsta)
- [Set up the app integration in Ping Identity](#set-up-the-app-integration-in-ping-identity)
- [Map your Ping Identity attributes](#map-your-ping-identity-attributes)
- [Assign user access in Ping Identity](#assign-user-access-in-ping-identity)
- [Kinsta setup](#kinsta-setup)
  - [Email domain](#email-domain)
  - [Set up Kinsta SAML](#set-up-kinsta-saml)
- [Test the authentication in MyKinsta](#test-the-authentication-in-mykinsta)
- [Change the session duration](#change-the-session-duration)

---

[Ping Identity](https://www.pingidentity.com/en.html) is an Identity Provider (IdP) that enables secure single sign-on (SSO), allowing your company’s users to access multiple applications with one login.

With Security Assertion Markup Language (SAML) SSO, employees sign in once using their company credentials (typically email and password). The IdP, such as Ping Identity, verifies their identity and grants seamless, secure access to all connected services, without requiring separate logins for each application.

Company owners or IT administrators can link their organization’s email domain (e.g., @mycompany.com) to the IdP so that anyone with a company email address is automatically recognized and can securely sign in to SAML-enabled tools.

Using Kinsta SAML SSO, you can connect Ping Identity to MyKinsta by creating a SAML application within Ping Identity, verifying your company’s email domain, and adding the required Ping Identity details in MyKinsta. This allows your team to log in with their existing company credentials, eliminating the need to create or manage separate MyKinsta accounts.

## Enable SSO in MyKinsta

When you set up SAML SSO, you can click **Save and exit setup** at any stage to store your progress and return later.

In MyKinsta, go to your ***username*** > **Company settings** > **Single sign-on**, and click **Enable**.

![Enable SSO in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-saml-sso-enable.png)

Enable SSO in MyKinsta.

Read through the introduction, which explains how SSO will be set up, and click **Continue**.

![Introduction to the steps required to set up SSO.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-sso-intro.png)

Introduction to the steps required to set up SSO.

The next page provides all the information you need to set up your SAML app within Ping Identity.

## Set up the app integration in Ping Identity

In MyKinsta, the **Create SAML app** tab provides all the information you need to set up your SAML app within Ping Identity. The following steps explain where to add this information.

![Information to create the SAML app at Ping Identity.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-create-saml-app.png)

Information to create the SAML app at Ping Identity.

Log in to Ping Identity as a user with admin access, and within **Environments**, click **Create Environment**.

![Create an environment within Ping Identity. ](https://kinsta.com/wp-content/uploads/2025/11/ping-create-environment.png)

Create an environment within Ping Identity.

Click **Create a Workforce Solution** and then click **Manage Environment**.

![Manage your environment in Ping Identity.](https://kinsta.com/wp-content/uploads/2025/11/ping-manage-environment.png)

Manage your environment in Ping Identity.

Click **Applications** and then click the plus sign to add a new application.

![Add an application in Ping Identity.](https://kinsta.com/wp-content/uploads/2025/11/ping-add-app-1.png)

Add an application in Ping Identity.

Enter the **Application name** from MyKinsta. You can also download the **App icon** from MyKinsta and upload it to the **Icon**, if required. Select **SAML Application** and click **Configure**.

![Application details in Ping Identity.](https://kinsta.com/wp-content/uploads/2025/11/ping-application-details.png)

Application details in Ping Identity.

Select **Manually Enter** and complete the **SAML Configuration** in Ping Identity as follows:

- **ACS URLs:** Copy and paste the **SSO/ACS URL** from MyKinsta.
- **Entity ID:** Copy and paste the **Entity ID** from MyKinsta.

Click **Save**.

![SAML Configuration in Ping Identity.](https://kinsta.com/wp-content/uploads/2025/11/ping-saml-configuration.png)

SAML Configuration in Ping Identity.

## Map your Ping Identity attributes

Click **Attribute Mappings** and then click the edit icon.

![Edit the attribute mappings in Ping Identity.](https://kinsta.com/wp-content/uploads/2025/11/ping-attribute-mappings.png)

Edit the attribute mappings in Ping Identity.

Add the following attributes:

| Attributes | PingOne Mappings | Required |
| --- | --- | --- |
| firstName | Given Name | Selected |
| lastname | Family Name | Selected |
| email | Email Address | Selected |

Click **Save**.

![Map the required attributes in Ping Identity.](https://kinsta.com/wp-content/uploads/2025/11/ping-edit-attribute-mappings.png)

Map the required attributes in Ping Identity.

## Assign user access in Ping Identity

By default, the new application will allow all users to access it. To define specific user groups for access to this, in Ping Identity, navigate to **Applications**, select the application you set up for the MyKinsta Dashboard, click **Access**, and then click the edit icon. You can choose whether you want only admin users to access the application or select which groups should have access.

![Assign user groups to the application in Ping Identity.](https://kinsta.com/wp-content/uploads/2025/11/ping-assign-user-access.png)

Assign user groups to the application in Ping Identity.

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

In Ping Identity, go to **Applications**, select the application you set up for the MyKinsta Dashboard, click **Overview**, and then scroll down to **Connection Details**.

This page provides all the information you need to set up SAML in MyKinsta.

![Connection details in Ping Identity.](https://kinsta.com/wp-content/uploads/2025/11/ping-connection-details.png)

Connection details in Ping Identity.

In MyKinsta, within the Single sign-on **Kinsta setup** tab, complete the fields as follows:

- **SSO URL:** Copy and paste the **Initiate Single Sign-On URL** from Ping Identity.
- **Entity ID:** Copy and paste the **Issuer ID** from Ping Identity.
- **Public certificate:** Within Ping Identity, click **Download Signing Certificate**, select **X509 PEM (.crt)**. Open this file in any text editor, and copy and paste the contents into MyKinsta.

Click **Continue**.

![Enter the required information from the IdP to set up Kinsta SAML.](https://kinsta.com/wp-content/uploads/2025/11/mykinsta-saml-config-ping.png)

Enter the required information from the IdP to set up Kinsta SAML.

## Test the authentication in MyKinsta

You cannot enable SAML SSO within MyKinsta without first testing the authentication.

In MyKinsta, within the Single sign-on **Test and finish** tab, click **Test authentication**.

![Test the SAML authentication within MyKinsta.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-saml-test-authentication.png)

Test the SAML authentication within MyKinsta.

A notification appears if the test was successful or if the test fails.

If the test fails, click **Back** and check your SAML settings within Ping Identity and within MyKinsta.

If the test is successful and you want to enable SAML, click **Save and set changes live**.

Your MyKinsta company users will now be able to sign in with SAML SSO or by entering their username and password. Users who sign in through an IdP are not required to complete Kinsta’s 2FA, as authentication is handled directly by the IdP.

If you want to force users to sign on via SAML, you can enable [Mandatory SSO](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#mandatory-single-sign-on) and add [Exceptions](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#exceptions). You can also enable [JIT provisioning](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#just-in-time-provisioning) to allow users authorized by your IdP to access your MyKinsta company without requiring an invitation.

![Sign in to MyKinsta with SAML SSO.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-sign-on-saml-sso.png)

Sign in to MyKinsta with SAML SSO.

## Change the session duration

Your Identity Provider (IdP) determines how long your SSO session remains active and when it expires. If your IdP doesn’t specify a session duration, MyKinsta defaults to a 24-hour session.

When your SSO session expires, you’ll be logged out of SSO. If you’re working within a company that uses SSO, you’ll be prompted to reauthenticate. If you have access to multiple companies in MyKinsta, you’ll remain logged in overall but will need to reauthenticate before accessing any company that requires SSO.

For details on adjusting session duration, refer to the [Ping Identity documentation](https://docs.pingidentity.com/pingone/directory/p1_manage_user_sessions_intro.html?_gl=1*7iinwk*_gcl_au*MTMwMzMwNjQ5My4xNzYyNTEyOTgy*_ga*MjA5MzYyMDUzMy4xNzYyNTEyOTcx*_ga_V94KKVLZPT*czE3NjI3Nzk4MTQkbzMkZzEkdDE3NjI3Nzk4MjYkajQ4JGwwJGg4MzI3NjA4OA..).
