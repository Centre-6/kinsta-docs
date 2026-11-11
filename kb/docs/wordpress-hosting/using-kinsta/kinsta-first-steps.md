---
url: "https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-first-steps/"
title: "After Go-Live: First Steps"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "using-kinsta"
section: ["WordPress Hosting", "Using Kinsta"]
kinsta_last_updated: "2026-10-12T16:26:03"
change_signal: "2026-10-12T16:26:03"
fetched_at: "2026-11-11T13:03:01Z"
sha256: "4223a6b6aa10044713bedc3f1ac1120450842cf7fe5adf453312740be8c69728"
body_chars: 7173
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# After Go-Live: First Steps

**Section:** WordPress Hosting > Using Kinsta
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-first-steps/
**Kinsta last updated:** 2026-10-12T16:26:03

## On this page

- [1. Turn on monitoring notifications](#1-turn-on-monitoring-notifications)
- [2. Check your email still works](#2-check-your-email-still-works)
- [3. Create your staging environment](#3-create-your-staging-environment)
- [4. Remove plugins you no longer need](#4-remove-plugins-you-no-longer-need)
- [5. Check your PHP version](#5-check-your-php-version)
- [6. Close your old hosting account safely](#6-close-your-old-hosting-account-safely)
- [7. Know how to get help](#7-know-how-to-get-help)
- [8. Check your billing details](#8-check-your-billing-details)

---

Once your site is live, a few loose ends are worth tying up in the first week: making sure nothing was left behind at your old host, that you’ll hear about problems, and that you know where to get help. If your site isn’t live yet, start with the [Go Live Checklist](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/go-live-checklist/).

## 1. Turn on monitoring notifications

**Why it matters:** Kinsta checks every site every 3 minutes. Our engineers fix infrastructure problems automatically, but if the problem is on your site, such as a plugin conflict, you’ll only hear about it if [notifications](https://kinsta.com/docs/user-settings/notifications/) are on.

**How to start:** Go to **User Settings** > **Notifications** and enable WordPress site monitoring notifications. You’ll then be emailed about site errors, SSL problems, expired domains, and DNS issues. See [Uptime Monitoring](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/uptime-monitoring/).

**Watch out for:** Only users with access to the site’s live environment receive alerts. Company Billing and WordPress Site Developer users don’t.

## 2. Check your email still works

**Why it matters:** Kinsta hosts your website, not your email mailboxes. If you moved your domain’s DNS to Kinsta, your email provider’s MX records must be added there too, or messages to your domain stop arriving.

**How to start:** Send a test email to and from an address on your domain. If anything fails and you use Kinsta’s DNS, check your MX records; see [Kinsta’s DNS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/#email-authentication) and, for Google Workspace, [Google MX Records](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/google-mx-records/).

## 3. Create your staging environment

**Why it matters:** A staging environment is a private copy of your site where you can test plugin updates, design changes, and PHP upgrades before visitors see them. Every site includes a free standard staging environment, and you’ll use it in the next two steps.

**How to start:**

1. In MyKinsta, select your site, click the environment name at the top of the page (for example, Live), and select **Create new environment**.
2. Select **Standard environment** and click **Continue**.
3. Select **Clone an existing environment**, then choose **Live** as the environment to clone.
4. Finish creating the environment. Your staging site gets its own URL, such as `stg-sitename-environmentname.kinsta.cloud`.

See [Staging Environments](https://kinsta.com/docs/wordpress-hosting/staging-environment/) for the full options.

**Worth knowing:**

- **Logging in:** A cloned staging site uses the same WordPress login as your live site until you change it.
- **Resources:** A standard staging environment has up to 2 PHP threads and doesn’t run edge caching or Kinsta CDN. It’s ideal for testing changes, but not for measuring speed. If you need a staging environment that matches live, see the premium staging add-on under [Add-Ons](https://kinsta.com/docs/wordpress-hosting/wordpress-add-ons/).
- **Keeping it current:** Staging doesn’t update itself when your live site changes. To test against fresh content, delete it and clone live again, or push from live to staging; see [Make Changes Safely](https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-make-changes-safely/).

## 4. Remove plugins you no longer need

**Why it matters:** some plugins were only needed at your old host, or do a job Kinsta now handles for you. Leaving them active adds load and can cause conflicts.

**Plugins to review:**

- **Page caching plugins:** Kinsta provides caching at the server level, and many caching plugins are incompatible with it.
- **Your previous host’s own plugin:** These usually only work on that host’s platform.
- **Redirect plugins:** No longer needed once your redirects are in MyKinsta.
- **Backup and uptime plugins:** Kinsta already backs up and monitors your site, so check whether you still need them.
- **Your own Patchstack plugin:** Kinsta includes Patchstack-powered [Vulnerability protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-vulnerability-protection/) at no extra cost, but it’s switched off on any site running its own Patchstack plugin. Unless you need your own Patchstack account, remove the plugin and Kinsta’s protection turns on within 12 hours. Check its status on your site’s **Info** page in MyKinsta.

**How to start:** Compare your plugin list with [Banned and Incompatible Plugins](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-banned-incompatible-plugins/). Deactivate plugins on your [staging environment](https://kinsta.com/docs/wordpress-hosting/staging-environment/) first to confirm nothing breaks.

## 5. Check your PHP version

**Why it matters:** Newer PHP versions are faster and still receive security fixes. Migrated sites sometimes arrive on an older version to match the previous host.

**How to start:** See which version your site uses and how to change it in [Restart and Update PHP](https://kinsta.com/docs/wordpress-hosting/php/wordpress-restart-update-php/). Test a new version on [staging](https://kinsta.com/docs/wordpress-hosting/staging-environment/) before changing it on live.

## 6. Close your old hosting account safely

**Why it matters:** Cancelling too early can take down services you didn’t realise were still at your old host.

**Before you cancel:**

1. Confirm your [domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/) points to Kinsta and your site loads from MyKinsta’s domain settings.
2. Check whether your old host also handles your domain registration, DNS, or email, and move those first.
3. Download a final backup of your site from the old host to keep.

## 7. Know how to get help

**[Contact Support](https://kinsta.com/docs/support/contact-support/):** Our Support team is available 24/7 from MyKinsta.

**[Scope of Support](https://kinsta.com/docs/support/scope-of-support/):** What our team can help with, and what’s outside it.

**[System status](https://status.kinsta.com/?_gl=1*rn5ekb*_ga*MjAwNDc0Mjk4NS4xNzg4ODgxOTM4*_ga_R8LLNPRZTN*czE3OTE1MzQyNDMkbzIzJGcxJHQxNzkxNTM5MjYyJGo2MCRsMCRoMCRkVUtEMTUzMXRlbXlfeHowX0MzbTFtOFNjdjJPOWNwVHZBZw..*_gcl_au*NzI0MDgyMTg0LjE3ODg4ODE5Mzg.):** Check here first if several sites have problems at once.

**[Community forum](https://community.kinsta.com/?_gl=1*rn5ekb*_ga*MjAwNDc0Mjk4NS4xNzg4ODgxOTM4*_ga_R8LLNPRZTN*czE3OTE1MzQyNDMkbzIzJGcxJHQxNzkxNTM5MjYyJGo2MCRsMCRoMCRkVUtEMTUzMXRlbXlfeHowX0MzbTFtOFNjdjJPOWNwVHZBZw..*_gcl_au*NzI0MDgyMTg0LjE3ODg4ODE5Mzg.):** Ask questions and learn from other Kinsta customers.

## 8. Check your billing details

**Why it matters:** Correct details mean your invoices are right the first time, which matters if you claim back tax.

**How to start:** Check your company address and any VAT or GST number under **Company settings** > **[Billing details](https://kinsta.com/docs/billing/update-billing-address/)**. Past invoices are under **[Invoices](https://kinsta.com/docs/billing/invoices/)**.
