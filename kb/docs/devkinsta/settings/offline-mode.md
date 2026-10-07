---
url: "https://kinsta.com/docs/devkinsta/settings/offline-mode/"
title: "Settings - Offline Mode"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "settings"
section: []
kinsta_last_updated: "July 18, 2024"
sitemap_lastmod: "2024-07-18T08:37:46+00:00"
fetched_at: "2026-10-07T22:36:44Z"
sha256: "acc8e4d7db43c699df9af76e6b39e8d55630c4a9cb80393feaa27e8e436430fc"
body_chars: 1780
extracted_with: "main article"
status: "live"
---

# Settings - Offline Mode

**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/settings/offline-mode/
**Kinsta last updated:** July 18, 2024

---

There may be times you need to work at a location where there is no internet connection. With Offline Mode, you can work on a site in DevKinsta without an internet connection.

When using Offline Mode, there’s some important information and limitations to keep in mind:

- Docker Images need to be downloaded before working in Offline Mode. If you try to start DevKinsta without the necessary Docker Images, you’ll see an error message that there is no internet connection and you are currently offline.
- WordPress Versions are limited to versions previously downloaded during site creation. This means you can only create or switch to WordPress versions that you previously installed at least once in DevKinsta.
- Logging in to MyKinsta, Sync (push and pull), and any application updates will not be available.

## Running DevKinsta in offline mode

Start DevKinsta as usual. If you do not have an internet connection, you’ll see a notification in the upper right corner that you are currently offline.

If you want to test Offline Mode before traveling to a location without internet, you can temporarily turn off your internet connection and open DevKinsta in Offline Mode.

![Running DevKinsta in Offline Mode.](https://kinsta.com/wp-content/uploads/2023/11/devkinsta-offline-mode-1.png)

Running DevKinsta in Offline Mode.

Other than the limitations listed above, you can work on and run your site(s) in DevKinsta as usual.

## Troubleshooting

When starting DevKinsta, if you see an error message that you are offline and DevKinsta is unable to load, this means Docker Images are missing. You’ll need to reconnect to the internet and download the missing Docker images. Once those are downloaded, you can work in Offline Mode in DevKinsta (without an internet connection).
