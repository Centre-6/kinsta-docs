---
url: "https://kinsta.com/changelog/improved-web-terminal/"
title: "An improved Web Terminal for apps gets you to the command line quicker"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "An improved Web Terminal for apps gets you to the command line quicker"]
kinsta_last_updated: "2026-05-14T19:01:16+00:00"
sitemap_lastmod: "2026-05-14T19:01:16+00:00"
fetched_at: "2026-10-07T22:37:33Z"
sha256: "c4dde5a083ae60343a401a8daf49dab24d22e66a9424e368d4e99a1d68fbd509"
body_chars: 3857
extracted_with: "main article"
status: "live"
---

# An improved Web Terminal for apps gets you to the command line quicker

**Section:** Changelog > An improved Web Terminal for apps gets you to the command line quicker
**Product:** Changelog
**Source:** https://kinsta.com/changelog/improved-web-terminal/
**Kinsta last updated:** 2026-05-14T19:01:16+00:00

---

Updated
:   May 14, 2026

![An illustration of the MyKinsta dashboard and the words: 'A better Web Terminal for App Hosting.'"](https://kinsta.com/wp-content/uploads/2024/04/improved-application-web-terminal-1024x536.png)

We’ve simplified the steps [Web Application Hosting](https://sevalla.com/application-hosting/) customers take to launch the MyKinsta Web Terminal and access the [containers](https://kinsta.com/blog/isolated-container-technology/) in which app processes are running.

The Web Terminal provides [command-line](https://kinsta.com/blog/linux-commands/) access to containers, allowing application developers to edit files and run scripts that help in application management or debugging.

Key changes in the new release of Web Terminal include:

- The terminal launches seamlessly within the [MyKinsta dashboard](https://kinsta.com/mykinsta/) instead of on a separate browser tab.
- Defining an IP “allowlist” is no longer required.
- Customers deploying applications using Dockerfiles are not required to specifically include Bash in their containers.

You can launch the Web Terminal in MyKinsta by selecting **Applications** > ***app name*** > **Web Terminal**:

![A screenshot of the application Web Terminal in the MyKinsta dashboard.](https://kinsta.com/wp-content/uploads/2024/04/mykinsta-applications-web-terminal.png)

An application Web Terminal associated with a web process running in MyKinsta.

You can now switch between terminals associated with different processes behind your application using a drop-down menu above the terminal window:

![Screenshot showing a closeup of the drop-down menu used to select application processes.](https://kinsta.com/wp-content/uploads/2024/04/mykinsta-web-terminal-select-process.png)

Selecting an alternate application process for Web Terminal access.

Above, we are about to switch to a terminal associated with a background worker process. This will disconnect the currently active web process terminal. (You can run multiple terminals simultaneously by opening MyKinsta’s Web Terminal page in separate browser tabs or windows.)

## Tips for using the Web Terminal

Here’s what to keep in mind when using the Web Terminal:

- The Web Terminal is available only when your application is deployed and running.
- Files you create within the terminal will not be available to your application unless you create them on a [persistent storage](https://kinsta.com/blog/persistent-storage/) volume associated with the app.
- Similarly, changes you make to files within the terminal will be lost during the next deployment unless those files are on persistent storage.
- There are no logs linked to Web Terminal activity.

## Take command of app development with Kinsta

An improved Web Terminal is just one of the recent enhancements rolled out for Application Hosting customers. We recently made it easier to [manage users](https://kinsta.com/changelog/paas-user-roles/) on your development team and added an “at-a-glance” view of your project’s components in a single [application diagram](https://kinsta.com/changelog/application-overview/). We’ve also made it possible to deploy applications from public Git repositories and using [Docker images](https://docs.sevalla.com/applications/docker-images).

If you aren’t already a Kinsta customer, browse our library of [quick-start examples](https://docs.sevalla.com/templates/overview) to see how to deploy your favorite technologies from Git hosts like [GitHub](https://docs.sevalla.com/applications/git/github#authenticate-and-authorize), [GitLab](https://docs.sevalla.com/applications/git/gitlab#authorize-the-kinsta-gitlab-application), and [Bitbucket](https://docs.sevalla.com/applications/git/bitbucket#grant-access-to-the-kinsta-bitbucket-application), and then start your [free trial](https://sevalla.com/application-hosting/) today.
