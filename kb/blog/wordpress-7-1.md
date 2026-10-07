---
url: "https://kinsta.com/blog/wordpress-7-1/"
title: "What\u2019s new in WordPress 7.1: Client-side media processing, design tools, Abilities API, and much more"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: []
kinsta_last_updated: "2026-08-07T17:08:42"
change_signal: "2026-08-07T17:08:42"
fetched_at: "2026-10-07T22:58:24Z"
sha256: "e2bd0a23e3fbb10684c5610ef80f61d60892b0a51db606ba583b925120d68166"
body_chars: 41868
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# What’s new in WordPress 7.1: Client-side media processing, design tools, Abilities API, and much more

**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/wordpress-7-1/
**Kinsta last updated:** 2026-08-07T17:08:42

## On this page

- [Client-side media processing](#client-side-media-processing)
  - [1. What is Client-Side Media Processing?](#1-what-is-client-side-media-processing)
  - [2. What are the technical features of Client-Side Media Processing?](#2-what-are-the-technical-features-of-client-side-media-processing)
  - [3. What are the benefits for WordPress users?](#3-what-are-the-benefits-for-wordpress-users)
  - [4. What changes for developers?](#4-what-changes-for-developers)
  - [5. What are the benefits for security?](#5-what-are-the-benefits-for-security)
  - [6. Official resources](#6-official-resources)
- [Enhancements for Notes](#enhancements-for-notes)
- [Admin UI improvements](#admin-ui-improvements)
  - [Persistent admin bar in the post and Site Editor](#persistent-admin-bar-in-the-post-and-site-editor)
  - [User’s color scheme extended to the Site Editor](#users-color-scheme-extended-to-the-site-editor)
  - [Command categories and improved command palette UI](#command-categories-and-improved-command-palette-ui)
  - [Identity screen in the Site Editor](#identity-screen-in-the-site-editor)
  - [Infinite Scrolling for the Media Library grid view](#infinite-scrolling-for-the-media-library-grid-view)
- [Core blocks and block improvements](#core-blocks-and-block-improvements)
  - [New Playlist and Tabs Blocks](#new-playlist-and-tabs-blocks)
  - [Editable blocks inside the Custom HTML block](#editable-blocks-inside-the-custom-html-block)
- [Improvements to the SVG icon system](#improvements-to-the-svg-icon-system)
  - [Registering and unregistering icons](#registering-and-unregistering-icons)
  - [Icon library and block updates](#icon-library-and-block-updates)
  - [New REST API endpoints for icons](#new-rest-api-endpoints-for-icons)
- [New design tools](#new-design-tools)
  - [Background gradient support](#background-gradient-support)
  - [Minimum width support](#minimum-width-support)
  - [Text shadow support in Global Styles](#text-shadow-support-in-global-styles)
- [Updates for developers](#updates-for-developers)
  - [Design system theming](#design-system-theming)
    - [Design tokens](#design-tokens)
    - [ThemeProvider](#themeprovider)
  - [Enhancements to the Abilities API](#enhancements-to-the-abilities-api)
    - [New execution lifecycle for the Abilities API](#new-execution-lifecycle-for-the-abilities-api)
    - [Filtering and manipulating abilities](#filtering-and-manipulating-abilities)
    - [New public exposure flag](#new-public-exposure-flag)
    - [Other improvements to the Abilities API](#other-improvements-to-the-abilities-api)
  - [More updates for developers](#more-updates-for-developers)
- [Next-gen hosting for next-gen WordPress](#next-gen-hosting-for-next-gen-wordpress)

---

WordPress 7.1 is scheduled for release on August 19th and promises to be an exciting update for developers, professionals, agencies, and bloggers across the ecosystem.

This second major release of the year introduces a wide range of updates covering nearly every aspect of the CMS. Among the new features, Client-Side Media Processing is the one we are most excited about. The reason is that here at Kinsta, we are obsessed with web performance and site speed, and this new media architecture marks a significant step forward—delivering noticeable improvements in server efficiency and faster page load times.

Beyond media handling, [WordPress 7.1](https://make.wordpress.org/core/2026/08/05/wordpress-7-1-field-guide/) brings notable enhancements to team collaboration, including new Notes features, as well as several UI refinements in the admin dashboard—such as a persistent admin bar and the new Identity screen in the Site Editor. The release includes new and upgraded blocks, expanded design tools, and a broad array of updates for developers.

Want to explore what’s coming next? Let’s dive into WordPress 7.1.

## Client-side media processing

Up until WordPress 7.0, generating image dimensions and thumbnails for display on the frontend, converting formats, and managing image rotation was all handled server-side via PHP.

Now, WordPress 7.1 introduces a new media processing architecture: image resizing, format conversion, EXIF rotation, and thumbnail generation now happen client-side, directly in the user’s browser.

This change should significantly improve site performance and reduce server resource consumption.

Let’s take a closer look at what changes in image processing:

### 1. What is Client-Side Media Processing?

While images were previously processed on the server by PHP using [GD](https://libgd.github.io/) or [Imagick](https://www.php.net/manual/en/book.imagick.php) libraries, image generation for various sizes, format conversion, and EXIF rotation now occur directly in the user’s browser—provided the browser supports the `Document-Isolation-Policy` (DIP) header to grant access to `SharedArrayBuffer`.

Because processing happens in the browser, WordPress no longer receives just a single image, but all the resulting image files from the processing pipeline. This has two main effects: lower server CPU and RAM usage, and more HTTP requests to upload the individual thumbnails.

At the time of this writing, only Chrome 137+ and Microsoft Edge 137+ (desktop) fully support the `Document-Isolation-Policy`. Safari and Firefox do not support the WASM pipeline, although Safari supports native decoding of [HEIC/HEIF](https://kinsta.com/blog/wordpress-6-7/#heic-format-support) formats to JPG.

![Client-Side Media Processing upload flow diagram](https://kinsta.com/wp-content/uploads/2026/08/wp-71-client-side-media-upload-flow.png)

Client-Side Media Processing upload flow (Image source: [WordPress.org](https://developer.wordpress.org/block-editor/explanations/architecture/client-side-media-architecture/))

### 2. What are the technical features of Client-Side Media Processing?

From an architectural standpoint, Client-Side Media Processing is managed through 3 core packages:

- The new `@wordpress/vips` package handles client-side processing using the [`libvips` library](https://www.libvips.org/) compiled into WebAssembly (`wasm-vips`). Widely considered one of the fastest and most efficient image processing libraries available, it runs in parallel inside a Web Worker—preventing the user interface from freezing and delivering significantly better performance than pure JavaScript.
- The `@wordpress/upload-media` package orchestrates the upload pipeline, including managing upload queues, upload concurrency (up to 5 concurrent uploads and 2 image processing operations), automatic retries, resuming interrupted uploads, and offline support.
- The `@wordpress/media-utils` package handles HTTP transport and REST API requests.

![WordPress 7.1 Client-Side Media Processing architecture diagram](https://kinsta.com/wp-content/uploads/2026/08/wp-71-client-side-media-processing-architecture-overview.png)

Client-Side Media Processing architecture overview (Image source: [WordPress.org](https://make.wordpress.org/core/2026/07/22/client-side-media-processing-in-wordpress-7-1/))

In addition to image processing, this new feature introduces automatic conversion of animated GIFs into MP4/WebM videos. The conversion is handled by the new `@wordpress/video-conversion` package, which wraps the [`mediabunny` library](https://mediabunny.dev/) in a Web Worker to convert opaque GIFs (without transparent backgrounds) into lightweight video files.

Client-Side Media Processing also introduces new REST API endpoints (`sideload`, `finalize`, and `replace_file`) along with 2 new parameters: `generate_sub_sizes` and `convert_format`.

### 3. What are the benefits for WordPress users?

Client-Side Media Processing offloads image processing from the server to the client. This frees the server from the heavy workload of generating thumbnails in various dimensions, rotating images, and converting formats, shifting that work directly to the user’s browser.

Here are some of the benefits of offloading media processing to the client for users:

- **Fewer PHP out-of-memory errors:** Client-Side Media Processing eliminates memory-exhaustion errors (`PHP memory limit exceeded`) that previously occurred when processing large image files.
- **Lower CPU and RAM consumption:** Another major win for the server is a substantial reduction in host CPU and RAM usage, freeing up resources for other tasks.
- **Better site performance:** The `libvips` library uses advanced compression algorithms that produce images that are, on average, ~15% smaller than those generated by GD or Imagick. This results in lighter images and faster page load times.
- **Greater upload resilience:** Each image upload requires an independent HTTP request. This leads to a higher volume of HTTP requests but ensures that every image is processed independently. Failed requests are automatically paused and retried.

Furthermore, animated GIFs can be automatically converted into more efficient autoplay videos, HEIC photos uploaded from iPhones can be converted to JPG by the browser before upload (bypassing potential server compatibility issues), and AVIF support now works even without server-side AVIF capabilities (the MIME-type check is bypassed for client-decoded uploads).

### 4. What changes for developers?

Developers can turn off client-side media processing using the new `wp_client_side_media_processing_enabled` filter. Here is an example:

```
add_filter( 'wp_client_side_media_processing_enabled', '__return_false' );
```

Beyond this, there are no major disruptions for plugin developers. Hooks associated with media processing continue to fire just as if the images were processed on the server.

Existing filters read settings from the server and continue to work as expected. For instance, the `wp_generate_attachment_metadata` filter runs twice: first during the initial upload (`create`) and a second time after the finalization endpoint is called (`update`). Plugins using this filter will continue to work as expected.

For theme developers, image sizes registered via `add_image_size()` are now generated client-side. If a theme defines an image size with dimensions identical to a default WordPress size, the images are “deduplicated” into a single image file registered under both size names.

### 5. What are the benefits for security?

Although Client-Side Media Processing is primarily designed for performance and efficiency rather than security, it offers several advantages that enhance WordPress site security.

First, it reduces the attack surface. As mentioned earlier, before WordPress 7.1, image processing relied on server-side libraries such as GD and Imagick. Over time, these libraries have been affected by various security vulnerabilities connected to image decoding.

With client-side image processing, the server no longer needs GD or Imagick because it receives preprocessed images. This significantly decreases the amount of sensitive code executed on the server.

Another security advantage is that image processing occurs within an isolated browser environment, using WebAssembly in a Web Worker.

Client-side processing also reduces the risk of Denial-of-Service (DoS) attacks, as the computational load is on the client.

To process images on the client, WordPress relies on [`SharedArrayBuffer`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer), a JavaScript object that allows the main thread and Web Workers to share the same memory space.

To grant access to `SharedArrayBuffer`, WordPress enables the `Document-Isolation-Policy: isolate-and-credentialless` [header](https://chromestatus.com/feature/5141940204208128). This provides an isolated execution context for the block editor in Chromium 137+ browsers (Chrome 137+ and Edge 137+).

In short, while the primary goal of Client-Side Media Processing is to improve performance and efficiency in media handling, this new feature also brings notable security enhancements.

### 6. Official resources

Client-Side Media Processing has been extensively documented for both users and developers. Check out the following resources for the details:

- Client-Side Media Processing in WordPress 7.1 ([dev note](https://make.wordpress.org/core/2026/07/22/client-side-media-processing-in-wordpress-7-1/))
- Client-Side Media Processing architecture ([Block Editor Handbook](https://developer.wordpress.org/block-editor/explanations/architecture/client-side-media-architecture/))
- Client-Side Media Processing ([How-to Guides](https://developer.wordpress.org/block-editor/how-to-guides/client-side-media/))
- Client-side media processing filters and parameters ([Hooks reference](https://developer.wordpress.org/block-editor/reference-guides/filters/editor-filters/#client-side-media-processing))

## Enhancements for Notes

First introduced in [WordPress 6.9](https://kinsta.com/blog/wordpress-6-9/#commenting-blocks-with-notes-in-wordpress-69), Notes have received numerous additions and improvements that make it a more complete collaboration tool.

First off, WordPress 7.1 adds [support for rich text in Notes](https://github.com/WordPress/gutenberg/issues/73413), making them “more expressive, clearer to read, and more aligned with user expectations from tools like Google Docs, Figma, GitHub, and other collaborative editors.”

This includes basic inline formatting such as bold (Ctrl/⌘ + B), italics (Ctrl/⌘ + I), links (Ctrl/⌘ + K), and emojis.

![Notes formatting options in WordPress 7.1](https://kinsta.com/wp-content/uploads/2026/07/wp-71-notes-formatting-options.png)

Notes now feature basic formatting options

Now you can add inline notes by selecting text fragments instead of just an entire block ([inline block commenting](https://github.com/WordPress/gutenberg/issues/59445)). It is also possible to add [multiple notes](https://github.com/WordPress/gutenberg/issues/75145) to the same block or text selection.

WordPress 7.1 also introduces [@mentions](https://github.com/WordPress/gutenberg/issues/73415) to tag your collaborators in notes, making the Notes functionality more similar to popular collaboration tools. When you type the @ character, a panel appears with a list of your site’s users for easy selection. The recipient of the mention will receive an email notification with a link back to the post.

Another addition concerns the visible portion of the notes. Long notes now [collapse by default](https://github.com/WordPress/gutenberg/issues/72822) so they don’t clutter too much screen space. A **Show more**/**Show less** toggle lets you display or hide the full text.

![A toggle button shows/hide text in long for notes](https://kinsta.com/wp-content/uploads/2026/07/Screenshot-2026-07-20-alle-08.02.31.png)

A toggle button shows/hide text in long for notes

You can view the full list of new features for Notes coming with WordPress 7.1 in the [Notes iteration for WordPress 7.1](https://github.com/WordPress/gutenberg/issues/76316).

## Admin UI improvements

The admin UI receives several updates that improve interface consistency and simplify navigation between screens.

### Persistent admin bar in the post and Site Editor

Before WordPress 7.1, the admin bar didn’t show in the post editor and the Site Editor. This behavior was inconsistent because the admin toolbar is the most-used element of the admin interface, and omitting it from the editors was not considered optimal. Starting with WordPress 7.1, this behavior changes, and the admin toolbar is now [visible in the post and Site Editor](https://make.wordpress.org/core/2026/07/13/consistent-navigation-in-wordpress-7-1-with-persistent-toolbar/).

![The Admin toolbar in the post editor](https://kinsta.com/wp-content/uploads/2026/07/wp-71-admin-toolbar-in-post-editor.png)

The Admin toolbar in the post editor

![The admin toolbar in the Site Editor](https://kinsta.com/wp-content/uploads/2026/07/wp-71-admin-toolbar-in-site-editor.png)

The admin toolbar in the Site Editor

### User’s color scheme extended to the Site Editor

Another improvement aimed at making the look of all admin areas consistent is to apply [the same color scheme](https://github.com/WordPress/gutenberg/pull/78397) set by the user on their settings page to the Site Editor as well. Before 7.1, the Site Editor sidebar was fixed to black.

![The Site Editor UI in WordPress 7.1](https://kinsta.com/wp-content/uploads/2026/07/wp-71-site-editor-ui.jpg)

The Site Editor sidebar color now matches the color set in the user’s preferences.

The editor sidebar also receives an update with WordPress 7.1. The site icon has been removed from the editor toolbar and now appears in the WordPress toolbar.

In previous versions, to go back to the WordPress admin, you had to click the site icon, which wasn’t technically a back button.

![The editor toolbar in WordPress 7.0](https://kinsta.com/wp-content/uploads/2026/08/editor-toolbar-in-wp-70.png)

The editor toolbar in WordPress 7.0

As a result, the site icon now appears only in the admin toolbar, while a clearer back button appears in the editor toolbar.

![The editor toolbar in WordPress 7.1](https://kinsta.com/wp-content/uploads/2026/08/wp-71-editor-toolbar.png)

The editor toolbar now features a proper back button

### Command categories and improved command palette UI

The command palette has received several [additions and modifications](https://github.com/WordPress/gutenberg/pull/75691) to improve its usability. First of all, the available commands have been divided into sections (recent, suggestions, and results) to make them easier to find.

![Command palette sections in WordPress 7.1](https://kinsta.com/wp-content/uploads/2026/07/wp-71-command-palette-sections.png)

Commands are now grouped into sections

The modal has been resized (512px), and the commands are now easier to read.

![The new command palette modal in WordPress 7.1](https://kinsta.com/wp-content/uploads/2026/07/wp-71-command-palette-search-results.png)

The new command palette modal

### Identity screen in the Site Editor

A new **Identity** item now appears under the **Design** menu in the Site Editor. The corresponding screen allows you to configure your Site [title, tagline](https://github.com/WordPress/gutenberg/pull/76264), [logo, and icon](https://github.com/WordPress/gutenberg/pull/76116). This lets you edit your site’s identity settings without leaving the Site Editor.

![Identity settings in Global Styles](https://kinsta.com/wp-content/uploads/2026/07/identity-settings.png)

Identity settings in Global Styles

### Infinite Scrolling for the Media Library grid view

Up until WordPress 7.0, it was possible to enable infinite scrolling for the Media Library grid view through the `media_library_infinite_scrolling` filter, which was set to `false` by default. Developers could change the default setting by adding the following line to their plugins:

```
add_filter( 'media_library_infinite_scrolling', '__return_true' );
```

Starting [with WordPress 7.1](https://make.wordpress.org/core/2026/07/23/media-library-infinite-scrolling-is-now-enabled-by-default-with-a-per-user-opt-out/), the `media_library_infinite_scrolling` filter is set to `true`, meaning that infinite scrolling in the Media Library grid view is active for all users by default.

In addition, a new setting on the user profile page in the WordPress admin allows you to set your infinite scrolling preferences.

![Disable infinite scrolling in the Media Library grid view option](https://kinsta.com/wp-content/uploads/2026/07/wp-71-disable-infinite-scrolling.png)

Disable infinite scrolling in the Media Library grid view option

WordPress stores the user’s choice in the user options using the `infinite_scrolling` meta key. You can retrieve the user preference this way:

```
$infinite_scrolling = get_user_option( 'infinite_scrolling', $user_id );
```

## Core blocks and block improvements

WordPress 7.1 introduces two new blocks and various improvements to existing ones.

### New Playlist and Tabs Blocks

A [new **Playlist** block](https://github.com/WordPress/gutenberg/issues/77421) lets you embed a simple playlist in your content.

![The Playlist block in WordPress 7.1](https://kinsta.com/wp-content/uploads/2026/07/wp-71-playlist-block.png)

The Playlist block in WordPress 7.1

Users can customize several aspects of the block’s appearance, including typography, background, dimensions, border, and elements. Style controls specific to this block include **Waveform & Play button** and **Waveform background**. The **Shape** control allows you to switch [waveform audio visualization](https://github.com/WordPress/gutenberg/pull/75203).

![Playlist block style customization](https://kinsta.com/wp-content/uploads/2026/07/wp-71-playlist-block-customized.png)

Customizing the style of the Playlist block

The [Playlist block](https://developer.wordpress.org/block-editor/reference-guides/core-blocks/core-blocks-media/core-block-playlist/) supports all audio files compatible with your WordPress installation. If you add support for a new MIME type, the block automatically inherits it.

The new core [Tabs block](https://github.com/WordPress/gutenberg/pull/69789) is designed to organize content into tabs. Each tab can contain any block, making it particularly useful for hosting content categorized by topic, FAQs, or product/service comparisons.

![The Tabs block in WordPress 7.1](https://kinsta.com/wp-content/uploads/2026/07/wp-71-tabs-block.jpg)

WordPress 7.1 features a new Tabs block

### Editable blocks inside the Custom HTML block

The Custom HTML block has received a [new enhancement](https://make.wordpress.org/core/2026/07/23/editable-blocks-inside-the-custom-html-block/). Now you can add editable blocks directly inside the HTML code. This enables you to combine static HTML and editable blocks within the same snippet.

![The Custom HTML block in WordPress 7.1](https://kinsta.com/wp-content/uploads/2026/08/wp-71-custom-html-block.png)

The Custom HTML block can now host both static HTML and editable blocks

Although they can be edited, editable blocks cannot be moved or removed, nor can additional blocks be added via the visual editor. However, the underlying code remains fully editable in the code editor.

Before WordPress 7.1, your content had to be either entirely static HTML or entirely made up of blocks. Now you can freely mix HTML and blocks, which is particularly helpful when generating content using AI models.

This change comes alongside the ability to add static HTML code to block variations. Thanks to the new `innerContent` support, you can register a variation of the HTML Code block as shown in the example below:

```
wp.blocks.registerBlockVariation( 'core/html', {
	name: 'custom-image-card',
	title: 'Custom image card',
	description: 'A custom HTML block with static header/footer and an editable image.',
	innerContent: [ 
		'<h2>Static heading</h2>\n', 
		null, 
		'\n<footer>Static footer</footer>' 
	],
	innerBlocks: [ 
		[ 
			'core/image', 
			{ 
				id: 419,
				sizeSlug: 'medium',
				linkDestination: 'none',
				url: 'https://example.com/wp-content/uploads/...',
				alt: ''
			} 
		] 
	],
} );
```

The `null` value in `innerContent` acts as a placeholder for the Image block.

Note that `innerContent` is only available for the Custom HTML block. Applying it to variations of other blocks will have no effect.

## Improvements to the SVG icon system

WordPress 7.0 introduced a [new Icon block](https://kinsta.com/blog/wordpress-7-0/#new-icon-block) and an Icon library. With WordPress 7.1, the icon management system gains a public API, enabling icons to be programmatically registered, rendered, and deleted, as well as fetched via the REST API.

### Registering and unregistering icons

To register an icon or an icon set, you must first register an icon collection by hooking the new `wp_register_icon_collection()` function into the init action:

```
function custom_icons_register_icon_collection() {
	wp_register_icon_collection(
		'my-icon-set',
		array(
			'label'       => __( 'My awesome icons', 'my-plugin' ),
			'description' => __( 'My personal set of icons.', 'my-plugin' ),
		)
	);
}
add_action( 'init', 'custom_icons_register_icon_collection' );
```

A collection has a unique name, which distinguishes it from core icons and other icon sets registered by third-party plugins. The collection name must start and end with a lowercase letter and can contain lowercase letters, numbers, hyphens, and underscores.

The function’s second argument is an array containing the collection’s label displayed in the Icon library and an optional description.

To remove a collection, use the `wp_unregister_icon_collection()` function. Removing a collection automatically deletes all icons associated with it.

To register an individual icon, use the `wp_register_icon()` function, as shown in the following example:

```
wp_register_icon(
	'my-icon-set/motorbike',
	array(
		'label'   => __( 'Motorbike', 'my-plugin' ),
		'content' => '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">...</svg>',
	)
);
```

In the example above, we registered an icon using an SVG string. You can also register an icon directly from an `.svg` file:

```
wp_register_icon(
	'my-icon-set/motorbike',
	array(
		'label'   => __( 'Motorbike', 'my-plugin' ),
		'file_path' => plugin_dir_path( __FILE__ ) . 'icons/motorbike.svg',
	)
);
```

It is important to note that the SVG is sanitized with `wp_kses`, and only the `<svg>`, `<path>`, and `<polygon>` elements are currently allowed. All other elements are filtered out, though the allowlist may be expanded to include additional elements and attributes in the future.

To delete an icon, you can use the `wp_unregister_icon()` function.

### Icon library and block updates

The Icon library has been updated accordingly and now features a sidebar displaying the list of icon collections registered on the site.

![The WordPress Icon library](https://kinsta.com/wp-content/uploads/2026/07/wp-71-icon-collection.png)

The WordPress core icon collection

![The WordPress Icon library](https://kinsta.com/wp-content/uploads/2026/07/wp-71-custom-icon-collection.png)

A custom icon collection in WordPress 7.1

The Icon block has also been updated. By default, the block now displays the Info icon instead of an empty placeholder as in previous versions. Additionally, two new controls in the block toolbar allow you to flip the icon vertically and horizontally.

![Icon block settings in WordPress 7.1](https://kinsta.com/wp-content/uploads/2026/07/wp-71-icon-block.png)

Icon block settings in WordPress 7.1

### New REST API endpoints for icons

New read-only REST API endpoints have also been introduced to access icon collections or specific icons.

For icon collections, you will use the following endpoints:

```
GET /wp/v2/icon-collections
GET /wp/v2/icon-collections/<collection>
```

To read icons, you will use the following endpoints instead:

```
GET /wp/v2/icons - Introduced with WordPress 7.0.
GET /wp/v2/icons/<collection>
GET /wp/v2/icons/<collection>/<name>
```

A user with the edit_posts capability must authenticate requests.

For a more in-depth overview of the Icon system in WordPress 7.1, check out the [dev note](https://make.wordpress.org/core/2026/07/24/registering-and-rendering-svg-icons-in-wordpress-7-1/).

## New design tools

Creators and editors now have new, improved design tools that let them style content blocks without resorting to custom CSS.

### Background gradient support

WordPress 7.1 introduces [`background.gradient` support](https://make.wordpress.org/core/2026/07/26/new-block-support-in-wordpress-7-1-background-gradient-background-gradient/) and a new admin UI control for background gradients.

In the block settings sidebar, a new Background panel with separate controls for Image, Color, and Gradient allows you to experiment with different combinations of background images, colors, and gradients while preventing conflicts.

![Background Gradient control in WordPress 7.1](https://kinsta.com/wp-content/uploads/2026/08/wp-71-background-gradient.jpg)

WordPress 7.1 features a new Background Gradient control

In WordPress 7.1, the `background.gradient` support is enabled by default for the Group, Accordion, Pullquote, Post Content, and Quote blocks. Theme developers can add support for `background.gradient` in block.json by adding a gradient property under styles.background or on a per-block basis, as shown in the following code:

```
{
	"styles": {
		"background": {
			"gradient": "linear-gradient( 135deg, #1e3c72 0%, #2a5298 100% )"
		},
		"blocks": {
			"core/group": {
				"background": {
					"gradient": "linear-gradient( 135deg, #f5f7fa 0%, #c3cf8d 100% )"
				}
			}
		}
	}
}
```

### Minimum width support

Another addition coming with WordPress 7.1 that designers and theme developers will love is [support for the `minWidth` dimension](https://make.wordpress.org/core/2026/07/26/new-block-support-in-wordpress-7-1-minimum-width/). This joins the existing support for `height`, `minHeight`, and `width`, completing the set of design tools for dimensions.

Theme developers can add support for minimum width through `theme.json`, either by enabling Appearance Tools or by adding the `dimensions.minWidth` field under settings:

```
{
	"settings": {
		"dimensions": {
			"minWidth": true
		}
	}
}
```

![Minimum width control in WordPress 7.1](https://kinsta.com/wp-content/uploads/2026/08/wp-71-min-width.jpg)

Minimum width control in WordPress 7.1

You can also add support for minimum width globally or on a per-block basis:

```
{
	"styles": {
		"dimensions": {
			"minWidth": "400px"
		},
		"blocks": {
			"core/group": {
				"dimensions": {
					"minWidth": "400px"
				}
			}
		}
	}
}
```

Block developers can similarly add `minWidth` support to `block.json`:

```
{
	"supports": {
		"dimensions": {
			"minWidth": true
		}
	}
}
```

The control is hidden by default in the sidebar, but you can change the default setting using `__experimentalDefaultControls`. In Global Styles, the control is visible by default.

### Text shadow support in Global Styles

WordPress 7.1 introduces [support for `text-shadow` in Global Styles](https://make.wordpress.org/core/2026/07/23/text-shadow-support-in-global-styles/). Previously, you would have needed a plugin or resorted to custom CSS.

Note that this is an [initial implementation](https://github.com/WordPress/gutenberg/pull/73320). A few key decisions are still pending, such as which UI control to use for customizing text shadows in the editor, and whether `text-shadow` should be available as a preset. For now, it is only possible to define `text-shadow` in your `theme.json` in one of the following ways:

```
{
	"$schema": "https://schemas.wp.org/wp/6.7/theme.json",
	"version": 3,
	"settings": {},
	"styles": {
		"typography": {
			"textShadow": "1px 1px 2em white, 0 0 2em yellow, 0 0 0.2em red;"
		},
		"blocks": {
			"core/paragraph": {
				"typography": {
					"textShadow": "1px 1px 2px red, 0 0 1em red, 0 0 0.2em red"
				}
			}
		},
		"elements": {
			"h2": {
				"typography": {
					"fontSize": "var:preset|font-size|x-large",
					"textShadow": "1px 1px 2em white, 0 0 2em yellow, 0 0 0.2em red;"
				}
			}
		}
	}
}
```

The following image shows the result of the above definitions.

![Text shadow in WordPress 7.1](https://kinsta.com/wp-content/uploads/2026/08/wp-71-text-shadow.png)

WordPress 7.1 supports text shadow via theme.json

## Updates for developers

The updates coming to theme and plugin developers with WordPress 7.1 are remarkable. The many additions and enhancements to the Abilities API and the design system theming strike us as the most noteworthy.

### Design system theming

WordPress 7.1 introduces a [new design system](https://make.wordpress.org/core/2026/07/31/design-system-theming-in-wordpress-7-1/) that plugin developers can use to customize the styling of admin interface elements. The new system consists of two parts: **Design tokens** and a new **ThemeProvider** React component.

#### Design tokens

[WordPress design tokens](https://github.com/WordPress/gutenberg/blob/trunk/packages/theme/docs/tokens.md) are [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties) that follow an established pattern. Here, for example, is the pattern for the Color token family:

```
--wpds-color-<property>-<target>-<tone>[-<emphasis>][-<state>]
```

Based on the pattern above, the following variable sets the background color for surfaces with normal emphasis:

```
--wpds-color-background-surface-neutral-strong
```

Starting with WordPress 7.1, design tokens can be used by any plugin that generates admin interface elements thanks to a new `wp-theme` stylesheet that includes a full set of semantic design tokens and is available as a plugin dependency. You can enqueue a custom stylesheet that uses `wp-theme` as shown below:

```
function myplugin_enqueue_admin_assets( $hook_suffix ) {
	wp_enqueue_style(
		'myplugin-admin-style',
		plugin_dir_url( __FILE__ ) . 'assets/css/admin.css',
		array( 'wp-theme' ),
		'1.0.0'
	);
}
add_action( 'admin_enqueue_scripts', 'myplugin_enqueue_admin_assets' );
```

The advantage of design tokens is that they can replace hard-coded CSS property values. See the following example from the dev note:

```
.card {
	background-color: var(--wpds-color-background-surface-neutral-strong);
	color: var(--wpds-color-foreground-content-neutral);
	border: var(--wpds-border-width-xs) solid var(--wpds-color-stroke-surface-neutral-weak);
	border-radius: var(--wpds-border-radius-lg);
	padding: var(--wpds-dimension-padding-2xl);
}
```

Design tokens can be used in conjunction with the ThemeProvider component to customize the appearance of specific areas of the admin page.

#### ThemeProvider

You can override the default design token values provided by the `wp-theme` stylesheet by wrapping the admin area’s content inside the new `ThemeProvider` React component, as shown in the following example from the dev note:

```
import { ThemeProvider } from '@wordpress/theme';
import { Card } from '@wordpress/ui';

function Application() {
	return (
		<ThemeProvider
			color={
				{
					primary: '#3858e9', 
					background: '#11004d' 
				}
			}
			cornerRadius="pronounced"
		>
			<Card.Root>
				<Card.Content>
					Card content
				</Card.Content>
			</Card.Root>
		</ThemeProvider>
	);
}
```

Given a primary and a background seed color, the component automatically generates a harmonious and consistent color ramp that provides accessible contrast between user interface elements.

The ThemeProvider allows plugin developers to express their brand identity within interface areas while remaining consistent with the overall style of the WordPress admin interface.

For a more in-depth analysis, please refer to the [dev note](https://make.wordpress.org/core/2026/07/31/design-system-theming-in-wordpress-7-1/) and the official documentation on [design tokens](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-theme/#design-tokens) and [ThemeProvider](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-theme/#theme-provider).

### Enhancements to the Abilities API

With the release of WordPress 7.1, the [Abilities API](https://kinsta.com/blog/wordpress-abilities-api/) receives several additions that extend its functionality.

#### New execution lifecycle for the Abilities API

First of all, the execution cycle is enhanced with [4 new filters](https://make.wordpress.org/core/2026/07/29/new-execution-lifecycle-filters-for-the-abilities-api-in-wordpress-7-1/) that run before, during, and after an ability’s execution.

![Execution lifecycle for the Abilities API in WordPress 7.1](https://kinsta.com/wp-content/uploads/2026/08/wp-71-abilities-api-lifecycle.png)

New execution lifecycle for the Abilities API in WordPress 7.1 (Source: [WordPress.org](https://make.wordpress.org/core/2026/07/29/new-execution-lifecycle-filters-for-the-abilities-api-in-wordpress-7-1/))

The `wp_pre_execute_ability` filter runs at the beginning of `WP_Ability::execute()` and is used to intercept and short-circuit the execution of an action even before WordPress starts processing it. If the filter returns a value other than the default `$pre` value (an error, data, or a boolean), WordPress stops immediately, bypasses checks, and returns that value.

This filter lends itself to interesting use cases, such as disabling an ability during site maintenance, rate limiting requests originating from the same IP, or mocking an ability’s response (Unit Testing).

The `wp_ability_normalize_input` filter runs right after default values are applied and before formal schema validation and permission checks. It is used to prepare or transform incoming data before it is validated and processed by the ability—for example, adding contextual metadata, normalizing data before validation, enriching an AI prompt, or halting ability execution in case of an error.

The `wp_ability_permission_result` filter lets you modify the result of permission checks performed before executing an ability. You can use it to add more fine-grained authorization rules, create a custom permission system, or bypass permissions in specific cases.

Note that you should use this filter with caution:

> Plugins should exercise particular care with this filter because returning `true` can override a denial from the ability’s original `permission_callback`.

The `wp_ability_execute_result` filter runs after the ability’s execution callback and before output validation, allowing you to modify the final result returned by an ability. It enables you to transform the response produced by the ability’s processing before it is returned to the caller.

#### Filtering and manipulating abilities

Before WordPress 7.1, filtering registered abilities required manually iterating over the registry using `array_filter()`. Starting with [WordPress 7.1](https://make.wordpress.org/core/2026/08/05/filtering-registered-abilities-with-wp_get_abilities-in-wordpress-7-1/), `wp_get_abilities()` accepts an optional array of arguments to filter registered abilities by `category`, `namespace`, `meta`, or a combination of these.

The following example shows how to retrieve abilities belonging to a specific category:

```
$abilities = wp_get_abilities(
	array(
		'category' => 'content-generation',
	)
);
```

You can also combine multiple parameters:

```
$abilities = wp_get_abilities(
	array(
		'category'  => 'content-generation',
		'meta'      => array(
			'public' => true,
		),
	)
);
```

For more advanced filtering, the API provides the `item_include_callback` and `result_callback` parameters—two callbacks used to include or exclude abilities from the array and to sort or manipulate the result set before it is returned.

Along with the updates to `wp_get_abilities()`, WordPress 7.1 introduces two new global filters:

- `wp_get_abilities_item_include`: Runs for every ability that passes the declarative filters and `item_include_callback`. You can use this filter to include or exclude specific abilities site-wide.
- `wp_get_abilities_result`: Runs after `result_callback`. You can use it to manipulate the entire result set of abilities across the site.

Refer to the [dev note](https://make.wordpress.org/core/2026/08/05/filtering-registered-abilities-with-wp_get_abilities-in-wordpress-7-1/) for a more in-depth overview of the updates to wp_get_abilities() and its associated filters.

#### New public exposure flag

WordPress 7.1 also introduces a [new metadata flag](https://make.wordpress.org/core/2026/08/04/a-unified-public-exposure-flag-for-abilities-in-wordpress-7-1/) to indicate that an ability is available for access by external clients, such as the REST API, MCP adapters, and AI agents.

When registering an ability, you can now use `meta.public` to allow your ability to be discovered and invoked through the REST abilities endpoints. Previously, you had to specify exposure separately for each channel—for example, by setting ‘show_in_rest’ => true to make an ability visible via REST.

#### Other improvements to the Abilities API

In addition to the updates seen above, WordPress 7.1 introduces [further enhancements](https://make.wordpress.org/core/2026/07/31/abilities-api-improvements-in-wordpress-7-1/) covering various aspects of the API.

Two new filters, `wp_ability_validate_input` and `wp_ability_validate_output`, allow plugins to validate input and output data using more complex rules than those expressible by the WordPress JSON Schema. The first filter runs after the input has been prepared and initial schema validation has passed. The second filter runs after the ability has executed and before the final result is returned.

The `wp_ability_invoked` action runs at the beginning of `WP_Ability::execute()` and can be used to track and log every attempt to invoke an ability. You can hook into this action to log access attempts to a specific ability, measure server load, set up daily or monthly usage counters, and detect brute-force call attempts.

Be careful, though:

> The action receives raw, unnormalized input. Plugins should therefore avoid logging input indiscriminately, because it may contain credentials, personal information, or other sensitive data.

### More updates for developers

The updates for developers don’t end here. WordPress 7.1 brings an impressive number of improvements and additions, providing new and more reliable development tools. With this new release, you’ll also find:

- [Four new filters to configure the Site Editor screens](https://make.wordpress.org/core/2026/07/31/filtering-site-editor-screens-in-wordpress-7-1/)
- [Post editor always iframed](https://make.wordpress.org/core/2026/08/03/iframed-editor-changes-in-wordpress-7-1/#what-s-changing-in-wordpress-7-1)
- [Updates to editor components](https://make.wordpress.org/core/2026/07/23/editor-components-updates-in-wordpress-7-1/)
- [jQuery UI updated to 1.14.2](https://make.wordpress.org/core/2026/07/29/jquery-ui-updated-to-1-14-2-in-wordpress-7-1/)
- [JSON Schema preparation for client compatibility](https://make.wordpress.org/core/2026/07/31/json-schema-preparation-for-client-compatibility-in-wordpress-7-1/).
- [Users can now apply styles to pseudo states](https://make.wordpress.org/core/2026/08/05/pseudo-and-custom-style-states-in-wordpress-7-1/).
- [Responsive block styles and configurable viewports](https://make.wordpress.org/core/2026/08/05/responsive-block-styles-and-configurable-viewports-in-wordpress-7-1/)
- [New functions for rendering tooltips and informational help](https://make.wordpress.org/core/2026/08/03/introducing-name-and-informational-tool-tips-in-wordpress-7-1/)

![Responsive styles in WordPress 7.1](https://kinsta.com/wp-content/uploads/2026/08/wp-71-responsive-styles.png)

You can define specific CSS rules for Mobile and Tablet from the visual editor, in Global Styles, or in theme.json.

## Next-gen hosting for next-gen WordPress

WordPress 7.1 marks a major step forward for the CMS across several fronts.

Client-side media processing represents a turning point in image management. Processing now occurs on the client side, resulting in greater server resource efficiency and faster page performance.

As for AI capabilities, following the groundbreaking updates in 6.9 and 7.0, WordPress 7.1 marks a moment of consolidation. The Abilities API gains new features that allow developers to build more reliable and secure AI integrations and capabilities.

Another powerful addition that developers and agencies will appreciate is the Theme Provider, which enables plugins to express their brand identity in the admin area while staying consistent with the WordPress dashboard interface.

There are also enhancements to Notes, new blocks, a more powerful SVG icon system, and much more. In short, WordPress is far from slowing down and is more forward-looking than ever.

For an increasingly advanced CMS, choosing a hosting provider that keeps pace with modern technologies is essential. Kinsta offers the ideal environment for next-generation WordPress sites: containerized cloud infrastructure, stellar performance, solid security, and fast, top-rated support.

If you haven’t tried our hosting yet, take advantage of the [free trial](https://kinsta.com/pricing/) on selected plans or [contact us](https://kinsta.com/talk-to-sales/) to learn more.
