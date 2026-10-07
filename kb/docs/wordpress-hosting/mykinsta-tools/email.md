---
url: "https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/email/"
title: "Email"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "mykinsta-tools"
section: ["WordPress Hosting", "Tools"]
kinsta_last_updated: "2024-09-17T10:25:37"
change_signal: "2024-09-17T10:25:37"
fetched_at: "2026-10-07T22:58:18Z"
sha256: "d39d06f98aa0b748d9540b424184ec09fd27e5a072d26f8eb0b193e7480840aa"
body_chars: 8367
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Email

**Section:** WordPress Hosting > Tools
**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/mykinsta-tools/email/
**Kinsta last updated:** 2024-09-17T10:25:37

## On this page

- [Email hosting](#email-hosting)
- [Recommended email providers](#recommended-email-providers)
- [MX records](#mx-records)
- [Sending emails from your website](#sending-emails-from-your-website)
  - [Transactional email limits](#transactional-email-limits)
  - [How does Kinsta handle violations?](#how-does-kinsta-handle-violations)
  - [How can I send non-transactional email or additional transactional email](#how-can-i-send-non-transactional-email-or-additional-transactional-email)

---

## Email hosting

We are committed to making Kinsta the best managed WordPress hosting platform in the industry. As part of that commitment, we don’t provide email as part of our hosting plans. For several reasons, we recommend [keeping your email and hosting separate](https://kinsta.com/blog/keep-email-and-hosting-separate/).

## Recommended email providers

Sending and receiving email is an integral part of doing business online, so we understand the importance of having a good email provider.

- We always recommend [Google Workspace](https://kinsta.com/blog/google-workspace/) (previously G Suite), which includes Gmail, one of the world’s best email services. It has a lot of features for a great price and allows you to use your own domain name. Many Kinsta clients utilize Google Workspace, and we even have a feature that lets you easily [add your Google MX records](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/google-mx-records/) with just a few clicks.
- [Microsoft Outlook](https://www.microsoft.com/en-us/microsoft-365/outlook/outlook-for-business), which is part of Microsoft 365, is another reliable email service that you can set up to use with your custom domain.
- [Zoho Mail](https://www.zoho.com/mail/) provides email hosting on a secure and encrypted email service.

## MX records

MX records are DNS records that direct your domain’s emails to your email provider. It’s important that these records are set up correctly, or you could experience an interruption in your email service.

If you’re using [Kinsta’s DNS](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/), you can add Gmail MX records with a few clicks in MyKinsta. If you’re using a different email provider, you can still add the necessary [MX records](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/#mx-record) to your domain in Kinsta DNS.

For other DNS providers, we recommend checking their specific documentation for more information on adding or editing MX records.

## Sending emails from your website

Your email provider will allow you to send and receive emails from and to your email address, but what about emails you need your site to send? Those are called transactional emails, which are those emails that are generated automatically by your WordPress website in response to some sort of user activity.

At Kinsta, all of our plans include support for transactional email on both Production and Staging sites. We send transactional emails via MailChannels, a secure and reliable email service. The address used for sending emails is called the ‘header from’ address, and you can configure it in WP Admin > **Settings** > **General** > **Administrator** **Email Address**. Transactional emails use the ‘envelope from’ address if this email address is not set. At Kinsta, we use containername@containername.kinstamailservice.com as the ‘envelope from’ address. Some email clients display both the ‘header from’ and ‘envelope from’ addresses. For instance, if your email is ‘wordpress@testsite.com‘ and your website is ‘mywebsite’, the email might show ‘wordpress@testsite.com via mywebsite.kinstamailservice.com’.

If you want to change the address used for sending emails but don’t want to change the administrator email address, you can use a plugin such as [WP Change Email Sender](https://wordpress.org/plugins/wp-change-email-sender/).

Kinsta’s MailChannels service includes DomainKeys Identified Mail (DKIM) support; this email authentication method uses a digital signature to let the receiver of an email know that the message was sent and authorized by the domain owner. This protects the domain against malicious emails sent from domains impersonating the kinstamailservice.com domain. If you use a custom domain, you must [set up DNS records](https://kinsta.com/docs/wordpress-hosting/wordpress-domains/dns/) for SPF and DMARC to enforce the email security policy.

Transactional email is email generated automatically by your WordPress website in response to some sort of user activity. For example, all of the following are transactional emails:

- New user registration notification emails.
- Password reset emails.
- Automatic order confirmations generated by WooCommerce or another ecommerce plugin.
- New comment moderation notifications sent to a website administrator.
- Comment reply notifications sent to users who have commented on your website.

This isn’t a complete list, but it illustrates the types of emails that are considered transactional.

What types of emails are not considered to be transactional? Transactional emails are sent automatically in response to user activity. Any email that does not meet that definition would not be considered a transactional email. The most common types of non-transactional emails are marketing emails, newsletters, and bulk product availability updates (sent to groups of users at the same time). Kinsta’s servers should not be used to send non-transactional email.

Some email providers now enforce stricter authentication requirements for bulk email senders, requiring Domain-based Message Authentication, Reporting, and Conformance (DMARC) alignment. Emails that don’t meet these requirements may be delayed or rejected. At Kinsta, outbound emails sent through the transactional email service do not currently support DMARC alignment. If you require DMARC compliance, we recommend configuring a third-party SMTP service. Many providers offer free plans. For setup guides, see:

- [How to Use a Free SMTP Server for WordPress Emails (Including Gmail SMTP Server)](https://kinsta.com/blog/free-smtp-server/)
- [How to Use the Gmail SMTP Server to Send Emails for Free](https://kinsta.com/blog/gmail-smtp-server/)

### Transactional email limits

While Kinsta does allow transactional email, we do have daily limits on the amount of transactional email allowed. For full details, please see our [Acceptable Use Policy](https://kinsta.com/legal/terms-service/#h-5-customer-obligations-and-acceptable-use).

The daily limits on transactional email are as follows:

- Single 35k, 65k, WP 2, Launch, Launch Plus, Build, and Expand plans may send up to 150 transactional emails per day.
- Single 125k, 315k, 500k, 750k, and WP 5, 10, 20, 40, and Scale and Lead plans may send up to 1,000 transactional emails per day.
- Single 1.25M, 1.9M, 2.5M, and 3.15M, Agency 20, 40, and 60, and WP 60, 80, 120, and 150 may send up to 3,000 transactional emails per day.

These limits are per plan and include all sites within the plan. For example, if you are on a WP 5 plan with 5 sites and you send 700 transactional emails from 1 site each day, you would only be able to send 300 transactional emails across the other 4 sites per day.

### How does Kinsta handle violations?

We have various monitoring tools that count outgoing emails and alert our Support team to violations of our transactional email policy. When a violation is discovered, our Support team will reach out to you to resolve the issue. In most cases, this means encouraging you to find an alternative means to send email. In the case of a significant violation of our policies regarding transactional email, email sending functionality may be temporarily disabled until the issue is resolved.

### How can I send non-transactional email or additional transactional email

If you need to send more transactional emails than what we allow or if you need to send non-transactional emails from your WordPress website, you have two options:

- For large volumes of transactional email, you can integrate a third-party transactional email service provider such as [SendGrid](https://kinsta.com/blog/sendgrid-wordpress/), [Mailgun](https://kinsta.com/blog/mailgun-wordpress/), or Mailjet.
- For non-transactional email, you can either integrate a third-party transactional email service provider (to send the email directly from your WordPress site) or switch to a third-party professional [email marketing platform such as Mailchimp](https://kinsta.com/blog/how-to-use-mailchimp/) or any other [Mailchimp alternative](https://kinsta.com/blog/mailchimp-alternatives/).

You can learn more about transactional email service providers and professional email marketing platforms by reading our blog post, [Email Marketing Software Recommendations](https://kinsta.com/blog/email-marketing-software/).
