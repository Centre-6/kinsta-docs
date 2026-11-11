---
url: "https://kinsta.com/blog/monitor-wordpress-ai-workloads/"
title: "Monitor WordPress AI workloads with Kinsta APM and MyKinsta server logs"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: []
kinsta_last_updated: "2026-10-08T19:34:34"
change_signal: "2026-10-08T19:34:34"
fetched_at: "2026-11-11T13:03:02Z"
sha256: "495c77c69cf453e3c36821f499503cb1940a384aba08bdccc37610e05bb8cde7"
body_chars: 26779
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Monitor WordPress AI workloads with Kinsta APM and MyKinsta server logs

**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/monitor-wordpress-ai-workloads/
**Kinsta last updated:** 2026-10-08T19:34:34

## On this page

- [How to monitor AI workloads in WordPress](#how-to-monitor-ai-workloads-in-wordpress)
- [AI image generation in WordPress](#ai-image-generation-in-wordpress)
  - [Step 1: Configure a connector in the Connectors screen](#step-1-configure-a-connector-in-the-connectors-screen)
  - [Step 2: Install and activate the official WordPress.org AI plugin](#step-2-install-and-activate-the-official-wordpressorg-ai-plugin)
  - [Step 3: Enable Kinsta APM and monitor the access logs in MyKinsta](#step-3-enable-kinsta-apm-and-monitor-the-access-logs-in-mykinsta)
  - [Step 4: Create a new post and generate a new featured image using AI](#step-4-create-a-new-post-and-generate-a-new-featured-image-using-ai)
- [Measuring the resource consumption of AI image generation](#measuring-the-resource-consumption-of-ai-image-generation)
  - [Kinsta APM breakdown](#kinsta-apm-breakdown)
    - [Step 1: Initializing the request](#step-1-initializing-the-request)
    - [Step 2: Triggering the Ability](#step-2-triggering-the-ability)
    - [Step 3: Routing to the client](#step-3-routing-to-the-client)
    - [Step 4: Building the prompt](#step-4-building-the-prompt)
    - [Step 5: Handing off to the HTTP transport layer](#step-5-handing-off-to-the-http-transport-layer)
    - [Step 6: Opening an HTTP connection](#step-6-opening-an-http-connection)
    - [The takeaway](#the-takeaway)
  - [Server log breakdown](#server-log-breakdown)
    - [1. Prompt Generation](#1-prompt-generation)
    - [2. Image Generation](#2-image-generation)
    - [3. Alt text generation](#3-alt-text-generation)
    - [4. Media integration](#4-media-integration)
    - [5. Download image](#5-download-image)
    - [What access logs tell you](#what-access-logs-tell-you)
  - [Client-side HTTP requests breakdown](#client-side-http-requests-breakdown)
    - [1. Prompt generation](#1-prompt-generation)
    - [2. Image generation](#2-image-generation)
    - [3. Alt text generation](#3-alt-text-generation)
    - [4. Image download](#4-image-download)
- [The impact of AI on site infrastructure](#the-impact-of-ai-on-site-infrastructure)

---

With the introduction of the [Abilities API](https://kinsta.com/blog/wordpress-abilities-api/) and the [AI Client](https://kinsta.com/blog/wordpress-ai/), WordPress has evolved into a true execution engine, bridging your applications with the AI models of your choice.

This monumental shift changes what the CMS is at its core. However, it also adds a layer of complexity to the overall ecosystem, making process observability and performance monitoring increasingly vital to managing a modern website.

Today, we’re not just here to tell you how important it is to monitor your site’s behavior as machines become more present (or intrusive) in your access logs. Instead, we want to give you clear, concrete proof of how these new AI features directly impact your site’s resources.

To do this, we’ll leverage two MyKinsta tools: Kinsta APM—our application performance monitoring tool—and server access logs. Both features are available to all Kinsta clients at no extra cost.

Curious to see how much AI is actually impacting your WordPress site? Let’s dive in!

## How to monitor AI workloads in WordPress

Your site interacts with AI in several ways. These range from [AI bot and crawler scans](https://kinsta.com/blog/ai-crawlers-wordpress/) to operations performed internally by plugins via the AI Client, to requests made by external applications and AI agents querying your site through the Abilities API.

Consider the time required to generate an image or transcribe an audio file. These AI operations often take several seconds to complete. During this time, a [PHP worker/thread](https://kinsta.com/changelog/workers-now-threads/) is unavailable for other operations, whether triggered by a human user or a machine.

While this might not be an issue for every site, it becomes a [critical factor to monitor](https://kinsta.com/ai-crawler-traffic/) carefully for high-traffic business sites and e-commerce stores with hundreds or thousands of products.

An [Application Performance Monitoring](https://kinsta.com/blog/application-performance-monitoring/) (APM) tool helps you accurately measure the [impact of AI](https://kinsta.com/blog/wordpress-ai-infrastructure/) on your WordPress site.

You could use a tool like [New Relic](https://kinsta.com/blog/wordpress-performance-new-relic/) to keep track of WordPress transactions, [hooks](https://kinsta.com/blog/wordpress-hooks/), plugins, themes, database queries, external requests, and everything that helps you pinpoint performance issues.

Kinsta users have access to a free [Application Performance Monitoring tool](https://kinsta.com/blog/apm-tools/) directly available inside the MyKinsta dashboard.

![A screenshot sowing the landing page of the APM took in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/02/unlocking-productivity-enable-apm-tool.png)

Enabling the Kinsta APM tool in MyKinsta.

To enable Kinsta APM, navigate to **Sites** > **sitename** > **APM** and click **Enable**. Select your desired interval and let the tool record your site’s activity.

When the monitoring is complete, you’ll receive an automated email with a link to the results page, where you can dive into [detailed charts](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/) covering transactions, plugins, themes, hooks, slow database queries, and external requests.

![Slowest external requests tab in Kinsta APM](https://kinsta.com/wp-content/uploads/2026/09/kinsta-apm-slowest-external-requests.png)

Slowest external requests tab in Kinsta APM

Access and error logs are another goldmine of insights into what is happening under the hood. Typically, you can access server logs through your hosting control panel or within your server’s file system via FTP or SSH.

These logs provide comprehensive data to troubleshoot errors, identify performance bottlenecks, and pinpoint your primary traffic sources.

Kinsta users can [download log files](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/) directly from the server via [SFTP](https://kinsta.com/blog/sftp-ssh-features/) or [SSH](https://kinsta.com/blog/how-to-use-ssh/), or through the [MyKinsta File manager](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-file-manager/). You can also inspect error, cache, and access logs directly using the MyKinsta **Log viewer**.

![access.log file in the MyKinsta Log viewer.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-logs-access-3.png)

access.log file in MyKinsta Log viewer.

In the following sections, we’ll analyze an AI operation to help you understand how to measure the impact of AI usage on your website and why it requires robust infrastructure and proper monitoring.

Let’s look at a real-world example by asking an AI model to generate a featured image for a blog post.

## AI image generation in WordPress

For our tests, we asked AI to generate a featured image for a WordPress blog post using the official WordPress.org AI plugin. To run the same tests, follow these steps:

1. [Configure a connector in the Connectors screen of the WordPress admin](#configure-connector)
2. [Install and activate the official WordPress.org AI plugin](#install-ai)
3. [Enable Kinsta APM and monitor the access logs in MyKinsta](#enable-kinsta-apm)
4. [Create a new post and generate a new featured image using the AI feature](#create-new-post)

Let’s get started.

### Step 1: Configure a connector in the Connectors screen

To get started, you’ll need an API key from your AI provider. We won’t be covering that step here, but you can check your provider’s documentation for details.

Once you have your API key, open your site admin and navigate to **Settings** > **Connectors**. Click on the **Activate** button for your AI provider and [enter your API key](https://kinsta.com/blog/wordpress-ai/#ai-connector).

![Connectors screen](https://kinsta.com/wp-content/uploads/2026/06/connectors-screen.png)

The centralized AI Connectors interface in the WordPress admin dashboard.

### Step 2: Install and activate the official WordPress.org AI plugin

Out of the box, WordPress provides the APIs and abstractions. To equip your site with an AI image generation feature, you’ll need to install a plugin that leverages the AI core infrastructure, such as the [official AI plugin](https://wordpress.org/plugins/ai/) provided by WordPress.org.

This plugin adds several abilities that you can inspect in the **Abilities Explorer** screen, under **Tools** > **Abilities Explorer**.

![The Abilities Explorer screen.](https://kinsta.com/wp-content/uploads/2026/09/abilities-explorer.png)

The Abilities Explorer screen generated by the WordPress.org AI plugin.

Among the registered abilities, notice **Image Generation and Editing**. This ability allows you to generate a featured image based on a post’s content or a custom prompt when invoked from the Media Library.

### Step 3: Enable Kinsta APM and monitor the access logs in MyKinsta

In MyKinsta, navigate to **Sites** > **sitename** > **APM** and enable Kinsta APM. Set a monitoring duration of 2 hours, then click **Enable monitoring time**.

![Enable Kinsta APM monitoring time.](https://kinsta.com/wp-content/uploads/2026/09/enable-monitoring-time.png)

Enable Kinsta APM monitoring time.

While the APM tool tracks performance behind the scenes, navigate to **Sites** > **sitename** > **Logs** and select the **access.log** tab. You can leave the default settings.

### Step 4: Create a new post and generate a new featured image using AI

Now, back in your WordPress admin dashboard, create a new post, enter a title and some content, and then click the **Generate featured image** button on the right.

![Generate featured image in the block editor.](https://kinsta.com/wp-content/uploads/2026/09/generate-featured-image.png)

Generate featured image in the block editor.

After a few moments, an AI-generated featured image shows up in the post settings sidebar.

![The AI-generated featured image.](https://kinsta.com/wp-content/uploads/2026/09/featured-image-generated.png)

The AI-generated featured image.

The operation we want to monitor is now complete. We can move on to breaking down the data.

## Measuring the resource consumption of AI image generation

Now let’s measure the impact of an image generation request from the WordPress Abilities API. The results of this test are not fixed, as they largely depend on the provider’s API processing and response times and the specific operations the plugin performs when sending the request.

Our goal here is to provide a framework and methodology that you can easily replicate in your own staging environments to measure AI operation resource consumption and execution times.

The analysis we propose looks at both sides of the coin. On the server side, we’ll analyze transactions using [Kinsta APM](https://kinsta.com/apm-tool/) and monitor HTTP requests through the [MyKinsta Log viewer](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/). On the client side, we’ll monitor what happens under the hood using browser developer tools.

Let’s get started!

### Kinsta APM breakdown

Once you have the AI-generated featured image for your post, wait a few minutes, then go back to the Kinsta APM page in MyKinsta and start exploring each tab.

The **Transactions** tab displays an **Overall transaction time** chart and a **Slowest transactions** table, where a transaction represents a backend activity that occurs to serve a request to your WordPress site (see [docs](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/#transaction)).

The image below shows overall transaction time during a two-minute window in which PHP execution took about 27 seconds, MySQL took 271 ms, and external transactions accounted for over 19 seconds.

![Overall transaction time in Kinsta APM.](https://kinsta.com/wp-content/uploads/2026/09/overall-transaction-time.png)

Overall transaction time in Kinsta APM.

The table below lists the **Slowest transactions**. As you can see, requests targeting the `/wp-json` endpoint consumed the most transaction time.

![Slowest transactions in Kinsta APM.](https://kinsta.com/wp-content/uploads/2026/09/slowest-transactions-wp-json.png)

Slowest transactions in Kinsta APM.

The **WordPress** tab provides the **Slowest WordPress plugins** and **Slowest WordPress hooks** tables. As expected, the slowest plugins were **ai-provider-for-google** and **ai**, which together accounted for nearly 90% of the total duration.

![Slowest WordPress plugins.](https://kinsta.com/wp-content/uploads/2026/09/slowest-wordpress-plugins.png)

Slowest WordPress plugins.

The **External** tab displays the Slowest external requests, sorted by **Total duration**.

![Slowest external requests in Kinsta APM.](https://kinsta.com/wp-content/uploads/2026/09/slowest-external-requests-1.png)

Slowest external requests in Kinsta APM.

Let’s break down this data:

- **Total Duration (%):** This is the percentage of time consumed by all requests to a transaction endpoint within the selected time frame. Note that this value is the sum of the duration of all requests to an endpoint, not of an individual transaction sample. In our example, POST requests to the `generativelanguage.googleapis.com` endpoint accounted for 95.51% of all external transactions, with GET requests to the same endpoint taking up 3.94%.
- **Total Duration:** This is the absolute amount of time a transaction endpoint consumes within the selected time frame. Again, this value represents the sum of the duration of all requests to a particular endpoint. In our example, `generativelanguage.googleapis.com` POST requests had a cumulative duration of over 18 seconds.
- **Max Duration:** The slowest transaction sample duration from the selected time frame.
- **Avg. Duration:** The average of all transaction sample durations from the selected time frame.
- **Rate Per Min:** The average number of times a transaction executed per minute.

When you click on a specific request, a **Transaction samples** modal shows up and displays the samples where the selected POST request ran.

![Transaction samples in Kinsta APM.](https://kinsta.com/wp-content/uploads/2026/09/transaction-samples.png)

Transaction samples in Kinsta APM.

Click on the slowest transaction sample to view the **Transaction trace timeline** table. Here, you can see a step-through presentation of spans (PHP processes, MySQL database queries, and external calls) for a specific transaction sample (see [docs](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/#transaction-trace-timeline)).

![Transaction trace timeline.](https://kinsta.com/wp-content/uploads/2026/09/transaction-trace-timeline.png)

Transaction trace timeline.

If you click on a span in the transaction trace timeline, you will see a detailed overview and a complete stack trace.

The stack trace details the exact PHP code executed, down to the specific file and line number (see [docs](https://kinsta.com/docs/wordpress-hosting/wordpress-monitoring/apm-tool/#stack-trace)).

The following image shows the full stack trace for the transaction that handled the image generation:

![Span details in Transaction trace timeline.](https://kinsta.com/wp-content/uploads/2026/09/span-details.png)

Span details in Transaction trace timeline.

Here is a breakdown:

#### Step 1: Initializing the request

WordPress receives the HTTP request, boots the core system via **wp-blog-header.php**, and dispatches it through the REST API controller (`WP_REST_Server`) to handle the incoming request synchronously.

![Initializing the HTTP request.](https://kinsta.com/wp-content/uploads/2026/09/stack-trace-1-initialization.png)

Initializing the HTTP request.

#### Step 2: Triggering the Ability

**Generate_Image.php** invokes the `generate_image` ability within the `WordPress\AI\Abilities\Image` namespace to generate the post image.

![Triggering the generate_image Ability.](https://kinsta.com/wp-content/uploads/2026/09/stack-trace-2-trigger.png)

Triggering the generate_image Ability.

#### Step 3: Routing to the client

**class-wp-ability.php** executes the callback, delegating execution to the `WP_AI_Client` module.

![Routing the execution to the AI Client.](https://kinsta.com/wp-content/uploads/2026/09/stack-trace-3-routing.png)

Routing the execution to the AI Client.

#### Step 4: Building the prompt

**PromptBuilder.php** builds the prompt, and **GoogleTextGenerationModel.php** converts the instructions into a request format compatible with Gemini APIs.

![Building the prompt.](https://kinsta.com/wp-content/uploads/2026/09/stack-trace-4-prompt-translation.png)

Building the prompt.

#### Step 5: Handing off to the HTTP transport layer

**HttpTransporter.php** hands off execution to the [WordPress HTTP API](https://kinsta.com/blog/wordpress-http-api/) (`http.php -> WP_Http->request`).

![Handing off to the HTTP transport layer.](https://kinsta.com/wp-content/uploads/2026/09/stack-trace-5-transport-layer.png)

Handing off to the HTTP transport layer.

#### Step 6: Opening an HTTP connection

`WP_Http` opens a synchronous connection, holding the PHP worker until Google returns a response (see [official docs](https://developer.wordpress.org/reference/classes/wp_http/request/)).

![Opening a synchronous connection.](https://kinsta.com/wp-content/uploads/2026/09/stack-trace-6-http-connection.png)

Opening a synchronous connection.

#### The takeaway

The key takeaway here is that the image generation task we measured **is a synchronous, blocking operation.**

The call passes from `WP_REST_Server` to `WP_Http->request` within the same HTTP request lifecycle. As a result, the PHP thread waits while it generates and returns the image.

In this example, the PHP thread handling the request remained occupied for +8 seconds. Additional available threads could still serve other requests. Still, concurrent AI operations can exhaust the PHP memory pool and increase queuing, latency, and timeout risk (see how Kinsta helps you [manage PHP threads and memory usage](https://kinsta.com/changelog/php-performance/)).

### Server log breakdown

While a stack trace records the exact sequence of PHP functions, methods, files, and lines of code traversed by the server to process a specific request, access logs record HTTP requests at the web server level.

An access log shows who made the request (IP address and User Agent), what was requested (URL or API endpoint), the response status code, and the request’s total execution time.

In short, log analysis gives you a complete, unfiltered view of what is happening on your server during an AI operation, such as generating the featured image in our example.

To generate that single image, WordPress executed four sequential calls to the Abilities API.

Here are the logs tracking the interaction with the Google API:

#### 1. Prompt Generation

```
POST "/wp-json/wp-abilities/v1/abilities/ai/image-prompt-generation/run?_locale=user" HTTP/2.0 200
PHP execution time: 5.432s
```

![The prompt generation log in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/09/prompt-generation-log.png)

The prompt generation log in MyKinsta

- **What this log tells you:** The plugin uses the `image-prompt-generation` ability to send the post content to Gemini to generate a descriptive image prompt (e.g., “A person shaking hands with a sleek futuristic robot…”).
- **Latency:** 5.43 seconds spent communicating with the Google API.

#### 2. Image Generation

```
POST "/wp-json/wp-abilities/v1/abilities/ai/image-generation/run?_locale=user" HTTP/2.0 200
PHP execution time: 9.795s
```

![The image generation log in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/09/image-generation-log.png)

The image generation log in MyKinsta.

- **What this log tells you:** This log entry corresponds directly to the transaction sample and stack trace we analyzed in the Kinsta APM section. The plugin sends the generated prompt to Google’s image generation model (Imagen) via the `image-generation` ability.
- **PHP execution time:** 9.79 seconds spent waiting for the image’s binary/base64 payload.

#### 3. Alt text generation

```
POST "/wp-json/wp-abilities/v1/abilities/ai/alt-text-generation/run?_locale=user" HTTP/2.0 200
PHP execution time: 11.305s
```

![The alt text generation log.](https://kinsta.com/wp-content/uploads/2026/09/alt-text-generation-log-1.png)

The alt text generation log.

- **What this log tells you:** Immediately after the image is created, the system triggers another automatic call to the Abilities API to generate the alt text. The ability then invokes Gemini to analyze and describe the newly generated image.
- **PHP execution time:** 11.30 seconds total.

The image has been generated. The next step is registering it in the WordPress Media Library.

#### 4. Media integration

```
POST "/wp-json/wp-abilities/v1/abilities/ai/image-import/run?_locale=user" HTTP/2.0 200
PHP execution time: 0.839
```

![The image import log in MyKinsta.](https://kinsta.com/wp-content/uploads/2026/09/image-import-log.png)

The image import log in MyKinsta.

- **What this log tells you:** WordPress downloads the file payload from the external API via the `image-import` ability and registers it in the Media Library.
- **PHP execution time:** 0.839 seconds.

#### 5. Download image

```
GET "/wp-content/uploads/2026/09/a-person-shaking-hands-with-a-sleek-futuristic-robot-inside-a-glass-dome-1024x559.jpg" HTTP/2.0 200
PHP execution time: 0.000
```

![Image download log.](https://kinsta.com/wp-content/uploads/2026/09/image-download-log.png)

The image download log.

- **What this log tells you:** The block editor fetches the imported image file directly from the `uploads` directory to render it in the UI. This is a static asset served directly by the web server, and no PHP processing is required.
- **PHP execution time:** 0.000 seconds.

#### What access logs tell you

If you sum up the execution times across the entire workflow for a single image generation, you get the overall execution time for the complete operation—including prompt generation, image generation, alt text generation, and image import into WordPress.

In our example, the logs provided the following execution times:

- image-prompt-generation: **5.43s**
- image-generation: **9.79s**
- alt-text-generation: **11.30s**
- image-import: **0.84s**

Total: **~27.36** cumulative seconds of PHP thread processing time!

This confirms our initial assumption: on a traditional hosting setup with limited resources, if two or three AI-based tasks run simultaneously, the server will quickly experience PHP thread saturation and stop responding to other site visitors for several seconds.

![PHP thread limit diagram in MyKinsta Analytics.](https://kinsta.com/wp-content/uploads/2026/09/mykinsta-analytics-php-thread-limit.png)

MyKinsta Analytics shows how many times the site reached its allocated PHP thread limit.

If your site implements multiple AI features, your hosting infrastructure becomes even more critical. Additionally, monitoring tools like **Kinsta APM** and **MyKinsta access logs** are great tools for measuring the impact of AI workloads, pinpointing performance bottlenecks, and adopting the right optimizations.

### Client-side HTTP requests breakdown

While Kinsta APM and server access logs help you understand AI’s impact on your site’s infrastructure, browser developer tools let you analyze the workflow from the client’s perspective.

To analyze network calls, you’ll follow these steps:

1. Open your WordPress admin and create a new post.
2. Open your preferred browser’s Developer Tools by pressing F12 (or **Right-Click > Inspect** / **Cmd + Option + I** on Mac).
3. Select the **Network** tab and filter by **Fetch/XHR** to display only asynchronous/REST API calls.
4. When you are ready, click on the **Generate featured image** button in the block editor.

Requests to the Abilities API endpoints start flowing in the **Network** panel. In Firefox Developer Tools, they will be flagged with a turtle icon, indicating slow requests.

Click on each of these requests, one by one, and observe the **Request**, **Response**, and **Timings** tabs for each request.

#### 1. Prompt generation

The first call to the Google AI API generates the prompt. For this operation, the request payload includes the post title and content.

![Prompt generation request payload.](https://kinsta.com/wp-content/uploads/2026/09/firefox-devtools-request-1.png)

The payload of this prompt generation request is the post content.

The response is the prompt sent to the Imagen model.

![The Google API response.](https://kinsta.com/wp-content/uploads/2026/09/firefox-devtools-response-1.png)

The Google API response.

Next, switch to the **Timings** tab to check execution times. The prompt generation for this latest image took **5.52** seconds.

![Prompt generation timings.](https://kinsta.com/wp-content/uploads/2026/09/firefox-devtools-timings-1.png)

Prompt generation resulted in a wait time of 5.52s.

#### 2. Image generation

Then follows the image generation request. The request payload is the prompt received with the previous request.

![Image generation request.](https://kinsta.com/wp-content/uploads/2026/09/firefox-devtools-request-2.png)

The payload for the image generation request is the received prompt.

The Google API response will be the base64 payload of the image.

![Image generation response.](https://kinsta.com/wp-content/uploads/2026/09/firefox-devtools-response-2.png)

The Google AI response is the base64 payload of the image.

The **Timings** tab provides the total execution time for the image generation. The request waited **9.92** seconds.

![Image generation timings.](https://kinsta.com/wp-content/uploads/2026/09/firefox-devtools-timings-2.png)

Image generation registered a wait time of nearly 10 seconds.

#### 3. Alt text generation

With the third call, the Abilities API requests the Google API to generate the image’s alt text. The request includes the base64 image payload.

![Alt text request.](https://kinsta.com/wp-content/uploads/2026/09/firefox-devtools-request-3.png)

The Abilities API sends a request to generate the image’s alt text.

The API response contains the image’s alt text.

![Alt text generation response.](https://kinsta.com/wp-content/uploads/2026/09/firefox-devtools-response-3.png)

The response from the Google API is the image’s alt text.

Despite the concise output, decoding the image and generating the text was particularly slow: **7.32s**.

![Alt text generation wait time.](https://kinsta.com/wp-content/uploads/2026/09/firefox-devtools-timings-3.png)

Alt text generation wait time.

#### 4. Image download

The fourth Abilities API request processes the binary payload, downloads the image file, generates image crops, and registers the image in the WordPress Media Library. The wait time for this final request was **1.79s**.

![Image download wait time.](https://kinsta.com/wp-content/uploads/2026/09/firefox-devtools-timings-4.png)

Wait time for the image download.

Let’s now sum up the wait times for the four requests executed by the Abilities API to generate the featured image:

- Prompt generation: **5.52s**
- Image generation: **9.92s**
- Alt text generation: **7.32s**
- Image download and registration: **1.79s**

The total wait time was a whopping **24.55** seconds.

## The impact of AI on site infrastructure

Whether you use third-party plugins or custom code to add AI features to your site, understanding their impact on server performance and resource consumption is critical.

Inefficient resource management or poor code architecture can quickly overload your server, leading to PHP resource saturation, server timeouts, excessive bandwidth usage, HTTP 5xx errors, or outright downtime.

A high-performance cloud host built on containerized infrastructure, multi-level caching, automatic database optimization, and scalable PHP workers can’t magically eliminate AI’s processing load. However, it gives your site the buffer it needs to prevent bottlenecks and resolve performance spikes before they impact your visitors.

Nobody wants a sluggish site during peak traffic events like Black Friday, and businesses can’t afford server timeouts when uptime directly impacts revenue. As machines play a bigger role in driving website functionality, choosing a performant, scalable hosting provider is no longer optional.

Kinsta delivers the performance, security, and observability modern WordPress sites need to thrive in the AI era. Want to see the difference firsthand? Check out our plans [here](https://kinsta.com/pricing/).
