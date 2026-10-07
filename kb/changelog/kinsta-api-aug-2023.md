---
url: "https://kinsta.com/changelog/kinsta-api-aug-2023/"
title: "Introducing New Kinsta API Endpoints (Environment CRUD, Edge Caching, Application Deployment)"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-09-16T09:42:59"
change_signal: "2026-09-16T09:42:59"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "c82126c1412a5e4c4f3bd3a50d14118d730034b93d436f992f59084889e4f96a"
body_chars: 7408
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Introducing New Kinsta API Endpoints (Environment CRUD, Edge Caching, Application Deployment)

**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-aug-2023/
**Kinsta last updated:** 2026-09-16T09:42:59

## On this page

- [What’s New In Kinsta API](#whats-new-in-kinsta-api)
  - [Application Hosting](#application-hosting)
    - [Manual Deployment](#manual-deployment)
  - [WordPress Hosting](#wordpress-hosting)
    - [Block/Unblock IP Addresses](#blockunblock-ip-addresses)
    - [Clearing Edge Cache](#clearing-edge-cache)
    - [Site Environments](#site-environments)
    - [Clone and Delete Sites](#clone-and-delete-sites)
    - [Examples](#examples)
  - [Database Hosting](#database-hosting)
- [Get Started With Kinsta API Today](#get-started-with-kinsta-api-today)

---

About three months ago, we [launched the beta version of the Kinsta API](https://kinsta.com/changelog/kinsta-api/) with functionalities that included retrieving details about WordPress, Applications, and Databases. It also allowed [creating a WordPress site](https://api-docs.kinsta.com/api-reference/wordpress-sites/create-a-site), [clearing site cache](https://api-docs.kinsta.com/api-reference/wordpress-site-tools/clear-site-cache), [restarting PHP engines](https://api-docs.kinsta.com/api-reference/wordpress-site-tools/restart-an-environments-php-engine), and tracking these resource-intensive [operation statuses](https://api-docs.kinsta.com/api-reference/operations/get-the-status-information-of-an-operation).

Since then, the [Kinsta API](https://kinsta.com/docs/kinsta-api/) team has been dedicated to continuously expanding the API’s capabilities based largely on user input. Kristof Siket, the Development Team Lead for the Kinsta API, affirmed the crucial role of your feedback in shaping feature priorities:

> User feedback drives the prioritization of feature exposure. If you believe a specific tool or endpoint should be included in the Kinsta API, feel free to [send in your feedback](https://kinsta.com/docs/service-information/kinsta-research-program/#how-to-join).

## What’s New In Kinsta API

The [Kinsta API](https://api-docs.kinsta.com/) has undergone substantial growth, introducing numerous new endpoints to complement its existing services. Let’s delve into these additions, highlighting how they enrich the management of [applications](https://sevalla.com/application-hosting/), [WordPress sites](https://kinsta.com/wordpress-hosting/), and [databases](https://sevalla.com/database-hosting/).

### Application Hosting

Upon its initial release, the Kinsta API provided access to application-related information, including deployment and [process details](https://api-docs.kinsta.com/tag/Application-Processes#operation/getProcessById), contributing to analytics data. Now, this information has been organized more effectively, enabling not just retrieval of deployment details.

#### Manual Deployment

You can now trigger application deployment through the [API](https://kinsta.com/blog/rest-api-vs-web-api/) with the [manual deployment](https://api-docs.kinsta.com/tag/Application-Deployments#operation/manualDeployApplication) endpoint. This means you can now programmatically deploy an application through various means, such as the terminal, a [CI/CD pipeline](https://kinsta.com/blog/how-to-setup-ci-cd-pipeline/), or an HTTP request.

Kristof notes that “while manual deployment is not yet equivalent to a Kinsta CLI’s `kinsta deploy` or `kinsta up` command (which would deploy directly from the file system rather than a Git branch), it’s already a valuable feature for customizing workflows”.

Manual deployment allows you to adopt Continuous Deployment & Delivery methodologies in your DevOps workflow, as we’ve detailed in articles featuring GitHub Actions and CircleCI integration:

- [How to Setup a CI/CD Pipeline with GitHub Actions and Kinsta API](https://kinsta.com/blog/how-to-setup-ci-cd-pipeline/)
- [Continuous Deployment of React Apps With CircleCI & Kinsta API](https://kinsta.com/blog/react-continuous-deployment/)

### WordPress Hosting

The number of endpoints for WordPress hosting has grown significantly compared to other services.

#### Block/Unblock IP Addresses

In addition to the clear site cache and restarting PHP engine site tools, we now have endpoints for you to [get the list of denied IPs](https://api-docs.kinsta.com/api-reference/wordpress-site-tools/get-list-of-denied-ips) and another to [update the list](https://api-docs.kinsta.com/api-reference/wordpress-site-tools/update-denied-ip-list). This simplifies the process of blocking unwanted IP addresses, whether they belong to bots, spammers, or other sources of malicious behavior.

#### Clearing Edge Cache

We have also created endpoints for [clearing a site’s edge cache](https://api-docs.kinsta.com/api-reference/wordpress-edge-caching/clear-site-edge-cache) with its environment ID. This is invaluable for agencies managing multiple sites as it enables integration with tools like [Slack](https://kinsta.com/blog/how-to-use-slack/) or custom interfaces, eliminating the need to navigate numerous MyKinsta pages.

#### Site Environments

A noteworthy set of new endpoints has also been released, enabling CRUD operations for WordPress site [environments](https://api-docs.kinsta.com/pages/wordpress-site-environments/description). This encompasses [retrieving environment details](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-site-environments), [creating WordPress site environments](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/create-a-wordpress-site-environment), [creating plain environments](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/create-a-plain-environment-no-wordpress-installed) devoid of WordPress installations, [cloning existing environments](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/clone-an-environment), and [deleting WordPress site environments](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/delete-a-wordpress-site-environment).

#### Clone and Delete Sites

Additionally, we’ve introduced the [clone site](https://api-docs.kinsta.com/api-reference/wordpress-sites/clone-existing-site) endpoint. Kristof explains that “cloning was a requested feature, particularly for agencies aiming to create sites from a **base site** with all necessary plugins and themes pre-installed”.

We’ve also incorporated the [delete site](https://api-docs.kinsta.com/api-reference/wordpress-sites/delete-a-site) endpoint, now complementing the create site endpoint. You can initiate site creation and deletion via the API.

#### Examples

We’ve written multiple guides showcasing diverse applications of the WordPress hosting endpoints:

- [How To Create a WordPress Site With Kinsta API](https://kinsta.com/blog/wordpress-api/)
- [How To Create and Use Kinsta API Access Key](https://kinsta.com/blog/kinsta-api-key/)
- [How To Clone a WordPress Site Using the Kinsta API and React](https://kinsta.com/blog/clone-site-kinsta-api/)
- [How To Build a Slackbot With Node.js and Kinsta API for Site Management](https://kinsta.com/blog/create-slackbot-site-management/)
- [Schedule Your Maintenance Tasks With Kinsta API (Clear Cache, Restart PHP Engine)](https://kinsta.com/blog/schedule-tasks-kinsta-api/)

### Database Hosting

While there haven’t been any major additions to Database hosting endpoints, we have deprecated the get database by name endpoint in favor of [get database with ID](https://api-docs.kinsta.com/tag/Databases#operation/getDatabaseById).

## Get Started With Kinsta API Today

There is a lot that can be done with the Kinsta API. Feel free to check out our [documentation](https://kinsta.com/docs/kinsta-api/) to understand [what’s possible](https://kinsta.com/docs/kinsta-api/#common-use-cases) with the API, how to get started, and the various [permission levels](https://kinsta.com/docs/kinsta-api/#authentication-and-user-access) and [limits to the API](https://kinsta.com/docs/kinsta-api/#rate-limit).

Unleash the power of automation and increase efficiency with the convenience of Kinsta API. Get started today!
