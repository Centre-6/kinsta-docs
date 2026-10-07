---
url: "https://kinsta.com/changelog/selective-push-environment/"
title: "Get selective when pushing staged environments"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Get selective when pushing staged environments"]
kinsta_last_updated: "2024-05-11T03:36:58+00:00"
sitemap_lastmod: "2024-05-11T03:36:58+00:00"
fetched_at: "2026-10-07T22:35:30Z"
sha256: "7f98f2430966d753d2a1747c7da183195c120af930b2ad8a25d224fd78d04ba3"
body_chars: 4484
extracted_with: "main article"
status: "live"
---

# Get selective when pushing staged environments

**Section:** Changelog > Get selective when pushing staged environments
**Product:** Changelog
**Source:** https://kinsta.com/changelog/selective-push-environment/
**Kinsta last updated:** 2024-05-11T03:36:58+00:00

---

Updated
:   May 11, 2024

![Illustration representing the WordPress staged-site deployment feature in MyKinsta and the words, 'Selective push environment.'](https://kinsta.com/wp-content/uploads/2024/05/changelog-selective-push-environment-1024x536.png)

An upgraded **Push environment** tool in the MyKinsta dashboard is giving [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/) customers dramatically more power when publishing from [staged environments](https://kinsta.com/docs/wordpress-hosting/staging-environment/).

New [selective push](https://kinsta.com/docs/wordpress-hosting/staging-environment/#push-staging-to-live-with-selective-push) functionality means customers can now deploy anything from entire sites to individual files or database tables from staging, allowing MyKinsta to support more development workflows.

## How to use Selective Push in MyKinsta

Whether you have a free or [premium add-on](https://kinsta.com/add-ons/) staging environment, the **Push environment** option is available any time a staged site is chosen from the WordPress sites list or from MyKinsta’s **Jump to or search** dialog, invoked by pressing `CTRL + /` (and also `CMD + /` on macOS):

![Screenshot showing WordPress environments at the top of the Jump to/Search dialog in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-selective-push-environment-search.png)

Choosing a live or staged environment in MyKinsta’s Jump to/Search dialog.

The website pictured above has a **Live** environment and two staged environments — named **Staging** and **Development**.

In the image below, the staged environment named **Development** has been selected, and the **Push environment** button located above the site details shows that we have the option, in this case, to push to **Live** or the other staged environment:

![Screenshot showing the selector for choosing a push target in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-selective-push-choose-target.png)

Selecting a target for the **Push environment** action.

After selecting a target environment, you can choose which file and database assets you want to push.

Files:

- All files and folders
- Specific files and folders
- (No files or folders)

Databases:

- All database tables
- Specific database tables
- (No database tables)

![Screenshot showing the selection of assets to be pushed from a staged environment.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-selective-push-choose-assets.png)

Selecting file and database assets to push from staged.

Above, we’ve chosen to push to **Live** only the folder containing our **acme** theme and the option to push any database content has been deselected.

To enable the push, the site name is entered in the confirmation field.

Below, a selective push of the database will send only the **wp_postmeta** and **wp_posts** tables to the target environment:

![Screenshot showing the selection of database tables to be pushed from a staged environment.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-selective-push-choose-database-tables.png)

Selecting individual database tables to push from staged.

When pushing database tables, you can enable an automatic search-and-replace that will swap any references to the staged environment’s domain with that of the target environment.

Finally, below, a selective push of files and folders will deploy just a single CSS style sheet and the folder named **assets** from within our **acme** theme folder:

![Screenshot showing the specification of a single file and a single folder to push from a staged environment.](https://kinsta.com/wp-content/uploads/2024/05/mykinsta-selective-push-choose-files-folders.png)

Specifying individual files or folders to push from staged.

Whatever selections you make when pushing from one environment to another, we’ll make an automatic backup of the target environment before beginning the action.

## WordPress made easy (and fast)

As an industry-leading managed WordPress host, Kinsta is dedicated to engineering new ways to make WordPress migration and [maintenance processes](https://kinsta.com/blog/wordpress-maintenance/) simpler than ever before.

If you’re looking for a [blazing fast](https://kinsta.com/blog/migrate-to-kinsta/) and [secure](https://kinsta.com/wordpress-hosting/security/) hosting provider, make sure to check out [Kinsta’s plans](https://kinsta.com/pricing/) to find the one that fits you best.
