---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/"
title: "WordPress Hosting - Analytics"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-analytics-mykinsta"
section: []
kinsta_last_updated: "May 20, 2026"
sitemap_lastmod: "2026-05-20T09:00:24+00:00"
fetched_at: "2026-10-07T22:38:53Z"
sha256: "2e1694f8f473b5e64458d652174e69e21b0b45f3cb36ae8ecb46b62e4c810f91"
body_chars: 39779
extracted_with: "main article"
status: "live"
---

# WordPress Hosting - Analytics

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/
**Kinsta last updated:** May 20, 2026

## On this page

- [Date selector](#date-selector)
  - [Billing period](#billing-period)
  - [Relative](#relative)
  - [Absolute](#absolute)
- [Download analytics](#download-analytics)
- [Plan usage](#plan-usage)
  - [What counts toward your plan usage (billable)](#what-counts-toward-your-plan-usage-billable)
  - [What does not count toward your plan usage](#what-does-not-count-toward-your-plan-usage)
  - [Plan usage overview](#plan-usage-overview)
  - [Plan usage distribution](#plan-usage-distribution)
  - [Visits](#visits)
  - [Bandwidth](#bandwidth)
  - [Disk space](#disk-space)
- [Top requests](#top-requests)
  - [Top requests by server bandwidth](#top-requests-by-server-bandwidth)
  - [Top requests by total bandwidth](#top-requests-by-total-bandwidth)
  - [Top requests by views](#top-requests-by-views)
- [Cache](#cache)
  - [Cache breakdown](#cache-breakdown)
  - [Server cache component stack](#server-cache-component-stack)
  - [Server cache component chart](#server-cache-component-chart)
  - [Top server cache bypasses](#top-server-cache-bypasses)
- [CDN & edge](#cdn-edge)
  - [CDN bandwidth](#cdn-bandwidth)
  - [Edge cache bandwidth](#edge-cache-bandwidth)
  - [Top files by requests](#top-files-by-requests)
  - [Top files by bytes](#top-files-by-bytes)
  - [Top file extensions by bytes](#top-file-extensions-by-bytes)
- [Performance](#performance)
  - [Average PHP + MySQL response time](#average-php-mysql-response-time)
  - [PHP throughput](#php-throughput)
  - [PHP memory limit reached](#php-memory-limit-reached)
  - [PHP thread limit](#php-thread-limit)
  - [AJAX usage](#ajax-usage)
  - [Top average PHP + MySQL response time](#top-average-php-mysql-response-time)
  - [Top maximum upstream time](#top-maximum-upstream-time)
- [Response](#response)
  - [Response code breakdown](#response-code-breakdown)
  - [Response stats](#response-stats)
  - [500 error breakdown](#500-error-breakdown)
  - [400 error breakdown](#400-error-breakdown)
  - [Redirect breakdown](#redirect-breakdown)
  - [Top 404 errors](#top-404-errors)
- [Audience](#audience)
  - [Top countries](#top-countries)
  - [Top browsers](#top-browsers)
  - [Top cities](#top-cities)
  - [Top user agents](#top-user-agents)
  - [Top referrers](#top-referrers)
  - [Top ASN](#top-asn)
  - [Top client IPs](#top-client-ips)
  - [Desktop vs. tablet vs. mobile](#desktop-vs-tablet-vs-mobile)
- [Bot traffic](#bot-traffic)
  - [Requests](#requests)
  - [Bot protection results](#bot-protection-results)
  - [Top traffic](#top-traffic)
  - [Spikes in bot traffic charts](#spikes-in-bot-traffic-charts)

---

With WordPress Analytics in MyKinsta, you can gain deeper insight into your site’s traffic, performance, resource usage, and caching behavior through a wide range of analytics data. These reports can also help you investigate and troubleshoot certain site issues directly from the MyKinsta dashboard.

Analytics data is retained for 3 months. After migrating to Kinsta, we recommend checking your Dashboard and Analytics pages regularly to help identify unexpected traffic spikes, performance issues, or unusual activity. If you notice anything concerning or unexplained, our [Support team](https://kinsta.com/docs/support/contact-support/) can help investigate further.

The MyKinsta Dashboard provides a quick overview of:

- Resource usage
- Data transfer (server bandwidth)
- Unique visits to your live site
- CDN usage (when applicable)

For more detailed reports across all sites in your plan, go to **Analytics** from your Dashboard.

To view analytics for a specific site, go to **Sites** > ***sitename*** > **Analytics**.

All analytics charts are displayed in Coordinated Universal Time (UTC).

![Company-level WordPress Analytics in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/08/wordpress-analytics-company.png)

Company-level WordPress Analytics in MyKinsta.

![WordPress site-level Analytics in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/08/wordpress-analytics-site.png)

WordPress site-level Analytics in MyKinsta.

## Date selector

Within **Analytics**, you can select the time frame for the charts. By default, the charts display the current billing period. To change this, click **Current Billing Period**, and then choose from **Billing period**, **Relative**, or **Absolute** options.

### Billing period

This is relative to the current date and your billing period. The **Past two billing periods** and **Current billing period** options display data from your billing period up to today’s date.

![Analytics billing period date selector.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-date-billing.png)

Analytics billing period date selector.

### Relative

The relative options show data for the specified number of days or hours, ending at the current date and time.

![Analytics relative date selector.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-date-relative.png)

Analytics relative date selector.

### Absolute

Use this option to select a custom start and end date. You can choose dates up to three months prior to today.

![Analytics absolute date selector.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-date-absolute.png)

Analytics absolute date selector.

## Download analytics

You can download the data from any of the analytics charts as a `.csv` file by clicking the download button on the corresponding chart.

![Download your analytics data as a .csv file.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-download-analytics.png)

Download your analytics data as a .csv file.

## Plan usage

Under the **Plan usage** section, you’ll find a breakdown of your plan’s resource consumption, including visits, bandwidth, and disk space. These charts reflect billable usage, not necessarily all the traffic your site receives. All other traffic may still reach your site and affect performance, but it is not included in your billing or these charts.

### What counts toward your plan usage (billable)

The following contributes towards your billing:

- A visit is counted when a unique IP address accesses your live site within a 24-hour period. A single visit to your site can result in multiple requests, each contributing to the total bandwidth consumed.
- The request is made to the live environment.
- Requests from the CDN or edge cache are still counted as visits, but they are excluded from server bandwidth.

### What does not count toward your plan usage

The following traffic may still reach your site and consume resources, but it is excluded from billing:

- Requests from most recognized [bot user agents](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/counting-visits/#bots-and-discrepancies-in-analytics) (we automatically filter these).
- Requests to staging environments (premium and standard).
- Requests that return status codes [401](https://kinsta.com/blog/401-error/), [403](https://kinsta.com/blog/403-forbidden-error/), [429](https://kinsta.com/blog/429-too-many-requests/), [451](https://kinsta.com/blog/error-451/), [499](https://kinsta.com/blog/499-error/), or [501](https://kinsta.com/blog/501-not-implemented-error/).
- Requests to wp-login.php.

### Plan usage overview

The plan usage overview shows the totals for all sites in your company’s plan. **Disk usage** information is calculated once every day for each website at various times. This means the amount of disk space used can vary during the day, and the total for all websites might not be entirely accurate until the next day.

![Plan usage chart.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-plan-usage-overview.png)

Plan usage chart.

### Plan usage distribution

The plan usage distribution report is only available within the company’s**Analytics**. It shows you a breakdown of the number of visits, CDN bandwidth, disk space usage, and server bandwidth usage for each WordPress site in your company plan. **Disk Space** refers to the storage capacity currently in use and always displays the most recent data within the specified time frame. You can sort this chart by **Visits**, **CDN bandwidth**, **Disk space**, or **Server bandwidth** in ascending or descending order by clicking on the corresponding header.

Kinsta’s hosting plans are based on either the total number of visitors to your live sites or the total monthly server bandwidth used by your live sites. This table shows how much of your plan each site uses. The disk space usage helps you identify which sites may require further analysis for troubleshooting issues.

![Plan usage distribution.](https://kinsta.com/wp-content/uploads/2025/09/wordpress-analytics-plan-usage-distribution.png)

Plan usage distribution.

### Visits

The **Visits** chart displays the number of visits to your **live WordPress environments** that count toward your **billable usage**. This chart does **not** represent the total traffic your site receives, only the portion included in your plan’s usage calculations. Because each analytics tool defines and filters traffic differently, your visit numbers may not match those reported by Google Analytics or any other service. Google Analytics filters, bot rules, and tracking exclusions do **not** apply to Kinsta’s visit counting. For a full explanation, see [how Kinsta counts visits](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/counting-visits/).

When you hover over a point on the graph, you’ll see:

- The number of billable visits for that day (or hour, depending on the selected timeframe)
- A percentage comparison to the previous data point

![Visits in MyKinsta Analytics.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-visits-4.png)

Visits in MyKinsta Analytics.

### Bandwidth

Kinsta’s bandwidth-based hosting plans are measured by the total monthly server bandwidth your sites use. The bandwidth usage report provides a detailed breakdown of your data usage, including Server bandwidth, CDN bandwidth, and Edge bandwidth. Find out more about [how Kinsta calculates server bandwidth](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/wordpress-calculating-bandwidth/).

![Bandwidth usage.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-bandwidth-5.png)

Bandwidth usage.

We strongly recommend that every customer implement a CDN. Not only because you’ll see an increase in speed, but this can be a great way to decrease server bandwidth and resources on your site. CDN bandwidth is very cheap or even free. Check out our in-depth post on the [benefits of a WordPress CDN](https://kinsta.com/blog/wordpress-cdn/) and why you should use one. Or, if you’re ready, check out how to [enable Kinsta’s CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/) on your site.

### Disk space

The disk space chart shows your storage limit and usage. **Note:** Disk space usage cannot be viewed for the past 24 hours.

![Disk space usage in MyKinsta.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-analytics-disk-space.png)

Disk space usage in MyKinsta.

## Top requests

Under **Top requests**, you can view the most requested resources on your site by bandwidth or views. All charts within **Top requests** include **all**traffic, regardless of whether this is from a real user or a bot.

### Top requests by server bandwidth

The top requests by server bandwidth report shows which requests on your sites consume the most server bandwidth. This is the data delivered directly from your origin server in response to requests to your site. For more information on how server bandwidth is measured, refer to [how Kinsta calculates server bandwidth](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/wordpress-calculating-bandwidth/).

![Top requests by server bandwidth.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-top-requests-server.png)

Top requests by server bandwidth.

### Top requests by total bandwidth

The top requests by total bandwidth report shows which requests on your sites consume the most bandwidth. This total includes bandwidth from the server, [CDN](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/), and [edge cache](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/).  
If your plan is based on **server bandwidth**, it reflects only the data delivered directly from your origin server in response to requests. Any data served from a CDN or edge cache is not counted toward your plan’s bandwidth usage.  
Because this report includes CDN and edge bandwidth, its totals will not match the server bandwidth measured in your plan. Find out more about [how Kinsta calculates server bandwidth](https://kinsta.com/docs/wordpress-hosting/wordpress-analytics-mykinsta/wordpress-calculating-bandwidth/).

![Top requests by total bandwidth.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-analytics-top-bandwidth.png)

Top requests by total bandwidth.

### Top requests by views

The top requests by views report shows you the most requested resources from your site on the server, regardless of size. If your site uses more bandwidth than expected, this report and the ones above can help you troubleshoot and determine where your bandwidth is going. A lot of times, you can easily spot a pattern.

![Top requests by views.](https://kinsta.com/wp-content/uploads/2025/11/wordpress-analytics-top-views.png)

Top requests by views.

## Cache

Under the **Cache** section, you can view a detailed breakdown of how requests are being served, including which cache layer handled each request and which were served directly from the site’s server.

You can also see cache performance metrics such as hits, misses, and bypasses, along with the top requests that are bypassing the cache.

This information helps you identify caching inefficiencies, troubleshoot performance issues, and optimize your caching strategy to improve response times and reduce load on your server.

### Cache breakdown

The Cache breakdown report shows the number of requests handled by each caching layer and which requests were served directly from the server (Non-cached).

The number of non-cached requests is calculated as the total of cache misses and bypasses across all cache layers. Because a single request can pass through multiple cache layers (server, edge, and CDN), the same request may be counted more than once if it misses or bypasses cache at multiple levels.

For this reason, the total non-cached requests may not match the **Server cache component stack** chart, which only includes requests handled at the server cache layer.

![Cache breakdown chart. ](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-cache-breakdown.png)

Cache breakdown chart.

### Server cache component stack

Whenever a file or resource is requested from Kinsta’s servers, it sends a value in the HTTP response header (**X-Kinsta-Cache**) to let you know the status of the cache. There are four types of cache response headers returned:

- **HIT:** A HIT means that the resource is being served from the cache on Kinsta’s servers. Typically, this is what you want to see.
- **BYPASS:** This means that a rule or conflict is probably preventing the resource from caching. We have rules in place so that certain things on your WordPress site aren’t cached. For example, your **/wp-login.php** page isn’t cached, which ensures proper functionality when you log in to your dashboard.
- **MISS:** This means that the content was not yet in the cache but will be after the first request. The second request to that file will be a cache HIT. Remember that each time you purge the cache on your WordPress site, it has to be rebuilt by people visiting it. This is why we recommend not clearing the entire cache constantly. The [Kinsta MU plugin](https://kinsta.com/docs/wordpress-hosting/kinsta-mu-plugin/) automatically purges only certain sections of your site so the rest can remain cached. Read more about [how Kinsta handles caching](https://kinsta.com/blog/wordpress-cache/).
- **EXPIRED:** This means the cached content has expired, and the new content from the hosting server has been fetched.

The Server cache component stack report shows the total number of cache response header values generated from your site.

![Server cache component stack chart.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-cache-stack.png)

Server cache component stack chart.

### Server cache component chart

The Server cache component chart is another way to view your total cache response header values.

![Server cache component chart.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-cache-chart.png)

Server cache component chart.

### Top server cache bypasses

The Top server cache bypasses report shows the top requests that bypass the cache on your site. We recommend you take a look at this and make sure those paths should be bypassing the cache.

![Top server cache bypasses report. ](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-cache-bypasses.png)

Top server cache bypasses report.

## CDN & edge

Under the **CDN & edge** section, if Kinsta’s CDN is enabled, you can view your CDN bandwidth, top files by requests, top files by bytes, and top file extensions by bytes. If a particular media file from your site is hogging all of your bandwidth, you can spot it here.

### CDN bandwidth

The CDN bandwidth usage report shows the **total CDN data your site has used**.

If you highlight a specific point in time on the graph, it will show you some comparison data, such as the percentage difference between each day.

![CDN bandwidth usage.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-cdn-bandwidth-3.png)

CDN bandwidth usage.

### Edge cache bandwidth

This chart shows the total data served by the [edge cache](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/).

If you highlight a specific point in time on the graph, it will show you some comparison data, such as the percentage difference between each day.

![Edge cache bandwidth usage.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-edge-bandwidth.png)

Edge cache bandwidth usage.

### Top files by requests

The top files by requests report shows you the most requested files on your site served by the CDN. This can help you identify which files are responsible for most of your CDN bandwidth usage.

![CDN top files by requests.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-top-files-requests-1.png)

CDN top files by requests.

### Top files by bytes

The top files by bytes report shows you the largest files on your site served by the CDN. This can help you identify large files that you may be able to optimize, reducing the file size and your CDN bandwidth usage.

![CDN top files by bytes.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-top-files-bytes-1.png)

CDN top files by bytes.

### Top file extensions by bytes

The top file extensions by bytes report shows you the top X file extensions served by the CDN. This can help you identify the type of media on your site responsible for most of your CDN bandwidth usage.

![CDN top file extensions by bytes.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-top-file-extensions-bytes-1.png)

CDN top file extensions by bytes.

## Performance

Under the **Performance** section, you can view your average PHP + MySQL response time, PHP throughput, PHP memory limit reached, PHP thread limit, AJAX usage, top average PHP + MySQL response time, and top maximum upstream time.

### Average PHP + MySQL response time

Whenever you visit a WordPress site, PHP and MySQL are used to compile and query the data you see on the page. This chart shows you the average response time of the PHP engine and the [MySQL engine](https://kinsta.com/blog/what-is-mysql/) for every uncached request.

If this value is high or shows a recent spike, feel free to open up a new chat with our Support team so they can check for any server-related issues. If no server-related issues are found, we recommend [using our APM tool to help diagnose performance issues](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/).

![Average PHP + MySQL response time.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-average-php-mysql.png)

Average PHP + MySQL response time.

### PHP throughput

Throughput is the number of transactions per unit of time. In this report, it refers to PHP throughput from your WordPress site. In other words, it shows how many total requests were executed for the selected time frame. The line graph shows a more detailed breakdown by hours or days (depending on the time frame).

![PHP throughput.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-php-throughput-1.png)

PHP throughput.

### PHP memory limit reached

This chart shows the number of times the [PHP memory limit](https://kinsta.com/docs/wordpress-hosting/php/#php-memory-limit) was reached. Kinsta’s default **PHP memory limit is 256MB**, which is more than enough for most WordPress plugins and sites. This limit exists to [prevent PHP scripts from consuming excessive memory](https://kinsta.com/blog/php-memory-limit/#what-should-php-memory-limit-be). If you set the limit too high, a misconfigured or broken script can cause serious issues by using up too much memory. If your site is set up correctly at Kinsta, you shouldn’t reach the PHP memory limit.

You can [change a site’s PHP memory limit per thread](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/#change-php-performance) within **Sites** > ***sitename*** > **Info** > **PHP performance** > **Change**. If you increase the memory per thread, this reduces the number of PHP threads available and, therefore, reduces the number of incoming requests your site can handle simultaneously. However, you can also change your **Total memory pool** to increase both the number of threads and memory available for your site.

![PHP memory limit reached chart.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-php-memory-limit.png)

PHP memory limit reached chart.

### PHP thread limit

The PHP thread limit chart shows how often the PHP engine reached the maximum allocated PHP threads. For example, if your plan includes 4 PHP threads, and your site utilizes all 4 PHP threads simultaneously and cannot immediately respond to incoming PHP requests, that would count as one instance of reaching the PHP thread limit.

This may only give you a partial picture of your PHP thread activity as this only records the number of times the PHP thread limit is reached and not how long all PHP threads were in use.

Each hosting plan at Kinsta includes a default number of [PHP threads](https://kinsta.com/docs/wordpress-hosting/php/#php-threads). You can [change the number of PHP threads](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/#change-php-performance) for each site within **Sites** > ***sitename*** > **Info** > **PHP performance** > **Change**. If you increase the number of threads, this reduces the memory limit per thread; however, you can also change your **Total memory pool** to increase both the number of threads and memory available for your site. The information in this chart can help you gauge whether or not your site is continuously hitting limits.

![PHP thread limit graph.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-php-thread-limit.png)

PHP thread limit graph.

### AJAX usage

AJAX (Asynchronous JavaScript and XML) is a term that describes using a client-side script that lets you update parts of a web page without having to do a postback or page refresh.

When it comes to WordPress, you may have seen **admin-ajax.php** in your speed tests. WordPress uses Ajax for core admin features like auto-saving posts, user session management, and notifications. The Ajax calls for those features are done through the **admin-ajax.php** file in **/wp-admin**.

The most common issues with Ajax in WordPress are plugins causing it to spike and CPU issues on the back end. For more details, check out our in-depth post on [diagnosing high Admin-AJAX usage](https://kinsta.com/blog/admin-ajax-php/) on your WordPress site.

![admin-ajax.php load time in a waterfall chart.](https://kinsta.com/wp-content/uploads/2022/08/high-admin-ajax-usage-1.png)

admin-ajax.php load time in a waterfall chart.

The **AJAX usage** chart shows the count of the admin-ajax requests, and you can see if there are Ajax usage spikes during specific periods. Select one of the bars in the chart, and you can see the number of Ajax requests for that particular time period. You can then utilize some of the tips in the post we mentioned above to narrow down the source of those spikes.

![AJAX usage chart in MyKinsta Analytics.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-ajax-usage-1.png)

AJAX usage chart in MyKinsta Analytics.

### Top average PHP + MySQL response time

This list shows the paths with the top response times from [PHP](https://kinsta.com/docs/wordpress-hosting/wordpress-reference/wordpress-glossary/#php) and [MySQL](https://kinsta.com/docs/wordpress-hosting/wordpress-reference/wordpress-glossary/#mysql). The time is the average per request, not the total time for all requests. These numbers can be one-time peaks, so it’s best to compare this list with the **Top maximum upstream time** list.

![Top average PHP + MySQL response time.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-top-average-php-mysql.png)

Top average PHP + MySQL response time.

### Top maximum upstream time

Upstream time is the total time taken for NGINX (and upstream servers) to process a request and send a response. This list shows the paths with the top PHP and MySQL upstream times (combined) for requests. The time is per request, not the total time for all requests.

![Top maximum upstream time.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-top-max-upstream.png)

Top maximum upstream time.

## Response

Under the **Response** section, you can view your response code breakdown, response stats, 500 error breakdown, 400 error breakdown, redirect breakdown, and top [404 errors](https://kinsta.com/blog/how-to-fix-error-404-not-found/). Check the HTTP status and redirect chain of any URL with our free [HTTP status and redirect checker](https://kinsta.com/tools/redirect-checker/). You can use this tool to review response headers, client-side errors, and test your redirects to ensure they work the way you want them to.

### Response code breakdown

The **Response code breakdown** chart lets you see an overview of the distribution of HTTP status codes served for the requested resources. Response codes, also known as [HTTP status codes](https://kinsta.com/blog/http-status-codes/), are not always bad. For example, a 200 HTTP status code means “Everything is OK.” This code is delivered when a web page or resource acts exactly the way it’s expected to. We’ll go into the others further below.

![Response code breakdown chart.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-response-code-breakdown-1.png)

Response code breakdown chart.

### Response stats

The **Response stats** report shows you the total number of redirects, errors, success rate, and error ratio. Every WordPress site will typically have a slight error rate ratio, which is completely normal.

![Response stats.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-response-stats-1.png)

Response stats.

### 500 error breakdown

The **500 error breakdown** chart shows you the total number of 500 errors that occurred on the server. Here is a more in-depth explanation of what each of these means:

- **500: “There was an error on the server and the request could not be completed.”** A generic code that means there was an “[internal server error](https://kinsta.com/blog/500-internal-server-error/).” Something went wrong on the server, and the requested resource was not delivered.
- **502: “Bad Gateway.”** This error code typically means that one server has received an invalid response from another. Sometimes a query or request will take too long, so it is canceled or killed by the server. Read more about how to fix a [502 bad gateway error](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/server-errors/#502-bad-gateway-error).
- **503: “The server is unavailable to handle this request right now.”** The request cannot be completed right now. This code may be returned by an overloaded server that cannot handle additional requests. We have a step-by-step guide on [how to fix the 503 service unavailable error in WordPress](https://kinsta.com/blog/http-error-503/).

![500 error breakdown graph.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-500-errors.png)

500 error breakdown graph.

### 400 error breakdown

The **400 error breakdown** chart shows you the total number of 400 errors that occurred on the server. Here is a more in-depth explanation of what each of these means:

- **401: “****[Unauthorized](https://kinsta.com/blog/401-error/)****.”** The server returns this error when the target resource lacks valid authentication credentials.
- **403: “Access to that resource is forbidden.”** This code is returned when a user attempts to access something they don’t have permission to access. For example, trying to view [password-protected content](https://kinsta.com/blog/password-protect-wordpress-site/) without logging in might produce a [403 error](https://kinsta.com/blog/403-forbidden-error/).
- **404: “The requested resource was not found.”** The most common error message of them all. This code means that the server can’t find the requested resource, and the [server does not know if it ever existed](https://kinsta.com/blog/how-to-fix-error-404-not-found/).
- **405: “****[Method not allowed](https://kinsta.com/blog/405-method-not-allowed-error/)****.”** This error is generated when the hosting server (origin server) supports the method received, but the target resource doesn’t.
- **429: “****[Too Many Requests](https://kinsta.com/blog/429-too-many-requests/)****.”** The server typically generates this error when the user has sent too many requests in a given amount of time (rate limiting). Often, this is caused by bots or scripts trying to brute-force their way into your default WordPress login page. You can help lock down your site by [changing your WordPress login URL](https://kinsta.com/blog/wordpress-login-url/#change-login-page).
- **499: “Client closed request.”** This error is returned by NGINX when the client closes the request while NGINX is still processing it.

![400 error breakdown graph.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-400-errors.png)

400 error breakdown graph.

### Redirect breakdown

The **Redirect breakdown** chart shows you the total number of redirects that occurred on the server. Remember that like 200 response codes, not all response codes are bad. 300 response codes typically mean you have moved the content elsewhere. 301 redirects, for example, are very important as they will help retain your SEO rankings for URL and site changes. Here is a more in-depth explanation of what each of these means.

- **301: “The requested resource has been moved permanently.”** This code is delivered when a web page or resource has been permanently replaced with a different resource. It is used for [permanent URL redirection](https://kinsta.com/docs/wordpress-hosting/redirect-rules/).
- **302: “The requested resource has moved but was found.”** This code indicates that the requested resource has been temporarily moved to a different location.
- **304: “The requested resource has not been modified since the last time you accessed it.”** This code tells the browser that resources stored in the browser cache haven’t changed. It [speeds up web page delivery](https://kinsta.com/blog/http-304/) by reusing previously downloaded resources.

![Redirect breakdown graph.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-redirect-breakdown.png)

Redirect breakdown graph.

### Top 404 errors

The **Top 404 errors** list helps you troubleshoot the most requested resources that visitors or [automated bots](https://kinsta.com/blog/wordpress-robots-txt/) are hitting that do not exist on your site.

![Top 404 errors.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-top-404-1.png)

Top 404 errors.

If you see a large number of 404 errors, it’s generally recommended that you go through your site and fix them for SEO and usability purposes. You can also look them up in [Google Search Console](https://kinsta.com/blog/google-search-console/) under crawl errors.

## Audience

In the **Audience** section, you can view the top countries, browsers, cities, user agents, referrers, ASNs, and IP addresses visiting your site. You can also see the Desktop vs. tablet vs. mobile dispersion. This helps you understand where your traffic comes from, identify visitor trends, and spot potentially suspicious or unwanted activity.

### Top countries

The **Top countries** list can help you determine if the data center your site is in is the best location. This list is a geo-analysis by country of visitors’ IP addresses. In the example below, the site should probably be placed on a server in the United States since most of the traffic is from there.

Kinsta now has 30 [data center locations](https://kinsta.com/docs/service-information/data-center-locations/) around the globe where you can host your WordPress site. For more details, check out our in-depth post about [network latency](https://kinsta.com/blog/network-latency/) and why it’s important to place your site strategically.

![Top countries list.](https://kinsta.com/wp-content/uploads/2026/07/wordpress-analytics-top-countries.png)

Top countries list.

### Top browsers

The **Top browsers** list shows which web browsers your visitors use most often to access your site. This can help you prioritise browser compatibility testing and ensure your site provides a consistent experience for the browsers your audience uses most.

![Top browsers list.](https://kinsta.com/wp-content/uploads/2026/07/wordpress-analytics-top-browsers.png)

Top browsers list.

### Top cities

The **Top cities** list shows you the geo analysis by city of visitors’ IP addresses.

![Top cities list.](https://kinsta.com/wp-content/uploads/2026/07/wordpress-analytics-top-cities.png)

Top cities list.

### Top user agents

The **Top user agents** list shows the browsers, operating systems, devices, and bots used to access your site. This can help you understand how visitors access your site, identify search engine crawlers and AI bots, and troubleshoot browser or device compatibility issues.

![Top user agents list.](https://kinsta.com/wp-content/uploads/2026/07/wordpress-analytics-top-agents.png)

Top user agents list.

### Top referrers

The **Top referrers** list shows the websites that directed visitors to your site. This can help you identify your main traffic sources, measure the effectiveness of marketing campaigns, and understand which external websites are driving the most visitors.

![Top referrers list.](https://kinsta.com/wp-content/uploads/2026/07/wordpress-analytics-top-referrers.png)

Top referrers list.

### Top ASN

An ASN (Automated System Number) identifies the network or organisation responsible for a range of IP addresses on the internet. The **Top ASN** list shows the networks or organisations your visitors are connecting from, such as internet service providers (ISPs), cloud providers, or hosting companies. This can help you identify traffic sources, distinguish legitimate visitors from bots or crawlers, and investigate unusual or suspicious traffic patterns.

![Top ASN list.](https://kinsta.com/wp-content/uploads/2026/07/wordpress-analytics-top-asn.png)

Top ASN list.

### Top client IPs

The **Top client IPs** list shows the IP addresses generating the most requests to your site. This can help you identify unusual traffic patterns, investigate sudden spikes in bandwidth usage, and detect potential malicious activity, such as brute force or DDoS attacks. Kinsta’s [Bot protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) automatically blocks malicious traffic, including DDoS and brute force attacks. If you identify suspicious IP addresses, [contact our Support Team](https://kinsta.com/docs/support/contact-support/), who can investigate further and block them if necessary.

![Top client IPs.](https://kinsta.com/wp-content/uploads/2026/07/wordpress-analytics-top-ips.png)

Top client IPs.

### Desktop vs. tablet vs. mobile

The desktop vs. tablet vs. mobile chart shows which devices users are using to access your site. In the example below, you can see that it’s primarily desktop traffic at 89%.

![Desktop vs. tablet vs. mobile dispersion chart.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-analytics-dispersion-1.png)

Desktop vs. tablet vs. mobile dispersion chart.

## Bot traffic

With [Kinsta’s bot protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/), you can control how different traffic types are blocked or challenged on your site. The Bot traffic section gives you a breakdown of human vs automated traffic and whether the traffic was allowed or not.

### Requests

This chart shows all requests made to your site in the past 24 hours and how Kinsta classified each one. It includes:

- **Likely humans:**  Traffic from real visitors who show normal browsing behavior and are most likely human.
- **Verified bots:** Automated traffic from legitimate, verified companies, such as Google, Bing, monitoring, and SEO tools.
- **Likely bots:** Traffic from unverified automation that is most likely generated by bots.
- **AI crawlers:** Traffic from bots that scan and collect website content to train, analyze, or power AI models.
- **Excessive-rate AI crawlers:** Traffic from AI crawlers making requests at a rate that overloads server resources.
- **Unclassified traffic:** Typically harmless traffic, usually internal service requests (such as error page requests) that don’t impact your origin server.
- **Automated traffic:** Requests confirmed to be generated by software rather than human users. This can include legitimate tools that aren’t classified as verified bots, such as WordPress management tools, custom API integrations, uptime monitors, or deployment scripts.
- **Malicious traffic:** Attack, DDoS, and abuse traffic.
- **Custom rules:** Requests that matched any [Kinsta-managed custom rules](#kinsta-bot-protection-and-custom-waf-rules) configured on your site.
- **WP automations:** Automated requests from common WordPress features, integrations, and background tasks. These can be allowed or blocked within [Allow typical WordPress automations](#allow-typical-wordpress-automations).

For more information about each traffic type, refer to [How traffic is classified in MyKinsta](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#how-traffic-is-classified-in-mykinsta).

Use the dropdown to select which traffic type to show on the chart.

![Requests chart.](https://kinsta.com/wp-content/uploads/2026/07/wordpress-analytics-bot-requests-1.png)

Requests chart.

### Bot protection results

The Bot protection results chart shows you the number of requests that have been allowed, challenged, or blocked through [Kinsta’s bot protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/).

- **Allowed:** Requests that were allowed to access your site.
- **Challenged:** Requests that were [challenged](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#what-is-a-challenge) and failed the verification, resulting in the request being blocked.
- **Blocked:** Requests that were blocked immediately based on your configured bot protection levels.

![Bot protection results chart.](https://kinsta.com/wp-content/uploads/2026/07/wordpress-analytics-bot-protection-results.png)

Bot protection results chart.

This chart is also available on your site’s **Info** page.

![Bot protection chart on the site Info page.](https://kinsta.com/wp-content/uploads/2026/07/wordpress-site-bot-protection.png)

Bot protection chart on the site Info page.

### Top traffic

This report shows the top paths, user agents, countries, and IPs for the last 24 hours. Use the dropdown to select a traffic type, such as malicious traffic, automated traffic, or AI crawlers, and the report will update to show the top paths, user agents, countries, and IPs for that traffic type.

For more information about each traffic type, refer to [How traffic is classified in MyKinsta](#how-traffic-is-classified-in-mykinsta).

![Top traffic report. ](https://kinsta.com/wp-content/uploads/2026/07/wordpress-bot-protection-top-traffic.png)

Top traffic report.

### Spikes in bot traffic charts

If your site experiences a large DDoS attack, Kinsta blocks well over 99% of the malicious traffic. A small fraction of requests can still reach the origin, since they closely resemble normal visitor traffic and are extremely difficult to identify as malicious. Even this small fraction can be 100 to 3,000 times, or more, your usual traffic volume during a large attack. With Bot protection enabled, this traffic is still evaluated against the bot protection rules and blocked.

Because of this, your bot traffic chart may show a huge spike on the day of the attack, with the other days appearing empty by comparison. This doesn’t mean there was no traffic on those days; the attack volume is simply so much larger that normal traffic becomes too small to register visibly on the same scale.

For example:

![Bot traffic analytics after a DDoS attack.](https://kinsta.com/wp-content/uploads/2026/03/wordpress-bot-protection-spikes.png)

Bot traffic analytics after a DDoS attack.
