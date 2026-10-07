---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-banned-incompatible-plugins/"
title: "Plugins and Themes - Banned and Incompatible Plugins"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-plugins-themes"
section: []
kinsta_last_updated: "June 3, 2026"
sitemap_lastmod: "2026-06-03T09:01:16+00:00"
fetched_at: "2026-10-07T22:39:06Z"
sha256: "fd50956115b52a97e9b408e7de6bb177be575b61798f92fd6d87af49a26b4c7e"
body_chars: 8070
extracted_with: "main article"
status: "live"
---

# Plugins and Themes - Banned and Incompatible Plugins

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-banned-incompatible-plugins/
**Kinsta last updated:** June 3, 2026

## On this page

- [Banned plugins](#banned-plugins)
  - [Caching plugins](#caching-plugins)
  - [Backup plugins](#backup-plugins)
  - [Image optimization plugins](#image-optimization-plugins)
  - [Video conversion plugins](#video-conversion-plugins)
  - [Performance plugins](#performance-plugins)
  - [Misc plugins](#misc-plugins)
  - [Security plugins](#security-plugins)
  - [Social media plugins](#social-media-plugins)
- [Nulled plugins](#nulled-plugins)
- [Incompatible plugins](#incompatible-plugins)
- [Wordfence](#wordfence)
- [Complete list](#complete-list)

---

Our platform at Kinsta is optimized for reliability, performance, and security. Because of this, there are some plugins that are not allowed or won’t work properly in the Kinsta environment. Generally speaking, we don’t allow caching, backup, or related posts plugins.

If a plugin is on our list, it’s because our sysadmin team has identified an issue with it. These problems are typically tied to performance or functionality. We are always working with third-party plugin developers to ensure compatibility with our platform. For example, WP Rocket used to be on our banned list, and now we are partners with them.

If you try to install a banned plugin, you will receive a warning message, and the installation will be blocked.

## Banned plugins

### Caching plugins

Using caching plugins will deteriorate performance and, in most cases, will not work on our platform. We already have different types of server-level caching implemented, both object caching and page caching, which is much better than any plugin can do on a PHP level. Learn more about how we handle [WordPress caching](https://kinsta.com/blog/wordpress-cache/).

- Cache Enabler

### Backup plugins

Kinsta already provides daily [automatic backups](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#wordpress-backups) and [downloadable backups](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#wordpress-backups) for all your sites on your account; therefore, backup plugins are not needed in most cases. They can also cause unnecessary performance issues and eat up your bandwidth.

Note: This list is not exhaustive;**all non-incremental backups are not allowed**.

- All-in-One WP Migration
- BackupBuddy
- BackWPup version 5.5 and below. BackWPup **version 5.6.0 and above is allowed** on Kinsta.
- Duplicator Pro
- Snapshot
- Updraft
- WP DB Backup
- WP DB Backup Made

If you do want to save backups offsite, see our post on [incremental backup plugins](https://kinsta.com/blog/wordpress-backup-plugins/) you can use at Kinsta. Incremental backups are where the backups are only made when changes have been made to a file or database tables. If you want to migrate your site to Kinsta using a migration plugin, we recommend using the free version of [Duplicator](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrate-wordpress-duplicator-plugin/) or [Migrate Guru](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrate-guru/). These plugins offer specific options for migrating your site as opposed to using a backup file. You can also refer to our blog post for [Migrating a WordPress site manually](https://kinsta.com/blog/migrate-wordpress-site/#migrating-a-wordpress-site-manually).

### Image optimization plugins

We do not allow **server-based** image optimization plugins or packages/software due to performance impacts. This also includes the installation of packages to be used by image optimization scripts. Our post on [image optimization](https://kinsta.com/blog/optimize-images-for-web/) contains plenty of WordPress plugins you can use that compress images on third-party cloud servers. These are fine to use at Kinsta.

### Video conversion plugins

We do not allow **server-based** video conversion and compression plugins or packages/software. This includes packages like FFmpeg, which may be required by some WordPress plugins. If your WordPress site requires video encoding functionality, we recommend integrating an external service like [Cloudinary](https://cloudinary.com/blog/automatic_video_transcoding).

### Performance plugins

- Better WordPress Minify
- P3 Profiler
- Optimize Database after Deleting Revisions
- WordPress [GZIP Compression](https://kinsta.com/blog/enable-gzip-compression/): GZIP is already enabled on all Kinsta servers.
- JCH Optimize (reasons: constant PHP stress, high bandwidth usage, can’t cache, can’t optimize for CDN)

### Misc plugins

- Allow PHP Execute
- Exec-PHP
- Inactive User Deleter
- Pipdig Power Pack (P3)
- WP RSS Multi Importer
- WordPress Popular Posts

### Security plugins

A lot of security plugins cause performance issues due to their always-on and scanning functionalities. At Kinsta, our infrastructure configuration and Cloudflare integration may impact the functionality of certain features in security plugins like IP blocking, geolocation-based rules, and more.

If your site is hosted at Kinsta, you don’t need to install a third-party security plugin because we have many popular security features built into our [MyKinsta dashboard](https://kinsta.com/mykinsta/) and infrastructure. For example, our [IP Deny tool](https://kinsta.com/docs/wordpress-hosting/site-management/block-ip-address/) lets you block rogue IP addresses before traffic hits your WordPress application, and we have a variety of rate limits set on popular WordPress endpoints. Our [free Cloudflare integration](https://kinsta.com/cloudflare-integration/) also includes additional security features like a secure firewall with a customized ruleset, [DDoS protection](https://kinsta.com/blog/what-is-a-ddos-attack/), and more.

If you’re not hosted on Kinsta, we recommend utilizing a proxy solution such as [Cloudflare](https://kinsta.com/blog/install-cloudflare/) or Sucuri in front of your site if you need extra protection or help to decrease malicious and bot traffic.

### Social media plugins

- Facebook Instant Articles & Google AMP Pages by PageFrog
- Facebook Open Graph, Google+ and Twitter Card Tags

## Nulled plugins

[Nulled plugins](https://kinsta.com/blog/nulled-wordpress-plugins-themes/) typically refer to premium WordPress plugins or themes that [have been hacked](https://kinsta.com/blog/wordpress-hacked/) or contain modified code designed to cause harm or collect information. These are obtained from a third-party website (not the original author or creator) and sometimes are made to work without a license key.

We offer a [free hack-fix guarantee here at Kinsta](https://kinsta.com/wordpress-hosting/security/), but this guarantee doesn’t apply if you’re using a nulled plugin.

## Incompatible plugins

- WooCommerce Amazon & eBay Integration: Requires PHP function `proc_open` which is disabled in our environment due to security reasons.

## Wordfence

[Wordfence](https://kinsta.com/blog/wordpress-security-plugins/#3-wordfence-security) is a free WordPress security plugin designed to protect WordPress websites from online threats, such as malware, hacking attempts, and other security vulnerabilities. It includes an endpoint firewall (WAF), a malware scanner, login security features, live traffic, and rules-based blocking. 

If you’re using Wordfence at Kinsta, it requires additional configuration to optimize the firewall. [Contact our Support team](https://kinsta.com/docs/support/contact-support/) to get the auto-prepend settings for the Wordfence setup. For more information, refer to the [Wordfence documentation](https://www.wordfence.com/help/firewall/optimizing-the-firewall/#on-kinsta).

It’s important to note that while Wordfence is a powerful security tool, no security plugin can provide absolute protection. You should also follow best practices for WordPress security, such as keeping plugins and themes updated, using strong passwords, and regularly backing up your websites.

## Complete list

Feel free to compare the list below against your current `/wp-content/plugins/` directory. Note: the `updraft` plugin listed here is a different plugin from Updraft Plus.

Copy

```
all-in-one-wp-migration
allow-php-execute
amazon-ebay-integration
backupbuddy
backwpup-pro
bwp-minify
cache-enabler
codistoconnect
duplicator-pro
exec-php
inactive-user-deleter
jch-optimize
login-wall
p3
p3-profiler
pagefrog
rvg-optimize-database
sg-cachepress
snapshot
updraft
wonderm00ns-simple-facebook-open-graph-tags
woocommerce-amazon-ebay-integration
wordpress-gzip-compression
wordpress-popular-posts
wp-rss-multi-importer
wp-db-backup
wp-db-backup-made
```
