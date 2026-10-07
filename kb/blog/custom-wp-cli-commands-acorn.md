---
url: "https://kinsta.com/blog/custom-wp-cli-commands-acorn/"
title: "How to build custom WP-CLI commands and automate WordPress maintenance with Acorn"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "WordPress Development", "How to build custom WP-CLI commands and automate WordPress maintenance with Acorn"]
kinsta_last_updated: "2026-05-20T20:31:16+00:00"
sitemap_lastmod: "2026-05-20T20:31:16"
fetched_at: "2026-10-07T22:42:48Z"
sha256: "39a4b3fc195e7ec56b486674fd14e2b3975fabb54837912772390a794b3becdf"
body_chars: 18031
extracted_with: "main article"
status: "live"
---

# How to build custom WP-CLI commands and automate WordPress maintenance with Acorn

**Section:** Resource Center > Blog > WordPress Development > How to build custom WP-CLI commands and automate WordPress maintenance with Acorn
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/custom-wp-cli-commands-acorn/
**Kinsta last updated:** 2026-05-20T20:31:16+00:00

## On this page

- [How to install Acorn and run commands](#how-to-install-acorn-and-run-commands)
- [Creating your first Artisan command](#creating-your-first-artisan-command)
- [How to build 3 practical maintenance commands](#how-to-build-3-practical-maintenance-commands)
  - [1. Cleaning orphaned post metadata](#1-cleaning-orphaned-post-metadata)
  - [2. Deleting expired transients](#2-deleting-expired-transients)
  - [3. Auditing autoloaded options](#3-auditing-autoloaded-options)
- [How to access WordPress data within commands](#how-to-access-wordpress-data-within-commands)
- [Custom WP-CLI commands are straightforward with Acorn and Artisan Console](#custom-wp-cli-commands-are-straightforward-with-acorn-and-artisan-console)

---

Author
:   [Joel Olawanle](https://kinsta.com/blog/author/joelolawanle/ "Posts by Joel Olawanle")

Updated
:   May 20, 2026

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![](https://kinsta.com/wp-content/uploads/2026/01/automating-wordpress-maintenance-with-wp-cli-and-acorn-1024x512.png)

You likely have PHP scripts that do various jobs, such as cleaning up orphaned post metadata or deleting expired transients. Over time, that collection grows and lives in a theme file, a plugin folder, or a tucked-away directory. Acorn helps to rein in this disorganization by bringing Laravel’s Artisan Console to WordPress.

This means you can build custom WP-CLI commands with structured class files that centralize your maintenance logic. These commands run consistently across development, staging, and production using progress indicators, formatted table output, proper error handling, and more. You can then trigger them via SSH, schedule them with cron jobs, or execute them during deployments.

## How to install Acorn and run commands

The first step is to install the dependencies you need. Acorn needs [PHP 8.2](https://kinsta.com/blog/php-8-2/) or higher, [Composer](https://kinsta.com/blog/install-composer/) for managing dependencies, and [WP-CLI](https://kinsta.com/blog/wp-cli/) running on your server. Kinsta includes WP-CLI on all hosting plans, so you can start building commands straight away.

You install Acorn through Composer using `composer require roots/acorn` within the project root. Then add boot code to either your theme’s `functions.php` file or your main plugin file:

```
<?php
use Roots\Acorn\Application;
if (! class_exists(\Roots\Acorn\Application::class)) {
    wp_die(
        __('You need to install Acorn to use this site.', 'domain'),
        '',
        [
            'link_url' => 'https://roots.io/acorn/docs/installation/',
            'link_text' => __('Acorn Docs: Installation', 'domain'),
        ]
    );
}

add_action('after_setup_theme', function () {
    Application::configure()
        ->withProviders([
            App\Providers\ThemeServiceProvider::class,
        ])
        ->boot();
}, 0);
```

The zero-config setup stores application cache and logs in the [WordPress cache directory](https://kinsta.com/blog/wordpress-cache/) at `[wp-content]/cache/acorn/`, with your commands living in the theme’s `app/` directory.

The traditional structure follows Laravel conventions, such as dedicated directories for `app/`, `config/`, `storage/`, and `resources/` at your project root. You set this up with one line:

```
wp acorn acorn:init storage && wp acorn vendor:publish --tag=acorn
```

If you run `wp acorn list`, this verifies your installation by displaying all the available Acorn commands. From this point, all custom commands you create are stored in the `app/Console/Commands/` directory. Acorn automatically discovers any command classes in this location and registers them with WP-CLI.

## Creating your first Artisan command

The `wp acorn make:command CleanupCommand` Artisan command generates your file with the structure you need. It contains three key elements that every Artisan command needs:

- A `$signature` property that defines your command name and options.
- The `$description` property for help text.
- A `handle()` method where your command logic lives.

In this case, it builds `app/Console/Commands/CleanupCommand.php` with a basic command structure:

```
<?php
namespace App\Console\Commands;
use Illuminate\Console\Command;
class CleanupCommand extends Command
{
    protected $signature = 'app:cleanup';
    protected $description = 'Command description';
    public function handle()
    {
        //
    }
}
```

The `$signature` property uses a specific syntax:

- A basic command only needs a name, such as `cleanup:run`.
- You add required arguments by wrapping them in curly braces (`cleanup:run {days}`, for example).
- Optional arguments get a question mark: `cleanup:run {days?}`.
- Options use double dashes: `cleanup:run {--force} {--limit=100}`.

Next, include a description for the command and your basic logic:

```
protected $signature = 'cleanup:test {--dry-run : Preview changes without executing}';
protected $description = 'Test cleanup command';
public function handle()
{
    $dryRun = $this->option('dry-run');

    if ($dryRun) {
        $this->components->info('Running in dry-run mode');
    }

    $this->components->info('Cleanup command executed');

    return 0;
}
```

You can test this using `wp acorn cleanup:test --dry-run`. The command outputs formatted messages using Artisan’s component system. The `$this->components->info()` method displays success messages in green. You can also use `$this->components->error()` for errors, `$this->components->warn()` for warnings, and `$this->line()` for plain text output.

## How to build 3 practical maintenance commands

Here are some examples that help you tackle database maintenance tasks that come up for lots of WordPress websites.

While each command includes error handling and largely follows WordPress coding standards to keep your data safe, you should still use these as a skeleton for your own projects rather than simply copy-paste them.

### 1. Cleaning orphaned post metadata

[Post metadata](https://kinsta.com/blog/last-updated/) sticks around after you delete posts. This happens when plugins bypass WordPress’s deletion hooks and leave metadata entries pointing to posts that no longer exist. Over time, this bloat slows down your database queries.

Once you create the command with `wp acorn make:command CleanupOrphanedMeta`, you can start with the command class structure and signature:

```
<?php
namespace App\Console\Commands;
use Illuminate\Console\Command;
class CleanupOrphanedMeta extends Command
{
    protected $signature = 'maintenance:cleanup-orphaned-meta 
                            {--dry-run : Preview orphans without deleting}';
    
    protected $description = 'Remove orphaned post metadata from wp_postmeta';
    public function handle()
    {
        global $wpdb;

        $dryRun = $this->option('dry-run');

        $this->components->info('Scanning for orphaned post metadata...');
```

The command uses a `LEFT JOIN` query to find these orphaned records. The pattern checks for `NULL` values in the posts table. If the join returns `NULL` the metadata belongs to a deleted post:

```
        // Find orphaned metadata
        $orphans = $wpdb->get_results("
            SELECT pm.meta_id, pm.post_id, pm.meta_key 
            FROM {$wpdb->postmeta} pm
            LEFT JOIN {$wpdb->posts} p ON pm.post_id = p.ID
            WHERE p.ID IS NULL
            LIMIT 1000
        ");

        if (empty($orphans)) {
            $this->components->info('No orphaned metadata found');
            return 0;
        }
```

When the command finds orphans, it shows you a count and samples a few records if you’re in dry-run mode. You need to verify what’s getting deleted before you commit:

```
        $count = count($orphans);
        $this->components->warn("Found {$count} orphaned metadata records");
        if ($dryRun) {
            $this->newLine();
            $this->line('Sample orphaned records:');

            foreach (array_slice($orphans, 0, 5) as $orphan) {
                $this->line("  → Post ID {$orphan->post_id}: {$orphan->meta_key}");
            }

            return 0;
        }
```

The actual deletion uses `$wpdb->prepare()` to avoid [SQL injection](https://kinsta.com/blog/sql-injection/) attacks. The command processes 1,000 records at a time, which prevents memory problems on sites with millions of metadata entries:

```
        // Delete orphaned records
        $metaIds = array_map(function($orphan) {
            return $orphan->meta_id;
        }, $orphans);

        $placeholders = implode(',', array_fill(0, count($metaIds), '%d'));

        $deleted = $wpdb->query(
            $wpdb->prepare(
                "DELETE FROM {$wpdb->postmeta} WHERE meta_id IN ({$placeholders})",
                ...$metaIds
            )
        );

        if ($deleted === false) {
            $this->components->error('Failed to delete orphaned metadata');
            return 1;
        }

        $this->components->info("Deleted {$deleted} orphaned metadata records");
        return 0;
    }
}
```

To run the command, use `wp acorn maintenance:cleanup-orphaned-meta --dry-run`.

### 2. Deleting expired transients

WordPress stores [transients](https://developer.wordpress.org/apis/transients/) in `wp_options` with expiration dates. While a daily [cron job](https://kinsta.com/blog/wordpress-cron-job/) cleans these up, you sometimes need to run a manual cleanup during maintenance windows or when transient bloat becomes a problem.

After you generate the command with `wp acorn make:command CleanupTransients`, you can set up the command structure:

```
<?php
namespace App\Console\Commands;
use Illuminate\Console\Command;
class CleanupTransients extends Command
{
    protected $signature = 'maintenance:cleanup-transients';
    protected $description = 'Delete expired transients from wp_options';
    public function handle()
    {
        global $wpdb;

        $this->components->info('Deleting expired transients...');
```

This deletion query uses multi-table `DELETE` syntax to remove both the transient and its timeout option at once. The query finds timeout records where the expiration timestamp has passed:

```
        // Delete expired regular transients
        $deleted = $wpdb->query(
            $wpdb->prepare(
                "DELETE a, b FROM {$wpdb->options} a, {$wpdb->options} b
                WHERE a.option_name LIKE %s
                AND a.option_name NOT LIKE %s
                AND b.option_name = CONCAT('_transient_timeout_', SUBSTRING(a.option_name, 12))
                AND b.option_value < %d",
                $wpdb->esc_like('_transient_') . '%',
                $wpdb->esc_like('_transient_timeout_') . '%',
                time()
            )
        );
```

Also check for errors and track the deletion count:

```
        if ($deleted === false) {
            $this->components->error('Failed to delete transients');
            return 1;
        }

        $transientCount = $deleted;
```

On [Multisite installations](https://kinsta.com/blog/wordpress-multisite/), the command runs a second query for site transients. These use different table prefixes but follow the same deletion pattern:

```
        // Delete expired site transients (multisite)
        if (is_multisite()) {
            $siteDeleted = $wpdb->query(
                $wpdb->prepare(
                    "DELETE a, b FROM {$wpdb->options} a, {$wpdb->options} b
                    WHERE a.option_name LIKE %s
                    AND a.option_name NOT LIKE %s
                    AND b.option_name = CONCAT('_site_transient_timeout_', SUBSTRING(a.option_name, 17))
                    AND b.option_value < %d",
                    $wpdb->esc_like('_site_transient_') . '%',
                    $wpdb->esc_like('_site_transient_timeout_') . '%',
                    time()
                )
            );

            if ($siteDeleted !== false) {
                $transientCount += $siteDeleted;
            }
        }

        $this->components->info("Deleted {$transientCount} expired transients");

        return 0;
    }
}
```

To execute the command, run `wp acorn maintenance:cleanup-transients`.

### 3. Auditing autoloaded options

[Autoloaded options](https://kinsta.com/blog/wp-options-autoloaded-data/) load on every request your WordPress site handles. You can start to see slowdowns and memory consumption spikes when this data crosses 1MB. This command finds your largest autoloaded options so you can track down which plugins cause the bloat.

First, create the audit command with `wp acorn make:command AuditAutoload`. Then, define the command signature with a configurable threshold:

```
<?php
namespace App\Console\Commands;
use Illuminate\Console\Command;
class AuditAutoload extends Command
{
    protected $signature = 'maintenance:audit-autoload 
                            {--threshold=1000000 : Size threshold in bytes}';

    protected $description = 'Audit autoloaded options size';
    public function handle()
    {
        global $wpdb;

        $threshold = (int) $this->option('threshold');

        $this->components->info('Calculating autoloaded options size...');
```

From here, calculate the total size of all autoloaded options:

```
        // Get total autoload size
        $result = $wpdb->get_row(
            "SELECT 
                SUM(LENGTH(option_value)) as total_bytes,
                COUNT(*) as total_count
            FROM {$wpdb->options}
            WHERE autoload = 'yes'"
        );

        $totalBytes = (int) $result->total_bytes;
        $totalCount = (int) $result->total_count;
        $totalMb = round($totalBytes / 1024 / 1024, 2);

        $this->newLine();
        $this->line("Total autoloaded: {$totalMb} MB ({$totalCount} options)");
```

The command runs a query for options above your threshold, sorts them by size, and limits results to the biggest 20:

```
        // Get largest autoloaded options
        $largeOptions = $wpdb->get_results(
            $wpdb->prepare(
                "SELECT option_name, LENGTH(option_value) as size_bytes
                FROM {$wpdb->options}
                WHERE autoload = 'yes'
                AND LENGTH(option_value) > %d
                ORDER BY size_bytes DESC
                LIMIT 20",
                $threshold
            )
        );

        if (empty($largeOptions)) {
            $this->components->info('No options exceed the threshold');
            return 0;
        }
```

Artisan’s `$this->table()` method formats these results as an ASCII table: reading tabular data in your terminal beats parsing the raw query output:

```
        $this->newLine();
        $this->components->warn('Large autoloaded options:');
        $this->newLine();

        $tableData = [];

        foreach ($largeOptions as $option) {
            $sizeKb = round($option->size_bytes / 1024, 2);
            $tableData[] = [
                $option->option_name,
                $sizeKb . ' KB'
            ];
        }

        $this->table(
            ['Option Name', 'Size'],
            $tableData
        );
```

The command throws a warning when the total autoload crosses 3MB, which indicates a performance problem you need to address:

```
        if ($totalBytes > 3000000) {
            $this->newLine();
            $this->components->error('Warning: Total autoload exceeds 3MB');
        }

        return 0;
    }
}
```

To run the audit, use `wp acorn maintenance:audit-autoload --threshold=500000`.

## How to access WordPress data within commands

WordPress functions work inside your command methods because Acorn boots within WordPress’s lifecycle. This means you can call some functions such as `get_posts()` or `get_option()` without any special setup:

```
public function handle()
{
    $posts = get_posts([
        'post_type' => 'post',
        'post_status' => 'publish',
        'numberposts' => 10,
    ]);

    foreach ($posts as $post) {
        $this->line($post->post_title);
    }

    return 0;
}
```

For direct database queries, declare the `$wpdb` global at the start of your method:

```
public function handle()
{
    global $wpdb;   

    $count = $wpdb->get_var(
        "SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_status = 'publish'"
    );

    $this->line("Published posts: {$count}");

    return 0;
}
```

`$wpdb->prepare()` is ideal whenever your queries include variables or user input as it helps to prevent SQL injection attacks:

```
$status = 'publish';
$postType = 'post';
$results = $wpdb->get_results(
    $wpdb->prepare(
        "SELECT ID, post_title FROM {$wpdb->posts} 
        WHERE post_status = %s AND post_type = %s",
        $status,
        $postType
    )
);
```

If you test for `false` after any database operations, this should let you catch errors:

```
$updated = $wpdb->update(
    $wpdb->posts,
    ['post_status' => 'draft'],
    ['ID' => 123],
    ['%s'],
    ['%d']
);

if ($updated === false) {
    $this->components->error('Database update failed');
    return 1;
}
```

[Custom post types](https://kinsta.com/blog/wordpress-custom-post-types/) and taxonomies work through standard WordPress functions:

```
$terms = get_terms([
    'taxonomy' => 'category',
    'hide_empty' => false,
]);

foreach ($terms as $term) {
    wp_update_term($term->term_id, 'category', [
        'description' => 'Updated via command',
    ]);
}
```

## Custom WP-CLI commands are straightforward with Acorn and Artisan Console

[Acorn](https://roots.io/acorn/) lets you access Laravel’s structured command classes, formatted output components, proper error handling, and more, while giving you full access to WordPress’ functions and data.

You can integrate commands through SSH access and cron scheduling within Kinsta. You can also add commands to your deployment scripts to automate maintenance, for instance using [GitHub Actions](https://kinsta.com/blog/github-actions-secret/) workflows.

If you’re ready to centralize your WordPress maintenance tasks with custom WP-CLI commands, [Kinsta’s managed WordPress hosting](https://kinsta.com/wordpress-hosting/) includes SSH access and WP-CLI on all plans.

Joel Olawanle
[Kinsta](https://kinsta.com/)

Joel is a Frontend developer working at Kinsta as a Technical Editor. He is a passionate teacher with love for open source and has written over 300 technical articles majorly around JavaScript and it's frameworks.

- [Website](https://joelolawanle.com/)
- [LinkedIn](https://www.linkedin.com/in/olawanlejoel/)
- [Twitter](https://twitter.com/olawanle_joel)
- [YouTube](https://www.youtube.com/@joelolawanle)
