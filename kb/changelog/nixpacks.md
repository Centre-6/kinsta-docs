---
url: "https://kinsta.com/changelog/nixpacks/"
title: "Introducing Nixpacks for Streamlined Deployments"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Introducing Nixpacks for Streamlined Deployments"]
kinsta_last_updated: "2026-05-14T19:08:07+00:00"
sitemap_lastmod: "2026-05-14T19:08:07+00:00"
fetched_at: "2026-10-07T22:36:18Z"
sha256: "847161b6be68e83c44685536f278b2b81942a4842aff351bbc37eb08ccbbd5d7"
body_chars: 4919
extracted_with: "main article"
status: "live"
---

# Introducing Nixpacks for Streamlined Deployments

**Section:** Changelog > Introducing Nixpacks for Streamlined Deployments
**Product:** Changelog
**Source:** https://kinsta.com/changelog/nixpacks/
**Kinsta last updated:** 2026-05-14T19:08:07+00:00

## On this page

- [What Is Nixpacks?](#what-is-nixpacks)
- [Build Container Images at Kinsta With Nixpacks](#build-container-images-at-kinsta-with-nixpacks)
- [Supported Languages](#supported-languages)
- [Experience the Future of Container Image Creation](#experience-the-future-of-container-image-creation)

---

Updated
:   May 14, 2026

![Introducing Nixpacks](https://kinsta.com/wp-content/uploads/2023/09/Introducing-Nixpacks_Feature_Updates_EN-1024x535.jpg)

When [we introduced Application Hosting](https://kinsta.com/changelog/application-database-hosting/), it came with two methods for setting up container images based on your repository: one [using Buildpacks](https://docs.sevalla.com/applications/build-options/buildpacks), which automates the container image setup, and the other via a [Dockerfile](https://docs.sevalla.com/applications/build-options/dockerfile), granting you the freedom to work with any programming language.

As part of our ongoing commitment to providing you with powerful tools and technologies to improve Application Hosting, we’re introducing [Nixpacks](https://docs.sevalla.com/applications/build-options/nixpacks) as a new option to automatically create container images for your applications based on your repository.

## What Is Nixpacks?

Similarly to Buildpacks, [Nixpacks](https://nixpacks.com/docs) is an open-source project that creates your application’s container image based on your repository. Nixpacks scripts use Nix binary to build your application, install dependencies, and configure your environment when your application is deployed. It is written in [Rust](https://kinsta.com/blog/rust-vs-python/) and offers a faster build time than Buildpacks.

It provides a standardized and simplified way to package and build applications by taking the source directory from your Git provider ([BitBucket](https://docs.sevalla.com/applications/git/bitbucket#grant-access-to-the-kinsta-bitbucket-application), [GitHub](https://docs.sevalla.com/applications/git/github#authenticate-and-authorize), and [GitLab](https://docs.sevalla.com/applications/git/gitlab#authorize-the-kinsta-gitlab-application)) and automatically detecting an application’s language, framework, and runtime dependencies. It then creates a runnable artifact (such as a [container image](https://kinsta.com/blog/docker-remove-images/)) containing everything you need to run your application.

One major benefit to using Nixpacks over Buildpacks is a built-in caching system for builds, which caches directories during the installation and build phases. This means after the first build is completed, subsequent builds are much faster.

## Build Container Images at Kinsta With Nixpacks

When you add an application in Kinsta, you can choose to use Nixpacks to automatically determine and create a container for your application based on your repository.

![Use Nixpacks to set up container image](https://kinsta.com/wp-content/uploads/2023/09/use-nixpacks-build-image.jpg)

Use Nixpacks to set up container image.

We recommend using Nixpacks due to its resource-efficient code compilation, faster build and deployment times, and extensive language and framework support.

Additionally, please make sure to specify the build path if you are using a different directory as your build source, distinct from the root of your repository.

When using Nixpacks, you do not need to specify a provider to build for, as it automatically detects this based on the files in the source directory. If your application requires additional providers, you can define them within the [Nixpacks configuration file](https://nixpacks.com/docs/guides/configuring-builds).

## Supported Languages

Nixpacks supports all major programming languages. You can find a comprehensive list in [our documentation](https://docs.sevalla.com/applications/build-options/nixpacks#supported-languages).

When using Nixpacks, you have to specify your language version in your application’s code. If you do not specify a version in your application’s code, Nixpacks uses the latest available version. To use a different language version, [set the version in your application’s files](https://docs.sevalla.com/applications/build-options/nixpacks#set-a-nixpacks-language-version).

If you want to use a language or a language version that is not a supported Nixpack language or version, use a [Dockerfile](https://docs.sevalla.com/applications/build-options/dockerfile). When you add your application, select the option **Use Dockerfile to set up container image**.

## Experience the Future of Container Image Creation

We believe that Nixpacks is a game-changer for our users, offering more efficiency and flexibility to manage container images for your applications. As technology evolves, Kinsta is committed to staying at the forefront, providing you with cutting-edge solutions to simplify your development process.

Give Nixpacks a try today and experience the future of container image creation at Kinsta by [reading our documentation for more information](https://docs.sevalla.com/applications/build-options/nixpacks).

We’re excited to see how this new addition will empower you to build and deploy applications more efficiently than ever before.
