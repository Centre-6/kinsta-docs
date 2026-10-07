---
url: "https://api-docs.kinsta.com/pages/wordpress-site-environments/description/"
title: "WordPress Site Environments"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-environments"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:55.465Z"
fetched_at: "2026-10-07T22:41:52Z"
sha256: "418e48e42f12452ccf35c30a5aafb5dee35436ca618aad8b816a760537c8e787"
body_chars: 3975
extracted_with: "main"
status: "live"
---

# WordPress Site Environments

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/pages/wordpress-site-environments/description/

---

The available WordPress site environments include:

- [Live](https://kinsta.com/blog/wordpress-api/)
- [Staging](https://kinsta.com/docs/wordpress-hosting/staging-environment)
- [Premium Staging](https://kinsta.com/docs/wordpress-hosting/staging-environment#premium-staging-environments)

Using the `environments` endpoint, you can:

- Get information about your site’s environments.
- [Create a new environment](https://kinsta.com/docs/wordpress-hosting/staging-environment#create-wordpress-staging-environment) (with or [without WordPress](https://kinsta.com/docs/wordpress-hosting/staging-environment#option-3-dont-install-wordpress-empty-environment)).
- [Push an environment](https://kinsta.com/docs/wordpress-hosting/wordpress-push-environments/)
- [Clone an existing environment](https://kinsta.com/docs/wordpress-hosting/staging-environment#option-1-clone-an-existing-environment).
- [Delete an environment](https://kinsta.com/docs/wordpress-hosting/staging-environment#delete-and-refresh-staging-environment).
- [Change PHP allocation settings](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/#change-php-performance).
- [Change the webroot subfolder](https://kinsta.com/docs/wordpress-hosting/site-management/#change-your-sites-path) of an environment.
- [Update redirect rules](https://kinsta.com/docs/wordpress-hosting/redirect-rules/).
- [Manage SFTP access and settings](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/).
- [Run WP CLI commands](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-wp-cli/).
- [Generate a phpMyAdmin login link](https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database-access/#phpmyadmin).
- [Create WP Admin logins and check if users already exist](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-wp-admin/).

You can obtain the `site_id` using the `GET` request with the [WordPress Sites](https://api-docs.kinsta.com/tag/WordPress-Sites#operation/getSites) endpoint.
The `site_id` is also shown in the URL in MyKinsta when you access the environment, for example in the URL `https://my.kinsta.com/sites/details/fbab4927-e354-4044-b226-29ac0fbd20ca/c84ce214-69b9-4a32-8e67-880672cf1d38?idCompany=bdd25d71-5706-4890-870f-1adda17c505d`:

- The `site_id` is `fbab4927-e354-4044-b226-29ac0fbd20ca`
- The `environment_id` is `c84ce214-69b9-4a32-8e67-880672cf1d38`
- The `company_id` is `bdd25d71-5706-4890-870f-1adda17c505d`

The `change-environment-php-allocation` and `change-site-php-allocation` endpoints are not currently available to customers who have any of following plans: Single 1.25M or above, WP 60 or above, Agency, or a custom plan.
The [PHP memory limit](https://kinsta.com/docs/wordpress-hosting/php/#php-memory-limit) and number of [PHP threads](https://kinsta.com/docs/wordpress-hosting/php/#php-threads) must add up to the existing total memory pool of the site. You can only change the total memory pool within [PHP performance](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/) in [MyKinsta](https://my.kinsta.com/).
`change-environment-php-allocation` can only be used for premium staging environments.
`change-site-php-allocation` updates the PHP memory limit of the live environment and all standard staging environments. Standard staging environments will always have 2 PHP threads regardless of their memory allocated. You cannot use this endpoint to update premium staging environments.
When using the `change-webroot-subfolder-of-environment` endpoint, the default web root path for a site is `/www/$site_path/public`. This default path cannot be changed, but you can append a subfolder, for example, `/www/$site_path/public/site`. To check the current path, use the `get-site-environments` endpoint, which displays the `web-root` field indicating any subfolder appended to `/public`. To revert the path to the default, send the request with an empty string `''` as the subfolder.
