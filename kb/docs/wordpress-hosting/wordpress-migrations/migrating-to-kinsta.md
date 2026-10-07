---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrating-to-kinsta/"
title: "Migrations"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-migrations"
section: []
kinsta_last_updated: "April 21, 2026"
sitemap_lastmod: "2026-04-21T09:45:13+00:00"
fetched_at: "2026-10-07T22:40:04Z"
sha256: "4b8fad7acbf0d0588233c2f5baa4e10c5dc601e04fb6a53629d7f2811e01845e"
body_chars: 23773
extracted_with: "main article"
status: "live"
---

# Migrations

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrating-to-kinsta/
**Kinsta last updated:** April 21, 2026

## On this page

- [Migration process](#migration-process)
- [Before you start](#before-you-start)
  - [Who can request a migration](#who-can-request-a-migration)
  - [What to prepare](#what-to-prepare)
  - [Special cases](#special-cases)
    - [eCommerce, membership, and community sites](#ecommerce-membership-and-community-sites)
    - [Bulk migrations](#bulk-migrations)
    - [Multisite network](#multisite-network)
    - [WordPress.com sites](#wordpresscom-sites)
    - [Reverse proxy, WP Engine Large FS, or other complex requirements](#reverse-proxy-wp-engine-large-fs-or-other-complex-requirements)
  - [How to minimize downtime](#how-to-minimize-downtime)
  - [Save and continue your migration request](#save-and-continue-your-migration-request)
- [Request a migration](#request-a-migration)
  - [Choose your timeframe](#choose-your-timeframe)
    - [As soon as possible](#as-soon-as-possible)
    - [On a specific date](#on-a-specific-date)
    - [Expedited migrations](#expedited-migrations)
  - [Choose your migration type](#choose-your-migration-type)
    - [Migrate from another host](#migrate-from-another-host)
  - [Site details](#site-details)
  - [Kinsta settings](#kinsta-settings)
  - [Review and submit](#review-and-submit)
- [After you submit](#after-you-submit)
  - [Malware removal](#malware-removal)
- [What to do when the migration is complete](#what-to-do-when-the-migration-is-complete)

---

When migrating your site to Kinsta, you have a few options to choose from, starting with [migrating the site yourself](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/wordpress-manual-migration/) or having our team do the migration for you.

**Kinsta migrations are free**. You can choose to migrate your site straight away, schedule the migration if your site is continuously updated or has special requirements, or purchase an [expedited migration](#expedited-migrations). Our migrations take place Monday through Friday; **we do not migrate sites on weekends**.

## Migration process

When Kinsta migrates your site, we need access credentials to connect to your site and transfer it to our infrastructure. The details we ask for typically include your hostname, username, password, and SFTP connection details.

We create a copy of your existing site and transfer it to our infrastructure. Once the migration is complete, you’ll receive a notification with instructions on how to test your site and confirm everything looks and functions correctly. Your original site will remain live during the migration. However, it’s important that you do not make any changes after the migration has started, as these updates will not be reflected in the migrated version.

After you’ve finished testing and are satisfied that everything is working as expected, you’ll need to [update your domain’s DNS records](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/) to point to Kinsta. Your site will not go live on Kinsta until these DNS changes are made. We also recommend following our [Go Live Checklist](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/go-live-checklist/) after the migration to ensure a smooth transition.

If you have any queries regarding your migration, contact our Migrations team by [opening a support ticket](https://kinsta.com/docs/support/contact-support/) from within MyKinsta. The Migrations team is available Monday – Friday, 24 hours a day. If you have an ongoing query, you can [switch to that chat](https://kinsta.com/docs/support/contact-support/#switch-chats) to continue the existing conversation.

## Before you start

### Who can request a migration

In order to request a migration, you must be a [Company Owner or Company Administrator.](https://kinsta.com/docs/company-settings/user-management/)

### What to prepare

1. **Check that you have an available site slot**. Kinsta creates a new site for your migration. Make sure your plan has an open spot before you begin.
2. **Gather your hosting credentials**. You’ll need your current host’s SFTP/SSH details, username, and password. If your host uses two-factor authentication (Cloudways, GoDaddy, SiteGround, or WP Engine), add **[[email protected]](https://kinsta.com/cdn-cgi/l/email-protection)** to your account before submitting your request, as 2FA can block our team’s access.
3. **If migrating from a backup**, make sure it contains both your site files and database, and that it’s ready to upload or accessible via a shareable link (Dropbox preferred).
4. **If your site is an e-commerce, membership, or community site**, plan for maintenance mode. Your site will need to be taken offline during the migration to prevent data loss. Coordinate the timing so you’re available to review and go live quickly afterward.
5. **Decide on SSL**. You’ll need to choose whether to generate a new free SSL certificate through Kinsta’s Cloudflare integration or upload your existing certificate. Have your key and certificate files ready if using the latter.
6. **Note any special requirements**. Bedrock/Trellis setup, reverse proxy rules, custom .htaccess or Nginx rules, WP Engine LargeFS, or a multisite network. You’ll need to include these in the Special Instructions field.
7. **Do not make changes to your site once the migration starts**. Any updates made after that point won’t carry over to Kinsta. If there are any changes or a delay between the migration and going live, [a second migration](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/perform-a-second-migration/) may be needed for any updates.
8. **Plan for post-migration DNS and service setup**. Pointing your domain to Kinsta, configuring third-party services, and setting up email are not included in the migration service; you’ll handle these yourself after the migration is complete. Common tasks include updating your domain’s [A records](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/), pointing nameservers to [Kinsta’s DNS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/), setting up a CDN such as Cloudflare or Sucuri, and [configuring your email service](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/email/). For more information, follow our [Go Live Checklist](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/go-live-checklist/) after the migration.

Once you have requested the migration, you can check the status of your migration(s) within [MyKinsta](https://my.kinsta.com/) > **Sites** > **Migrations** tab. Our Migrations team will also keep you updated on the status of your migration.

Once your migration is complete, we’ll send you details for testing the site and for pointing your website to Kinsta if everything looks good. Please always wait until we have confirmed that the migration is complete and that you’ve fully tested the migrated site before [making it live](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/go-live-checklist/).

### Special cases

#### eCommerce, membership, and community sites

For frequently updated sites (e.g., eCommerce, membership, or community sites using WooCommerce or Easy Digital Downloads), we strongly recommend enabling [maintenance mode](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/wordpress-migration-faqs/#what-is-maintenance-mode) during migration to prevent data loss. If that’s not possible, [contact our Support Team](https://kinsta.com/docs/support/contact-support/) to discuss alternatives.

While in maintenance mode, visitors see a notice and cannot place orders, register, update profiles, or publish content.

Once enabled, we migrate a copy of your site to Kinsta. After completion, you’ll receive instructions to preview it. The migrated site isn’t in maintenance mode, but it won’t be publicly accessible until you [update your DNS to point to Kinsta](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/).

**Your live site will remain in maintenance mode until the DNS is updated and fully propagated.** After migration, review and test the site, then [update the DNS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/) so visitors are routed to Kinsta and normal activity can resume.

Most migrations take 1–3 hours, with another 1–3 hours for review. [DNS propagation](https://kinsta.com/blog/dns-propagation/) typically takes around 1 hour, but can vary depending on TTL settings.

#### Bulk migrations

If you have a large number of WordPress sites you’d like us to migrate, you can [contact our support team](https://kinsta.com/docs/support/contact-support/) to perform a bulk migration.

#### Multisite network

If you want to migrate a WordPress multisite network, you must migrate it as a whole. The Kinsta migrations team cannot migrate a single sub-site of a multisite network into a standalone site; to do this, we recommend [working with a developer](https://kinsta.com/blog/hire-wordpress-developer/).

#### WordPress.com sites

For WordPress.com migrations, **we cannot do a traditional migration** because WordPress.com does not allow access to the site files or the database. We can only export your WordPress content, such as posts, pages, comments, meta tags, etc., and import the content into a new WordPress installation here at Kinsta.

Because we cannot access the site files, we cannot transfer your WordPress theme, plugins, or any other customizations made to the site. This means your site will not look the same as it does on WordPress.com, and any functionality that depends on a plugin will not work until you reinstall your site’s plugins.

After the migration, you or your [web developer](https://kinsta.com/blog/hire-wordpress-developer/) will need to reinstall the theme and plugins, and recreate any customizations you made on WordPress.com (if applicable).

#### Reverse proxy, WP Engine Large FS, or other complex requirements

If your site uses a reverse proxy, WP Engine’s LargeFS feature, or other complex requirements, please let us know in the **Special instructions** when you request the migration.

### How to minimize downtime

You can minimize downtime in a few ways:

- **Be ready to review immediately:** Schedule your migration for a time when you can start testing as soon as it completes, and keep an eye out for the Migrations team’s completion message.
- **Lower DNS TTL in advance:** 12–24 hours before migration, reduce your domain’s TTL to 300 seconds (5 minutes) to speed up propagation. After launch, increase it back to around 3600 seconds (1 hour). If you’re using Cloudflare, you don’t need to change TTL.
- **Prepare for previewing:** Review [how to preview your site on Kinsta](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/site-preview/) so you can quickly verify everything post-migration.
- **Be ready to update DNS:** Familiarize yourself with [pointing your domain to Kinsta](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/) so you can switch traffic over as soon as the site is confirmed working.

### Save and continue your migration request

While working on your migration request, if you need to stop and come back to it later, we’ve got you covered. Your request is automatically saved as a **Draft** if you leave the form and go to another part of MyKinsta in the same tab, if you close the tab in your browser, or even if you close the browser.

You can view all your migration requests in [MyKinsta](https://my.kinsta.com/) on the **Migrations** tab within **Sites**. If the migration request hasn’t been submitted, it will have a status of **Draft**. You can click the name to continue entering the required information and submit the request.

If a migration request is pending, you can click the name to view the migration details page, where you can track its progress.

![Click on a migration request name to continue editing or view the migration details page.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-draft-migration.png)

Click on a migration request name to continue editing or view the migration details page.

## Request a migration

To start a migration in [MyKinsta](https://my.kinsta.com/), log in and go to **Sites** > **Add site** > **Request migration**. If you haven’t yet added any sites, you’ll see two buttons instead of a list of sites on the **Sites** page. Click **Request a migration** to start your migration request.

![Select Request migration on the Sites page in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-request-migration.png)

Select Request migration on the Sites page in MyKinsta.

### Choose your timeframe

You must choose when you would like Kinsta to perform the migration from the following options:

#### As soon as possible

Migrations are usually completed within one business day. If you select this option, our Migrations team will check all of the information you’ve provided and notify you before the migration starts.

#### On a specific date

Our Migrations team will start the migration on the date and time you have requested. The timings depend upon receiving the correct information to complete the migration. If we’re unable to access the site or backup for the migration, that may delay the migration, depending on how long it takes to get the necessary information.

#### Expedited migrations

If you’re concerned about downtime or need to get your site live on Kinsta quickly, we offer expedited migrations for just $49 per site. [Agency plans](https://kinsta.com/wordpress-hosting/agencies/) include free expedited migration credits, with the number of credits determined by the number of sites in your plan. To check your available credits, navigate to [MyKinsta](https://my.kinsta.com/) > **Company settings** > **My Plan** > **Expedited migrations**.

With expedited migrations, our goal is to complete the process within 8 hours, between 9 AM and 11 PM, Monday to Friday (UTC). If we don’t meet this 8-hour target, we’ll refund your migration fee. While we strive to work as quickly as possible, certain factors, such as complex site requirements, slow transfer speeds from your current provider, or sites larger than 10GB, may extend the migration time. If we anticipate that the migration will take longer than 8 hours, we will keep you updated throughout the process.

### Choose your migration type

![Choose your migration type in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/10/wordpress-choose-migration-type.png)

Choose your migration type in MyKinsta.

There are two types of migrations to choose from:

- [Migrate from another host](#migrate-from-another-host): Share information about your current hosting provider so the Migration team can access the site to perform the transfer.
- [Migrate from a backup](#migrate-from-a-backup): Provide a link to files using cloud storage services such as Drive, Dropbox, etc., or upload a backup file (whether it’s created with Duplicator, ManageWP, or cPanel) to an existing Kinsta website.

#### Migrate from another host

On the **Source details** tab, select your current hosting provider. We’ll then ask for the details we need to access your site. Depending on your provider, we’ll ask you to either:

- **Add us as a user:** Add **[[email protected]](https://kinsta.com/cdn-cgi/l/email-protection)** as a user on your current hosting account.
- **Provide your hosting details:** Enter the login and connection details for your current host. This may include your host’s name, your username and password, and your SFTP connection details. For some hosts, we may also ask for your hosting control panel login. After entering your details, select **I confirm that I have tested the credentials provided above and they are working correctly**.

You can usually find these details in your current host’s control panel. For instructions specific to your provider, see [Source Details by Hosting Provider](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migration-source-details/). You can also contact your current host or the [Kinsta Support team](https://kinsta.com/docs/support/contact-support/) for help.

Once you’ve uploaded the backup, select **I confirm that my backup contains all of my site’s files and is accessible for migration**, and then click **Next**.

![Choose your backup type and how you want to share the backup with the Kinsta migrations team.](https://kinsta.com/wp-content/uploads/2026/10/wordpress-migrate-backup.png)

Choose your backup type and how you want to share the backup with the Kinsta migrations team.

### Site details

Next, we’ll ask for your domain, WordPress credentials, and WordPress admin URL, as well as whether your site is a Bedrock/Trellis site, ecommerce, community, or membership site, if it’s a multisite, and if it uses HTTPS.

![Complete the site details in your migration request.](https://kinsta.com/wp-content/uploads/2026/10/wordpress-migration-site-details.png)

Complete the site details in your migration request.

- **Domain name of site to transfer**: This is the domain you want to use to access your site.
- **Add domain with wildcard**: A wildcard domain ensures that any requests to a subdomain of `*.domain.com` resolve to the same IP address as your main domain. For example, if you have a wildcard DNS record for `*.example.com` pointing to `123.123.123.123`, any requests to `sub.example.com` or `blog.example.com` will be resolved to `123.123.123.123`.
- **WordPress username**: Your WordPress username.
- **WordPress password**: Your WordPress password.
- **WordPress admin URL**: The URL you use to access WP Admin.
- **Is your site ecommerce, or does it process orders, memberships, or user-generated content?**: These sites usually change continuously; therefore, we recommend putting them into maintenance mode to prevent data loss when migrating. If you select this option, you can select the option to **Enable maintenance mode**. Placing a site in maintenance mode means that the site content cannot be updated. While the site is in maintenance mode, a maintenance message is displayed, orders cannot be placed, users cannot register or edit their profiles, and new content cannot be published on the site.
- **Is it a multisite installation?**: If you have a multisite, select this option and choose whether your site is a **Subdomain** or **Subdirectory**. You must migrate the multisite network as a whole. The Kinsta migrations team cannot migrate a single sub-site of a multisite network into a standalone site.
- **Do you use a Bedrock or Trellis configuration?**: Select this option if your site uses the Bedrock or Trellis configuration and enter the **Root path** where the WordPress application is installed.
- **Does your site use HTTPS?**: If you select this option, you can choose to generate a new SSL certificate in MyKinsta (using our [free Cloudflare integration](https://kinsta.com/cloudflare-integration/)) or upload an existing certificate (if you have the key and certificate file).

After entering your site details, click **Next** to continue.

### Kinsta settings

You now need to complete the details for your site’s new home at Kinsta. Enter a unique name and choose your site’s data center from the [30 data center locations](https://kinsta.com/docs/service-information/data-center-locations/) available. If you have a dedicated [server,](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/dedicated-server/) you can choose this in the **Data center location**. You should also note this in the special instructions.

Let us know if there’s any special information or instructions we should know about for your site, such as forcing HTTPS or any special **.htaccess** or Nginx rules that you may need. You should also let us know if your site is a WordPress.com site, if it uses WP Engine’s Large FS feature, if it requires a reverse proxy, or if it has any other complex requirements.

![Add your Kinsta site details to your migration request.](https://kinsta.com/wp-content/uploads/2026/10/wordpress-migration-kinsta-details.png)

Add your Kinsta site details to your migration request.

Once you’ve completed your Kinsta settings, click **Next** to review your migration details.

### Review and submit

Carefully review the details of your request for any typos or errors. If you have requested an expedited migration, ensure the correct payment method is selected. If you need to change anything in the request, click the **Back** button to return to the previous page and update the information.

Once you’ve confirmed all of the information is correct, select **I’ve reviewed the details above and I’m ready to submit this migration request**, and **If full access to the source site isn’t available (for example, only a wp-admin login), you give Kinsta permission to use the Migrate Guru plugin to complete the migration**. This allows the Kinsta migrations team to use [Migrate Guru](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrate-guru/) to migrate your site if they are unable to access your site through your hosting provider.

Once you’ve selected the required options, click **Finish and submit** to submit your request.

![Review and submit your migration.](https://kinsta.com/wp-content/uploads/2026/10/wordpress-migration-review-submit.png)

Review and submit your migration.

## After you submit

Your pending migrations will show up in the **Migrations** tab under **Sites** in MyKinsta, and you can check the status anytime. Our Migrations team will also keep you updated on the status.

**Do not make changes to your site once the migration starts**. Your original site will remain live during the migration. However, it’s important that you do not make any changes after the migration has started, as these updates will not be reflected in the migrated version. If there are any changes or a delay between the migration and going live, [a second migration](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/perform-a-second-migration/) may be needed for any updates.

If you have any additional migrations to submit, click **Request new migration** to begin a new migration request.

![View migration requests on the Migrations tab within the WordPress sites page in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-pending-migration-1.png)

View migration requests on the Migrations tab within the WordPress sites page in MyKinsta.

### Malware removal

As part of every migration, our Migrations team performs a thorough scan of your site’s files for signs of malware or malicious code.

If malware is detected, we pause the migration and notify you before proceeding. At that point, you can choose one of the following options:

- Proceed with the migration and have Kinsta remove the malware.
- Cancel the migration, clean the site yourself, or work with a third-party security provider to remove the infection on your current host, and then reschedule the migration once the site has been cleaned.

If you choose to have Kinsta remove the malware, we quarantine infected files instead of permanently deleting them. The quarantined files are moved to the `~/private` directory within your site’s WordPress files, where they remain inaccessible to the public. This allows you to review or recover the files later if needed.

Quarantining files helps preserve potentially important data while preventing infected files from being publicly accessible or executed.

## What to do when the migration is complete

Once your migration is complete, you’ll receive a notification with steps to preview and test your site on Kinsta before it goes live. You can also find a post-migration checklist within your site’s **Info** page:

![Post-migration checklist. ](https://kinsta.com/wp-content/uploads/2023/11/wordpress-migration-checklist.png)

Post-migration checklist.

To test and preview your site using the [Site Preview tool](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/site-preview/):

1. Log in to MyKinsta, and go to **WordPress sites** > ***sitename*** > **Tools**.
2. On **Site Preview**, click **Enable**, enter your live domain, and select how long you’d like the preview enabled (1, 4, 8, or 24 hours).

You’ll then be able to access and test the site as if it were live.

Take time to verify your content, functionality, and any eCommerce or membership features (for example, stores using WooCommerce). Don’t update your DNS until you’ve fully tested everything.

Once you’re confident the site is working correctly, set up any [redirects](https://kinsta.com/docs/wordpress-hosting/redirect-rules/), [update your domain’s DNS records](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/) to point to Kinsta, and then [run a speed test](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/website-testing-tools/).

After [DNS propagation](https://kinsta.com/blog/dns-propagation/) is complete, visitors will be routed to your site on Kinsta. Only cancel your previous hosting once you’ve confirmed the site is loading correctly from Kinsta.
