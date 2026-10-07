---
url: "https://kinsta.com/docs/wordpress-hosting/wordpress-reference/technical-faq/"
title: "Reference - Technical FAQ"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "wordpress-reference"
section: []
kinsta_last_updated: "September 18, 2026"
sitemap_lastmod: "2026-09-18T09:56:30+00:00"
fetched_at: "2026-10-07T22:40:43Z"
sha256: "db8b4b8566efd8d84cb5d0aa01a8fa4acca22d9de536e600c958a6932513bdb3"
body_chars: 38732
extracted_with: "main article"
status: "live"
---

# Reference - Technical FAQ

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/wordpress-reference/technical-faq/
**Kinsta last updated:** September 18, 2026

## On this page

- [Evaluating Kinsta](#evaluating-kinsta)
  - [How much faster will my site be on Kinsta’s platform?](#how-much-faster-will-my-site-be-on-kinstas-platform)
  - [Can I try my site on Kinsta to see the performance differences compared to my current host?](#can-i-try-my-site-on-kinsta-to-see-the-performance-differences-compared-to-my-current-host)
  - [Why does Kinsta cost what it does?](#why-does-kinsta-cost-what-it-does)
  - [Does Kinsta offer high-availability hosting or load-balanced solutions (multi-location)?](#does-kinsta-offer-high-availability-hosting-or-load-balanced-solutions-multi-location)
  - [Are any countries blocked on Kinsta?](#are-any-countries-blocked-on-kinsta)
    - [What about China?](#what-about-china)
    - [What about Russia?](#what-about-russia)
- [Signing up & migrating](#signing-up-migrating)
  - [Do you offer domain registration?](#do-you-offer-domain-registration)
  - [How long does it take to migrate my site? Will my site be down during migration?](#how-long-does-it-take-to-migrate-my-site-will-my-site-be-down-during-migration)
  - [Can we see the performance benefits before pointing the DNS to Kinsta?](#can-we-see-the-performance-benefits-before-pointing-the-dns-to-kinsta)
    - [Option 1](#option-1)
    - [Option 2](#option-2)
  - [Why am I still seeing a message saying my domain isn’t pointed to Kinsta?](#why-am-i-still-seeing-a-message-saying-my-domain-isnt-pointed-to-kinsta)
- [Initial setup & configuration](#initial-setup-configuration)
  - [What is considered a WordPress install at Kinsta?](#what-is-considered-a-wordpress-install-at-kinsta)
  - [How does Kinsta count multisites?](#how-does-kinsta-count-multisites)
  - [Does Kinsta support multisite?](#does-kinsta-support-multisite)
  - [Does Kinsta have staging for multisite environments?](#does-kinsta-have-staging-for-multisite-environments)
  - [Can I use the SSL certificate I purchased somewhere else?](#can-i-use-the-ssl-certificate-i-purchased-somewhere-else)
  - [Do I need a server type, CSR code, and RSA key to activate SSL?](#do-i-need-a-server-type-csr-code-and-rsa-key-to-activate-ssl)
  - [Is a dedicated IP necessary for an SSL certificate?](#is-a-dedicated-ip-necessary-for-an-ssl-certificate)
  - [Do you provide SAML certificates?](#do-you-provide-saml-certificates)
  - [What are your platform settings? (PHP info and versions)?](#what-are-your-platform-settings-php-info-and-versions)
    - [PHP info](#php-info)
    - [Server](#server)
    - [Database](#database)
    - [TLS](#tls)
- [Building & developing](#building-developing)
  - [Can I add other PHP scripts?](#can-i-add-other-php-scripts)
  - [Can I install or use node/npm on my WordPress site?](#can-i-install-or-use-nodenpm-on-my-wordpress-site)
  - [Can I host HTML sites?](#can-i-host-html-sites)
  - [Does Kinsta have Git support?](#does-kinsta-have-git-support)
  - [Can I add custom rules to Nginx configurations?](#can-i-add-custom-rules-to-nginx-configurations)
  - [Is Kinsta compatible with Zapier?](#is-kinsta-compatible-with-zapier)
  - [Can I use MCP to automatically deploy my website in MyKinsta?](#can-i-use-mcp-to-automatically-deploy-my-website-in-mykinsta)
  - [On staging, can I only push the database live?](#on-staging-can-i-only-push-the-database-live)
  - [Can I have more than one database?](#can-i-have-more-than-one-database)
  - [What is the MySQL hostname of my site’s database?](#what-is-the-mysql-hostname-of-my-sites-database)
- [Running day-to-day](#running-day-to-day)
  - [Can I use a caching plugin?](#can-i-use-a-caching-plugin)
  - [Can you increase the default cache expiration time?](#can-you-increase-the-default-cache-expiration-time)
  - [How does Kinsta handle caching for WooCommerce and Easy Digital Downloads?](#how-does-kinsta-handle-caching-for-woocommerce-and-easy-digital-downloads)
  - [Can I whitelist an IP address?](#can-i-whitelist-an-ip-address)
  - [Do you have a list of banned plugins?](#do-you-have-a-list-of-banned-plugins)
  - [Does Kinsta block AI bots/crawlers?](#does-kinsta-block-ai-botscrawlers)
  - [Which ports are accessible on Kinsta?](#which-ports-are-accessible-on-kinsta)
  - [Do you support HTTP/2 (HTTP2)?](#do-you-support-http2-http2)
  - [Do my sites get a dedicated IP?](#do-my-sites-get-a-dedicated-ip)
  - [How often do you perform site monitoring/uptime checks?](#how-often-do-you-perform-site-monitoringuptime-checks)
  - [Will Kinsta host my emails?](#will-kinsta-host-my-emails)
- [Scaling & growing](#scaling-growing)
  - [Can I ask for additional storage if needed (or PHP threads, installs, etc.)?](#can-i-ask-for-additional-storage-if-needed-or-php-threads-installs-etc)
  - [What are PHP threads? How do I know how many I need?](#what-are-php-threads-how-do-i-know-how-many-i-need)
  - [How much CPU and RAM does each plan have?](#how-much-cpu-and-ram-does-each-plan-have)
  - [Does Kinsta offer reseller/white-label solutions?](#does-kinsta-offer-resellerwhite-label-solutions)
  - [Can I use a custom domain with Kinsta’s CDN?](#can-i-use-a-custom-domain-with-kinstas-cdn)
- [Trust, security & compliance](#trust-security-compliance)
  - [What is Kinsta’s Cloudflare integration?](#what-is-kinstas-cloudflare-integration)
  - [Is Kinsta SOC 2 Compliant?](#is-kinsta-soc-2-compliant)
  - [Is Kinsta PCI compliant?](#is-kinsta-pci-compliant)
  - [Does Kinsta provide HIPAA-compliant hosting?](#does-kinsta-provide-hipaa-compliant-hosting)
  - [Do you provide root access?](#do-you-provide-root-access)
- [Ongoing support & troubleshooting](#ongoing-support-troubleshooting)
  - [Can I run load tests?](#can-i-run-load-tests)
  - [What is your SLA?](#what-is-your-sla)
  - [Did we miss anything?](#did-we-miss-anything)

---

Below we’ve compiled all the **most common technical** **questions** about Kinsta in one place.

## Evaluating Kinsta

### How much faster will my site be on Kinsta’s platform?

Almost all sites we [migrate](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrating-to-kinsta/) from other managed WordPress hosting providers run faster at Kinsta.

You can view an example of this in our [case study with SkyRocketWP](https://kinsta.com/case-studies/skyrocketwp/). They came to Kinsta searching for a faster site for their clients, and they found that and much more. They ended up moving over 100 sites to Kinsta from [WP Engine](https://kinsta.com/wp-engine-alternative/) and saw, on average, a 49% decrease in page load times.

Another example is [WP Buffs](https://kinsta.com/case-studies/wp-buffs/), who saw their page load times cut in half. Just by switching to Kinsta and activating our built-in CDN, they also cut their bounce rate down by an average of 21%.

Kinsta utilizes leading cloud platforms to ensure lightning-fast network speeds. You can choose from any of our 30 global [data centers](https://kinsta.com/docs/service-information/data-center-locations/). Placing your site closer to your visitors helps decrease latency and [TTFB](https://kinsta.com/blog/ttfb/) while ensuring lightning-fast load times. Pair that with our HTTP/3 CDN, the latest versions of PHP, and our [isolated container technology](https://kinsta.com/blog/isolated-container-technology/); we’ve got the best performance stack in the industry.

Thanks to our high-performing machines, many of our clients experience up to a [200% boost in performance](https://kinsta.com/wordpress-hosting/)!

### Can I try my site on Kinsta to see the performance differences compared to my current host?

We don’t offer short-term trials, but here’s what we do have:

- **First month free:** We offer the first month free on our [Single 35k visits, Single 20GB bandwidth, WP 2, and Launch plans](https://kinsta.com/pricing/), allowing you to explore all of Kinsta’s features without any upfront payment. After the first month, regular plan pricing applies.
- **30-day money-back guarantee:** On all other plans (including add-ons), we offer a [30-day money-back guarantee](https://kinsta.com/docs/service-information/money-back-guarantee/). If you cancel your hosting account within the first 30 days, you’ll receive a full refund, making it a risk-free way to try Kinsta!
- **No long-term contracts:** You can cancel your subscription at any time without being locked into a long-term commitment.
- **Looking to try a custom plan:** [Contact our sales team](https://kinsta.com/contact-us/) to discuss what options are available for your site.

### Why does Kinsta cost what it does?

To answer this, we recommend you first read through our [Why Us](https://kinsta.com/why-us/) page, where we outline a lot of the differences between us and our competition.

If you’re coming from another managed WordPress host such as WP Engine, SiteGround, or Flywheel, check out these in-depth comparisons:

- [Kinsta vs WP Engine](https://kinsta.com/wp-engine-alternative/)
- [Kinsta vs SiteGround](https://kinsta.com/siteground-alternative/)
- [Kinsta vs Flywheel](https://kinsta.com/flywheel-hosting-alternative/)

Kinsta uses high‑performance, enterprise‑grade servers to host your WordPress sites. We currently offer 30 different locations.

Our [support](https://kinsta.com/docs/support/contact-support/) is different from anyone else. We don’t hire level 1 or level 2 support reps. Our team is comprised of only the best Linux engineers and WordPress developers. You get to chat with the same team members who support our Fortune 500 companies! This means fewer frustrations and less bouncing around, and ensures you get your problems resolved fast. We are available 24/7.

### Does Kinsta offer high-availability hosting or load-balanced solutions (multi-location)?

We do not offer high-availability (HA) hosting or run multiple load-balanced instances of each site. We do offer an [SLA-backed uptime guarantee](https://kinsta.com/docs/service-information/guaranteed-uptime/). Each site runs in a single Linux container, with the database running as a service within the site container. If you’d like to learn more, check out our article about our [Kinsta architecture](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/wordpress-infrastructure/).

### Are any countries blocked on Kinsta?

In some countries, Internet Service Providers (ISPs) restrict access to certain websites or online services. These restrictions may be due to government censorship, legal regulations, or business-related factors such as licensing agreements. Access is typically blocked by IP address or through DNS filtering, which prevents users from reaching specific content.

Certain countries or regions, including Cuba, Crimea, Iran, North Korea, Sudan, and Syria, are subject to U.S. trade restrictions, which may result in limited access to some Kinsta services. For the most up-to-date information, refer to the [U.S. Department of the Treasury’s website](https://www.treasury.gov/resource-center/sanctions/Programs/Pages/Programs.aspx).

If you are traveling in one of these restricted regions and need to access MyKinsta or update your website, you may be able to do so using a reputable VPN service, such as ExpressVPN or NordVPN.

#### What about China?

Websites hosted at Kinsta are generally accessible from within China, and many of our clients successfully target users there. However, because access depends on Chinese government controls, we cannot guarantee that your site will always be available.

You can [test your website to see if it’s accessible](https://kinsta.com/blog/great-firewall-of-china-cloud-platforms/) behind the Great Firewall of China.

#### What about Russia?

We are no longer accepting [new clients from Russia](https://kinsta.com/docs/service-information/new-accounts-from-russia/). This applies only to new clients; at this time, we are permitting existing clients to remain on the platform provided they comply with our Terms of Service. Also, we are not permitting the addition of new domain names that include the top-level domain for Russia (.ru) to our platform.

## Signing up & migrating

### Do you offer domain registration?

We don’t offer domain registration services. If you’re looking for a place [to register your domain](https://kinsta.com/blog/how-much-does-a-domain-name-cost/), check out places like [Cloudflare](https://www.cloudflare.com/en-gb/products/registrar/), [Name.com](https://www.name.com/), [Squarespace](https://domains.squarespace.com/), [NameCheap](https://www.namecheap.com/), [Hover](https://www.hover.com/), and [Enom](http://www.enom.com/). For more information about how to choose a domain registrar, refer to our blog post [How to Select the Best Domain Registrar (Our Recommendations)](https://kinsta.com/blog/best-domain-registrar/).

### How long does it take to migrate my site? Will my site be down during migration?

After signing up, you can request a free [hands-off migration](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrating-to-kinsta/) immediately from the MyKinsta dashboard. You can choose to migrate your site straight away, schedule the migration if your site is continuously updated or has special requirements, or purchase an [expedited migration](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrating-to-kinsta/#expedited-migrations) for $49 USD.

We will complete your migration as soon as possible, which could take up to 2 business days. We aim to complete expedited migrations within 8 hours. Our team will notify you of your migration status, and you can track the status in our MyKinsta dashboard.

Moving your site to Kinsta usually doesn’t incur any downtime. However, sites that are updated continuously, such as e-commerce (WooCommerce and Easy Digital Downloads), membership, and community sites, must be placed into [maintenance mode during migration](https://kinsta.com/docs/wordpress-hosting/wordpress-migrations/migrating-to-kinsta/#how-kinsta-migrates-dynamic-wordpress-sites) to prevent data loss.

Our team will notify you when they’re finished, along with how to preview your site before going live.

### Can we see the performance benefits before pointing the DNS to Kinsta?

You can test your site on Kinsta before changing the DNS using one of the following options:

#### Option 1

Create a [subdomain](https://kinsta.com/blog/wordpress-subdomain/), such as`test.yoursite.com`,  and point only the subdomain’s DNS to Kinsta. This allows you to compare the test site with your current live site.

To ensure the subdomain works correctly, you’ll need to perform a search and replace on your site. Start by [taking a backup](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/) of your site, then use Kinsta’s [search and replace tool](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/mykinsta-search-replace-tool/) to update it with your temporary subdomain.

Once testing is complete, you can [restore your site](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#restore-wordpress-backups) with just one click. Alternatively, if significant changes occurred on your live site during testing, you may prefer to perform a fresh migration after completing your tests.

#### Option 2

You could test locally from your location with Chrome DevTools by simply [editing your hosts file](https://kinsta.com/blog/edit-hosts-file/).

### Why am I still seeing a message saying my domain isn’t pointed to Kinsta?

If you have your own [Cloudflare account and pointed your domain](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-add-a-domain/) (allowing up to 24 hours for DNS to propagate), but you’re still seeing either of the following, check the **Page Rules** in your Cloudflare account:

- a banner or warning that your site isn’t pointed to Kinsta and is subject to service interruption.
- a status of “Confirming that you have pointed your domain to Kinsta.”

In your Cloudflare Page Rules, if the root domain is redirected to the WWW domain or vice versa, the domain that is being redirected cannot be verified in MyKinsta.

To resolve this issue, you’ll need to remove the redirect in Cloudflare Page Rules. This will allow the domain to be verified in MyKinsta. The redirect to the primary domain will now be handled at Kinsta.

## Initial setup & configuration

### What is considered a WordPress install at Kinsta?

Each Kinsta hosting plan allows one or more WordPress installs. **Each install equals 1 WordPress site**, which consists of its files (core files, theme files, plugin files) and a database.

The one exception to this is a multisite install, which we explain in the next question.

### How does Kinsta count multisites?

Multisite setups are considered one install each. For example, you could have one multisite with 10 subsites. This is still considered one install because all the subsites in the network share the same core WordPress files and database.

### Does Kinsta support multisite?

We support [WordPress multisite installations](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/multisite-network/) on our multiple-site plans. If you’re currently on our Single 35k visits plan or Single 20GB bandwidth plan, you’ll need to [upgrade](https://kinsta.com/pricing/) to a Single 65k visits plan, or Single 40GB bandwidth plan, or above to utilize multisite.

### Does Kinsta have staging for multisite environments?

Depending on how your [multisite is set up](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/multisite-network/), it may or may not work with our staging environment.

- If it’s a subdirectory multisite (example.com, example.com/subsite1, example.com/subsite2), it will work fine with our staging environment.
- If it’s a subdomain multisite (example.com, subsite1.example.com, subsite2.example.com), it will work fine as long as the subsites don’t require HTTPS. If the subsites do require HTTPS, you’ll have to bypass SSL errors on staging to access the subsites. This doesn’t impact functionality in any way.
- If it’s a domain-mapped multisite (loads different subsites at completely different domains, i.e., example.com, example1.com, example2.com), it won’t work without significant manual setup, which will have to be reversed if you push your staging database to your live site.
  - **Option 1:** Turn off or remove domain mapping and go back to the standard subdirectory/subdomain setup. Manually search and replace in the database to update the domains used for the subsites.
  - **Option 2:** Set up staging subdomains for each live domain, add all those to the staging site, and then run a search and replace in the database to update the domains used for the subsites.

### Can I use the SSL certificate I purchased somewhere else?

Yes, whether it’s a new SSL certificate, an [SSL you need to transfer](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/), or a certificate you’ll be regenerating at your SSL provider. For more details, check out our guide on [How to install an SSL certificate](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/) in MyKinsta.

We also offer free automatic Cloudflare SSL certificates (wildcard configurations are supported). So, unless there is a reason you need your own SSL certificate, it’s much quicker and easier to use our free SSL.

### Do I need a server type, CSR code, and RSA key to activate SSL?

It depends on the type of certificate you are using. We have [free SSL certificates](https://kinsta.com/blog/free-ssl-certificate/) available to all Kinsta customers, provided by our [Cloudflare integration](https://kinsta.com/cloudflare-integration/). These SSL certificates do not require a CSR or key to install on your WordPress site.

If you’re purchasing your own custom SSL certificate, you’ll need the server type, CSR code, and RSA key. For more details, please see our guide on [how to add an SSL certificate](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/wordpress-ssl-certificates/) and what to select for each value.

### Is a dedicated IP necessary for an SSL certificate?

When it pertains to SSL, a [dedicated IP](https://kinsta.com/blog/dedicated-ip-address/) is not necessary and has not been required since June 2003. The IPv4 pool is depleted and people saw that coming so they came up with a technique called [Server Name Indication](https://en.wikipedia.org/wiki/Server_Name_Indication) (SNI) that allows multiple certificates to be on the same IP. All modern browsers support it and it’s a technique that we and other hosting companies use every day for clients’ sites.

### Do you provide SAML certificates?

Kinsta does not provide SAML certificates; however, you can use [SAML Single Sign-On (SSO)](https://kinsta.com/docs/company-settings/wordpress-saml-sso/) to connect your company’s Identity Provider (IdP), such as Okta, OneLogin, or Google Workspace, directly to MyKinsta. This allows your team to sign in using their existing company credentials, eliminating the need to create or manage separate MyKinsta passwords.

### What are your platform settings? (PHP info and versions)?

Below are the settings, server software, and versions used on Kinsta’s hosting platform. As a Managed WordPress service, we have the optimal PHP settings configured to work best with WordPress sites. If you have specific PHP requirements, feel free to reach out to our [Support Team](https://kinsta.com/docs/support/contact-support/) to discuss your needs.

#### PHP info

Kinsta offers PHP 7.4, 8.0, 8.1, 8.2, 8.3, 8.4 and 8.5. These are the default settings for PHP:

| PHP setting | Value |
| --- | --- |
| memory_limit | 256M for the following plans:  - Single 750k visits and below - Single 500GB bandwidth and below - WP 40 and below - Launch - Launch Plus - Build - Expand - Scale - Lead   512MB for the following plans:   - Single 1.25M visits and above - Single 750GB bandwidth and above - WP 60 and above - Agency plans |
| upload_max_filesize post_max_size | 128M for the following plans:  - Single 125k visits and below - Single 65GB bandwidth and below - WP 2 - Launch - Launch Plus - Build - Expand   256M for the following plans:   - Single 315k visits and above - Single 125GB bandwidth and above - WP 5 and above - Scale - Lead   If you have a dedicated server, this can be increased to 500M. |
| max_input_vars | 10000 for the following plans:  - Single 125k visits and below - Single 65GB bandwidth and below - WP 2 - Launch - Launch Plus - Build - Expand   15000 for the following plans:   - Single 315k visits and above - Single 125GB bandwidth and above - WP 5 and above - Scale - Lead |
| max_execution_time max_input_time | 300 for the following plans:  - Single 750k visits and below - Single 500GB bandwidth and below - WP 40 and below - Launch - Launch Plus - Build - Expand - Scale - Lead   600 for the following plans:   - Single 1.25M visits and above - Single 750GB bandwidth and above - WP 60 and above - Agency plans |
| max_file_uploads | 20 for the following plans:  - Single 125k visits and below - Single 65GB bandwidth and below - WP 2 - Launch - Launch Plus - Build - Expand   50 for the following plans:   - Single 315k visits to Single 750k visits - Single 125GB to Single 500GB bandwidth - WP 5 to WP 40 - Scale - Lead   100 for the following plans:   - Single 1.25M visits and above - Single 750GB bandwidth and above - WP 60 and above - Agency plans |

Depending on your WordPress plan, you may be able to increase these values if required. Please contact our [Support Team](https://kinsta.com/docs/support/contact-support/) to find out what options are available to you.

#### Server

Kinsta utilizes [Nginx](https://kinsta.com/blog/what-is-nginx/) as a web server, currently running 1.15.9 or higher.

#### Database

Kinsta utilizes MariaDB 11.4 or higher. Both the database and web server run on `localhost`.

#### TLS

All Kinsta servers and our CDN support [TLS 1.3](https://kinsta.com/blog/tls-1-3/) or higher. Make sure to read our [TLS vs SSL guide](https://kinsta.com/blog/tls-vs-ssl/).

## Building & developing

### Can I add other PHP scripts?

With [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/), you can also set up a simple non-WordPress PHP script alongside your WordPress site, but we do not provide [support for non-WordPress scripts and applications](https://kinsta.com/docs/support/scope-of-support/managed-wordpress-scope-of-support/) in Managed WordPress Hosting.

[Sevalla’s Application Hosting](https://sevalla.com/application-hosting/) allows you to host pretty much any application (not just PHP).

### Can I install or use node/npm on my WordPress site?

If you’re on a Single 1.25M visits plan, Single 750GB bandwidth plan, or above, or a WP 60 plan or above, you can [contact the Kinsta Support team](https://kinsta.com/docs/support/contact-support/) to install node/nodejs/npm on our server for your site.

### Can I host HTML sites?

You can host HTML sites at Kinsta. With [Managed WordPress Hosting](https://kinsta.com/wordpress-hosting/), if the default WordPress **index.php** isn’t found in the /public directory, the server will automatically load **index.html**. If a different page is used for the website’s homepage, you’ll need to [open a new chat](https://kinsta.com/docs/support/contact-support/) with our Support team, and they can add a special rule on the server for this to work properly. Note: We don’t provide any additional support for non-WordPress sites for Managed WordPress Hosting.

[Sevalla’s Application Hosting](https://sevalla.com/application-hosting/) allows you to host pretty much any application. HTML sites can also be hosted with [Sevalla’s Static Site Hosting](https://sevalla.com/static-site-hosting/).

### Does Kinsta have Git support?

We have the Git client available at Kinsta, so you can SSH in and pull your own Git repo down from Github, Gitlab, Bitbucket, or any other third party. However, we don’t yet have the feature released yet where you can just `git push kinsta my_site` and it automatically gets deployed.

Check out [how to use Git at Kinsta](https://kinsta.com/docs/wordpress-hosting/site-management/git/).

### Can I add custom rules to Nginx configurations?

Yes, however, as this requires root access, you must contact [Kinsta’s support team](https://kinsta.com/contact-us/) to add custom rules to the Nginx configuration.

### Is Kinsta compatible with Zapier?

Yes, WordPress sites hosted on Kinsta are compatible with Zapier automations via the **[xmlrpc.php](https://kinsta.com/blog/xmlrpc-php/)** endpoint. By default, we disable all access to **xmlrpc.php** because it’s a common attack vector for hackers and other malicious actors. If you’re experiencing issues with integrating Zapier with WordPress on Kinsta, please open a new chat with our Support team, and we can assist you in allowing your Zapier integration.

### Can I use MCP to automatically deploy my website in MyKinsta?

MyKinsta doesn’t currently support Model Context Protocol (MCP) or one-click Git push deployments for WordPress sites.

If you’re using an AI coding assistant that supports MCP, you can still use it to generate or modify code, but you’ll need to deploy those changes using a supported deployment workflow.

We recommend using a CI/CD solution such as [GitHub Actions](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-github-cicd/), [GitLab CI/CD](https://kinsta.com/docs/wordpress-hosting/site-management/gitlab-ci-cd/), or [Bitbucket Pipelines](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-bitbucket-pipelines/)  to automatically deploy code changes whenever commits are pushed to a repository.

You can also use third-party deployment tools such as [DeployHQ](https://www.deployhq.com/), [Buddy](https://buddy.works/guides/wordpress), [WP Pusher](https://wppusher.com/), or [Deployer for Git](https://wordpress.org/plugins/deployer-for-git/) to automate deployments from Git repositories. Availability and supported features vary by tool, so refer to each provider’s documentation for setup instructions.

### On staging, can I only push the database live?

Our staging environment includes [Selective Push](https://kinsta.com/docs/wordpress-hosting/staging-environment/#push-staging-to-live-with-selective-push), which provides you with more granular control over what to push live. You can choose to push only the files, specific files or folders, only the database, specific database tables, or both the files and the database from your staging environment to your live site.

### Can I have more than one database?

We only allow **one database per WordPress site**.

With [Sevalla’s Database Hosting](https://sevalla.com/database-hosting/), you can host as many databases as you want.

### What is the MySQL hostname of my site’s database?

All you usually need to know is that your database hostname is `localhost` at Kinsta. But if you’d like to learn more about the topic or need to connect remotely to a database, we have a dedicated article showing you how to [connect directly to your site’s database.](https://kinsta.com/docs/wordpress-hosting/database-management/wordpress-database-access/)

## Running day-to-day

### Can I use a caching plugin?

We don’t allow caching plugins because we provide **five types of cache**, which are all automatically done at the software or server level. This is controlled by our [Kinsta MU plugin](https://kinsta.com/docs/wordpress-hosting/kinsta-mu-plugin/), which is installed by default on all WordPress sites.

Read more about [how Kinsta handles caching](https://kinsta.com/blog/wordpress-cache/).

**Exception:**  [We do allow WP Rocket](https://kinsta.com/blog/wp-rocket/), version 3.0 and higher. Their caching functionality is automatically disabled when running on Kinsta, so you can use our built-in caching but still utilize the other optimization features WP Rocket offers.

### Can you increase the default cache expiration time?

Our page cache is set to expire every 1 hour by default. If you want to adjust this to be longer, in [MyKinsta](https://my.kinsta.com/) go to **Sites** > ***sitename*** > **Caching** > **Server Caching** > **Change cache expiration**.

In the modal/pop-up that appears, select your desired cache expiration and click the **Change expiration** button. For sites that don’t change often, it can be beneficial in terms of performance to have a longer cache expiration.

### How does Kinsta handle caching for WooCommerce and Easy Digital Downloads?

We have server-level caching rules already in place for popular ecommerce solutions such as WooCommerce and Easy Digital Downloads. By default, certain pages that should never be cached, such as cart, my-account, and checkout, are excluded from caching. Users automatically bypass the cache when the `woocommerce_items_in_cart` or `edd_items_in_cart` cookies are detected to ensure a smooth and in-sync checkout process.

Some plugins may require additional configuration to work properly. If you’re seeing any issues with caching, such as cart contents being cached and viewable by other visitors, additional Nginx rules may need to be added to your site’s Nginx configuration.

Because hosting environments can vary in setup/configuration, there are a variety of ways that plugins, themes, and sites can have incompatibilities or require certain configurations. It can be difficult for developers of complex plugins and engineers of complex hosting environments to account for every possibility, setup, or configuration.

If there’s an additional section of your ecommerce site that needs to bypass the cache or additional rules that need to be added to your Nginx configuration for compatibility, you can always [contact our Support team](https://kinsta.com/docs/support/contact-support/).

### Can I whitelist an IP address?

Yes. In [Kinsta’s bot protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) settings, you can add an IP address to [Exceptions](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/#exceptions) and set it to **Allow**.

IP addresses in the allow list are exempt from bot protection rules, meaning they will not be challenged or blocked by bot protection features such as verification checks or rate-based restrictions.

However, these exceptions apply only to bot protection. They do not override Kinsta’s core security systems. If a request is identified as malicious or violates platform-level security rules, it may still be blocked to protect your site and the Kinsta platform.

In short, allowing an IP address ensures trusted IPs bypass bot protection, while maintaining essential security safeguards.

### Do you have a list of banned plugins?

Yes, we don’t allow certain third-party plugins because they are known to hurt performance, not work on our platform, or are simply not needed, as we provide a better and easier way to do the same thing in MyKinsta. Check out the [full list of banned plugins](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-banned-incompatible-plugins/).

### Does Kinsta block AI bots/crawlers?

Kinsta automatically excludes traffic from well-known and clearly identifiable bots from plan usage calculations. User agents that confidently identify themselves as bots or crawlers are filtered from analytics and do not count toward your usage.

Some automated or suspicious traffic, however, cannot always be definitively identified as either automated or human. This type of traffic may still count toward usage if the requests successfully reach your site.

To help manage this, [Kinsta’s Bot Protection](https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/wordpress-tools-bot-protection/) can identify and classify potentially automated or abusive traffic based on traffic behavior. You can then choose how this traffic is handled, including challenging or blocking suspicious requests before they reach your site.

If you notice large volumes of suspicious or likely automated traffic, enabling stricter Bot Protection settings can help reduce the number of automated requests reaching your site and minimize their impact on performance and resource usage.

### Which ports are accessible on Kinsta?

While Cloudflare may show multiple open ports during a security scan, Kinsta only allows incoming web traffic through ports 80 (HTTP) and 443 (HTTPS) via our firewall. These are the standard ports used for serving websites securely.

If you’re using SSH or SFTP, Kinsta assigns randomly generated external ports for secure connections. These additional ports are only accessible for those specific services and are not open to general web traffic.

### Do you support HTTP/2 (HTTP2)?

Yes, we do. Our infrastructure supports HTTP/2 for all of our clients. If you would like to learn more, we’ve published a very [detailed guide about HTTP/2.](https://kinsta.com/learn/what-is-http2/)

### Do my sites get a dedicated IP?

No, we don’t provide dedicated IP addresses. A shared IP is quite common nowadays with most WordPress hosting providers, as for many configurations, there is no need for a dedicated IP address. Since we offer a free Cloudflare integration for all sites hosted on Kinsta, our shared IPs are actually Cloudflare IPs.

Our allocated Cloudflare IPs are only used for sites on our infrastructure. This means if your site is hosted on Kinsta, you won’t share an IP address with sites hosted outside Kinsta — some of which may contain adult or spam content. Check out our in-depth blog post explaining the [difference between dedicated IPs and shared IPs](https://kinsta.com/blog/dedicated-ip-address/).

If you’re looking for a dedicated IP because you need to add a single IP to an allowlist for a third-party service (maybe a payment processor like PayPal or similar), you’ll want to use your site’s [external IP](https://kinsta.com/docs/wordpress-hosting/site-management/ip-addresses/) for that. This is the IP address that other servers see when your site connects to that other server.

### How often do you perform site monitoring/uptime checks?

Your WordPress site is checked every 3 minutes. If something needs attention, our engineers will begin investigating immediately. If [WordPress site monitoring notifications](https://kinsta.com/docs/user-settings/notifications/) are enabled in MyKinsta, we’ll also send you an email for any site errors, DNS errors, SSL errors, or expired domains.

### Will Kinsta host my emails?

We don’t include email in our plans since we fully commit all of our resources to WordPress hosting. However, we do recommend Google Workspace or a couple of other email providers.

Check out our blog post on all the [downfalls of using your hosting provider for email](https://kinsta.com/blog/email-marketing-software/).

## Scaling & growing

### Can I ask for additional storage if needed (or PHP threads, installs, etc.)?

It depends on what you need. If you need additional disk space, we have a [disk space add-on](https://kinsta.com/docs/billing/wordpress-hosting-plans/overages/#disk-space-add-on) that allows you to **increase the storage space of your hosting plan** with a few simple clicks. Need an extra 80 GB? No problem.

If you want to increase a site’s PHP memory pool, threads, or memory per thread, you can purchase the [PHP performance add-on](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/) within **Sites** > ***sitename*** > **Info** > **PHP performance** > **Change**.

Another affordable and effective alternative is to offload large files to a separate storage service like Amazon S3 or Google Cloud Storage. This is a great way to reduce the storage needed for your site and keep your hosting costs down.

- [Offload Media to Amazon S3](https://kinsta.com/blog/wordpress-amazon-s3/)
- [Offload Media to Google Cloud Storage](https://kinsta.com/blog/wordpress-google-cloud-storage/)

If you need additional WordPress installs, you can purchase the [WordPress site add-on](https://kinsta.com/docs/wordpress-hosting/wordpress-add-ons/#wordpress-site-add-on). This allows you to increase the number of sites without upgrading your plan.

If you need a plan that doesn’t fit any of our standard offerings, you can [open a new ticket](https://kinsta.com/docs/support/contact-support/) with our Account Management team, and they can go over the amount of disk space, PHP threads, and the number of installs allocated to each plan. They can also help you determine if a [custom plan](https://kinsta.com/docs/billing/wordpress-hosting-plans/#custom-wordpress-hosting-plan) would be a good fit for your site(s).

### What are PHP threads? How do I know how many I need?

PHP threads determine how many simultaneous uncached requests your site can handle at a time. Each uncached request is handled by a PHP thread.

Each of our hosting plans includes a certain number of PHP threads by default. The number included in each plan is based on resource usage needed for typical sites. In general, sites with lots of static content — articles, static pages, blog posts — don’t need many PHP threads.

The number of PHP threads needed may vary per site due to third-party plugins, queries, dynamic content, and the number of cached vs uncached responses. In Kinsta, you can increase the number of threads or the memory per thread within [PHP performance](https://kinsta.com/docs/wordpress-hosting/php/wordpress-php-performance/).

### How much CPU and RAM does each plan have?

Kinsta utilizes leading cloud platforms in multiple data centers. On our standard plans, each live site container has access to 12 CPUs and 8 GB of RAM by default, and each staging environment has access to 1 CPU and 8 GB of RAM.

### Does Kinsta offer reseller/white-label solutions?

We do not offer your typical reseller plan at the moment. However, many agencies use Kinsta and sell hosting to their clients. Our [multi-user permissions](https://kinsta.com/docs/company-settings/user-management/) make this easy. We also do have [white label options](https://kinsta.com/docs/wordpress-hosting/kinsta-mu-plugin/#white-label-and-customize-the-kinsta-mu-plugin) on our Kinsta MU plugin which is by default installed on all WordPress sites.

You can also earn passive income by referring clients to Kinsta by joining our [affiliate program](https://kinsta.com/affiliates/).

### Can I use a custom domain with Kinsta’s CDN?

Thanks to Kinsta’s CDN, your site’s cached assets are served from your primary domain. It is not currently possible to utilize an alternate domain or subdomain to serve CDN assets.

## Trust, security & compliance

### What is Kinsta’s Cloudflare integration?

All sites on Kinsta are protected by our free Cloudflare integration. Cloudflare is a leading provider of web security and performance services. With our Cloudflare integration, sites hosted on Kinsta are protected by an intelligent firewall that also includes free DDoS protection. For more details, check out our detailed article on our [Cloudflare integration](https://kinsta.com/blog/cloudflare-integration/).

### Is Kinsta SOC 2 Compliant?

Yes! Kinsta is SOC-compliant. You can request a copy of our SOC 2 Type II report on our [Trust Report](https://trust.kinsta.com/) page. For more information about our SOC 2 compliance, including frequently asked questions, see our [SOC 2 documentation](https://kinsta.com/docs/service-information/soc-2/).

### Is Kinsta PCI compliant?

We do not guarantee PCI compliance, and we are not able to audit your site to verify that you’re doing things right, either. However, that doesn’t mean you can’t be PCI compliant when hosting your website with us. In fact, we have many clients who have worked with third-party auditors to pass PCI compliance scans. In many of these cases, we’ve had to make a few minor adjustments upon request, but these clients have been able to pass the audit just fine after a little fine-tuning on both our end and theirs.

Check out additional details regarding [PCI-compliant hosting at Kinsta](https://kinsta.com/blog/pci-compliant-hosting/).

### Does Kinsta provide HIPAA-compliant hosting?

Kinsta does not offer a HIPAA-compliant hosting product, and we do not enter into Business Associate Agreements (BAAs) with our customers. You should not store or transmit protected health information (PHI) on Kinsta, and you are solely responsible for determining whether your use of Kinsta is subject to HIPAA or similar healthcare data regulations.

That said, security is foundational to our platform. Kinsta maintains a SOC 2 Type 2 report, prepared by an independent auditor, that includes an examination of our controls against the HIPAA Security Rule safeguards. You can request our SOC 2 Type 2 report on our [Trust Report](https://trust.kinsta.com/) page.

If you have a healthcare-related use case, [contact our sales team](https://kinsta.com/contact-us/) to discuss your requirements.

### Do you provide root access?

No, we don’t provide root access. Full root access is a double-edged sword: while it allows you to literally do whatever you want with a server (including edit system-critical files), we cannot provide support for something that we’re not familiar with or didn’t set up.

## Ongoing support & troubleshooting

### Can I run load tests?

Load testing is prohibited on the MyKinsta platform. For more information about what testing is allowed, please refer to our [Terms of Service](https://kinsta.com/legal/terms-service/#h-5-acceptable-use-policy-and-protection-of-the-services). You can run a Website speed test, which typically measures the total load time of a page, including [MySQL](https://kinsta.com/blog/what-is-mysql/) + PHP response times. Tools like [Pingdom](https://kinsta.com/blog/pingdom-speed-test/) or [GTmetrix](https://kinsta.com/blog/gtmetrix-speed-test/) are commonly used for this type of test.

### What is your SLA?

Check out our complete [Service Level Agreement (SLA)](https://kinsta.com/legal/service-level-agreement/).

### Did we miss anything?

If you have any other technical questions we’ve perhaps missed, make sure to leave them in the feedback form below. 👇 Or you can always open a chat with our Support team.
