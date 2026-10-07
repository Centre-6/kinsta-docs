---
url: "https://kinsta.com/docs/devkinsta/devkinsta-site-management/email-inbox/"
title: "Email Inbox"
tier: "docs"
product: "devkinsta"
product_label: "DevKinsta (local dev tool, not hosting)"
subsection: "devkinsta-site-management"
section: ["DevKinsta", "Site Management"]
kinsta_last_updated: "2024-07-18T08:36:00"
change_signal: "2024-07-18T08:36:00"
fetched_at: "2026-10-07T22:58:19Z"
sha256: "c6ed8b04552f7996589ec019878805f97c562bcda899ac38c833183f74a222c8"
body_chars: 1022
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Email Inbox

**Section:** DevKinsta > Site Management
**Product:** DevKinsta (local dev tool, not hosting)
**Source:** https://kinsta.com/docs/devkinsta/devkinsta-site-management/email-inbox/
**Kinsta last updated:** 2024-07-18T08:36:00

## On this page

- [View email](#view-email)
- [Manipulate email](#manipulate-email)
- [Email service logs](#email-service-logs)

---

With the Email inbox feature, you can have a separate inbox for every site. DevKinsta catches all outgoing emails from PHP `mail()`. Behind the scenes, DevKinsta uses [MailHog as an email client](https://kinsta.com/blog/mailhog/).

The Email inbox can be viewed for each site by clicking on the envelope icon on the left side of the **Site info** page.

![DevKinsta Email inbox.](https://kinsta.com/wp-content/uploads/2023/11/devkinsta-email-inbox.png)

DevKinsta Email inbox.

## View email

Click on one of your emails in the list, and it’ll show you the details. DevKinsta can display both HTML and plain text emails.

![Preview of an email in the DevKinsta email inbox. ](https://kinsta.com/wp-content/uploads/2023/11/devkinsta-email-1024x471.png)

Preview of an email in the DevKinsta email inbox.

## Manipulate email

You can do the following with the emails:

- Read
- Delete
- See raw content

## Email service logs

You can check MailHog logs with the following command:

```
docker logs -f devkinsta_mailhog
```
