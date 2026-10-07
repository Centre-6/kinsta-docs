---
url: "https://kinsta.com/changelog/static-site-hosting/"
title: "Kinsta Static Site Hosting is Fast and Free"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Kinsta Static Site Hosting is Fast and Free"]
kinsta_last_updated: "2026-05-06T14:31:09+00:00"
sitemap_lastmod: "2026-05-06T14:31:09+00:00"
fetched_at: "2026-10-07T22:36:06Z"
sha256: "e055883bb324511a9cf47dbd8714017abffb4ff9168de4c2064353f3fd49320e"
body_chars: 6634
extracted_with: "main article"
status: "live"
---

# Kinsta Static Site Hosting is Fast and Free

**Section:** Changelog > Kinsta Static Site Hosting is Fast and Free
**Product:** Changelog
**Source:** https://kinsta.com/changelog/static-site-hosting/
**Kinsta last updated:** 2026-05-06T14:31:09+00:00

## On this page

- [Static Site Basics](#static-site-basics)
- [What You Get for Free With Static Site Hosting](#what-you-get-for-free-with-static-site-hosting)
- [How Static Site Hosting Works at Kinsta](#how-static-site-hosting-works-at-kinsta)
- [Time to Start Building Your Static Site](#time-to-start-building-your-static-site)

---

Updated
:   May 6, 2026

![An illustration representing static site hosting.](https://kinsta.com/wp-content/uploads/2023/10/free-static-site-hosting-1024x536.jpg)

After months of Beta testing, Kinsta is making [Static Site Hosting](https://sevalla.com/static-site-hosting/) available to anyone who needs to serve up HTML pages and assets like JavaScript and CSS files at lightning-fast speed.

Kinsta can build and push your static site project to the 300+ data centers in the [Cloudflare](https://kinsta.com/cloudflare-integration/) global network — and we do it for free.

Wait! Fast *and* free?

Yes, and to help explain how we do that, let’s back up and answer the question: [What is a static website](https://kinsta.com/blog/what-is-a-static-website/)?

## Static Site Basics

“Static Site Hosting serves files without any kind of backend processing,” says Andras Gerencser, Director of Development at Kinsta. “This simplicity makes it an efficient, high-performance hosting option.”

Gerencser says typical components of a static website — [HTML](https://kinsta.com/blog/what-is-html/), [CSS](https://kinsta.com/blog/css-best-practices/), [JavaScript](https://kinsta.com/javascript/), and media files — can be delivered to browsers without being generated dynamically by code running on a server.

“Some basic examples include personal portfolios, CV websites, simpler business websites, marketing pages, or documentation sites,” he says. “It’s also possible to use [static site generators](https://docs.sevalla.com/static-sites/get-started/static-site-generators) to compile static assets from other sources, such as Markdown files or a CMS.”

Michael Fuller, a JavaScript developer at Kinsta who helped launch Static Site Hosting, adds that static site generators turn those inputs into “a working website”:

“They do this by providing themes, plugins, and automating repetitive tasks such as replacing text, creating links between pages, image optimization, or converting a document into HTML,” he says.

And Gerencser points out that “static sites” can be more dynamic than that label implies.

“You can use Static Site Hosting to set up a frontend with any kind of backend, such as a Node.js service on our [Application Hosting](https://sevalla.com/application-hosting/) platform or a headless WordPress running on our [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/) platform,” he says.

Fuller calls that a “mixed approach”:

“Since JavaScript is usually served as a static asset, you can create a static site that uses a JavaScript framework to talk to a server managed separately,” he says. “This way, you get the speed benefits in your initial load times, combined with the flexibility of a dynamic site.”

## What You Get for Free With Static Site Hosting

In addition to the tools used to build and deploy your static sites, free [SSL certificates](https://docs.sevalla.com/applications/domains#install-a-custom-ssl-certificate), support for [custom domain names](https://docs.sevalla.com/applications/domains), and an optional [API for site management](https://api-docs.kinsta.com/tag/Static-Sites), Kinsta’s free hosting is available for those whose projects adhere to the following (generous) limits:

- 100 static sites per company
- 1 concurrent build per site
- 1 GB build image size per site
- 600 build minutes per month per company
- 100 GB bandwidth per month per company

## How Static Site Hosting Works at Kinsta

Developers deploying a static site with Kinsta begin with their project in a Git repository hosted by [BitBucket](https://docs.sevalla.com/applications/git/bitbucket#grant-access-to-the-kinsta-bitbucket-application), [GitHub](https://docs.sevalla.com/applications/git/github#authenticate-and-authorize), or [GitLab](https://docs.sevalla.com/applications/git/gitlab#authorize-the-kinsta-gitlab-application). A connection to the Git repository and configuration settings required to build and deploy the site is managed through [MyKinsta](https://kinsta.com/mykinsta/).

But your website doesn’t have to be built using a static site generator. As long as you can get your static web assets into a repository at one of the supported Git hosts, your project can be deployed as a static site.

![Screenshot: Creating an initial static site in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/10/create-static-site-mykinsta-start.png)

Getting started with your first static site in MyKinsta.

When you [add a static site](https://docs.sevalla.com/static-sites/get-started/add-a-static-site) that is built when deployed, MyKinsta can automatically detect the build settings required by a variety of popular static site generators:

![Screenshot: Suggested static site build settings.](https://kinsta.com/wp-content/uploads/2023/10/static-site-hosting-build-settings.png)

Build settings detected for a project using Astro to generate a static site.

“After that,” says Gerencser, “MyKinsta passes the files from your repository to an isolated pod in one of our Kubernetes clusters, which can run your build command if needed. The output — your static files — will then be uploaded to Cloudflare’s R2 storage.”

“This means that your files are distributed to more than 260 Cloudflare servers around the world — always delivering them from the nearest location to your website visitors,” he says.

![Diagram showing the resources used for static site hosting at Kinsta.](https://kinsta.com/wp-content/uploads/2023/10/static-site-hosting-infrastructure.png)

A look at the infrastructure behind Kinsta’s Static Site Hosting.

With your static site up and running, you can make it public in style with your own domain name and free SSL support:

![Screenshot: Adding a custom domain for a static site.](https://kinsta.com/wp-content/uploads/2023/10/static-site-hosting-add-domain.png)

Adding a custom domain for your static site in MyKinsta

## Time to Start Building Your Static Site

If you want to get up and running quickly with [Static Site Hosting](https://sevalla.com/static-site-hosting/) at Kinsta, see our growing library of [quick-start examples](https://docs.sevalla.com/templates/overview) for compatible static site generators. These examples include Git repositories you can copy to kick-start your own deployments.

Want to get fancy with your “static” site and generate dynamic content using JavaScript? Combine [Static Site Hosting](https://sevalla.com/static-site-hosting/) with [Application Hosting](https://docs.sevalla.com/applications/overview) and [Database Hosting](https://sevalla.com/database-hosting/) to build the backend your web project needs.
