---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/wordpress-infrastructure/"
title: "Get Started - Infrastructure"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-getting-started"
section: []
kinsta_last_updated: "January 13, 2026"
sitemap_lastmod: "2026-01-13T15:49:38+00:00"
fetched_at: "2026-10-07T22:37:49Z"
sha256: "bed97794a8868645e147416a0ef894238389079e4152833a320b17c63517ce6b"
body_chars: 2150
extracted_with: "main article"
status: "live"
---

# Get Started - Infrastructure

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/wordpress-infrastructure/
**Kinsta last updated:** January 13, 2026

---

Our [managed WordPress hosting](https://kinsta.com/wordpress-hosting/) platform doesn’t fall into any of the traditional hosting categories. Kinsta’s top-tier cloud infrastructure and high-performance servers deliver dedicated resources and lightning-fast speeds from 30 global data centers, allowing you to host closer to your audience for optimal performance.

Every site on our platform runs in an **isolated software container** that contains all of the software resources required to run the site (Linux, NGINX, PHP, MySQL). This means that the software that runs each site is **100% private and is not shared** even between your own sites.

We use [Linux containers](https://linuxcontainers.org/) as the underlying container technology for our infrastructure.

![A diagram of Kinsta’s WordPress Hosting architecture.](https://kinsta.com/wp-content/uploads/2026/07/kinsta-wordpress-hosting-architecture.png)

A diagram of Kinsta’s WordPress Hosting architecture.

Each site container runs on a generously sized virtual machine in one of multiple [data centers](https://kinsta.com/docs/service-information/data-center-locations/) and is secured by our free Cloudflare integration.

On our standard plans, each live site container has access to 12 CPUs and 8 GB of RAM by default. Each [staging environment](https://kinsta.com/docs/wordpress-hosting/staging-environment/) on our standard plans has access to 1 CPU and 8 GB of RAM.

## Kinsta firewall

Kinsta offers a fully managed Web Application Firewall (WAF) with regularly updated custom rulesets and configurations, providing continuous protection against emerging threats. All web traffic is routed through Cloudflare, which delivers Layer 3, 4, and 7 DDoS protection and blocks malicious TCP/UDP connections at the network edge. Furthermore, we employ an automated feature that constantly detects brute force attacks on your site’s `/wp-login.php` path. We then block these actors from our entire infrastructure, further strengthening our security measures.

To learn more about how Kinsta is different from other hosts, read [Why us – how Kinsta is different](https://kinsta.com/why-us/).
