---
url: "https://kinsta.com/changelog/file-manager/"
title: "Manage WordPress files in the MyKinsta dashboard"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Manage WordPress files in the MyKinsta dashboard"]
kinsta_last_updated: "2026-06-06T13:30:35+00:00"
sitemap_lastmod: "2026-06-06T13:30:35+00:00"
fetched_at: "2026-10-07T22:37:47Z"
sha256: "e729019d4491d3725ddc6c91547f37d486741ec08be3b6f4e2b27ea5cde740cf"
body_chars: 7717
extracted_with: "main article"
status: "live"
---

# Manage WordPress files in the MyKinsta dashboard

**Section:** Changelog > Manage WordPress files in the MyKinsta dashboard
**Product:** Changelog
**Source:** https://kinsta.com/changelog/file-manager/
**Kinsta last updated:** 2026-06-06T13:30:35+00:00

## On this page

- [How to manage files and folders in MyKinsta](#how-to-manage-files-and-folders-in-mykinsta)
  - [Working with folders](#working-with-folders)
  - [Working with files](#working-with-files)
  - [Working with symlinks](#working-with-symlinks)
- [Tell us what you think](#tell-us-what-you-think)

---

Updated
:   June 6, 2026

![An illustration representing the new file manager within the MyKinsta dashboard.](https://kinsta.com/wp-content/uploads/2026/06/mykinsta-new-file-manager-1024x536.png)

Based on our totally unscientific survey (we asked a few people), the file most often edited in a WordPress installation is `config.php`. Usually less than 4KB, this file contains the information a site needs to get online after a migration or changes (sometimes unexpected) to the database backend.

But editing `config.php` (even in an emergency) demands access to the server’s file system usually available only through tools like an FTP/SFTP client. That means you need to add server addresses, usernames, and passwords to another application that has access to your website.

Our new **Files** tool in the MyKinsta dashboard provides quick access to every file in a WordPress installation, including essential components like configuration files. Maybe more importantly, the work within the **Files** tool we call the file manager around here happens under the same security umbrella you have chosen for MyKinsta’s multi-factor authentication.

## How to manage files and folders in MyKinsta

The new file manager is just a couple of clicks away when you log in to MyKinsta. After selecting a WordPress site in the dashboard, you’ll find **Files** in the left-hand menu:

![A screenshot of the MyKinsta dashboard with the Files option highlighted.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files.png)

Accessing **Files** in the MyKinsta dashboard.

From here, you can now…

- Navigate the directories of a WordPress installation
- Upload, download, rename, move, copy, and delete files
- Create, rename, move, copy, and delete folders
- Rename, move, copy, and delete symbolic links (symlinks)
- View and edit text files (including PHP, JavaScript, and style sheet documents)

What’s more, some of these actions can be performed in bulk for multiple files and folders simultaneously.

Let’s take a closer look at some of these capabilities. But first, a warning:

### Working with folders

Navigate your website’s file system by clicking on folder names. A breadcrumb menu at the top of the file manager display allows you to jump to any location on the current path.

At any time, you can create a new folder at the current location by clicking the Create folder button near the top of the page:

![A screenshot showing the MyKinsta file manager interface with the Create folder button hilighted.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-create-folder.png)

Locating the **Create folder** button.

Other folder actions (renaming, moving, copying, or deleting) begin by clicking on the kebab (three-dot) menu to the right of a folder name:

![A screenshot showing the kebab menu with folder actions in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-folder-options.png)

The kebab menu initiates most folder actions.

When copying or moving a folder, you will be asked to navigate to the destination for the action:

![A screenshot showing the dialog for moving a file in the MyKinsta file manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-move-folder.png)

Moving a folder in MyKinsta’s file manager.

**Note:** When moving, copying, or deleting a folder, you will be moving, copying, or deleting all of that folder’s contents.

The file manager opens with a view of the `public` folder, which is the root directory of most WordPress sites at Kinsta. But you can navigate up another level for access to resources like site logs:

![Screenshot showing folder contents within the MyKinsta file manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-file-manager-server-root.png)

Display of folder contents within the MyKinsya file manager.

The `logs` folder in the display above is a symlink. The real path of a symlink is displayed beside the file or folder name (`/var/log/siteslogs` in this case).

### Working with files

Viewing the contents of a file is the default action for plain-text documents in the file manager. Simply click on the filename to view documents like PHP code, JavaScripts, CSS, and more:

![A screenshot showing a file view in MyKinsta's file manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-view-file.png)

Viewing a PHP file in MyKinsta’s file manager.

You can’t view binary files (like images, PDFs, audio and video files, and Word documents). If you attempt to view a binary file, you are asked if you would like to download the file instead:

![A screenshot showing the prompt to download a binary file in MyKinsta's file manaager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-file-manager-view-binary-file.png)

A download prompt for a binary ZIP file in the MyKinsta file manager.

**View** is just one of the actions available for files in the kebab menu to the right of a filename:

![A screen shot showing the actions available for files in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/05/wordpress-files-file-options-2.png)

The file options menu in the MyKinsta file manager.

You can begin editing a file by selecting **Edit** in the kebab menu or by clicking the **Edit** button when viewing a file:

![](https://kinsta.com/wp-content/uploads/2026/06/wordpress-file-manager-edit-button.png)

Locating the **Edit** button in the file manager’s file viewer.

After making edits, you can write the revised file to disk by clicking the **Save changes** button:

![A screenshot with the Save changes button highlighted in the MyKinsta file manager,](https://kinsta.com/wp-content/uploads/2026/05/wordpress-file-manager-edit-file.png)

The **Save changes** button commits edits to disk.

Files can also be downloaded from the server and uploaded:

![A screenshot with the Upload file button highlighted in the MyKinsta file manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-upload-file.png)

Locating the **Upload file** button in MyKinsta’s file manager.

This is a great way to download a file for editing in your preferred application before returning it to the server.

Like with folders, when moving or copying a file, the file manager will ask you to navigate to a target destination:

![A screenshot showing the dialog when copying a file in the MyKinsta file manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-copy-file.png)

The file manager dialog for copying a file.

You can move, copy, and delete multiple files and folders simultaneously. Select the target files and folders using the checkboxes to the left of their names and then choose the desired action from the **Actions** menu:

![A screenshot showing the options available in the kebab menu when executing bulk actions.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-bulk-actions.png)

An example of bulk actions in the MyKinsta file manager.

### Working with symlinks

You can use the file manager to rename, move, copy, and delete symlinks:

![A screenshot showing the kebab menu actions for symlinks in the MyKinsta file manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-symlink-options.png)

The actions available for symlinks in the MyKinsta file manager.

## Tell us what you think

June 2026 marked the first release of the file manager. You can learn more about the feature in our [extensive documentation](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-file-manager/), and we hope you’ll find it to be a time-saver right inside MyKinsta.

Do you have your own wish list for an in-dashboard file manager? [Let us know](https://kinsta.com/kinsta-support/)!
