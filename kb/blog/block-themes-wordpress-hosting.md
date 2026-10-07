---
url: "https://kinsta.com/blog/block-themes-wordpress-hosting/"
title: "How modern block themes are changing WordPress hosting"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "WordPress Hosting", "How modern block themes are changing WordPress hosting"]
kinsta_last_updated: "2026-03-17T11:46:54+00:00"
sitemap_lastmod: "2026-03-17T11:46:54"
fetched_at: "2026-10-07T22:42:41Z"
sha256: "201eea2c56d39c95d93eec138910c761a1b0e6632b0840dd5a2856d095844aa6"
body_chars: 11849
extracted_with: "main article"
status: "live"
---

# How modern block themes are changing WordPress hosting

**Section:** Resource Center > Blog > WordPress Hosting > How modern block themes are changing WordPress hosting
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/block-themes-wordpress-hosting/
**Kinsta last updated:** 2026-03-17T11:46:54+00:00

## On this page

- [What happens when a WordPress page is requested](#what-happens-when-a-wordpress-page-is-requested)
  - [1. The browser sends the request](#1-the-browser-sends-the-request)
  - [2. Cache check](#2-cache-check)
  - [3. WordPress fires up](#3-wordpress-fires-up)
  - [4. Main query resolution](#4-main-query-resolution)
  - [5. Template resolution](#5-template-resolution)
    - [Classic themes](#classic-themes)
    - [Block themes](#block-themes)
  - [6. Layout assembly](#6-layout-assembly)
    - [Classic themes](#classic-themes)
    - [Block themes](#block-themes)
  - [7. Content structure](#7-content-structure)
    - [Classic themes](#classic-themes)
    - [Block themes](#block-themes)
  - [8. Dynamic rendering](#8-dynamic-rendering)
  - [9. Styling](#9-styling)
  - [10. Final output](#10-final-output)
- [Where block themes shift the load](#where-block-themes-shift-the-load)
- [Hosting considerations for block-based sites](#hosting-considerations-for-block-based-sites)
  - [Coordinated caching across layers](#coordinated-caching-across-layers)
  - [PHP capacity and runtime performance](#php-capacity-and-runtime-performance)
  - [Database and object caching](#database-and-object-caching)
  - [Observability and monitoring](#observability-and-monitoring)
- [Running WordPress the way it works today](#running-wordpress-the-way-it-works-today)

---

Author
:   [Bud Kraus](https://kinsta.com/blog/author/budkraus/ "Posts by Bud Kraus")

Updated
:   March 17, 2026

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![](https://kinsta.com/wp-content/uploads/2026/03/how-modern-block-themes-change-hosting-1-1024x512.png)

Managed WordPress hosting exists to run WordPress well. It provides an environment tuned for how WordPress behaves under load, how it handles [caching](https://kinsta.com/blog/wordpress-caching-plugins/), and how it executes PHP.

[Block themes](https://kinsta.com/blog/wordpress-block-themes/) do not change the fundamentals of hosting, but they do change where performance bottlenecks appear. This is where the role of the web host becomes clearer. Infrastructure alone does not make a site fast; poorly tuned infrastructure becomes apparent in modern WordPress workflows, especially when dynamic blocks, the [Site Editor](https://kinsta.com/blog/wordpress-full-site-editing/), previews, and logged-in sessions are involved.

To understand why, it helps to look at what actually happens during a page request and how hosting decisions affect the user experience when a block-based architecture is used.

## What happens when a WordPress page is requested

Let’s walk through a simple request that returns a [200 OK response](https://kinsta.com/blog/http-status-codes/#understanding-http-status-code-classes).

### 1. The browser sends the request

A user enters a URL or clicks a link. If the server’s IP address is not already cached, the browser performs a [DNS lookup](https://kinsta.com/blog/reduce-dns-lookups/). It then opens a TCP connection and negotiates a secure [TLS](https://kinsta.com/blog/tls-vs-ssl/) session.

Before WordPress is involved, the request passes through the web server and any configured layers such as firewalls or reverse proxies.

### 2. Cache check

The server checks whether a valid cached version of the requested page exists.

If a [full-page HTML cache](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/) is available and valid, WordPress does not execute. The cached response is returned immediately.

If no cache entry exists, or if caching is intentionally bypassed for logged-in users, previews, or specific endpoints, the request continues to WordPress.

### 3. WordPress fires up

WordPress loads its core files, active plugins, and the active theme. It initializes hooks and prepares to resolve the request.

At this stage, WordPress does not yet render output. It determines what content is being requested.

### 4. Main query resolution

Using rewrite rules and query variables, WordPress builds and executes the main database query. It determines whether the request is for a single post, page, archive, search result, or another content type.

Only after this does template selection begin.

### 5. Template resolution

This is where block and classic themes begin to differ structurally.

#### Classic themes

WordPress evaluates the template hierarchy and selects the appropriate PHP template file, such as single.php, page.php, or archive.php. That file contains PHP logic that outputs HTML directly.

#### Block themes

WordPress checks whether a customized block template exists in the database. If one exists, it takes priority. If not, WordPress falls back to the block template file included in the theme, such as single.html or index.html.

The selected template is then processed through the block rendering system.

### 6. Layout assembly

#### Classic themes

The layout is constructed through PHP templates. These templates combine markup, logic, and function calls to produce HTML output.

#### Block themes

The layout is assembled from block templates, template parts, and post content. Block markup is parsed, and each block is rendered into HTML before the final output is generated.

### 7. Content structure

#### Classic themes

Post content is primarily stored as HTML in the database. During output, WordPress applies filters, shortcodes, and other processing before rendering.

#### Block themes

Block content is stored as HTML with embedded block metadata, for example:

```
<!-- wp:image {"id":123} -->

<img src="logo.png">

<!-- /wp:image -->
```

When WordPress processes this content, it parses the block structure, understands attributes and nesting, and applies block-level attributes and styles such as spacing, alignment, and typography before generating the final HTML.

### 8. Dynamic rendering

Dynamic rendering exists in both classic and block themes. Many classic themes rely on custom queries, widgets, or shortcodes that generate output at runtime.

In block-based architectures, dynamic behavior is formalized through dynamic blocks. For example, a Query Loop block generates its markup during the request using PHP rather than storing static HTML in the database.

When full-page caching is bypassed, this rendering workflow happens on every request.

### 9. Styling

For classic themes, styling is typically delivered through [static CSS files](https://kinsta.com/blog/wordpress-css/) enqueued by the theme.

For block themes, global styles defined in `theme.json` and block metadata allow WordPress to automatically generate consistent CSS. This reduces the need for large handcrafted stylesheets and centralizes design configuration.

### 10. Final output

After templates, content, blocks, and styles are processed, WordPress produces the final HTML response.

The server sends the payload to the browser. If configured, the response may then be cached for future requests.

## Where block themes shift the load

The request lifecycle you just walked through applies to both [classic and block themes](https://kinsta.com/blog/wordpress-theme-core-concepts/). WordPress still resolves queries, selects templates, executes PHP, and returns HTML.

What changes with block themes is not the foundation, but where work happens and when it cannot be skipped.

First, [templates](https://kinsta.com/blog/wordpress-post-templates/) can live in the database. When a user edits a template in the Site Editor, WordPress stores that version and prioritizes it over the file in the theme directory. This adds flexibility, but it also means deployments and cache invalidation need to account for database-stored templates.

Second, [dynamic blocks](https://kinsta.com/blog/dynamic-blocks/) make runtime rendering more visible. Classic themes can generate dynamic output through custom queries, widgets, or shortcodes. Block themes formalize this pattern through dynamic blocks, such as the Query Loop block. When full-page caching is bypassed, these blocks execute PHP during the request.

Third, editor workflows rely heavily on REST endpoints. Saving templates, updating global styles, previewing changes, and interacting with patterns generate uncached requests. These paths depend directly on PHP execution, database performance, and object caching.

Finally, global styles defined in `theme.json` centralize design decisions. When styles or template structures change, cache coordination becomes more important to ensure that visitors and editors see updated output immediately.

None of these shifts requires a different type of hosting. They do make certain infrastructure weaknesses more visible, particularly in uncached and logged-in scenarios.

With that in mind, the next step is to look at what a well-configured hosting environment should handle in a block-based setup.

## Hosting considerations for block-based sites

Block themes do not introduce new hosting requirements. They make existing ones more important to get right.

A well-configured environment should account for both cached and uncached paths, especially for editors and logged-in users.

### Coordinated caching across layers

[Full-page caching](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/) remains the most effective performance layer for anonymous traffic. Public pages should be cached aggressively, while previews, logged-in sessions, and specific endpoints are automatically bypassed.

[Object caching](https://kinsta.com/docs/wordpress-hosting/caching/redis-cache/) also plays a significant role. By storing repeated query results and computed data structures in memory, an object cache reduces database load and improves both frontend and backend responsiveness.

Cache invalidation needs to be coordinated. When content, templates, or global styles are updated, related pages should refresh promptly. Poor cache coordination can result in outdated layouts, inconsistent styles, or confusing preview behavior.

A CDN complements this setup by caching static assets such as images, fonts, and scripts closer to visitors.

[Caching](https://kinsta.com/blog/wordpress-cache/) is not about one layer. It is about how these layers work together.

### PHP capacity and runtime performance

When full-page caching is bypassed, WordPress executes PHP to resolve queries, render templates, and process dynamic blocks.

This makes PHP capacity planning important. The environment should provide enough [PHP threads](https://kinsta.com/blog/php-threads/) to handle expected concurrency without queue buildup. [Memory limits](https://kinsta.com/blog/php-memory-limit/) should be configured to prevent swapping under load.

OPcache should be enabled and properly sized so that PHP bytecode does not need to be recompiled repeatedly. During deployments, OPcache should refresh so updated code runs immediately.

These practices apply to all WordPress sites, but block-based workflows can make performance issues more noticeable when rendering is dynamic.

### Database and object caching

Block templates customized in the Site Editor are stored in the database. Block content includes structured metadata that WordPress parses before output. While this processing is efficient, it still depends on database responsiveness when caching is bypassed.

A persistent object cache reduces repeated queries and helps stabilize performance for both frontend visitors and editors working inside the dashboard.

### Observability and monitoring

As more activity shifts into runtime paths, visibility becomes more important. Hosts and site owners should monitor:

- Cache hit ratios
- PHP worker utilization and queue length
- Database query performance
- REST API response times
- Time to first byte for cached and uncached requests

Block themes do not require specialized infrastructure. They do make it easier to see when infrastructure is loosely configured.

## Running WordPress the way it works today

Block themes do not change what WordPress needs from hosting. They make it clearer when those needs are not met.

When templates live in the database, when dynamic blocks render at runtime, and when editors rely on uncached REST requests, infrastructure is no longer invisible. It either supports the workflow smoothly or it gets in the way.

That is where [managed hosting for WordPress](https://kinsta.com/pricing/) makes a difference.

At Kinsta, the entire stack is built specifically for how WordPress operates today, from coordinated caching and persistent object caching to tuned PHP performance and global CDN delivery on powerful cloud infrastructure. The goal is to ensure both visitors and editors experience consistent performance, even when rendering happens dynamically.

Block-based WordPress is not heavier. It is more transparent. And when the foundation is solid, that transparency works in your favor.

Bud Kraus

Bud Kraus has been working with WordPress as an in-class and online instructor, site developer, and content creator since 2009. He has produced instructional videos and written many articles for WordPress businesses.
