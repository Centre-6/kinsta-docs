---
url: "https://kinsta.com/changelog/application-healthcheck/"
title: "Slash application downtime with Kinsta healthcheck"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-05-14T19:05:00"
change_signal: "2026-05-14T19:05:00"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "4d11df7ddd7b883626c60bb2ff901cea8b99e4bfdc3f3afaff12322578268e1f"
body_chars: 3286
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Slash application downtime with Kinsta healthcheck

**Product:** Changelog
**Source:** https://kinsta.com/changelog/application-healthcheck/
**Kinsta last updated:** 2026-05-14T19:05:00

---

A new healthcheck feature can help [Web Application Hosting](https://sevalla.com/application-hosting/) customers keep their apps up and running consistently, even during redeployments.

Application owners can enable healthcheck by defining a health-testing endpoint (path) within an app’s [web process](https://docs.sevalla.com/applications/processes#web-process) settings. Kinsta’s healthcheck service polls that endpoint every 10 seconds with the expectation that a healthy application will return an [HTTP request](https://kinsta.com/blog/what-is-an-http-request/) response of 200 (success).

Kinsta’s healthcheck helps improve an application’s uptime in two ways:

1. During regular runtime, Kinsta will attempt to restart the application’s pods automatically if the check fails three times in a row.
2. During the redeployment of an application, Kinsta will keep the existing pod running until the new deployment successfully responds to the healthcheck polling. That’s zero downtime on deployments!

## Enable healthcheck for your application

To specify a healthcheck endpoint for your application within the MyKinsta dashboard, navigate to **Applications** > ***app_name*** > **Processes** and then click the **Edit** icon beside your app’s web process:

![Screen shot showing an application's process list in the MyKinsta dashboard.](https://kinsta.com/wp-content/uploads/2024/05/application-healthcheck-edit-process.png)

Locating the Edit icon for an application’s web process.

Below, we’ve specified the path `/health` for an application’s healthcheck endpoint in the **Edit process** dialog:

![Screenshot of the Edit Process dialog in the MyKinsta dashboard.](https://kinsta.com/wp-content/uploads/2024/05/application-healthcheck-edit-path.png)

Adding a healthcheck path to an application’s web process.

You can specify any healthcheck path for which a successful HTTP response would signify that your application is up and running. That could be as simple as your application’s root path `/` or an endpoint specifically developed for the healthcheck task.

If your application requires database access to be fully functional, your healthcheck endpoint should return a successful HTTP response only if database connectivity is functional. This will ensure that a deployment that includes a database won’t go live until the app and its database are talking.

## Choose Kinsta for zero downtime

If you’re not already a Kinsta customer, here’s how you can get your next project deployed without downtime on our Application Hosting platform:

1. Get inspired by browsing our library of [quick-start examples](https://docs.sevalla.com/templates/overview) to see how to deploy your favorite technologies from Git hosts like [GitHub](https://docs.sevalla.com/applications/git/github#authenticate-and-authorize), [GitLab](https://docs.sevalla.com/applications/git/gitlab#authorize-the-kinsta-gitlab-application), and [Bitbucket](https://docs.sevalla.com/applications/git/bitbucket#grant-access-to-the-kinsta-bitbucket-application).
2. [Create your MyKinsta account](https://kinsta.com/signup/wp/) and start building risk-free!

When you deploy, your application will run on top-tier infrastructure in the [Google Cloud](https://kinsta.com/blog/cloud-platform-for-developers/).
