---
url: "https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/site-preview/"
title: "Tools - Site Preview"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "mykinsta-tools"
section: []
kinsta_last_updated: "May 6, 2026"
sitemap_lastmod: "2026-05-06T10:52:01+00:00"
fetched_at: "2026-10-07T22:40:09Z"
sha256: "ecc2af2e741c8163b3106d0fefe037572e40a2c3bd9edb172d160aed6fd9224e"
body_chars: 5047
extracted_with: "main article"
status: "live"
---

# Tools - Site Preview

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/site-preview/
**Kinsta last updated:** May 6, 2026

## On this page

- [Enable Site Preview](#enable-site-preview)
- [Disable Site Preview](#disable-site-preview)
- [Previewing a multisite](#previewing-a-multisite)
- [Notifications](#notifications)

---

With Site Preview, when you migrate your WordPress site to Kinsta, you can preview your site over your [WordPress temporary URL](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-temporary-url/) (e.g. https://sitename.kinsta.cloud) before you make it live, even if the database or hard-coded files still use your live domain or another domain. Site Preview allows you to view your site at Kinsta without having to make any changes to your site’s database, files, or your domain’s DNS records. This tool lets WordPress think the URL it should use is the temp URL, without the hassle of running a search and replace in your site’s database.

## Enable Site Preview

To activate Site Preview in MyKinsta, head over to your site’s **Tools** tab and click on the **Enable** button under **Site Preview**.

![Enable Site Preview in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/06/wordpress-tools-site-preview.png)

Enable Site Preview in MyKinsta.

In the **Site Preview** modal/pop-up that appears, enter your live site’s domain. This needs to be the domain that is currently configured within your WordPress install and is typically the live domain but could be a different domain, depending on where you migrated the site from.

Choose how long you want Site Preview to be enabled under **Auto-disable** and click the **Enable Site Preview** button.

![Enter your live domain and enable Site Preview.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-enable-site-preview-2.png)

Enter your live domain and enable Site Preview.

Once Site Preview is enabled, click **Domains** and open your site’s **temporary URL** in your browser. This is the URL that ends in `.kinsta.cloud`, for example `website.kinsta.cloud`, and may be different from your Primary domain.

![Open your site's temporary URL.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-open-temp-url.png)

Open your site’s temporary URL.

You’ll be able to view the site just like you normally would on the live domain. You can also confirm that Site Preview is working by inspecting your site with your browser’s developer tools and looking for the `X-Kinsta-preview-mode: active` header on the Network tab.

![Viewing the X-Kinsta-preview-mode: active header in your browser.](https://kinsta.com/wp-content/uploads/2021/12/preview-mode-active-header.jpg)

Viewing the X-Kinsta-preview-mode: active header in your browser.

If you’re happy with the migrated content and you want to make the site live, you can [disable the site preview](#Disable-Site-Preview). To see what steps are required to make the site live, check out our [Go Live Checklist](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/go-live-checklist/).

## Disable Site Preview

Once you’re finished previewing your site, you can disable Site Preview. To do this, you have two options:

**Option 1:** On your site’s **Domains** page, click the **Disable Site Preview** button next to the temporary domain.

![Disable Site Preview on the Domains page in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-domains-disable-site-preview-2.png)

Disable Site Preview on the Domains page in MyKinsta.

**Option 2:** Head back over to your site’s **Tools** tab in MyKinsta and click the **Disable** button under **Site Preview**.

![Disable Site Preview in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/06/wordpress-tools-site-preview-disable.png)

Disable Site Preview in MyKinsta.

## Previewing a multisite

To preview a WordPress multisite, you’ll need to disable and re-enable Site Preview for each domain or subdomain you want to preview. The steps to preview a multisite are:

1. Enable Site Preview for the domain you want to test first (example.com) by entering the domain in the **Domain of your site** field in the **Enable Site Preview** modal/pop-up.
2. Open your site’s Kinsta temporary URL in your browser and test the site thoroughly.
3. Disable Site Preview and re-enable it for the domain or subdomain you want to test next (site1.example.com) by entering the domain or subdomain in the **Domain of your site** field in the **Enable Site Preview** modal/pop-up.
4. Open your site’s Kinsta temporary URL in your browser again and test the subsite thoroughly. You’ll use the same Kinsta temporary URL to preview each site. **Note:** If you do not see the correct subsite, try clearing your browser cache or loading the URL in an incognito/private window.
5. Repeat until any domains or subdomains you want to preview are tested. Turn Site Preview off for the last time.

## Notifications

We send email notifications to the **Company Owner**, **Company Administrator**, and **Company Developer**  [users](https://kinsta.com/docs/company-settings/user-management/) when:

- Site Preview is enabled by a user.
- Site Preview is disabled by a user.
- Site Preview is automatically disabled after the time selected in Auto-disable.

Note: If our Support team enables or disables Site Preview, we do not send any email notifications.
