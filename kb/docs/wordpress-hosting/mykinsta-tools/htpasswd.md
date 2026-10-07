---
url: "https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/htpasswd/"
title: "Tools - htpasswd Protection"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "mykinsta-tools"
section: []
kinsta_last_updated: "September 24, 2024"
sitemap_lastmod: "2024-09-24T14:13:22+00:00"
fetched_at: "2026-10-07T22:38:24Z"
sha256: "7340c2794bfa14097876ac0ef5e598c88dbc1b0b135d064f83fa8cca32499ecf"
body_chars: 4304
extracted_with: "main article"
status: "live"
---

# Tools - htpasswd Protection

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/htpasswd/
**Kinsta last updated:** September 24, 2024

## On this page

- [How to enable password protection on your site](#how-to-enable-password-protection-on-your-site)
  - [Wrong credentials or canceling prompt](#wrong-credentials-or-canceling-prompt)
  - [Alternate prompts in different browsers](#alternate-prompts-in-different-browsers)
- [How to change credentials or disable password protection](#how-to-change-credentials-or-disable-password-protection)

---

When working on a WordPress site, there may be times when you may not want it to be accessible to the public. Perhaps you’re developing a site for a client and only want that client to have access. A relatively easy way to lock down your site is to password protect it. You can do this with our MyKinsta **.htpasswd** tool, which uses what is referred to as basic HTTP authentication.

## How to enable password protection on your site

Our **.htpasswd** tool adds password protection to your **entire** WordPress site, not just the WordPress admin. The tool is available for both live sites and [staging environments](https://kinsta.com/docs/wordpress-hosting/staging-environment/).

1. Log in to [MyKinsta](https://my.kinsta.com/login/).
2. Go to**Sites** and click on the site that you want to enable password protection on.
3. Click on **Tools** on the left-hand side. Then scroll down, and under **Password protection**, click **Enable**.
   ![Enable .htpasswd protection.](https://kinsta.com/wp-content/uploads/2025/06/wordpress-tools-password-protection.png)

   Enable .htpasswd protection.
4. In the **Enable password protection** modal/pop-up that appears, enter a **Username** and **Password** to use for authentication. To generate a new password and copy it to your clipboard, use the refresh (redo) and copy icons next to the password field. Then click the **Enable** button.
   ![.htpasswd username and password](https://kinsta.com/wp-content/uploads/2023/11/wordpress-enable-password-enable-1024x329.png)

   .htpasswd username and password
5. You can then visit your WordPress site to ensure it’s working correctly. When trying to access your site, you will see a modal/pop-up asking for your **Username** and **Password**. Enter the Username and Password you set up in the **Password protection** tool in MyKinsta, and click the **Sign In** button.

![.htpasswd authentication prompt](https://kinsta.com/wp-content/uploads/2019/06/htpasswd-authentication-prompt.png)

.htpasswd authentication prompt

You will then be able to access your WordPress site for the remainder of your browser’s session.

![.htpasswd successful authentication](https://kinsta.com/wp-content/uploads/2019/08/htpasswd-successful-authentication.png)

.htpasswd successful authentication

### Wrong credentials or canceling prompt

If a wrong username or password is entered, the modal/pop-up will reappear. If the credentials prompt is closed or canceled, the browser will return a 401 [HTTP status code](https://kinsta.com/blog/http-status-codes/), and the user will see a “[401 Authorization Required](https://kinsta.com/blog/401-error/)” message.

![Nginx 401 authorization required error in Chrome](https://kinsta.com/wp-content/uploads/2019/08/nginx-401-authorization-required-chrome.png)

Nginx 401 authorization required error in Chrome

### Alternate prompts in different browsers

The security prompt may appear slightly different, depending on your browser. In Chrome, the modal/pop-up is titled **Sign in** (as shown above).

In Mozilla Firefox, it will be an **Authentication Required** modal/pop-up.

![Authentication required prompt in Firefox.](https://kinsta.com/wp-content/uploads/2019/08/authentication-required-prompt-in-firefox.png)

Authentication required prompt in Firefox.

In Safari, it will be a **Log in to…** modal/pop-up.

![.htpasswd login prompt in Safari](https://kinsta.com/wp-content/uploads/2019/08/htpasswd-login-prompt-safari.png)

.htpasswd login prompt in Safari

## How to change credentials or disable password protection

You can change the credentials or disable password protection at any time by going back to the **.htpasswd** tool in [MyKinsta](https://my.kinsta.com/) and clicking the **Modify** button.

![Change or disable Password protection.](https://kinsta.com/wp-content/uploads/2025/06/wordpress-tools-password-protection-modify.png)

Change or disable Password protection.

If you need to password-protect just a portion of your site, a specific page, or further customize logins, check out our in-depth guide on [WordPress password protection](https://kinsta.com/blog/password-protect-wordpress-site/).

You can also [open a new chat](https://kinsta.com/docs/support/contact-support/) with our Support team if you need additional help. We’re here to help.
