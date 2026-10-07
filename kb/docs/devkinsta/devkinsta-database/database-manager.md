---
url: "https://kinsta.com/docs/devkinsta/devkinsta-database/database-manager/"
title: "Database Manager"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-database"
section: ["DevKinsta", "Database Management"]
kinsta_last_updated: "2024-08-19T12:21:44"
change_signal: "2024-08-19T12:21:44"
fetched_at: "2026-10-07T22:58:19Z"
sha256: "aa3b540f29b7d542ef640003b7f8ce2c06621e9c109f50b442f1db69ae2fab94"
body_chars: 3277
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Database Manager

**Section:** DevKinsta > Database Management
**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-database/database-manager/
**Kinsta last updated:** 2024-08-19T12:21:44

## On this page

- [Accessing your database](#accessing-your-database)
- [Basic usage](#basic-usage)
  - [Switching databases](#switching-databases)
  - [Viewing table structure](#viewing-table-structure)
  - [Viewing table data](#viewing-table-data)
  - [Manipulating data](#manipulating-data)
- [Via command line](#via-command-line)
  - [Enter through Virtual Machine](#enter-through-virtual-machine)
  - [Enter through host machine](#enter-through-host-machine)

---

[Adminer](https://kinsta.com/blog/adminer/) is a user interface for managing your database. It is similar to phpMyAdmin but has a reduced footprint and is snappier to work with. For documentation see the [Adminer website](https://www.adminer.org/).

![Adminer user interface](https://kinsta.com/wp-content/uploads/2021/01/adminer-1024x570.png)

Adminer user interface

## Accessing your database

You can access your site’s database in three ways.

- Click on the **More** menu (kebab/three-dot) in the site list and select **Open database manager**.
- Click the **Database manager** button at the top of the **Site info** page.
- Database manager is available through [the host machine](#enter-through-host-machine) on port `15100` on your site’s IP (which you can find on the **Site info** page).

## Basic usage

### Switching databases

When you visit Adminer by clicking a button in DevKinsta, you are always taken to the appropriate database automatically, but you can switch between them within Adminer as well. You can switch between databases using the dropdown at the top of the left-hand sidebar.

### Viewing table structure

Clicking on any table name in the sidebar will take you to the structure view of that table. You can see each field and the type of data it holds.

### Viewing table data

Clicking **SELECT** in the sidebar next to the table name will take you to a page that shows you the first 50 items within that table. You can dive into different parts of the table using the controls at the top of the page.

![Adminer select data](https://kinsta.com/wp-content/uploads/2021/01/adminer-select-1024x268.png)

Adminer select data

You need to click the blue title above the boxes to gain access to the forms they contain. You can then set up views using multiple select, search, sort, limit, and text length directives. Note that your searches are mapped to the URL so you can save views by bookmarking the page.

If you need a more elaborate SQL query to view data, you can click **Edit** next to the query displayed at the top of the screen to gain access to an SQL editor.

### Manipulating data

You can edit any row by clicking the edit link within the results. When on the select data page you can add new items by clicking the **NEW ITEM** button. This will give you a form with all the fields to fill out.

You can run complex SQL queries by clicking the **SQL COMMAND** link at the top of the sidebar. This will take you to the SQL editor where you can type your query. Clicking **History** in the box below the editor will bring up recently run commands you can load up.

## Via command line

If you’d like to access your database via the terminal/command line, you can do that.

### Enter through Virtual Machine

Enter the `devkinsta_db` container:

```
docker exec -it devkinsta_db bash
```

Connect to the database:

```
mysql -h localhost -u root -p
```

Run SQL commands like:

```
show databases;
```

### Enter through host machine

You can find this information on the **Site** info page.

![DevKinsta database details.](https://kinsta.com/wp-content/uploads/2023/11/devkinsta-database-info-1024x371.png)

DevKinsta database details.

Enter the database directly from the host OS:

```
mysql -h 192.168.99.254 -P 15100 -u root -p
```
