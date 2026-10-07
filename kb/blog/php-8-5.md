---
url: "https://kinsta.com/blog/php-8-5/"
title: "PHP 8.5: Here's what's new in the latest release"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "PHP Updates", "PHP 8.5: Here\u2019s what\u2019s new in the latest release"]
kinsta_last_updated: "2026-05-20T20:31:34+00:00"
sitemap_lastmod: "2026-05-20T20:31:34"
fetched_at: "2026-10-07T22:43:04Z"
sha256: "6361adb0cb25067cbeb0a7f653ab47e255a777a12a80cff7819bc17a3aab6743"
body_chars: 14387
extracted_with: "main article"
status: "live"
---

# PHP 8.5: Here's what's new in the latest release

**Section:** Resource Center > Blog > PHP Updates > PHP 8.5: Here’s what’s new in the latest release
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/php-8-5/
**Kinsta last updated:** 2026-05-20T20:31:34+00:00

## On this page

- [New features and improvements in PHP 8.5](#new-features-and-improvements-in-php-85)
  - [Chain function calls with a pipe operator](#chain-function-calls-with-a-pipe-operator)
  - [Parse URLs with the new URI extension](#parse-urls-with-the-new-uri-extension)
  - [Get strict with a new max_memory_limit INI directive](#get-strict-with-a-new-max-memory-limit-ini-directive)
  - [Grab the first or last values in an array](#grab-the-first-or-last-values-in-an-array)
  - [Get reminded to use a function’s return value](#get-reminded-to-use-a-functions-return-value)
    - [Other enhancements related to attributes](#other-enhancements-related-to-attributes)
- [Deprecations and removals in PHP 8.5](#deprecations-and-removals-in-php-85)
- [Summary](#summary)

---

Author
:   [Steve Bonisteel](https://kinsta.com/blog/author/stevebonisteel/ "Posts by Steve Bonisteel")

Updated
:   May 20, 2026

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![An illustration representing the new release of PHP and showing the version number 8.5.](https://kinsta.com/wp-content/uploads/2025/12/whats-new-in-php-8.5-1024x512.png)

The PHP Group has released version 8.5 of the open source scripting language that powers much of the Web, including sites using the WordPress CMS.

The release of PHP 8.5 in November marked the second year of the PHP community’s commitment to delivering major updates on an annual schedule, followed by [two full years of active support](https://www.php.net/supported-versions.php) for each release.

Although 8.5 is brand-new, we’ve already got it covered in our annual [PHP benchmarking](https://kinsta.com/blog/php-benchmarks/) behind a variety of popular CMS platforms and frameworks.

If you’re planning to [migrate PHP applications to version 8.5](https://www.php.net/manual/en/migration85.php), you’ll need to know what has changed in this latest release. That includes new features you might be able to harness to improve your code and old functionality that PHP’s developers are getting ready to remove.

Here’s what we think are highlights of the new release:

## New features and improvements in PHP 8.5

Let’s start with new additions to the PHP code base. These changes usually begin as [Requests for Comments (RFCs)](https://wiki.php.net/rfc) that might eventually be approved and assigned to a future PHP release.

The new features described below are the ones capturing most of the attention around PHP 8.5.

### Chain function calls with a pipe operator

A new pipe (`|>`) operator chains function calls in a way that will feel vaguely familiar to JavaScript programmers. The pipe operates left to right, passing a single value along the chain at each step.

With previous versions of PHP, programmers might have accomplished a similar task by nesting functions or stepping through a series of function calls on each step’s returned value.

Here’s a simple example using the new pipe operator:

```
$text = ' New-in-php-8.4 ';

$result = $text
    |> trim(...)
    |> (fn($str) => str_replace('4', '5', $str))
    |> (fn($str) => str_replace('-', ' ', $str))
    |> strtoupper(...);

var_dump($result);
// string(14) "NEW IN PHP 8.5"
```

(Note that we are using the [first-class callable syntax](https://kinsta.com/blog/php-8-1/#firstclass-callable-syntax) `(...)` introduced in PHP 8.1 with the `trim()` and `strtoupper()` function calls.)

The piped chain above could be written on a single line, but readability is supposed to be one of the benefits of this new operator.

The above is equivalent to nesting those operations (in the reverse order) like this:

```
$text = " New-in-php-8.4 ";

$result = strtoupper(
    str_replace(‘-, ' ',
        str_replace('4', '5', 
            trim($text)
         )
     )
);
```

Alternatively, a programmer might have completed the task in earlier PHP versions like this:

```
$text = " New-in-php-8.4 ";

$result = trim($text);
$result = str_replace('4', '5', $result);
$result = str_replace(‘-, ' ', $result);
$result = strtoupper($result);
```

### Parse URLs with the new URI extension

URLs (also known as URIs to those who are more exacting) are essential to Web navigation, but the `parse_url()` function that has been built into PHP since version 4 is well known to have trouble with malformed input that can lead to errors when attempting to manipulate or validate website addresses.

To improve URL parsing, PHP 8.5 incorporates the [uriparser](https://uriparser.github.io/) and [Lexbor](https://lexbor.com/) libraries for support of [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986) and [WHATWG URL](https://url.spec.whatwg.org/) standards, respectively.

You can invoke the uniparser library by starting work with the new URI extension like this:

```
$uri = new Uri\Rfc3986\Uri("https://kinsta.com/blog/php-8-5/"); 

echo $uri->getScheme();       // https
echo $uri->getHost();         // kinsta.com
echo $uri->getPath();         // /blog/php-8-5
```

Alternatively, you can choose the Lexbor WHATWG URL library like this:

```
$uri = new Uri\WagWg\Url("https://kinsta.com/blog/php-8-5/"); 

echo $uri->getScheme();       // https
echo $uri->getUnicodeHost();  // kinsta.com
echo $uri->getAsciiHost();    // kinsta.com
echo $uri->getPath();         // /blog/php-8-5
```

The examples above are the most basic. The two libraries represented by the URI extension in PHP 8.5 share some functionality and also pack significant differences.

One important difference is that the RFC 3986 library supports both “raw” and “normalized-decoded” representations of URIs. This can be useful when working with percent-encoded input and output. Used in a browser, for example, these two URIs are identical:

- <https://kinsta.com/mykinsta/>
- <https://kinsta.com/%6D%79%6B%69%6E%73%74%61/>

In previous versions of PHP, you might start with `rawurldecode()` and `rawurlencode()` (which are also RFC 3986 compliant), but the new extension is ready to work with all the components of URIs right out of the box, whether they are encoded or not.

Here are some examples straight from the [RFC behind the new parsing API](https://wiki.php.net/rfc/url_parsing_api):

```
$uri = new Uri\Rfc3986\Uri("https://%61pple:p%61ss@ex%61mple.com/foob%61r?%61bc=%61bc");
  
echo $uri->getRawUserInfo();  // %61pple:p%61ss
echo $uri->getUserInfo();     // apple:pass
 
echo $uri->getRawUsername();  // %61pple
echo $uri->getUsername();     // apple
 
echo $uri->getRawPassword();  // p%61ss
echo $uri->getPassword();     // pass
 
echo $uri->getRawHost();      // ex%61mple.com
echo $uri->getHost();         // example.com
 
echo $uri->getRawPath();      // /foob%61r
echo $uri->getPath();         // /foobar
 
echo $uri->getRawQuery();     // %61bc=%61bc
echo $uri->getQuery();        // abc=abc
```

When using the WHATWG URL library with the new extension, all URIs are treated as “raw,” so there is no separate set of functions to support alternate formatting. But the library can convert between the ASCII and Unicode characters often seen in URIs.

### Get strict with a new max_memory_limit INI directive

They say that with great power comes great responsibility. If that power includes choosing how much server memory your PHP application might attempt to use, you could be responsible for application crashes when processes consume more memory than is available.

Part of a typical PHP installation is a `php.ini` file with configuration information that includes a directive specifying a memory-consumption limit for any PHP process ([or thread](https://kinsta.com/blog/php-threads-vs-php-memory-limit/)). A common INI directive for a memory limit of 128 MB looks like this:

```
// php.ini
memory_limit 128M
```

On some hosting platforms, developers of PHP applications can override `memory_limit` on the fly using the `ini_set()` function in their code:

```
ini_set(‘memory_limit’, ‘256M’);
 
// Start code that requires up to 256 MB of memory
```

You can also pass the function the value **-1**, like `ini_set('memory_limit', '-1')` — to enforce no limit at all.

Overriding the INI directive for a memory limit can be risky for developers who are not intimately familiar with the memory configurations of the servers on which their applications will run. If one or multiple PHP threads attempt to consume more than the total memory pool, the result can be an application crash without warning at run-time.

PHP 8.5 adds a `max_memory_limit` INI directive that serves as a hard ceiling, even in setups where developers have access to `init_set()` to tweak memory use in their code.

Here are example entries in the `php.ini` file of a PHP 8.5 installation:

```
// php.ini
max_memory_limit 256M
memory_limit 128M
```

With a `max_memory_limit` of 256 MB, here’s what happens in our PHP code:

```
ini_set('memory_limit', '256M');  // This is OK
ini_set('memory_limit', '512M');  // Fail with warning
ini_set('memory_limit', '-1');    // Fail with warning
```

Attempting to set a new memory limit of 512 MB (or unlimited) above will not be successful. Instead, PHP will set the memory limit to the value assigned to `max_memory_limit` in the `php.ini` file and issue a warning. (The warning message might display on screen and be logged, depending on the PHP installation’s error-reporting settings.)

A wise approach for PHP 8.5 developers would be to use the `ini_get()` function to see if the new maximum limit has been defined, like `ini_get('max_memory_limit')` — and then adjust according to the value returned. With versions of PHP prior to 8.5, that call would safely return `false`.

### Grab the first or last values in an array

Raise your hand if you would have assumed PHP already had functions to read the values stored as the first or last members of an array.

Turns out, it did not. But since [PHP 7.3](https://kinsta.com/blog/php-7-3/#array-key-first-last), it has had functions to uncover the first and last **keys** in an array. So, to find the first and last values, you could employ the `array_key_first()` or `array_key_last()` functions and then use the keys returned to reference the values you are looking for:

```
$array = ["One", "Two", "Three"];

echo $array[array_key_first($array)]; // "One"
```

PHP 8.5 eliminates a step for that task and allows you to reach the values directly with new `array_first()` and `array_last()` functions.

It’s all pretty simple:

```
$array = ["One", "Two", "Three"];

echo array_first($array);  // "One"
echo array_last($array);   // "Three"
echo array_last([]);       // null
```

Above, you can see that an empty array will return `null`, but that alone doesn’t confirm that the entire array is empty, since an array value can be null:

```
echo array_last([1, 2, null]); // null
```

### Get reminded to use a function’s return value

PHP 5.8 adds a new `#[\NoDiscard]` attribute that indicates a function’s return value might be critical. PHP will confirm that the return value is consumed in some way and, if not, trigger a warning.

A simple example:

```
#[\NoDiscard("this message property will be appended to the built-in warning.")]
function foo(): string {
    return 'bar';
}

// Warning:
// The return value of function foo() is expected to be consumed,
// this message property will be appended to the built-in warning.
foo();

// This will not trigger a warning:
$result = foo();

// Also satisfactory is the (void) cast:
(void) foo();
```

In the example above, the return value of the defined function is not used at all in the first instance, triggering a warning. But when assigned to the variable `$result` or cast as `void`, the value was deemed to have been consumed.

The authors of the [RFC behind this addition](https://wiki.php.net/rfc/marking_return_value_as_important) to PHP 8.5 described more compelling uses for this attribute than the simple example above. One scenario was a critical function with more complex error reporting than a simple pass/fail, and best conveyed through the function’s return value.

#### Other enhancements related to attributes

In addition to the new `#[\NoDiscard]` attribute, other enhancements to attribute metadata functionality in the new release include:

- Attributes can now target constants.
- The `#[\Override]` attribute can now be applied to properties.
- The `#[\Deprecated]` attribute can be used on traits and constants.
- A new `#[\DelayedTargetValidation]` attribute can be used to suppress compile-time errors from core and extension attributes that are used on invalid targets.

## Deprecations and removals in PHP 8.5

With each PHP release comes a list of functionality flagged for removal in future versions. Using deprecated features in your code will trigger warnings. When finally removed from PHP, their use can result in fatal errors.

Here are some notable elements deprecated or removed in PHP 8.5:

- The backtick operator as an alias for `shell_exec()` has been deprecated.
- Non-canonical cast names `(boolean)`, `(integer)`, `(double)`, and `(binary)` have been deprecated. Instead, use `(bool)`, `(int)`, `(float)`, and `(string)` instead.
- The disable_classes INI setting has been removed as it causes various engine assumptions to be broken.
- Terminating `case` statements with a semicolon instead of a colon has been deprecated.
- Using null as an array offset or when calling `array_key_exists()` is now deprecated. Use an empty string instead.
- It is no longer possible to use “array” and “callable” as class alias names in `class_alias()`.
- The `__sleep()` and `__wakeup()` magic methods have been soft-deprecated. Instead, the `__serialize()` and `__unserialize()` magic methods should be used.
- A warning is now emitted when casting NAN to other types.
- Destructuring non-array values (other than null) using `[]` or `list()` now emits a warning.
- A warning is now emitted when casting floats (or strings that look like floats) to `int` if they cannot be represented as one.

## Summary

That was a look at the highlights of the PHP 8.5 release. We’re confident that the new pipe operator and improved URI parsing will be popular with developers. Maybe even the new `array_first()` and `array_last()` functions, which we would have bet money on already existing.

But any new PHP release encompasses hundreds of changes. You can find a [complete list of PHP 8.5 updates](https://github.com/php/php-src/blob/PHP-8.5/UPGRADING) in the PHP Group’s official GitHub repository.

Meanwhile, here at Kinsta, we’re working to make PHP 8.5 available to our [WordPress hosting](https://kinsta.com/wordpress-hosting/) customers. When that’s online, you’ll be able to switch to the new release using our [PHP settings](https://kinsta.com/docs/wordpress-hosting/php/wordpress-restart-update-php/#update-php) tools.

Steve Bonisteel
[Kinsta](https://kinsta.com/)

Steve Bonisteel is a Technical Editor at Kinsta who began his writing career as a print journalist, chasing ambulances and fire trucks. He has been covering Internet-related technology since the late 1990s.
