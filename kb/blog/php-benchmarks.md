---
url: "https://kinsta.com/blog/php-benchmarks/"
title: "PHP 8.5 benchmarks: The state of PHP performance across major CMSs and frameworks"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "PHP Updates", "PHP 8.5 benchmarks: The state of PHP performance across major CMSs and frameworks"]
kinsta_last_updated: "2025-12-13T22:44:47+00:00"
sitemap_lastmod: "2025-12-13T22:44:47"
fetched_at: "2026-10-07T22:41:47Z"
sha256: "35e1b7e3f4458225b8ebdf769a263a409ad31cb09e4e451f4d4f9866cc3633c8"
body_chars: 27501
extracted_with: "main article"
status: "live"
---

# PHP 8.5 benchmarks: The state of PHP performance across major CMSs and frameworks

**Section:** Resource Center > Blog > PHP Updates > PHP 8.5 benchmarks: The state of PHP performance across major CMSs and frameworks
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/php-benchmarks/
**Kinsta last updated:** 2025-12-13T22:44:47+00:00

## On this page

- [Our PHP benchmarking setup](#our-php-benchmarking-setup)
  - [Test environment](#test-environment)
  - [Configuration details](#configuration-details)
- [WordPress](#wordpress)
  - [WordPress benchmarks](#wordpress-benchmarks)
- [WooCommerce](#woocommerce)
  - [WooCommerce benchmarks](#woocommerce-benchmarks)
- [WordPress Easy Digital Downloads (EDD)](#wordpress-easy-digital-downloads-edd)
  - [EDD benchmarks](#edd-benchmarks)
- [Laravel](#laravel)
  - [Laravel benchmarks](#laravel-benchmarks)
- [Symfony](#symfony)
  - [Symfony benchmarks](#symfony-benchmarks)
- [Joomla](#joomla)
  - [Joomla benchmarks](#joomla-benchmarks)
- [Drupal](#drupal)
  - [Drupal benchmarks](#drupal-benchmarks)
- [CakePHP](#cakephp)
  - [CakePHP benchmarks](#cakephp-benchmarks)
- [CodeIgniter](#codeigniter)
  - [CodeIgniter benchmarks](#codeigniter-benchmarks)
- [Craft CMS](#craft-cms)
  - [Craft CMS benchmarks](#craft-cms-benchmarks)
- [October CMS](#october-cms)
  - [October CMS benchmarks](#october-cms-benchmarks)
- [OpenCart](#opencart)
  - [OpenCart benchmarks](#opencart-benchmarks)
- [Grav](#grav)
  - [Grav benchmarks](#grav-benchmarks)
- [PHP usage statistics](#php-usage-statistics)
  - [Share of server-side languages](#share-of-server-side-languages)
  - [PHP’s position among server-side languages](#phps-position-among-server-side-languages)
  - [Long-term usage trends](#long-term-usage-trends)
  - [PHP version adoption and upgrade trends](#php-version-adoption-and-upgrade-trends)
- [What these benchmarks mean in practice](#what-these-benchmarks-mean-in-practice)

---

Author
:   [Joel Olawanle](https://kinsta.com/blog/author/joelolawanle/ "Posts by Joel Olawanle")

Updated
:   December 13, 2025

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![](https://kinsta.com/wp-content/uploads/2025/12/php-benchmark-2-1024x512.png)

PHP 8.5 has now been officially released, and developers naturally want to know what kind of performance improvements they can expect across popular CMSs and frameworks.

To find out, we benchmarked 13 widely used CMSs and frameworks, including WordPress, WooCommerce, Drupal, Joomla, Laravel, Symfony and CodeIgniter, on PHP 8.2, 8.3, 8.4, and 8.5 under identical conditions. WordPress was also tested on PHP 7.4, since a notable share of sites still run on that version.

Our intention is to provide a clear, practical look at how performance shifts across recent PHP releases and what you can expect when upgrading.

## Our PHP benchmarking setup

To ensure consistent and reproducible results, all benchmarks were executed in identical, isolated environments using Docker Compose. Each PHP version and CMS/framework was tested independently with its own containers, database, and configuration.

### Test environment

- **Machine:** Ubuntu 24.04.3 LTS virtual machine (Kinsta internal benchmarking environment), 30 vCPU, 120 GB Memory, 100 GB SSD.
- **Virtualization:** Google Cloud Platform compute instance running inside an isolated Docker environment.
- **Web stack:** `nginx:alpine` or `nginx:stable` (depending on CMS requirements) with PHP-FPM (official Docker images), JIT disabled, and OPcache enabled using standard production settings.
- **Database:** MariaDB 10.11 (official Docker image).
- **PHP versions tested:** 7.4, 8.2, 8.3, 8.4, and 8.5. All based on the official php:<version>-fpm Docker images.
- **Tooling:** ApacheBench (ab) with five runs per configuration and one warmup request before each test.
- **Parameters:**
  - Concurrency: **15** simultaneous requests
  - Requests per run: **1000**

- **Results:** Measured in requests per second (req/s). A higher number indicates faster request handling and better performance.

### Configuration details

We kept the application and server configuration close to what you would deploy in a straightforward production environment:

- **PHP and OPcache:**
  - `memory_limit=128M` (Drupal: 256M)
  - `max_execution_time=30`
  - `opcache.enable=1`, `opcache.jit_buffer_size=0`
  - `opcache.memory_consumption=128`
  - Interned strings buffer: 8 MB (16 MB for WordPress)
  - Timestamps checked every 2 seconds (`validate_timestamps=0` for WordPress)
  - No custom FPM tuning
- **Framework and CMS settings:**
  - **Laravel:** APP_ENV=production, APP_DEBUG=false
  - **WordPress:** WP_DEBUG=false
  - **Drupal:** Production mode (no development modules enabled)
  - No debug bars, profiler plugins, or development extensions

Let’s take a look at the results.

## WordPress

WordPress.org is an open-source CMS and remains the most popular CMS worldwide, powering [over 43% of all websites](https://w3techs.com/technologies/details/cm-wordpress).

It was originally built for blogging but has since evolved into a versatile platform capable of supporting everything from personal blogs to large e-commerce sites and enterprise applications. The WordPress REST API also makes it function as a [headless CMS](https://kinsta.com/blog/headless-wordpress-hosting/), compatible with modern JavaScript frameworks and SSGs.

For this test, we used a default WordPress 6.8.0 installation with no additional plugins or caching layers.

### WordPress benchmarks

- **Tested Versions:** WordPress 6.8.0
- **Tested URL:** `/`
- **Response size:** 49,788 bytes (~48.6 KB)
- **Results:**
  - **PHP 7.4:** 139.06 req/s
  - **PHP 8.2:** 146.09 req/s
  - **PHP 8.3:** 142.75 req/s
  - **PHP 8.4:** 148.22 req/s
  - **PHP 8.5:** 148.30 req/s

![WordPress 6.8.0 performance on PHP 7.4, 8.2, 8.3, 8.4 and 8.5 (in req/s).](https://kinsta.com/wp-content/uploads/2025/12/wordpress-set.png)

WordPress 6.8.0 performance on PHP 7.4, 8.2, 8.3, 8.4, and 8.5 (in req/s).

WordPress shows steady performance improvements when moving from PHP 7.4 to modern PHP versions. PHP 8.4 and PHP 8.5 deliver the fastest results in our tests, both landing around 148 req/s, with PHP 8.5 slightly ahead.

Performance between PHP 8.2, 8.3, 8.4, and 8.5 remains close, and no major regressions appeared. The biggest gain comes from upgrading older sites still running PHP 7.4, which sees a approx. 6.6% improvement when moving to PHP 8.5.

## WooCommerce

WooCommerce is the most widely used e-commerce plugin for WordPress, powering [over three million](https://trends.builtwith.com/shop/WooCommerce-Checkout) live stores worldwide, which accounts for approximately [8% of all e-commerce sites](https://trends.builtwith.com/shop) on the internet.

WooCommerce also leverages the extensive WordPress ecosystem, providing access to plugins, WP-CLI, hooks, filters, and REST API endpoints to manage and enhance your store with ease.

### WooCommerce benchmarks

- **Tested version:** Woo 10.2.2 on WordPress 6.8.0
- **Tested URL:** `/?post_type=product`
- **Response size:** 88,855 bytes (~86.8 KB) and 54,822 bytes (~53.5 KB) on PHP 8.5
- **Results:**
  - **PHP 7.4:** 44.20 req/s
  - **PHP 8.2:** 54.67 req/s
  - **PHP 8.3:** 53.74 req/s
  - **PHP 8.4:** 53.37 req/s
  - **PHP 8.5:** 71.02 req/s

![Woo 10.2.2 performance on PHP 7.4, 8.2, 8.3, 8.4 and 8.5 (in req/s).](https://kinsta.com/wp-content/uploads/2025/12/woo-set.png)

Woo 10.2.2 performance on PHP 7.4, 8.2, 8.3, 8.4 and 8.5 (in req/s).

WooCommerce experiences a substantial performance improvement when upgrading from PHP 7.4 to modern PHP versions, with PHP 8.2 delivering about 23% higher throughput than PHP 7.4. Performance remains stable across PHP 8.2–8.4, with only minor variation.

The standout result here is PHP 8.5, which reaches 71.02 req/s, a roughly 33% increase over PHP 8.4. This jump aligns with the notably smaller response size served during the test, suggesting changes in output structure or rendering overhead that reduced payload cost.

## WordPress Easy Digital Downloads (EDD)

Easy Digital Downloads (EDD) is a WordPress e-commerce plugin focused on selling digital products (downloads, licenses, subscriptions). It’s widely used for software, courses, media assets, and memberships where a streamlined checkout and file delivery flow matters.

### EDD benchmarks

- **Tested version:** Easy Digital Downloads 3.5.2 on WordPress 6.8
- **Tested URL:** `/?page_id=9`
- **Response size:** 54,177.75 bytes (~ 52.92 KB)
- **Results:**
  - **PHP 8.2:** 85.80 req/s
  - **PHP 8.3:** 85.69 req/s
  - **PHP 8.4:** 85.54 req/s
  - **PHP 8.5:** 86.52 req/s

![EDD 3.5.2 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).](https://kinsta.com/wp-content/uploads/2025/12/edd-set.png)

EDD 3.5.2 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).

EDD shows consistent performance across PHP 8.2–8.5, with all versions delivering nearly identical throughput. This demonstrates that EDD’s workload is already highly optimized and doesn’t suffer significant changes from the incremental improvements in recent PHP releases.

## Laravel

Laravel is an open-source PHP framework that offers web developers a range of tools and resources to build modern web applications.

Laravel is both versatile and easy to use, thanks to its built-in features, including a command-line interface (Artisan), native authentication, and a model-view-controller (MVC) architecture.

### Laravel benchmarks

- **Tested version:** Laravel 12.33.0
- **Tested URL:** `/`
- **Response size:** 80,650 bytes (~ 78.8 KB)
- **Results:**
  - **PHP 8.2:** 730.11 req/s
  - **PHP 8.3:** 708.44 req/s
  - **PHP 8.4:** 695.98 req/s
  - **PHP 8.5:** 700.33 req/s

![Laravel 12.33.0 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).](https://kinsta.com/wp-content/uploads/2025/12/laravel-set.png)

Laravel 12.33.0 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).

In our benchmarks, PHP 8.2 delivered the highest throughput at 730.11 req/s, with PHP 8.3, 8.4, and 8.5 following closely behind.

The Laravel results above reflect a baseline (“bare”) test commonly used in framework benchmarks. It measures minimal framework overhead by serving the default Welcome page, with no database queries, authentication, or application logic involved. The larger response size of about 80 KB reflects Laravel’s full-stack HTML output rather than real workload complexity.

To validate real-world behavior, we also ran a separate API-focused benchmark that included authentication (Sanctum), multiple Eloquent ORM queries with eager loading, request validation, pagination, and JSON serialization. In that scenario, Laravel consistently delivered between 430 and 445 req/s across PHP 8.2 to 8.5, which is expected once database access and application logic become the dominant cost.

![Laravel 12.33.0 API focused performance in req/s.](https://kinsta.com/wp-content/uploads/2025/12/laravel-api-focused-benchmark.png)

Laravel 12.33.0 API focused performance in req/s.

The key takeaway is that Laravel’s performance remains stable across modern PHP versions, and real-world throughput is shaped far more by application design and infrastructure than by PHP minor versions alone.

## Symfony

Symfony is one of the most widely used PHP frameworks, with over [85 million downloads](https://packagist.org/packages/symfony/symfony) on Packagist. Its component-based architecture powers many modern PHP platforms, so we added Symfony to the benchmark suite in response to strong community demand.

For this test, we set up a Symfony application that mirrors a typical real-world workload. The app includes database access using Doctrine ORM, a controller that fetches a set of records, and a Twig template that renders the results into HTML.

### Symfony benchmarks

- **Tested version:** Symfony 7.4
- **Tested URL:** `/`
- **Response size:** 12,175 bytes (~11.9 KB)
- **Results:**
  - **PHP 8.2:** 1018.84 req/s
  - **PHP 8.3:** 953.88 req/s
  - **PHP 8.4:** 992.53 req/s
  - **PHP 8.5:** 1002.17 req/s

![Symfony 7.4 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).](https://kinsta.com/wp-content/uploads/2025/12/symfony-benchmark.png)

Symfony 7.4 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).

Symfony shows stable throughput across all PHP versions, with performance differences falling within normal variance. PHP 8.2 delivered the fastest result at 1,018 req/s, while PHP 8.5 performed nearly the same at 1,002 req/s.

The consistent response size (~12 KB) across all runs confirms that the workload remains identical, and the small changes in throughput reflect expected runtime behavior rather than framework-level differences.

## Joomla

Joomla is a popular open-source CMS built on a model–view–controller web application framework that can be used independently of the CMS to build online applications. It features a flexible system that is easy to extend and customize due to its large extension library.

### Joomla benchmarks

- **Tested version:** Joomla 5.2.2
- **Tested URL:** `/`
- **Response size:** 7,713 bytes (~ 7.5 KB)
- **Results:**
  - **PHP 8.2:** 290.30 req/s
  - **PHP 8.3:** 287.37 req/s
  - **PHP 8.4:** 289.23 req/s

![Joomla 5.2.2 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).](https://kinsta.com/wp-content/uploads/2025/12/joomla-set.png)

Joomla 5.2.2 performance on PHP 8.2, 8.3, 8.4, and 8.5 (in req/s).

Joomla’s performance remains very stable across all tested PHP versions. Throughput stays between 287 and 290 req/s, with no meaningful performance regressions or spikes. PHP 8.2 produced the highest value in this series, but the differences between PHP 8.2, 8.3, and 8.4 are minimal within a 1% range.

## Drupal

Drupal is a powerful open-source CMS known for its flexibility, scalability, and security, making it a top choice for enterprise websites, universities, and government organizations. It is ideal for complex websites that require custom data structures, multilingual support, and role-based content workflows.

In January 2025, Drupal 7 [officially reached end of life](https://www.drupal.org/about/announcements/blog/drupal-7-has-reached-end-of-life-psa-2025-01-06) after more than 14 years of community support. However, it still powers [31% of the 684k+ active Drupal sites](https://www.drupal.org/project/usage/drupal). This explains why we included Drupal 7 in our benchmarks alongside Drupal 10 and Drupal 11 to reflect real-world usage during the transition period.

### Drupal benchmarks

- **Tested version:** Drupal 7, 10, and 11
- **Tested URL:** `/`
- **Response sizes:**
  - Drupal 7 – 7,985 bytes (~ 7.8 KB)
  - Drupal 10 – 16,476 bytes (~ 16.1 KB)
  - Drupal 11 – 15,606 bytes (~ 15.2 KB)

- **Results for Drupal 7:**
  - **PHP 8.2:** 907.53 req/s
  - **PHP 8.3:** 900.26 req/s

- **Results for Drupal 10:**
  - **PHP 8.2:** 1401.43 req/s
  - **PHP 8.3:** 782.84 req/s
  - **PHP 8.4:** 1391.39 req/s

- **Results for Drupal 11:**
  - **PHP 8.3:** 782.84 req/s
  - **PHP 8.4:** 817.40 req/s

![Drupal 7, 10 and 11 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).](https://kinsta.com/wp-content/uploads/2025/12/drupal-benchmark.png)

Drupal 7, 10 and 11 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).

Across its tested PHP versions, Drupal 10 shows higher throughput on PHP 8.2 and 8.4 compared to its own PHP 8.3 result.

Drupal 11, still relatively new, shows strong but slightly lower throughput, ranging between 780 and 840 req/s. Drupal 7 maintains around 920 req/s on both PHP 8.2 and PHP 8.3, which is expected given its older architecture.

## CakePHP

CakePHP is a modern PHP framework designed to help developers build robust web applications quickly and efficiently.

The latest release, CakePHP 5, introduces significant improvements in performance and developer experience. It features an updated ORM, improved dependency injection, streamlined middleware management, and stronger type safety across the framework.

### CakePHP benchmarks

- **Tested version:** CakePHP 5.2.0
- **Tested URL:** `/`
- **Response size:** 7,573 bytes (~ 7.4 KB)
- **Results:**
  - **PHP 8.2:** 74.70 req/s
  - **PHP 8.3:** 75.53 req/s
  - **PHP 8.4:** 74.16 req/s
  - **PHP 8.5:** 73.76 req/s

![CakePHP 5.2.0 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).](https://kinsta.com/wp-content/uploads/2025/12/cake-php-set.png)

CakePHP 5.2.0 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).

CakePHP delivers stable performance across all tested PHP versions, with results ranging between 73 and 76 req/s. PHP 8.3 produced the highest throughput in this series, but overall differences remain small.

## CodeIgniter

CodeIgniter is a lightweight PHP framework built for developers who need a fast, secure, and minimal foundation for full-featured web applications.

It maintains its hallmark simplicity while introducing modern standards, such as PSR compliance, improved dependency management, context-sensitive escaping, and built-in protection against CSRF/XSS attacks.

### CodeIgniter benchmarks

- **Tested version:** CodeIgniter 4.6.3
- **Tested URL:** `/`
- **Response size:** 46,103 bytes (~ 45 KB) and 17,243 bytes (~ 17 KB) on PHP 8.5
- **Results:**
  - **PHP 8.2:** 1,216.41 req/s
  - **PHP 8.3:** 1,197.53 req/s
  - **PHP 8.4:** 1,214.03 req/s
  - **PHP 8.5:** 1,874.14 req/s

![CodeIgniter 4.6.3 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).](https://kinsta.com/wp-content/uploads/2025/12/codeigniter-benchmark.png)

CodeIgniter 4.6.3 performance on PHP 8.2, 8.3, 8.4, and 8.5 (in req/s).

PHP 8.2–8.4 all produce very similar throughput at around 1,200 req/s.

The standout result is PHP 8.5, which jumped to 1,874 req/s, a 54% increase over PHP 8.4. This spike aligns with the significantly smaller response size served under PHP 8.5 (17 KB vs. 45 KB), suggesting changes in rendered output, routing behavior, or default template content within the test environment.

## Craft CMS

Craft CMS is a flexible, content-first CMS built to empower designers, developers, and content teams to create custom digital experiences. It gives teams complete control over structure, design, and workflow, making it a favorite among creative agencies and enterprise brands.

### Craft CMS benchmarks

- **Tested version:** Craft CMS 5.0
- **Tested URL:** `/`
- **Response size:** 6,257 bytes (~ 6.1 KB)
- **Results:**
  - **PHP 8.2:** 201.23 req/s
  - **PHP 8.3:** 197.04 req/s
  - **PHP 8.4:** 196.23 req/s
  - **PHP 8.5:** 197.70 req/s

![Craft CMS 5.0 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).](https://kinsta.com/wp-content/uploads/2025/12/craft-cms-set.png)

Craft CMS 5.0 performance on PHP 8.2, 8.3, 8.4, and 8.5 (in req/s).

Craft CMS demonstrates very stable performance across all PHP 8.x versions, with results ranging between 196 and 201 req/s. PHP 8.2 delivered the highest throughput in this series, but the difference across versions is minimal.

## October CMS

October CMS is a modern, Laravel-based CMS built for developers who value simplicity, flexibility, and performance. It powers [over 100,000 websites](https://trends.builtwith.com/cms/October-CMS) worldwide.

Its foundation on the Laravel framework makes it a natural choice for teams already using Laravel, offering a familiar structure while adding a powerful visual backend for content editing. October CMS’s modular design, plugin marketplace, and reusable CMS components allow developers to accelerate production without sacrificing quality or customization.

### October CMS benchmarks

- **Tested version:** October CMS 4.0 (using Laravel 12.0)
- **Tested URL:** `/`
- **Response size:** 17,211 bytes (~ 16.8 KB)
- **Results:**
  - **PHP 8.2:** 173.54 req/s
  - **PHP 8.3:** 152.75 req/s
  - **PHP 8.4:** 151.38 req/s
  - **PHP 8.5:** 162.71 req/s

![October CMS 4.0 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).](https://kinsta.com/wp-content/uploads/2025/12/octobercms-set.png)

October CMS 4.0 performance on PHP 8.2, 8.3, 8.4, and 8.5 (in req/s).

OctoberCMS performs best on PHP 8.2, reaching 173.54 req/s, followed by a noticeable dip on PHP 8.3 and 8.4. PHP 8.5 shows a meaningful recovery, climbing back to 162.71 req/s, though still short of the PHP 8.2 peak.

The trend is consistent with frameworks built on Laravel, exhibiting small fluctuations across PHP 8.x versions, with no significant regressions or gains.

## OpenCart

OpenCart is a popular open-source e-commerce platform that powers over 470,000 stores worldwide. It’s free to use, easy to install, and flexible enough to support businesses of all sizes.

OpenCart provides powerful store management tools that enable users to manage products, orders, customers, taxes, and coupons from a single, intuitive dashboard. It includes built-in SEO optimization, supports multiple stores from a single admin panel, and connects seamlessly with thousands of extensions and themes through its large marketplace.

### OpenCart benchmarks

- **Tested version:** OpenCart CMS 4.1.0.3
- **Tested URL:** `/`
- **Response size:** 32,713 bytes (~ 32.0 KB)
- **Results:**
  - **PHP 8.2:** 143.47 req/s
  - **PHP 8.3:** 142.04 req/s
  - **PHP 8.4:** 141.54 req/s
  - **PHP 8.5:** 142.45 req/s

![OpenCart CMS 4.1.0.3 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).](https://kinsta.com/wp-content/uploads/2025/12/open-cart-set.png)

OpenCart CMS 4.1.0.3 performance on PHP 8.2, 8.3, 8.4, and 8.5 (in req/s).

OpenCart demonstrates extremely consistent performance across all PHP 8.x versions, with results concentrated tightly between 141 and 143 req/s.

The best performance is seen with PHP 8.2, but PHP 8.5 follows closely at 142.45 req/s, showing no regressions and maintaining stable throughput.

## Grav

Grav is a modern, open-source flat-file CMS that emphasizes simplicity, speed, and flexibility. Unlike traditional database-driven systems, Grav stores content in plain text files using Markdown, making it extremely lightweight and easy to deploy.

### Grav benchmarks

- **Tested version:** Grav 1.8.0
- **Tested URL:** `/`
- **Response size:** 13,814 bytes (~ 13.5 KB)
- **Results:**
  - **PHP 8.2:** 600.36 req/s
  - **PHP 8.3:** 603.66 req/s
  - **PHP 8.4:** 586.49 req/s
  - **PHP 8.5:** 1,029.07 req/s

![Grav 1.8.0 performance on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).](https://kinsta.com/wp-content/uploads/2025/12/gravcms-benchmark.png)

Grav 1.8.0 performance on PHP 8.2, 8.3, 8.4, and 8.5 (in req/s).

Grav performs consistently on PHP 8.2–8.4, with throughput between 590 and 605 req/s. PHP 8.5 experiences a performance increase of about 75%, reaching 1,029 req/s.

## PHP usage statistics

With the [relea](https://kinsta.com/blog/php-8-5/)[se of PHP 8.5](https://www.php.net/releases/8.5/en.php), the language continues to evolve with new capabilities, including the pipe operator (`|>`), improved error handling with fatal error stack traces, and enhanced internationalization tools like `IntlListFormatter`. These updates modernize PHP’s developer experience while maintaining broad ecosystem compatibility.

To understand how PHP is used today, let’s look at a few key industry statistics.

### Share of server-side languages

PHP remains the dominant server-side language on the web, powering over 73% of websites that rely on server-side processing.

![Distribution of server-side powered web apps (W3Techs).](https://kinsta.com/wp-content/uploads/2025/12/php-programming-lang-usage.png)

Distribution of server-side powered web apps ([W3Techs](https://w3techs.com/technologies/overview/programming_language)).

### PHP’s position among server-side languages

When examining the market positions of the five most popular server-side languages, JavaScript dominates among developers of high-traffic sites, while PHP holds a strong middle ground, powering many websites and maintaining a steady average traffic rank over the years.

PHP powers the majority of the world’s most visited platforms, including microsoft.com, facebook.com, wikipedia.org, wordpress.org, and wordpress.com.

![Market positions among server-side programming languages. (W3Techs).](https://kinsta.com/wp-content/uploads/2025/12/php-market-position.png)

Market positions among server-side programming languages. ([W3Techs](https://w3techs.com/technologies/market/programming_language)).

### Long-term usage trends

PHP’s sustained leadership is supported by its mature ecosystem, flexible architecture, strong backward compatibility, and ease of maintenance. These factors have allowed PHP to remain a dependable foundation for both legacy systems and modern applications.

![Programming languages usage through time (W3Techs).](https://kinsta.com/wp-content/uploads/2025/12/php-server-side-usage.png)

Programming languages usage through time ([W3Techs](https://w3techs.com/technologies/history_overview/programming_language/ms/y)).

### PHP version adoption and upgrade trends

Version adoption statistics show that many developers remain cautious about upgrading major PHP versions. This behavior directly affects usage trends at the subversion level.

When PHP 8.0 was first released, adoption lagged due to compatibility concerns with PHP 7.4. However, since PHP 7.4 reached end-of-life in January 2023, usage patterns have shifted noticeably.

- PHP 7.4 usage dropped from over 35% in 2023 to 27.8% today
- The entire PHP 7.x family now represents 36.9% of active installations

![PHP subversion usage (W3Techs).](https://kinsta.com/wp-content/uploads/2025/12/php-subversion-usage.png)

PHP subversion usage ([W3Techs](https://w3techs.com/technologies/details/pl-php)).

## What these benchmarks mean in practice

Across all 13 CMSs and frameworks tested, our 2025 PHP benchmarks show that for most workloads, performance between PHP 8.2, 8.3, 8.4, and 8.5 doesn’t shift dramatically.

![Performance of all tested CMSs and frameworks on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).](https://kinsta.com/wp-content/uploads/2025/12/cms-frameworks-benchmarks-1.png)

Performance of all tested CMSs and frameworks on PHP 8.2, 8.3, 8.4 and 8.5 (in req/s).

Modern PHP is already highly optimized, and incremental releases rarely produce large speed jumps on their own. Upgrading to the newest version isn’t a guaranteed shortcut to faster applications.

**While these benchmarks reveal how each CMS or framework performs under identical lab conditions, real-world performance depends heavily on the hosting environment behind it.** Factors like CPU allocation, PHP workers, caching layers, container isolation, and database optimization all influence how much of PHP’s raw engine speed actually turns into faster page loads.

WordPress, WooCommerce, and Easy Digital Downloads, in particular, benefit from these especially under high traffic or heavy e-commerce loads.

This is exactly the layer a managed platform can optimize for you. At [Kinsta](https://kinsta.com/wordpress-hosting/), the platform is engineered to eliminate infrastructure bottlenecks and deliver consistent, high-performance PHP execution across all workloads.

With Kinsta, you get:

- World-class managed hosting for [WordPress](https://kinsta.com/wordpress-hosting/) and [WooCommerce](https://kinsta.com/wordpress-hosting/woocommerce/), built on a high-performance global network.
- One-click PHP version switching, including the latest PHP 8.4 and 8.5 releases.
- [PHP performance add-on](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/) to increase your PHP memory pool, threads, and per-thread limits to handle traffic surges or resource-heavy sites.
- Developer tools like SSH, Git, WP-CLI, and ionCube Loader preinstalled.
- [Staging environments](https://kinsta.com/docs/wordpress-hosting/staging-environment/), automatic daily backups, redirect rules, and performance monitoring with [Kinsta APM](https://kinsta.com/apm-tool/).
- [Isolated container technology](https://kinsta.com/blog/isolated-container-technology/), hardware firewalls, and Cloudflare DDoS protection for maximum security.
- [Kinsta API](https://kinsta.com/docs/kinsta-api/) for automation and integration with your workflows.
- 24/7 expert support from engineers who truly understand WordPress and PHP.

Kinsta’s infrastructure is also [SOC 2 compliant](https://kinsta.com/docs/service-information/soc-2/) and built on the fastest available virtual machines.

For teams building modern web applications with frameworks such as Laravel, CodeIgniter, or other PHP-based stacks, [Sevalla](https://sevalla.com/) (a product by Kinsta) offers a comprehensive cloud application platform that supports Docker-based deployments, auto-scaling, managed databases, and containerized apps, which is a strong match for real-world PHP workloads.

[Join](https://kinsta.com/pricing/) thousands of developers and businesses already running WordPress faster with Kinsta.

Joel Olawanle
[Kinsta](https://kinsta.com/)

Joel is a Frontend developer working at Kinsta as a Technical Editor. He is a passionate teacher with love for open source and has written over 300 technical articles majorly around JavaScript and it's frameworks.

- [Website](https://joelolawanle.com/)
- [LinkedIn](https://www.linkedin.com/in/olawanlejoel/)
- [Twitter](https://twitter.com/olawanle_joel)
- [YouTube](https://www.youtube.com/@joelolawanle)
