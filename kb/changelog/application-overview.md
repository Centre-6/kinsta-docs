---
url: "https://kinsta.com/changelog/application-overview/"
title: "MyKinsta offers a \"big-picture\" view of your application"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "MyKinsta offers a \u201cbig-picture\u201d view of your application"]
kinsta_last_updated: "2026-05-14T19:01:52+00:00"
sitemap_lastmod: "2026-05-14T19:01:52+00:00"
fetched_at: "2026-10-07T22:36:14Z"
sha256: "9e9b8b0306bd1c5456526f3312406bed233777a381808633daace79046e0cabe"
body_chars: 4487
extracted_with: "main article"
status: "live"
---

# MyKinsta offers a "big-picture" view of your application

**Section:** Changelog > MyKinsta offers a “big-picture” view of your application
**Product:** Changelog
**Source:** https://kinsta.com/changelog/application-overview/
**Kinsta last updated:** 2026-05-14T19:01:52+00:00

---

Updated
:   May 14, 2026

![Illustration of the Application Overview diagram in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/04/new-app-overview-page-mykinsta-1024x536.png)

An update of the [MyKinsta](https://kinsta.com/mykinsta/) dashboard gives [Web Application Hosting](https://sevalla.com/application-hosting/) customers a new perspective on their projects.

The **Overview** page for each application now includes a visual representation of the various components behind the app — from the client-facing features of Kinsta’s [Cloudflare integration](https://kinsta.com/blog/cloudflare-integration/) to the processes running on our [Google Cloud](https://kinsta.com/blog/cloud-platform-for-developers/) virtual machines.

Access an **Overview** page and the new app diagram by selecting **Applications** on MyKinsta’s left-hand menu, choosing one of your current apps, and then clicking on the menu’s **Overview** option:

![Screenshot of the application overview diagram in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/04/mykinsta-application-overview.png)

A diagram detailing an app’s various components in MyKinsta.

Also on the **Overview** page, below the diagram, is a list of the application’s most recent deployments.

## What you’ll find on the Overview diagram

Let’s take a closer look at the information you’ll find on the **Overview** page’s application diagram.

Under the application name at the top of the page is information about your [Git repository](https://docs.sevalla.com/applications/git/overview), including:

- Whether automatic deployment on Git commits is enabled
- The name and path of your Git repository
- The name of the repository branch containing the application code

You can click on the branch name to visit the repository on your Git host.

![Screenshot: Detail of the application's Git repository information.](https://kinsta.com/wp-content/uploads/2024/04/mykinsta-application-overview-git.png)

Git repository information on the application diagram.

The left-hand side of the diagram details the client-facing side of your application and the status of services available through Cloudflare, including:

- Whether [DDoS protection](https://kinsta.com/blog/what-is-a-ddos-attack/) is enabled (enabled by default)
- Whether the [Kinsta CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/) is enabled
- Whether [Edge Caching](https://kinsta.com/blog/edge-caching/) is enabled

![Screenshot: Cloudflare services on the application overview diagram.](https://kinsta.com/wp-content/uploads/2024/04/mykinsta-application-overview-cloudflare.png)

The status of Cloudflare-based services in the application diagram.

The heart of the application diagram details the resources and settings for the processes running on Kinsta’s virtual machines.

Every application has a web process, and its card in the diagram displays details that include:

- The port on which the application is listening
- The application’s start command
- The server resources (RAM and CPUs)
- The number of instances
- The application’s domain (URL)

Your application may also have background workers and cron jobs, and cards for such processes will appear on the diagram with information on their resource usage.

![Screenshot: Application services detailed on the new overview diagram.](https://kinsta.com/wp-content/uploads/2024/04/mykinsta-application-overview-services.png)

Information about an application’s web process, background worker, and cron job.

Buttons on the cards allow you to click through directly to a service’s logs or settings.

## Start building your application

Looking for inspiration for your next application? Browse our library of [quick-start examples](https://docs.sevalla.com/templates/overview) to see how to deploy your favorite technologies from Git hosts like [GitHub](https://docs.sevalla.com/applications/git/github#authenticate-and-authorize), [GitLab](https://docs.sevalla.com/applications/git/gitlab#authorize-the-kinsta-gitlab-application), and [Bitbucket](https://docs.sevalla.com/applications/git/bitbucket#grant-access-to-the-kinsta-bitbucket-application).

Your application can adapt to surges in traffic with our optional [automatic scaling](https://kinsta.com/changelog/automatic-scaling/), or preserve data across deployments with [persistent storage](https://kinsta.com/changelog/persistent-storage/).

Get started with a [free trial](https://sevalla.com/application-hosting/) today.
