---
url: "https://kinsta.com/blog/wordpress-file-manager-mykinsta/"
title: "How to access and edit your WordPress files in MyKinsta (no FTP client required)"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "Web Development Tools", "How to access and edit your WordPress files in MyKinsta (no FTP client required)"]
kinsta_last_updated: "2026-07-21T13:48:05+00:00"
sitemap_lastmod: "2026-07-21T13:48:05"
fetched_at: "2026-10-07T22:42:12Z"
sha256: "ba2f3f90c03ca87af0f12d1abb1c53e4f31c6166cd6a3bfe460536a9aec83fbc"
body_chars: 15924
extracted_with: "main article"
status: "live"
---

# How to access and edit your WordPress files in MyKinsta (no FTP client required)

**Section:** Resource Center > Blog > Web Development Tools > How to access and edit your WordPress files in MyKinsta (no FTP client required)
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/wordpress-file-manager-mykinsta/
**Kinsta last updated:** 2026-07-21T13:48:05+00:00

## On this page

- [Why file access without FTP matters](#why-file-access-without-ftp-matters)
- [Accessing the file manager in MyKinsta](#accessing-the-file-manager-in-mykinsta)
- [What you can do with the file manager](#what-you-can-do-with-the-file-manager)
  - [Browse and navigate your file system](#browse-and-navigate-your-file-system)
  - [View and edit files](#view-and-edit-files)
  - [Upload files](#upload-files)
  - [Download files](#download-files)
  - [Create folders](#create-folders)
  - [Rename, move, and copy files and folders](#rename-move-and-copy-files-and-folders)
  - [Delete files and folders](#delete-files-and-folders)
  - [Bulk operations](#bulk-operations)
  - [Symlinks](#symlinks)
- [Real-world scenarios where this saves time](#real-world-scenarios-where-this-saves-time)
  - [Fixing a broken site when wp-admin is inaccessible](#fixing-a-broken-site-when-wp-admin-is-inaccessible)
  - [Editing wp-config.php](#editing-wp-configphp)
  - [Tweaking a theme file](#tweaking-a-theme-file)
  - [Removing a file that should not be there](#removing-a-file-that-should-not-be-there)
  - [Checking and downloading your error logs](#checking-and-downloading-your-error-logs)
  - [Uploading a custom plugin or theme manually](#uploading-a-custom-plugin-or-theme-manually)
- [What the file manager does not replace](#what-the-file-manager-does-not-replace)
- [Your hosting dashboard is now your file manager too](#your-hosting-dashboard-is-now-your-file-manager-too)

---

Author
:   [Joel Olawanle](https://kinsta.com/blog/author/joelolawanle/ "Posts by Joel Olawanle")

Published
:   July 22, 2026

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![](https://kinsta.com/wp-content/uploads/2026/06/how-to-access-and-edit-your-wordpress-files-in-mykinsta-1024x512.png)

It is 11 p.m., something just broke on a client site, you need to rename a plugin folder to deactivate it, but `wp-admin` is down. So you open [FileZilla](https://kinsta.com/blog/how-to-use-filezilla/), realize you never saved the [SFTP credential](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/)s, dig around for the server details, configure a new connection, wait for the directory tree to load, and finally rename a single folder.

Five minutes of setup for a five-second task. It is a workflow that has not changed much in 20 years, and it has always had more friction than it needs.

With the [MyKinsta](https://kinsta.com/mykinsta/) file manager, you can now browse, edit, upload, move, copy, delete, and manage your WordPress files directly inside your hosting dashboard, no [FTP client](https://kinsta.com/blog/best-ftp-clients/) required.

This article walks you through everything the file manager can do and covers the real-world scenarios where it saves you the most time.

## Why file access without FTP matters

FTP and SFTP are not going away. For heavy-duty tasks like bulk migrations, automated deployments, or syncing thousands of files, a dedicated client is still the right tool. But for most everyday tasks that come up while running a WordPress site, the setup overhead is disproportionate to the job.

There is also a [security reason](https://kinsta.com/blog/wordpress-plugin-vulnerability/) to avoid the most popular alternative. When people want quick file access without a client, the usual answer is a file manager plugin installed inside WordPress. It is convenient, but the security record is bad. WP File Manager, one of the most widely used options, had a [zero-day vulnerability in 2020](https://www.wordfence.com/blog/2020/09/700000-wordpress-users-affected-by-zero-day-vulnerability-in-file-manager-plugin/) that carried a CVSS score of 10.0, the maximum possible severity rating.

![700,000 WordPress users affected by file manager plugin vulnerability.](https://kinsta.com/wp-content/uploads/2026/06/700000-wordpress-file-manager-plugin-vulnerability.png)

700,000 WordPress users affected by file manager plugin vulnerability.

It allowed unauthenticated attackers to upload PHP webshells directly to the server with no login required, and it was being actively exploited in the wild on the same day it was disclosed. Over 700,000 sites were running the affected versions, according to Wordfence, which reported the issue.

The core issue is not bad code in one plugin, but the category. Any plugin that needs to read, write, and delete files across your entire [WordPress installation](https://kinsta.com/blog/install-wordpress-locally/) is doing something powerful, and powerful things inside WordPress inherit all of WordPress’s attack surface. If an attacker finds a way past the authentication layer, the file manager is exactly what they want to find waiting for them.

A hosting-level file manager sidesteps this entirely. It lives outside WordPress, is protected by your Kinsta account credentials, and adds nothing to the site’s attack surface.

## Accessing the file manager in MyKinsta

To open the file manager, go to **Sites** in the MyKinsta sidebar, select the environment you want to work on, and click the **Files** tab.

![File manager in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/06/file-manager-mykinsta.png)

File manager in MyKinsta.

The file manager opens at the `public` directory by default, which is where WordPress lives in most Kinsta installations. If your public directory has been renamed or moved, it opens at that root directory instead.

Once you are in, the interface works like a standard desktop file browser. Click a folder to open it, use the breadcrumbs at the top to navigate back up the directory tree, and use the kebab menu (the three-dot icon) next to any file or folder to see your available options.

![File manager kebab menu.](https://kinsta.com/wp-content/uploads/2026/06/file-manager-kebab-menu.png)

File manager kebab menu.

It’s also important to know that every action taken in the file manager is recorded in the MyKinsta [activity log](https://kinsta.com/docs/company-settings/activity-log/), which you can find under **User activity** in your dashboard.

![User activity tracking file manager.](https://kinsta.com/wp-content/uploads/2026/06/user-activity-tracking-file-manager.png)

User activity tracking file manager.

For teams and agencies where multiple people have access to a site, this matters more than it might seem. If a file gets renamed or deleted and something breaks, the activity log tells you exactly who made the change and when.

## What you can do with the file manager

The file manager covers the full range of tasks you would normally need a client or plugin for.

### Browse and navigate your file system

Click any folder to open it, use the breadcrumbs to move back up, and scroll through files and folders as you normally would.

Symlinks are shown alongside regular files and directories, with the link target displayed so you know exactly where they point.

![Symlinks shown alongside regular files and directories.](https://kinsta.com/wp-content/uploads/2026/06/symlinks-in-file-manager.png)

Symlinks shown alongside regular files and directories.

### View and edit files

The built-in editor supports all text-based file types, including PHP, HTML, CSS, JavaScript, JSON, XML, YAML, and SQL. To open a file in read-only mode, simply click its filename or select **View** from the kebab menu.

![View files in MyKinsta file manager.](https://kinsta.com/wp-content/uploads/2026/06/view-files-mykinsta.png)

View files in MyKinsta file manager.

If you need to make a change while viewing, click the **Edit** button directly from that window. You can also select **Edit** from the kebab menu on the file list to go straight into edit mode.

![Edit files in MyKinsta file manager.](https://kinsta.com/wp-content/uploads/2026/06/edit-files-mykinsta.png)

Edit files in MyKinsta file manager.

The editor shows numbered lines, which makes it easier to orient yourself in longer files and to reference specific lines when debugging. When you are done, click **Save changes**. The update takes effect immediately.

### Upload files

Navigate to the folder where you want the file to land and click **Upload file**. You can select multiple files at once from your computer, and they will all upload to the selected folder.

![Upload files in MyKinsta file manager.](https://kinsta.com/wp-content/uploads/2026/06/upload-files-mykinsta.png)

Upload files in MyKinsta file manager.

### Download files

Select **Download** from the kebab menu. The file is downloaded to your computer via your web browser and saved according to your browser’s download settings.

Depending on your browser configuration, the file may be saved automatically to your default download location, or you may be prompted to choose where to save it.

### Create folders

Navigate to the location where you want the new folder, and click **Create folder**.

![Create folder in MyKinsta file manager.](https://kinsta.com/wp-content/uploads/2026/06/create-folder-mykinsta.png)

Create folder in MyKinsta file manager.

Type a name, and click **Create folder**.

![Add folder name to create folder in file manager.](https://kinsta.com/wp-content/uploads/2026/06/add-folder-name.png)

Add folder name to create folder in file manager.

It’s important to note that two folders with the same name cannot exist in the same directory.

### Rename, move, and copy files and folders

All three operations use the kebab menu. For moving and copying, you browse to the destination folder after selecting the operation and then confirm. To rename, type the new name and confirm it in place.

![Rename, move, and copy files and folders.](https://kinsta.com/wp-content/uploads/2026/06/rename-move-copy-files-folders.png)

Rename, move, and copy files and folders.

One thing to be careful about: WordPress, plugins, and themes often reference files by their exact path. If you rename `wp-content/uploads/2024` to something else, anything pointing to that path stops working.

Before renaming or moving anything, check that nothing else depends on the original location. Taking a [backup](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/) before structural changes is a good habit.

### Delete files and folders

Select **Delete** from the kebab menu. If you are deleting a folder that contains files or subfolders, the confirmation dialog will tell you the folder is not empty and that everything inside will be permanently removed.

![Delete files and folders MyKinsta file manager.](https://kinsta.com/wp-content/uploads/2026/06/delete-files-folder-mykinsta.png)

Delete files and folders MyKinsta file manager.

Deletions are permanent. **There is no recycle bin or undo.** Back up before deleting anything you are not completely sure about.

### Bulk operations

Select multiple files and folders, click **Actions**, and choose **Move**, **Copy**, or **Delete**.

![Bulk operations to move, copy and delete files & folders.](https://kinsta.com/wp-content/uploads/2026/06/bulk-operation-file-manager.png)

Bulk operations to move, copy and delete files & folders.

This works across a mix of files and folders in the same directory, which makes cleanup tasks much faster than handling items one at a time.

### Symlinks

Symlinks appear alongside regular files and folders, with the link target visible in the file manager. You can rename, move, copy, and delete them from the kebab menu. All of these operations affect only the link itself. The original file or folder the symlink points to is not touched.

## Real-world scenarios where this saves time

The features above cover the mechanics. These are the situations where you should reach for the file manager.

### Fixing a broken site when wp-admin is inaccessible

A bad plugin update or a syntax error in a configuration file can take the WordPress dashboard down entirely. When that happens, you cannot log in through the normal route to fix it.

The file manager does not depend on WordPress being functional. Navigate to `wp-content/plugins/`, find the plugin that caused the problem, and rename its folder.

![Rename plugin folder in MyKinsta file manager.](https://kinsta.com/wp-content/uploads/2026/06/rename-plugin-folder.png)

Rename plugin folder in MyKinsta file manager.

WordPress treats a renamed plugin folder as a missing plugin and automatically deactivates it. The site comes back up, and you never needed a file transfer client.

### Editing wp-config.php

`wp-config.php` stores essential WordPress settings, including your database credentials, debugging options, security keys, and table prefix. Because it is a plain-text file, you can open and update it directly in the built-in editor.

![Edit wp-config.php file with MyKinsta file manager.](https://kinsta.com/wp-content/uploads/2026/06/edit-wp-config-php-file.png)

Edit wp-config.php file with MyKinsta file manager.

Make your change, click **Save**, and it is live immediately.

### Tweaking a theme file

If you need to add a function to `functions.php`, fix a template, or adjust some CSS, navigate to `wp-content/themes/your-theme/`, open the file, and edit it directly.

![Tweaking a theme file.](https://kinsta.com/wp-content/uploads/2026/06/tweak-theme-file.png)

Tweaking a theme file.

One caveat worth repeating: direct edits to a theme’s files will be overwritten the next time that theme updates. For anything beyond a temporary fix, a child theme is the right approach.

### Removing a file that should not be there

If a failed upload left a partial file, or a plugin dropped a log file that has grown to several gigabytes, or a backup script wrote to the wrong directory. In each of these cases, you can find the file and delete it in under a minute without opening a client.

### Checking and downloading your error logs

MyKinsta has a [dedicated **Logs** tab](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/) in the sidebar that lets you view your current `error.log` and `access.log` directly in the browser. For most debugging situations, that is the faster route.

The file manager gives you the full logs directory. Navigate to the `logs` folder and you will see every rotated log file going back several days, including `cache-purge.log` files and compressed `.gz` archives.

![Access logs in MyKinsta file manager.](https://kinsta.com/wp-content/uploads/2026/06/access-logs-file-manager.png)

Access logs in MyKinsta file manager.

If you are tracking down an issue that started three days ago, you can find the exact file for that date, open it in the viewer, or download it to share with a developer or the [Kinsta support team](https://kinsta.com/docs/support/contact-support/).

### Uploading a custom plugin or theme manually

If you have a private or custom-built plugin or theme that is not in the WordPress directory, you can upload the files directly to `wp-content/plugins/` or `wp-content/themes/`.

![Uploading a custom plugin or theme manually.](https://kinsta.com/wp-content/uploads/2026/06/upload-plugin-theme.png)

Uploading a custom plugin or theme manually.

For larger files in particular, this is more reliable than using the [WordPress dashboard uploader](https://kinsta.com/blog/wordpress-file-upload/).

## What the file manager does not replace

The file manager handles most everyday file tasks, but here are situations where SFTP is still the better choice.

- **Bulk operations at scale.** If you are transferring hundreds or thousands of files, a dedicated client handles that more reliably than a browser-based tool.
- **Automated and scripted workflows.** CI/CD pipelines, deployment scripts, and programmatic file sync all need SFTP with key-based authentication. The file manager is built for manual work, not automation.
- **Very large file uploads.** SFTP clients handle large transfers more robustly, with better recovery if a connection drops mid-transfer.

For everything else, the file manager gets the job done without leaving MyKinsta.

## Your hosting dashboard is now your file manager too

The MyKinsta file manager has eliminated so many trade-offs.

It is not a standalone tool you install or configure. It is part of the same dashboard that you use to manage backups, [staging environments](https://kinsta.com/docs/wordpress-hosting/staging-environment/), [DNS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/), and performance. That matters because file access is rarely something you plan for. It comes up during an incident, a quick client request, or a late-night fix.

Having it one click away inside a dashboard you are already in changes how you respond to those moments.

Head to **Sites > [site name] > Files** to get started. You can also reach out to the [support team](https://kinsta.com/docs/support/contact-support/) if you have questions.

Joel Olawanle
[Kinsta](https://kinsta.com/)

Joel is a Frontend developer working at Kinsta as a Technical Editor. He is a passionate teacher with love for open source and has written over 300 technical articles majorly around JavaScript and it's frameworks.

- [Website](https://joelolawanle.com/)
- [LinkedIn](https://www.linkedin.com/in/olawanlejoel/)
- [Twitter](https://twitter.com/olawanle_joel)
- [YouTube](https://www.youtube.com/@joelolawanle)
