---
url: "https://kinsta.com/blog/remote-wordpress-development-kinsta-ssh/"
title: "Remote WordPress development on Kinsta with SSH"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "WordPress Hosting", "Remote WordPress development on Kinsta with SSH"]
kinsta_last_updated: "2026-02-05T09:57:10+00:00"
sitemap_lastmod: "2026-02-05T09:57:10"
fetched_at: "2026-10-07T22:42:51Z"
sha256: "76923d1c87a81a6c5981e714794854402835b754b6f844cf8b77a25d2e2c89be"
body_chars: 6792
extracted_with: "main article"
status: "live"
---

# Remote WordPress development on Kinsta with SSH

**Section:** Resource Center > Blog > WordPress Hosting > Remote WordPress development on Kinsta with SSH
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/remote-wordpress-development-kinsta-ssh/
**Kinsta last updated:** 2026-02-05T09:57:10+00:00

## On this page

- [Getting started](#getting-started)
- [Connecting to your Kinsta site using SSH](#connecting-to-your-kinsta-site-using-ssh)
- [When remote WordPress development makes sense](#when-remote-wordpress-development-makes-sense)

---

Author
:   [Joel Olawanle](https://kinsta.com/blog/author/joelolawanle/ "Posts by Joel Olawanle")

Updated
:   February 5, 2026

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![](https://kinsta.com/wp-content/uploads/2026/02/remote-wordpress-development-on-kinsta-with-ssh-1024x512.png)

Local WordPress development often starts simple but quickly becomes complex. As sites grow larger and databases get heavier, maintaining local environments can feel like unnecessary overhead, especially when your production and staging environments already live on [powerful hosting infrastructure](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/wordpress-infrastructure/).

With SSH access available on all Kinsta [managed hosting for WordPress](https://kinsta.com/wordpress-hosting/) plans, developers can connect securely to the Kinsta environment and work with their WordPress files remotely.

In this article, we explore how remote WordPress development on Kinsta works using SSH and VSCode. This approach also applies to other IDEs, such as Cursor and Antigravity.

## Getting started

To begin, you need access to your site’s SSH credentials. You can find these in **MyKinsta** > **WordPress Sites** > **[sitename]** > **Info**, under the **Primary SFTP/SSH user** section.

Here, you see the following connection details:

- Host
- Username
- Port
- Password or SSH key

![SSH and SFTP user details displayed in the MyKinsta dashboard.](https://kinsta.com/wp-content/uploads/2026/01/kinsta-ssh-stfp-user-details.png)

SSH/SFTP user details displayed in the MyKinsta.

These details are required to connect to your environment over SSH.

Next, install the [Remote – SSH extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) in Visual Studio Code or your preferred IDE. Click the **Extensions** icon in the left sidebar, search for **Remote – SSH**, and install the extension.

![Remote SSH extension interface showing connection options.](https://kinsta.com/wp-content/uploads/2026/01/remote-ssh-extension.png)

Remote SSH extension.

## Connecting to your Kinsta site using SSH

Before connecting through your IDE, it’s a good idea to confirm that SSH access works from your local machine.

Open a terminal (or PowerShell on Windows) and run the following command, replacing the placeholders with the values from MyKinsta:

```
ssh username@host -p port
```

If the connection is successful, you are prompted to enter your password and logged into the server. Once confirmed, you can use the same credentials in your IDE.

To connect using VS Code, open the **Command Palette**:

- **macOS:** `Cmd + Shift + P`
- **Windows/Linux:** `Ctrl + Shift + P`

From the Command Palette, select or search for **Remote-SSH: Open SSH Configuration File**.

![Accessing the SSH config file to manage saved SSH connections.](https://kinsta.com/wp-content/uploads/2026/01/access-ssh-config-file.png)

Manage saved SSH connections.

If this is your first time using Remote – SSH, VS Code prompts you to choose an SSH configuration file. Select the default SSH config file for your system (for example, `~/.ssh/config`).

![Using the SSH config file to simplify SSH connections.](https://kinsta.com/wp-content/uploads/2026/01/use-ssh-config-file.png)

Simplify SSH connections with SSH config file.

Once the file opens, add a new entry using your Kinsta SSH details:

```
Host kinsta-mysite
    HostName 12.345.67.890
    Port 12345
    User username
```

Save the file, then reopen the **Command Palette** and run **Remote-SSH: Connect to Host…**. Select `kinsta-mysite`, and VS Code opens a new remote window, prompting you to enter your password (or uses your SSH key, if configured).

![Adding a password for an SSH connection during setup.](https://kinsta.com/wp-content/uploads/2026/01/add-password-for-ssh.png)

Add password for an SSH connection.

Once connected, you can then choose a directory. For WordPress sites on Kinsta, your site files are located at `/www/[sitename]/public`.

![Accessing remote server files over an SSH connection.](https://kinsta.com/wp-content/uploads/2026/01/access-remote-files.png)

Accessing remote server files.

At this point, you are working directly on the remote environment.

![Remote files from a WordPress server accessed via SSH.](https://kinsta.com/wp-content/uploads/2026/01/remote-files-wordpress-server.png)

Remote files from a WordPress server.

VS Code or your preferred IDE treats the files as if they were local, allowing you to edit code, run commands, and use extensions without downloading the site to your machine.

## When remote WordPress development makes sense

Remote WordPress development isn’t meant to replace every local workflow, but it can be a better fit in specific scenarios where local setups become more of a burden than a benefit.

In a recent LinkedIn discussion about moving WordPress sites between hosts, [one developer highlighted](https://www.linkedin.com/feed/update/urn:li:activity:7405287995534168064/?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7405287995534168064%2C7405946455821172736%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287405946455821172736%2Curn%3Ali%3Aactivity%3A7405287995534168064%29) the ability to use VS Code’s SSH extension to work directly on a Kinsta-hosted site as a key advantage, noting that it eliminates local environment setup, avoids storing customer data on a developer’s machine, and simplifies working with large databases.

That said, remote development should be used intentionally. For ongoing feature development or larger changes, pairing this approach with a [staging environment](https://kinsta.com/docs/wordpress-hosting/staging-environment/) and [MyKinsta’s Push Environments](https://kinsta.com/docs/wordpress-hosting/wordpress-push-environments/) provides a safer and more structured workflow.

If you’re already hosting WordPress sites on Kinsta, SSH access is available by default. And if you’re exploring hosting options that support modern, developer-friendly workflows, Kinsta’s [managed hosting for WordPress](https://kinsta.com/wordpress-hosting/) is built with SSH, staging, and flexible deployment tools out of the box.

Joel Olawanle
[Kinsta](https://kinsta.com/)

Joel is a Frontend developer working at Kinsta as a Technical Editor. He is a passionate teacher with love for open source and has written over 300 technical articles majorly around JavaScript and it's frameworks.

- [Website](https://joelolawanle.com/)
- [LinkedIn](https://www.linkedin.com/in/olawanlejoel/)
- [Twitter](https://twitter.com/olawanle_joel)
- [YouTube](https://www.youtube.com/@joelolawanle)
