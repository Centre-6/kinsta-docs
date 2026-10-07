---
url: "https://kinsta.com/blog/blade-templating-wordpress-radicle/"
title: "Blade templating in WordPress: modern template development with Radicle on Kinsta"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "WordPress Development", "Blade templating in WordPress: modern template development with Radicle on Kinsta"]
kinsta_last_updated: "2026-05-20T20:31:13+00:00"
sitemap_lastmod: "2026-05-20T20:31:13"
fetched_at: "2026-10-07T22:41:27Z"
sha256: "93ae050d8eb59900a25c41605c3987718c2fe2274fab2476e54fc91a99e3c547"
body_chars: 16736
extracted_with: "main article"
status: "live"
---

# Blade templating in WordPress: modern template development with Radicle on Kinsta

**Section:** Resource Center > Blog > WordPress Development > Blade templating in WordPress: modern template development with Radicle on Kinsta
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/blade-templating-wordpress-radicle/
**Kinsta last updated:** 2026-05-20T20:31:13+00:00

## On this page

- [Why WordPress template development needs component-based architecture](#why-wordpress-template-development-needs-component-based-architecture)
- [How to build primary layouts that eliminate duplicate code](#how-to-build-primary-layouts-that-eliminate-duplicate-code)
- [Creating reusable UI components for consistent design patterns](#creating-reusable-ui-components-for-consistent-design-patterns)
- [Connecting WordPress data to Blade templates with view composers](#connecting-wordpress-data-to-blade-templates-with-view-composers)
- [Building Blocks for the WordPress Site Editor with Blade rendering](#building-blocks-for-the-wordpress-site-editor-with-blade-rendering)
- [How Kinsta’s caching boosts Blade’s compiled view performance](#how-kinstas-caching-boosts-blades-compiled-view-performance)
- [Modern WordPress theme development includes Radicle and Kinsta](#modern-wordpress-theme-development-includes-radicle-and-kinsta)

---

Author
:   [Joel Olawanle](https://kinsta.com/blog/author/joelolawanle/ "Posts by Joel Olawanle")

Updated
:   May 20, 2026

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![](https://kinsta.com/wp-content/uploads/2026/01/blade-templating-in-wordpress-modern-template-development-with-radicle-on-kinsta-1024x512.png)

Traditional WordPress theme development relies on repeating header and footer markup across template files. Each time you update a navigation menu or footer element, you need to locate every template file that includes the markup and make the necessary changes in multiple locations. This creates maintenance overheads and increases the risk of inconsistencies across your site.

[Radicle](https://roots.io/radicle/) brings [Laravel’s Blade templating engine](https://kinsta.com/blog/laravel-blade/) to WordPress through [Acorn’s](https://roots.io/acorn/) component-based architecture. Instead of scattering markup across template files, you define reusable components once and reference them throughout your theme. When you need to update a UI element, you modify a single component file rather than hunting through dozens of templates.

## Why WordPress template development needs component-based architecture

WordPress stores templates in a theme directory structure where `header.php` and `footer.php` appear in every page template through `get_header()` and `get_footer()` calls. This works for basic sites but causes problems when scaling across complex projects.

For example, a site with [custom post types](https://kinsta.com/blog/wordpress-custom-post-types/), landing pages, and marketing templates includes the same navigation markup, footer structure, and sidebar elements in each template file. This requires you to search through multiple template files to add a new menu item or update a contact form in the footer.

Radicle organizes Blade templates in `resources/views/` with separate directories for layouts, components, and Blocks:

- `components`. This directory includes self-contained UI elements such as headings and buttons.
- `layouts`. This holds structural templates that define page scaffolding.
- `blocks.` You store [Block templates](https://kinsta.com/blog/wordpress-block-themes/) that integrate with the WordPress Site Editor here.

This organization creates a single source of truth for each UI element. An `x-heading` component defines heading markup and styling in one location. So, when you use this component across templates, Blade references the single definition. By extension, updating the component updates every instance across your site.

## How to build primary layouts that eliminate duplicate code

Instead of duplicating navigation and footer markup, you can use template inheritance to create a parent layout that defines the site shell.

A layout starts with a Blade component file in `resources/views/components/`. The `layout.blade.php` file defines the HTML structure that wraps the page content. This includes the `doctype`, head section with meta tags and asset references, navigation structure, and footer elements. The key element in a layout is the `$slot` variable, which Blade uses as the content injection point.

```
<html>
<head>
    <title>{{ $title ?? 'My Site' }}</title>
</head>

<body>
    <nav>
        <!-- Navigation markup -->
    </nav>

    <main>
        {{ $slot }}
    </main>

    <footer>
        <!-- Footer markup -->
    </footer>

</body>
</html>
```

Child templates extend this layout using Blade’s component syntax. A page template wraps its content in the `x-layout` component tags. Blade processes this by rendering the layout component and injecting the child content where the `$slot` variable appears:

```
<x-layout>
    <h1>Page Title</h1>
    <p>Page content goes here.</p>
</x-layout>
```

Named slots provide additional injection points for dynamic content (such as page titles). Instead of accepting a default slot, you define specific slots with names. The `x-slot` component with a `name` attribute passes content to these designated locations:

```
<x-layout>
    <x-slot name="title">
        Custom Page Title
    </x-slot>

    <h1>Page Heading</h1>
    <p>Page content.</p>
</x-layout>
```

The layout component accesses named slots through variables that match the slot names. This lets you inject content into multiple layout locations from a single child template.

## Creating reusable UI components for consistent design patterns

Blade components centralize styling and markup for common interface elements.

Instead of writing button markup with [Tailwind classes](https://kinsta.com/blog/tailwind-css/) in every template, you create a button component that encapsulates the markup. The component accepts ‘props’ for customization while maintaining consistent base styling.

Using the `x-heading` component with other typography components is a good example of this. It accepts a `level` prop that determines the HTML element (`h1`, `h2`, `h3`) and a `size` prop that controls the visual scale. The component maps these props to Tailwind classes internally, which keeps the implementation details separate.

```
<x-heading level="h1" size="3xl">
    Main Page Title
</x-heading>

<x-heading level="h2" size="2xl">
    Section Heading
</x-heading>
```

The component file in `resources/views/components/heading.blade.php` defines the markup and styling logic using Blade’s `@props` directive to define accepted properties and their defaults. Each component constructs the appropriate HTML element with classes based on the prop values.

An `x-link` component follows the same pattern with variant support for different link styles, and a variant prop switches between default, button, and unstyled presentations.

UI components such as `x-button` let you achieve the same with interactive elements. The `button` component supports size and variant props for different button styles. When you combine it with a framework such as [Alpine.js](https://alpinejs.dev/) through the `x-modal` component, you can handle interactions without scattering JavaScript across templates:

```
<x-button variant="primary" @click="showModal = true">
    Open Modal
</x-button>

<x-modal x-show="showModal">
    <p>Modal content</p>
</x-modal>
```

Props work well for strings, booleans, and other simple data. Slots serve better for complex content that includes markup. For example, the `modal` component uses a default slot to accept the full modal content rather than passing HTML through a prop.

## Connecting WordPress data to Blade templates with view composers

View composers let you aggregate data from multiple sources before rendering a template. Here, you create a `composer` class that handles data retrieval and transformation rather than querying posts directly in templates. Instead, the template receives structured data to display.

Radicle’s `Post` model simplifies working with WordPress post data using a few different methods:

- `title()` returns the post title.
- The `content()` method retrieves filtered post content.
- `excerpt()` accepts a word count and generates an excerpt.
- `permalink()` returns the post URL.

For featured images, `hasThumbnail()` checks whether an image exists, and `thumbnail()` retrieves the image HTML with a specified size:

```
$post = Post::find(123);
echo $post->title();
echo $post->excerpt(30);
if ($post->hasThumbnail()) {
    echo $post->thumbnail('large');
}
```

View composer classes live in `app/View/Composers/` and extends `Roots\Acorn\View\Composer`. The class defines which views it applies to through the protected static `$views` property, which accepts an array of template names. For a front page composer, you specify `'front-page'` to target the `front-page.blade.php` template:

```
namespace App\View\Composers;
use App\Models\Post;
use Roots\Acorn\View\Composer;
class FrontPage extends Composer

{
    protected static $views = ['front-page'];
    public function with()
    {
        return [
            'recentPosts' => Post::recent(6)->get(),
            'totalPosts' => Post::published()->count(),
        ];
    }
}
```

The `with()` method returns an array where keys become variable names in the template. The values can be [Eloquent collections](https://laravel.com/docs/11.x/eloquent-collections), individual models, or any data structure. Regardless, this method runs before any template renders and prepares the data.

The `front-page.blade.php` template accesses these variables directly. Blade’s `@foreach` directive loops through posts, and each iteration provides access to the `Post` model methods:

```
<div class="posts-grid">
    @foreach ($recentPosts as $post)
        <article>
            @if ($post->hasThumbnail())
                <img src="{{ $post->thumbnail('medium') }}" alt="{{ $post->title() }}">
            @endif

            <h2>
                <a href="{{ $post->permalink() }}">{{ $post->title() }}</a>
            </h2>

            <p>{{ $post->excerpt(20) }}</p>
        </article>
    @endforeach
</div>
<p>Total posts: {{ $totalPosts }}</p>
```

In this pattern, the composer handles querying and data transformation while the template focuses on markup and display logic. When you need to modify the data structure or add new queries, you update the composer without touching template files.

## Building Blocks for the WordPress Site Editor with Blade rendering

Radicle uses server-side rendering for Site Editor Blocks through Blade templates. The JavaScript editor component handles the Block interface in the WordPress admin, and the Blade template handles the frontend output.

This lets you build Block interfaces with React (for instance) while rendering production HTML with Blade.

The `wp acorn make:block` command generates three files for each Block:

- A PHP class in `app/Blocks/` manages server-side logic.
- The JSX component in `resources/js/editor/` defines the block editor interface.
- Blade templates in `resources/views/blocks/` renders the frontend output.

A `wp acorn make:block latest-posts` command creates `LatestPosts.php`, `latest-posts.block.jsx`, and `latest-posts.blade.php`. The JSX file defines the Block’s attributes and editor controls while the dynamic blocks use `InspectorControls` to add settings in the Block sidebar. You import controls from `@wordpress/components` and compose them into a settings interface.

```
import { InspectorControls } from '@wordpress/block-editor';
import { RangeControl, ToggleControl, RadioControl } from '@wordpress/components';
export const attributes = {
    posts: { type: 'number', default: 5 },
    displayFeaturedImage: { type: 'boolean', default: false },
    postLayout: { type: 'string', default: 'list' },
};

export const edit = ({ attributes, setAttributes }) => {
    return (
        <>
            <InspectorControls>
                <RangeControl
                    label="Number of posts"
                    value={attributes.posts}
                    onChange={(value) => setAttributes({ posts: value })}
                    min={1}
                    max={10}
                />
                <ToggleControl
                    label="Display featured image"
                    checked={attributes.displayFeaturedImage}
                    onChange={(value) => setAttributes({ displayFeaturedImage: value })}
                />
                <RadioControl
                    label="Layout"
                    selected={attributes.postLayout}
                    options={[
                        { label: 'List', value: 'list' },
                        { label: 'Grid', value: 'grid' },
                    ]}
                    onChange={(value) => setAttributes({ postLayout: value })}
                />
            </InspectorControls>
        </>
    );
};
```

The `render_block` filter in `BlocksServiceProvider.php` intercepts Block rendering and passes attributes to the Blade template. It also receives the Block content and Block data. You check the Block name, query necessary data, and return the rendered Blade view:

```
add_filter('render_block', function ($block_content, $block) {
    if ($block['blockName'] === 'radicle/latest-posts') {
        $attributes = $block['attrs'] ?? [];

        $posts = get_posts([
            'numberposts' => $attributes['posts'] ?? 5,
            'post_status' => 'publish',
        ]);

        return view('blocks.latest-posts', [
            'posts' => $posts,
            'displayFeaturedImage' => $attributes['displayFeaturedImage'] ?? false,
            'postLayout' => $attributes['postLayout'] ?? 'list',
        ]);
    }

    return $block_content;
}, 10, 2);
```

The Blade template uses PHP arrays to manage conditional layouts. Here, you define layout configurations as nested arrays that map layout names to CSS classes and HTML elements.

```
@php
$layoutConfig = [
    'grid' => [
        'container' => 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6',
        'element' => 'div',
    ],
    'list' => [
        'container' => 'space-y-6',
        'element' => 'div',
    ],
];
$config = $layoutConfig[$postLayout];
@endphp
<div class="{{ $config['container'] }}">
    @foreach ($posts as $post)
        <article>
            @if ($displayFeaturedImage && has_post_thumbnail($post))
                {{ get_the_post_thumbnail($post, 'medium') }}
            @endif

            <h3>{{ $post->post_title }}</h3>
        </article>
    @endforeach
</div>
```

This pattern creates flexible blocks where editor controls adjust the frontend output without duplicating template logic: JavaScript handles the user interface, PHP handles data queries, and Blade handles markup structure.

## How Kinsta’s caching boosts Blade’s compiled view performance

Blade compilation essentially converts `.blade.php` templates to plain PHP code. After Blade completes a complete parse of the template and Blade syntax, it stores a compiled file in `storage/framework/views/`. This compilation happens once per template change rather than on every page load, but subsequent requests skip the compilation and executes cached PHP.

The process transforms Blade directives into PHP functions. For instance, the `@foreach` directive becomes a `foreach` loop; the `{{ $variable }}` syntax becomes an `echo` statement with escaping.

Kinsta’s server-level caching (both [edge caching](https://kinsta.com/blog/edge-caching/) and [Redis object caching](https://kinsta.com/docs/wordpress-hosting/caching/redis-cache/)) work alongside Blade’s compilation cache to create multiple performance tiers. Blade’s compiled views sit between these layers, which provide template execution times that benefit from both upstream caching and downstream optimization.

During deployment, Blade clears the cache when you push template changes to staging or production environments. Although Blade detects template modifications during development, your deployment processes should include clearing the view cache through running `php artisan view:clear` or `wp acorn view:clear` within your deployment script.

## Modern WordPress theme development includes Radicle and Kinsta

The combination of Radicle’s Laravel-inspired structure and [Kinsta’s managed hosting infrastructure](https://kinsta.com/wordpress-hosting/) gives you a foundation for scaling WordPress projects. Agencies that manage multiple client sites can harness consistent component patterns across projects. For developers, you can work with familiar Laravel conventions while maintaining compatibility with WordPress.

Your next step depends on your current setup. If you’re starting fresh, begin by installing Radicle and creating your first Blade component. If you’re migrating an existing theme, identify repetitive markup patterns and convert them to components one section at a time. Focus on high-value areas such as navigation, headers, and footers where component benefits are immediate.

If you need managed WordPress hosting that supports modern development workflows, [Kinsta offers functionality](https://kinsta.com/wordpress-hosting/) that works with tools such as Radicle and Acorn.

Joel Olawanle
[Kinsta](https://kinsta.com/)

Joel is a Frontend developer working at Kinsta as a Technical Editor. He is a passionate teacher with love for open source and has written over 300 technical articles majorly around JavaScript and it's frameworks.

- [Website](https://joelolawanle.com/)
- [LinkedIn](https://www.linkedin.com/in/olawanlejoel/)
- [Twitter](https://twitter.com/olawanle_joel)
- [YouTube](https://www.youtube.com/@joelolawanle)
