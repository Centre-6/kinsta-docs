---
url: "https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-github-cicd/"
title: "Site Management - GitHub Actions Integration"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "site-management"
section: []
kinsta_last_updated: "November 17, 2025"
sitemap_lastmod: "2025-11-17T09:38:43+00:00"
fetched_at: "2026-10-07T22:39:07Z"
sha256: "ea61ed715b187987968be0377b220f012124d134124ba071423158cf0d712a96"
body_chars: 8557
extracted_with: "main article"
status: "live"
---

# Site Management - GitHub Actions Integration

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-github-cicd/
**Kinsta last updated:** November 17, 2025

## On this page

- [1. Download a backup of your site](#1-download-a-backup-of-your-site)
- [2. Set up the GitHub repository](#2-set-up-the-github-repository)
- [3. Set up GitHub secrets for Kinsta](#3-set-up-github-secrets-for-kinsta)
- [4. Generate an SSH key on your Kinsta server](#4-generate-an-ssh-key-on-your-kinsta-server)
- [5. Add the SSH key to GitHub](#5-add-the-ssh-key-to-github)
- [6. Configure Git to use SSH on the Kinsta server](#6-configure-git-to-use-ssh-on-the-kinsta-server)
- [7. Create the GitHub Actions workflow](#7-create-the-github-actions-workflow)
- [8. Test the workflow](#8-test-the-workflow)

---

For advanced users, GitHub CI/CD (Continuous Integration/Continuous Delivery or Continuous Deployment) can automatically deploy code changes to your Kinsta site whenever a new commit is pushed to the designated branch. This setup enables seamless code deployment from your local environment via [SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) and [GitHub actions](https://docs.github.com/en/actions), allowing continuous updates to your site.

To follow these steps, you must have an existing site hosted on Kinsta and a [GitHub account](https://github.com/).

## 1. Download a backup of your site

You can download a backup of your site to set up the GitHub repository and work on it locally. Alternatively, you can use [DevKinsta](https://kinsta.com/docs/devkinsta/) to pull your site from the Kinsta server and work on it locally.

In [MyKinsta](https://my.kinsta.com/), go to**Sites** > ***sitename*** > **Backups** > **Download** > **Create backup now**.

![Create a downloadable backup in MyKinsta. ](https://kinsta.com/wp-content/uploads/2024/09/wordpress-create-backup-now.png)

Create a downloadable backup in MyKinsta.

When your backup is ready, click **Download**, save this to your local computer, and unzip the files to a folder.

## 2. Set up the GitHub repository

Open the folder containing your site’s files in your preferred code editor. To prevent uploading unnecessary WordPress core files, media uploads, or sensitive information, add a `.gitignore` file to the root directory of your project. You can use a standard WordPress [.gitignore template](https://github.com/github/gitignore/blob/main/WordPress.gitignore), copy its contents, and save it to ensure only the essential files are tracked.

Create a GitHub repository and [push your site’s files to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github#adding-a-local-repository-to-github-with-github-cli).

## 3. Set up GitHub secrets for Kinsta

To automate deployments from GitHub to Kinsta, you need key SSH details, including your username, password, port, and IP address. As these are sensitive, you must store them securely as GitHub Secrets.

Within GitHub, go to your repository, click **Settings** > **Secrets and variables** > **Actions** > **New repository secret**.

Add the following secrets using the **Primary SFTP/SSH user** details from your site’s **Info** page in MyKinsta:

|  |  |
| --- | --- |
| Secret name | Secret |
| KINSTA_SERVER_IP | Host e.g. 12.34.56.78 |
| KINSTA_USERNAME | Username e.g. kinstahelp |
| PASSWORD | Password |
| PORT | Port e.g. 12345 |

![SSH information to add secrets to GitHub.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-ssh-info-1.png)

SSH information to add secrets to GitHub.

## 4. Generate an SSH key on your Kinsta server

Open a new terminal and SSH into your Kinsta server using the **SSH terminal command** from your site’s **Info** page in MyKinsta.

![SSH terminal command for your site.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-ssh-terminal-command-4.png)

SSH terminal command for your site.

Enter your site’s password and then generate a new SSH key using the following command, replacing `[email protected]` with your email address:

Copy

```
ssh-keygen -t rsa -b 4096 -C "[email protected]"
```

Press **Enter** to save the key to the default location and leave the passphrase blank when prompted.

![Generate an SSH key.](https://kinsta.com/wp-content/uploads/2024/09/wordpress-generate-ssh-key-1024x600.png)

Generate an SSH key.

## 5. Add the SSH key to GitHub

Access the contents of the public key file (e.g., `~/.ssh/id_rsa.pub`), with the following command:

Copy

```
cat ~/.ssh/id_rsa.pub
```

In GitHub, go to **Settings** > **SSH and GPG keys** > **New SSH key**, enter a title (e.g., “Kinsta Server Key”), ensure the **Key type** is **Authentication Key**, paste the public key into **Key**, and click **Add SSH Key**. If you are a member of an organization using Deploy keys, you must add your SSH key as a deploy key. For more details, see the [GitHub documentation on Deploy keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys).

## 6. Configure Git to use SSH on the Kinsta server

In MyKinsta, on the **Info** page, copy the **Path** from **Environment details**.

![Path on your site's Info page.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-site-path-4.png)

Path on your site’s Info page.

In the terminal, navigate to your site’s live directory with the following command, replacing `/www/your-site/public` with the path copied from MyKinsta.

Copy

```
cd /www/your-site/public
```

Initialize the directory as a Git repository and set the remote URL to use SSH with the following command, replacing `your-username` and `your-repo` with your git credentials and repository:

Copy

```
git init
git remote add origin [email protected]:your-username/your-repo.git
```

Confirm that the SSH setup works by running the following command:

Copy

```
ssh -T [email protected]
```

You should see a message similar to: “Hi your-username! You’ve successfully authenticated, but GitHub does not provide shell access.” Your Kinsta server is now ready to receive and deploy updates from GitHub directly through GitHub Actions.

## 7. Create the GitHub Actions workflow

This workflow deploys changes to Kinsta automatically whenever you push to the `main` branch. To automate the deployment, you need to define how the deployment will happen using a [YAML](https://yaml.org/) file.

In your GitHub repository, create a new directory called `.github/workflows` inside this directory, create a new file called `deploy.yml` and add the following content to the file, replacing `your-site` with the folder name from the path on your Kinsta site:

Copy

```
name: Deploy to Kinsta

on:
  push:
    branches:
      - main # Trigger the workflow only when changes are pushed to the main branch

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      # Setup Node.js (only if needed for build tasks)
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20.x'

      # Checkout the latest code from the GitHub repository
      - name: Checkout code
        uses: actions/[email protected]

      # Deploy to Kinsta via SSH
      - name: Deploy via SSH
        uses: appleboy/[email protected]
        with:
          host: ${{ secrets.KINSTA_SERVER_IP }}
          username: ${{ secrets.KINSTA_USERNAME }}
          password: ${{ secrets.PASSWORD }}
          port: ${{ secrets.PORT }} # Optional, default is 22
          script: |
            # Navigate to the live site directory
            cd /www/your-site/public

            # Pull the latest changes from the GitHub repository
            git fetch origin main
            git reset --hard origin/main  # Ensure the live site matches the latest main branch
```

This workflow does the following:

- **Trigger**: The workflow is triggered every time code is pushed to the `main` branch of your GitHub repository.
- **Jobs**: The workflow contains one `job` called `deploy`, which runs on an Ubuntu virtual machine (`ubuntu-latest`).
- **Checkout code**: This uses the `actions/[email protected]` action to pull the latest code from your GitHub repository.
- **Deploy to Kinsta via SSH**:
  - The `appleboy/ssh-action` plugin establishes an SSH connection with your Kinsta server using the secrets you’ve stored in GitHub (host, username, password, and, optionally, the port). The script within this step runs the following commands:
  - **Deployment Commands**:
    - `cd /www/your-site/private`: Navigates to the live directory where WordPress is hosted.
    - `git fetch origin main`: Fetches the latest changes from the `main` branch in your GitHub repository.
    - `git reset --hard origin/main`: Updates the live site with the latest code from the branch.

## 8. Test the workflow

Once you’ve set up the workflow, you can test it by pushing a small change to your GitHub repository’s `main` branch. Each time you push a change, GitHub Actions automatically triggers the deployment, pulling the latest version of your code and deploying it to your live site on Kinsta.

You can monitor the status of your deployment by going to the **Actions** tab in your GitHub repository. If the workflow encounters errors, you’ll see detailed logs to help you troubleshoot and fix the issues.
