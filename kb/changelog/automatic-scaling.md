---
url: "https://kinsta.com/changelog/automatic-scaling/"
title: "Automatic Scaling Helps Your Application Keep Pace With Demand"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Automatic Scaling Helps Your Application Keep Pace With Demand"]
kinsta_last_updated: "2026-05-14T19:00:51+00:00"
sitemap_lastmod: "2026-05-14T19:00:51+00:00"
fetched_at: "2026-10-07T22:36:13Z"
sha256: "4ff3beace654a915cf8fb3f292376be5c56e6dc911242cf614c3da263f2b3ba9"
body_chars: 5533
extracted_with: "main article"
status: "live"
---

# Automatic Scaling Helps Your Application Keep Pace With Demand

**Section:** Changelog > Automatic Scaling Helps Your Application Keep Pace With Demand
**Product:** Changelog
**Source:** https://kinsta.com/changelog/automatic-scaling/
**Kinsta last updated:** 2026-05-14T19:00:51+00:00

## On this page

- [Enabling Automatic Horizontal Scaling](#enabling-automatic-horizontal-scaling)
- [How Automatic Scaling Works at Kinsta](#how-automatic-scaling-works-at-kinsta)
- [Start Autoscaling Your Application Today](#start-autoscaling-your-application-today)

---

Updated
:   May 14, 2026

![Illustration representing the automatic horizontal scaling configuration interface.](https://kinsta.com/wp-content/uploads/2023/10/automatic-scaling-1024x536.jpg)

The addition of automatic horizontal scaling to Kinsta’s Application Hosting platform means it’s now easier to deliver exactly the power your app needs to meet changing demands on server resources.

Horizontal scaling — adding or removing instances of pods running your application’s web process — can now be configured to trigger automatically based on CPU usage. That can help your application ramp up to handle heavy loads or scale back in both power and cost when demand is lower.

Giuseppe Silletti, Tech Lead for a team of Kinsta’s [Application Hosting](https://sevalla.com/application-hosting/) and [Database Hosting](https://sevalla.com/database-hosting/) developers, says variability in demand on server resources is common for web applications.

“Imagine an ecommerce platform experiencing a sudden surge in traffic due to a flash sale,” Silletti explains. “Thousands of users are simultaneously accessing the website to browse products, add items to their carts, and proceed to checkout. The sudden influx of traffic increases the CPU and memory utilization of the web server. The CPU utilization spikes to 85%, well above the normal levels. The current number of web server instances is insufficient to handle this increased load, resulting in delayed response times and potential timeouts.”

“Horizontal scaling becomes essential here,” he says. “By monitoring metrics like CPU utilization, additional web server instances are spun up to distribute the incoming traffic load, ensuring that the user experience remains seamless and responsive.”

## Enabling Automatic Horizontal Scaling

When configuring your applications on the Kinsta platform, you can specify the CPU and memory requirements of Kubernetes pods for web service, background worker, and [cron job processes](https://docs.sevalla.com/applications/processes#cron-job-process). You can also manually choose how many instances of each pod are needed.

When specifying resources for a web service, the new **[Automatic scaling](https://docs.sevalla.com/applications/scalability#automatic-horizontal-scaling)** option allows you to define a minimum and maximum number of pods (anywhere from 1 to 10) for the process.

![Screenshot: Automatic scaling configuration in the MyKinsta dashboard. ](https://kinsta.com/wp-content/uploads/2023/10/autoscaling-enabled-during-application-creation.png)

**Automatic scaling**: Choose minimum and maximum numbers of pod instances.

“Increasing the pod size — vertical scaling — means augmenting the CPU, memory, and other resources allocated to each existing pod,” Silletti says. “It’s a quick way to enhance the performance but has limitations due to the maximum resources available on the node.”

“Increasing the number of pods — horizontal scaling — involves deploying additional instances of the pod across the cluster,” he says. “It’s a more flexible approach to manage increased load and is not limited by the individual node’s capacity.”

## How Automatic Scaling Works at Kinsta

With automatic scaling enabled, demand on the Web service’s pods is monitored to see if loads are below or above 80% of capacity.

“When the CPU usage exceeds the defined threshold, Kubernetes autoscaling triggers the creation of additional pods to balance the load,” Silletti says. “The service’s load balancer automatically identifies these new pods and distributes incoming traffic among all available pods.”

“When Kubernetes identifies that the resource utilization is below the defined threshold, it initiates the process to remove pods. It ensures that even after removing a pod, the remaining pods can efficiently handle the traffic load while staying below the threshold.”

Even with automatic scaling enabled, users might need help determining what values to select for those minimum and maximum pod instances. Silletti’s advice?

“Initially, set a baseline for your app’s resource usage under normal and peak load conditions,” he says. “Then utilize tools and metrics to monitor the application’s performance and resource utilization. Reevaluate and adjust the configurations as needed to ensure optimal performance.”

## Start Autoscaling Your Application Today

Do you have an idea for an application that could benefit from the automatic scaling of pod resources? Here’s how you can get up to speed quickly with Kinsta’s Application Hosting platform:

1. Browse our growing library of [quick-start examples](https://docs.sevalla.com/templates/overview) to see how to deploy your favorite technologies from Git hosts like [GitHub](https://docs.sevalla.com/applications/git/github#authenticate-and-authorize), [GitLab](https://docs.sevalla.com/applications/git/gitlab#authorize-the-kinsta-gitlab-application), and [Bitbucket](https://docs.sevalla.com/applications/git/bitbucket#grant-access-to-the-kinsta-bitbucket-application).
2. Review our official [application scaling documentation](https://docs.sevalla.com/applications/scalability).
3. Create your MyKinsta account and start building risk-free!

When you deploy, your code and its persistent storage services will run on the [Google Cloud Platform’s](https://kinsta.com/blog/cloud-platform-for-developers/) top-tier infrastructure, backed by the platform’s [C2 virtual machines](https://kinsta.com/wordpress-hosting/).

That’s a home for your application with room to grow.
