---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrate-guru/"
title: "Migrate Guru"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-migrations"
section: ["WordPress Hosting", "Migrations"]
kinsta_last_updated: "2026-04-20T15:04:44"
change_signal: "2026-04-20T15:04:44"
fetched_at: "2026-10-07T22:58:21Z"
sha256: "7da38478623ce18ce8f0a614284e1e7939d94a3a522b277d82fce224446a6aba"
body_chars: 5101
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Migrate Guru

**Section:** WordPress Hosting > Migrations
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrate-guru/
**Kinsta last updated:** 2026-04-20T15:04:44

## On this page

- [Add a site in MyKinsta](#add-a-site-in-mykinsta)
- [Install Migrate Guru on both sites](#install-migrate-guru-on-both-sites)
- [Copy the migration key](#copy-the-migration-key)
- [Initiate the migration](#initiate-the-migration)
- [Test the migrated site and go live](#test-the-migrated-site-and-go-live)

---

[Migrate Guru](https://wordpress.org/plugins/migrate-guru/) is a free plugin available from WordPress.org. It is relatively easy to use, works well even with larger WordPress sites, and is compatible with Kinsta.

This guide is provided to help you perform your own migration. However, please note that Migrate Guru may not be fully compatible with some WordPress sites. Our Support team is always happy to help with basic migration questions, but cannot assist with failed migrations, as this falls outside of the [scope of our support](https://kinsta.com/docs/support/scope-of-support/managed-wordpress-scope-of-support/).

**Kinsta migrations are free**, if you’re at all worried about the integrity of your data, we highly recommend [using our professional Migrations team](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrating-to-kinsta/).

## Add a site in MyKinsta

Once you’ve signed up for a Kinsta hosting plan, to use Migrate Guru, you’ll need to [add a site in MyKinsta](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/new-site/).

When creating the site, be sure to select the **Install WordPress** option.

![Create a site in MyKinsta and install WordPress.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-add-site-install-wordpress.png)

Create a site in MyKinsta and install WordPress.

While your new site is being created, you can move on to the next steps.

## Install Migrate Guru on both sites

1. While the site is being created in MyKinsta, go to your existing website (the one you want to migrate) and log in to the WordPress Admin area.
2. Navigate to **Plugins** > **Add New**, and then search for **Migrate Guru**.

   ![Install Migrate Guru from the WordPress repository.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-install-migrate-guru.png)

   Install Migrate Guru from the WordPress repository.
3. Once you locate the plugin, click **Install Now** to install it and then **Activate** to activate the plugin.
4. In MyKinsta, go to your new site, click **Log in to WP Admin**, and repeat steps 2 and 3 to install and activate the Migrate Guru plugin on your new site.

## Copy the migration key

In your new MyKinsta site, click **Log in to WP Admin**, select **Migrate Guru**, click **Copy Key**, and then **Copy Key** again.

![Copy Key in Migrate Guru on your new site. ](https://kinsta.com/wp-content/uploads/2023/11/wordpress-migrate-guru-copy-key.png)

Copy Key in Migrate Guru on your new site.

## Initiate the migration

1. Go back to your existing site that you want to migrate to MyKinsta, and within WP Admin, select **Migrate Guru**.
2. In step 1, click **Yes, I’ve installed it**.

   ![Step 1: confirm you've installed the plugin on both sites in Migrate Guru.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-migrate-guru-step-1-1.png)

   Step 1: Confirm you’ve installed the plugin on both sites in Migrate Guru.
3. In step 2, paste the key you copied from your new site, and click **Validate Key**.

   ![Step 2: validate your key in Migrate Guru.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-migrate-guru-step-2.png)

   Step 2: Validate your key in Migrate Guru.
4. In step 3, enter your email address, confirm the sites are correct for migrating from and to, and click **Initiate Migration**.

   ![Step 3: Initiate the migration in Migrate Guru. ](https://kinsta.com/wp-content/uploads/2023/11/wordpress-migrate-guru-step-3.png)

   Step 3: Initiate the migration in Migrate Guru.
5. Migrate Guru will then redirect you to their BlogVault page, which shows you the migration progress.

   ![Migration progress.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-migrate-guru-progress.png)

   Migration progress.
6. Once the migration is complete you can [test the migrated site and go live](#test-the-migrated-site-and-go-live).

## Test the migrated site and go live

To test and preview your site using the [Site Preview tool](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/site-preview/):

1. Log in to MyKinsta, and go to **WordPress sites** > ***sitename*** > **Tools**.
2. On **Site Preview**, click **Enable**, enter your live domain, and select how long you’d like the preview enabled (1, 4, 8, or 24 hours).

You’ll then be able to access and test the site as if it were live.

Take time to verify your content, functionality, and any eCommerce or membership features (for example, stores using WooCommerce). Don’t update your DNS until you’ve fully tested everything.

Once you’re confident the site is working correctly, [update your domain’s DNS records](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/) to point to Kinsta. Follow the [Go Live Checklist](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/go-live-checklist/) to help ensure nothing is missed.

After [DNS propagation](https://kinsta.com/blog/dns-propagation/) is complete, visitors will be routed to your site on Kinsta. Only cancel your previous hosting once you’ve confirmed the site is loading correctly from Kinsta.
