---
url: "https://api-docs.kinsta.com/pages/backups/description/"
title: "Backups"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "backups"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:55.466Z"
fetched_at: "2026-10-07T22:41:47Z"
sha256: "0dd4c3066554ea7a43070b761c627fa29d272a327899bf4dc46b03eaa3b92920"
body_chars: 1251
extracted_with: "main"
status: "live"
---

# Backups

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/pages/backups/description/

---

You can use `backups` endpoint to get a list of your site’s [backups](https://kinsta.com/docs/wordpress-hosting/wordpress-backups) a list of all [downloadable backups](https://kinsta.com/docs/wordpress-hosting/wordpress-backups#downloadable-backups), and the date of the next available downloadable backup.
You can send a `POST` request to [restore a backup](https://kinsta.com/docs/wordpress-hosting/wordpress-backups#restore-wordpress-backups) to any of your site’s environments.
You can also send a `DEL` request to remove a backup from any of your site’s environments.
You can obtain the `environment_id` using the `GET` request with the [WordPress Site Environments](https://api-docs.kinsta.com/tag/WordPress-Site-Environments#operation/getSiteEnvironments) endpoint.
The `environment_id` is also shown after the `site_id` in the URL in MyKinsta when you access the environment, for example in the URL `https://my.kinsta.com/sites/details/fbab4927-e354-4044-b226-29ac0fbd20ca/c84ce214-69b9-4a32-8e67-880672cf1d38?idCompany=bdd25d71-5706-4890-870f-1adda17c505d`:

- The `site_id` is `fbab4927-e354-4044-b226-29ac0fbd20ca`
- The `environment_id` is `c84ce214-69b9-4a32-8e67-880672cf1d38`
- The `company_id` is `bdd25d71-5706-4890-870f-1adda17c505d`
