---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/"
title: "WordPress Hosting - Troubleshooting"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-troubleshooting"
section: []
kinsta_last_updated: "January 21, 2026"
sitemap_lastmod: "2026-01-21T10:45:09+00:00"
fetched_at: "2026-10-07T22:37:52Z"
sha256: "7056da771e67a23edfd921453788629c588924215dcbb9036f4af4519582b303"
body_chars: 2561
extracted_with: "main article"
status: "live"
---

# WordPress Hosting - Troubleshooting

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/
**Kinsta last updated:** January 21, 2026

---

The WordPress troubleshooting section of our documentation helps you to identify any issues with your site, explains how to improve the site’s performance, and guides you through what to do if you encounter an error. It includes:

- [Server Logs](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/): Explains how to access and download your server logs, what each log file contains, and the formats.
- [Debugging](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/wordpress-debugging/): How to enable debug mode in WordPress to troubleshoot and identify any issues with your site.
- [Troubleshooting Performance](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/troubleshooting-wordpress-performance/): How to troubleshoot common performance issues on your site.
- [Speed and Load Testing](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/website-testing-tools/): How to perform speed and load testing before making your site live.
- [Cloudflare Errors](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/cloudflare-errors/): This explains what to do when you get errors 520, 521, or 1020.
- [Server Errors](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/server-errors/): How to fix errors 502 and 504.
- [Database Connection Errors](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/fix-error-establishing-a-database-connection-in-wordpress/): What to do when you can’t connect to your database.
- [SSH and SFTP Errors](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/cant-connect-delete-ssh-known-hosts/): What to do when you can’t connect via SSH or SFTP.

### Plugin or theme issues

If a plugin or theme uses its own caching and you’re seeing issues, such as resources loading from old URLs, missing updates, or layout problems, try clearing that plugin or theme cache first before clearing the site cache. For instructions, refer to the plugin or theme’s documentation. For example, the Avada theme maintains its own CSS and JS cache and [provides documentation about how to manage it](https://avada.com/documentation/general-cache-information/).

If your theme or plugin also includes CSS or JS optimization features separate from caching, regenerate those files and then clear the plugin or theme cache before clearing the server cache. For instance, Avada includes a Critical CSS feature and recommends regenerating it after updates, followed by clearing both plugin and server caches.
