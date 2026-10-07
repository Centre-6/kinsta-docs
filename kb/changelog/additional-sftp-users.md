---
url: "https://kinsta.com/changelog/additional-sftp-users/"
title: "Create accounts for additional SFTP users in MyKinsta"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Create accounts for additional SFTP users in MyKinsta"]
kinsta_last_updated: "2025-04-24T20:44:22+00:00"
sitemap_lastmod: "2025-04-24T20:44:22+00:00"
fetched_at: "2026-10-07T22:37:06Z"
sha256: "e597baa23129606e989fbca83e4c563bf68bc136465a4d609d384f2666c1a475"
body_chars: 4903
extracted_with: "main article"
status: "live"
---

# Create accounts for additional SFTP users in MyKinsta

**Section:** Changelog > Create accounts for additional SFTP users in MyKinsta
**Product:** Changelog
**Source:** https://kinsta.com/changelog/additional-sftp-users/
**Kinsta last updated:** 2025-04-24T20:44:22+00:00

## On this page

- [How to manage additional SFTP users](#how-to-manage-additional-sftp-users)
  - [Adding or removing additional SFTP users](#adding-or-removing-additional-sftp-users)
  - [What if Primary SFTP/SSH user access is disabled?](#what-if-primary-sftpssh-user-access-is-disabled)
- [WordPress management made easier and more flexible](#wordpress-management-made-easier-and-more-flexible)

---

Published
:   April 24, 2025

![An illustration representing the dialog in MyKinsta for adding additional SFTP users.](https://kinsta.com/wp-content/uploads/2025/04/changelog-additional-sftp-users-1024x512.png)

You can now create multiple SFTP user accounts for each WordPress website you manage in your [MyKinsta dashboard](https://kinsta.com/mykinsta/). This means Kinsta customers can assign SFTP logins to members of their team without having to share the credentials of the Primary SFTP/SSH user that is initially enabled for each WordPress environment.

[SFTP](https://kinsta.com/blog/how-to-use-sftp/) is used by WordPress administrators to gain direct access to the files within a site installation and to perform tasks ranging from theme and plugin management to emergency error fixes.

The new functionality supports teams that want to keep a handle on security while helping team members with varying responsibilities be effective in their roles.

## How to manage additional SFTP users

You can add SFTP users by navigating in MyKinsta to **WordPress sites** > ***sitename/environment*** > **Info** > **Additional SFTP users**:

![Adding additional STP users within the MyKinsta dashboard.](https://kinsta.com/wp-content/uploads/2025/04/additional-sftp-users.png)

This WordPress environment currently has no additional SFTP user accounts.

**Note:** It’s important to remember that these SFTP logins are unique to each WordPress environment. So, you might provide developers on your team with SFTP access to a [staging site](https://kinsta.com/blog/wordpress-staging-site/), but not a live site.

After clicking the **Add new user** button, you are prompted to provide the details for the new SFTP account:

![The prompts for access credentials in MyKinsta when adding additional SFTP users.](https://kinsta.com/wp-content/uploads/2025/04/additional-sftp-user-details.png)

Providing the access details for an additional SFTP user.

Here’s what you will define in the dialog shown above:

- **Username:** Usernames can include letters, numbers, dashes (hyphens), and underscores, but not spaces or other special characters.
- **Password:** MyKinsta will generate a complex password automatically, but you can provide your own or have MyKinsta regenerate its suggestion.
- **Root directory:** By default, the `public` folder is the root directory for additional SFTP user accounts, but you can restrict that further by specifying a path to some other location below that.
- **Read/write permissions:** New SFTP accounts will have read/write access on the server by default, but you can choose to allow read-only access — suitable, for example, when the user’s only role is to download site backups.

In the example below, the login with the username **dev** is being assigned a root directory under `wp-content` where the user will have access only to files within the `themes` folder and below:

![Specifying an alternate root directory when adding an SFTP user within the MyKinsta dashboard.](https://kinsta.com/wp-content/uploads/2025/04/additional-sftp-user-subdirectory.png)

Specifying an alternate root directory for an SFTP login.

When defining an alternate root directory for an SFTP user account, the path/folder must already exist on the server.

### Adding or removing additional SFTP users

After creating additional SFTP users, you can delete or modify those accounts back on the **Info** page and the **Additional SFTP users** card:

![A screenshot that includes the drop-down menu for editing or removing an SFTP user in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/04/additional-sftp-user-edit-remove.png)

Editing or removing an SFTP account.

Click the kebab (three-dot) menu beside any SFTP user entry and select **Edit** or **Remove** from the drop-down menu to begin making those changes.

### What if Primary SFTP/SSH user access is disabled?

Login access for additional SFTP users is independent of permissions for the **Primary SFTP/SSH user**. You can disable access entirely for that default account while permitting logins for additional SFTP user accounts (maybe with decreased permissions):

![A screenshot showing that the default SFTP/SSH account for a WordPress environment is disabled, while additional SFTP account access is enabled.](https://kinsta.com/wp-content/uploads/2025/04/additional-sftp-user-primary-disabled.png)

Additional SFTP users are allowed here while the default SFTP/SSH account is disabled.

## WordPress management made easier and more flexible

Making [WordPress management](https://kinsta.com/blog/wordpress-maintenance/) easier is what we do. If you are not already a customer and are looking for [fast](https://kinsta.com/blog/migrate-to-kinsta/) and [secure](https://kinsta.com/wordpress-hosting/security/) WordPress hosting, check out [Kinsta’s plans](https://kinsta.com/pricing/) to find the one that fits you best.
