---
url: "https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-your-maintenance-routine/"
title: "Your Maintenance Routine"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "using-kinsta"
section: ["WordPress Hosting", "Using Kinsta"]
kinsta_last_updated: "2026-10-12T16:34:19"
change_signal: "2026-10-12T16:34:19"
fetched_at: "2026-11-11T13:03:01Z"
sha256: "bc36c9e2d9d2440ba98b94117807747883092b14c7ec026fef99916cb6aface4"
body_chars: 8293
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Your Maintenance Routine

**Section:** WordPress Hosting > Using Kinsta
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-your-maintenance-routine/
**Kinsta last updated:** 2026-10-12T16:34:19

## On this page

- [Every day: Kinsta handles this for you](#every-day-kinsta-handles-this-for-you)
- [Every week: about 15 to 30 minutes](#every-week-about-15-to-30-minutes)
- [Every month: about 1 to 2 hours](#every-month-about-1-to-2-hours)
- [Every quarter](#every-quarter)
- [Every year](#every-year)
- [Spend less time on maintenance](#spend-less-time-on-maintenance)

---

A WordPress site needs regular upkeep. For a typical small business site, that’s around 15 to 30 minutes a week and 1 to 2 hours a month. Kinsta does many of these tasks for you automatically. This page shows what’s already handled, what’s left for you, and which Kinsta tool makes each job quicker.

## Every day: Kinsta handles this for you

You don’t need to do anything here, as long as notifications are turned on so you hear when something needs attention.

- **Check your site is up:**  [Uptime monitoring](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/uptime-monitoring/) checks every 3 minutes and emails you about errors.
- **Back up your site:**  [Automatic daily backups](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/), kept for 14 to 30 days depending on your plan.
- **Scan for vulnerable plugins and themes:** MyKinsta scans every plugin and theme daily and flags known [vulnerabilities](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/#plugin-and-theme-vulnerabilities).
- **Block exploits of known vulnerabilities:**  [Vulnerability protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-vulnerability-protection/) blocks attacks on your plugins, themes, and WordPress version, even before a fix is out.
- **Block attacks:** Cloudflare’s firewall, DDoS protection, and [bot protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/).
- **Update plugins and themes:** Done daily for you with [Kinsta Automatic Updates](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-plugins-themes-automatic-updates/), if you add it.

## Every week: about 15 to 30 minutes

Updates matter most. In 2025, 11,334 new WordPress vulnerabilities were reported, and 91% of them were in plugins. Almost half had no fix available when they became public. Kinsta’s vulnerability protection blocks known exploits during that gap, but only an update fixes the code, so apply fixes as soon as they appear.

- **Update plugins and themes, or check what was updated for you:** Update from [Plugins and themes](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-manage-plugins-themes/) in MyKinsta, or review the [Automatic Updates log](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-plugins-themes-automatic-updates/#view-installed-updates) and its before-and-after screenshots.
- **Act on vulnerability alerts:**  [Vulnerable plugins and themes](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/#plugin-and-theme-vulnerabilities) are flagged in MyKinsta.
- **Test the forms, bookings, or checkout that bring in business:** No tool needed; submit a test enquiry or order yourself.
- **Clear spam comments and suspicious new users:** Done in WordPress. If spam is constant, raise your [bot protection level](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/).
- **Look into any alerts you received:**  [Server logs](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/) in MyKinsta show what happened and when.

## Every month: about 1 to 2 hours

- **Update WordPress core:** Test major releases on your free [staging environment](https://kinsta.com/docs/wordpress-hosting/staging-environment/) first, then [push to live](https://kinsta.com/docs/wordpress-hosting/wordpress-push-environments/).
- **Check a backup actually restores:**  [Restore](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#restoring-wordpress-backups-to-staging) a recent backup to staging and click through it, without touching live.
- **Run a [speed test](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/website-testing-tools/) and check slow pages:** Compare with earlier results, then use the [APM tool](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/) on any page that’s slower.
- **Check plan usage and disk space:** Go to **Analytics** > [**Plan usage**](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/#plan-usage) in MyKinsta.
- **Review bot traffic:** See the [**Top traffic report**](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#top-traffic) under **Bot protection**.
- **Clean up the database:** Remove old revisions, spam, and expired data with [WP-CLI](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-wp-cli/) or a cleanup plugin. Take a [backup](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/) first.

## Every quarter

- **Review who has access:** Check MyKinsta users in **[User Management](https://kinsta.com/docs/company-settings/user-management/)** and WordPress accounts with the **[WordPress Users](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-users/)** tool. Remove anyone who no longer needs access.
- **Delete plugins and themes you don’t use:** Check which are inactive under **[Plugins and Themes](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-manage-plugins-themes/)** in MyKinsta, then delete them from your WordPress dashboard or with [WP-CLI](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-wp-cli/). Inactive plugins can still be exploited, so delete rather than just deactivate.
- **Test your full checkout or sign-up journey:** Run through it on [staging](https://kinsta.com/docs/wordpress-hosting/staging-environment/) so test orders don’t reach your live store.
- **Review traffic trends:** Use [**Analytics**](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/) in MyKinsta, alongside your own analytics tool.
- **Review bot protection settings and exceptions:** Remove [exceptions](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#exceptions) for services you no longer use.
- **Check your PHP version:** Upgrade on staging first; see [Restart and Update PHP](https://kinsta.com/docs/wordpress-hosting/php/wordpress-restart-update-php/).

## Every year

- **Renew your domain:** Kinsta alerts you if a domain on your site has expired, but renew before that point with your registrar.
- **Check SSL certificates:** Kinsta’s free SSL is managed for you. [Custom certificates](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/#option-two-custom-ssl-certificate) you uploaded need renewing yourself.
- **Check your plan still fits:** Compare a year of usage with [Choosing the Right Plan](https://kinsta.com/docs/billing/wordpress-hosting-plans/wordpress-choosing-the-right-plan/).
- **Remove or refresh outdated pages:** Add [redirects](https://kinsta.com/docs/wordpress-hosting/redirect-rules/) for any page you delete so visitors and search engines aren’t sent to an error.
- **Review your privacy policy and cookie consent:** There’s no Kinsta tool for this; check your site still meets the rules where your visitors are.

## Spend less time on maintenance

- **Let updates run themselves:**  [Kinsta Automatic Updates](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-plugins-themes-automatic-updates/) installs plugin and theme updates daily. It compares screenshots of up to five key pages before and after each update, and rolls back automatically if something looks wrong. It costs $3 per environment per month after a month’s free trial.
- **Manage many sites at once:**  [Bulk actions](https://kinsta.com/docs/wordpress-hosting/site-management/#bulk-actions) on the **Sites** page apply updates and settings to several sites in one go; see [Work as a Team](https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-work-as-a-team/).
- **Make changes safely:** Staging and push environments mean testing never puts your live site at risk; see [Make Changes Safely](https://kinsta.com/docs/wordpress-hosting/using-kinsta/kinsta-make-changes-safely/).
- **Get alerted instead of checking:** With [notifications](https://kinsta.com/docs/user-settings/notifications/) on, you only need to act when something goes wrong.
