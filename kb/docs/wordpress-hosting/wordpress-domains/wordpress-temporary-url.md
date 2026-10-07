---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-temporary-url/"
title: "Temporary URL"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-domains"
section: ["WordPress Hosting", "Domains and DNS"]
kinsta_last_updated: "2025-07-01T15:04:06"
change_signal: "2025-07-01T15:04:06"
fetched_at: "2026-10-07T22:58:21Z"
sha256: "5456b2464eefb8c05a8041f7505670116e618fd5857c8428a191ba737764fbe4"
body_chars: 3201
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Temporary URL

**Section:** WordPress Hosting > Domains and DNS
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-temporary-url/
**Kinsta last updated:** 2025-07-01T15:04:06

---

Every site created at Kinsta comes with a WordPress temporary URL so that it’s immediately accessible to you even before you point your custom domain to the site at Kinsta. These temporary domains use this format: **https://sitename.kinsta.cloud**.

When you add your site to MyKinsta, the temporary URL is generated using your site name. If your site name uses non-Latin characters such as Chinese Hanzi, Japanese Kana, Arabic, or Thai, these are converted to Latin characters for our systems to work correctly.

Google has its policies on duplicate content/URLs, so to avoid this SEO issue, we enforce an `X-Robots-Tag` HTTP header with a value of `noindex, nofollow, nosnippet, noarchive` on the temporary URL.

This means **sitename.kinsta.cloud** URLs won’t be indexed by search engines. The same applies to [staging environment](https://kinsta.com/docs/wordpress-hosting/staging-environment/) URLs.

Our old temporary URL formats were **sitename.kinsta.com** and **sitename.tempXXX.kinsta.cloud**. If you’ve been a Kinsta client for a while, your site might still be using one of these formats.

Once your site is created, you’ll be able to access your new WordPress site using the temporary URL. You can see it in [MyKinsta](https://my.kinsta.com/) in the **Domains** tab under **Sites**.

![WordPress temporary URL for a Kinsta site](https://kinsta.com/wp-content/uploads/2023/11/wordpress-domains-temporary-domain-2.png)

WordPress temporary URL for a Kinsta site

After building or transferring your site to Kinsta, you’ll need to [add your custom domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/ "How to add a domain to your install") on the **Domains** page and point your DNS to Kinsta. Once the DNS propagates, you won’t need the temporary URL anymore.

## Fix site redirecting to sitename.kinsta.cloud

If you create a new site without a custom domain, the temporary URL (sitename.kinsta.cloud) is created automatically, as described above. This means the site URL and home URL will be sitename.kinsta.cloud.

If you [add a custom domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/) to the site in MyKinsta, set it as the primary domain but do not select the option to run a search and replace it; your site will use the temporary URL. In this case, for your site to use your custom domain, you’ll need to adjust a few settings in your WordPress dashboard or use the [search and replace tool](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/mykinsta-search-replace-tool/) in MyKinsta.

We recommend using the search and replace tool, but if you haven’t yet added any content or uploaded any images or other media, you can make the change in the WordPress dashboard.

Log in to your WordPress dashboard (**/wp-admin**) and go to **Settings** > **General**. Update your **WordPress Address URL** and **Site Address URL** with the URL of your custom domain.

![Changing the Kinsta temporary URL to your custom URL in WordPress settings.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-update-temporary-url.png)

Changing the Kinsta temporary URL to your custom URL in WordPress settings.
