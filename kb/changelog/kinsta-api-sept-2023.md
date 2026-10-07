---
url: "https://kinsta.com/changelog/kinsta-api-sept-2023/"
title: "New Kinsta API Endpoints: Clear CDN Cache and Push Environment"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-05-06T15:13:54"
change_signal: "2026-05-06T15:13:54"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "765f9bb34a95d32904d2145748a110600398dae7069f12230ce2510b5199d315"
body_chars: 5257
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# New Kinsta API Endpoints: Clear CDN Cache and Push Environment

**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-sept-2023/
**Kinsta last updated:** 2026-05-06T15:13:54

## On this page

- [5 New Kinsta API Endpoints](#5-new-kinsta-api-endpoints)
  - [1. Push Environment](#1-push-environment)
  - [2. Clear Kinsta CDN cache](#2-clear-kinsta-cdn-cache)
  - [3. Create Database](#3-create-database)
  - [4. Delete Database](#4-delete-database)
  - [5. Delete Application](#5-delete-application)
- [Get Started With Kinsta API Today](#get-started-with-kinsta-api-today)

---

Since the [launch of the Kinsta API](https://kinsta.com/changelog/kinsta-api/), our team has been actively introducing new endpoints. In our [most recent Changelog update](https://kinsta.com/changelog/kinsta-api-aug-2023/), Kristof Siket, the Development Team Lead for the Kinsta API, emphasized the significant role your feedback plays in shaping our feature priorities:

> *“User feedback drives the prioritization of feature exposure. If you believe a specific tool or endpoint should be included in the Kinsta API, feel free to [send in your feedback](https://kinsta.com/docs/service-information/kinsta-research-program/#how-to-join).”*

Today, we’re thrilled to announce the addition of five new endpoints to the API (Application Programming Interface). This release expands the capability of interacting programmatically with your applications, WordPress sites, and databases, opening up exciting possibilities for streamlined management and automation.

## 5 New Kinsta API Endpoints

Let’s delve into the new endpoints added to the API:

### 1. Push Environment

The [Push Environment endpoint](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/push-a-wordpress-site-environment) plays a pivotal role in our [WordPress Hosting](https://kinsta.com/wordpress-hosting/) service, enabling you to seamlessly transfer content from one environment to another. For instance, you can move content from a [staging to a live environment](https://kinsta.com/docs/wordpress-hosting/staging-environment/#push-staging-to-live-1).

This endpoint is good for automated workflows, where users can execute end-to-end (e2e) [tests](https://kinsta.com/blog/jest/) and then automatically promote the staging environment to live. It also fits perfectly into time-based release workflows, where all changes made to a default “dev” environment are released live every week.

### 2. Clear Kinsta CDN cache

The [Kinsta CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#kinstas-cdn) is enabled by default on all new sites. It leverages [Cloudflare’s network](https://kinsta.com/blog/cloudflare-integration/), offering a number of advantages over traditional CDN providers, such as [HTTP/3](https://kinsta.com/blog/http3/) support, [image optimization](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#image-optimization-1), and more.

Previously, we introduced an endpoint to [clear your WordPress site’s Edge Cache](https://api-docs.kinsta.com/api-reference/wordpress-edge-caching/clear-site-edge-cache), but now we’ve added an endpoint to [clear your CDN Cache](https://api-docs.kinsta.com/api-reference/wordpress-cdn/clear-site-cdn-cache), empowering you to programmatically clear both your site’s Edge cache and CDN cache.

Clearing the CDN cache is often the first step in troubleshooting when you encounter discrepancies on your site’s front end. You can opt to automate this process or create a command that can be [triggered via a Slackbot](https://kinsta.com/blog/create-slackbot-site-management/).

### 3. Create Database

For [Database Hosting](https://sevalla.com/database-hosting/), we are delighted to announce that you can now programmatically [create database](https://api-docs.kinsta.com/tag/Databases#operation/createDatabase) with the Kinsta API.

To create a database, simply specify the database type (e.g., Redis, PostgreSQL, MariaDB, or MySQL), version number, and other essential details like name, password, and username.

This allows you to create a [customized interface](https://kinsta.com/blog/wordpress-api/) for your company, simplifying the database management process without the need to access [MyKinsta](https://my.kinsta.com/).

### 4. Delete Database

Similar to the [create database](https://api-docs.kinsta.com/tag/Databases#operation/createDatabase) endpoint, you can also [delete database](https://api-docs.kinsta.com/tag/Databases#operation/deleteDatabase) with the API. To do this, all you need to specify is the database ID.

### 5. Delete Application

The [Application Hosting](https://sevalla.com/application-hosting/) service has seen substantial API enhancements, but one crucial endpoint was missing: [Delete Application](https://api-docs.kinsta.com/tag/Applications#operation/deleteApplication). With the addition of this endpoint, you can now effortlessly delete an application by specifying its ID programmatically.

This streamlines the process and eliminates the need to interact with the MyKinsta dashboard for routine operations.

## Get Started With Kinsta API Today

There is a lot that can be done with the Kinsta API. Feel free to check out the following to understand what’s possible with the API, how to get started, and the various permission levels and limits of the API:

- [Kinsta API Documentation](https://kinsta.com/docs/kinsta-api/)
- [Changelog 1: Introducing Kinsta API: The Power of Automation for Site Management](https://kinsta.com/changelog/kinsta-api/)
- [Changelog 2: Introducing New Kinsta API Endpoints (Environment CRUD, Edge Caching, Application Deployment)](https://kinsta.com/changelog/kinsta-api-aug-2023/)

Unlock the boundless potential of automation and enhance efficiency with the user-friendly Kinsta API. Get started today!
