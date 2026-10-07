---
url: "https://kinsta.com/changelog/push-to-other-sites/"
title: "Cross-site deployments of WordPress environments are now possible"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2025-11-03T11:56:11"
change_signal: "2025-11-03T11:56:11"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "a4cd89bcdbea407d12f6c75f7f2ea70787cc936851477ddf36b183d391d44bdf"
body_chars: 3309
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Cross-site deployments of WordPress environments are now possible

**Product:** Changelog
**Source:** https://kinsta.com/changelog/push-to-other-sites/
**Kinsta last updated:** 2025-11-03T11:56:11

---

Another enhancement to the **Push Environment** functionality of the [MyKinsta dashboard](https://kinsta.com/mykinsta/) has made it possible to deploy environments across distinct WordPress sites.

Previously, live and staging environments (or just selected assets within those environments) could be copied from one instance to another under the umbrella of a single site. Now, the target for **Push Environment** can be associated with a completely different site.

The new capability is a great solution for developers who want to deploy a “template” WordPress installation to multiple sites.

It also enables what is now the simplest way to move an existing site to a [different data center](https://kinsta.com/docs/service-information/data-center-locations/). The only caveat is that the source and target environments for the push are available under the same company account.

## Pushing an environment to another site

The steps to deploy environments across sites begin like any push, by navigating to **WordPress Sites** in MyKinsta and then clicking on the environment you want to use as the source:

![Screenshot showing the selection of a site's environment on the MyKinsta WordPress Sites page.](https://kinsta.com/wp-content/uploads/2025/10/push-environment-to-other-sites-select.png)

Choosing the source environment for a push.

Clicking on the source environment will display that environment’s details in the **Site Information** page. To push the environment to another site:

1. Click the **Push environment** button near the top of the page.
2. Select a target environment under the dropdown’s **Push to other sites** label.

![Screenshot showing the selection of an environment as a target for a push.](https://kinsta.com/wp-content/uploads/2025/10/push-environment-to-other-sites-target.png)

Choosing an environment on another site for deployment.

Above, the first entry in the dropdown (**Push to Live**) is an environment under the same site, ACME Dynamite Co. Under the **Push to other sites** label are environments on a second site, ACME Anvil Co.

After choosing the target environment, the **Push to other sites** confirmation dialog will appear:

![A screenshot of the Push to other sites confirmation dialog.](https://kinsta.com/wp-content/uploads/2025/10/push-environment-to-other-sites-confirmation.png)

The **Push to other sites** confirmation dialog.

In addition to confirming the source and target environments for the push, you can configure a [selective push](https://kinsta.com/docs/wordpress-hosting/wordpress-push-environments/#3-select-which-files-and-database-tables-to-push) of just certain files and database tables.

You can also optionally request a **Search & Replace** operation to automatically convert references to the domain on the source environment to those of the target environment on the other site.

## WordPress development made simpler

We’re dedicated to delivering tools that simplify [WordPress maintenance](https://kinsta.com/blog/wordpress-maintenance/). If you’re not already a customer but are looking for [fast](https://kinsta.com/blog/migrate-to-kinsta/) and [secure](https://kinsta.com/wordpress-hosting/security/) WordPress hosting, consider [Kinsta’s plans](https://kinsta.com/pricing/) to find the one that best suits your needs.
