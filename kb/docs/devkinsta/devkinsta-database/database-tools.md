---
url: "https://kinsta.com/docs/devkinsta/devkinsta-database/database-tools/"
title: "Database Management - External Database Tools"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-database"
section: []
kinsta_last_updated: "August 13, 2024"
sitemap_lastmod: "2024-08-13T11:21:21+00:00"
fetched_at: "2026-10-07T22:38:14Z"
sha256: "ec8d6fe64376743c7869045d300d46048f52e1a944c4394d8b832cf7afbbf2ef"
body_chars: 2612
extracted_with: "main article"
status: "live"
---

# Database Management - External Database Tools

**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-database/database-tools/
**Kinsta last updated:** August 13, 2024

---

Your WordPress database stores data required for your site to function, including information such as:

- Posts, pages, and other content.
- Comments on your posts or pages.
- Information about your site’s visitors.
- Categories and tags.
- Site settings.
- Plugin and theme data.

WordPress uses [MySQL](https://www.mysql.com/), a free, open-source database management system that enables the database to store information and provide you with access to it. When WordPress needs to update the database, it sends a MySQL ‘query’ to the database, which provides instructions about which data to update and how to update it. However, you can also directly access your database to run your own MySQL queries to perform tasks that you may not be able to do from your dashboard. For more information about the WordPress database, refer to [A Beginner’s Guide to WordPress Database: What It Is and How to Access It](https://kinsta.com/blog/wordpress-database/).

You can set up applications like [TablePlus](https://tableplus.com/) or [Sequel Ace](https://sequel-ace.com/) to access your local site’s database. All the access information you need can be found on your site’s detail page in DevKinsta.

![DevKinsta database details.](https://kinsta.com/wp-content/uploads/2023/11/devkinsta-database-info-1024x371.png)

DevKinsta database details.

## TablePlus

Create a new connection in TablePlus and select MySQL as the connection type. Add the following information to the form:

- **Name:** We recommend using the site name for ease of identification.
- **Host:** The IP of your site found under **HOST** in DevKinsta.
- **Port:** The port number under **PORT** in DevKinsta.
- **User:** Copy from the **USERNAME** field in DevKinsta.
- **Password:** Copy from the **PASSWORD** field in DevKinsta.
- **Database:** Copy from the **DATABASE NAME** field in DevKinsta.

![TablePlus Setup details](https://kinsta.com/wp-content/uploads/2023/11/devkinsta-tableplus.png)

TablePlus Setup details

## Sequel Ace

Click on Quick Connect in Sequel Ace and fill out the form with the following information:

- **Name:** We recommend using the site name for ease of identification.
- **Host:** The IP of your site found under **HOST** in DevKinsta.
- **Username:** Copy from the **USERNAME** field in DevKinsta.
- **Password:** Copy from the **PASSWORD** field in DevKinsta.
- **Database:** Copy from the **DATABASE NAME** field in DevKinsta.
- **Port:** The port number under **PORT** in DevKinsta.

![Sequel Ace Setup details](https://kinsta.com/wp-content/uploads/2023/11/devkinsta-sequelace.png)

Sequel Ace Setup details
