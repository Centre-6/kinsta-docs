---
url: "https://kinsta.com/docs/devkinsta/devkinsta-site-management/subdomain-multisite/"
title: "Multisite Subdomain"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-site-management"
section: ["DevKinsta", "Site Management"]
kinsta_last_updated: "2024-08-19T12:08:44"
change_signal: "2024-08-19T12:08:44"
fetched_at: "2026-10-07T22:58:19Z"
sha256: "091b18fed03730739e9c5acc2fbd900913d3310c7ed468c899d56cf950da9732"
body_chars: 2566
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Multisite Subdomain

**Section:** DevKinsta > Site Management
**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-site-management/subdomain-multisite/
**Kinsta last updated:** 2024-08-19T12:08:44

---

To run a [multisite](https://kinsta.com/blog/wordpress-multisite/) in DevKinsta that uses [subdomains](https://kinsta.com/blog/wordpress-subdomain/) for the subsites (subsite.example.local), a few adjustments will need to be made. These steps are **not** necessary if your multisite network uses subdirectories/subfolders (example.local/subsite).

This is also part of a workaround if you have a subdomain type of multisite with [domain mapping](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/). You will first need to [deactivate your domain mapping plugin](https://kinsta.com/blog/disable-wordpress-plugins/) (if applicable) or change the mapped domains to subdomains (if your mapping is done with the domain mapping built into WordPress multisite). Then you can continue with the steps below.

**Important notes:**

- This tutorial requires you to edit your hosts file, which is generally considered an intermediate to advanced topic. We have a guide here with instructions for Windows and Mac: [How to Edit Your Hosts File – Preview Site Before Updating DNS 2](https://kinsta.com/blog/edit-hosts-file/). If you’re not comfortable making these changes or have any trouble after making changes to your hosts file, we recommend [working with a developer](https://kinsta.com/blog/hire-wordpress-developer/) or IT professional to set this up.
- Each time you add a new subsite, you’ll need to repeat the steps outlined here.
- These steps will need to be done whether you start a new subdomain multisite or import an existing site from Kinsta.

## Edit your hosts file

Note: If you haven’t already, add your new subsite(s) in your WordPress dashboard, then edit your hosts file as described below.

1. Find the lines in your hosts file that coincide with your multisite. Example:  
   `127.0.0.1 example.local`  
   `127.0.0.1 www.example.local`  
   `::1 example.local`  
   `::1 www.example.local`
2. Add each subdomain beneath the multisite lines like:  
   `127.0.0.1 example.local`  
   `127.0.0.1 www.example.local`  
   `127.0.0.1 subdomain.example.local`  
   `::1 example.local`  
   `::1 www.example.local`  
   `::1 subdomain.example.local`
3. After adding your subdomain(s), save your changes to your hosts file.

You should now be able to visit your subsite on your local site.

![Viewing a DevKinsta subdomain multisite in the browser.](https://kinsta.com/wp-content/uploads/2022/06/devkinsta-subdomain-multisite-browser.png "Viewing a DevKinsta subdomain multisite in the browser")

Viewing a DevKinsta subdomain multisite in the browser.
