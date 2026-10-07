---
url: "https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database/"
title: "Database Management - Database"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "database-management"
section: []
kinsta_last_updated: "December 22, 2025"
sitemap_lastmod: "2025-12-22T10:18:31+00:00"
fetched_at: "2026-10-07T22:39:09Z"
sha256: "18778e480b12996b2347d04f73baeba0ee32da4da1acbad18b476bae1edc36fb"
body_chars: 7057
extracted_with: "main article"
status: "live"
---

# Database Management - Database

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database/
**Kinsta last updated:** December 22, 2025

## On this page

- [Sort and filter your data](#sort-and-filter-your-data)
- [Export your database](#export-your-database)
- [SQL console](#sql-console)
  - [Example SQL queries](#example-sql-queries)
    - [List all users](#list-all-users)
    - [Get all published posts](#get-all-published-posts)
    - [Get all pages](#get-all-pages)
    - [Get all approved comments](#get-all-approved-comments)
    - [Delete all spam comments](#delete-all-spam-comments)
- [Edit a value](#edit-a-value)
- [Add a record](#add-a-record)
- [Add a table](#add-a-table)
- [Settings](#settings)
- [Report a bug](#report-a-bug)

---

With MyKinsta’s database manager, you can manage your site’s MySQL database right from the MyKinsta UI. The database manager lets you run queries, view and edit data, add records and tables, and more, all without needing to use an external tool or download your database.

To access the database manager, navigate to **Sites** > ***Site Name****>* **Database**. When you first access it, a warning appears to advise you to proceed with caution and use a staging environment to test your changes before making them live. To stop this message from appearing, select **Don’t show me this warning again**. To access the database manager, click **Open Database**.

![Access the database manager.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-database.png)

Access the database manager.

![WordPress database manager in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-database-open.png)

WordPress database manager in MyKinsta.

## Sort and filter your data

Within the database manager, you can sort the columns by using the arrows at the top of each column; you can also choose which columns you want to show using the **Columns** option. You can use **Filters** to display specific data, and you can apply multiple filters simultaneously. When a filter is applied, an exclamation point appears on the **Filters** option.

![Apply filters to your database to show specific data.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-database-filter.png)

Apply filters to your database to show specific data.

To open and edit the filter within the [SQL console](#sql-console), click **Open in SQL**.

![Database SQL editor.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-database-filter-sql.png)

Database SQL editor.

You can create customized views of your database for easier access to the data you need. Click the plus icon, then select **Create View**. From there, you can give your view a name, choose the tables and columns to display, and apply any necessary conditions. Any views you create can be accessed in the **Database studio** option.

![Create a new view for your database.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-database-create-view.png)

Create a new view for your database.

To open and edit the view within the [SQL console](#sql-console), click **Open in SQL console**.

## Export your database

Within the database manager, you can export your entire database or just selected data to a `.json`, `.csv`, or `.xlsx` file. To export your data, click the ellipsis (three-dots) and choose the file type you want to export to.

![Export your database.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-database-export.png)

Export your database.

## SQL console

Within the database manager, you can access an SQL console where you can run SQL queries on your database. The SQL editor lets you view the **Database Schema**, **Prettify** the code for better readability, and **Run** the SQL directly in the console. When you run the SQL query, you can choose to show the results as a table or as JSON, and export the results to a `.json`, `.csv`, or `.xlsx` file. You can also store these queries as snippets and create folders to organise the snippets.

![Database SQL console.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-database-sql-console.png)

Database SQL console.

### Example SQL queries

The following are examples of SQL queries you may want to run in your WordPress database.

#### List all users

Copy

```
SELECT ID, user_login, user_email, user_registered FROM wp_users;
```

#### Get all published posts

Copy

```
SELECT ID, post_title, post_date FROM wp_posts WHERE post_type = 'post' AND post_status = 'publish';
```

#### Get all pages

Copy

```
SELECT ID, post_title FROM wp_posts WHERE post_type = 'page';
```

#### Get all approved comments

Copy

```
SELECT comment_ID, comment_author, comment_content FROM wp_comments WHERE comment_approved = 1;
```

#### Delete all spam comments

Copy

```
DELETE FROM wp_comments WHERE comment_approved = 'spam';
```

## Edit a value

To edit a value within a record, double-click the cell containing the value you want to change. You can then delete the cell’s contents and enter the required value, or simply type over the existing data.

![Edit a value in your database.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-database-edit-value.png)

Edit a value in your database.

After making your changes, press Enter. The updated cell will be highlighted in yellow to indicate that a change has been made. To apply the changes to your database, click **Save x change(s)**. If you decide not to keep the changes, click **Discard changes** instead.

![Save changes to the values in your database.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-database-edit-value-save.png)

Save changes to the values in your database.

## Add a record

To add a record to your database, click **Add record**, enter the required data into the table, and click **Save x change(s)**.

![Add a record to your database table.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-database-add-record.png)

Add a record to your database table.

## Add a table

To add another table to your database, click the plus icon and then **Create Table**. You can then name the table and define its columns, specifying the data type, constraints, default values, and expressions for any generated data. Additionally, you can add table-level constraints and indexes as needed. You can view all of the database tables, within **Database studio**.

![Add a new table to your database.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-database-add-table.png)

Add a new table to your database.

Once you’ve added the required columns, click **Review and create**, this will show you the SQL for the new table, if this looks correct, click **Create table**.

## Settings

The following settings are available within the database manager:

- **Table rows count:** Displays the total number of rows in each table. This action performs a light scan of the table, which may slow down performance, particularly for large tables or databases with many rows.
- **Expand subviews:** If a table contains a foreign key to another table, you can open the related data in a subview. This option keeps subviews open, allowing you to easily explore related records without navigating away.
- **Pagination type:** Choose how you want to view the results, **Limit offset** allows you to determine how many rows are shown per page, **Pages** shows the rows in batches of 50.
- **Editor font size:** Changes the size of the font in the SQL console.
- **Editor keybindings**: Choose which keybinding profile you want to use for your keyboard shortcuts from VS Code, Vim, or Emacs.

## Report a bug

If you encounter an issue while using the Database, click **Report a bug**, you can then click **Download Error Context** and contact our [Support Team](https://kinsta.com/docs/support/contact-support/) with this information.
