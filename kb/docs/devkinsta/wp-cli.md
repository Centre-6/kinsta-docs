---
url: "https://kinsta.com/docs/devkinsta/wp-cli/"
title: "DevKinsta - WP-CLI"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "wp-cli"
section: []
kinsta_last_updated: "January 25, 2024"
sitemap_lastmod: "2024-01-25T16:44:42+00:00"
fetched_at: "2026-10-07T22:37:54Z"
sha256: "310269b8ea9e055934073ef2adab0922d4ce43f8c1b217fed978d9b895a8604a"
body_chars: 498
extracted_with: "main article"
status: "live"
---

# DevKinsta - WP-CLI

**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/wp-cli/
**Kinsta last updated:** January 25, 2024

---

[WP-CLI](https://wp-cli.org/) is the command-line interface for WordPress. You can update plugins, configure multisite installations, [and much more](https://kinsta.com/blog/wp-cli/) without using a web browser.

## Access to WP-CLI

Enter into `devkinsta_fpm` container:

Copy

```
docker exec -u www-data -it devkinsta_fpm bash
```

Go to your site folder:

Copy

```
cd /www/kinsta/public/siteName
```

Run `WP-CLI` command:

Copy

```
wp search-replace remote-domain.com my-local-site.local
```
