---
url: "https://kinsta.com/docs/devkinsta/devkinsta-site-management/"
title: "Site Management"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-site-management"
section: ["DevKinsta"]
kinsta_last_updated: "2026-02-18T05:53:45"
change_signal: "2026-02-18T05:53:45"
fetched_at: "2026-10-07T22:58:19Z"
sha256: "dce1b9d79484fa06205de26603c830225bf356ae62738dd42b3821c0c85f1364"
body_chars: 5749
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Site Management

**Section:** DevKinsta
**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-site-management/
**Kinsta last updated:** 2026-02-18T05:53:45

## On this page

- [The Sites list](#the-sites-list)
  - [Search, filter, and sort the Sites list](#search-filter-and-sort-the-sites-list)
- [The Site info page](#the-site-info-page)
  - [Basic site information](#basic-site-information)
  - [Site status](#site-status)
  - [Top level domain](#top-level-domain)
  - [HTTPS](#https)
  - [Database details](#database-details)
  - [WordPress specific settings](#wordpress-specific-settings)
- [The site itself](#the-site-itself)
  - [HTTPS](#https)
- [Files](#files)
- [WordPress backend (WP Admin)](#wordpress-backend-wp-admin)
- [Database management](#database-management)
- [Email inbox](#email-inbox)
- [Logging](#logging)

---

Once a site is created, you can modify it as you would expect. You can view information about your sites in two locations, the **Sites** list and the **Site info** page.

## The Sites list

The **Sites** list is your development center where you can see everything you’re working on at the moment.

![Sites list in DevKinsta.](https://kinsta.com/wp-content/uploads/2023/11/devkinsta-sites-1024x342.png)

Sites list in DevKinsta.

The list shows you some at-a-glance details like WordPress and PHP versions and site size. You can open the site or the site folder with quick buttons, or you can click the kebab (three-dot) menu next to each site to [**clone a site**](https://kinsta.com/docs/devkinsta/devkinsta-getting-started/creating-a-site#clone-a-site) or access the **database manager** and other tools.

You can click on any site to go to the **Site info** page, where you’ll find more information and tools.

### Search, filter, and sort the Sites list

When viewing 10 or more sites, fields for searching, filtering, and sorting sites will appear above the sited list:

- Begin typing in the search field to narrow the list by site name.
- The filter tabs can be used to narrow the list by running or stopped sites. Set this back to **All** to show all sites.
- Use the sort field to sort the list by date added or alphabetically; in either ascending or descending order.

## The Site info page

Each site’s info page contains access information, quick buttons for tools, and built-in features such as the `WP_DEBUG` switcher.

![Site info page in DevKinsta.](https://kinsta.com/wp-content/uploads/2023/11/devkinsta-dashboard.png)

Site info page in DevKinsta.

### Basic site information

- Site Type
- Site Host
- Site Name
- Webserver
- PHP Version
- Database
- Site Path

### Site status

- Start or stop your site

### Top level domain

- Change the [top-level domain](https://kinsta.com/blog/what-is-a-tld/#what-is-a-tld-explained-in-more-detail) for the site

### HTTPS

- Enable or disable HTTPS

### Database details

- Host
- Port
- Database Name
- Username
- Password
- Socket
- Size

### WordPress specific settings

- Version
- WordPress Multisite
- Enable or disable `WP_DEBUG`
- Enable or disable `WP_AUTO_UPDATE`

## The site itself

Your site can be reached using any of the following:

- the open site icon next to each site in the **Sites** list,
- by clicking **Open site** on the **Site info** page,
- by visiting the site’s URL (which you can find under **Site Host** on the **Site** info page).

### HTTPS

You can visit your local sites through HTTPS by enabling SSL and HTTPS. First, open the **Site info** page and turn on **HTTPS**. Behind the scenes, a self-signed certificate will be generated and stored in the host OS. DevKinsta writes to the local keystore, and for this operation, it needs permission. On macOS, type your password; on Windows, accept the confirmation dialog.

![Activate SSL and HTTPS on your site in DevKinsta. ](https://kinsta.com/wp-content/uploads/2023/11/devkinsta-ssl-https-1024x765.png)

Activate SSL and HTTPS on your site in DevKinsta.

**Note:** If you’re using Firefox and see an [SSL error](https://kinsta.com/blog/ssl_error_rx_record_too_long/) when trying to view your site, here are the steps to solve that issue in Firefox on Windows:

1. Type **about:config** in the address bar and press **Enter**.
2. A warning page may appear. Click **Accept the Risk and Continue** to go to the about:config page.
3. Type **security.enterprise_roots.enabled** in the **Search** field.
4. Click the toggle button next to the preference **security.enterprise_roots.enabled** to change its value from false to **true**.
5. Restart Firefox

For more details and solutions for other operating systems, see Firefox’s guide to [Setting Up Certificate Authorities (CAs) in Firefox](https://support.mozilla.org/en-US/kb/setting-certificate-authorities-firefox).

## Files

All of your PHP files, WordPress theme, and dependencies are located in your default site folder.

- `C:\Users\username\DevKinsta\sitename` is the default directory for Windows users.
- `/users/username/DevKinsta/sitename` is the default folder for Mac users.

You can change the default site folder in [Settings](https://kinsta.com/docs/devkinsta/settings).

## WordPress backend (WP Admin)

You can reach the WordPress dashboard by:

- clicking the WordPress icon in the **Sites** list,
- clicking the **WP Admin** button on the site detail page,
- or visiting it in your browser (the WordPress dashboard can be accessed by appending “/wp-admin” to your site’s URL).

## Database management

Adminer is a database management tool and can be accessed by:

- clicking the kebab (three-dot) icon in the **Sites** list and selecting **Open database Manager** in the dropdown menu,
- or clicking the **Database manager** button on the **Site** info page.

For more information about Adminer, see our [Database Manager](https://kinsta.com/docs/devkinsta/devkinsta-database/database-manager) guide.

## Email inbox

DevKinsta catches all emails that are sent by your site. You can manage emails site by site. More details are available in our [Email Inbox](https://kinsta.com/docs/devkinsta/devkinsta-site-management/email-inbox) article.

![DevKinsta Email inbox.](https://kinsta.com/wp-content/uploads/2023/11/devkinsta-email-inbox.png)

DevKinsta Email inbox.

## Logging

Both **access.logs** and **php-fpm.logs** are available for debugging and troubleshooting your site locally. Navigate to the **DevKinsta/logs/** folder to view site logs. Every site’s separate log file can be viewed in your favorite text editor. Head over to [Logging](https://kinsta.com/docs/devkinsta/devkinsta-troubleshooting/logging). to learn more.
