---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/"
title: "Troubleshooting"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-troubleshooting"
section: ["WordPress Hosting"]
kinsta_last_updated: "2026-01-21T10:45:09"
change_signal: "2026-01-21T10:45:09"
fetched_at: "2026-10-07T22:58:19Z"
sha256: "160a89d3374815323d0670c080ddd787ea04a89254e49b1e86251828c10abd2d"
body_chars: 2555
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Troubleshooting

**Section:** WordPress Hosting
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/
**Kinsta last updated:** 2026-01-21T10:45:09

---

The WordPress troubleshooting section of our documentation helps you to identify any issues with your site, explains how to improve the site’s performance, and guides you through what to do if you encounter an error. It includes:

- [Server Logs](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/): Explains how to access and download your server logs, what each log file contains, and the formats.
- [Debugging](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/wordpress-debugging/): How to enable debug mode in WordPress to troubleshoot and identify any issues with your site.
- [Troubleshooting Performance](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/troubleshooting-wordpress-performance): How to troubleshoot common performance issues on your site.
- [Speed and Load Testing](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/website-testing-tools): How to perform speed and load testing before making your site live.
- [Cloudflare Errors](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/cloudflare-errors): This explains what to do when you get errors 520, 521, or 1020.
- [Server Errors](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/server-errors): How to fix errors 502 and 504.
- [Database Connection Errors](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/fix-error-establishing-a-database-connection-in-wordpress): What to do when you can’t connect to your database.
- [SSH and SFTP Errors](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/cant-connect-delete-ssh-known-hosts): What to do when you can’t connect via SSH or SFTP.

### Plugin or theme issues

If a plugin or theme uses its own caching and you’re seeing issues, such as resources loading from old URLs, missing updates, or layout problems, try clearing that plugin or theme cache first before clearing the site cache. For instructions, refer to the plugin or theme’s documentation. For example, the Avada theme maintains its own CSS and JS cache and [provides documentation about how to manage it](https://avada.com/documentation/general-cache-information/).

If your theme or plugin also includes CSS or JS optimization features separate from caching, regenerate those files and then clear the plugin or theme cache before clearing the server cache. For instance, Avada includes a Critical CSS feature and recommends regenerating it after updates, followed by clearing both plugin and server caches.
