---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/wordpress-connection-errors/"
title: "Troubleshooting - Connection Errors"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-troubleshooting"
section: []
kinsta_last_updated: "October 11, 2024"
sitemap_lastmod: "2024-10-11T15:21:09+00:00"
fetched_at: "2026-10-07T22:38:25Z"
sha256: "c0354bfa2d7629dea20c7a879ad5f1468c4c8061ff8dde8ac154ca6cae3c88d6"
body_chars: 6775
extracted_with: "main article"
status: "live"
---

# Troubleshooting - Connection Errors

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/wordpress-connection-errors/
**Kinsta last updated:** October 11, 2024

## On this page

- [Troubleshoot connection errors](#troubleshoot-connection-errors)
  - [Client-side](#client-side)
  - [Server-side](#server-side)

---

When you try to connect to your site, you may encounter an error such as one of the following, depending on your browser:

> This site can’t be reached  
> Hmm. We’re having trouble finding that site.  
> Hmmm… can’t reach this page.  
> Safari Can’t Find the Server  
> Safari Can’t Open the Page

You may even get a related error, such as:

> ERR_NAME_NOT_RESOLVED  
> ERR_CONNECTION_TIMED_OUT  
> ERR_CONNECTION_REFUSED

These errors do not give a specific reason for the error; therefore, you must troubleshoot both the client and the server to diagnose the issue.

## Troubleshoot connection errors

### Client-side

To determine if the issue is on the client side, you should check the following:

1. **Check your Internet connection**:
   - Try loading other websites to see if you can connect to them.
   - Restart your router or modem.
   - Try connecting to a different Wi-Fi or use mobile data to see if the problem persists.
2. **Clear your browser’s cache**:
   - Cached data can sometimes cause connection issues, especially if the website’s IP address or configuration has changed.
   - Open the site in incognito mode to rule out any cache or cookie-related issues.
3. **Disable Browser Extensions**: Some extensions (like VPNs, ad blockers, or security tools) can block websites. Disable all extensions and try accessing the site again.
4. **Check Firewall and Security Software**:
   - Overly strict security settings can block certain websites. Temporarily turn off your firewall, antivirus, or security software to see if that resolves the issue. If you’re unsure how to do this, refer to [Disable the Windows firewall](https://support.microsoft.com/en-us/windows/turn-microsoft-defender-firewall-on-or-off-ec0844f7-aebd-0583-67fe-601ecf5d774f) or [Disable the Firewall in macOS](https://support.apple.com/en-gb/guide/mac-help/mh11783/mac).
   - Some browsers have built-in security features that could block access to the site. Make sure your browser’s settings are not blocking the site.
5. **Ensure no proxy is interfering**: If your browser or system uses an unreachable or misconfigured proxy, it could block access to sites. For example, in Chrome, go to **Settings** > **Advanced** > **System** > **Open your computer’s proxy settings** and make sure no proxy is active unless you need one.
6. **Update Browser and Operating System**:
   - An outdated browser can sometimes cause compatibility issues with websites. Check for updates in your browser’s settings.
   - Keeping your OS updated ensures that network-related bugs are fixed.
7. **Check for DNS Issues**:
   - Sometimes, outdated DNS records can cause problems. Flush your DNS cache to clear this.
     - Windows: Open the Command Prompt and type `ipconfig /flushdns`.
     - macOS: Open the Terminal and type `sudo killall -HUP mDNSResponder`.
   - You can change your DNS settings to a more reliable service like Google DNS (8.8.8.8, 8.8.4.4) or Cloudflare DNS (1.1.1.1), or look up a [free DNS server](https://www.lifewire.com/free-and-public-dns-servers-2626062/) to use.
     - Windows: Go to **Control Panel** > **Network and Sharing Center** > **Change adapter settings**, right-click your network connection, and select **Properties**. Select **Internet Protocol Version 4 (TCP/IPv4)**, and change the DNS settings.
     - macOS: Go to **System Settings** > **Network** > Select your network and click **Details**, then go to the **DNS** tab and enter the new DNS addresses.

### Server-side

If you are the owner of the site that has the connection error, you should check the following:

1. **Check MyKinsta is running**: View the [MyKinsta status page](https://status.kinsta.com/) to see if there are any issues we are currently aware of. You can also subscribe to updates, and we’ll notify you when there is an issue.
2. **Verify DNS Configuration**:
   - Ensure that your domain is pointing to the correct server IP address. You can use [DNS Checker](https://dnschecker.org/) to check your DNS records. Look for an A record (for IPv4) or an AAAA record (for IPv6) to ensure the domain resolves to the correct IP, and ensure CNAME records are correctly configured.
   - If you recently changed your DNS settings, there could be a propagation delay (which can take up to 48 hours), and not all users will be able to access your site during this time.
   - Verify that your domain’s nameservers are correct with your domain registrar (e.g., GoDaddy, Namecheap, etc.). If nameservers are incorrect, your domain will fail to resolve.
3. **Check SSL Certificates**: Kinsta includes free SSL certificates. Once you’ve added your domain, this certificate will automatically secure your site. However, if you’re using a [custom SSL certificate](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/#option-two-custom-ssl-certificate), you should check that it is valid and hasn’t expired. If the SSL certificate has expired, renew it immediately through your SSL provider (e.g., Let’s Encrypt, Cloudflare, etc.).
4. **Check your server logs**: Your site’s [server logs](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/) can help identify the cause of a connection issue. We recommend checking:
   - The [error logs](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/#error-log) for any database connection issues.
   - The [access logs](https://kinsta.com/docs/wordpress-hosting/wordpress-troubleshooting/view-server-logs/#access-log) for HTTP status codes, response sizes, and processing time that might point to what’s going wrong.
5. **Investigate Database Issues**:
   - Verify that your WordPress database is running and accessible. [Access your database](https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database-access/) to ensure the database server is running.
6. **Clear the site’s cache**: Sometimes, old cached data can cause connectivity issues. Clear your [server cache](https://kinsta.com/docs/wordpress-hosting/caching/site-caching/#clear-cache-in-mykinsta), [edge cache](https://kinsta.com/docs/wordpress-hosting/caching/edge-caching/#clear-edge-cache), and [CDN cache](https://kinsta.com/docs/wordpress-hosting/wordpress-cdn/kinsta-cdn/#how-to-clear-kinstas-cdn-cache).
7. **Verify Hosting and Domain Services**:
   - In [MyKinsta](https://my.kinsta.com/) ensure your plan is active and hasn’t been cancelled due to a [failed payment](https://kinsta.com/docs/billing/payments/unpaid-invoice/).
   - Make sure your domain registration is up to date. If the domain has expired, renew it with your registrar.

If none of the steps above resolve the issue, please [contact our Support Team](https://kinsta.com/docs/support/contact-support/).
