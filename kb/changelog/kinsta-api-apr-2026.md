---
url: "https://kinsta.com/changelog/kinsta-api-apr-2026/"
title: "Manage WordPress Admin auto-login users with the Kinsta API"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: ["Changelog", "Manage WordPress Admin auto-login users with the Kinsta API"]
kinsta_last_updated: "2026-05-20T20:30:51+00:00"
sitemap_lastmod: "2026-05-20T20:30:51+00:00"
fetched_at: "2026-10-07T22:37:39Z"
sha256: "25fb0dc45f7c024ae521bc0f01a3e7278b6e7841932676bdbf26336b3a2a1bb9"
body_chars: 3731
extracted_with: "main article"
status: "live"
---

# Manage WordPress Admin auto-login users with the Kinsta API

**Section:** Changelog > Manage WordPress Admin auto-login users with the Kinsta API
**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-apr-2026/
**Kinsta last updated:** 2026-05-20T20:30:51+00:00

## On this page

- [Check if a WordPress admin user exists](#check-if-a-wordpress-admin-user-exists)
- [Create a WordPress admin user](#create-a-wordpress-admin-user)
- [Generate a WordPress Admin login link](#generate-a-wordpress-admin-login-link)
- [Add WP Admin auto-login to your own workflows](#add-wp-admin-auto-login-to-your-own-workflows)

---

Updated
:   May 20, 2026

![An illustration representing steps for WordPress auto-login and the title "New API endpoints."](https://kinsta.com/wp-content/uploads/2026/04/kinsta-api-endpoints-for-wp-admin-login-1024x536.png)

In March, Kinsta introduced [one-click access to WordPress Admin](https://kinsta.com/changelog/wordpress-admin-login/) in MyKinsta. Now, we have extended that feature to the [Kinsta API](https://kinsta.com/docs/kinsta-api/) with three new endpoints for checking whether a matching WordPress admin user exists, creating one when needed, and generating a login link.

These additions make it easier to build your own onboarding, support, or admin workflows around WordPress Admin auto-login.

## Check if a WordPress admin user exists

The new `wpa-user-exists` endpoint lets you check whether a WordPress administrator account already exists for a given email address in an environment.

This is useful when you want to decide whether to create a user first or go straight to generating a login link.

**Example request:**

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/[email protected] \
  --header 'Authorization: Bearer <token>'
```

**Example response:**

```
{
  "has_wp_admin_user": true
}
```

You can find full request and response details in the API documentation for [checking whether a WordPress admin user exists](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/check-if-wp-admin-user-exists-by-email).

## Create a WordPress admin user

If the email address does not already exist in WordPress, you can create a new administrator account with the API’s `wpa-create-user` endpoint.

This is especially useful for automated setup flows, internal tooling, or support workflows where you want to prepare access before generating a login link.

**Example request:**

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-create-user \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "email": "[email protected]",
  "first_name": "John",
  "last_name": "Doe"
}
'
```

**Example response:**

```
{
  "create_wp_admin_user": true
}
```

You can learn more in the API documentation for [creating a WordPress admin user](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/create-wp-admin-user).

## Generate a WordPress Admin login link

Once a matching WordPress admin user exists, you can generate a login link using the API’s `wpa-login-url` endpoint.

This gives you a programmatic way to support the same WordPress Admin auto-login experience available in MyKinsta, while letting you choose which WordPress admin account to log in with.

**Example request:**

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-login-url \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "email": "[email protected]"
  }'
```

**Example response:**

```
{
  "login_link": "https://mysite.kinsta.cloud?wp-login.php?kinsta-sso=<token>"
}
```

You can find more details in the API documentation for [generating a WordPress Admin login link](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-wp-admin-login-link-by-email).

## Add WP Admin auto-login to your own workflows

These new endpoints extend the WordPress Admin auto-login feature beyond MyKinsta to the [Kinsta API](https://api-docs.kinsta.com/pages/introduction).

Whether you’re building internal tools, automating site setup, or simplifying admin access for your team, you now have more control over how WordPress Admin login is handled programmatically.
