---
url: "https://kinsta.com/changelog/web-terminal/"
title: "Access Your Application Through the New Web Terminal"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Access Your Application Through the New Web Terminal"]
kinsta_last_updated: "2026-05-14T19:07:02+00:00"
sitemap_lastmod: "2026-05-14T19:07:02+00:00"
fetched_at: "2026-10-07T22:36:18Z"
sha256: "cd82bed2842a5338618cdb8bcfe7ff2db2457d61d0725a53a3fd33819b130e05"
body_chars: 3272
extracted_with: "main article"
status: "live"
---

# Access Your Application Through the New Web Terminal

**Section:** Changelog > Access Your Application Through the New Web Terminal
**Product:** Changelog
**Source:** https://kinsta.com/changelog/web-terminal/
**Kinsta last updated:** 2026-05-14T19:07:02+00:00

---

Updated
:   May 14, 2026

![Command line access with the new Kinsta Web Terminal feature](https://kinsta.com/wp-content/uploads/2023/05/Web_Terminal_Feature_Update_EN-1024x536.jpg)

The web terminal gives you command-line access to the web process on your application so you can securely run scripts and read files. This is a useful tool for debugging issues, performance monitoring, and manually executing scripts ad-hoc.

The commands available for execution depend entirely on which executables are available within your application.  
Currently, you can only run web processes with the Web Terminal. It doesn’t support background processes or [Cron jobs](https://kinsta.com/changelog/cron-jobs/).

Before you can use the web terminal, you need to set up authentication where you can specify exactly which IP addresses have access. You can go to [Test your IPv6](https://test-ipv6.com/) and use it to locate your own IP addresses. We recommend adding your IPv4 and IPv6 IP addresses, as the connection may come from either.

## How To Set Up Authentication

To access the web terminal, you must:

- Sign in to your [MyKinsta dashboard](https://my.kinsta.com/).
- Provide at least 1 valid IP address.
- Not duplicate IP addresses.
- Have at least one successful deployment.
- Have a healthy application that is running. If there are any errors or if the application is stopped, the web terminal will not be available.

![Access Web Terminal](https://kinsta.com/wp-content/uploads/2023/05/web-terminal-setup.png)

Access Web Terminal

To add IP addresses, click **Set up authentication**.

![Add an IP address](https://kinsta.com/wp-content/uploads/2023/05/add-ip-address.png)

Add an IP address

Enter the first IP address you want to allow. You can add more IP addresses by clicking on the **Add another** option. Once you have entered all the IP addresses you want to allow, click **Set up authentication**.

To find out more about Web Terminal, including how to start and stop, as well as how to set up Web Terminal with a Dockerfile and troubleshoot, check out our [Web Terminal documentation](https://docs.sevalla.com/applications/web-terminal).

## Why Host Your Application With Kinsta?

When you deploy your application to Kinsta from [GitHub, Bitbucket, or GitLab](https://kinsta.com/changelog/bitbucket-gitlab-support/), your code runs on the [Google Cloud Platform‘s](https://kinsta.com/blog/cloud-platform-for-developers/) top-tier infrastructure, powered by that platform’s [C2 virtual machines](https://kinsta.com/wordpress-hosting/) and in an isolated container.

And you can choose any of 24 data centers around the world as the home for your application.

Applications managed through your MyKinsta dashboard leverage Google Cloud Build, which generates the image of your application based on the information in buildpacks or your Dockerfile. If you configure your application to deploy automatically, that happens every time you commit a change to your repository on your Git host.

If your application is public-facing, you can rely on our Cloudflare integration for [DDoS protection](https://kinsta.com/blog/what-is-a-ddos-attack/).

Are you interested in trying out this feature? [You can do that for free](https://sevalla.com/application-hosting/)!
