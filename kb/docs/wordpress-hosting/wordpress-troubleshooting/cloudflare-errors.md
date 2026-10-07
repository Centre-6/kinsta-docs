---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/cloudflare-errors/"
title: "Cloudflare Errors"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-troubleshooting"
section: ["WordPress Hosting", "Troubleshooting"]
kinsta_last_updated: "2024-07-17T11:27:23"
change_signal: "2024-07-17T11:27:23"
fetched_at: "2026-10-07T22:58:19Z"
sha256: "2f9311a3d8cf17dcb4421ae2160fd769860dde1e6602c6a099d25ecea5a7da8f"
body_chars: 4099
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Cloudflare Errors

**Section:** WordPress Hosting > Troubleshooting
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/cloudflare-errors/
**Kinsta last updated:** 2024-07-17T11:27:23

## On this page

- [Errors 520 and 521](#errors-520-and-521)
  - [What’s causing the error?](#whats-causing-the-error)
  - [Site visitor](#site-visitor)
  - [Site owner or administrator non-Cloudflare domain](#site-owner-or-administrator-non-cloudflare-domain)
  - [Site owner or administrator Cloudflare domain](#site-owner-or-administrator-cloudflare-domain)
- [Error 1020: Access Denied](#error-1020-access-denied)
  - [What’s causing the ‘Error 1020: Access Denied’](#whats-causing-the-error-1020-access-denied)
  - [Site visitor](#site-visitor)
  - [Site owner or administrator non-Cloudflare domain](#site-owner-or-administrator-non-cloudflare-domain)
  - [Site owner or administrator Cloudflare domain](#site-owner-or-administrator-cloudflare-domain)

---

## Errors 520 and 521

Error 520 and Error 521 are Cloudflare-specific errors that indicate an issue between Cloudflare and the website’s server. There are a number of possible causes, so there are troubleshooting steps that need to be followed to track down the source.

### What’s causing the error?

Error 520 indicates Cloudflare received an empty, unknown, or unexpected response from the server. Error 521 indicates that the server refused a connection with Cloudflare.

If you see either of these errors on a site hosted at Kinsta, check out the information below to see the next steps to resolve this issue.

### Site visitor

If you see one of these errors while visiting a site, but you aren’t the site owner or administrator, we recommend contacting the site owner so they can resolve the issue.

Be sure to include a screenshot of the error or at least the Cloudflare Ray ID that is shown below the error.

### Site owner or administrator non-Cloudflare domain

If you’re the site owner or administrator and do not have your own Cloudflare account, [open a new chat with our Support team](https://kinsta.com/docs/support/contact-support/). The following information isn’t required but can be helpful as we look into the issue:

1. The date and time the error occurred.
2. The Cloudflare Ray ID shown under the error message.
3. Any steps you or your visitor were taking when the error occurred (e.g. clicking on a link, updating content, adding something to a cart, submitting a form, or other action).

### Site owner or administrator Cloudflare domain

If you’re the site owner or administrator and have your own Cloudflare account, check out our detailed guides for resolving each of these errors:

- [How to Fix Cloudflare’s Error 520](https://kinsta.com/blog/error-520/)
- [How to Fix Cloudflare’s Error 521](https://kinsta.com/blog/error-521/)

## Error 1020: Access Denied

Error 1020: Access Denied might not be a common issue you’ll see, but it could be the case you or your client’s site might experience it. In this article, we’ll dig deeper into what’s causing the error and what to do when you see it.

### What’s causing the ‘Error 1020: Access Denied’

Error 1020 Access Denied is caused when a firewall rule has been violated on a site protected by Cloudflare. It can be triggered if a site visitor tries to directly access an endpoint that is protected.

If you see this on a site hosted at Kinsta, check out the information below to see the next steps to resolve this issue.

### Site visitor

If you see the Error 1020 Access Denied while visiting a site, but you aren’t the site owner or administrator, we recommend contacting the site owner so they can resolve the issue.

Be sure to include a screenshot of the error or at least the **Cloudflare Ray ID** that is shown below the error.

![Cloudflare Error 1020 Acess denied.](https://kinsta.com/wp-content/uploads/2021/10/cloudflare-error-1020.jpg "Cloudflare Error 1020 Acess denied")

Cloudflare Error 1020 Acess denied.

### Site owner or administrator non-Cloudflare domain

If you’re the site owner or administrator and do not have your own Cloudflare account with firewall rules implemented, contact our [Support team](https://kinsta.com/docs/support/contact-support/) and provide the following information so we can investigate and resolve this issue:

1. The date and time the error occurred.
2. The **Cloudflare Ray ID** shown under the error message.
3. Any steps you or your visitor were taking when the error occurred (e.g. clicking on a link, updating content, adding something to a cart, submitting a form, or other action).

### Site owner or administrator Cloudflare domain

If you’re the site owner or administrator and have your own Cloudflare account with firewall rules implemented, you’ll need to check the Firewall Events Log (**Firewall** > **Events**) to see which rule is being violated and causing the request to be blocked.

If you don’t see any blocked events in your Firewall Events Log, contact our Support team with the information listed above (in the non-Cloudflare domain section).
