---
url: "https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-bitbucket-pipelines/"
title: "Site Management - Bitbucket Pipelines"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "site-management"
section: []
kinsta_last_updated: "May 27, 2026"
sitemap_lastmod: "2026-05-27T14:04:50+00:00"
fetched_at: "2026-10-07T22:40:14Z"
sha256: "de3b928b35636a68e4d516d5faf93edcbbf8fb5c407ade785dcb349b22882789"
body_chars: 12244
extracted_with: "main article"
status: "live"
---

# Site Management - Bitbucket Pipelines

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-bitbucket-pipelines/
**Kinsta last updated:** May 27, 2026

## On this page

- [1. Download a backup of your site](#1-download-a-backup-of-your-site)
- [2. Set up the Bitbucket repository](#2-set-up-the-bitbucket-repository)
- [3. Set up SSH authentication](#3-set-up-ssh-authentication)
- [4. Push your code to Bitbucket](#4-push-your-code-to-bitbucket)
- [5. Set up SSH access in MyKinsta to Bitbucket](#5-set-up-ssh-access-in-mykinsta-to-bitbucket)
- [6. Add SSH public key to MyKinsta](#6-add-ssh-public-key-to-mykinsta)
- [7. Add the SSH key to Bitbucket](#7-add-the-ssh-key-to-bitbucket)
- [8. Configure Git to use SSH on the Kinsta server](#8-configure-git-to-use-ssh-on-the-kinsta-server)
- [9. Add environment variables to Bitbucket](#9-add-environment-variables-to-bitbucket)
- [10. Bitbucket Pipeline configuration](#10-bitbucket-pipeline-configuration)
- [11. Test the pipeline](#11-test-the-pipeline)

---

For advanced users, Bitbucket CI/CD (Continuous Integration/Continuous Delivery or Continuous Deployment) can automatically deploy code changes to your Kinsta site whenever a new commit is pushed to the designated branch. This setup enables seamless code deployment from your local environment via [SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) and [Bitbucket Pipelines](https://www.atlassian.com/software/bitbucket/features/pipelines), allowing continuous updates to your site.

To follow these steps, you must have an existing site hosted on Kinsta and a [Bitbucket account](https://bitbucket.org/product/).

## 1. Download a backup of your site

You can download a backup of your site to set up the Bitbucket repository and work on it locally. Alternatively, you can use [DevKinsta](https://kinsta.com/docs/devkinsta/) to pull your site from the Kinsta server and work on it locally.

In [MyKinsta](https://my.kinsta.com/), go to**Sites** > ***sitename*** > **Backups** > **Download** > **Create backup now**.

![Create a downloadable backup in MyKinsta. ](https://kinsta.com/wp-content/uploads/2024/09/wordpress-create-backup-now.png)

Create a downloadable backup in MyKinsta.

When your backup is ready, click **Download**, save this to your local computer, and unzip the files to a folder.

## 2. Set up the Bitbucket repository

Open the folder containing your site’s files in your preferred code editor. To prevent uploading unnecessary WordPress core files, media uploads, or sensitive information, add a `.gitignore` file to the root directory of your project. You can use a standard WordPress [.gitignore template](https://github.com/github/gitignore/blob/main/WordPress.gitignore), copy its contents, and save it to ensure only the essential files are tracked.

In Bitbucket, go to your workspace and create a new repository. Ensure **Include a README** and **Include .gitignore** are set to **No**. Once the repository is created, you also need to enable pipelines. In the repository, go to **Settings** and select **Enable Pipelines**.

## 3. Set up SSH authentication

To securely connect to your Bitbucket repository, you must set up SSH authentication.

Generate an SSH key pair on your local machine using the following command, replacing `[email protected]` with your email address:

Copy

```
ssh-keygen -t ed25519 -C "[email protected]"
```

Save the key pair in a location you can easily reference (e.g., `~/.ssh/id_rsa_bitbucket`).

Open and copy the public key (`~/.ssh/id_rsa_bitbucket.pub`). In Bitbucket, go to **Settings** > **Personal Bitbucket Settings** > **SSH Keys** > **Add key** and paste the details of the public key. This authorizes your machine to push code securely.

![Add the SSH key to Bitbucket Settings.](https://kinsta.com/wp-content/uploads/2024/11/add-ssh-key-bitbucket.png)

Add the SSH key to Bitbucket Settings.

Add the same key in [MyKinsta](https://my.kinsta.com/), go to your username > **User Settings** > **Add SSH Key**, paste the same public key details, and click **Add SSH key**.

## 4. Push your code to Bitbucket

Open the folder containing your site’s files in your preferred code editor and use the following commands to push your code to Bitbucket, replacing `your-username` and `your-repo` with your Bitbucket username and repository name:

Copy

```
# Initialize a new Git repository
git init
# Stage all files for the first commit
git add .
# Commit the files with a message
git commit -m "Initial commit of WordPress site files"
# Add the Bitbucket repository as the remote origin
git remote add origin [email protected]:your-username/your-repo.git
# Push the files to Bitbucket
git push -u origin main
```

## 5. Set up SSH access in MyKinsta to Bitbucket

To allow the Kinsta server to pull code from Bitbucket, you must generate an SSH key on the server and add its public key to your MyKinsta and Bitbucket account.

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

## 6. Add SSH public key to MyKinsta

This step adds your SSH public key to your site’s **authorized_keys** file (only writable by root and MyKinsta) and will allow Bitbucket to SSH into your site to deploy code changes. In MyKinsta, click your name in the upper-right corner and select **User settings** from the dropdown menu.

![MyKinsta user settings.](https://kinsta.com/wp-content/uploads/2026/01/wordpress-user-settings.png)

MyKinsta user settings.

Scroll down and click the **Add SSH key** button.

![Add SSH key in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/06/add-ssh-key.png)

Add SSH key in MyKinsta.

In the modal/pop-up window, specify a **Label** (name) for the SSH key, paste your public key in the **SSH key** field, and click **Add SSH key** to finalize the process.

![Add your SSH key in MyKinsta.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-add-ssh-key-add-1024x471.png)

Add your SSH key in MyKinsta.

## 7. Add the SSH key to Bitbucket

Access the contents of the public key file (e.g., `~/.ssh/id_rsa.pub`), with the following command:

Copy

```
cat ~/.ssh/id_rsa.pub
```

Copy the entire output, then in Bitbucket, go to **Settings** > **Personal Bitbucket Settings** > **SSH Keys** > **Add key** and add the public key. This authorizes the Kinsta server to access your Bitbucket repository securely.

## 8. Configure Git to use SSH on the Kinsta server

In MyKinsta, on the **Info** page, copy the **Path** from **Environment details**.

![Path on the site's Info page.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-site-path-4.png)

Path on the site’s Info page.

In the terminal, navigate to your site’s live directory with the following command, replacing `/www/your-site/public` with the path copied from MyKinsta.

Copy

```
cd /www/your-site/public
```

Initialize the directory as a Git repository and set the remote URL to use SSH with the following command, replacing `your-username` and `your-repo` with your Bitbucket credentials and repository:

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

You should see a message similar to: “authenticated via ssh key. You can use git to connect to Bitbucket. Shell access is disabled.” Your Kinsta server is now ready to receive and deploy updates from Bitbucket directly through Bitbucket pipelines.

## 9. Add environment variables to Bitbucket

To store sensitive Kinsta information securely, you need to add environment variables to Bitbucket. In MyKinsta, go to **Sites** > ***sitename***> **Info**; from the **Primary** **SFTP/SSH user** section, you need the **Host**, **Port**, and **Username.**

![Username, IP address, and Port from the site's Info page.](https://kinsta.com/wp-content/uploads/2023/11/wordpress-sftp-ssh-info-1.png)

Username, IP address, and Port from the site’s Info page.

In Bitbucket, go to **Repository Settings** > **Repository Variables** and add the following:

- `KINSTA_USERNAME`: This is your SSH **Username** for the Kinsta server. Bitbucket Pipelines uses it to log in and execute deployment commands.
- `KINSTA_SERVER_IP`: This is the SSH **Host** address of your Kinsta server. It allows Bitbucket Pipelines to know which server to connect to for deployment.
- `PORT`: This is the SSH **Port** used by your Kinsta server. Kinsta servers use a custom port, so you must specify that here.
- `SSH_PRIVATE_KEY`: This is your base64-encoded SSH private key from your local machine. Bitbucket pipelines use this key to authenticate to your Kinsta server. To encode your private key in base64, run the following command, copy the output, and add it as the value:

  Copy

  ```
  cat ~/.ssh/id_rsa | base64
  ```

## 10. Bitbucket Pipeline configuration

To automate deployments, you need to create a `bitbucket-pipelines.yml` configuration file. In the local folder containing your site’s files, create a new file called `bitbucket-pipelines.yml` and add the following content to the file, replacing `your-site` with the folder name from the path on your Kinsta site:

Copy

```
image: atlassian/default-image:3

pipelines:
  branches:
    main:
      - step:
          name: Deploy to Kinsta
          script:
            - pipe: atlassian/ssh-run:0.8.1
              variables:
                SSH_USER: $KINSTA_USERNAME
                SERVER: $KINSTA_SERVER_IP
                PORT: $PORT
                COMMAND: |
                  cd /www/your-site/public &&
                  git fetch origin main &&
                  git reset --hard origin/main
                SSH_KEY: $SSH_PRIVATE_KEY
                DEBUG: 'true'
```

This pipeline is set up to automate deployments to your Kinsta server whenever there’s a new push to the `main` branch. The workflow does the following:

- **Image:** The `image` declaration defines the environment used by Bitbucket Pipelines and can usually be left unchanged.
- **Pipeline trigger**: The `pipelines` section is configured to trigger when a push is made to the `main` branch. This means any new commit to the `main` branch automatically starts the deployment.
- **Step**: This is named “Deploy to Kinsta” for clarity. It contains the main deployment actions.
- **SSH-run pipe**: This uses the `atlassian/ssh-run` pipe, which allows Bitbucket to connect to your Kinsta server via SSH and execute commands remotely. This pipe simplifies setting up an SSH session, running the commands, and closing the session, so there’s no need to manage SSH details manually in the script.
- **Deployment commands**: The `COMMAND` block contains the commands that deploy the latest code to your WordPress site. Here’s what each command does:
  - The first command navigates to the live directory where WordPress is hosted.
  - The second command then runs `git fetch origin main` to pull the latest code from the main branch in Bitbucket.
  - The last command then updates the live site with the latest code from the main branch.

This configuration handles all aspects of the deployment – from connecting to Kinsta to updating your site files – so your WordPress site on Kinsta will stay up-to-date automatically with each push to `main`.

## 11. Test the pipeline

Commit and push the `bitbucket-pipelines.yml` configuration file to the `main` branch. This automatically triggers the pipeline and starts the deployment process. You can monitor the deployment’s progress in the Bitbucket Pipelines dashboard. If everything is set up correctly, Bitbucket will connect to your Kinsta server, fetch the latest code, and deploy it to your live site.

For troubleshooting, check the pipeline logs in Bitbucket, especially if `DEBUG` is set to `"true"`. The logs provide detailed information about each step, which can help identify any connection or configuration issues.

If the pipeline isn’t connecting to your Kinsta server properly, this could be due to the remote URL being set to HTTPS instead of SSH. To confirm, [SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/) into your Kinsta server and run the following command in your site’s directory:

Copy

```
git remote -v
```

If it shows `https://` instead of `ssh://`, you’ll need to update the remote URL so that the SSH key can be used for authentication. Run the following command to switch to SSH:

Copy

```
git remote set-url origin [email protected]:your-username/your-repo.git
```

After updating the URL, push your changes again, and the pipeline should connect using the SSH key.
