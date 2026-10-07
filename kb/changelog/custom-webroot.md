---
url: "https://kinsta.com/changelog/custom-webroot/"
title: "Set custom webroots for your WordPress sites with Kinsta API"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-09-16T09:54:26"
change_signal: "2026-09-16T09:54:26"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "efdb83ea625604b9a3fe34f11f00e364122e22a02191ec95f3d5a5100f19718d"
body_chars: 2807
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Set custom webroots for your WordPress sites with Kinsta API

**Product:** Changelog
**Source:** https://kinsta.com/changelog/custom-webroot/
**Kinsta last updated:** 2026-09-16T09:54:26

---

You can now set custom webroots for your WordPress sites at Kinsta using our public [API](https://kinsta.com/docs/kinsta-api/). This gives developers and agencies greater flexibility when managing deployments, version control, or customized site structures, without needing to contact [support](https://kinsta.com/kinsta-support/).

Previously, if you wanted to change a site’s webroot (for example, to support structures like [Bedrock](https://roots.io/bedrock/), where the public-facing folder is `/public/web`), you had to open a support ticket. Now, you can handle it programmatically, saving time for teams managing multiple environments or complex workflows.

## How to change your WordPress site’s webroot

To change a site’s webroot, send a `POST` request to the Kinsta API’s `/change-webroot-subfolder` endpoint for a specific environment.

Here’s an example `POST` request:

```
curl -i -X POST \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/change-webroot-subfolder' \
  -H 'Authorization: Bearer ' \
  -H 'Content-Type: application/json' \
  -d '{
    "web_root_subfolder": "your_subfolder_name",
    "clear_all_cache": true,
    "refresh_plugins_and_themes": true
  }'
```

In this request:

- `env_id` is the ID of the WordPress environment you want to update.
- `web_root_subfolder` sets the new subfolder you want to use as the webroot (for example, `/web`, `/release_v2`, or nested paths like `/current/web`).
- `clear_all_cache` (optional) determines whether the site’s cache should be cleared during the change. Defaults to `true`.
- `refresh_plugins_and_themes` (optional) refreshes plugin and theme files to avoid conflicts after switching. Defaults to `true`.

Once you send the request, Kinsta updates the server configuration to point to the new subfolder. Additionally, it can clear the cache and refresh plugin and theme files if you have those options enabled.

After the process completes, the updated webroot path appears in your MyKinsta **Environment details**, as shown below.

![Updated webroot path displayed in the Environment details](https://kinsta.com/wp-content/uploads/2025/04/webroot-mykinsta.png)

Updated webroot path displayed in the Environment details.

## WordPress management that fits your workflow

With the [Kinsta API](https://api-docs.kinsta.com/), you can do more than just set a custom webroot. Automate updates across multiple sites, integrate webroot changes into your deployment process, or even build tools like [Slackbots](https://kinsta.com/blog/create-slackbot-site-management/) to manage your environments on the fly.

It’s all about giving you more control — and making it easier to run WordPress sites the way you want.

Not a Kinsta customer yet? Check out our [hosting plans](https://kinsta.com/pricing/) to see what’s possible.
