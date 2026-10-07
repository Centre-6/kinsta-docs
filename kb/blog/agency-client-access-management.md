---
url: "https://kinsta.com/blog/agency-client-access-management/"
title: "Why client access management is the quiet scaling killer for agencies"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: []
kinsta_last_updated: "2026-06-10T18:32:28"
change_signal: "2026-06-10T18:32:28"
fetched_at: "2026-10-07T22:58:25Z"
sha256: "141238f40401b77eb2605a40797889d41c9f9a66086edb97288fb732859eb488"
body_chars: 16447
extracted_with: "wp-rest:content.rendered"
status: "live"
---

# Why client access management is the quiet scaling killer for agencies

**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/agency-client-access-management/
**Kinsta last updated:** 2026-06-10T18:32:28

## On this page

- [How ‘access sprawl’ develops quietly inside a growing agency](#how-access-sprawl-develops-quietly-inside-a-growing-agency)
- [The two permission systems every agency needs to understand](#the-two-permission-systems-every-agency-needs-to-understand)
  - [MyKinsta roles and what they actually control](#mykinsta-roles-and-what-they-actually-control)
  - [WordPress dashboard roles and where they fit](#wordpress-dashboard-roles-and-where-they-fit)
- [What agencies typically get wrong when involving clients](#what-agencies-typically-get-wrong-when-involving-clients)
  - [“We’ll manage access manually”](#well-manage-access-manually)
  - [“Clients don’t need that much access”](#clients-dont-need-that-much-access)
  - [“This hasn’t caused issues yet”](#this-hasnt-caused-issues-yet)
- [How to structure access on Kinsta as your agency scales](#how-to-structure-access-on-kinsta-as-your-agency-scales)
  - [Handing off a site to a client’s own account](#handing-off-a-site-to-a-clients-own-account)
  - [Running a quarterly access review](#running-a-quarterly-access-review)
- [Your client access structure is really a relationship infrastructure](#your-client-access-structure-is-really-a-relationship-infrastructure)

---

When an agency is small, managing user access is more a matter of habit than a process. You share Admin credentials because it’s faster, [grant company-level access](https://kinsta.com/docs/company-settings/user-management/#add-users-from-the-company-users-page) in [MyKinsta](https://kinsta.com/mykinsta/) because setting up a site-level user takes a few extra minutes, and leave a contractor in the system because removing them isn’t urgent.

The problem is that these shortcuts become part of the template for every project that follows. By the time a client asks who changed a setting, or a contractor you parted ways with last quarter turns out to still have access to a live site, that pattern has reproduced across your entire portfolio.

Client access management is the kind of problem that scales alongside your agency without drawing attention to itself, until it surfaces at the worst possible moment.

Kinsta’s [permission model](https://kinsta.com/docs/company-settings/user-management/#mykinsta-user-roles-and-permissions-chart) gives you the infrastructure to make access decisions as deliberate as any other part of your agency workflow.

## How ‘access sprawl’ develops quietly inside a growing agency

Access sprawl typically starts with a decision that made sense once and got repeated without review. The first instance is usually low-stakes, such as sharing admin credentials with a client during a project review, because setting up a separate account would take ten minutes you don’t have.

The second is similar: you give a contractor [Company Developer](https://kinsta.com/docs/company-settings/user-management/) access in MyKinsta because creating a site-level user feels like extra work at the end of an onboarding call. Both choices feel proportionate, but neither was made with scale in mind.

However, each of these sets a precedent for the next project. Within a year, an agency managing twenty client sites can have a dozen users with access levels that were never deliberate:

- Ex-employees who were never removed upon leaving.
- Contractors holding permissions for projects that ended months ago.
- Clients with company-level visibility into data that was never intended for them.

## The two permission systems every agency needs to understand

A Kinsta setup involves two separate permission systems. You control access to the hosting environment within MyKinsta and set what users can do inside the application through WordPress.

However, because they operate independently, conflating the two is where most access mistakes begin.

### MyKinsta roles and what they actually control

MyKinsta has [six roles across two levels](https://kinsta.com/blog/manage-users-hosting-account/), and understanding the boundary between them is what makes the system work in your favor.

![A close-up of the Invite users panel showing an email address entered and the Company Developer options chosen.](https://kinsta.com/wp-content/uploads/2026/06/invite-developer.png)

The Invite users panel within MyKinsta showing setting up a Company Developer role.

There are four company-level roles:

- **Company Owner.** There’s one per account, and it’s the only role that can cancel a plan or transfer company ownership. It operates identically to Company Administrator in day-to-day use and belongs with the agency principal.
- **Company Administrator.** This gives complete control of all company data and full access to every site, including migration requests. It includes billing visibility and the ability to change plans, so it’s for senior team members you trust with those responsibilities.
- **Company Developer.** The role lets you manage all sites and DNS across the account, along with site-level users. Company Developers can view the list of company users (including email addresses and roles), but cannot modify company-level access or see billing details. This is the right default for most internal developers.
- **Company Billing.** This is for giving access to billing details only, such as invoices, company names, and addresses. Use this for finance contacts who need invoice visibility and nothing else.

The two site-level roles are where client and contractor access belongs:

- **Site Administrator.** You get complete access to a specific site and all its environments, including DNS management for that site. Assignees cannot remove the site from the company account, submit migration requests, or create [premium staging environments](https://kinsta.com/docs/wordpress-hosting/staging-environment/).
- **Site Developer**. This gives access to staging environments only. They cannot touch the live environment, push staging to production, or see company-level data of any kind.

The protective logic of site-level roles is the foundation of a sound client access policy. In short, exposure for a user role is scoped to one site. In the case of a Site Developer, to staging only.

### WordPress dashboard roles and where they fit

[WordPress user roles](https://kinsta.com/docs/wordpress-hosting/site-management/wordpress-users/) govern what users can do inside WordPress and are entirely independent of MyKinsta. So, a user can hold a WordPress role without any MyKinsta access, and vice versa.

A common mismatch is granting a client Site Administrator access in MyKinsta and WordPress Administrator access on the same site simultaneously. The result is a client who can adjust server-level settings in one system while installing plugins, managing users, and changing themes in the other.

Matching the WordPress role to the actual task is important:

- **A client managing content** needs Editor access in WordPress and no MyKinsta access.
- **A developer building on staging** needs Site Developer access in MyKinsta and potentially Administrator access in WordPress on the staging environment. You should review this before the go-live.
- **A client taking over their site post-handoff** needs Site Administrator access in MyKinsta and a WordPress Administrator role, if their capability and the project scope justify both.

The same principle applies in both systems: grant the minimum access the role requires. Granting more because it’s easier to explain creates exposure that’s invisible until it produces a problem.

## What agencies typically get wrong when involving clients

Most agencies don’t arrive at a broken access setup through negligence, but through reasonable beliefs in isolation. However, each belief has a failure mode that isn’t apparent until circumstances produce it.

### “We’ll manage access manually”

Manual access management works when a portfolio is small and the team is stable, but breaks when neither of those things are true.

For example, a client who receives Company Developer access by mistake because an invitation was sent at the company level instead of the site level can view the email addresses and roles of every user in your account. Likewise, a contractor given WordPress Administrator access on a project site can export the entire user table, including any client contacts stored there.

While neither amount to a dramatic security incident, they are exposures that a written access policy would have prevented. A simple table that maps project roles to MyKinsta roles and WordPress roles is enough:

|  |  |  |  |
| --- | --- | --- | --- |
| **Project role** | **MyKinsta role** | **WordPress role** | **Notes** |
| **Agency owner or principal** | Company Owner | Administrator | One per account. The only role that can cancel a plan or transfer company ownership |
| **Senior developer or account lead** | Company Administrator or Company Developer | Administrator | Use Company Administrator if billing visibility is appropriate; Company Developer if it isn’t |
| **Project contractor** | Site Developer | Administrator (staging only) | Staging access only. Cannot push to live or delete staging environments |
| **Client — content management** | None | Editor | No hosting visibility needed for content tasks |
| **Client — post-handoff ownership** | Site Administrator | Administrator | Only if their capability and project scope justify both |

When the decision is already made, the onboarding step becomes execution rather than a judgment call under time pressure.

### “Clients don’t need that much access”

Restricting client access feels like risk management, although in practice it’s not the same. For instance, a client who needs to update a staff bio, swap a hero image, or publish a blog post doesn’t need server access.

If they don’t have a WordPress role that lets them do those things, each task becomes a ticket in your project management tool. Giving appropriate access is a decision that removes recurring demand from your team. For example, a client with Editor access in WordPress will handle their own content without any visibility into the hosting environment.

[Organic Media Group](https://kinsta.com/case-studies/organic-media-group/), a digital marketing agency managing client portfolios on Kinsta, describes the experience from the team side:

> I can throw somebody new in there, and they can manage a couple of these accounts with no problems.

The same logic applies client side. The MyKinsta interface is accessible to users without a technical background, and the role structure keeps their exposure scoped to what they own.

### “This hasn’t caused issues yet”

Access incidents typically either surface immediately or appear months later when the circumstances align. So, a contractor who still has staging access to a project that ended six months ago isn’t a problem until they make a change. The longer the gap between a permission being granted and the next review, the harder it becomes to reconstruct what happened and when.

![The MyKinsta dashboard showing a list of active and expired API keys, along with the options to create new ones.](https://kinsta.com/wp-content/uploads/2026/06/api-keys.png)

The MyKinsta dashboard showing a list of active and expired API keys.

Also, manual offboarding can consistently miss certain access issues. For example, removing a user from MyKinsta does not automatically revoke API keys they may have created or reset [SSH/SFTP credentials](https://kinsta.com/blog/sftp-ssh-features/).

Both require a separate step. To revoke API keys, go to **Company settings** > **API keys**, identify any keys the departing user created, and delete them. To reset [SSH/SFTP credentials](https://kinsta.com/blog/sftp-ssh-features/), go to the site level, navigate to Info, and regenerate the credentials. Neither happens automatically when a user is removed.

![The User Activity screen within MyKinsta showing a number of entries based on actions taken by the user.](https://kinsta.com/wp-content/uploads/2026/06/user-activity.png)

The User Activity screen within MyKinsta showing a number of entries of user actions.

The [activity log](https://kinsta.com/docs/company-settings/activity-log/) helps here, but only if you’re reviewing it. Company Administrators and Company Developers can filter the log by user or site, and each entry is clickable to show the action in detail. When offboarding a user, filter the log by their name before removing them. This gives you a record of their last actions and confirms whether any changes need to be reviewed or reversed.

## How to structure access on Kinsta as your agency scales

First, look at your role structure. Start from **Company settings > Users > Invite users** in MyKinsta. From the invitation modal, you can invite up to ten users at once by entering their email addresses separated by commas, then choose whether to grant **Company** or **Site** access.

![The MyKinsta Invite users modal showing an email address field, a role selector set to Company Developer, and a Send invite button.](https://kinsta.com/wp-content/uploads/2026/06/invite-users.png)

The MyKinsta Invite users modal within MyKinsta.

Here’s how to assign roles across a standard agency team and client relationship:

- An agency owner or principal should get the **Company Owner** role.
- Senior developers and account leads could get either the **Company Administrator** if billing visibility is appropriate for their role, or **Company Developer** if it isn’t. Company Developer is the right default for most internal technical staff.
- For project contractors, assign the **Site Developer** role on the relevant staging environment only.
- If you have clients with content management responsibilities, assign **Editor** access in WordPress. They need no MyKinsta access unless the project scope explicitly includes self-managed hosting.

For site-specific roles (such as Site Developer), choose **Site** rather than **Company** in the invitation modal. From here, you search for the site and set the correct role.

As a reminder, assign the **Site Administrator** role in MyKinsta and a WordPress **Administrator** role for clients taking ownership post-handoff, if their capability warrants it.

One setting worth enabling across your account is [two-factor authentication](https://kinsta.com/changelog/two-factor-authentication/) (2FA). Kinsta requires 2FA for all users and supports both email and authenticator app verification. You can see which method each user has enabled under **Company settings** > **Users** > **2FA**. For an agency managing multiple client sites, ensuring every user on your account has 2FA active is a baseline control that sits alongside your role structure.

### Handing off a site to a client’s own account

When a project completes, and the client is taking full ownership, Kinsta lets you [transfer the site](https://kinsta.com/docs/company-settings/transfer-ownership/) directly to their own Kinsta account rather than leaving it in yours with reconfigured permissions.

To initiate the transfer, navigate to **Sites** in MyKinsta, click the three-dot (kebab) menu on the site row, then select **Transfer site** from the drop-down menu.

![The MyKinsta Sites list with the three-dot kebab menu open on a site row, showing Transfer site as one of the available options.](https://kinsta.com/wp-content/uploads/2026/06/transfer-site.png)

The MyKinsta Sites list showing the Transfer site option for a specific site.

In the dialog box, enter the email address or Company ID of the destination account. You can also select any DNS domains to transfer alongside the site and optionally recommend a Kinsta plan for the client. Click **Transfer site** to send the request.

Once the client logs into Kinsta, the site appears as an **Incoming transfer** in their **Sites** list. They accept by clicking the site name, then **Commit transfer > Accept transfer**.

### Running a quarterly access review

Scheduling a quarterly review is a quick way to close the gaps that day-to-day offboarding misses. First, go to **Company settings > Users** in MyKinsta and pull the full user list. You can filter by site to see who has access to each client property.

Next, cross-reference the list against your active project records. Anyone whose project has ended and who hasn’t been removed is a gap. You remove users by clicking the trash icon on their row, or select multiple users and click **Remove**.

As a reminder, remove any associated API keys and verify that any SSH/SFTP credentials have been rotated for any site with recent personnel changes.

## Your client access structure is really a relationship infrastructure

Access management is an ongoing concern and can have security consequences. The way you structure permissions signals to clients whether a site is isolated from others and if your agency operates with a process or a habit.

The next step is to put the access policy in writing using the role mapping table above, and run a first quarterly review on your existing portfolio to surface what has already accumulated. From there, the access structure you build becomes visible to clients in the right ways: a contractor who can only access staging, a client whose content tools don’t expose your hosting environment, and a clean offboarding when a project ends. That’s what it looks like when an agency operates with a process rather than a habit.

For agencies managing client sites at scale, Kinsta’s [Agency Partner Program](https://kinsta.com/agency-partner-program/) gives you dedicated support, co-selling resources, and tooling designed around the way agencies hosting on Kinsta work.
