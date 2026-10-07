---
url: "https://kinsta.com/blog/wordpress-6-9/"
title: "New features, new blocks, new APIs: here is what\u2019s new in WordPress 6.9"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: []
kinsta_last_updated: "2026-05-20T20:31:35"
change_signal: "2026-05-20T20:31:35"
fetched_at: "2026-10-07T22:58:27Z"
sha256: "e948692f6299ff11684f508950dfc8499d1a2c23aa85296253b483c852e77139"
body_chars: 39080
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# New features, new blocks, new APIs: here is what’s new in WordPress 6.9

**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/wordpress-6-9/
**Kinsta last updated:** 2026-05-20T20:31:35

## On this page

- [New core blocks](#new-core-blocks)
  - [Accordion](#accordion)
  - [Terms Query](#terms-query)
  - [Time to Read](#time-to-read)
  - [Math](#math)
  - [Comments Link and Comments Count](#comments-link-and-comments-count)
- [Improvements to existing blocks](#improvements-to-existing-blocks)
  - [Fixed background padding issue for the Heading block](#fixed-background-padding-issue-for-the-heading-block)
  - [Selectable HTML element for Button and Separator blocks](#selectable-html-element-for-button-and-separator-blocks)
  - [tagName selector for the Post Content block](#tagname-selector-for-the-post-content-block)
  - [Custom link icons for Social Links](#custom-link-icons-for-social-links)
  - [Sorting by menu order in the Query Loop block](#sorting-by-menu-order-in-the-query-loop-block)
  - [Updates to the Navigation block](#updates-to-the-navigation-block)
  - [Stretchy Heading and Stretchy Paragraph block variations](#stretchy-heading-and-stretchy-paragraph-block-variations)
  - [Poster image support for the Cover block](#poster-image-support-for-the-cover-block)
- [Commenting blocks with Notes in WordPress 6.9](#commenting-blocks-with-notes-in-wordpress-69)
- [Block visibility control](#block-visibility-control)
- [Command palette extended to the admin dashboard](#command-palette-extended-to-the-admin-dashboard)
- [What’s new for developers](#whats-new-for-developers)
  - [Abilities API](#abilities-api)
  - [Block Bindings API improvements](#block-bindings-api-improvements)
  - [Enhancements to DataViews and DataForm](#enhancements-to-dataviews-and-dataform)
  - [Enhancements to the Interactivity API](#enhancements-to-the-interactivity-api)
    - [Adding IDs to Interactivity API directives](#adding-ids-to-interactivity-api-directives)
    - [Script modules and stylesheets loading](#script-modules-and-stylesheets-loading)
    - [Router regions inside interactive elements](#router-regions-inside-interactive-elements)
    - [New attachTo property for router regions](#new-attachto-property-for-router-regions)
    - [getServerState and getServerContext synchronization](#getserverstate-and-getservercontext-synchronization)
  - [Additional updates for developers](#additional-updates-for-developers)
- [Looking ahead: from WordPress 6.9 to 7.0](#looking-ahead-from-wordpress-69-to-70)

---

WordPress 6.9 is just around the corner, and we can’t wait to use some of the many fantastic new features that will be included in the latest release of the world’s most popular CMS.

At a glance, the main improved areas in WordPress 6.9 include the following:

- New core blocks (Accordion, Math, and more) for greater flexibility in content creation.
- Major editor improvements, making the building experience even more fluid and intuitive.
- New developer APIs such as the Abilities API, updates to the Interactivity API, and the Block Bindings API, along with other additional upgrades slated for the 6.9 release.
- Improvements to workflows and collaboration with Notes, block visibility option, and the expansion of the Command Palette.

These updates ensure a better experience for everyone: WordPress users will enjoy more powerful editing and collaboration tools, while developers will benefit from more advanced integration capabilities thanks to an enhanced set of APIs.

There’s a lot to cover, so let’s explore the new features coming with WordPress 6.9 that have excited us the most:

## New core blocks

Following [this GitHub issue](https://github.com/WordPress/gutenberg/issues/71026), WordPress 6.9 introduces six new blocks, expanding the block editor’s creative capabilities and eliminating the need for users to install additional plugins. These new blocks include **Accordion**, **Term Query**, **Time to Read**, **Math**, **Comment Count**, and **Comment Link**.

For years, contributors debated whether new blocks should live in core or remain in plugin territory. WordPress 6.9 takes a practical path forward. In the words of Mathias Ventura,

> I think not having these blocks in the core library severely limits the expressiveness that theme builders (and users) can depend upon to build great designs and it can fracture the overall experience, forcing people to go for more fully equipped block libraries instead or desist altogether if they plan to release something broadly.

Now, let’s take a closer look at each of the new blocks merged into the core with WordPress 6.9.

### Accordion

The long-awaited **Accordion** block is finally coming to the core. It is not a single block, but rather a nested block structure that you can easily explore from the Block Inspector.

![The Accordion block structure.](https://kinsta.com/wp-content/uploads/2025/11/accordion-block-structure.png)

The Accordion block structure in the post editor.

Each Accordion block consists of the following inner blocks:

- **Accordion:** The container for nested Accordion items.
- **Accordion item:** It is the directly nested element and consists of a heading and a panel.
- **Accordion heading:** A clickable heading that opens and closes a panel.
- **Accordion panel:** This panel contains the Accordion item content and can include any type of block.

![An Accordion block in the code editor.](https://kinsta.com/wp-content/uploads/2025/11/accordion-block-code.png)

An Accordion block in the code editor.

The block has a minimalist style, but Justin Tadlock’s excellent guide, [“Styling accordions in WordPress 6.9](https://developer.wordpress.org/news/2025/10/styling-accordions-in-wordpress-6-9/),” provides the essential knowledge to customize the appearance of your accordions.

Check out the PRs [#64119](https://github.com/WordPress/gutenberg/pull/64119), [#71222](https://github.com/WordPress/gutenberg/pull/71222), and [#71388](https://github.com/WordPress/gutenberg/pull/71388) for full details on the new Accordion block.

### Terms Query

WordPress 6.9 introduces a new **Terms Query** block. Similar to the Query block, it displays terms instead of posts. This new block is actually a **Terms Template** containing a **Row** block with a **Term Name** and a **Term Count**.

![Terms Query block structure](https://kinsta.com/wp-content/uploads/2025/11/terms-query-block-structure.png)

Terms Query block structure

The Terms Query block comes with several configuration options. You can set the taxonomy, sort the list items, specify the selected items, and choose to show or hide empty or nested terms. You can also set the number of terms to show.

![Terms Query block settings](https://kinsta.com/wp-content/uploads/2025/11/terms-query-block-settings.png)

Terms Query block settings

The Term Template has two display modes: List and Grid. Grid view allows you to customize the position of grid elements and the number of columns.

![Terms Query in Grid view](https://kinsta.com/wp-content/uploads/2025/11/terms-query-block-grid-view.png)

The Terms Query block has two modes: List and Grid

You can also change the tags of block elements. For instance, you could use an `h2` element for the Term Name block. You can also insert blocks between the elements of the Terms Query block. The image below shows a Separator block between rows.

![Customizing the Terms Query block](https://kinsta.com/wp-content/uploads/2025/11/terms-query-block-customization.png)

Customizing the Terms Query block

To learn more about the Terms Query block, check out PR [#70720](https://github.com/WordPress/gutenberg/pull/70720) and Issue [#49094](https://github.com/WordPress/gutenberg/issues/49094).

### Time to Read

As its name suggests, the **Time to Read** block displays the reading time for the current post or page. The block has two modes, Time to Read and [Word Count](https://github.com/WordPress/gutenberg/pull/71841), and an option to display the reading time as either a [range](https://github.com/WordPress/gutenberg/pull/71606) or a specific value.

![The Time to Read block](https://kinsta.com/wp-content/uploads/2025/11/time-to-read-block.png)

The Time to Read block

![The Time to Read block in Word Count mode](https://kinsta.com/wp-content/uploads/2025/11/word-count-mode.png)

The Time to Read block in Word Count mode

### Math

The **Math** block allows you [insert mathematical formulas](https://github.com/WordPress/gutenberg/pull/72182) into your content. Just write your formulas in [LaTeX syntax](https://en.wikibooks.org/wiki/LaTeX/Mathematics), and they will be converted into the corresponding mathematical symbols.

![Math block preview.](https://kinsta.com/wp-content/uploads/2025/11/math-block.png)

The Math block allows you to insert mathematical formulas into posts and pages.

It is also possible to insert inline formulas.

![Adding inline math in WordPress 6.9](https://kinsta.com/wp-content/uploads/2025/11/inline-math.png)

Adding inline math in WordPress 6.9

### Comments Link and Comments Count

The **Comments Link** and **Comments Count** blocks are [no longer marked as experimental](https://github.com/wordpress/gutenberg/issues/73179). Both blocks are now available for use in the Site Editor and the Post Editor.

## Improvements to existing blocks

WordPress 6.9 introduces minor and major updates to a multitude of blocks, improving their functionality and/or usability.

### Fixed background padding issue for the Heading block

A CSS specificity issue with the Heading block’s background padding has been fixed with WordPress 6.9. Before this release, the padding styles applied to the Heading block affected other blocks that used headings, such as the Accordion block.

Thanks to the use of the `:where()` pseudo-class, the CSS selector for headers that use backgrounds has been made more specific, as described in the [dev notes](https://make.wordpress.org/core/2025/11/12/heading-block-css-specificity-fix-in-wordpress-6-9/).

```
h1, h2, h3, h4, h5, h6 {
	&:where(.wp-block-heading).has-background {
		padding: ...;
	}
}
```

If a theme uses the `.has-background` class with heading elements that are not Heading blocks, these elements [no longer receive](https://github.com/WordPress/gutenberg/pull/72837) the default background padding.

### Selectable HTML element for Button and Separator blocks

To improve accessibility, [you can now select](https://make.wordpress.org/core/2025/06/11/whats-new-in-gutenberg-21-0-11-june/) the HTML elements of the Button and Separator blocks.

For the Button block, [you can choose](https://github.com/WordPress/gutenberg/pull/70139) between `<a>` and `<button>` in the block’s Advanced settings.

![Button block Advanced settings](https://kinsta.com/wp-content/uploads/2025/11/button-block-settings.png)

Button block Advanced settings

For the Separator block, [you can choose](https://github.com/WordPress/gutenberg/pull/70185) between `<hr>` and `<div>`.

![Separator block Advanced settings](https://kinsta.com/wp-content/uploads/2025/11/separator-block-settings.png)

Separator block Advanced settings

### tagName selector for the Post Content block

Starting with WordPress 6.9, you can select the semantically [appropriate wrapper](https://github.com/WordPress/gutenberg/pull/70698) for the **Post Content** block. You can choose between `<main>`, `<section>`, or `<article>`.

![HTML element option for the Post Content block](https://kinsta.com/wp-content/uploads/2025/11/html-element-option-post-content.png)

HTML element option for the Post Content block

### Custom link icons for Social Links

A new `block_core_social_link_get_services` filter now allows developers to add custom link icons to the Social Links block using block variations. This addition provides more options for customizing the Social Links block and eliminates the need for the core to manage a long list of services.

You can find the technical details and the code to register a Social Link variation in the PR [#70261](https://github.com/WordPress/gutenberg/pull/70261). The following image shows the result in the post editor.

![A custom link icon in WordPress 6.9](https://kinsta.com/wp-content/uploads/2025/11/custom-social-link-icon.png)

A custom link icon in WordPress 6.9

### Sorting by menu order in the Query Loop block

In addition to post title and date, you can now sort post types that support page attributes in the Query Loop block by menu order. To try out this new feature, create multiple pages and use Quick edit to edit each one.

![Change menu order in the Pages screen.](https://kinsta.com/wp-content/uploads/2025/11/menu-order-quick-edit.png)

Change menu order in the Pages screen.

You can also change the menu item order by editing each page individually. In the Page sidebar on the left, click the Actions button (the three dots in the top right corner). Then, select Order. A pop-up will appear with a numeric field for setting the menu order.

![Select menu order from the Actions menu.](https://kinsta.com/wp-content/uploads/2025/11/menu-order-option.png)

Select menu order from the Actions menu.

![Change menu order](https://kinsta.com/wp-content/uploads/2025/11/change-menu-order.png)

Change menu order

After setting the page order, create a new page and add a Query Loop block. Select **Pages** as the post type and sort them by **Menu Order**.

The `menu_order` value is available for all post types in the database; however, you need to register support for the `page-attributes` feature to make this setting available for your custom post types.

For further information on this feature, refer to PR [#68781](https://github.com/WordPress/gutenberg/pull/68781).

### Updates to the Navigation block

The Navigation Block has undergone several updates. Here is a quick list of the major ones:

A new **Create Page** button has been [added to the Link UI](https://github.com/WordPress/gutenberg/pull/71188) of the Navigation Link block. This update includes the option to publish the page immediately.

![Create Page from the Navigation block's Link UI](https://kinsta.com/wp-content/uploads/2025/11/create-page-from-link-ui.png)

Create Page from the Navigation Link block’s Link UI

![Publish immediately option](https://kinsta.com/wp-content/uploads/2025/11/publish-immediately-link-ui.png)

Publish immediately option

This functionality is also available in the Button block, even when it is included in the Navigation Menu.

![Create page command in the Button block's Link Ui](https://kinsta.com/wp-content/uploads/2025/11/create-page-button.png)

Create page command in the Button block’s Link Ui

Thanks to the Block Bindings API, the URL attribute of the Navigation Link block [dynamically updates](https://github.com/WordPress/gutenberg/pull/71630) when the original URL changes, provided the link is to an entity, such as a Page or Post.

![Synced link URL](https://kinsta.com/wp-content/uploads/2025/11/synced-link-url.png)

Synced link URL

A [new toggle option](https://github.com/WordPress/gutenberg/pull/67262) in the Navigation Link block settings sidebar now allows users to configure navigation links to open in a new tab. Previously, the **Open in new tab** option was only available in the context menu modal link. With this addition, the option is easier to locate, as it is positioned next to all the other settings in the sidebar.

![Open in new tab option in the Navigation Link block's link UI](https://kinsta.com/wp-content/uploads/2025/11/open-link-in-new-tab.png)

Open in new tab option in the Navigation Link block’s link UI

You can now set a [transparent background](https://github.com/WordPress/gutenberg/pull/69379) for the Navigation Menu block from the editor interface. Before WordPress 6.9, you had to use custom CSS code to achieve this effect.

### Stretchy Heading and Stretchy Paragraph block variations

The Stretchy Heading and Stretchy Paragraph blocks are two new variations that automatically stretch text to fit the full width of the container.

You can insert the two variations in two different ways: directly from the Block inserter or from the dropdown menu of the Heading and Paragraph block toolbar.

![Stretchy Heading and Stretchy Paragraph block variations](https://kinsta.com/wp-content/uploads/2025/11/stretchy-heading-paragraph.png)

Stretchy Heading and Stretchy Paragraph block variations

![Transform to Stretchy Paragraph](https://kinsta.com/wp-content/uploads/2025/11/transform-to-stretchy-paragraph.png)

Transform to Stretchy Paragraph

### Poster image support for the Cover block

Thanks to a new `poster-image` component, [the Cover block now supports poster images](https://github.com/WordPress/gutenberg/pull/70816). This is particularly useful for large videos and for users with slow connections, improving the user experience.

Now that we’ve explored the major additions and improvements to core blocks, let’s examine how WordPress 6.9 facilitates team collaboration on content creation, tailored to individual responsibilities. This release introduces two powerful features that will significantly enhance collaboration and workflows inside the editor: **Notes** and **visibility**.

## Commenting blocks with Notes in WordPress 6.9

You can now add notes to blocks in the Post editor. This feature enables asynchronous collaboration between team members, allowing you to track activities and streamline editorial workflows.

Since this is a feature specific to the post editor, users must have the `edit_posts` capability for that post to add notes. This means that:

- Logged-in users with the Admin or Editor role can view all notes on all posts.
- Authors and Contributors can view and edit the notes they have created.
- Subscribers cannot view notes.

To add a new note, click on the **Add Note** button in the block toolbar.

![A new Add Note item appears in the Options menu of the block toolbar.](https://kinsta.com/wp-content/uploads/2025/11/add-note-button.png)

A new Add Note item appears in the Options menu of the block toolbar.

This displays a new Notes sidebar and a note panel to add your note.

![Adding a note to a block in WordPress 6.9](https://kinsta.com/wp-content/uploads/2025/11/note-panel.png)

Adding a note to a block in WordPress 6.9

You can toggle the Notes sidebar on/off by clicking on the **All Notes** button that appears after you have added your first note.

![All notes control in the editor settings toolbar.](https://kinsta.com/wp-content/uploads/2025/11/all-notes-button.png)

All notes control in the editor settings toolbar.

Notes can be resolved, modified, or deleted.

![Edit note in WordPress 6.9](https://kinsta.com/wp-content/uploads/2025/11/edit-note.png)

Edit note in WordPress 6.9

Notes are enabled by default for posts and pages, but you can also enable them for your custom post types thanks to the new `notes` support. Here is a simple example of how to add Notes support for a custom post type:

```
register_post_type( 'book', array(
	'label' => 'Books',
	'public' => true,
	'show_in_rest' => true,
	'supports' => array(
		'title',
		'editor' => array( 'notes' => true ),
		'author',
		'excerpt',
	),
) );
```

Adding note support when registering a custom post type is pretty straightforward. However, adding note support to an existing post type is a bit trickier. Fortunately, core developers are [already working](https://core.trac.wordpress.org/ticket/64156) to streamline the process, and we can expect updates to this feature in future WordPress releases.

Technically, notes are comments and are stored in the `wp_comments` table with the `comment_type` field set to `note`. To access notes programmatically from a plugin, use the `get_comments()` function as follows:

```
$args = array(
	'post_id' => $post_id,
	'type'    => 'note',
);
$notes = get_comments( $args );
```

Note that when trying to retrieve notes from a plugin, you must specify the `note` type because note-type comments are excluded from query results by default.

When a user adds a note to a block, the post’s author receives a notification email. These emails are enabled by default, but can be disabled from the WordPress dashboard by navigating to **Settings** > **Discussion** > **Email me whenever** and deselecting the new option **Anyone posts a note**.

![Email notification settings in WordPress 6.9](https://kinsta.com/wp-content/uploads/2025/11/notification-settings-wp-69.png)

Email notification settings in WordPress 6.9

Developers can control these notifications programmatically by using the `notify_post_author` filter.

Please note that this is the initial version of the notes feature. The development team is already working on the [next iteration for WordPress 7.0](https://github.com/WordPress/gutenberg/issues/73260).

Furthermore, in WordPress 6.9, notes are only available at the block level. [Inline notes](https://github.com/WordPress/gutenberg/issues/59445) should be implemented in future iterations.

Refer to the [developer notes](https://make.wordpress.org/core/2025/11/15/notes-feature-in-wordpress-6-9/) and the [Block Commenting iteration for WordPress 6.9](https://github.com/WordPress/gutenberg/issues/66377) for a more in-depth analysis of the new Notes features with several code examples.

## Block visibility control

WordPress 6.9 introduces a new block API and a new interface for controlling block visibility on the frontend and in the editor.

This feature is useful for hiding blocks that are not yet ready to be displayed, and it complements the new Notes feature perfectly. Now, teams can collaborate on creating pages and finalize sections only when they are complete and approved.

To try out the new feature, create a new post or page and add one or more blocks or patterns. Then, hide the block or pattern from the Block Settings dropdown menu or List View, and check the effect in both the editor and the frontend.

![Hiding blocks in WordPress 6.9](https://kinsta.com/wp-content/uploads/2025/11/hide-blocks-list-view.png)

Hiding blocks in WordPress 6.9

![The new block visibility control](https://kinsta.com/wp-content/uploads/2025/11/block-visibility-control.png)

The new block visibility control

## Command palette extended to the admin dashboard

The Command palette is now available in [both the site editor and the WordPress dashboard](https://github.com/WordPress/gutenberg/pull/71030) (Ctrl+K or Command+K) to make navigation easier and faster. Type in the palette to search, navigate the dashboard, or perform actions directly. For example, typing “add” will bring up a menu of actions such as **Add Post**, **Add Media File**, **Add User**, and more.

![The Command palette in the Posts screen](https://kinsta.com/wp-content/uploads/2025/11/command-palette-wp-69.png)

The Command palette in the Posts screen

Several proposals have been made to extend and improve the command palette, and new commands will be added in the future. Follow the conversation in the [Command Palette Overview](https://github.com/WordPress/gutenberg/issues/66648) issue to stay updated.

## What’s new for developers

Now, let’s move on to the part of WordPress 6.9 that developers will find most exciting. A brand new set of APIs now enables developers to make their plugins accessible to AI systems. But that’s not all! WordPress 6.9 also brings many improvements to existing APIs, including the Interactivity API, Block Bindings, and the DataViews API.

Let’s explore the new features in detail.

### Abilities API

WordPress 6.9 introduces the [Abilities API](https://make.wordpress.org/core/2025/11/10/abilities-api-in-wordpress-6-9/), a new functional interface that provides a standardized registry, allowing plugins, themes, and WordPress core to expose their capabilities in both human- and machine-readable formats.

This [centralized registry](https://make.wordpress.org/ai/2025/07/17/abilities-api/) is where all functionality can be formally registered for discovery, validation, and execution consistently via PHP, REST APIs, and AI solutions.

The new Abilities API directly benefits WordPress users by allowing external services—such as AI assistants, external apps, and UI features like the Command Palette—to understand and execute WordPress actions (for example, publishing or editing) in a standardized way.

What are the benefits of this for developers?

The first benefit is **clarity**: An ability is a registered feature with a description, input, and output.

The second essential aspect of the new API is **standardization**. The API ensures that commands are formulated and understood consistently, regardless of the environment. This could be the WordPress dashboard, the block editor, an external app accessing via the REST API, or an AI assistant.

Another key aspect is **workflow automation**. With the Abilities API, you can create sequences of operations enabling developers to build complex automated workflows.

Developers can use the Abilities API for [various purposes](https://github.com/WordPress/gutenberg/issues/70710), including extending the Command Palette’s functionality, creating automated workflows, and more.

Once registered, abilities become [accessible to AI systems](https://make.wordpress.org/ai/2025/07/17/abilities-api/), such as ChatGPT and Gemini:

> The API manages registration and permissions, while protocol Adapters translate these into formats external AI systems understand. This establishes a robust connection between WordPress functionality and AI assistants, with the first-party API serving as the definitive source for exposed logic.

An ability is “a self-contained unit of functionality with defined inputs, outputs, permissions, and execution logic.”

The API provides a set of functions that allow you to manage every aspect of Abilities and Ability Categories. It also offers new REST API endpoints, actions, and filter hooks.

To register a new ability, the API provides the new `wp_abilities_api_init` action and the `wp_register_ability` function. Here is the function signature:

```
wp_register_ability( string $name, array $args ): ?\WP_Ability
```

`wp_register_ability` accepts the following parameters:

- `$name` (*string*) is a unique identifier for the ability
- `$args` (*array*) is an array of arguments

The function returns an instance of `WP_Ability` if registration was successful and `null` in case of failure.

Here’s an example of how to register an Ability, taken from [the documentation](https://github.com/WordPress/abilities-api/blob/trunk/docs/php-api.md#registering-a-simple-data-retrieval-ability-without-an-input-schema):

```
add_action( 'wp_abilities_api_init', 'my_plugin_register_site_info_ability' );
function my_plugin_register_site_info_ability() {
	wp_register_ability( 'my-plugin/get-site-info', array(
		'label' => __( 'Get Site Information', 'my-plugin' ),
		'description' => __( 'Retrieves basic information about the WordPress site including name, description, and URL.', 'my-plugin' ),
		'category' => 'data-retrieval',
		'output_schema' => array(
			'type' => 'object',
			'properties' => array(
				'name' => array(
					'type' => 'string',
					'description' => 'Site name'
				),
				'description' => array(
					'type' => 'string',
					'description' => 'Site tagline'
				),
				'url' => array(
					'type' => 'string',
					'format' => 'uri',
					'description' => 'Site URL'
				)
			)
		),
		'execute_callback' => function() {
			return array(
				'name' => get_bloginfo( 'name' ),
				'description' => get_bloginfo( 'description' ),
				'url' => home_url()
			);
		},
		'permission_callback' => '__return_true',
		'meta' => array(
			'annotations' => array(
				'readonly' => true,
				'destructive' => false
			),
		),
	));
}
```

Here’s what this code does:

- `wp_abilities_api_init` is the action to hook into when registering a new ability, ensuring that the Abilities API is fully initialized before attempting to register the new ability.
- `wp_register_ability` is the function that registers a new ability. The first argument is the unique identifier of the ability (`my-plugin/get-site-info`); the second argument is an array of settings.
- `label` is a human-readable label to be used in the UI (e.g., the command palette).
- `description` is the description of the ability
- `category` is the ability category
- `output_schema` is an array that defines the data returned by the ability.
- `execute_callback` is a callback function that is executed when the ability is invoked.
- `permission_callback` is a function that is executed to verify whether the user or agent has permission to execute the ability.
- `meta` is an array of optional metadata.

Developers will find more details with many code examples in the following resources:

- [Abilities API in WordPress 6.9](https://make.wordpress.org/core/2025/11/10/abilities-api-in-wordpress-6-9/)
- [Introducing the WordPress Abilities API](https://developer.wordpress.org/news/2025/11/introducing-the-wordpress-abilities-api/)
- [Abilities API](https://make.wordpress.org/ai/2025/07/17/abilities-api/)
- [Abilities API GiutHub repo](https://github.com/WordPress/abilities-api)
- [Abilities API Developer Documentation](https://github.com/WordPress/abilities-api/tree/trunk/docs)

### Block Bindings API improvements

WordPress 6.9 introduces several improvements to the [Block Bindings API](https://kinsta.com/blog/wordpress-6-5/#block-bindings-api).

First, support for the Block Bindings API has been expanded to include other blocks.

- The **Data** block now accepts any date, regardless of the post’s publication or update date. This was made possible by adding the new `core/post-data` data source. You can try it yourself by adding a Date block to a post and assigning it a custom date. Then, add another Date block and select the **Post Date** variation. Then change the publication date, save the post, and check the differences. For technical details, please refer to the [PR #70585](https://github.com/WordPress/gutenberg/pull/70585).
- WordPress 6.9 also adds [support for the Image block’s caption attribute](https://github.com/WordPress/gutenberg/pull/72476) in [pattern overrides](https://kinsta.com/blog/wordpress-block-patterns/#synced-pattern-overrides).

The editor’s UI has been enhanced to show different Block Bindings sources. Users can switch between data sources and bind or unbind attributes in just a few clicks (see image below).

WordPress 6.9 also introduces a couple of interesting changes for developers.

A new `block_bindings_supported_attributes_{$block_type}` filter has been added to the API for use on the server side. This filter allows you to specify which block attributes can be connected to a custom data source.

On the client side, you can now register custom sources using the `getFieldsList` method in the source registration function.

The [dev notes](https://make.wordpress.org/core/2025/11/12/block-bindings-improvements-in-wordpress-6-9/) provide a valuable block of code that you can copy and paste into your browser’s console to view the improved Block Bindings UI.

The following image shows the new source selector for a Paragraph block.

![The Block Bindings UI in WordPress 6.9](https://kinsta.com/wp-content/uploads/2025/11/block-binding-ui-wp-69.png)

The Block Bindings UI in WordPress 6.9

### Enhancements to DataViews and DataForm

The DataViews and DataForm APIs provide a modern, standardized way to view and manage structured data, such as lists of posts, pages, or media.

The two APIs serve different purposes.

- The [DataViews API](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-dataviews/) is designed for viewing and navigating data. It enables you to create views, including tables, grids, and lists. You can also search, filter, and sort data with it.
- The [DataForm API](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-dataviews/#dataform) is designed for modifying the elements of a dataset.

![Pages section in List layout in the Site Editor](https://kinsta.com/wp-content/uploads/2025/11/pages-section-wp-69.jpg)

An example of DataViews: Displaying pages in List layout in the Site Editor

With WordPress 6.9, these two APIs receive several improvements. Below is a list of the main additions:

- The [DataViews gains](https://make.wordpress.org/core/2025/11/11/dataviews-dataform-et-al-in-wordpress-6-9/) new fields, controls, and operators. Among the various additions, you’ll find new media, boolean, email, and array field type definitions, new `checkbox` and `toggleGroup` Edit controls, new filter operators, and much more.
- The validation system has been [completely overhauled](https://make.wordpress.org/core/2025/11/11/dataviews-dataform-et-al-in-wordpress-6-9/#field-api-isvalid). All fields now support “the `required` and `elements` rule, as well as defining custom validation via the custom function.”
- In addition to the `datetime` field type, the DataViews now [support the `date` field type](https://github.com/WordPress/gutenberg/pull/70657). This allows you to display items based solely on the date. This addition also enables filtering by date using the new `Calendar` component.
- The new release also adds `DateCalendar` and `DateRangeCalendar` components.
- The table layout has been improved further. It is now possible to [select multiple items](https://github.com/WordPress/gutenberg/pull/70891) by using **Control/⌘ + click**.
- The [new `groupByField` property](https://github.com/WordPress/gutenberg/issues/57967) enables you to visually group data based on field values, making it easier to organize data. This feature is available for both [grid](https://github.com/WordPress/gutenberg/pull/70752) and [table](https://github.com/WordPress/gutenberg/pull/71055) layouts.
- WordPress 6.9 also introduces performance improvements to DataViews. Before version 6.9, the `FeaturedImageView` component used in DataViews loaded images at full size. This meant that sites with many large preview images had to load several megabytes of images. Starting with 6.9, however, [the grid layout uses responsive images](https://github.com/WordPress/gutenberg/pull/70493), which significantly improves backend performance for sites that use a large number of images.

Other noteworthy changes to DataViews include:

- Introduced [locked filters](https://github.com/WordPress/gutenberg/pull/71075) that allow viewing the effects of filters without modifying them. This is useful for pre-configured views.
- A new [Edit control](https://github.com/WordPress/gutenberg/pull/70836) has been implemented for the `date` field.
- The [DataViews empty state](https://github.com/WordPress/gutenberg/pull/70867) can now be customized, allowing you to customize the message or provide a React node for further customization.

For a complete list of additions and changes to the DataViews and DataForm APIs, please refer to the [dev notes](https://make.wordpress.org/core/2025/11/11/dataviews-dataform-et-al-in-wordpress-6-9/) and PRs [#70567](https://github.com/WordPress/gutenberg/pull/70567/files) and [#70578](https://github.com/WordPress/gutenberg/pull/70578).

### Enhancements to the Interactivity API

As the name suggests, the [Interactivity API](https://kinsta.com/blog/wordpress-interactivity-api/) enables developers to create interactive blocks that react in real time to user interactions. In short, this is a tool for building rich user experiences and making sites attractive, dynamic, and engaging.

First introduced in [WordPress 6.5](https://kinsta.com/blog/wordpress-6-5/), the Interactivity API receives significant updates in this release. Below are some of the most interesting additions.

#### Adding IDs to Interactivity API directives

You can now add IDs to Interactivity API directives. This feature is useful because it allows you to work around the limitation of not being able to use multiple attributes with the same name in the same HTML element.

To [assign an ID to a directive](https://github.com/WordPress/gutenberg/pull/72161), append a triple-dash (`---`) followed by the ID, as in the following example:

```
<div
	data-wp-watch---my-unique-id="callbacks.firstWatch"
	data-wp-watch---another-id="callbacks.secondWatch"
></div>
```

#### Script modules and stylesheets loading

This [change](https://github.com/WordPress/gutenberg/pull/70353) enables more comprehensive and fluid client-side navigation. WordPress now replaces style sheets and loads script modules “after” client-side navigation. This has significant implications.

- The new algorithm reuses style sheets shared with previous pages, loads new ones not present in those pages, and disables unused ones. This minimizes network requests.
- Script modules are also managed more efficiently thanks to the new `importmap` definitions.
- Finally, prefetching preloads all the style sheets and script modules that have not yet been preloaded.

#### Router regions inside interactive elements

Another addition is support for router regions inside interactive elements. Previously, the router region — the area of the page that updates when the user clicks on a link — had to be a root interactive element. This meant that the content would not update if the router region was located within another interactive element. WordPress 6.9 [changes things](https://github.com/WordPress/gutenberg/pull/71635), enabling developers to place router regions within interactive elements.

#### New attachTo property for router regions

Router regions now accept a new `attachTo` property that can be defined inside the `data-wp-router-region directive`. Thanks to [this new property](https://github.com/WordPress/gutenberg/pull/70421), the routing region can now be rendered even when it is not present on the initial page. The value of `attachTo` needs to be a CSS selector pointing to the parent element where the router region will be injected. Here is an example from the dev notes:

```
<div
	data-wp-interactive="example"
	data-wp-router-region='{ "id": "example/region", "attachTo": "body" }'
>
	I'm in a new region!
</div>
```

#### getServerState and getServerContext synchronization

The `getServerState()` and `getServerContext()` functions [have been improved](https://github.com/WordPress/gutenberg/pull/72381). Now, when these functions track a value that does not change during client-side navigation, the values are reset. Additionally, only properties on the current page are preserved, while those from previous pages are removed.

For a more in-depth overview of the improvements to the Interactivity API with code examples, check [Interactivity API’s client navigation improvements in WordPress 6.9](https://make.wordpress.org/core/2025/11/12/interactivity-apis-client-navigation-improvements-in-wordpress-6-9/) and [Changes to the Interactivity API in WordPress 6.9](https://make.wordpress.org/core/2025/11/12/changes-to-the-interactivity-api-in-wordpress-6-9/).

For a comprehensive overview of the Interactivity API, refer to [our in-depth guide](https://kinsta.com/blog/wordpress-interactivity-api/).

### Additional updates for developers

WordPress 6.9 introduces a variety of updates for developers. Here is a quick list of dev notes:

- [Updates to the HTML API](https://make.wordpress.org/core/2025/11/21/updates-to-the-html-api-in-6-9/)
- [Admin menu search query changed](https://make.wordpress.org/core/2025/11/19/admin-menu-search-query-changed/)
- [New streaming block parser](https://make.wordpress.org/core/2025/11/19/introducing-the-streaming-block-parser-in-wordpress-6-9/)
- [PHP 8.5 support](https://make.wordpress.org/core/2025/11/21/php-8-5-support-in-wordpress-6-9/)
- [Accessibility improvements](https://make.wordpress.org/core/2025/11/19/accessibility-improvements-in-wordpress-6-9/)
- [Updates and bug-fixes to the wp_mail() function](https://make.wordpress.org/core/2025/11/18/more-reliable-email-in-wordpress-6-9/)
- [Improved UTF-8 support](https://make.wordpress.org/core/2025/11/18/modernizing-utf-8-support-in-wordpress-6-9/)
- [Cache Keys for Query Groups](https://make.wordpress.org/core/2025/11/17/consistent-cache-keys-for-query-groups-in-wordpress-6-9/)
- [Improvements to URL-escaping functions](https://make.wordpress.org/core/2025/11/19/url-escaping-functions-can-support-https-as-the-default-protocol-in-wordpress-6-9/)
- [Updates to the post editor for full iframe integration](https://make.wordpress.org/core/2025/11/12/preparing-the-post-editor-for-full-iframe-integration/)
- [Standardize Block Inspector Settings to use ToolsPanel](https://github.com/WordPress/gutenberg/issues/67813)
- [Legacy Internet Explorer Code Removed](https://make.wordpress.org/core/2025/11/19/legacy-internet-explorer-code-removed/)
- [Preformance improvements](https://make.wordpress.org/core/2025/11/18/wordpress-6-9-frontend-performance-field-guide/)
- [More changes for developers](https://make.wordpress.org/core/2025/11/17/miscellaneous-developer-focused-changes-in-6-9/)

## Looking ahead: from WordPress 6.9 to 7.0

WordPress 6.9 introduces meaningful upgrades across the block editor, APIs, and collaborative workflows, updates that will continue evolving in 7.0. As the platform becomes more dynamic and more deeply connected to AI-driven tooling, having performance-forward hosting becomes increasingly important. If you’re preparing for 6.9 or planning for what’s coming next, explore [Kinsta plans](https://kinsta.com/pricing/) to power your WordPress projects with confidence.
