---
url: "https://kinsta.com/docs/devkinsta/wp-cli/"
title: "WP-CLI"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "wp-cli"
section: ["DevKinsta"]
kinsta_last_updated: "2024-01-25T16:44:42"
change_signal: "2024-01-25T16:44:42"
fetched_at: "2026-10-07T22:58:19Z"
sha256: "0a613dfe36efabe45aba3507b1f026b8ca18f641ff7962184e3262afa273e9fe"
body_chars: 480
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# WP-CLI

**Section:** DevKinsta
**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/wp-cli/
**Kinsta last updated:** 2024-01-25T16:44:42

---

[WP-CLI](https://wp-cli.org/) is the command-line interface for WordPress. You can update plugins, configure multisite installations, [and much more](https://kinsta.com/blog/wp-cli/) without using a web browser.

## Access to WP-CLI

Enter into `devkinsta_fpm` container:

```
docker exec -u www-data -it devkinsta_fpm bash
```

Go to your site folder:

```
cd /www/kinsta/public/siteName
```

Run `WP-CLI` command:

```
wp search-replace remote-domain.com my-local-site.local
```
