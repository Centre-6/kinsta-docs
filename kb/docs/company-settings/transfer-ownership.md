---
url: "https://kinsta.com/docs/company-settings/transfer-ownership/"
title: "Company Settings - Transfer Ownership"
tier: "docs"
product: "company-settings"
product_label: "MyKinsta Company Settings"
subsection: "transfer-ownership"
section: []
kinsta_last_updated: "October 1, 2025"
sitemap_lastmod: "2025-10-01T11:31:07+00:00"
fetched_at: "2026-10-07T22:37:34Z"
sha256: "ae6804b7f8d78e296b84f4d153f269453db3cb8c4e8d6ccb6d0c70a82d7e2ba1"
body_chars: 12477
extracted_with: "main article"
status: "live"
---

# Company Settings - Transfer Ownership

**Product:** MyKinsta Company Settings
**Source:** https://kinsta.com/docs/company-settings/transfer-ownership/
**Kinsta last updated:** October 1, 2025

## On this page

- [Transfer company ownership](#transfer-company-ownership)
  - [Important notes](#important-notes)
  - [Transfer ownership](#transfer-ownership)
- [Transfer a site to another company](#transfer-a-site-to-another-company)
  - [Important notes](#important-notes)
  - [1. Find the company ID or email address of the destination company](#1-find-the-company-id-or-email-address-of-the-destination-company)
  - [2. Initiate the site transfer as the source company](#2-initiate-the-site-transfer-as-the-source-company)
  - [3. Finalize the site transfer with the destination company](#3-finalize-the-site-transfer-with-the-destination-company)
    - [No Kinsta account, no plan recommended](#no-kinsta-account-no-plan-recommended)
    - [No Kinsta account, plan recommended](#no-kinsta-account-plan-recommended)
    - [Kinsta account with multiple companies](#kinsta-account-with-multiple-companies)
    - [Accepting the transfer in MyKinsta](#accepting-the-transfer-in-mykinsta)

---

In MyKinsta, we’ve made it as easy as possible to transfer company ownership from one user to another within **Users** and to move a site from your company account to another company with our site transfer tool.

## Transfer company ownership

With our multi-user feature, you can create and manage a team, giving them access to various aspects of your WordPress sites. As mentioned in our [how user roles work](https://kinsta.com/docs/company-settings/user-management/) article, there is a special role: the **Company Owner**.

This role is exactly the same as a **Company Administrator** in all but one respect; only **Company Owners** can close down an account or transfer company ownership (to a **Company Administrator** in the same account). Each company can have only one owner, but it is possible to transfer ownership between users.

### Important notes

- **Only the Company Owner can initiate a company transfer.** You must be logged into MyKinsta as the Company Owner to transfer a **company**.
- **The recipient must be a Company Administrator.** The user you’re transferring the company to must have the Company Administrator role in their MyKinsta account.
- **All site data and settings will be retained.** When you transfer a company, you are changing the owner, not the sites; therefore, all of the sites and data within MyKinsta will remain as they are**.**

### Transfer ownership

Log in to [MyKinsta](https://my.kinsta.com)[,](https://my.kinsta.com) then from the **Dashboard**, click **Company settings**, then **Users**. Click **Transfer ownership** on the right-hand side of your user’s row.

In the modal/pop-up that appears, select an available **Company Administrator** in the **New Owner** dropdown. Enter your password and click **Confirm** to transfer ownership.

![Transfer company ownership.](https://kinsta.com/wp-content/uploads/2023/11/transfer-ownership-1024x513.png)

Transfer company ownership.

## Transfer a site to another company

There are several reasons why you may need to transfer a site to another company:

1. You’re a WordPress agency that needs to hand off a site to a client’s personal Kinsta account.
2. You’re a business owner who wants to transfer a site to a WordPress management company for [routine maintenance](https://kinsta.com/blog/wordpress-maintenance/).
3. You’re moving on to another project and want to transfer your site to a third party.

To transfer any sites under [your company in MyKinsta](https://kinsta.com/blog/manage-users-hosting-account/) to another company’s account, follow the steps below.

### Important notes

- **Company Owners and Company Administrators can initiate a site transfer.** You must be logged into MyKinsta as the Company Owner or Company Administrator to transfer a **site**.
- **The recipient must be a Company Owner or Company Administrator.** The user you’re transferring the site to must have the Company Owner or Company Administrator role in their MyKinsta account.
- **All site data and settings will be transferred.** This includes:
  - SSH/SFTP settings
  - Caching configuration
  - Enabled features
  - SSL certificates
  - Domain settings
- **DNS records managed in MyKinsta will also be transferred.** If your DNS is managed through MyKinsta, those records will move with the site.
- **PHP, Redis, and Premium staging add-ons are transferred with the site.** Any active PHP, Redis, or Premium staging [add-ons](https://kinsta.com/docs/wordpress-hosting/wordpress-add-ons/) will automatically move to the new company along with the site. All other add-ons are disabled when the site is transferred.
- **PHP performance is preserved during transfer.** If the current site has a higher [PHP memory pool](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/) than what’s included in the destination company’s plan, MyKinsta will automatically apply a PHP performance add-on to match the existing performance. For example, if your site currently uses a 2.5GB PHP memory pool and the new company’s plan includes only 1.5GB, a 1GB PHP memory add-on will be added automatically to preserve the original performance level.

### 1. Find the company ID or email address of the destination company

If you’re transferring the site to someone who already has an account and a Kinsta company, find the company ID or email address of the destination company’s owner or administrator. The company ID can be found in [MyKinsta](https://my.kinsta.com/) under **Company settings** > **Billing details** > **Company ID**. The email addresses of company users can be found under **Users** in MyKinsta.

![Kinsta Company ID in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-billing-company-id.png)

Kinsta Company ID in MyKinsta.

If you do not have MyKinsta access to the destination company or do not know the email address of a company owner or company administrator, you’ll need to get in touch with the company directly to get the company ID or email address.

If you’re transferring the site to someone who doesn’t already have an account with Kinsta, get in touch with them to get the email address they want to use at Kinsta. As part of the transfer, they’ll need to set up an account and company at Kinsta.

### 2. Initiate the site transfer as the source company

The next step is to initiate the site transfer (both live and staging site environments) from the source company, which is your company.

To do this, navigate to **Sites** in MyKinsta, click the kebab (three-dot) menu for the site you wish to transfer, then select the **Transfer** **site** option in the dropdown menu that appears.

![Select Transfer site to begin transferring your site to another company.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-transfer-site-1.png)

Select Transfer site to begin transferring your site to another company.

In the modal/pop-up that appears, enter the email address or company ID. You can also optionally choose a recommended plan for the site you’re transferring and enter your Affiliate ID (if applicable).

If you’re using [Kinsta’s DNS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/) for a domain assigned to the site being transferred, we recommend moving that as well. Under **Transfer domain**, select the relevant domain(s) and click the **Next** button to proceed to the confirmation step.

![Enter the destination company ID and select the domains to transfer.](https://kinsta.com/wp-content/uploads/2023/11/transfer-site-details-1024x823.png)

Enter the destination company ID and select the domains to transfer.

To confirm the site transfer, accept the following prompts:

- The site will be transferred from this company account.
- Transferring this site does not cancel the WordPress Hosting plan. This prompt only appears if the site you are transferring is the only WordPress site on your plan.

Enter the site name and click **Transfer** **site**. Once the site is transferred, you’ll have an open spot in your plan for a new site. If you also want to cancel your WordPress Plan, you can do this from within **Company settings** > **My Plan** > **Cancel plan**; refer to [Cancel WordPress Plan](https://kinsta.com/docs/billing/wordpress-hosting-plans/cancel-wordpress-plan/).

![Click the Transfer site button to confirm your site transfer.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-transfer-site-confirmation-1024x574.png)

Click the Transfer site button to confirm your site transfer.

Next, the destination company will have to confirm the site transfer. In your MyKinsta account (the source company), the site will appear as **Pending transfer** for the company owner and company administrator(s).

![A site pending transfer to another company in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-pending-transfer-1.png)

A site pending transfer to another company in MyKinsta.

**Note:** Until the destination company accepts the site transfer, you can revoke the transfer in **Sites** > ***sitename*** > **Info**.

![Cancel/revoke a site transfer in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-revoke-site-transfer.png)

Cancel/revoke a site transfer in MyKinsta.

### 3. Finalize the site transfer with the destination company

After you’ve initiated the site transfer, the company owner and company administrator(s) of the destination company will receive a notification email.

Here’s how things look on their end, depending on a few factors:

1. If you recommended a plan.
2. If the recipient already has a Kinsta account.
3. If the recipient has more than one company.

#### No Kinsta account, no plan recommended

![Site transfer email with no plan recommended.](https://kinsta.com/wp-content/uploads/2023/11/email-site-transfer-no-account.png)

Site transfer email with no plan recommended.

If no plan is recommended, clicking on the **Register an account** button will take them to the Kinsta plans page, where they can select their plan and then begin the signup process.

![Kinsta Managed WordPress Hosting Pricing page.](https://kinsta.com/wp-content/uploads/2023/11/register-an-account.png)

Kinsta Managed WordPress Hosting Pricing page.

#### No Kinsta account, plan recommended

![Site transfer email with a recommended plan.](https://kinsta.com/wp-content/uploads/2023/11/email-site-transfer-no-account-recommend-plan-1024x859.png)

Site transfer email with a recommended plan.

If a plan is recommended, clicking on the **Register** button will take them to the signup page where they can set up their Kinsta account.

![Kinsta signup page.](https://kinsta.com/wp-content/uploads/2023/11/sign-up-small.png)

Kinsta signup page.

#### Kinsta account with multiple companies

If the accepting user already has a Kinsta account, they have the option to transfer the site to any of their companies or transfer the site to a new company.

![Site transfer email showing multiple companies.](https://kinsta.com/wp-content/uploads/2023/11/email-site-transfer-multiple-companies.png)

Site transfer email showing multiple companies.

Clicking the **Transfer to this company button** will take them to the company’s **WordPress Sites** list in MyKinsta.

#### Accepting the transfer in MyKinsta

The site being transferred will appear as an **Incoming transfer**. Clicking on the site name will give them the option to accept or reject the transfer.

![Incoming site transfer in the destination company’s MyKinsta WordPress Sites list.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-incoming-transfer.png)

Incoming site transfer in the destination company’s MyKinsta WordPress Sites list.

To commit the site transfer they should click on **Commit transfer** in MyKinsta. If they do not want to accept your request, they can dismiss it by clicking on **Reject transfer** instead.

![Commit to the site transfer. ](https://kinsta.com/wp-content/uploads/2023/11/wordpress-commit-transfer-1024x398.png)

Commit to the site transfer.

To accept the transfer after committing to it, they should click **Accept transfer**.

![Accept a site transfer.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-accept-transfer-1024x396.png)

Accept a site transfer.

If the site being transferred includes active [add-ons](https://kinsta.com/docs/wordpress-hosting/wordpress-add-ons/), the receiving company will see which add-ons are active. They must accept the transfer with the add-ons. If the add-ons are no longer needed, they can [cancel them](https://kinsta.com/docs/billing/wordpress-hosting-plans/cancel-wordpress-plan/#other-cancellations-and-deletions) after the transfer is complete.

![Accept a site transfer with add-ons.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-accept-transfer-add-ons.png)

Accept a site transfer with add-ons.

If the destination company’s plan does not have enough sites or KinstaDNS slots to receive the incoming site, they’ll be prompted to upgrade their plan after accepting the transfer.

If they click **Cancel** without rejecting the transfer, they’ll still be able to accept it within 72 hours.

![A plan upgrade may be needed to accommodate a site transfer.](https://kinsta.com/wp-content/uploads/2023/11/accept-transfer-limit-reached-1024x341.png)

A plan upgrade may be needed to accommodate a site transfer.

After the site transfer is accepted, you (the source company’s owner) and any company administrator(s) — will receive a notification email.
