---
url: "https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-constants/"
title: "PHP - PHP Constants"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "php"
section: []
kinsta_last_updated: "December 10, 2024"
sitemap_lastmod: "2024-12-10T12:23:07+00:00"
fetched_at: "2026-10-07T22:38:26Z"
sha256: "7cdf535960503c5e3a6b761d699aa0f22c3306c7eaddc0fdb89d8bf71fd0906c"
body_chars: 2637
extracted_with: "main article"
status: "live"
---

# PHP - PHP Constants

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-constants/
**Kinsta last updated:** December 10, 2024

---

PHP constants store fixed values that remain the same throughout your site. These constants are also referred to as environment variables. They are automatically global, which is ideal for values that need to be accessed in multiple places.

If you use a non-standard WordPress setup, such as Bedrock or Trellis, Kinsta may not be able to locate the `DB_PASSWORD` variable and, therefore, is unable to update the database password when you:

- Add a new site by cloning an existing environment
- Add a staging environment by cloning an existing environment
- Push staging to live
- Restore a backup
- Change the database password in MyKinsta

To resolve this issue, Kinsta provides the `SERVER_SECRET_DB_PASSWORD` PHP constant for use on the Kinsta servers. When you define this constant within the `config.php` file, MyKinsta uses it to identify your site’s database password. You can define it as follows:

Copy

```
define('DB_PASSWORD', defined('SERVER_SECRET_DB_PASSWORD') ? SERVER_SECRET_DB : 'asdijfhkjasdbfkjhbajiksd' );
```

You can define the following PHP constants to use with Kinsta servers:

- `SERVER_SECRET_DB_USER`
- `SERVER_SECRET_DB_PASSWORD`
- `SERVER_SECRET_DB_HOST`
- `SERVER_SECRET_DB_NAME`

For example, you can define the constants in the `config.php` file as follows:

Copy

```
define('DB_NAME', defined('SERVER_SECRET_DB_NAME') ? SERVER_SECRET_DB_NAME : 'newsitetest');
define('DB_USER', defined('SERVER_SECRET_DB_USER') ? SERVER_SECRET_DB_USER : 'newsitetest');
define('DB_PASSWORD', defined('SERVER_SECRET_DB_PASSWORD') ? SERVER_SECRET_DB : 'asdijfhkjasdbfkjhbajiksd' );
define('DB_HOST', defined('SERVER_SECRET_DB_HOST') ? SERVER_SECRET_DB_HOST : 'localhost');
```

Alternatively, you can define the constants as follows:

Copy

```
define('DB_NAME',SERVER_SECRET_DB_NAME);
define('DB_USER',SERVER_SECRET_DB_USER);
define('DB_PASSWORD',SERVER_SECRET_DB_PASSWORD);
define('DB_HOST',SERVER_SECRET_DB_HOST);
```

### WP_ENVIRONMENT_TYPE

Kinsta automatically sets the `WP_ENVIRONMENT_TYPE` environment variable for each environment. This tells WordPress, and any plugins or themes that check for it, whether it’s running in production, staging, or development.

| Environment | Value |
| --- | --- |
| Live | production |
| Staging | staging |
| Development | development |

You can read the value in PHP using the WordPress helper function:

Copy

```
php$environment = wp_get_environment_type();
// Returns 'production', 'staging', or 'development'
```

This is useful for conditionally loading debugging tools, disabling certain plugins, or changing behaviour between environments without hardcoding logic.
