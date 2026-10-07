---
url: "https://kinsta.com/docs/wordpress-hosting/php/"
title: "WordPress Hosting - PHP"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "php"
section: []
kinsta_last_updated: "September 18, 2026"
sitemap_lastmod: "2026-09-18T09:54:48+00:00"
fetched_at: "2026-10-07T22:44:22Z"
sha256: "a1bd2463a6bda36882ee573fbfa80087743b7ffe3e376b979324ca834e779596"
body_chars: 10323
extracted_with: "main article"
status: "live"
---

# WordPress Hosting - PHP

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/php/
**Kinsta last updated:** September 18, 2026

## On this page

- [How PHP is processed](#how-php-is-processed)
- [PHP threads](#php-threads)
  - [Kinsta plans and PHP threads](#kinsta-plans-and-php-threads)
- [PHP memory limit](#php-memory-limit)
  - [Kinsta plans and PHP memory](#kinsta-plans-and-php-memory)
- [Interaction between PHP threads and memory](#interaction-between-php-threads-and-memory)
- [Interaction between PHP threads, CPU, and RAM](#interaction-between-php-threads-cpu-and-ram)
- [Default PHP values](#default-php-values)
- [Disabled PHP functions](#disabled-php-functions)

---

PHP (Hypertext Preprocessor) is an open-source scripting language that is especially suited for web development. It runs on the server side, meaning it processes code on the web server before sending it to the client (browser). WordPress is built on PHP; therefore, it’s essential for WordPress sites. PHP enables your WordPress site to:

- Generate dynamic content and display it on a website in real time.
- Interact with your database, allowing it to fetch and store data.
- Handle forms and process user input, making WordPress sites more interactive.
- Use themes and plugins to extend WordPress’s core capabilities.
- Improve performance by ensuring much of the heavy lifting happens on the web server before the content reaches the user’s browser.

## How PHP is processed

When a visitor visits an uncached page or performs an action on a page (e.g., adding something to a cart, submitting a form, etc.), the following process occurs:

1. The web server receives that request.
2. The web server passes the request to PHP, which is assigned to an available [PHP thread](#php-threads).
3. The PHP thread executes the PHP script (e.g., fetching data from the database or processing forms).
4. While processing, the PHP thread uses a portion of the server’s memory up to the [PHP memory](#php-memory) limit set in Kinsta.
5. If there are multiple concurrent visitors, each request is assigned to a different PHP thread. If all threads are busy, additional requests wait until a thread becomes available.
6. PHP then generates an HTML page using your theme’s PHP files (and any plugin files, if applicable).
7. PHP hands the rendered HTML page back to the web server.
8. The page is served to the visitor.

If your site does not use caching or is not optimized, PHP threads may be busy for longer, which can degrade performance and lead to timeouts or 503 and 504 errors when visitors access your site. For information about how to check the PHP performance and how to optimize your PHP threads, refer to [PHP performance](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/).

## PHP threads

PHP threads (previously known as PHP workers) are individual PHP processes responsible for handling incoming requests to your website. Each thread processes one request at a time, meaning if you have two threads, only two requests can be processed simultaneously.

Once a PHP thread finishes processing a request (e.g., rendering a page or fetching data from a database), it becomes free to handle the next one.

PHP threads really come into play when a site doesn’t or can’t cache most of its content. The more dynamic a website is, the more PHP threads it will likely need. Cached content doesn’t require PHP threads; they’re really only needed when the site needs to query the database to get or change information. An optimized site handles requests quickly, freeing up PHP threads for the next request in the queue.

For information about how to optimize your PHP threads, refer to [PHP performance](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/).

### Kinsta plans and PHP threads

The following table shows the default PHP pool, thread count, and memory per thread that are included by default in each plan at Kinsta:

| **Plan** | **Pool size** | **Thread count** | **Memory per thread** |
| --- | --- | --- | --- |
| Single 35k visits Single 20GB bandwidth | 512MB | 2 | 256MB |
| Single 65k visits Single 40GB bandwidth  Launch  Launch Plus  Build  Expand  Scale  Lead | 1GB | 4 | 256MB |
| Single 125k visits Single 65GB bandwidth | 1.5GB | 6 | 256MB |
| Single 315k visits Single 125GB bandwidth | 1.5GB | 6 | 256MB |
| Single 500k visits Single 250GB bandwidth | 2GB | 8 | 256MB |
| Single 750k visits Single 500GB bandwidth | 2GB | 8 | 256MB |
| Single 1.25M visits Single 750GB bandwidth | 5GB | 10 | 512MB |
| Single 1.9M visits Single 1125GB bandwidth | 6GB | 12 | 512MB |
| Single 2.5M visits Single 1500GB bandwidth | 7GB | 14 | 512MB |
| Single 3.15M visits Single 1875GB bandwidth | 8GB | 16 | 512MB |
| WP 2 | 512MB | 2 | 256MB |
| WP 5 | 1GB | 4 | 256MB |
| WP 10 | 1GB | 4 | 256MB |
| WP 20 | 1.5GB | 6 | 256MB |
| WP 40 | 1.5GB | 6 | 256MB |
| WP 60 | 4GB | 8 | 512MB |
| WP 80 | 5GB | 10 | 512MB |
| WP 120 | 6GB | 12 | 512MB |
| WP 150 | 7GB | 14 | 512MB |
| Agency 20 | 3GB | 6 | 512MB |
| Agency 40 | 3GB | 6 | 512MB |
| Agency 60 | 4GB | 8 | 512MB |

You can [change the number of PHP threads](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/#change-php-performance) for each site within **Sites** > ***sitename*** > **Info** > **PHP performance** > **Change**.

## PHP memory limit

The PHP memory limit defines the maximum amount of memory (RAM) each PHP thread can use while processing a request.

This limit is crucial because PHP scripts (especially in WordPress) often need to handle memory-intensive tasks such as large database queries, media uploads, or complex calculations.

If a script exceeds the set memory limit, it results in an error (e.g., “Allowed memory size exhausted”). This prevents one script from consuming excessive server resources.

### Kinsta plans and PHP memory

Kinsta’s default memory limit is:

**256MB** for the following plans:

- Single 750k visits and below
- Single 500GB bandwidth and below
- WP 40 and below
- Launch
- Launch Plus
- Build
- Expand
- Scale
- Lead

**512MB** for the following plans:

- Single 1.25M visits and above
- Single 750GB bandwidth and above
- WP 60 and above
- Agency plans

This limit exists to [prevent PHP scripts from consuming excessive memory](https://kinsta.com/blog/php-memory-limit/#what-should-php-memory-limit-be). If you set the limit too high, a misconfigured or broken script can cause serious issues by using up too much memory.

You can [change a site’s PHP memory limit](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/#change-php-performance) within **Sites** > ***sitename*** > **Info** > **PHP performance** > **Change**.

## Interaction between PHP threads and memory

The number of PHP threads should not be confused with the PHP memory limit. PHP threads are individual PHP processes that handle incoming web requests, whereas the PHP memory limit specifies the maximum amount of memory (RAM) a single PHP script can use during execution.

PHP threads manage concurrency by processing multiple requests simultaneously, whereas the PHP memory limit manages resource allocation by restricting the memory usage of individual scripts. This prevents any single script from using all the server’s available memory.

PHP memory limits are important for scripts requiring substantial memory, such as those performing large database queries, handling large file uploads, or executing complex calculations. If you encounter memory limit errors on your site, increasing the number of PHP threads won’t resolve this issue. Instead, you should [increase the memory per thread](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/#change-php-performance) within **Sites** > ***sitename*** > **Info** > **PHP performance** > **Change**.

## Interaction between PHP threads, CPU, and RAM

When adding PHP threads, CPU and RAM resources must be taken into account. If you increase the number of PHP threads, but the server needs more CPU and RAM to support those threads, this will create a bottleneck because the requests won’t be handled efficiently.

Here at Kinsta, each custom LXD container is configured with 12 CPUs and 8 GB of RAM. Additionally, our high-performance, enterprise-grade servers help your site’s PHP threads run more efficiently. Our scalable infrastructure ensures that your WordPress site’s PHP threads have enough CPU resources to operate at peak performance.

## Default PHP values

As a Managed WordPress service, Kinsta has the optimal PHP settings configured to work best with WordPress sites. If you have specific PHP requirements, feel free to reach out to our Support Team to discuss your needs.

Kinsta offers PHP 7.4, 8.0, 8.1, 8.2, 8.3, 8.4 and 8.5. These are the default settings for PHP:

| PHP setting | Value |
| --- | --- |
| memory_limit | 256M for the following plans:  - Single 750k visits and below - Single 500GB bandwidth and below - WP 40 and below - Launch - Launch Plus - Build - Expand - Scale - Lead   512MB for the following plans:   - Single 1.25M visits and above - Single 750GB bandwidth and above - WP 60 and above - Agency plans |
| upload_max_filesize post_max_size | 128M for the following plans:  - Single 125k visits and below - Single 65GB bandwidth and below - WP 2 - Launch - Launch Plus - Build - Expand   256M for the following plans:   - Single 315k visits and above - Single 125GB bandwidth and above - WP 5 and above - Scale - Lead   If you have a dedicated server, this can be increased to 500M. |
| max_input_vars | 10000 for the following plans:  - Single 125k visits and below - Single 65GB bandwidth and below - WP 2 - Launch - Launch Plus - Build - Expand   15000 for the following plans:   - Single 315k visits and above - Single 125GB bandwidth and above - WP 5 and above - Scale - Lead |
| max_execution_time max_input_time | 300 for the following plans:  - Single 750k visits and below - Single 500GB bandwidth and below - WP 40 and below - Launch - Launch Plus - Build - Expand - Scale - Lead   600 for the following plans:   - Single 1.25M visits and above - Single 750GB bandwidth and above - WP 60 and above - Agency plans |
| max_file_uploads | 20 for the following plans:  - Single 125k visits and below - Single 65GB bandwidth and below - WP 2 - Launch - Launch Plus - Build - Expand   50 for the following plans:   - Single 315k visits to Single 750k visits - Single 125GB to Single 500GB bandwidth - WP 5 to WP 40 - Scale - Lead   100 for the following plans:   - Single 1.25M visits and above - Single 750GB bandwidth and above - WP 60 and above - Agency plans |

## Disabled PHP functions

The following PHP functions are disabled on MyKinsta and cannot be enabled:

- `exec() / shell_exec()`
- `popen`
- `proc_open`
- `proc_close`
- `proc_get_status`
- `proc_terminate`
- `proc_nice`
- `posix_kill`
- `symlink`
- `getmypid`
- `getpwuid / posix_getpwuid`
- `pcntl_signal()`
- `get_current_user`
- `disk_total_space()`
