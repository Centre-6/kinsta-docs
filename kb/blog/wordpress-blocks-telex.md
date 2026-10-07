---
url: "https://kinsta.com/blog/wordpress-blocks-telex/"
title: "Building WordPress blocks with Telex"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "WordPress Development", "Building WordPress blocks with Telex"]
kinsta_last_updated: "2026-01-20T16:30:42+00:00"
sitemap_lastmod: "2026-01-20T16:30:42"
fetched_at: "2026-10-07T22:42:49Z"
sha256: "c92d33f7d191a6273461d732dd75ad5bb5b269a380591b1be087a6cd0258c9a8"
body_chars: 10391
extracted_with: "main article"
status: "live"
---

# Building WordPress blocks with Telex

**Section:** Resource Center > Blog > WordPress Development > Building WordPress blocks with Telex
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/wordpress-blocks-telex/
**Kinsta last updated:** 2026-01-20T16:30:42+00:00

## On this page

- [How Telex works in practice](#how-telex-works-in-practice)
  - [Vibe coding an Embed ChatGPT block](#vibe-coding-an-embed-chatgpt-block)
  - [Vibe coding a Social Draft block](#vibe-coding-a-social-draft-block)
- [Drawbacks and workarounds](#drawbacks-and-workarounds)
- [What’s next for building blocks with AI](#whats-next-for-building-blocks-with-ai)

---

Author
:   [Bud Kraus](https://kinsta.com/blog/author/budkraus/ "Posts by Bud Kraus")

Published
:   February 12, 2026

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![](https://kinsta.com/wp-content/uploads/2026/01/building-a-wordpress-block-weith-telex-1024x512.png)

[Telex](https://telex.automattic.ai/) is an experimental, browser-based free tool from Automattic that uses AI to generate [WordPress blocks](https://kinsta.com/blog/gutenberg-blocks/) from natural language prompts.

Instead of setting up a [local development environment](https://kinsta.com/devkinsta/), configuring build tools, and scaffolding a block by hand, Telex lets you describe what you want, preview the result, and download a ready-to-install plugin.

This article explores what that workflow looks like in practice and what kinds of blocks it is realistically suited for today. Using two real examples, including a more complex editor-only block, we look at how far Telex can take you and where manual intervention is still required.

![Telex user interface](https://kinsta.com/wp-content/uploads/2026/01/telex-ui.png)

Telex user interface.

## How Telex works in practice

Telex follows an assembly-line style workflow. You describe the block you want using natural language, then Telex maps that request onto a predefined WordPress block scaffold based on the standard create-block tooling.

![How Telex works](https://kinsta.com/wp-content/uploads/2026/01/how-telex-works-e1768826046392.png)

How Telex works.

From there, AI fills in the details such as block [metadata](https://kinsta.com/blog/meta-description-wordpress/), editor UI, rendering logic, and basic styling within those constraints. The block is then built in a hosted [Node.js](https://kinsta.com/blog/what-is-node-js/) environment, previewed in [WordPress Playground](https://kinsta.com/blog/wordpress-playground/), and packaged as a ZIP plugin that’s ready to upload.

Under the hood, the generated plugin follows a familiar structure, closely aligned with `create-block`:

```
block-name/
├── build/
├── src/
│   ├── edit.js
│   ├── save.js
│   ├── index.js
│   ├── style.scss
│   └── editor.scss
├── block.json
├── package.json
├── readme.md
└── .gitignore
```

Let’s build our first of two blocks.

### Vibe coding an Embed ChatGPT block

You may recall a time when it was common to see a Google search box embedded in a web page, allowing users to search a site or the web. If you need to provide that kind of experience for your users, but this time with [ChatGPT](https://kinsta.com/blog/chatgpt-wordpress/) input, here’s how.

This is a great place to start, as you can focus on getting comfortable with Telex’s UI without being too concerned about prompt refinement or multiple iterations.

Start as a logged-in user with [wordPress.com](http://wordpress.com) credentials, and you can describe your initial prompt. Here is what we used:

```
We would like to create a block that embeds the ChatGPT prompt to allow users to use it on the frontend.
```

See the UI below:

![Telex interface showing an input prompt for configuring an automation.](https://kinsta.com/wp-content/uploads/2026/01/telex-input-prompt.png)

Initial Telex input prompt.

Telex creates the ChatGPT embed block, which includes the prompt input box, message history display, and styling that matches ChatGPT’s aesthetic.

At this point, the block outputs an error message in the editor UI.

![Block displaying an error message during workflow execution.](https://kinsta.com/wp-content/uploads/2026/01/block-displaying-error-message.png)

Block displaying error message.

We asked Telex to resolve the issue and were guided through generating a ChatGPT API key and adding it to the block via the Inspector sidebar. In this case, we felt that using an external API for the block did not introduce an unwarranted security risk.

![Block inspector panel showing configuration options and settings.](https://kinsta.com/wp-content/uploads/2026/01/block-inspector.png)

ChatGPT API Key added to the Block Inspector.

Finally, we ran a quick test on the frontend to confirm that everything was working as expected.

![Frontend displaying the initial response generated from a prompt.](https://kinsta.com/wp-content/uploads/2026/01/frontend-displaying-initial-prompt-response.png)

Frontend displaying initial prompt and response.

### Vibe coding a Social Draft block

For our second example, let’s push Telex a bit further by building an internal block for drafting social media posts (one that lets content be written, reviewed, and exported for scheduling without needing a separate collaboration tool or a paid team plan).

We can start with this setup prompt:

```
Build a custom WordPress block named ‘Social Draft’. We will give you further instructions after you set up.
```

Instead of overloading Telex with instructions, it’s often better to use another AI tool (like ChatGPT) to work out a solid set of requirements first. That includes defining your goals, what the frontend should look like, how data is stored, how users interact with the system, and more. Here’s an excerpt from what ChatGPT came back with:

```
Goal
Build an editor-only WordPress block that acts as an internal content-prep tool for drafting social media posts, similar to a lightweight Google Docs workflow. The block should support text, links, images, and video embeds, along with platform selection, alternative versions of the copy, post status, notes, and an export panel optimized for copying content into a social publishing platform.

The block must not render anything on the frontend. It should exist solely for editor workflows, with save() returning null.

Editor UI
The main draft area (“Copy”) should be implemented using InnerBlocks rather than a single RichText field, allowing paragraphs, images, embeds, and lists. An option to add two alternative versions of the copy should be available, each with the same flexibility as the main draft. Simple one-time duplication controls should allow content to be copied between sections when needed.
Additional controls include platform selection via checkboxes, a single status field (Draft, Ready for review, Scheduled, or Not used), and a plain-text notes field.

An export panel should extract plain text from the selected draft or alternative, ignore media, and provide a one-click way to copy the result. Detected media (images and embeds) can be listed for reference, but are not included in the copied output.
All data should be stored within the block using attributes and InnerBlocks. No external APIs are required.
```

When we give this to Telex, the result was UI as expected, but the Social Draft block could not display in the content area.

![Block UI showing a missing content area in the interface.](https://kinsta.com/wp-content/uploads/2026/01/bloc-ui-missing-content-area.png)

Block UI is missing in the content area.

Many times, you have to go through several iterations when vibe coding, and that’s what happened.

Telex identified problems related to how InnerBlocks were being initialized and attempted to restructure the block to fix the rendering issue. These early attempts didn’t succeed, and the block still failed to display correctly in the editor.

At this point, we asked Telex if it could process our request, as we were losing confidence. We reiterated that all UI was exposed, save for what we needed (the ability to add and display the block).

Telex replied:

```
I completely understand your frustration, and yes, I can absolutely do this.I can see the problem - the useBlockProps is being applied but the block isn't rendering visible content in the canvas. The issue is that while we have all the controls and structure, the block wrapper isn't being properly rendered as a visible container. Let me fix this by ensuring the block has proper structure and visibility.
```

We finally got our UI and began a quick probe.

![Social media post data displayed in a structured analytics view.](https://kinsta.com/wp-content/uploads/2026/01/social-media-post-data.png)

Social media post data block.

After many other refinements, the result was a functional block where we accomplished our MVP.

![Social draft block showing a generated social media post draft.](https://kinsta.com/wp-content/uploads/2026/01/social-draft-block.png)

A working MVP for our Social Drafts block.

## Drawbacks and workarounds

Telex has come a long way in a short time, but once you start using it beyond simple experiments, a few limitations become apparent. Most of these aren’t blockers, but they do shape how and when Telex is best used.

1. There’s no built-in way to roll back a prompt. You can ask Telex to undo a change, but a more reliable approach is to save prompts as text or Markdown, version downloaded ZIP files, or use Git once you move the block locally.
2. Telex immediately (re)generates the block after you submit a prompt, with no ability to undo or restore previous versions. To avoid an unwanted action, ask Telex, “How would you do…” for your prompt before you build, re-try, or similar command.
3. Telex is not an IDE. While you can view the generated source code, there’s no way to edit it directly within Telex.
4. Telex is best suited for brainstorming and prototyping. For production use, it’s safest to limit it to very simple blocks where external integrations, complex logic, or security- and performance-sensitive concerns are not a priority.

## What’s next for building blocks with AI

Telex offers a glimpse into how AI can fit into modern WordPress development. It lowers the cost of experimentation, shortens the distance between idea and prototype, and makes block scaffolding more approachable.

At the same time, the examples here show that understanding the block editor still matters.

Once a block is ready to move beyond experimentation, having a reliable [WordPress environment like Kinsta](https://kinsta.com/wordpress-hosting/) makes it easier to test, iterate, and ship with confidence.

Bud Kraus

Bud Kraus has been working with WordPress as an in-class and online instructor, site developer, and content creator since 2009. He has produced instructional videos and written many articles for WordPress businesses.
