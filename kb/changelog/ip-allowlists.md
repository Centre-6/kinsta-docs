---
url: "https://kinsta.com/changelog/ip-allowlists/"
title: "Lock down SFTP/SSH and phpMyAdmin access with IP allowlists"
tier: "changelog"
product: "changelog"
product_label: "Changelog"
subsection:
section: []
kinsta_last_updated: "2024-07-25T01:42:54"
change_signal: "2024-07-25T01:42:54"
fetched_at: "2026-10-07T22:58:22Z"
sha256: "55ba7892f0a6fe8f247a5cebbb262e8d5ae1660d0048f982691b651e83c4387d"
body_chars: 4288
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Lock down SFTP/SSH and phpMyAdmin access with IP allowlists

**Product:** Changelog
**Source:** https://kinsta.com/changelog/ip-allowlists/
**Kinsta last updated:** 2024-07-25T01:42:54

## On this page

- [How to configure IP allowlists in MyKinsta](#how-to-configure-ip-allowlists-in-mykinsta)
  - [Removing addresses from the IP allowlist](#removing-addresses-from-the-ip-allowlist)
- [We take security seriously at Kinsta](#we-take-security-seriously-at-kinsta)

---

Kinsta’s [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/) customers can now restrict access to their websites via SFTP/SSH and to their phpMyAdmin database dashboards to clients connecting only from allowed IP addresses.

This security enhancement is in addition to other recent updates to [SFTP/SSH configuration](https://kinsta.com/changelog/sftp-ssh-updates/) within the [MyKinsta dashboard](https://kinsta.com/mykinsta/) that help guard access to your websites. The earlier enhancements added support for:

- Disabling SFTP/SSH access.
- Disabling passwords as an authentication method.
- Auto-expiration of passwords.
- Downloading access configurations for use in third-party applications.

With the addition of IP allowlists for SFTP/SSH and [phpMyAdmin](https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database-access/), you can eliminate connection attempts from unknown IP addresses.

## How to configure IP allowlists in MyKinsta

IP allowlists are managed on the **Site Information** page in MyKinsta, found under **WordPress Sites** > ***sitename*** > **Info**.

On the **SFTP/SSH** panel, you’ll find an edit icon to the right of the **IP allowlist** label. Click that icon to begin adding or deleting IP addresses that are permitted to connect for shell or SFTP access:

![Screenshot showing the SFTP/SSH panel in MyKinsta and the edit icon for an IP allowlist.](https://kinsta.com/wp-content/uploads/2024/07/mykinsta-ip-allowlist-sftp-ssh.png)

Clicking the edit icon to manage an SFTP/SSH IP allowlist.

Similarly, you can specify IPs permitted to access the phpMyAdmin tool by clicking the edit icon beside the **IP allowlist** label in the **Database access** panel:

![Screenshot showing the database access panel in MyKinsta and the edit icon for an IP allowlist.](https://kinsta.com/wp-content/uploads/2024/07/mykinsta-ip-allowlist-phpmyadmin.png)

Clicking the edit icon to manage a phpMyAdmin IP allowlist.

Clicking the allowlist edit icon on either panel will launch an **Update IP allowlist** dialog like the one below:

![Screenshot showing the dialog or editing IP allowlists in MyKinsta.](https://kinsta.com/wp-content/uploads/2024/07/mykinsta-ip-allowlist-update-ipaddresses.png)

Adding an IP address to an allowlist in MyKinsta.

Build an allowlist by entering valid addresses in the **Add IP addresses** field and clicking the **Add** button.

Some tips:

- You can add multiple IP addresses at once by separating them with commas.
- You can specify an IP address block using the usual syntax. Example: **35.238.77.1/32**.

When an allowlist is active for SFTP/SSH or phpMyAdmin, the number of IPs allowed will be shown on the service’s panel on the **Site Information** page:

![Screenshot showing a database access panel in MyKinsta a report of two addresses in an IP allowlist.](https://kinsta.com/wp-content/uploads/2024/07/mykinsta-ip-allowlist-allowed-ips.png)

This **Database access** panel indicates the phpMyAdmin allowlist contains two IPs.

### Removing addresses from the IP allowlist

There are two ways to remove entries within the **Update IP allowlist** dialog:

1. Click the trashcan icon beside individual entries.
2. Use the checkboxes to select entries in the list and then click the red **Remove IP address(es)** button.

![Screenshot showing an address highlighted in an IP allowlist and the button used to delete it.](https://kinsta.com/wp-content/uploads/2024/07/mykinsta-ip-allowlist-delete-ips.png)

Removing the selected IP address from an allowlist.

## We take security seriously at Kinsta

Kinsta leverages the [Google Cloud](https://kinsta.com/google-cloud-alternative/) and [Cloudflare](https://kinsta.com/blog/cloudflare-integration/) to provide additional protection for customer websites, including firewalling, DDoS protection, and free wildcard SSL.

Independent auditors have also confirmed our compliance with [System and Organization Controls](https://kinsta.com/docs/service-information/soc-2/) (SOC) security standards. To learn more, read Kinsta’s SOC 2 Type II report. (You can Request it through our [Trust report page](https://trust.kinsta.com/).)

Get started with our secure environment by finding the best [web hosting plan](https://kinsta.com/pricing/) for you.
