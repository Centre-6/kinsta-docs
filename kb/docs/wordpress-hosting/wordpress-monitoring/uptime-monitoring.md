---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/uptime-monitoring/"
title: "Uptime Monitoring"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-monitoring"
section: ["WordPress Hosting", "Monitoring"]
kinsta_last_updated: "2026-02-27T10:05:44"
change_signal: "2026-02-27T10:05:44"
fetched_at: "2026-10-07T22:58:19Z"
sha256: "064aa4a1c7c4b54e9a6fd2f9ad0e260ac3b2c2c62cec3db4433dc229bdffd150"
body_chars: 3916
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Uptime Monitoring

**Section:** WordPress Hosting > Monitoring
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/uptime-monitoring/
**Kinsta last updated:** 2026-02-27T10:05:44

---

We monitor the uptime of all WordPress sites on our platform, checking your site every 3 minutes. If our monitoring detects that a site isn’t loading due to an infrastructure issue, our engineers respond quickly to get service restored to the site. If the issue is caused by something on the site itself, like a plugin conflict or a code error, we’ll notify you, but resolving it is outside our [scope of support](https://kinsta.com/docs/support/scope-of-support/).

Additionally, when WordPress site monitoring notifications are enabled in MyKinsta (**User Settings** > **Notifications**), if we detect one of the errors below in 3 consecutive checks on your WordPress site, we’ll send you an email to let you know your site needs critical attention:

- **Site Errors** – We use a custom-built tool to monitor for errors on your site, regardless of the cause. If we detect one, we’ll send you an email notification. This notifies you of the issue but doesn’t necessarily mean our team will resolve it, depending on the cause.
- **SSL Errors** – If there’s a configuration issue with your domain and the SSL certificate expires, we’ll notify you.
- **Domain Expiration** – If we detect an expired domain assigned to your Kinsta site, we’ll send you an alert.
- **Domain Resolution** – If we detect that a domain cannot be resolved due to incorrect DNS configuration, misconfigured nameservers, or temporary DNS resolution failures, we’ll email you to let you know.

![Example of a monitoring notification email](https://kinsta.com/wp-content/uploads/2023/11/wordpress-monitoring-notification-1-1024x876.png)

Example of a monitoring notification email

## Maintenance period

Kinsta’s maintenance window occurs daily, Monday through Sunday, from 2 am to 5 am local time, aligned with the time zone of the respective data center hosting each application or site. While maintenance isn’t necessarily conducted every day, if it does occur, it will take place within this timeframe. Typically, there is no downtime in this duration, resulting in little to no impact on your websites, applications, and databases. If you want to view information about specific maintenance or find out if there are any disruptions to our website, control panel, or hosting platform, refer to the [Kinsta Status page](https://status.kinsta.com/).

We do not send monitoring notifications if maintenance is performed during this time. For more information, refer to [Kinsta’s Service Level Agreement](https://kinsta.com/legal/service-level-agreement/).  

## WordPress site monitoring notes

Some scenarios that may interfere with our uptime monitoring include:

- [Password protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/htpasswd/) (basic authentication). If this is enabled, your site will return a 401 error to our monitor.
- A site in maintenance mode (which can happen when running updates or if a maintenance mode plugin is enabled) may return a 503 response, which prevents monitoring.
- We can’t monitor non-WordPress sites.
- Bot blocking service or plugin. If you block all bots or if you’ve blocked our *kinsta-bot* user agent, our monitor will receive a 406 response code and won’t be able to monitor the site.
- If either our uptime monitor’s IP address(es) or origin country (geo-blocking) is blocked, this will prevent monitoring. If you activate these features on Kinsta’s servers, we can add exceptions so our monitor won’t be blocked.
- Custom caching rules and configurations at CDN, proxy, or security services may cause issues. Caching everything, including Kinsta’s query string HEAD request, will interfere with our monitoring.
- Sites with reverse proxy setups where the primary domain isn’t redirecting to the target URL can’t be monitored.
- If the primary domain doesn’t resolve to the install where it’s added, or it has a redirect to another domain (listed in the same site’s domain list).
