---
url: "https://kinsta.com/blog/wordpress-block-bindings-api/"
title: "The WordPress Block Bindings API: What it is and how to use it to build dynamic websites"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "WordPress Development", "The WordPress Block Bindings API: What it is and how to use it to build dynamic websites"]
kinsta_last_updated: "2025-12-31T07:10:31+00:00"
sitemap_lastmod: "2025-12-31T07:10:31"
fetched_at: "2026-10-07T22:43:00Z"
sha256: "50867b23e9649643f848639427bca8e81921929c9a05cac226f5ffe4a44c2843"
body_chars: 30579
extracted_with: "main article"
status: "live"
---

# The WordPress Block Bindings API: What it is and how to use it to build dynamic websites

**Section:** Resource Center > Blog > WordPress Development > The WordPress Block Bindings API: What it is and how to use it to build dynamic websites
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/wordpress-block-bindings-api/
**Kinsta last updated:** 2025-12-31T07:10:31+00:00

## On this page

- [The Block Bindings API: Basic concepts](#the-block-bindings-api-basic-concepts)
- [How to register custom Block Bindings data sources: A real-life example](#how-to-register-custom-block-bindings-data-sources-a-real-life-example)
  - [Step 1: Create a basic plugin](#step-1-create-a-basic-plugin)
  - [Step 2: Register post meta fields](#step-2-register-post-meta-fields)
  - [Step 3: Register Block Bindings source](#step-3-register-block-bindings-source)
  - [Step 4: Retrieve data from an external source](#step-4-retrieve-data-from-an-external-source)
- [How to use the Block Bindings API](#how-to-use-the-block-bindings-api)
- [How to create a UI for your custom Block Bindings sources](#how-to-create-a-ui-for-your-custom-block-bindings-sources)
- [What else can you do with the Block Bindings API?](#what-else-can-you-do-with-the-block-bindings-api)

---

Author
:   [Carlo Daniele](https://kinsta.com/blog/author/carlodaniele/ "Posts by Carlo Daniele")

Updated
:   December 31, 2025

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![](https://kinsta.com/wp-content/uploads/2025/12/the-wordpress-block-bindings-api-what-it-is-and-how-to-use-it-to-build-dynamic-websites-1024x512.png)

The Block Bindings API is a powerful tool in the block editor that lets you connect any data source to a block’s attributes.

This API was first introduced in [WordPress 6.5](https://kinsta.com/blog/wordpress-6-5/#block-bindings-api) and, in its initial implementation, enabled WordPress users to display custom field values within posts and pages.

The Block Bindings API serves as the foundation for other robust WordPress features. Examples include [Synced pattern overrides](https://kinsta.com/blog/wordpress-6-6/#synced-pattern-overrides) and the **Post Date** block variation introduced in [WordPress 6.9](https://kinsta.com/blog/wordpress-6-9/#block-bindings-api-improvements).

So, exactly what is the Block Bindings API? And what is it used for? We will provide a simple introduction and a real-world example showing how to create bindings between Gutenberg blocks and external data sources.

Let’s get to work.

## The Block Bindings API: Basic concepts

As we mentioned above, the Block Bindings API allows you to create bindings between a data source and the attributes of a block.

If you’re not familiar with block attributes, navigate to the `src` directory of the Gutenberg project’s block library on GitHub, find the Paragraph block, and open the [`block.json` file](https://github.com/WordPress/gutenberg/blob/trunk/packages/block-library/src/paragraph/block.json). The `attributes` property provides a list of the Paragraph block’s attributes.

```
"attributes": {
	"content": {
		"type": "rich-text",
		"source": "rich-text",
		"selector": "p",
		"role": "content"
	},
	"dropCap": {
		"type": "boolean",
		"default": false
	},
	"placeholder": {
		"type": "string"
	},
	"direction": {
		"type": "string",
		"enum": [ "ltr", "rtl" ]
	}
},
```

The following blocks support the Block Bindings API as of WordPress 6.9 and can therefore be linked to your custom fields:

| Supported blocks | Attributes |
| --- | --- |
| Paragraph | content |
| Title | content |
| Image | id, url, alt, title, caption |
| Button | text, url, linkTarget, rel |

To connect your custom fields to Gutenberg blocks, you must first [register them](https://developer.wordpress.org/reference/functions/register_post_meta/). The following code registers a custom field via a WordPress plugin or your theme’s [`functions.php` file](https://kinsta.com/blog/wordpress-functions-php/):

```
add_action( 'init', function() {
	register_post_meta( 'your-post-type', 'myplugin_meta_key', [
		'show_in_rest'  => true,
		'single'        => true,
		'type'          => 'string',
		'description'   => __( 'City name', 'textdomain' ),
		'auth_callback' => 'is_user_logged_in',
	] );
} );
```

`register_post_meta` accepts an array of attributes that define the characteristics of custom fields, and the documentation provides a [complete list](https://developer.wordpress.org/reference/functions/register_meta/) of them. To make a custom field available to the Block Bindings API, you must set `show_in_rest` to true. As of WordPress 6.9, `string` is the only supported type.

To see the Block Bindings API in action with custom fields, create a new WordPress plugin and register a meta field with the code shown above.

```
<?php
/**
 * Plugin Name: Block Bindings example
 * Description: Example plugin that uses the Block Bindings API.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL2 or later
 * Text Domain: block-bindings-example
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

add_action( 'init', function() {
	register_post_meta( '', 'block_bindings_image_url', [
		'show_in_rest'  => true,
		'single'	    => true,
		'type'		    => 'string',
		'description'   => __( 'City name', 'block-bindings-example' ),
		'auth_callback' => 'is_user_logged_in',
	] );
} );
```

In your WordPress dashboard, activate the plugin. Then, navigate to the Posts screen and create a new post. When you select a supported block, the **Attributes** panel in the Block Settings sidebar will display the list of attributes that can be bound to a registered custom field.

![A screenshot showing the Image block attributes that support Block Bindings](https://kinsta.com/wp-content/uploads/2025/12/image-block-attributes-block-bindings-ui.png)

Image block attributes that support Block Bindings

Open the **Options** menu in the top right corner and select **Preferences**. In the **General** tab, locate the **Advanced** section and enable custom fields. Save your changes, wait for the page to reload, then return to the editor.

![A screenshot of the block editor's preferences.](https://kinsta.com/wp-content/uploads/2025/12/enable-custom-fields.png)

Enable custom fields in the editor’s Preferences.

Your next step is to insert an Image block. With the block selected, click the **+** icon in the **Attributes** panel and select the **url** attribute. The Attributes panel will then show a list of available meta fields. Select url again. Now, you will see the list of meta fields available for the current post type.

![A screenshot showing a custom field and the Block Bindings UI.](https://kinsta.com/wp-content/uploads/2025/12/attributes-panel-image-block.png)

Binding a custom field to the url attribute of an Image block in the Block Bindings UI.

Select your meta field and save the post. You should now see your image in both the editor and the frontend.

![A screenshot of the block editor with an Image block with the url attribute bound to a custom field value.](https://kinsta.com/wp-content/uploads/2025/12/block-bindings-image-url.jpg)

An Image block with the url attribute bound to a custom field value.

Starting with [version 6.7 of WordPress](https://kinsta.com/blog/wordpress-6-7/), you can use the Label attribute to display text in the editor interface. The following code block shows an example:

```
add_action( 'init', function() {
	register_post_meta( '', 'block_bindings_image_url', [
		'show_in_rest'  => true,
		'single'        => true,
		'type'          => 'string',
		'description'   => __( 'City image', 'block-bindings-example' ),
		'label'         => __('Image URL'),
		'auth_callback' => 'is_user_logged_in',
	] );
} );
```

![A screenshot showing custom field labels in the Block Bindings UI](https://kinsta.com/wp-content/uploads/2025/12/custom-field-label-in-block-bindings-ui.png)

Custom field labels in the Block Bindings UI

When you open the code editor, you can see a JSON object within the image block delimiter. The `metadata.bindings.url` property shows that the `url` of the image block is linked to a metadata field.

```
<!-- wp:image {
	"metadata":{
		"bindings":{
			"url":{
				"source":"core/post-meta",
				"args":{
					"key":"block_bindings_image_url"
				}
			}
		}
	}
} -->
<figure class="wp-block-image"><img alt="/></figure>
<!-- /wp:image -->
```

The `source` property specifies the data source for the block bindings. The `args.key` property establishes a reference to your meta field.

The most interesting aspect of the Block Bindings API is its ability to register custom data sources, which opens up some exciting new possibilities for developers. Next, we’ll explore how to use data from third-party services with the Block Bindings API.

## How to register custom Block Bindings data sources: A real-life example

Once you are familiar with the Block Bindings API’s basic concepts, we can move on to its more advanced and interesting aspects for developers.

As mentioned earlier, the Block Bindings API allows you to register custom data sources. This enables you to retrieve data from a remote source and/or manipulate raw data to generate useful information that can be automatically inserted into your content.

In this section, you learn how to maximize the potential of Block Bindings through a practical example that you can use as a foundation for developing your own custom applications.

Suppose you want to retrieve data from an external source and display it in your posts, pages, or [custom post types](https://kinsta.com/blog/wordpress-custom-post-types/). For instance, you might query a weather service API by sending a request with the latitude and longitude of a city to get real-time weather data, which you could then display on your site.

Thanks to the Block Bindings API, you can display the current temperature or provide your readers with the weather forecast for the coming days. You can also programmatically change the `url` attribute of one or more images on the page depending on weather conditions.

To add this feature to your WordPress website, you need to create a plugin. Follow these steps:

### Step 1: Create a basic plugin

The first step is to create the plugin files. Navigate to the `wp-content/plugins` directory of your WordPress installation and create a new folder called `block-bindings-example`. Inside this folder, add the following files:

```
/wp-content/plugins/
└── /block-bindings-example/
	├── block-bindings-example.php
	└── /includes/
		├── binding-sources.php
		├── meta-fields.php
		└── weather-api.php
```

Open the `block-bindings-example.php` file in your favorite [code editor](https://kinsta.com/blog/free-html-editor/) and add the following code:

```
<?php
/**
 * Plugin Name: Block Bindings Example
 * Description: Use WordPress Block Bindings API (6.5+) to dynamically bind weather data from Open-Meteo API to Gutenberg blocks using custom post meta and a custom binding source.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL2 or later
 * Text Domain: block-bindings-example
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit; // Exit if accessed directly
}

/**
 * Cache duration for weather data: 30 minutes
 * This reduces API calls and improves performance
 */
define( 'BB_WEATHER_CACHE_TIME', HOUR_IN_SECONDS / 2 );

require_once plugin_dir_path( __FILE__ ) . 'includes/meta-fields.php';
require_once plugin_dir_path( __FILE__ ) . 'includes/binding-sources.php';
require_once plugin_dir_path( __FILE__ ) . 'includes/weather-api.php';

/**
 * Setup function
 */
function bb_init_setup() {
	bb_register_post_meta();
	bb_register_binding_sources();
}
add_action( 'init', 'bb_init_setup' );
```

Here’s what this code does:

- The constant `BB_WEATHER_CACHE_TIME` determines how long weather data is cached. This reduces API calls, improves page performance, and lowers service costs.
- The `require_once` expressions include the necessary scripts to register meta fields, register the binding source, and retrieve data from the API.
- The setup function calls two functions that register the post meta fields and the custom binding sources.

### Step 2: Register post meta fields

The next step is to register the meta fields you need for your use case. Open the `meta-fields.php` file in the `includes` folder and add the following code:

```
<?php
/**
 * Registers custom post meta fields so they appear in the REST API and Block Bindings editor panel
 */
function bb_register_post_meta() {

	if ( ! function_exists( 'register_post_meta' ) ) {
		return;
	}

	register_post_meta( 'post', 'block_bindings_city_name', [
		'show_in_rest'  => true,
		'single'        => true,
		'type'          => 'string',
		'description'   => __( 'Add city name', 'block-bindings-example' ),
		'label'         => __( 'City name', 'block-bindings-example' ),
		'auth_callback' => 'is_user_logged_in',
	] );

	register_post_meta( 'post', 'block_bindings_image_url', [
		'show_in_rest'  => true,
		'single'        => true,
		'type'          => 'string',
		'description'   => __( 'Add city image URL', 'block-bindings-example' ),
		'label'         => __( 'City image URL', 'block-bindings-example' ),
		'auth_callback' => 'is_user_logged_in',
	] );

	register_post_meta( 'post', 'block_bindings_city_lat', [
		'show_in_rest'  => true,
		'single'        => true,
		'type'          => 'string',
		'description'   => __( 'Add city latitude', 'block-bindings-example' ),
		'label'         => __( 'Latitude', 'block-bindings-example' ),
		'auth_callback' => 'is_user_logged_in',
	] );

	register_post_meta( 'post', 'block_bindings_city_lng', [
		'show_in_rest'  => true,
		'single'        => true,
		'type'          => 'string',
		'description'   => __( 'Add city longitude', 'block-bindings-example' ),
		'label'         => __( 'Longitude', 'block-bindings-example' ),
		'auth_callback' => 'is_user_logged_in',
	] );
}
```

The `register_post_meta` function registers a meta key for use in posts. Note that to use meta fields registered this way with the Block Bindings API, you must set `show_in_rest` to `true` and `type` to `string`. See the [documentation](https://developer.wordpress.org/reference/functions/register_post_meta/) for more information.

### Step 3: Register Block Bindings source

It’s time to register your binding source. Open the `binding-sources.php` file and add the following code:

```
<?php
/**
 * Registers a custom Block Bindings source: bb/weather-condition
 */
function bb_register_binding_sources() {

	if ( ! function_exists( 'register_block_bindings_source' ) ) {
		return;
	}
	
	register_block_bindings_source(
		'bb/weather-condition',
		[
			'label'              => __( 'Weather Condition', 'block-bindings-example' ),
			'get_value_callback' => 'bb_get_weather_condition_value',
			'uses_context'       => [ 'postId' ], // We need postId to get meta values
		]
	);
}
```

The `register_block_bindings_source()` function requires the source name and a callback function that retrieves data from a source and returns the manipulated value.

Then, in the same `binding-sources.php` file, define the callback function.

```
function bb_get_weather_condition_value( array $source_args, WP_Block $block_instance ) {

	$key = $source_args['key'] ?? null;
	if ( ! $key ) {
		return null;
	}

	$post_id = bb_resolve_binding_post_id( $block_instance );

	if ( ! $post_id || $post_id <= 0 ) {
		error_log( 'BB DEBUG: Could not determine post ID for weather binding (bb/weather-condition)' );
		return null;
	}

	$weather_data = bb_fetch_and_cache_weather_data( $post_id );

	if ( ! is_array( $weather_data ) || ! isset( $weather_data[ $key ] ) ) {
		error_log( sprintf( 'BB DEBUG: Weather key "%s" is unavailable for post ID %d', $key, $post_id ) );
		return null;
	}

	$value = $weather_data[ $key ];

	// Special formatting: append °C symbol for temperature
	if ( $key === 'temperature' ) {
		return $value . '°C';
	}

	return $value;
}
```

Let’s break down this function:

- `$source_args['key']` identifies the data bound to the block attribute.
- The next line retrieves the ID of the current post with a call to the bb_resolve_binding_post_id() defined below.
- Then, it calls the `bb_fetch_and_cache_weather_data` function, which retrieves the data from the API. We will define this function in the next step.
- `$weather_data[$key]` contains the data provided by the API, such as temperature and weather state.
- If the key is `temperature`, it appends `°C` to the provided value.
- The function then returns the final value.

Next, define the function that retrieves the current post ID:

```
function bb_resolve_binding_post_id( WP_Block $block_instance ) {
	$post_id = $block_instance->context['postId'] ?? null;

	if ( $post_id && $post_id > 0 ) {
		return (int) $post_id;
	}

	$global_post_id = get_the_ID();
	if ( $global_post_id && $global_post_id > 0 ) {
		return (int) $global_post_id;
	}

	$queried_object_id = get_queried_object_id();
	if ( $queried_object_id && $queried_object_id > 0 ) {
		return (int) $queried_object_id;
	}

	return null;
}
```

### Step 4: Retrieve data from an external source

As mentioned above, we retrieve data from the [Open-Meteo service](https://open-meteo.com/) (free for non-commercial use).

To retrieve the current temperature and weather conditions, you need to send a request to the API that includes the latitude and longitude of a given location and the query var `current=weather_code,temperature_2m`. Below is an example request:

```
https://api.open-meteo.com/v1/forecast?latitude=-33.8717&longitude=151.2299¤t=weather_code,temperature_2m
```

The API provides a response similar to the following:

```
{
	"latitude": -33.8717,
	"longitude": 151.2299,
	"generationtime_ms": 0.030875205993652344,
	"utc_offset_seconds": 0,
	"timezone": "GMT",
	"timezone_abbreviation": "GMT",
	"elevation": 13.0,
	"current_units": {
		"time": "iso8601",
		"interval": "seconds",
		"weather_code": "wmo code",
		"temperature_2m":"°C"
	},
	"current": {
		"time": "2025-12-01T16:00",
		"interval": 900,
		"weather_code": 3,
		"temperature_2m":7.3
	}
}
```

![Open-Meteo response in Postman for Visual Studio Code](https://kinsta.com/wp-content/uploads/2025/12/postman-for-vsc.png)

Open-Meteo response in Postman for Visual Studio Code

Now that you know how to get the data you need, open the `weather-api.php` file and add the following code:

```
function bb_fetch_and_cache_weather_data( $post_id ) {
	$lat = get_post_meta( $post_id, 'block_bindings_city_lat', true );
	$lng = get_post_meta( $post_id, 'block_bindings_city_lng', true );

	// Normalize decimal separator: replace comma with dot (common in European formats)
	$lat = str_replace( ',', '.', trim( $lat ) );
	$lng = str_replace( ',', '.', trim( $lng ) );

	if ( ! is_numeric( $lat ) || ! is_numeric( $lng ) ) {
		error_log( 'BB DEBUG: Invalid latitude/longitude values after normalization' );
		return false;
	}

	$transient_key = 'bb_weather_data_' . $post_id;
	$cached_data   = get_transient( $transient_key );

	if ( $cached_data !== false ) {
		error_log( "BB DEBUG: Cache hit for post ID {$post_id}" );
		return $cached_data;
	}

	// Build Open-Meteo API URL
	$api_url = sprintf(
		'https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s¤t=weather_code,temperature_2m',
		rawurlencode( $lat ),
		rawurlencode( $lng )
	);

	error_log( "BB DEBUG: Fetching weather data from: {$api_url}" );

	$response = wp_remote_get( $api_url, [ 'timeout' => 10 ] );

	if ( is_wp_error( $response ) ) {
		error_log( 'BB DEBUG: API request failed – ' . $response->get_error_message() );
		return false;
	}

	if ( wp_remote_retrieve_response_code( $response ) !== 200 ) {
		error_log( 'BB DEBUG: API returned non-200 status code' );
		return false;
	}

	$body = wp_remote_retrieve_body( $response );
	$data = json_decode( $body, true );

	if ( ! $data || ! isset( $data['current'] ) ) {
		error_log( 'BB DEBUG: Invalid or empty API response' );
		return false;
	}

	$temperature  = $data['current']['temperature_2m'] ?? null;
	$weather_code = $data['current']['weather_code'] ?? 0;

	$mapped_data = [
		'temperature'    => round( (float) $temperature ),
		'weather_state'  => bb_map_wmo_code_to_state( (int) $weather_code ),
	];

	// Cache for 30 minutes
	set_transient( $transient_key, $mapped_data, BB_WEATHER_CACHE_TIME );

	error_log( 'BB DEBUG: Weather data fetched and cached successfully' );

	return $mapped_data;
}
```

This function retrieves current weather data from the Open-Meteo API and stores it in the cache using [transients](https://kinsta.com/blog/wp-options-autoloaded-data/#clean-up-transients). Let’s take a closer look.

- Two calls to `get_post_meta` retrieve the latitude and longitude of your location.
- The following two lines normalize the decimal separator in case the user enters a comma instead of a period.
- The conditional block checks if the values are in numerical format using `is_numeric()`.
- Next, it checks if the data is in cache. If so, it returns the cached data and stops the function without sending any request to the API.
- If no data is found in cache, it builds the request and stores the response.
- The following lines provide `temperature` and `weather_code`.
- `weather_code` is mapped to `weather_state` thanks to the `bb_map_wmo_code_to_state` function, which is defined below.
- The data is saved with `set_transient`.
- Finally, the function returns the mapped data.

Last, define the function that translates `weather_code` into a human-readable string:

```
function bb_map_wmo_code_to_state( $code ) {
	if ( $code >= 0 && $code <= 3 ) {
		return 'clear';
	} elseif ( $code >= 51 && $code <= 67 ) {
		return 'rainy';
	} elseif ( $code >= 71 && $code <= 77 ) {
		return 'snowy';
	} elseif ( $code >= 95 ) {
		return 'thunderstorm';
	}
	return 'cloudy';
}
```

The code is complete, and your plugin is ready for testing.

## How to use the Block Bindings API

It’s time to learn how to use the new features added to your site with the Block Bindings API!

In your WordPress dashboard, navigate to the Plugins screen and activate the **Block Bindings Example** plugin you just created.

![Plugins screen](https://kinsta.com/wp-content/uploads/2025/12/plugins-screen.png)

Activate the plugin in your WordPress dashboard.

After that, create a new post or page. Add an Image block, a title, and four Row blocks containing two paragraphs each, as shown in the image below. Then, save the post.

![A screenshot of the block editor canvas with blocks.](https://kinsta.com/wp-content/uploads/2025/12/adding-blocks.png)

Add blocks to the editor canvas.

Following, add your custom fields and save the post again.

![Add custom fields to the post.](https://kinsta.com/wp-content/uploads/2025/12/add-custom-fields.png)

Add custom fields to the post.

Select the Image block and find the **Attributes** panel in the Block Settings sidebar. Click the **+** button to open the dropdown menu, which displays the list of Image block attributes that support Block Bindings. Select the **url** item.

![A screenshot showing the Image block attributes that support Block Bindings](https://kinsta.com/wp-content/uploads/2025/12/image-block-attributes-block-bindings-ui.png)

Image block attributes that support Block Bindings

After selecting the block attribute, the **Advanced** tab will display a new **URL** element with the description “Not connected.” Click on the **url** item again to view the list of available binding sources. **Post Meta** provides the four custom fields registered for the post type, along with their respective values. Select **City Image URL**.

![A screenshot of the Block Bindings UI](https://kinsta.com/wp-content/uploads/2025/12/registered-post-meta-fields.png)

Connect registered meta fields.

You assigned the **City Image URL** meta field to the **url** attribute of the Image block. You should now see a photo of the city you chose.

Follow the same process for the other meta fields. Assign the **City Name** field to the `content` attribute of the Heading block and the **Latitude** and **Longitude** fields to the corresponding Paragraph blocks.

Now, connect the last two blocks to your custom binding source. Unfortunately, as you saw in the previous screenshots, this option is not available in the editor UI.

Currently, you need to switch to the code editor and manually write the markup for the two blocks linked to your binding source. Below is the code to display the temperature provided by the Open-Meteo service:

```
<!-- wp:paragraph {
	"metadata":{
		"bindings":{
			"content":{
				"source":"bb/weather-condition",
				"args":{
					"key":"temperature"
				}
			}
		}
	}
} -->
<p>Placeholder</p>
<!-- /wp:paragraph -->
```

With this method, the name of your binding source will appear in the editor as **Weather Condition**, but the actual data will only be visible in the front end.

![An example of block bindings with custom data sources](https://kinsta.com/wp-content/uploads/2025/12/block-bindings-example.jpg)

An example of block bindings with custom data sources

Clearly, manually adding a JSON object to the block markup isn’t a user-friendly process. Fortunately, [WordPress 6.9](https://kinsta.com/blog/wordpress-6-9/) introduced significant improvements to the Block Bindings API, making it possible to create a UI for custom data sources. Let’s try improving our plugin with a custom UI.

## How to create a UI for your custom Block Bindings sources

To create a UI for your custom binding source, you need to write some JavaScript code. First, create a `js` subfolder under `/includes` and then create a **block-bindings-ui.js** file inside it. The plugin structure is now the following:

```
/wp-content/plugins/
└── /block-bindings-example/
	├── block-bindings-example.php
	└── /includes/
		├── binding-sources.php
		├── meta-fields.php
		├── weather-api.php
		└── /js/
			└──	block-bindings-ui.js
```

As a first step, add the JS script to the main file of your plugin:

```
function bb_enqueue_weather_bindings_ui() {
	if ( ! is_admin() ) {
		return;
	}

	$js_path = plugin_dir_path( __FILE__ ) . 'includes/js/block-bindings-ui.js';

	if ( ! file_exists( $js_path ) ) {
		error_log('[BB Weather] ERROR: JS file not found -> ' . $js_path);
		return;
	}

	$version = filemtime( $js_path );

	wp_enqueue_script(
		'bb-weather-bindings-ui',
		plugins_url( 'includes/js/block-bindings-ui.js', __FILE__ ),
		[ 'wp-blocks', 'wp-element', 'wp-dom-ready' ], // Minimal dependencies, sufficient for this script
		$version,
		true
	);

	error_log('[BB Weather] Script enqueued correctly - URL: ' . plugins_url( 'includes/js/block-bindings-ui.js', __FILE__ ) . '?ver=' . $version);
}
add_action( 'enqueue_block_editor_assets', 'bb_enqueue_weather_bindings_ui' );
```

Here’s what this function does:

- First, it checks that the current user is in the context of the admin area.
- Next, it checks that the `block-bindings-ui.js` file exists in the plugin’s `/includes/js` folder.
- The `wp_enqueue_script()` function enqueues the script for use in the editor. For a detailed description of the function, please refer to the [documentation](https://developer.wordpress.org/reference/functions/wp_enqueue_script/).
- It uses the [`enqueue_block_editor_assets` hook](https://developer.wordpress.org/reference/hooks/enqueue_block_editor_assets/) to queue scripts for the editing interface.

Now open the `block-bindings-ui.js` file and write the following code:

```
wp.blocks.registerBlockBindingsSource({
	name: 'bb/weather-condition',
	label: 'Weather Condition',
	useContext: [ 'postId', 'postType' ],
	getValues: ( { bindings } ) => {
		if ( bindings.content?.args?.key === 'temperature' ) {
			return {
				content:
					'Current temperature provided by Open-Meteo.',
			};
		}
		if ( bindings.content?.args?.key === 'weather_state' ) {
			return {
				content:
					'Current conditions.',
			};
		}
		return {
			content: bindings.content,
		};
	},
	getFieldsList() {
		console.log('%c[BB Weather] getFieldsList executed -> dropdown visible', 'color: lime; font-weight: bold;');
		return [
			{ label: 'Temperature (°C)',   type: 'string', args: { key: 'temperature' } },
			{ label: 'Weather Conditions',  type: 'string', args: { key: 'weather_state' } }
		];
	}
});
```

- The `registerBlockBindingsSource()` function registers a binding source in the block editor.
- `name` is a unique identifier for your binding source. It must match exactly the name used in PHP with `register_block_bindings_source()`.
- `label` is a human-readable name displayed in the **Source** dropdown of the **Attributes** panel.
- `useContext` sets the context values this source needs from the block. `postId` is required so that the source knows which post’s meta/weather data to read.
- `getValues` provides a preview of the bounded value inside the block editor. It returns the options that appear in the dropdown after the user selects the binding source (“Weather Condition” in our example). This method is available since WordPress 6.9.
- `getFieldsList` returns the options that appear in the dropdown after the user selects the binding source (“Weather Conditions” in our example).

Save the file and return to the editor. Your **Weather Conditions** source is now available in the editor UI, alongside **Post Meta**. Reload the page, then connect a Paragraph or Header block to your binding source. The image below shows the result.

![Custom Block Binding source UI](https://kinsta.com/wp-content/uploads/2025/12/custom-binding-source-ui.png)

Custom Block Binding source UI

The final image shows the result on the website’s frontend.

![A post that shows data from an external binding source ](https://kinsta.com/wp-content/uploads/2025/12/custom-data-with-block-bindings.jpg)

A post that shows data from an external binding source

## What else can you do with the Block Bindings API?

This article only scratches the surface of what you can build with the Block Bindings API. The great thing is that the development of this powerful WordPress feature is far from over, and we can expect new implementations and additions in the future.

Integrating the Block Bindings API with other powerful WordPress APIs, such as the [Interactivity API](https://kinsta.com/blog/wordpress-interactivity-api/), allows you to build dynamic, interactive applications that extend well beyond the traditional blogging features that made WordPress popular in its early years.

WordPress is no longer just a blogging platform or a website builder. It is now set to become a multipurpose development platform for all types of web applications.

The more powerful your applications are, the more important your hosting service becomes. Kinsta offers Premium managed hosting with high performance, robust security, extensive automation, and top-notch support recognized as industry-leading by [G2 users](https://kinsta.com/blog/g2-awards/).

The most powerful web applications require the best hosting infrastructure. Take a look at [Kinsta plans](https://kinsta.com/pricing/) to find the one that best suits your site’s needs.

Carlo Daniele
[Kinsta](https://kinsta.com/)

Carlo is a passionate lover of webdesign and front-end development. He has been playing with WordPress for more than 20 years, also in collaboration with Italian and European universities and educational institutions. He has written hundreds of articles and guides about WordPress, published both on Italian and international websites, as well as on printed magazines. You can find him on [LinkedIn](https://www.linkedin.com/in/carlodaniele/).

- [Website](https://frammentidicodice.com/)
- [Twitter](https://twitter.com/carlodaniele)
