---
url: "https://kinsta.com/blog/wordpress-interactivity-api/"
title: "Unlocking new possibilities with the WordPress Interactivity API"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "API", "Unlocking new possibilities with the WordPress Interactivity API"]
kinsta_last_updated: "2025-11-10T11:25:28+00:00"
sitemap_lastmod: "2025-11-10T11:25:28"
fetched_at: "2026-10-07T22:43:13Z"
sha256: "992cfb8590f6a01f51e4e8b382965e17592487bf18caf1959d8ed4291d334c84"
body_chars: 37263
extracted_with: "main article"
status: "live"
---

# Unlocking new possibilities with the WordPress Interactivity API

**Section:** Resource Center > Blog > API > Unlocking new possibilities with the WordPress Interactivity API
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/wordpress-interactivity-api/
**Kinsta last updated:** 2025-11-10T11:25:28+00:00

## On this page

- [What you need before you start with the Interactivity API](#what-you-need-before-you-start-with-the-interactivity-api)
- [What is the Interactivity API?](#what-is-the-interactivity-api)
- [The structure of interactive blocks](#the-structure-of-interactive-blocks)
  - [package.json](#packagejson)
  - [block.json](#blockjson)
  - [render.php](#renderphp)
  - [view.js](#viewjs)
- [Interactivity API directives](#interactivity-api-directives)
- [Global state, local context, and derived state](#global-state-local-context-and-derived-state)
  - [Global state](#global-state)
  - [Local context](#local-context)
  - [Derived state](#derived-state)
- [Actions and callbacks](#actions-and-callbacks)
- [How to build an interactive block](#how-to-build-an-interactive-block)
  - [The edit.js file](#the-editjs-file)
  - [The render.php file](#the-renderphp-file)
  - [The view.js file](#the-viewjs-file)
- [Summary](#summary)

---

Author
:   [Carlo Daniele](https://kinsta.com/blog/author/carlodaniele/ "Posts by Carlo Daniele")

Updated
:   November 10, 2025

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![](https://kinsta.com/wp-content/uploads/2025/10/how-to-create-interactive-blocks-1024x512.png)

In previous posts on this blog, we have explored WordPress block development from various angles. We have examined the development of both [static](https://kinsta.com/blog/gutenberg-blocks/) and [dynamic](https://kinsta.com/blog/dynamic-blocks/) blocks and [extended the functionality of core blocks](https://kinsta.com/blog/gutenberg-plugin/). However, the approach we have taken so far has essentially allowed us to create standard blocks that did not react to user interactions in real time. In short, these blocks were non-interactive.

In this article, we will explore a new approach to block development, which will allow us to create interactive blocks thanks to a new, powerful WordPress API: the **WordPress Interactivity API**. Introduced in [WordPress 6.5](https://kinsta.com/blog/wordpress-6-5/#interactivity-api), this API enables you to create blocks that react in real time to user interactions, allowing you to create rich user experiences and make your sites attractive, dynamic, and engaging.

There’s a lot to talk about, but before we begin, let’s take a look at the essential requirements!

## What you need before you start with the Interactivity API

As the Interactivity API is based on [React](https://kinsta.com/blog/what-is-react-js/), you will need at least a basic knowledge of [server-side JavaScript](https://kinsta.com/blog/what-is-node-js/) and React, as well as build tools such as [npm](https://kinsta.com/blog/what-is-npm/) and npx. You will also need a thorough understanding of [WordPress development](https://kinsta.com/blog/wp-scripts-development/) and the [Gutenberg block editor](https://kinsta.com/blog/gutenberg-wordpress-editor/).

Once you have acquired the necessary skills, you will need a [local development environment](https://kinsta.com/blog/mamp-alternative/) that enables you to quickly and easily launch a WordPress site. We recommend [DevKinsta](https://kinsta.com/devkinsta/), our local development suite designed specifically for WordPress. With DevKinsta, you can set up a new local WordPress site in just a few clicks and customise it in detail.

When you create a new WordPress project in DevKinsta, you can set the following options:

- Top Level domain: Default .local
- PHP version
- Database name
- Enable HTTPS
- WordPress details
- WordPress auto update
- Multisite

Additionally, you can import an existing MyKinsta website from a backup.

![Configuring a local website in DevKinsta](https://kinsta.com/wp-content/uploads/2025/10/devkinsta-new-website.png)

Configuring a local website in DevKinsta

## What is the Interactivity API?

The Interactivity API is a WordPress-native API that enables you to add interactivity to Gutenberg blocks and, consequently, to posts and pages on a WordPress site. It is a lightweight, modern solution that takes a [declarative approach](https://developer.wordpress.org/block-editor/reference-guides/interactivity-api/core-concepts/the-reactive-and-declarative-mindset/) to managing user interactions.

Creating an interactive block from scratch requires advanced PHP and [server-side JavaScript](https://developer.wordpress.org/block-editor/reference-guides/interactivity-api/core-concepts/server-side-rendering/) development skills. However, there is no need to reinvent the wheel with every new project, as WordPress provides a [template for creating interactive blocks](https://developer.wordpress.org/block-editor/reference-guides/packages/packages-create-block-interactive-template/):

```
npx @wordpress/create-block --template @wordpress/create-block-interactive-template
```

This template includes everything you need to scaffold an interactive block, including two working examples you can use as a reference for your first project: a button to toggle the current theme and a button to expand/collapse a paragraph.

To get started, open your favourite command line tool, navigate to the **Plugins** directory of your local WordPress installation, and type the following:

```
npx @wordpress/create-block your-interactive-block --template @wordpress/create-block-interactive-template
```

Allow a few moments for the installation to complete, then open your project folder using your preferred [code editor](https://kinsta.com/blog/free-html-editor/). We recommend using [Visual Studio Code](https://kinsta.com/blog/best-text-editors/#visual-studio-code), but you can use whichever editor you feel most comfortable with.

![An interactive block in Visual Studio Code](https://kinsta.com/wp-content/uploads/2025/09/interactive-block.png)

The interactive block project provided by the `@wordpress/create-block-interactive-template`

From the command line, navigate to the new plugin’s folder and [start the development server](https://developer.wordpress.org/block-editor/getting-started/quick-start-guide/#basic-usage) using the following command:

```
npm start
```

From now on, any changes you make to your block will be visible in real time in your WordPress installation.

Next, in your WordPress admin, navigate to the **Plugins** screen and activate the **Interactivity API** plugin that you have just created. Create a new post or page, then search for **Your interactive block** in the block inserter and add it to your content. Save the post and preview it on the frontend. You will see a yellow block containing two buttons. The first button changes the background color of the block, and the second button shows or hides the paragraph content.

![An example interactive block](https://kinsta.com/wp-content/uploads/2025/09/interactivity-api-example.png)

An example interactive block provided by the `@wordpress/create-block-interactive-template`

Now that you have a plugin to refer to for the topics covered in this article, we can move on and explore interactive blocks more deeply.

## The structure of interactive blocks

The structure of interactive blocks is the same as [traditional blocks](https://kinsta.com/blog/gutenberg-blocks/#a-walkthrough-of-the-starter-block-scaffolding). You will still need a `package.json`, a `block.json`, an `edit.js` file, and a `style.scss` file. Additionally, you will need a `render.php` file for server-side rendering and a `view.js` file to handle frontend interactivity.

Let’s take a look at the specific bricks of an interactive block by breaking down the individual files of the starter project.

### package.json

The `package.json` file is [used in Node projects](https://docs.npmjs.com/cli/v7/configuring-npm/package-json) to identify your project, manage scripts, and manage and install dependencies during development.

The following is the `package.json` for the interactive block provided by the `create-block-interactive-template`:

```
{
	"name": "your-interactive-block",
	"version": "0.1.0",
	"description": "An interactive block with the Interactivity API.",
	"author": "The WordPress Contributors",
	"license": "GPL-2.0-or-later",
	"main": "build/index.js",
	"scripts": {
		"build": "wp-scripts build --experimental-modules",
		"format": "wp-scripts format",
		"lint:css": "wp-scripts lint-style",
		"lint:js": "wp-scripts lint-js",
		"packages-update": "wp-scripts packages-update",
		"plugin-zip": "wp-scripts plugin-zip",
		"start": "wp-scripts start --experimental-modules"
	},
	"dependencies": {
		"@wordpress/interactivity": "latest"
	},
	"files": [
		"[^.]*"
	],
	"devDependencies": {
		"@wordpress/scripts": "^30.24.0"
	}
}
```

The `scripts` and `dependencies` sections are particularly important here.

- `build`: Compiles source code into JavaScript for production. The `--experimental-modules` option enables support for WordPress [script modules](https://make.wordpress.org/core/2024/03/04/script-modules-in-6-5/).
- `start`: Starts the development server. Note that the `--experimental-modules` option is specified again.
- `dependencies`: Includes runtime dependencies with the latest package of the Interactivity API.

### block.json

The `block.json` file is the manifest for your Gutenberg block. It specifies metadata, media, scripts, and styles to load. By default, the `create-block-interactive-template` generates the following `block.json`:

```
{
	"$schema": "https://schemas.wp.org/trunk/block.json",
	"apiVersion": 3,
	"name": "create-block/your-interactive-block",
	"version": "0.1.0",
	"title": "Your Interactive Block",
	"category": "widgets",
	"icon": "media-interactive",
	"description": "An interactive block with the Interactivity API.",
	"example": {},
	"supports": {
		"interactivity": true
	},
	"textdomain": "your-interactive-block",
	"editorScript": "file:./index.js",
	"editorStyle": "file:./index.css",
	"style": "file:./style-index.css",
	"render": "file:./render.php",
	"viewScriptModule": "file:./view.js"
}
```

The following fields are essential for an interactive block:

- `apiVersion`: `3` is the latest version of the Block API and supports the latest block features, such as Script Modules.
- `supports`: Specifies block supports. `"interactivity": true` adds support for the Interactivity API.
- `render`: Specifies the PHP file responsible for rendering in the frontend. This file is where you add the directives that make a block interactive.
- `viewScriptModule`: Specifies the JavaScript file that contains the interactivity logic. This file is only loaded on the frontend and only if the page contains the interactive block.

### render.php

The `render.php` is where you build the markup of a dynamic block. To make your block interactive, you need to add attributes that make the DOM elements of your block interactive.

The `render.php` file in the starter project looks like the following:

```
<?php
/**
 * PHP file to use when rendering the block type on the server to show on the front end.
 *
 * The following variables are exposed to the file:
 *     $attributes (array): The block attributes.
 *     $content (string): The block default content.
 *     $block (WP_Block): The block instance.
 *
 * @see https://github.com/WordPress/gutenberg/blob/trunk/docs/reference-guides/block-api/block-metadata.md#render
 */

// Generates a unique id for aria-controls.
$unique_id = wp_unique_id( 'p-' );

// Adds the global state.
wp_interactivity_state(
	'create-block',
	array(
		'isDark'    => false,
		'darkText'  => esc_html__( 'Switch to Light', 'your-interactive-block' ),
		'lightText' => esc_html__( 'Switch to Dark', 'your-interactive-block' ),
		'themeText'	=> esc_html__( 'Switch to Dark', 'your-interactive-block' ),
	)
);
?>

<div
	<?php echo get_block_wrapper_attributes(); ?>
	data-wp-interactive="create-block"
	<?php echo wp_interactivity_data_wp_context( array( 'isOpen' => false ) ); ?>
	data-wp-watch="callbacks.logIsOpen"
	data-wp-class--dark-theme="state.isDark"
>
	<button
		data-wp-on--click="actions.toggleTheme"
		data-wp-text="state.themeText"
	></button>

	<button
		data-wp-on--click="actions.toggleOpen"
		data-wp-bind--aria-expanded="context.isOpen"
		aria-controls="<?php echo esc_attr( $unique_id ); ?>"
	>
		<?php esc_html_e( 'Toggle', 'your-interactive-block' ); ?>
	</button>

	<p
		id="<?php echo esc_attr( $unique_id ); ?>"
		data-wp-bind--hidden="!context.isOpen"
	>
		<?php
			esc_html_e( 'Your Interactive Block - hello from an interactive block!', 'your-interactive-block' );
		?>
	</p>
</div>
```

Here’s what this code does:

- `wp_interactivity_state`: Gets and/or sets the [initial global state](https://developer.wordpress.org/reference/functions/wp_interactivity_state/) of an Interactivity API store.
- `data-wp-interactive`: [Enables the Interactivity API](https://developer.wordpress.org/block-editor/reference-guides/interactivity-api/api-reference/#wp-interactive) on the DOM element and its children. Its value must be the unique namespace of your plugin or block.
- `wp_interactivity_data_wp_context()`: Generates the `data-wp-context` directive, which [provides a local state](https://developer.wordpress.org/reference/functions/wp_interactivity_data_wp_context/) to a specific HTML node and its children.
- `data-wp-watch`: [Runs a callback](https://developer.wordpress.org/block-editor/reference-guides/interactivity-api/api-reference/#wp-watch) when a node is created and every time the state or context changes.
- `data-wp-class--dark-theme`: Adds or removes the `dark-theme` class to the HTML element.
- `data-wp-on--click`: [Runs code synchronously](https://developer.wordpress.org/block-editor/reference-guides/interactivity-api/api-reference/#wp-on) on click event.
- `data-wp-text`: [Sets the inner text](https://developer.wordpress.org/block-editor/reference-guides/interactivity-api/api-reference/#wp-text) of the HTML element.
- `data-wp-bind--aria-expanded` and `data-wp-bind--hidden`: [Set HTML attributes](https://developer.wordpress.org/block-editor/reference-guides/interactivity-api/api-reference/#wp-bind) (`aria-expanded` and `hidden`) on the corresponding elements based on a boolean or string value.

### view.js

This file [defines the Store](https://developer.wordpress.org/block-editor/reference-guides/interactivity-api/api-reference/#on-the-client-side) that contains the logic and data needed for the block behaviour, including state, actions, and callbacks.

The following is the `view.js` file generated by the starter project:

```
/**
 * WordPress dependencies
 */
import { store, getContext } from '@wordpress/interactivity';

const { state } = store( 'create-block', {
	state: {
		get themeText() {
			return state.isDark ? state.darkText : state.lightText;
		},
	},
	actions: {
		toggleOpen() {
			const context = getContext();
			context.isOpen = ! context.isOpen;
		},
		toggleTheme() {
			state.isDark = ! state.isDark;
		},
	},
	callbacks: {
		logIsOpen: () => {
			const { isOpen } = getContext();
			// Log the value of `isOpen` each time it changes.
			console.log( `Is open: ${ isOpen }` );
		},
	},
} );
```

- `store`: The main function used to create and register the Global state and logic of the block.
- `getContext`: A function used within actions and callbacks to access the local state (the `context`) of the DOM element that triggered the event.
- `state`: Defines the global reactive data of the block.
- `actions`: Includes the functions that define the logic and change the state.
- `callbacks`: Includes the functions to execute in response to specific events or state changes automatically.

It’s a lot to take in, but don’t worry! Everything will become clearer once you have read the following sections.

Now, let’s examine the key concepts of the Interactivity API: directives, store, state, actions, and callbacks.

## Interactivity API directives

Like other frontend libraries such as Alpine.js and [Vue.js](https://kinsta.com/topic/vue-js/), the Interactivity API uses special HTML attributes that enable you to respond to events on the page, update the application’s state, manipulate the DOM, apply CSS styles, handle user input, and much more.

These attributes are called **directives** and allow you to connect your markup to the underlying JavaScript logic.

Below is a list of the directives that you will use the most.

| Function | Directive | Description |
| --- | --- | --- |
| Activation/Namespace | `data-wp-interactive` | Activates the API for the element and its children. The value must be set to the unique identifier of your plugin. |
| Local state | `data-wp-context` | Provides a local state (“context”) for the current element and all its children. It accepts a JSON object. Note that it’s recommended to use `wp_interactivity_data_wp_context()` to set it in PHP (typically `render.php`). |
| Attribute Binding | `data-wp-bind--[attribute]` | Sets an HTML attribute (e.g., `disabled`, `value`) based on a reactive state or context value (a boolean or string value). |
| Text Modification | `data-wp-text` | Sets the element’s inner text content. It accepts only strings. |
| CSS Class Toggling | `data-wp-class--[classname]` | Adds or removes a CSS class depending on a boolean value. |
| Inline styling | `data-wp-style--[css-property]` | Adds or removes an inline style class depending on a boolean value. |
| Event Handling | `data-wp-on--[event]` | Executes code in response to standard DOM events such as `click` or `mouseover`. |
| Initial Execution | `data-wp-init` | Runs a callback function once, only when the node is created. |
| State Watching | `data-wp-watch` | Runs a callback when the node is created and again whenever the state or context changes. |
| List Iteration | `data-wp-each` | Renders a list of elements. |

For a complete list of directives, check the [Interactivity API dev notes](https://make.wordpress.org/core/2024/03/04/interactivity-api-dev-note/) and [API reference](https://developer.wordpress.org/block-editor/reference-guides/interactivity-api/api-reference/).

## Global state, local context, and derived state

Before you start using the Interactivity API, it is essential that you familiarize yourself with the [fundamental concepts of state management](https://developer.wordpress.org/block-editor/reference-guides/interactivity-api/core-concepts/undestanding-global-state-local-context-and-derived-state/) in frontend development. Those who regularly develop with React, Vue, or Angular will already be familiar with these concepts. For those who are new to these technologies, it may be helpful to provide some general definitions.

### Global state

**Global state** refers to the set of data accessible from almost all components of an application. In the case of the Interactivity API, for example, the global state affects all interactive blocks on the page, keeping them in sync. For instance, when a user adds a product to their basket, this is reflected in the shopping cart block.

When using the Interactivity API, you should set the initial values of the Global state on the server using the `wp_interactivity_state()` function. In the starter project described above, this function is used in the `render.php` file as follows:

```
// Adds the global state.
wp_interactivity_state(
	'create-block',
	array(
		'isDark'    => false,
		'darkText'  => esc_html__( 'Switch to Light', 'your-interactive-block' ),
		'lightText' => esc_html__( 'Switch to Dark', 'your-interactive-block' ),
		'themeText'	=> esc_html__( 'Switch to Dark', 'your-interactive-block' ),
	)
);
```

[This function](https://developer.wordpress.org/reference/functions/wp_interactivity_state/) accepts two arguments:

- A unique identifier for the store namespace. In this case, `create-block`.
- An array of data that will be merged with the existing store namespace, if it exists.

The initial global state values are then used to render the page. You can access the Global state values directly by using `state` in the directive attribute values, as in the following code:

```
<button
	data-wp-on--click="actions.toggleTheme"
	data-wp-text="state.themeText"
></button>
```

The `store()` function provides the main access point to the Global state from JavaScript, limited to the selected namespace. Going back to the starter project code, the `store()` function is used in the `view.js` file as follows:

```
import { store, getContext } from '@wordpress/interactivity';

const { state } = store( 'create-block', {
	state: { ... },
	actions: { ... },
	callbacks: { ... },
} );
```

To access the global state, you can use the `state` property:

```
actions: {
	toggleTheme() {
		state.isDark = ! state.isDark;
	},
},
```

### Local context

**Local context** is data that can only be accessed by a specific component and its direct children. A WordPress interactive block provides an independent state for the block and its nested elements.

When using the Interactivity API, you can access the Local context using the `getContext()` function. Referring again to the starter project, when the user clicks on the Toggle button, the `toggleOpen()` action is triggered, accessing the component’s Local context:

```
actions: {
	toggleOpen() {
		const context = getContext();
		context.isOpen = ! context.isOpen;
	},
},
```

- `getContext()`: Retrieves the block’s local state object. This object’s properties are defined in the component markup (`render.php`) using the `wp_interactivity_data_wp_context()` function.
- `context.isOpen = ! context.isOpen;`: Switches the value of the `isOpen` property in the component’s Local context.

### Derived state

**Derived state** refers to data calculated dynamically from existing Global or Local state.

For instance, take a look at the code in the `view.js` file, specifically in this section:

```
const { state } = store( 'create-block', {
	state: {
		get themeText() {
			return state.isDark ? state.darkText : state.lightText;
		},
	},
	...
}
```

This block defines the `themeText` Derived state within the Global state defined in the `create-block` namespace.

- `get themeText()` is not a fixed value, but rather a function that is executed each time you attempt to read the `themeText` property. It should not be invoked like a normal function because the Interactivity API treats it as a state property and automatically recalculates its value whenever the values of other state properties change. In the above code, the `themeText` property value is recalculated each time the `isDark` property value changes. If `state.isDark` is `true`, then `themeText` takes the value of `state.darkText`; otherwise, it takes the value of `state.lightText`.

For a more comprehensive overview of the concepts described in this section, see [Understanding global state, local context and derived state](https://developer.wordpress.org/block-editor/reference-guides/interactivity-api/core-concepts/undestanding-global-state-local-context-and-derived-state/).

## Actions and callbacks

Actions and callbacks determine the response to user interaction and state changes.

The `actions` section of an interactive block contains functions that are executed in response to user-generated events. These functions primarily serve to modify the Local or Global state of the component. Take the following code from the `view.js` file:

```
actions: {
	toggleOpen() {
		const context = getContext();
		context.isOpen = ! context.isOpen;
	},
	...
},
```

- In this section of code, the `toggleOpen()` function uses `getContext()` to access the Local context of the block that triggered the action to switch the value of the `isOpen` property.

Similarly, you can access the Global state:

```
actions: {
	...,
	toggleTheme() {
		state.isDark = ! state.isDark;
	},
},
```

- The `toggleTheme()` function accesses the global `state` object directly and changes the value of the `isDark` property.

Actions are triggered via the `data-wp-on--[event]` directive. For instance, in the `render.php` file, you will find the following button:

```
<button
	data-wp-on--click="actions.toggleOpen"
	data-wp-bind--aria-expanded="context.isOpen"
	aria-controls="<?php echo esc_attr( $unique_id ); ?>"
>
```

- In this HTML code, the `data-wp-on--click` attribute activates the `toggleOpen` action when the user clicks on the toggle button.

The `callbacks` section contains functions that are executed automatically when the data on which they depend changes. Their purpose is to produce side effects in response to a state change.

In the basic project generated by `create-block-interactive-template`, you will find the following callback:

```
callbacks: {
	logIsOpen: () => {
		const { isOpen } = getContext();
		// Log the value of `isOpen` each time it changes.
		console.log( `Is open: ${ isOpen }` );
	},
},
```

- The `logIsOpen` function uses the `isOpen` variable, which is available in the Local context.
- The callback retrieves the value of `isOpen` using `getContext()`.
- Every time the value of `isOpen` changes, the function throws a message to the browser console.

![A message in the console informs the user of the change in the Local context.](https://kinsta.com/wp-content/uploads/2025/10/toggle-is-open.png)

A message in the console informs the user of the change in the Local context.

## How to build an interactive block

Now that we’ve covered the theory, it’s time to start having some fun with code! In the second part of this guide, you’ll learn how to create an interactive block that enables users to add products to an ideal shopping basket, with quantities and totals that update automatically. This is a demonstration example, but we hope it provides a clear understanding of how to use state, actions, and callbacks.

![The interactive block in the editor](https://kinsta.com/wp-content/uploads/2025/10/interactive-counter-editor-view.png)

The interactive block in the editor

We will create a block called **Interactive Counter** using the `create-block-interactive-template`. To get started, open your command line tool and type the following:

```
npx @wordpress/create-block interactive-counter --template @wordpress/create-block-interactive-template
```

Next, navigate to your new project directory and run the first build.

```
cd interactive-counter && npm run build
```

Open the project in your code editor now. In the `/src` directory, look for the `block.json` file. It should look something like this:

```
{
	"$schema": "https://schemas.wp.org/trunk/block.json",
	"apiVersion": 3,
	"name": "create-block/interactive-counter",
	"version": "0.1.0",
	"title": "Interactive Counter",
	"category": "widgets",
	"icon": "media-interactive",
	"description": "An interactive block with the Interactivity API.",
	"supports": {
		"interactivity": true
	},
	"textdomain": "interactive-counter",
	"editorScript": "file:./index.js",
	"editorStyle": "file:./index.css",
	"style": "file:./style-index.css",
	"render": "file:./render.php",
	"viewScriptModule": "file:./view.js"
}
```

Feel free to customize it, but ensure that you don’t modify the essential fields described above.

### The edit.js file

The next step is to create the block that will appear in the editor. To do this, you will need to edit the `/src/edit.js` file. Open the file and modify it as follows:

```
import { __ } from '@wordpress/i18n';
import { useBlockProps } from '@wordpress/block-editor';
import './editor.scss';

export default function Edit({ attributes, setAttributes }) {
	const blockProps = useBlockProps();
	const products = [
		{ id: 'product1', name: __('Product 1', 'interactive-counter'), price: 10.00 },
		{ id: 'product2', name: __('Product 2', 'interactive-counter'), price: 15.00 },
		{ id: 'product3', name: __('Product 3', 'interactive-counter'), price: 20.00 },
	];

	return (
		<div {...blockProps}>
			<h3>{__('Shopping Cart', 'interactive-counter')}</h3>
			<ul>
				{products.map((product) => (
					<li key={product.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
						<span style={{ flex: 1 }}>{product.name} - ${product.price.toFixed(2)}</span>
						<div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
							<button disabled>-</button>
							<span>0</span>
							<button disabled>+</button>
						</div>
						<span style={{ flex: 1, textAlign: 'right' }}>
							{__('Subtotal:', 'interactive-counter')} $0.00
						</span>
					</li>
				))}
			</ul>
			<div style={{ borderTop: '1px solid #ccc', paddingTop: '15px' }}>
				<p style={{ display: 'flex', justifyContent: 'space-between' }}>
					<strong>{__('Subtotal:', 'interactive-counter')}</strong>
					<span>$0.00</span>
				</p>
				<p style={{ display: 'flex', justifyContent: 'space-between' }}>
					<strong>{__('Tax (22%):', 'interactive-counter')}</strong>
					<span>$0.00</span>
				</p>
				<p style={{ display: 'flex', justifyContent: 'space-between' }}>
					<strong>{__('Total:', 'interactive-counter')}</strong>
					<span>$0.00</span>
				</p>
			</div>
			<p>{__('Quantities and totals will be interactive in the frontend.', 'interactive-counter')}</p>
		</div>
	);
}
```

This code generates a custom block in the back end. The block will be interactive only in the front end. For more details on the `/src/edit.js` file, please refer to our Gutenberg [block development](https://kinsta.com/blog/gutenberg-blocks/) [guides](https://kinsta.com/blog/dynamic-blocks/).

### The render.php file

The next file to edit is `/src/render.php`. Open the file and replace the existing code with the following:

```
<?php
/**
 * Render callback for the interactive-counter block.
 */

$products = [
	['id' => 'product1', 'name' => __('Product 1', 'interactive-counter'), 'price' => 10.00],
	['id' => 'product2', 'name' => __('Product 2', 'interactive-counter'), 'price' => 15.00],
	['id' => 'product3', 'name' => __('Product 3', 'interactive-counter'), 'price' => 20.00],
];

// Initialize global state
wp_interactivity_state('interactive-counter', [
	'products' => array_map(function ($product) {
		return [
			'id' => $product['id'],
			'name' => $product['name'],
			'price' => $product['price'],
			'quantity' => 0,
			'subtotal' => '0.00',
		];
	}, $products),
	'vatRate' => 0.22,
]);
```

Here’s what this code does:

- First, it creates a hard-coded array of products. Each product has an ID, a name, and a price.
- Next, it initializes the Global state with `wp_interactivity_state`. The first parameter is the store name, which must match that used in `view.js`.
- Then, it maps the previous array of products to a new `products` array, adding quantity and subtotal to the properties of the original array. This new array provides the data structure that you will use in `view.js`.
- `vatRate` sets the default value for tax calculation.

Next, add the following to the above code:

```
<div <?php echo get_block_wrapper_attributes(); ?> data-wp-interactive="interactive-counter" data-wp-init="callbacks.init">
	<h3><?php echo esc_html__('Cart', 'interactive-counter'); ?></h3>
	<ul>
		<?php foreach ($products as $index => $product) : ?>
			<li data-wp-context='{
				"productId": "<?php echo esc_attr($product['id']); ?>",
				"quantity": 0,
				"subtotal": "0.00"
			}' 
			data-wp-bind--data-wp-context.quantity="state.products[<?php echo $index; ?>].quantity" 
			data-wp-bind--data-wp-context.subtotal="state.products[<?php echo $index; ?>].subtotal">
				<span class="product-name"><?php echo esc_html($product['name']); ?> - $<?php echo esc_html(number_format($product['price'], 2)); ?></span>
				<div class="quantity-controls">
					<button data-wp-on--click="actions.decrement">-</button>
					<span data-wp-text="context.quantity">0</span>
					<button data-wp-on--click="actions.increment">+</button>
				</div>
				<span class="product-subtotal">
					<?php echo esc_html__('Subtotal:', 'interactive-counter'); ?>
					$<span data-wp-text="context.subtotal">0.00</span>
				</span>
			</li>
		<?php endforeach; ?>
	</ul>
	<div class="totals">
		<p>
			<strong><?php echo esc_html__('Subtotal:', 'interactive-counter'); ?></strong>
			$ <span data-wp-text="state.subtotal">0.00</span>
		</p>
		<p>
			<strong><?php echo esc_html__('Tax (22%):', 'interactive-counter'); ?></strong>
			$ <span data-wp-text="state.vat">0.00</span>
		</p>
		<p>
			<strong><?php echo esc_html__('Total:', 'interactive-counter'); ?></strong>
			$ <span data-wp-text="state.total">0.00</span>
		</p>
	</div>
</div>
```

Here’s what this code does:

- The `get_block_wrapper_attributes()` function in the `div` container is a WordPress function that generates the standard attributes of a block. In this case, it generates the class attribute `"wp-block-create-block-interactive-counter"`.
- The `data-wp-interactive` attribute makes this block interactive.
- The `data-wp-init` attribute triggers the `init` callback defined in `view.js`.
- The `foreach` loop generates a list item for each product in the `products` array.
- `data-wp-context` defines the Local context for the block.
- `data-wp-bind` binds the value of `data-wp-context.quantity` to the global `state.products[$index].quantity` property.
- The same happens in the line below with the subtotal.
- The following two buttons activate the `decrement` and `increment` actions thanks to the `data-wp-on--click` attribute.
- The `data-wp-text` attribute in the `span` updates the element’s content based on the current value of `context.quantity`.

The rest of the code is self-explanatory, so let’s move on to the next file.

### The view.js file

This file contains the logic for your interactive block.

```
import { store, getContext } from '@wordpress/interactivity';

store('interactive-counter', {
	state: {
		get subtotal() {
			const { products } = store('interactive-counter').state;
			return products
				.reduce((sum, product) => sum + product.price * (product.quantity || 0), 0)
				.toFixed(2);
		},
		get vat() {
			const { subtotal, vatRate } = store('interactive-counter').state;
			return (subtotal * vatRate).toFixed(2);
		},
		get total() {
			const { subtotal, vat } = store('interactive-counter').state;
			return (parseFloat(subtotal) + parseFloat(vat)).toFixed(2);
		},
	},
	actions: {
		increment: () => {
			const context = getContext();
			const { products } = store('interactive-counter').state;
			const product = products.find(p => p.id === context.productId);
			if (product) {
				product.quantity = (product.quantity || 0) + 1;
				product.subtotal = (product.price * product.quantity).toFixed(2);
				context.quantity = product.quantity;
				context.subtotal = product.subtotal;
				console.log(`Incremented ${context.productId}:`, { quantity: product.quantity, subtotal: product.subtotal, context });
			} else {
				console.warn('Product not found:', context.productId);
			}
		},
		decrement: () => {
			const context = getContext();
			const { products } = store('interactive-counter').state;
			const product = products.find(p => p.id === context.productId);
			if (product && (product.quantity || 0) > 0) {
				product.quantity -= 1;
				product.subtotal = (product.price * product.quantity).toFixed(2);
				context.quantity = product.quantity;
				context.subtotal = product.subtotal;
				console.log(`Decremented ${context.productId}:`, { quantity: product.quantity, subtotal: product.subtotal, context });
			} else {
				console.warn('Cannot decrement:', context.productId, product?.quantity);
			}
		},
	},
	callbacks: {
		init: () => {
			const { products } = store('interactive-counter').state;
			products.forEach((product, index) => {
				product.quantity = 0;
				product.subtotal = '0.00';
				console.log(`Initialized product ${index}:`, { id: product.id, quantity: product.quantity, subtotal: product.subtotal });
			});
		},
	},
});
```

This file defines the store for the `interactive-counter` namespace. It manages state, actions, and callbacks:

```
store('interactive-counter', {
	state: { ... },
	actions: { ... },
	callbacks: { ... },
});
```

Let’s take a closer look.

- `state`: Defines three computed state properties (getters): `subtotal`, `vat`, and `total`. These functions retrieve values from the Global state and calculate the values to be returned.
- `actions`: Defines two functions executed on events: `increment` and `decrement`. These functions retrieve the `products` array from the Global state, retrieve the current product from the Local context based on `context.productId`, update the current product’s property values (`quantity` and `subtotal`), and sync the Local context with the new values.
- `callbacks`: Defines an `init` callback for initialization.

The following image shows the interactive block in the frontend.

![An interactive counter built with the Interactivity API](https://kinsta.com/wp-content/uploads/2025/10/interactive-counter.png)

An interactive counter built with the Interactivity API

## Summary

In this article, we introduced the main features of the WordPress Interactivity API. We delved into key concepts such as Global state, Local context, directives, actions, and callbacks. You learnt how to create an interactive block from scratch using the `@wordpress/create-block-interactive-template`, and we put this into practice by creating a real block that interacts with user input.

We hope that we have provided you with the necessary tools and knowledge to create fantastic, dynamic, and interactive WordPress websites using the WordPress Interactivity API.

Happy coding!

Carlo Daniele
[Kinsta](https://kinsta.com/)

Carlo is a passionate lover of webdesign and front-end development. He has been playing with WordPress for more than 20 years, also in collaboration with Italian and European universities and educational institutions. He has written hundreds of articles and guides about WordPress, published both on Italian and international websites, as well as on printed magazines. You can find him on [LinkedIn](https://www.linkedin.com/in/carlodaniele/).

- [Website](https://frammentidicodice.com/)
- [Twitter](https://twitter.com/carlodaniele)
