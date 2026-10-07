---
url: "https://kinsta.com/docs/company-settings/wordpress-saml-sso/microsoft-entra-saml-sso/"
title: "SAML Single Sign-On (SSO) - Microsoft Entra SAML SSO"
tier: "docs"
product: "company-settings"
product_label: "MyKinsta Company Settings"
subsection: "wordpress-saml-sso"
section: []
kinsta_last_updated: "November 14, 2025"
sitemap_lastmod: "2025-11-14T17:50:58+00:00"
fetched_at: "2026-10-07T22:37:44Z"
sha256: "cafb38cb228f63213aea80200c4cc1633b03d373eab258150341edfd96398251"
body_chars: 10269
extracted_with: "main article"
status: "live"
---

# SAML Single Sign-On (SSO) - Microsoft Entra SAML SSO

**Product:** MyKinsta Company Settings
**Source:** https://kinsta.com/docs/company-settings/wordpress-saml-sso/microsoft-entra-saml-sso/
**Kinsta last updated:** November 14, 2025

## On this page

- [Enable SSO in MyKinsta](#enable-sso-in-mykinsta)
- [Set up the app integration in Microsoft Entra](#set-up-the-app-integration-in-microsoft-entra)
- [Map your Microsoft Entra attributes](#map-your-microsoft-entra-attributes)
- [Assign users to the Microsoft Entra app](#assign-users-to-the-microsoft-entra-app)
- [Kinsta setup](#kinsta-setup)
  - [Email domain](#email-domain)
  - [Set up Kinsta SAML](#set-up-kinsta-saml)
- [Test the authentication in MyKinsta](#test-the-authentication-in-mykinsta)
- [Change the session duration](#change-the-session-duration)

---

[Microsoft Entra](https://entra.microsoft.com/) (formerly Azure) is an Identity Provider (IdP) that enables secure single sign-on (SSO), allowing your company’s users to access multiple applications with one login.

With Security Assertion Markup Language (SAML) SSO, employees sign in once using their company credentials (typically email and password). The IdP, such as Microsoft Entra, verifies their identity and grants seamless, secure access to all connected services, without requiring separate logins for each application.

Company owners or IT administrators can link their organization’s email domain (e.g., @mycompany.com) to the IdP so that anyone with a company email address is automatically recognized and can securely sign in to SAML-enabled tools.

Using Kinsta SAML SSO, you can connect Microsoft Entra to MyKinsta by creating a SAML application within Microsoft Entra, verifying your company’s email domain, and adding the required Microsoft Entra details in MyKinsta. This allows your team to log in with their existing company credentials, eliminating the need to create or manage separate MyKinsta accounts.

## Enable SSO in MyKinsta

When you set up SAML SSO, you can click **Save and exit setup** at any stage to store your progress and return later.

In MyKinsta, go to your ***username*** > **Company settings** > **Single sign-on**, and click **Enable**.

![Enable SSO in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-saml-sso-enable.png)

Enable SSO in MyKinsta.

Read through the introduction, which explains how SSO will be set up, and click **Continue**.

![Introduction to the steps required to set up SSO.](https://kinsta.com/wp-content/uploads/2025/08/wordpress-sso-intro.png)

Introduction to the steps required to set up SSO.

The next page provides all the information you need to set up your SAML app within Microsoft Entra.

## Set up the app integration in Microsoft Entra

In MyKinsta, the **Create SAML app** tab provides all the information you need to set up your SAML app within Microsoft Entra. The following steps explain where to add this information.

![Information to create the SAML app at Microsoft Entra.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-create-saml-app.png)

Information to create the SAML app at Microsoft Entra.

Log in to Microsoft Entra as a user with admin access, and within the Microsoft Entra admin center, click **Entra ID** > **Enterprise applications** > **New application**.

![Create a new application in Microsoft Entra.](https://kinsta.com/wp-content/uploads/2025/10/entra-new-sso-app.png)

Create a new application in Microsoft Entra.

Click **Create your own application**, enter a name for your application, for example, MyKinsta Dashboard, and click **Create**.

![Create your own application in Microsoft Entra.](https://kinsta.com/wp-content/uploads/2025/10/entra-sso-create-app.png)

Create your own application in Microsoft Entra.

Once the application is created, click **Single sign-on** and select **SAML**.

![Select SAML as the sign-on method for your Microsoft Entra app.](https://kinsta.com/wp-content/uploads/2025/10/entra-sso-app-saml.png)

Select SAML as the sign-on method for your Microsoft Entra app.

Within **Basic SAML Configuration**, click **Edit**.

![Edit the basic SAML configuration in your Microsoft Entra app.](https://kinsta.com/wp-content/uploads/2025/10/entra-sso-basic-saml-configuration-1.png)

Edit the basic SAML configuration in your Microsoft Entra app.

Complete the **Basic SAML Configuration** in Microsoft Entra as follows:

- **Identifier (Entity ID):** Click **Add identifier** and then copy and paste the **Entity ID** from MyKinsta.
- **Reply URL (Assertion Consumer Service URL):** Click **Add reply URL** and then copy and paste the **SSO/ACS URL** from MyKinsta.
- **Sign on URL:** Copy and paste the **Start URL** from MyKinsta.

Leave all other fields as default and click **Save**.

![Complete the Basic SAML Configuration with the information from MyKinsta.](https://kinsta.com/wp-content/uploads/2025/10/entra-sso-app-configure.png)

Complete the Basic SAML Configuration with the information from MyKinsta.

## Map your Microsoft Entra attributes

Within Microsoft Entra, you must map the firstName, lastName, and email attributes from MyKinsta to the correct fields within Microsoft Entra. For more information about how to do this, refer to the [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/identity-platform/saml-claims-customization).

## Assign users to the Microsoft Entra app

In Microsoft Entra, go to **Enterprise apps**, select the application you set up for the MyKinsta Dashboard, click **Users and groups**, and then click **Add user/group**.

![Add users/groups to the app in Microsoft Entra.](https://kinsta.com/wp-content/uploads/2025/10/entra-sso-add-users.png)

Add users/groups to the app in Microsoft Entra.

Click **None selected**, select the users or groups you want to grant MyKinsta access via SSO, and then click **Select**.

![Select the required users or groups within Microsoft Entra.](https://kinsta.com/wp-content/uploads/2025/10/entra-sso-select-users.png)

Select the required users or groups within Microsoft Entra.

Click **Assign** and then click **Assign to People**. If you have your users set up in groups, click **Assign to Groups**. Click **Assign** on each user or group you want to assign to the Kinsta SAML SSO application and then click **Done**.

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

In Microsoft Entra, go to **Enterprise apps**, select the application you set up for the MyKinsta Dashboard, and click **Single sign-on**.

In MyKinsta, within the Single sign-on **Kinsta setup** tab, complete the fields as follows:

- **SSO URL:** Copy and paste the **Login URL** from the **Set up MyKinsta Dashboard** section in Microsoft Entra.
- **Entity ID:** Copy and paste the **Microsoft Entra Identifier** from the **Set up MyKinsta Dashboard** section in Microsoft Entra.

![Microsoft Entra SSO URL and Entity ID for MyKinsta.](https://kinsta.com/wp-content/uploads/2025/10/entra-sso-set-up-kinsta-app.png)

Microsoft Entra SSO URL and Entity ID for MyKinsta.

- **Public certificate:** In Microsoft Entra, within **SAML Certificates**, click **Download** on **Certificate (Base64)**. Open this file in any text editor, and copy and paste the contents into MyKinsta.

![Download the certificate from Microsoft Entra.](https://kinsta.com/wp-content/uploads/2025/10/entra-sso-set-up-certificate-1.png)

Download the certificate from Microsoft Entra.

Click **Continue**.

![Enter the required information from the IdP to set up Kinsta SAML.](https://kinsta.com/wp-content/uploads/2025/10/wordpress-saml-kinsta-entra.png)

Enter the required information from the IdP to set up Kinsta SAML.

## Test the authentication in MyKinsta

You cannot enable SAML SSO within MyKinsta without first testing the authentication.

In MyKinsta, within the Single sign-on **Test and finish** tab, click **Test authentication**.

![Test the SAML authentication within MyKinsta.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-saml-test-authentication.png)

Test the SAML authentication within MyKinsta.

A notification appears if the test was successful or if the test fails.

If the test fails, click **Back** and check your SAML settings within Microsoft Entra and within MyKinsta.

If the test is successful and you want to enable SAML, click **Save and set changes live**.

Your MyKinsta company users will now be able to sign in with SAML SSO or by entering their username and password. Users who sign in through an IdP are not required to complete Kinsta’s 2FA, as authentication is handled directly by the IdP.

If you want to force users to sign on via SAML, you can enable [Mandatory SSO](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#mandatory-single-sign-on) and add [Exceptions](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#exceptions). You can also enable [JIT provisioning](https://kinsta.com/docs/company-settings/wordpress-saml-sso/#just-in-time-provisioning) to allow users authorized by your IdP to access your MyKinsta company without requiring an invitation.

![Sign in to MyKinsta with SAML SSO.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-sign-on-saml-sso.png)

Sign in to MyKinsta with SAML SSO.

## Change the session duration

Your Identity Provider (IdP) determines how long your SSO session remains active and when it expires. If your IdP doesn’t specify a session duration, MyKinsta defaults to a 24-hour session.

When your SSO session expires, you’ll be logged out of SSO. If you’re working within a company that uses SSO, you’ll be prompted to reauthenticate. If you have access to multiple companies in MyKinsta, you’ll remain logged in overall but will need to reauthenticate before accessing any company that requires SSO.

For details on adjusting session duration, refer to the [Microsoft Entra Documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-session-lifetime).
