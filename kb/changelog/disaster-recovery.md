---
url: "https://kinsta.com/changelog/disaster-recovery/"
title: "Go beyond backups with Kinsta Disaster Recovery"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Go beyond backups with Kinsta Disaster Recovery"]
kinsta_last_updated: "2026-08-19T14:49:55+00:00"
sitemap_lastmod: "2026-08-19T19:23:39+00:00"
fetched_at: "2026-10-07T22:36:30Z"
sha256: "b0dfeab0b45fd9c9511f9181b977cfb5032c19dc2537298ab3dc7b06b0277d68"
body_chars: 4932
extracted_with: "main article"
status: "live"
---

# Go beyond backups with Kinsta Disaster Recovery

**Section:** Changelog > Go beyond backups with Kinsta Disaster Recovery
**Product:** Changelog
**Source:** https://kinsta.com/changelog/disaster-recovery/
**Kinsta last updated:** 2026-08-19T14:49:55+00:00

---

Published
:   August 19, 2026

![An illustration representing replication of a website across data centers with the words 'Disaster recovery.'](https://kinsta.com/wp-content/uploads/2026/08/kinstas-disaster-recovery-changelog-1024x536.png)

In 2021, fire at a data center building in Strasbourg, France, destroyed thousands of servers and knocked more than 3.5 million websites offline. [Reuters reported](https://www.reuters.com/article/world/millions-of-websites-offline-after-fire-at-french-cloud-services-firm-idUSKBN2B20NT/) at the time that affected customers of the data center’s operator, OVHcloud, included the French government, banks, news organizations, and about two percent of all websites using the .fr country code top-level domain.

Last fall, a fire at South Korea’s National Information Resources Service data center forced more than 600 government systems offline, with some taking weeks to relaunch.

[Cloudflare Radar](https://radar.cloudflare.com/) tracks Internet traffic outages and anomalies daily. Fortunately, the numbers show meltdowns at public data centers are extremely rare, but incidents like the OVHcloud fire prove they can happen. That’s why enterprises looking to ensure business continuity demand that the ability to recover from such disasters is built into their hosting plans.

Kinsta is now offering our [dedicated server](https://kinsta.com/blog/dedicated-server/) customers disaster recovery backed by continuous data replication between geographically separate data centers.

## Real disaster recovery is more than just a backup

If you accidentally delete important files or database tables (or even your entire website), it can *feel* like a disaster. Still, that’s a situation from which Kinsta customers can generally recover quickly, thanks to the automatic backups created at least daily on our platform.

But a real disaster — perhaps caused by fire, flood, earthquake, even war — can render an entire data center inaccessible. And backups are typically co-located in your website’s data center.

What’s more, provisioning a new virtual server in a different data center can take time. Kinsta’s disaster recovery solution helps you restore service in another location quickly, with access to more recent data than you may have with off-site backups alone.

The Disaster Recovery add-on for dedicated server customers provides continuous asynchronous data replication between a current live server and a secondary server ready to go live in a distant data center.

Asynchronous replication means the data on the recovery server can be a couple of minutes behind, though this window can extend under heavy traffic or high write loads. In the event of a true disaster, switching traffic to the recovery server is a deliberate, hands-on process rather than an instant automatic failover, so there will be a window of downtime while failover is carried out.

Customers who choose the disaster recovery add-on can count on Kinsta’s Support team to be with them every step of the way. First, we’ll identify a secondary data center that supports any geolocation requirements you might have. If a disaster occurs, we’ll assess the situation, handle the switchover to your recovery environment, and notify you once your site is back online. When it’s time to return to your original data center, we’ll work with you to coordinate the move back

If your business needs this kind of protection against data center disasters, [Kinsta Support](https://kinsta.com/docs/support/contact-support/) can get you connected.

## Dedicated servers for WordPress hosting at Kinsta

Complex MySQL queries and PHP code interpretation can sap server resources. When the result of that processing is difficult to cache, as it is for many e-commerce sites, the server load can be unrelenting.

Kinsta’s dedicated servers provide customers with full access to a cloud device’s CPU and RAM to handle such loads. Many customers opt for dedicated servers to handle anticipated traffic surges during a major sales event or high-profile promotion, when additional resources and more control over PHP settings can be critical.

You can begin the process of obtaining a dedicated server for your website in MyKinsta by navigating to **Sites** > ***sitename*** > **Add-ons** and then clicking the **Request add-on** button under **Dedicated server**:

![A screenshot showing the Dedicated server option among the add-ons available in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/08/mykinsta-add-ons-dedicated-server.png)

Beginning the request for a dedicated server in MyKinsta.

You’ll be asked for dedicated server requirements to complete the add-on request, and then our account management team will follow up to help get your server running.

And now, our dedicated server customers can add disaster recovery support, backed by continuous data replication between geographically separated data centers.
