---
url: "https://kinsta.com/docs/company-settings/wordpress-saml-sso/google-workspace-saml-sso/"
title: "Google Workspace SAML SSO"
tier: "docs"
product: "company-settings"
product_label: "MyKinsta Company Settings"
subsection: "wordpress-saml-sso"
section: ["Company Settings", "SAML Single Sign-On (SSO)"]
kinsta_last_updated: "2026-01-16T15:21:11"
change_signal: "2026-01-16T15:21:11"
fetched_at: "2026-10-07T22:58:17Z"
sha256: "d72c639f582e3db86982bd62e4a5cb25148158bb143d9c2a3cf3ef38eae2fe7a"
body_chars: 10158
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Google Workspace SAML SSO

**Section:** Company Settings > SAML Single Sign-On (SSO)
**Product:** MyKinsta Company Settings
**Source:** https://kinsta.com/docs/company-settings/wordpress-saml-sso/google-workspace-saml-sso/
**Kinsta last updated:** 2026-01-16T15:21:11

## On this page

- [Enable SSO in MyKinsta](#enable-sso-in-mykinsta)
- [Create the app in Google Workspace](#create-the-app-in-google-workspace)
- [Kinsta setup](#kinsta-setup)
  - [Email domain](#email-domain)
  - [Set up Kinsta SAML](#set-up-kinsta-saml)
- [Add the service provider details in Google Workspace](#add-the-service-provider-details-in-google-workspace)
- [Map your Google Workspace attributes](#map-your-google-workspace-attributes)
- [Set up user access to the Google Workspace app](#set-up-user-access-to-the-google-workspace-app)
- [Test the authentication in MyKinsta](#test-the-authentication-in-mykinsta)
- [Change the session duration](#change-the-session-duration)

---

Google Workspace is an Identity Provider (IdP) that enables secure single sign-on (SSO), allowing your company’s users to access multiple applications with one login.

With Security Assertion Markup Language (SAML) SSO, employees sign in once using their company credentials (typically email and password). The IdP, such as Google Workspace, verifies their identity and grants seamless, secure access to all connected services, without requiring separate logins for each application.

Company owners or IT administrators can link their organization’s email domain (e.g., @mycompany.com) to the IdP so that anyone with a company email address is automatically recognized and can securely sign in to SAML-enabled tools.

Using Kinsta SAML SSO, you can connect Google Workspace to MyKinsta by creating a SAML application within Google Workspace, verifying your company’s email domain, and adding the required Google Workspace details in MyKinsta. This allows your team to log in with their existing company credentials, eliminating the need to create or manage separate MyKinsta accounts.

## Enable SSO in MyKinsta

When you set up SAML SSO, you can click **Save and exit setup** at any stage to store your progress and return later.

In MyKinsta, go to your ***username*** > **Company settings** > **Single sign-on**, and click **Enable**.

![Enable SSO in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-saml-sso-enable.png)

Enable SSO in MyKinsta.

Read through the introduction, which explains how SSO will be set up, and click **Continue**.

![Introduction to the steps required to set up SSO.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-sso-intro.png)

Introduction to the steps required to set up SSO.

The next page provides all the information you need to set up your SAML app within Google Workspace.

## Create the app in Google Workspace

In MyKinsta, the **Create SAML app** tab provides all the information you need to set up your SAML app within Google Workspace. The following steps explain where to add this information.

![Information to create the SAML app at Google Workspace.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-create-saml-app.png)

Information to create the SAML app at Google Workspace.

Log in to Google Workspace as a user with admin access, open the **Google Apps** menu, and select the **Admin** app.

![Open the Admin app in Google.](https://kinsta.com/wp-content/uploads/2025/10/saml-sso-google-admin.png)

Open the Admin app in Google.

Select **Web and mobile apps**, and then click **Add app** > **Add custom SAML app**.

![Add a custom SAML app in Google. ](https://kinsta.com/wp-content/uploads/2025/10/saml-sso-google-add-saml-app.png)

Add a custom SAML app in Google.

In the **App name**, enter the **App name** from MyKinsta. You can also download the **App icon** from MyKinsta and upload this to the **App Icon**, and add a **Description** if required. Click **Continue**.

![Enter the app details in Google. ](https://kinsta.com/wp-content/uploads/2025/10/saml-sso-google-app-details.png)

Enter the app details in Google.

## Kinsta setup

In MyKinsta, on **Create SAML app**, click **Continue** so that you are on the **Kinsta setup** page. We will return to the **Create SAML app** tab in the next step when adding the service provider details to Google Workspace.

### Email domain

In the **Domain name**, enter the email domain users will use to sign in using SAML SSO, and click **Add domain**.

Only MyKinsta accounts with an email address matching the verified domain can authenticate via SAML. For example, if SAML is enabled for `example.com`, only users with an `@example.com` email address will be able to sign in for that company.

If the domain has already been verified in MyKinsta through DNS management or as a site domain, it will automatically be verified. If it hasn’t, you’ll be prompted to add a TXT record to your DNS management service to confirm domain ownership.

![Add the TXT record to your DNS to verify ownership.](https://kinsta.com/wp-content/uploads/2025/09/kinsta-verify-domain-saml.png)

Add the TXT record to your DNS to verify ownership.

Because DNS changes can take time to propagate, you can click **Save and exit setup** to store your progress and return later.

### Set up Kinsta SAML

In Google Workspace, the **Google Identity Provider details** tab provides all the information you need to set up SAML in MyKinsta.

![Google Identity Provider details to set up the Kinsta app. ](https://kinsta.com/wp-content/uploads/2025/10/saml-sso-google-idp-details.png)

Google Identity Provider details to set up the Kinsta app.

In MyKinsta, within the Single sign-on **Kinsta setup** tab, complete the fields as follows:

- **SSO URL:** Copy and paste the **SSO URL** from Google Workspace.
- **Entity ID:** Copy and paste the **Entity ID** from Google Workspace.
- **Public certificate:** Copy and paste the contents of the **Certificate** from Google Workspace.

Click **Save and exit setup**.

![Enter the required information from the IdP to set up Kinsta SAML.](https://kinsta.com/wp-content/uploads/2025/10/saml-sso-kinsta-setup-google.png)

Enter the required information from the IdP to set up Kinsta SAML.

## Add the service provider details in Google Workspace

In MyKinsta, within **Single sign-on**, click **Enable** again, and then click **Continue** so you are on the **Create SAML app** tab.

Within Google Workspace, click **Continue** to the **Service provider details** tab and complete as follows:

- **ACS URL:**Copy and paste the **SSO/ACS URL** from MyKinsta.
- **Entity ID:** Copy and paste the **Entity ID** from MyKinsta.
- **Start URL:** Copy and paste the **Start URL** from MyKinsta.
- **Signed response:** Select this option.
- **Name ID format:** EMAIL.
- **Name ID:** Basic Information > Primary email.

Click **Continue**.

![Enter the service provider details from MyKinsta into Google. ](https://kinsta.com/wp-content/uploads/2025/10/saml-sso-google-service-provider-details.png)

Enter the service provider details from MyKinsta into Google.

## Map your Google Workspace attributes

Within **Attribute mapping**, you can add the first name, last name, and email to the login credentials. Complete these as follows, and click **ADD MAPPING** after each entry:

| Google directory attributes | App attributes |
| --- | --- |
| First name | firstName |
| Last name | lastName |
| Primary email | email |

Click **Finish**.

![Map the first name, last name, and email in Google to the MyKinsta fields.](https://kinsta.com/wp-content/uploads/2025/10/saml-sso-google-attribute-mapping.png)

Map the first name, last name, and email in Google to the MyKinsta fields.

## Set up user access to the Google Workspace app

In Google Workspace, in the Admin app, go to **Apps** > **Web and mobile apps**, select the MyKinsta application, and click **User access**.

![Select User access on the MyKinsta application in Google Workspace.](https://kinsta.com/wp-content/uploads/2025/10/saml-sso-google-user-access.png)

Select User access on the MyKinsta application in Google Workspace.

Select the **Group(s)** or **Organisational unit(s)** you want to grant access to MyKinsta via SAML. Then select **ON** or **ON for everyone** and click **SAVE**. For more information about Groups and Organisational units, refer to [Google Workspace Admin Help](https://support.google.com/a?sjid=10187148707879574500-EU#topic=4388346).

![Select the Group(s) or Organisational unit(s) you want to grant access to MyKinsta via SAML.](https://kinsta.com/wp-content/uploads/2025/10/saml-sso-google-change-user-access.png)

Select the Group(s) or Organisational unit(s) you want to grant access to MyKinsta via SAML.

To test authentication, make sure the MyKinsta user account you’re signed in with is assigned.

## Test the authentication in MyKinsta

You cannot enable SAML SSO within MyKinsta without first testing the authentication.

In MyKinsta, within Single sign-on, click **Continue** until you are on the **Test and finish** tab, and click **Test authentication**.

![Test the SAML authentication within MyKinsta.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-saml-test-authentication.png)

Test the SAML authentication within MyKinsta.

A notification appears if the test was successful or if the test fails.

If the test fails, click **Back** and check your SAML settings within Google Workspace and within MyKinsta.

If the test is successful and you want to enable SAML, click **Save and set changes live**.

Your MyKinsta company users will now be able to sign in with SAML SSO or by entering their username and password. Users who sign in through an IdP are not required to complete Kinsta’s 2FA, as authentication is handled directly by the IdP.

If you want to force users to sign on via SAML, you can enable [Mandatory SSO](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#mandatory-single-sign-on) and add [Exceptions](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#exceptions). You can also enable [JIT provisioning](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#just-in-time-provisioning) to allow users authorized by your IdP to access your MyKinsta company without requiring an invitation.

![Sign in to MyKinsta with SAML SSO.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-sign-on-saml-sso.png)

Sign in to MyKinsta with SAML SSO.

## Change the session duration

Your Identity Provider (IdP) determines how long your SSO session remains active and when it expires. If your IdP doesn’t specify a session duration, MyKinsta defaults to a 24-hour session.

When your SSO session expires, you’ll be logged out of SSO. If you’re working within a company that uses SSO, you’ll be prompted to reauthenticate. If you have access to multiple companies in MyKinsta, you’ll remain logged in overall but will need to reauthenticate before accessing any company that requires SSO.

For details on adjusting session duration, refer to the [Google Workspace Admin Help](https://support.google.com/a/answer/7576830?sjid=15638353417037270933-EU).
