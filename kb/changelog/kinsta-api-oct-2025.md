---
url: "https://kinsta.com/changelog/kinsta-api-oct-2025/"
title: "Manage SSH and SFTP access with the Kinsta API"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2026-05-20T20:31:40"
change_signal: "2026-05-20T20:31:40"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "ef8aed82978233fd2d1741cb41a4b9b3aa7dced1067dc792505624795bb7e160"
body_chars: 7437
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Manage SSH and SFTP access with the Kinsta API

**Product:** Changelog
**Source:** https://kinsta.com/changelog/kinsta-api-oct-2025/
**Kinsta last updated:** 2026-05-20T20:31:40

## On this page

- [Enable or disable SSH/SFTP access](#enable-or-disable-sshsftp-access)
- [Manage authentication methods](#manage-authentication-methods)
- [Generate and rotate SFTP passwords](#generate-and-rotate-sftp-passwords)
- [Manage IP allowlists](#manage-ip-allowlists)
- [Define credential expiration intervals](#define-credential-expiration-intervals)
- [Retrieve connection details](#retrieve-connection-details)
- [Build secure automation workflows](#build-secure-automation-workflows)

---

[SSH and SFTP acce](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/)[ss](https://kinsta.com/docs/wordpress-hosting/connecting-with-sftp/) have always been a major part of how developers connect securely to their [WordPress environments](https://kinsta.com/docs/wordpress-hosting/staging-environment/) at Kinsta.

Over the years, we’ve enhanced these tools with [IP allowlists](https://kinsta.com/changelog/ip-allowlists/), [multiple authentication methods](https://kinsta.com/changelog/sftp-ssh-updates/), and fine-grained access controls to strengthen security while maintaining developer flexibility.

![SFTP and SSH access options in MyKinsta](https://kinsta.com/wp-content/uploads/2025/10/mykinsta-sftp-ssh.png)

SFTP and SSH access options in MyKinsta.

Now, we’re extending those same capabilities to the [Kinsta API](https://kinsta.com/docs/kinsta-api/), expanding on our existing [SFTP user management endpoints](https://api-docs.kinsta.com/pages/additional-sftp-users/description) to give you complete programmatic control over SSH and SFTP access.

Let’s review the new endpoints and explore how you can use them to automate SSH and SFTP access across your environments.

## Enable or disable SSH/SFTP access

The new `/ssh/set-status` endpoint lets you programmatically enable or disable SSH and SFTP access for any environment.

This is useful for automating security in deployment workflows. For example, temporarily enabling access while pushing updates, then disabling it once the deployment is complete.

**Endpoint:**

```
POST /sites/environments/{env_id}/ssh/set-status
```

**Example request:**

```
curl -i -X POST \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-status' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  -H 'Content-Type: application/json' \
  -d '{ "is_enabled": true }'
```

See full request and response details in the [API reference](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/enabledisable-sftpssh).

## Manage authentication methods

You can now also control how users authenticate, whether via SSH keys or username and password.

This gives you more flexibility when managing different types of contributors or external tools that need to connect to your environments.

For example, while your internal team might use SSH key-based authentication exclusively, a temporary collaborator or automated service might need password access for a limited time. With this new API endpoint, you can enable or disable password authentication programmatically and remove it once it’s no longer needed.

**Endpoint:**

```
POST /sites/environments/{env_id}/ssh/set-password-status
```

**Example request:**

```
curl -i -X POST \  'https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-password-status' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  -H 'Content-Type: application/json' \
  -d '{ "is_enabled": true }'
```

See more in the [API reference](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/enabledisable-sftpssh-password-access).

## Generate and rotate SFTP passwords

Strong password management is critical for secure workflows, especially when multiple developers or automated services access environments.

With this release, you can now generate and retrieve SFTP passwords programmatically, making it easy to automate credential rotation or issue short-term access for deployments or contractors.

**Endpoints:**

```
POST /sites/environments/{env_id}/ssh/generate-password
GET /sites/environments/{env_id}/ssh/password
```

**Example request (generate password):**

```
curl -i -X POST \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/generate-password' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

You can find full request and response examples in the API reference for [generating passwords](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/generate-sftp-password) and [password retrieval](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-sftpssh-password).

## Manage IP allowlists

You can now programmatically manage IP allowlists for SSH and SFTP access. This provides a simple way to restrict environment access to only approved networks, helping teams enforce strong security policies without manual updates in MyKinsta.

For example, if your CI/CD runners or office IPs change frequently, your automation can update the allowlist dynamically, allowing only those systems to connect to your environments.

**Endpoints:**

```
POST /sites/environments/{env_id}/ssh/set-allowed-ips
GET /sites/environments/{env_id}/ssh/get-allowed-ips
```

**Example request (retrieve allowlist):**

```
curl -i -X GET \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/get-allowed-ips' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>'
```

**Example response:**

```
{
  "environment": {
    "active_container": {
      "stfp_ip_allowlist": ["127.0.0.1"]
    }
  }
}
```

You can find complete examples for both [retrieving](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-sftpssh-ip-allowlist) and [updating IP allowlists](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/update-sftpssh-ip-allowlist) in the API reference.

## Define credential expiration intervals

To help teams enforce short-lived credentials and reduce long-term exposure, you can now set SSH/SFTP credential expiration intervals directly through the API.

This allows you to automatically expire access after a defined period, depending on your team’s security policy.

**Endpoint:**

```
POST /sites/environments/{env_id}/ssh/change-expiration-interval
```

**Example request:**

```
curl -i -X POST \
  'https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/change-expiration-interval' \
  -H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
  -H 'Content-Type: application/json' \
  -d '{ "interval": "24h" }'
```

You can find detailed examples and available interval options in the [API reference](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/change-sftpssh-password-expiration-interval).

## Retrieve connection details

When managing multiple environments or automating deployments, it’s often useful to quickly fetch the SSH/SFTP connection details without logging in to MyKinsta.

The new `/ssh/config` endpoint allows you to programmatically retrieve all the necessary information to connect, including host, port, username, and even a ready-to-use SSH command.

**Endpoint:**

```
GET /sites/{site_id}/environments/{env_id}/ssh/config
```

**Example response:**

```
{
  "port": "22",
  "host": "example.sftp.kinsta.cloud",
  "user": "kinsta_user",
  "ssh_command": "ssh kinsta_user@example.sftp.kinsta.cloud -p 22"
}
```

You can find complete request and response examples in the [Kinsta API reference](https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-sftpssh-connections-config).

## Build secure automation workflows

With these new endpoints, you can fully automate SSH and SFTP access across your environments.

From onboarding developers to rotating credentials and enforcing network policies, the Kinsta API gives you the flexibility to integrate secure connection management into your existing DevOps workflows.

Explore all endpoint details and request examples in the [Kinsta API reference](https://api-docs.kinsta.com/).
