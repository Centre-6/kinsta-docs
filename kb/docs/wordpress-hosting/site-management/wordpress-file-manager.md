---
url: "https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-file-manager/"
title: "File Manager"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "site-management"
section: ["WordPress Hosting", "Site Management"]
kinsta_last_updated: "2026-06-19T15:21:57"
change_signal: "2026-06-19T15:21:57"
fetched_at: "2026-10-07T22:58:16Z"
sha256: "fe9dc67157ac6102dbaa63a4c50deca3608d2aa7a78e7d98a3567b5bd4e65db3"
body_chars: 16163
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# File Manager

**Section:** WordPress Hosting > Site Management
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-file-manager/
**Kinsta last updated:** 2026-06-19T15:21:57

## On this page

- [File Manager limitations](#file-manager-limitations)
- [Folder options](#folder-options)
  - [Rename a folder](#rename-a-folder)
  - [Move a folder](#move-a-folder)
  - [Copy a folder](#copy-a-folder)
  - [Duplicate a folder](#duplicate-a-folder)
  - [Delete a folder](#delete-a-folder)
  - [Create a new folder](#create-a-new-folder)
  - [Sharing links to folders](#sharing-links-to-folders)
- [File options](#file-options)
  - [View a file](#view-a-file)
  - [Edit a file](#edit-a-file)
  - [Download a file](#download-a-file)
    - [Download log files](#download-log-files)
  - [Rename a file](#rename-a-file)
  - [Move a file](#move-a-file)
  - [Copy a file](#copy-a-file)
  - [Duplicate a file](#duplicate-a-file)
  - [Delete a file](#delete-a-file)
  - [Upload a file](#upload-a-file)
- [Symlinks](#symlinks)
  - [Rename a symlink](#rename-a-symlink)
  - [Move a symlink](#move-a-symlink)
  - [Copy a symlink](#copy-a-symlink)
  - [Delete a symlink](#delete-a-symlink)
- [Bulk options](#bulk-options)

---

The MyKinsta File Manager gives you quick, direct access to your WordPress site’s files and folders. You can browse, view, edit, rename, download, upload, move, copy, and delete files, as well as create, rename, move, copy, and delete folders, all within the MyKinsta dashboard without needing to connect via SFTP, saving you time and effort.

To access the File Manager in MyKinsta, click **Sites**, select the ***sitename***, and click **Files**. The default directory that opens is the Public directory. If the public directory does not exist or has been renamed, it opens at the root directory.

![File Manager in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-1.png)

File Manager in MyKinsta.

## File Manager limitations

The following limitations apply to MyKinsta’s File Manager:

- **Upload size:** Files larger than 100 MB cannot be uploaded.
- **Upload time:** Uploads that take longer than 20 minutes will fail, this usually only happens due to a slow connection.
- **Viewing and editing:** You can only view and edit files that contain readable text, such as code, configuration, and markup files (for example, PHP, HTML, CSS, JavaScript, JSON, XML, YAML, and SQL). Files larger than 10 MB cannot be opened in the built-in viewer or editor.
- **Non-readable text files:**  You cannot view document, media, or binary file formats. This includes files such as PDFs, Word documents, spreadsheets, images, videos, audio files, fonts, archives, or executables. To view these files, you must download them.
- **Download size:** There is no explicit file-size cap, but very large downloads may fail if the transfer is too slow or times out.
- **Action links:** If an upload, download, or edit takes too long to start, you may need to retry it.

## Folder options

Click on a folder to view its contents. To rename, move, copy, duplicate, or delete a folder, use the kebab (three dots) and select the required option.

![Rename, move, copy, duplicate, or delete a WordPress folder in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-file-manager-folder-options.png)

Rename, move, copy, duplicate, or delete a WordPress folder in MyKinsta’s File Manager.

### Rename a folder

To rename a folder, use the kebab (three dots) and select **Rename**. Enter the new name for the folder, and click **Rename folder**.

![Rename a folder in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/05/wordpress-files-rename-folder.png)

Rename a folder in MyKinsta’s File Manager.

### Move a folder

To move a folder, use the kebab (three dots) and select **Move**. Browse to the destination where you want to move the folder, click a folder to open it, or use the breadcrumbs to navigate back to a parent folder. Then click **Move folder** to move the folder into the selected location.

![Move a folder in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-move-folder.png)

Move a folder in MyKinsta’s File Manager.

### Copy a folder

To copy a folder, use the kebab (three dots) and select **Copy**. Browse to the destination where you want to copy the folder to, click a folder to open it, or use the breadcrumbs to navigate back to a parent folder. Then click **Copy folder** to copy the folder into the selected location.

![Copy a folder in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-copy-folder.png)

Copy a folder in MyKinsta’s File Manager.

### Duplicate a folder

To duplicate a folder and its contents, use the kebab (three dots) and select **Duplicate**. By default, the duplicate uses the original folder name with **copy** added. To use a different name, enter it in **New folder name**, then click **Duplicate folder**.

![Duplicate a folder in MyKinsta's file manager. ](https://kinsta.com/wp-content/uploads/2026/06/wordpress-duplicate-folder.png)

Duplicate a folder in MyKinsta’s file manager.

### Delete a folder

To delete a folder, use the kebab (three dots) and select **Delete**.

If the folder contains files or subfolders, the confirmation window will indicate that the folder is not empty, and deleting it will also permanently delete all of its contents.

To confirm the deletion, click **Delete folder**.

![Delete a folder in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/05/wordpress-files-delete-folder.png)

Delete a folder in MyKinsta’s File Manager.

### Create a new folder

To create a new folder, browse to the destination where you want to create the folder, click a folder to open it, or use the breadcrumbs to navigate back to a parent folder and click **Create folder**.

![Create a new folder in WordPress with MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-create-folder.png)

Create a new folder in WordPress with MyKinsta’s File Manager.

Enter a name for the folder, and click **Create folder**.

![Add a folder name and click Create folder. ](https://kinsta.com/wp-content/uploads/2026/02/wordpress-files-create-folder-2.png)

Add a folder name and click Create folder.

### Sharing links to folders

To share a link to a specific folder, copy the URL and send it to the person you want to share it with. You can only share folder links with users who already have access to the environment. Folder links stay active for 30 days; after that, clicking an expired link opens the default folder instead of the specific one.

## File options

To view, edit, download, rename, move, copy, duplicate, or delete a file, click the kebab (three dots) and select the required option.

![View, edit, download, rename, move, copy, duplicate, or delete a WordPress file in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-file-manager-file-options.png)

View, edit, download, rename, move, copy, duplicate, or delete a WordPress file in MyKinsta’s File Manager.

### View a file

To view a file, use the kebab (three dots) and select **View**. You can use File Manager to view files that contain readable text, such as code, configuration, and markup files (for example, PHP, HTML, CSS, JavaScript, JSON, XML, YAML, and SQL).

You cannot view document, media, or binary file formats. This includes files such as PDFs, Word documents, spreadsheets, images, videos, audio files, fonts, archives, or executables. To view these files, you must download them.

You cannot view files larger than 10 MB within File Manager. To view these files, you must download them.

You can also [edit the file](#edit-a-file) from the view window. To go back to File Manager, click the cross to close the file.

![View a file in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-view-file.png)

View a file in MyKinsta’s File Manager.

### Edit a file

To edit a file, use the kebab (three dots) and select **Edit**. You can use File Manager to edit files that contain readable text, such as code, configuration, and markup files (for example, PHP, HTML, CSS, JavaScript, JSON, XML, YAML, and SQL).

You cannot edit document, media, or binary file formats. This includes files such as PDFs, Word documents, spreadsheets, images, videos, audio files, fonts, archives, or executables. To edit these files, you must download them, make the changes, and upload them again.

You cannot edit files larger than 10 MB within File Manager. To edit these files, you must download them.

When you make the required changes to your file, click **Save changes**. To go back to File Manager, click the cross to close the file.

![Edit a file in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/05/wordpress-file-manager-edit-file.png)

Edit a file in MyKinsta’s File Manager.

### Download a file

To download a file, use the kebab (three dots) and select **Download**. The file is downloaded to your default download location, which varies by operating system, as follows:

- **Windows:** C:\Users\<username>\Downloads
- **macOS:** /Users/<username>/Downloads
- **Linux:** /home/<username>/Downloads

There is no limit to the download size; however, large downloads may fail if the transfer is too slow or times out.

#### Download log files

Kinsta’s File Manager provides a quick and easy way to download log files from your site.

1. In MyKinsta, go to **Sites** > ***sitename*** > **Files**.
2. To access the site’s root directory, click the root directory path in the breadcrumbs.

   ![Click the root directory path to access the logs.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-file-manager-root.png)

   Click the root directory path to access the logs.
3. Open the **logs** folder.

   ![Open the logs folder. ](https://kinsta.com/wp-content/uploads/2026/06/wordpress-file-manager-logs.png)

   Open the logs folder.
4. Locate the log file you want to download, click the kebab (three-dots), and then click **Download**.

   ![Download the log file. ](https://kinsta.com/wp-content/uploads/2026/06/wordpress-file-manager-download-logs.png)

   Download the log file.

The log file is downloaded to your computer and can be opened with any text editor for further analysis.

### Rename a file

To rename a file, use the kebab (three dots) and select **Rename**. Enter the new name for the file, and click **Rename file**.

![Rename a file in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/05/wordpress-files-rename-file.png)

Rename a file in MyKinsta’s File Manager.

### Move a file

To move a file, use the kebab (three dots) and select **Move**. Browse to the destination where you want to move the file, click a folder to open it, or use the breadcrumbs to navigate back to a parent folder. Then click **Move file** to move the file into the selected location.

![Move a file in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-move-file.png)

Move a file in MyKinsta’s File Manager.

### Copy a file

To copy a file, use the kebab (three dots) and select **Copy**. Browse to the destination where you want to copy the file to, click a folder to open it, or use the breadcrumbs to navigate back to a parent folder. Then click **Copy file** to copy it into the selected location.

![Copy a file in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-copy-file.png)

Copy a file in MyKinsta’s File Manager.

### Duplicate a file

To duplicate a file, use the kebab (three dots) and select **Duplicate**. By default, the duplicate uses the original file name with **copy** added. To use a different name, enter it in **New file name**, then click **Duplicate file**.

![Duplicate a file in MyKinsta's file manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-duplicate-file.png)

Duplicate a file in MyKinsta’s file manager.

### Delete a file

To delete a file, use the kebab (three dots) and select **Delete**. To confirm the deletion, click **Delete file**.

![Delete a file in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/05/wordpress-files-delete-file.png)

Delete a file in MyKinsta’s File Manager.

### Upload a file

To upload a file, browse to the directory you want to upload it to, then click **Upload file**. Files larger than 100 MB cannot be uploaded within File Manager.

You cannot upload a file with the same name as an existing file in the folder. If a file with that name already exists, you’ll be asked if you want to overwrite the existing file or skip it.

![Upload a file to your WordPress site in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-upload-file.png)

Upload a file to your WordPress site in MyKinsta.

Browse to the file on your computer and click **Open**.

If you need to cancel the file upload, click **Cancel upload**.

![Cancel a file upload. ](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-cancel-upload.png)

Cancel a file upload.

If the file upload fails, click **See details** to see which files failed to upload and the reason why.

![Failed upload details.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-failed.png)

Failed upload details.

## Symlinks

A symlink is a shortcut or a link that points to another file or folder within your WordPress directory. It lets you access a file or directory from one location while the actual file lives somewhere else.

Symlinks are commonly used for:

- **Shared files or assets:** Multiple WordPress sites may use the same uploads folder, plugin, or media library through a symlink instead of storing duplicate copies.
- **External or mounted storage:** A symlink can point the `uploads` directory to external storage, such as a mounted network drive or cloud storage volume.
- **Development workflows:** Developers often symlink plugins or themes from a local development repository into the WordPress `wp-content` directory, so changes update immediately without copying files.
- **Keeping large files outside the main WordPress directory:** Large media libraries, backups, or generated files can be stored outside the main WordPress installation while still appearing accessible from within WordPress through a symlink.

If a folder or file uses a symlink, the link to that file or folder is shown in MyKinsta’s File Manager.

![Symlink in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-symlink.png)

Symlink in MyKinsta’s File Manager.

To rename, move, copy, or delete a symlink, click the kebab (three dots) and select the required option.

![Rename, move, copy, or delete a symlink in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-symlink-options.png)

Rename, move, copy, or delete a symlink in MyKinsta’s File Manager.

### Rename a symlink

To rename a symlink, use the kebab (three dots) and select **Rename**. Enter the new name for the symlink, and click **Rename symlink**. Renaming a symlink only changes the name of the link itself; it does not rename or modify the original file or folder it points to.

![Rename a symlink in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/05/wordpress-files-rename-symlink.png)

Rename a symlink in MyKinsta’s File Manager.

### Move a symlink

To move a symlink, use the kebab (three dots) and select **Move**. Browse to the destination where you want to move the symlink, click a folder to open it, or use the breadcrumbs to navigate back to a parent folder. Then click **Move symlink** to move the symlink to the selected location. This only moves the link; it does not move the original file or folder it points to.

![Move a symlink in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-move-symlink.png)

Move a symlink in MyKinsta’s File Manager.

### Copy a symlink

To copy a symlink, use the kebab (three dots) and select **Copy**. Browse to the destination where you want to copy the symlink to, click a folder to open it, or use the breadcrumbs to navigate back to a parent folder. Then click **Copy symlink** to copy the symlink to the selected location.

![Copy a symlink in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-files-copy-symlink.png)

Copy a symlink in MyKinsta’s File Manager.

### Delete a symlink

To delete a symlink, use the kebab (three dots) and select **Delete**. To confirm the deletion, click **Delete symlink**.

![Delete a symlink in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/05/wordpress-files-delete-symlink.png)

Delete a symlink in MyKinsta’s File Manager.

## Bulk options

You can move, copy, duplicate, and delete multiple files and folders simultaneously. Select the required files and folders, click **Actions**, and select **Move**, **Copy**, **Duplicate**, or **Delete**.

![Move, copy, duplicate, or delete multiple files and folders in MyKinsta's File Manager.](https://kinsta.com/wp-content/uploads/2026/06/wordpress-file-manager-bulk-actions.png)

Move, copy, duplicate, or delete multiple files and folders in MyKinsta’s File Manager.
