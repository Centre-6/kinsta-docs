---
url: "https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/mykinsta-search-replace-tool/"
title: "Search and Replace"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "mykinsta-tools"
section: ["WordPress Hosting", "Tools"]
kinsta_last_updated: "2024-08-13T09:56:47"
change_signal: "2024-08-13T09:56:47"
fetched_at: "2026-10-07T22:58:20Z"
sha256: "fc96c9f79762b048ccdaee4de155e68c848787ddd0f317236fdcc6def269b7e8"
body_chars: 9059
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Search and Replace

**Section:** WordPress Hosting > Tools
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/mykinsta-search-replace-tool/
**Kinsta last updated:** 2024-08-13T09:56:47

## On this page

- [How to use the search and replace tool in MyKinsta](#how-to-use-the-search-and-replace-tool-in-mykinsta)
- [Troubleshooting](#troubleshooting)
  - [Tips and notes](#tips-and-notes)
  - [Data too long](#data-too-long)
  - [Skipping an uninitialized class](#skipping-an-uninitialized-class)
- [Tips and examples](#tips-and-examples)
  - [Tips](#tips)
  - [Examples](#examples)
    - [Replace www.www.domain.com with www.domain.com](#replace-wwwwwwdomaincom-with-wwwdomaincom)
    - [Replace email address domain only](#replace-email-address-domain-only)
    - [Replace http URLs with https URLs](#replace-http-urls-with-https-urls)
    - [Replace custom domain with temporary domain](#replace-custom-domain-with-temporary-domain)

---

In [MyKinsta](https://my.kinsta.com/), you can find a handy tool for doing a search and replace on your site’s content without having to install a plugin, install a script, or use the command line.

**Note:** When a search and replace is performed, we automatically create a [system-generated backup](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/) in MyKinsta that can be restored if needed (**Sites** > ***sitename*** > **Backups** **> System generated**).

## How to use the search and replace tool in MyKinsta

To locate this tool, log in to MyKinsta, click on**Sites** in the left sidebar, and click on the name of the website you want to run the search and replace on:

Click on the **Tools** tab, look for or scroll to the **Search and replace** section, and click **Search and replace**.

![Search and replace button in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/06/wordpress-tools-search-replace.png)

Search and replace button in MyKinsta.

There are a number of different operations you can use this tool for. In this example, we’ll change some URLs that use “http” to ones using “https” in the database.

In the search field, enter the value you want to look for in the database, and hit **Search**. The search and replace tool will display the number of occurrences for the given string:

![Using the search field in the search and replace tool.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-search-replace-search-1024x434.png)

Using the search field in the search and replace tool.

![Completed search in the search and replace tool.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-search-replace-results-1024x479.png)

Completed search in the search and replace tool.

To search and replace, check the **Replace** box and enter the new text, URL, or other value in the **Replace with** field:

![Searching for an old URL and replacing it with a new URL with the search and replace tool in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-search-replace-replace-1024x700.png)

Searching for an old URL and replacing it with a new URL with the search and replace tool in MyKinsta.

We recommend leaving the **Clear cache** **when ready** box checked to automatically purge your site’s cache after the search and replace process. That way, visitors will see the updated version of your website right away. Then, click the **Replace** button.

After the WordPress search and replace is complete, you’ll see a confirmation dialog showing the number of replacements that were processed. When you’re done, click **Cancel** or the **X** in the upper right corner of the modal/pop-up to exit the tool. That’s it!

## Troubleshooting

When doing a search and replace, there are a couple of errors that may occur that will need some work on your part (or your developer) to resolve. If the fixes shown below do not resolve the issue or if you aren’t comfortable working with [WP-CLI](https://kinsta.com/blog/wp-cli/), we recommend [working with a developer](https://kinsta.com/blog/hire-wordpress-developer/).

### Tips and notes

- We recommend making a backup or exporting a copy of the database before running search-replace and making changes to your database.
- The WP-CLI `export` command can be used to export a copy of your database.
- Running the WP-CLI search-replace command with the `--dry-run` flag first can help you get a better understanding of what will be changed before actually making any changes.
- If errors appear in a search and replace that’s part of [pushing staging to live](https://kinsta.com/docs/wordpress-hosting/staging-environment/#push-staging-to-live-1), the push to live will not complete. In this case, to push staging to live, you’ll need to do one of the following:
  - Resolve any issues in the staging environment’s database before pushing to live.
  - Push staging to live without the Run Search & Replace option checked and perform the search and replace manually after the push completes.

### Data too long

This error happens when trying to update a column with a string longer than the value allowed and will look something like:

> Data too long for column ‘guid’ at row 1

To work around or fix this, you can try one of the following:

- Run a [search-replace with WP-CLI](https://developer.wordpress.org/cli/commands/search-replace/) and skip the affected column with the `--skip-columns` flag (e.g. `--skip-columns=guid`).
- Work with a developer to alter the column and increase the length allowed for the value.

### Skipping an uninitialized class

This error usually happens when search and replace encounters an object it needs to load the class for in order to interpret the object, but the plugin or theme the class comes from cannot be loaded correctly. It will look something like:

> Skipping an uninitialized class “Some_PHP_Class”, replacements can not be completed.

To work around this error, you can try running a [search-replace with WP-CLI](https://developer.wordpress.org/cli/commands/search-replace/). If that fails, try the search-replace with WP-CLI again and add the `--skip-plugins --skip-themes` flags to the command.

## Tips and examples

Now that we know how to use the search and replace tool, let’s go over some tips and examples.

### Tips

- As also noted above, searching is **case sensitive**, so searching for “WordPress” is different from searching for “wordpress.”
- When replacing URLs, best practice is to either include the full URL, including the protocol (http:// or https://), or at least the leading forward slash before the domain (e.g. /example.com). This prevents unintentionally changing the domain of email addresses.
- You can search and replace entire sentences, including spaces and punctuation.
- For custom site configurations like Bedrock, or in the case of a plugin or theme error, the search and replace tool may not be able to complete. For these situations, we recommend trying the [WP-CLI search-replace](https://kinsta.com/blog/wordpress-search-and-replace/#4-perform-the-search-and-replace-directly-with-wpcli) command with the `--skip-plugins` and/or `--skip-themes` flags as needed.
- Some plugins and/or themes may have their own search and replace tools that will need to be used due to the way they save information in the database. A few popular examples are:
  - [BeTheme Muffin Content Builder](https://forum.muffingroup.com/betheme/discussion/12/muffin-content-builder-migrate-tool-3-0-change-builder-paths-for-images-etc-while-site-migration)
  - [OptimizePress](https://help.optimizepress.com/article/1085-update-url-references-after-moving-domain)

- If your plugin or theme has its own built-in cache, you’ll need to clear that cache after doing a search and replace. Some popular examples are:
  - [Beaver Builder](https://docs.wpbeaverbuilder.com/beaver-builder/troubleshooting/debugging/issue-fixer-clear-the-cache/)
  - [Divi](https://divitheme.net/clear-divi-cache/)
  - [WPML](https://wpml.org/documentation/support/wpml-troubleshooting-options/)

- Speaking of cache, if your search and replace doesn’t seem to have updated your site, you may have additional caching besides the server cache handled by Kinsta. You’ll want to make sure you clear all cache in this order:
  - Clear any built-in theme or plugin cache.
  - Clear site/server cache (yes, clear this again if you cleared any theme or plugin cache).
  - Clear browser cache.

### Examples

Be sure to replace the example domains as needed.

#### Replace www.www.domain.com with www.domain.com

This can happen if you already had some instances of www.domain.com in your site’s content, then switched the primary domain from domain.com to www.domain.com in MyKinsta, and checked the box to **Run search and replace after change**.

**Search:** /www.www.domain.com

**Replace with:** /www.domain.com

#### Replace email address domain only

Maybe you want to use a shorter version of your domain for email sending and receiving or, for some other reason, need to replace the domain of email addresses only without affecting any other instances of the domain (e.g. in image URLs or links).

**Search:** @olddomain.com

**Replace with:** @newdomain.com

#### Replace http URLs with https URLs

While you can redirect [HTTP to HTTPS in MyKinsta](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/#redirect-http-to-https-in-mykinsta) for your primary domain, you may want to update all URLs in your content as well, or there may be other URLs besides the primary domain you want to change.

**Search:** http://domain.com

**Replace with:** https://domain.com

#### Replace custom domain with temporary domain

If you want to replace one domain with another in your site’s database without affecting email addresses, here’s how. Note the leading forward slash (/) and be sure to replace **olddomain.com** and **newdomain.com** with your old and new domains, respectively.

**Search:** /olddomain.com

**Replace:** /newdomain.com
