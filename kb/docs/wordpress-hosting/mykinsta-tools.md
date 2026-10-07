---
url: "https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/"
title: "WordPress Hosting - Tools"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "mykinsta-tools"
section: []
kinsta_last_updated: "May 5, 2026"
sitemap_lastmod: "2026-05-05T09:57:58+00:00"
fetched_at: "2026-10-07T22:40:07Z"
sha256: "5c18666466d7d3c08f8de5228d55733b3eeaaa724d5ea10ce00cd9fae05cb602"
body_chars: 10438
extracted_with: "main article"
status: "live"
---

# WordPress Hosting - Tools

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/
**Kinsta last updated:** May 5, 2026

## On this page

- [Restart PHP](#restart-php)
- [WordPress debugging](#wordpress-debugging)
- [Search and replace](#search-and-replace)
- [New Relic monitoring](#new-relic-monitoring)
- [Blackfire monitoring](#blackfire-monitoring)
- [Rate limit control](#rate-limit-control)
- [Password protection](#password-protection)
- [Force HTTPS](#force-https)
- [Geolocation](#geolocation)
- [ionCube Loader](#ioncube-loader)
  - [How to enable ionCube Loader in MyKinsta](#how-to-enable-ioncube-loader-in-mykinsta)
- [PHP settings](#php-settings)
- [Remove Set-Cookie headers](#remove-set-cookie-headers)
- [Site preview](#site-preview)
- [Early hints](#early-hints)
- [DevKinsta](#devkinsta)

---

The Tools page in MyKinsta (**Sites** > ***sitename*** > **Tools**) is where you can find several tools to help you manage your WordPress site. We describe each tool below and provide links to documentation with more details.

![The WordPress Hosting Tools page in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/06/wordpress-tools.png)

The WordPress Hosting Tools page in MyKinsta.

## Restart PHP

While Managed WordPress Hosting includes self-healing PHP, you can also [restart PHP](https://kinsta.com/docs/wordpress-hosting/php/) for your site with this tool.

## WordPress debugging

[Enabling WordPress debug mode](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/wordpress-debugging/) can be helpful when troubleshooting. You can enable and disable debug mode in MyKinsta without editing your site’s **wp-config.php** file.

## Search and replace

The [search and replace tool](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/mykinsta-search-replace-tool/) makes it easy to do a search and replace in your site’s content from within MyKinsta. No need to install a plugin, use a script, or use the command line.

## New Relic monitoring

If you prefer to use New Relic instead of [Kinsta’s APM Tool](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/), this is where you can [start New Relic monitoring](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/custom-new-relic-tracking/), add your license key, and turn off monitoring when you’re finished troubleshooting. You can also change or remove your license key while monitoring is active. To minimize overhead and avoid conflicting data, we recommend you only use only one performance monitoring tool at a time.

## Blackfire monitoring

If you have a [Blackfire](https://www.blackfire.io/monitoring/) account, you can use [Blackfire monitoring](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/wordpress-blackfire-monitoring/) to view detailed information about your site’s performance helping you to identify issues and optimize your site. Add your Server ID and Token and when you’ve finished troubleshooting you can turn off monitoring.To minimize overhead and avoid conflicting data, we recommend you only use only one performance monitoring tool at a time.

## Rate limit control

This option is only available for environments hosted on a [dedicated server](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/dedicated-server/).

By default, Kinsta applies rate limits on PHP requests, including login attempts, to all sites, even those not on a dedicated server. These limits help protect your site from attacks and excessive bot traffic. For sites on a dedicated server, the rate limit control option provides additional flexibility, allowing you to disable these limits when necessary and re-enable them at any time.

## Password protection

There may be times when you’re working on a site and do not want it to be available to the public. You quickly add basic HTTP authentication to your site by [enabling Password protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/htpasswd/).

## Force HTTPS

Serving sites over HTTPS instead of HTTP is a recommended and fairly standard practice. When you enable [Force HTTPS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/#redirect-http-to-https-in-mykinsta), all traffic will be redirected from HTTP to HTTPS.

## Geolocation

[Enabling Geolocation](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/ip-geolocation/) makes it possible to direct traffic and customize your site visitor’s experience based on location (as determined by IP geolocation).

## ionCube Loader

[ionCube](https://kinsta.com/blog/ioncube-loader/) is a tool for encrypting PHP scripts for secure licensing and other use cases. If your site has a plugin, theme, or PHP script that uses ionCube to encrypt its code, you’ll need to enable the ionCube Loader extension.

We’ve built a tool to enable ionCube Loader right in [MyKinsta](https://my.kinsta.com/).

### How to enable ionCube Loader in MyKinsta

To enable ionCube Loader for your WordPress site, there are just a few steps you need to follow:

1. [Log in to MyKinsta](https://my.kinsta.com/).
2. Navigate to your site’s **Tools** page.
3. Click the **Enable** button under **IonCube Loader**.

![Enable ionCube Loader in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/06/wordpress-tools-ioncube-loader.png)

Enable ionCube Loader in MyKinsta.

After enabling ionCube Loader in MyKinsta, PHP scripts encoded with ionCube in your site environment will be able to be decoded and executed.

## PHP settings

To change your site’s PHP version, click **Change** under [PHP settings](https://kinsta.com/docs/wordpress-hosting/php/). Choose the **PHP version** and whether to enable or disable **Automatic PHP updates**; if enabled, Kinsta automatically upgrades the PHP to the latest supported version when the current version reaches its end of life. If you want to enable **Automatic PHP updates** without changing the PHP version, select **Unchanged** in the **PHP version** dropdown.

![Choose your PHP version and enable or disable automatic updates.](https://kinsta.com/wp-content/uploads/2024/10/wordpress-change-php-settings-1-1024x479.png)

Choose your PHP version and enable or disable automatic updates.

If you select a Long-Term Support (LTS) PHP version, automatic updates are disabled. The latest officially supported PHP version is 8.1; LTS versions only receive security patches, which may result in reduced performance compared to an officially supported version. To enhance your website’s performance, we recommend upgrading to the latest officially supported PHP version.

![Select a long-term support (LTS) PHP version.](https://kinsta.com/wp-content/uploads/2024/10/wordpress-change-php-settings-lts-1-1024x652.png)

Select a long-term support (LTS) PHP version.

You can also change the PHP version for one or multiple sites, including staging sites, simultaneously from the**Sites** page. Select the checkboxes next to the site(s) you want to change the PHP version on, click **Actions**, and choose **Change PHP settings**.

![Select which environments you want to update the PHP version for.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-bulk-actions-change-php-1.png)

Select which environments you want to update the PHP version for.

Choose the **PHP version** and whether to enable or disable **Automatic PHP updates**; if enabled, Kinsta automatically upgrades the PHP to the latest supported version when the current version reaches its end of life. If you want to enable **Automatic PHP updates** without changing the PHP version, select **Unchanged** in the **PHP version** dropdown.

If you select a Long-Term Support (LTS) PHP version, automatic updates are disabled. The latest officially supported PHP version is 8.1; LTS versions only receive security patches, which may result in reduced performance compared to an officially supported version. To enhance your website’s performance, we recommend upgrading to the latest officially supported PHP version.

![Choose the PHP version you want to update to and enable or disable automatic updates.](https://kinsta.com/wp-content/uploads/2024/10/wordpress-change-php-settings-bulk-1-1024x569.png)

Choose the PHP version you want to update to and enable or disable automatic updates.

Once the process is complete, a success message will appear.

## Remove Set-Cookie headers

The Remove `Set-Cookie` headers tool allows you to enable or disable the removal of `Set-Cookie`  headers from cached responses. Enabled means any `Set-Cookie` headers are removed from all cached responses. Disabled means if a page on your site contains a `Set-Cookie` header and that page is cached, the `Set-Cookie` header will be included in the cached response.

As of June 13, 2022, this tool is enabled by default, and the `Set-Cookie` header is removed from cached responses in all **newly created** sites at Kinsta. If your site was created before June 13, 2022, and you need to remove the `Set-Cookie` header from cached responses, you can do so with this tool.

If your site is working as expected with no issues, you are probably okay with leaving it in its current state (whether that’s enabled or disabled). This tool is intended for advanced users and developers. If you’re not sure whether or not you need to enable or disable this tool, we recommend working with a developer to determine what’s best for your site’s specific configuration.

[Cookies](https://kinsta.com/blog/wordpress-cookies-php-sessions/) typically contain user-specific information and should not be cached and returned to other users. Cookies are set with the `Set-Cookie` header, so we can prevent the accidental caching and potential sharing of cookies by removing the `Set-Cookie` header from all cached responses.

To use the tool, log in to [MyKinsta](https://my.kinsta.com/) and navigate to **Sites** > ***sitename*** > **Tools** > **Remove Set-Cookie headers** and click the **Enable** or **Disable** button (depending on the current state of the tool).

![Enable or disable Remove Set-Cookie headers in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/06/wordpress-tool-sremove-set-cookie-headers.png)

Enable or disable Remove Set-Cookie headers in MyKinsta.

## Site preview

The [Site Preview](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/site-preview/) tool lets you preview your site with your [WordPress temporary URL](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-temporary-url/) (e.g. https://sitename.kinsta.cloud) with no changes to your site’s database, files, or your domain’s DNS.

## Early hints

[Early Hints](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/early-hints/) is a web standard you can use to improve page load times. As part of [Kinsta’s Cloudflare integration](https://kinsta.com/blog/cloudflare-integration/), Early Hints can be enabled for your WordPress site.

## DevKinsta

[DevKinsta](https://kinsta.com/docs/devkinsta/) is Kinsta’s local development tool that makes it possible to design, develop, and deploy WordPress sites with a single click on your local machine. DevKinsta is free and available for macOS, Windows, and Ubuntu. Click the **Download** button to get started.
