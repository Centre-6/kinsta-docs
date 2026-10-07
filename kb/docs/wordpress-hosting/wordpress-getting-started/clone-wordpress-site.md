---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/clone-wordpress-site/"
title: "Clone a Site"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-getting-started"
section: ["WordPress Hosting", "Get Started"]
kinsta_last_updated: "2025-06-11T15:42:57"
change_signal: "2025-06-11T15:42:57"
fetched_at: "2026-10-07T22:58:21Z"
sha256: "99b0d3cb8e93b95cab5d9e453c833df1c72f0d7eebafd6854525b42280448c57"
body_chars: 3462
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Clone a Site

**Section:** WordPress Hosting > Get Started
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/clone-wordpress-site/
**Kinsta last updated:** 2025-06-11T15:42:57

## On this page

- [Clone your site in MyKinsta](#clone-your-site-in-mykinsta)
- [After cloning](#after-cloning)
- [Important notes](#important-notes)

---

The clone feature in [MyKinsta](https://my.kinsta.com/) copies your entire WordPress site, including the database and files. New SFTP, SSH, and database credentials are automatically created during the process, and you can access those in MyKinsta once the cloned site is created.

To use this feature, you’ll need to be on a Multiple-site plan, and you’ll need to have at least one unused space open/available on your plan for the new site. If you do not have an unused space to clone your site, you can clone it to a [Premium Staging Environment](https://kinsta.com/docs/wordpress-hosting/staging-environment/#premium-staging-environments).

## Clone your site in MyKinsta

1. Log in to [MyKinsta](https://my.kinsta.com/), click on **Sites** > **Add site** > **Create new site**.

   ![Create a WordPress site in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-add-site-5.png)

   Create a WordPress site in MyKinsta.
2. On the **Add site** page, select **Clone** and click **Continue**.

   ![Clone an existing environment in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-add-site-clone.png)

   Clone an existing environment in MyKinsta.
3. Select the site you want to clone and either the **Live** or **Staging** environment. Enter a name for the new site and click **Continue**.  

   ![Next step in cloning an existing environment in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-clone-environment.png)

   Next step in cloning an existing environment in MyKinsta.

Depending on the size of your site, the cloning process usually takes about 10-20 minutes to complete. Once it’s complete, your newly cloned site will be in your **Sites** list.

If the process doesn’t complete after an hour, open a chat with our [Support team](https://kinsta.com/docs/support/contact-support/) so they can examine the cloning process and resolve that delay.

## After cloning

If you didn’t add a custom domain during the cloning process, you can use the site’s [temporary URL](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-temporary-url/) to access it until you’re ready to add a custom domain.

When you’re ready to add your site’s custom domain and go live, check out our [Add a Domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/) guide and [Go Live Checklist](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/go-live-checklist/).

## Important notes

- Hardcoded URLs in files will need to be updated with the new site URL.
- If URLs stored in plugin or theme settings were not automatically updated with the automatic search and replace during the cloning process, they will also need to be updated.
- If themes or plugins have built-in cache, that will need to be cleared.
- [SSH keys](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/#how-to-connect-to-ssh-with-ssh-keys) are retained when a site is cloned as these are stored in your **User settings**.
- Your cloned site is completely separate from the original site. It counts against your plan’s total number of sites, visits, and bandwidth (if applicable).
- If social sharing plugins like CoSchedule or Social Networks Auto Poster are active on your site, they may automatically begin sharing content from the cloned site. Be sure any URLs related to those are updated, or deactivate the plugin(s) until your new site is live and you’re ready to use them.
