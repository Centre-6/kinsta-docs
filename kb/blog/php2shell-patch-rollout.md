---
url: "https://kinsta.com/blog/php2shell-patch-rollout/"
title: "Inside Kinsta\u2019s emergency PHP2Shell patch rollout"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: []
kinsta_last_updated: "2026-10-29T17:16:12"
change_signal: "2026-10-29T17:16:12"
fetched_at: "2026-11-11T13:03:02Z"
sha256: "9316db1afd0f99c85421b0aed793602502bd41c8e70c100c7ecd66bda176d593"
body_chars: 17814
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Inside Kinsta’s emergency PHP2Shell patch rollout

**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/php2shell-patch-rollout/
**Kinsta last updated:** 2026-10-29T17:16:12

## On this page

- [Preparing for PHP2Shell before the patches were available](#preparing-for-php2shell-before-the-patches-were-available)
- [How we activated Cloudflare’s emergency WAF rules](#how-we-activated-cloudflares-emergency-waf-rules)
  - [Adding temporary PHP configuration protections](#adding-temporary-php-configuration-protections)
- [Deploying PHP patches across hundreds of thousands of containers](#deploying-php-patches-across-hundreds-of-thousands-of-containers)
  - [Why older PHP versions needed additional fixes](#why-older-php-versions-needed-additional-fixes)
- [Monitoring attacks and checking for signs of compromise](#monitoring-attacks-and-checking-for-signs-of-compromise)
- [Resolving the incident and continuing verification](#resolving-the-incident-and-continuing-verification)
- [Responding to customers who took additional precautions](#responding-to-customers-who-took-additional-precautions)
- [What the response meant for Kinsta customers](#what-the-response-meant-for-kinsta-customers)

---

On October 21, 2026, attackers were already targeting websites with requests designed to exploit two critical PHP vulnerabilities known as [PHP2Shell](https://en.wikipedia.org/wiki/PHP2Shell). The official security patches weren’t available yet, but our engineering and security teams were already working to protect Kinsta-hosted websites.

The response involved several moving parts. Our team enabled emergency [Cloudflare firewall rules](https://kinsta.com/blog/cloudflare-settings-wordpress/), adjusted PHP configurations, and prepared to deploy patches across hundreds of thousands of containers as soon as they became available. At the same time, our [Support team](https://kinsta.com/kinsta-support/) was responding to an influx of questions from customers concerned about their websites.

By October 23, our Cloudflare protections had blocked more than 550,000 requests targeting the vulnerabilities. We had also deployed the necessary PHP security updates across our hosting platform and found no evidence of successful breaches.

![Event summary stats](https://kinsta.com/wp-content/uploads/2026/10/kinsta-event-summary.png)

Event summary stats

Here’s how the response unfolded, from the first signs of exploitation to the patch rollout and the work that followed.

## Preparing for PHP2Shell before the patches were available

On October 20, the PHP security team [announced an upcoming critical security release](https://www.php.net/archive/2026.php#2026-10-20-1), scheduled for the following day. The announcement warned of two vulnerabilities with a [CVSS 4.0](https://www.first.org/cvss/v4.0/) severity rating of 9.2 and encouraged PHP users to prepare to update their installations as soon as patches became available.

The vulnerabilities, later identified as [CVE-2026-109618](https://www.cve.org/CVERecord?id=CVE-2026-109618) and [CVE-2026-109619](https://www.cve.org/CVERecord?id=CVE-2026-109619), affect PHP’s internal memory handling and could, under certain conditions, allow attackers to execute code remotely without authentication.

The announcement was particularly significant for WordPress websites because PHP runs the application itself. Updating a WordPress plugin or theme couldn’t fix these vulnerabilities. The underlying PHP runtime needed security fixes.

For hosting providers like Kinsta, the initial challenge was protecting websites before the official patches became available. Our team began preparing for the release, but exploitation attempts were already appearing.

![A character from The IT Crowd typing rapidly at a computer. GIF via GIPHY](https://kinsta.com/wp-content/uploads/2026/10/engineers-at-work.gif)

Engineering team at work (Source: [GIPHY](https://giphy.com/gifs/13HgwGsXF0aiGY)).

According to [Laszlo Farkas](https://linkedin.com/in/thatlaszlo/), Director of Engineering at Kinsta, our team began observing requests targeting the vulnerabilities in the early hours of October 21. Engineers manually checked the targeted sites and continued monitoring activity for signs of a successful breach.

By then, we’d already taken steps to protect the websites on our platform.

## How we activated Cloudflare’s emergency WAF rules

Every website hosted on Kinsta sits behind Cloudflare, including production and [staging environments](https://kinsta.com/docs/wordpress-hosting/staging-environment/). This allows our engineering team to apply firewall protections across the hosting platform without requiring customers to configure rules for individual websites.

Ahead of the public PHP2Shell disclosure, [Cloudflare introduced emergency Web Application Firewall (WAF) rules](https://blog.cloudflare.com/php-vulnerabilities-waf-protection/) to detect exploitation attempts. Our engineering team closely monitored Cloudflare’s WAF changelog as new rules became available, reviewed them, and set their action to Block as soon as possible.

Because every Kinsta site already sits behind Cloudflare, we could apply these protections across our hosting platform, covering both production and staging environments without requiring customers to take any action.

That platform-wide protection mattered because PHP2Shell wasn’t a typical application-level vulnerability. The attacks targeted PHP itself, so WordPress security updates or plugin-level protection wouldn’t have addressed the underlying problem.

The WAF rules let us block known exploitation attempts while we prepared PHP patches. Cloudflare continued updating its protections as attackers changed their techniques. Its [technical report on PHP2Shell](https://blog.cloudflare.com/php-vulnerabilities-waf-protection/) describes how attackers modified their payloads to get around existing detections.

Cloudflare also introduced [full transaction detection](https://blog.cloudflare.com/full-transaction-waf/), which analyzes signals from both the HTTP request and the server’s response. This provides additional information for identifying suspicious requests and can prevent a matching response from reaching the requester.

Our engineers could see attack patterns changing as new rules became available.

By October 23, the Cloudflare protections covering Kinsta sites had blocked **more than 550,000 requests targeting PHP2Shell**.

This figure represents blocked requests associated with the vulnerabilities, not successful compromises or unique attackers. It reflects the suspicious traffic our firewall protections handled while the team worked on deploying the PHP fixes.

### Adding temporary PHP configuration protections

We didn’t rely on Cloudflare alone. While waiting for patched PHP packages, our engineering team also rolled out PHP configuration changes across our hosting environments to reduce exposure to known exploitation paths.

One change involved turning off PHP’s session upload progress feature using the session.upload_progress.enabled setting.

PHP’s [security advisory](https://www.php.net/archive/2026.php#2026-10-21-5) identifies this setting as a mitigation for certain exploitation paths. Turning it off helps block attacks that rely on PHP’s session upload progress handling, although it doesn’t address every possible way the vulnerabilities could be exploited.

The firewall rules and configuration changes provided additional protection while patches were unavailable or still being deployed. However, updating the PHP runtime remained necessary.

On October 23, the PHP team published an additional advisory recommending that session upload progress remain turned off until a subsequent bug-fix release. This reinforced the precaution our engineering team had already taken.

Our Cloudflare rules and local configuration protections remained in place throughout the patch rollout, regardless of whether an individual environment had received its updated PHP package.

## Deploying PHP patches across hundreds of thousands of containers

When the PHP development team released the security updates on October 21, our next challenge was getting those fixes deployed across the hosting infrastructure.

The official releases included PHP 8.2.35, 8.3.36, 8.4.27, and 8.5.12. However, Kinsta also supports older PHP versions, which required security fixes from third-party maintainers.

We worked with [Freexian](https://www.freexian.com/), our PHP package provider, to obtain patched packages for the PHP versions running across our platform, including older long-term-support versions.

The packages became available progressively, not all at once. As each build arrived in our package mirror, our engineering team validated it and began deployment without waiting for every PHP branch to be ready.

Here’s how the rollout progressed:

|  |  |
| --- | --- |
| **Date and time (UTC)** | **What happened** |
| **Oct 21, ~14:00–17:45** | PHP released the security patches. PHP 8.5.12 became available in our package mirror at 14:24, and deployment began at 15:54. By 17:45, tens of thousands of containers had been updated. |
| **Oct 21, 18:50–19:04** | PHP 8.3.36 became available, and deployment began alongside PHP 8.5. |
| **Oct 21, 21:17–22:28** | Patched packages for PHP 7.4, 8.0, and 8.1 became available, with further deployments beginning at 22:28. |
| **Oct 21–22, 23:25–01:37** | PHP 8.2 and 8.4 packages arrived at 23:25, with deployment starting at 01:37 on October 22. |
| **Oct 22, 04:31** | Only 1,888 containers, approximately 0.5% of the total, remained to be updated and required additional attention. |
| **Oct 22, 08:26** | We confirmed 100% protection coverage and marked the incident resolved. |

The ability to deploy changes at this scale was one of the most important parts of the response.

Farkas highlighted how quickly the team could deploy changes across the infrastructure:

“This is the part I’m most proud of. Once a change is validated and we know it won’t break anything, we can roll it out across the entire infrastructure within a couple of hours.”

That capability allowed our team to deploy patched PHP packages across hundreds of thousands of containers within hours.

We also didn’t have to coordinate PHP updates with individual customers. Kinsta manages PHP at the platform level, so once Engineering validated an updated package, we could deploy it across the affected environments without asking site owners to install updates themselves.

### Why older PHP versions needed additional fixes

The rollout also had to account for the difference between PHP’s officially supported branches and older versions maintained by third-party vendors.

The PHP project released security updates for PHP 8.2 through 8.5. Versions such as PHP 7.4, 8.0, and 8.1 were no longer receiving regular security releases directly from the PHP project, although long-term-support providers could supply backported fixes.

[Backporting](https://en.wikipedia.org/wiki/Backporting) allows maintainers to apply security fixes to an older software branch without requiring users to upgrade to a newer PHP version.

This meant we could deploy security updates for those older PHP environments as Freexian released patched packages.

It also explains why a PHP version number alone doesn’t always tell you whether a particular security fix has been applied. Vendor-maintained packages can include patched code without displaying the same version number as PHP’s official upstream release.

Throughout the rollout, we continued deploying updates while maintaining the additional firewall and configuration protections.

## Monitoring attacks and checking for signs of compromise

Deploying patches was only one part of the response. Our team also needed to determine whether any observed exploitation attempts succeeded.

When we first noticed activity targeting Kinsta-hosted websites in the early hours of October 21, our engineers manually investigated the sites involved.

They continued monitoring suspicious traffic and spot-checking hosting environments throughout the incident, looking for signs that attackers had successfully exploited the vulnerabilities.

Cloudflare security events helped us understand what was being targeted and how attack patterns changed as we released new rules. However, blocked-request counts alone couldn’t tell us whether any attacks had succeeded.

That’s why the manual checks mattered. Our team also stayed in close contact with [Patchstack](https://patchstack.com/), our [Vulnerability Protection](https://kinsta.com/vulnerability-protection/) partner, sharing information about the threats and attack patterns both teams observed. We also participated in discussions with other hosting providers to exchange information and good practices as the wider PHP community responded.

These efforts complemented our work with Cloudflare and Freexian. Cloudflare supplied protections against exploitation attempts, Freexian provided the patched PHP packages, and coordination with security partners helped our engineers understand how the threat was developing.

Throughout the incident, we found [no evidence of successful PHP2Shell-related breaches](https://kinsta.com/blog/php2shell-kinsta-wordpress/).

That finding is based on the monitoring and investigations carried out during the response. This doesn’t mean there were no attacks, as the firewall data shows. It means our checks did not identify signs of successful compromise.

## Resolving the incident and continuing verification

On October 22 at 08:26 UTC, we marked the PHP security incident resolved on our [public status page](https://status.kinsta.com/incidents/c0c6xl1ghpb2).

![PHP security incident resolved](https://kinsta.com/wp-content/uploads/2026/10/it-is-done.gif)

PHP security incident resolved (Source: [GIPHY](https://giphy.com/gifs/zCME2Cd20Czvy)).

By then, we had rolled out security updates across the platform, and all sites were protected by combined patching and mitigation measures.

The resolution didn’t mean we stopped checking. Our team continued verifying environments and monitoring protections after the public incident was closed.

This mattered during a rollout involving multiple PHP branches and hundreds of thousands of containers. At 04:31 UTC, around 0.5% of containers still required additional attention. Our engineers continued working through those remaining environments and verifying the results rather than treating the availability of a patched package as proof that every installation had been updated.

The Cloudflare rules and PHP configuration protections also remained in place during this verification work.

For customers, the PHP security updates required no manual patching or version switching.

## Responding to customers who took additional precautions

The response to PHP2Shell extended well beyond hosting providers. As news of the vulnerabilities spread, government agencies and other organizations worldwide began temporarily taking websites offline while preparing security updates.

In the Netherlands, the [National Cyber Security Centre](https://www.ncsc.nl/alerts/update-php-kwetsbaarheden-nog-steeds-reden-om-direct-te-patchen) took its own website offline as a precaution. Government websites in Germany, France, Belgium, and Finland were also temporarily suspended. In Japan, Prime Minister Sanae Takaichi [issued an urgent warning on X](https://www.japantimes.co.jp/business/2026/10/22/tech/japan-php-vulnerabilities/), urging website operators to apply the patches as soon as possible or temporarily suspend services if they couldn’t update immediately.

![Prime Minister Sanae Takaichi issued an urgent warning on X.](https://kinsta.com/wp-content/uploads/2026/10/takaichi-tweet-about-php.png)

Prime Minister Sanae Takaichi issued an urgent warning on X.

At Kinsta, we saw similar concerns among our customers. Our Support team received a significant increase in questions about PHP2Shell, and some customers began taking additional precautions to protect their websites.

These included using MyKinsta’s [environment suspension feature](https://kinsta.com/changelog/environment-suspension/) to take sites offline, enabling site-wide challenges through Bot Protection, or asking Support to block incoming traffic at the server level. Customers proactively suspended approximately 3,000 sites during the incident.

Given the severity of the vulnerabilities and the precautions being taken elsewhere, these decisions were understandable. However, Engineering did not recommend that customers take their Kinsta-hosted websites offline. We had already enabled Cloudflare’s emergency WAF rules across our hosting platform, so sites that remained online continued receiving those protections without becoming unavailable to visitors.

Our Support team began advising customers against unnecessary suspensions while Engineering continued deploying the PHP patches.

Once we rolled out the security updates, we reviewed the suspension actions taken during the incident to identify websites customers took offline specifically because of PHP2Shell.

Our team then reactivated those environments while leaving sites suspended for unrelated reasons untouched. This required distinguishing precautionary suspensions from other intentional suspensions, rather than simply restoring every environment that had been taken offline.

Beyond blocking attacks and deploying patches, our teams also had to help customers recover from precautions they had taken during the incident.

## What the response meant for Kinsta customers

PHP2Shell required coordination across Engineering, Support, and several external security and infrastructure partners. But the platform handled the patching itself.

Customers didn’t have to track each PHP release’s availability, determine which patched package their website needed, or install the updates themselves.

Farkas explained what the response ultimately meant for Kinsta customers:

“For me, the main message is that clients didn’t have to think about any of it: what to update, when, or how. They were just protected on our platform.”

The customer response during the incident also showed why communicating those protections mattered. Some customers took websites offline even though the emergency WAF rules were already active, and our teams subsequently worked to restore environments suspended because of the vulnerabilities.

Meanwhile, our engineering team deployed the PHP security updates across hundreds of thousands of containers without requiring customers to manage the changes.

For a record of the security updates and the incident’s resolution, see our [PHP security incident report](https://status.kinsta.com/incidents/c0c6xl1ghpb2).

For guidance on what the vulnerabilities mean for your website, see our companion article, [PHP2Shell: How Kinsta protected WordPress sites](https://kinsta.com/blog/php2shell-kinsta-wordpress/).
