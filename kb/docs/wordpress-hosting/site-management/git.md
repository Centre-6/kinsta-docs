---
url: "https://kinsta.com/docs/wordpress-hosting/site-management/git/"
title: "Site Management - Git"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "site-management"
section: []
kinsta_last_updated: "July 1, 2025"
sitemap_lastmod: "2025-07-01T15:48:40+00:00"
fetched_at: "2026-10-07T22:37:25Z"
sha256: "a188dcab5fa0f22b95e2a9516d87dea293e531b407d4789ac4f501d7b72168d3"
body_chars: 4640
extracted_with: "main article"
status: "live"
---

# Site Management - Git

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/site-management/git/
**Kinsta last updated:** July 1, 2025

## On this page

- [Preparation and notes](#preparation-and-notes)
- [Pull repo](#pull-repo)
  - [Pull a private repo](#pull-a-private-repo)
  - [Pull a private repo with 2FA](#pull-a-private-repo-with-2fa)
- [Clone repo](#clone-repo)
  - [Clone a private repo](#clone-a-private-repo)
  - [Clone a private repo with 2FA](#clone-a-private-repo-with-2fa)

---

We have the Git client available at Kinsta, so you can access your site with SSH and pull your Git repo down from [GitHub](https://kinsta.com/blog/git-vs-github/), GitLab, Bitbucket, or any other third-party. SSH access is available on all of Kinsta’s hosting plans.

We don’t yet have the feature of using `git push kinsta my_site` to automatically deploy, but you can still use Git at Kinsta by following the instructions below.

Another way of doing this is to utilize [WP Pusher](https://wppusher.com/). Many of our clients use this and it makes it super easy, as you don’t have to know how to use Git or SSH.

Austin also has an excellent tutorial on how to [set up automatic Git deployment with Kinsta](https://anchor.host/automatic-git-deploy-with-kinsta-via-ssh/) using SSH.

Some other alternatives include [Beanstalk](https://beanstalkapp.com/) and [DeployHQ](https://www.deployhq.com/). Otherwise, you can follow the more detailed Git instructions below.

## Preparation and notes

You can create a deployment script that will access your site’s container via SSH and pull the latest version of your repo to your site.

You will need your [SSH details](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) and **Path** for your Kinsta site, which can be found on the **Info** page of your site in [MyKinsta](https://my.kinsta.com/)  (**Sites** > ***sitename*** > **Info**).

![Path and SSH terminal command in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-site-path-shh-command.png)

Path and SSH terminal command in MyKinsta.

In the examples below, we’re using GitHub. If you’re using a different service, replace the GitHub URL with your repository’s URL.

## Pull repo

The command to pull your repo to your **public** directory will look something like this:

Copy

```
ssh user@ip-address -p portnumber "cd public-root && git pull https:// github.com/USER/REPO.git "
```

Replace the bold values with your site’s details from MyKinsta:

- Replace **ssh user@ip-address -p port-number** with the **SSH terminal command** in MyKinsta (**Sites** > ***sitename*** > **Info** > **SFTP/SSH**).
- Replace **public-root** with the **Path** in MyKinsta (**Sites** > ***sitename*** > **Info** > **Environment details**).

### Pull a private repo

If it’s a private repo, you’ll need a way to authenticate or log in. Here’s an example of pulling a private repository from GitHub by adding login credentials to the command:

Copy

```
ssh user@ip-address -p portnumber "cd public-root && git pull https:// username:password @ github.com/USER/REPO.git "
```

### Pull a private repo with 2FA

If two-factor authentication is enabled, an access token/app password is needed. Here are instructions from some popular services on how to create a token to authenticate your command:

- [GitHub personal access tokens (PATs)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [Bitbucket app passwords](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/)
- [GitLab tokens](https://docs.gitlab.com/ee/security/token_overview.html)

Here’s an example of how to pull a repo that has 2FA enabled from GitHub, using a token to authenticate:

Copy

```
ssh user@ip-address -p portnumber "cd public-root && git pull https:// TOKEN @ github.com/USER/REPO.git "
```

Note: If the git pull above doesn’t contain credentials and the HTTPS path, it will attempt to look locally (rather than at the hosted repo) and show the message: “Everything up-to-date.”

## Clone repo

To clone a repo:

Copy

```
git clone https:// github.com/USER/REPO.git
```

### Clone a private repo

If it’s a private repo, you’ll need a way to authenticate or log in. Here’s an example of pulling a private repository from GitHub by adding login credentials to the command:

Copy

```
git clone https:// username:password @ github.com/USER/REPO.git
```

### Clone a private repo with 2FA

If two-factor authentication is enabled, an access token/app password is needed. Here are instructions from some popular services on how to create a token to authenticate your command:

- [GitHub personal access tokens (PATs)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [Bitbucket app passwords](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/)
- [GitLab tokens](https://docs.gitlab.com/ee/security/token_overview.html)

Here’s an example of how to clone a repo that has 2FA enabled at GitHub, using a token to authenticate:

Copy

```
git clone https:// TOKEN @ github.com/USER/REPO.git
```
