---
url: "https://kinsta.com/blog/ai-wordpress-developers/"
title: "Why WordPress expertise still matters in AI-assisted development"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: []
kinsta_last_updated: "2026-10-08T19:27:10"
change_signal: "2026-10-08T19:27:10"
fetched_at: "2026-11-11T13:03:02Z"
sha256: "7c1b04c204b1de2851871cf19fb400fd93413c56c8babb47ab4e34835ce06ebd"
body_chars: 6956
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Why WordPress expertise still matters in AI-assisted development

**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/ai-wordpress-developers/
**Kinsta last updated:** 2026-10-08T19:27:10

## On this page

- [AI-generated code still needs review](#ai-generated-code-still-needs-review)
- [Understanding the problem comes before writing the code](#understanding-the-problem-comes-before-writing-the-code)
- [From code production to code review](#from-code-production-to-code-review)
- [Prompt engineering isn’t the whole story](#prompt-engineering-isnt-the-whole-story)
- [Where does this leave the WordPress developer?](#where-does-this-leave-the-wordpress-developer)

---

AI is changing how WordPress [developers](https://kinsta.com/blog/types-of-developers/) work. It can generate code, help troubleshoot errors, explain unfamiliar APIs, and turn a plain-language request into a prototype. But producing code and deciding whether it belongs on a production website are different tasks.

That distinction matters in WordPress. Decisions about architecture, performance, security, accessibility, and maintainability require an understanding of the project. A developer has to assess how AI-generated code fits the site’s plugins, themes, APIs, and business requirements.

AI can help propose and implement a solution, but the developer still has to evaluate the approach, challenge incorrect assumptions, and check that the result solves the intended problem.

For this article, we spoke with four WordPress developers about how they apply that judgment in their work with AI.

## AI-generated code still needs review

AI can suggest functions and APIs that don’t exist, misunderstand project requirements, make incorrect assumptions, and introduce subtle bugs.

Generated code can also omit security measures such as input validation, sanitization, or output escaping. Those checks remain part of  [WordPress’s security guidance](https://developer.wordpress.org/apis/security/), regardless of how the code was produced.

A concrete example appears in Kinsta’s walkthrough of  [using AI tools to spin up a WordPress plugin](https://kinsta.com/blog/ai-plugin-development/). The plugin created a restricted user role. During attempts to remove the Quick Edit link, Cursor sometimes removed the Edit function as well. Getting the requested interface change was not enough; the role still needed to retain its intended functionality.

The lesson is not simply to ask AI to try again. The developer needs to check behavior that should remain unchanged, not just the feature the tool was asked to modify.

## Understanding the problem comes before writing the code

Writing code is only one part of professional WordPress development. An experienced developer also has to understand the problem and translate business requirements into a technical solution.

That means deciding what should be built, how the pieces should fit together, and how the solution serves the business over time. It includes choosing an appropriate architecture, evaluating tradeoffs, and anticipating maintenance needs.

Mark Szymanski’s experience illustrates that work. He describes moving beyond “pixel pushing” toward using AI to help build more complex business applications. The objective isn’t simply to produce a working website faster. It’s to determine what combination of technologies best solves the underlying business problem.

Jos Velasco describes using AI to analyze server data and identify patterns that would be time-consuming to find manually. A suggested pattern still needs to be checked against the site’s behavior before the developer decides what to change.

## From code production to code review

When AI generates changes faster than a team can assess them, review becomes the bottleneck.

The issue isn’t simply whether AI-generated code runs. Someone has to determine whether it behaves as intended, follows appropriate  [WordPress coding standards](https://kinsta.com/blog/wordpress-coding-standards/), fits the larger application, and is ready for production.

![Generate, Review, Decide, and Ship.](https://kinsta.com/wp-content/uploads/2026/10/Generate-Review-Decide-Ship.jpeg)

Generate, Review, Decide, and Ship.

Jos Velasco raises a related concern about reviewing AI-assisted contributions to WordPress. AI can help create a patch, but contributors and committers still have to assess whether it belongs in the project.

[WordPress’s AI contribution guidelines](https://make.wordpress.org/ai/handbook/ai-guidelines/) make the contributor’s responsibility explicit: understand the submitted code, review and validate it, and run the relevant tests. That responsibility begins before a patch reaches a maintainer.

Developers also use AI to help manage the review process. Rich Tabor has  [described using Claude Code and Copilot as complementary tools](https://richtabor.com/i-dont-vibe-code), asking one to review work produced with the other while he makes the technical decisions. Mike Auteri also incorporates automated code review into his workflow.

Auteri uses a test-driven development approach: **the human writes the tests; the AI writes the implementation.** By establishing the expected behavior first, the developer defines what the implementation needs to satisfy rather than leaving AI to infer both the requirements and the solution.

Neither passing tests nor receiving a favorable AI review guarantees that a change is ready for production.  [GitHub’s guidance on Copilot](https://docs.github.com/en/copilot/responsible-use/agents) notes that automated review can miss problems or flag issues that do not exist, and should supplement human review rather than replace it.

## Prompt engineering isn’t the whole story

Learning how to communicate effectively with AI is valuable, but knowing how to write a clever prompt isn’t the defining skill of an AI-assisted developer.

The more important skill is knowing what context AI needs, what constraints it should operate within, and what a successful result should look like.

Mark Szymanski addresses the context problem with what he calls an  [AI Operating System (AIOS)](https://markszymanski.co/videos/ai-operating-system-aios/). One part of that setup is a collection of files containing business information, development principles, client histories, and other project-specific knowledge. Rather than repeatedly asking AI to work from a generic prompt, he supplies context about the project and the business behind it.

Providing that context doesn’t remove the need to understand the output. Without a foundation in WordPress and web development, someone may be able to produce working code without understanding what compromises it makes or whether it is appropriate for the project.

## Where does this leave the WordPress developer?

AI does not automatically make every WordPress developer more valuable. The opportunity is to use it to accomplish more while retaining the judgment needed to choose an approach, review the implementation, and maintain the result.

AI can help build the solution. The experienced developer is still responsible for making sure it’s the right one.

At Kinsta, we support that work with [staging environments](https://kinsta.com/docs/wordpress-hosting/staging-environment/) to test changes before they go live, built-in [performance monitoring](https://kinsta.com/apm-tool/) to investigate slow pages, and WordPress engineers available [24/7 for hosting support](https://kinsta.com/kinsta-support/). Explore our [Hosting for WordPress](https://kinsta.com/wordpress-hosting/) to see how it fits your next project.
