---
url: "https://kinsta.com/blog/ai-agent-guardrails/"
title: "Why AI agents need guardrails instead of unlimited access"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "Bot Traffic", "Why AI agents need guardrails instead of unlimited access"]
kinsta_last_updated: "2026-09-15T19:21:31+00:00"
sitemap_lastmod: "2026-09-15T19:21:31"
fetched_at: "2026-10-07T22:40:37Z"
sha256: "621661e0d64bce2e9664159bfaa44137b7ab5d954f2688fd1b8ac012d9d985cb"
body_chars: 16686
extracted_with: "main article"
status: "live"
---

# Why AI agents need guardrails instead of unlimited access

**Section:** Resource Center > Blog > Bot Traffic > Why AI agents need guardrails instead of unlimited access
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/ai-agent-guardrails/
**Kinsta last updated:** 2026-09-15T19:21:31+00:00

## On this page

- [Why access to production is a risk for an AI agent](#why-access-to-production-is-a-risk-for-an-ai-agent)
- [How staging can turn an AI agent’s error into a minor event](#how-staging-can-turn-an-ai-agents-error-into-a-minor-event)
- [Using the principle of least privilege before an AI agent hits WordPress](#using-the-principle-of-least-privilege-before-an-ai-agent-hits-wordpress)
- [Why backups should be a big part of your agentic workflow](#why-backups-should-be-a-big-part-of-your-agentic-workflow)
- [How to check the scope of AI agentic workflow within MyKinsta](#how-to-check-the-scope-of-ai-agentic-workflow-within-mykinsta)
  - [Confirm that staging is your default path](#confirm-that-staging-is-your-default-path)
  - [Review what can access your API keys](#review-what-can-access-your-api-keys)
  - [Check that agentic workflows have a restore point](#check-that-agentic-workflows-have-a-restore-point)
  - [Use the activity log to check for rogue actions](#use-the-activity-log-to-check-for-rogue-actions)
- [Guardrails make AI autonomy safe to deploy](#guardrails-make-ai-autonomy-safe-to-deploy)

---

Author
:   [Jeremy Holcombe](https://kinsta.com/blog/author/jeremyholcombe/ "Posts by Jeremy Holcombe")

Published
:   October 6, 2026

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![AI agents need guardrails](https://kinsta.com/wp-content/uploads/2026/09/ai-agents-need-guardrails-not-unlimited-access-1024x512.png)

Deleting your entire production database and backups is not something a human will do often, but it is possible for an AI agent running under strict instructions. A credential mismatch within the codebase is not something an agent will check.

Without guardrails, it will carry on regardless. This is what happened to [PocketOS](https://www.business-standard.com/technology/tech-news/claude-ai-agent-opus-46-deletes-pocketos-database-9-secs-jer-crane-126042800659_1.html) in April 2026, but it wasn’t the AI agent’s fault. Instead, it shows that the infrastructure and control around agentic workflows need human oversight.

This post looks at employing those agentic guardrails using Kinsta’s functionality. The Kinsta API and MyKinsta dashboard both play a part. As AI agents take on more work, they need strict checks where a human approves destructive steps.

## Why access to production is a risk for an AI agent

When it comes to failures, a typical script and an AI agent falter in different ways. With a script, you see an error on screen. Even if you encounter a White Screen of Death, that’s still an error on display. This is because you build error handling into a script under all but the rarest of cases.

However, the nature of AI is to comply with a task. This means an AI agent can report success but throw silent errors. This [still happens](https://github.com/anthropics/claude-code/issues/32281) because a model wants to help you succeed. This causes [fabricated or synthesized results](https://yurukusa.github.io/cc-safe-setup/opus-48-fabricated-tool-results.html).

For WordPress, an agent that crawls changelogs, API responses, scraped content, or anything else as part of its task set is open to exposure. In April 2026, [Essential Plugin](https://techcrunch.com/2026/04/14/someone-planted-backdoors-in-dozens-of-wordpress-plugins-used-in-thousands-of-websites/) released a backdoor that sent malicious code to over 400,000 sites before being shut down. However, this doesn’t provide a fix for compromised sites.

An AI agent that applies plugin updates automatically as part of its workflow doesn’t know the difference between legitimate and compromised updates. Unless you include a staging review, this sort of attack can happen to you too. Opsin Labs’ 2026 report on agentic adoption highlights that 60% of AI agents have more permissions than necessary. It’s the same permissions issue for human WordPress teams, now showing up for agents.

## How staging can turn an AI agent’s error into a minor event

A staging review as part of your workflow instructions gives you a way to challenge specific aspects of agentic deployment. For example, if a developer pushes a planned change, they know what those changes are.

In contrast, an AI agent running through instructions as part of a multi-step task is simply trying to complete the task for you. Combining this with potential information synthesis means a review checkpoint is a necessity.

If you compare the WordPress supply chain attack with an agent making production-level updates, both make changes without review. [Kinsta provides free staging](https://kinsta.com/docs/wordpress-hosting/staging-environment/) for all sites to help combat this problem:

![The MyKinsta dashboard for a single site showing a drop-down menu to either select an existing environment or create a new one.](https://kinsta.com/wp-content/uploads/2026/09/environment-select.png)

Selecting a staging environment within MyKinsta.

You also have the option for [premium staging environments](https://kinsta.com/changelog/premium-staging-environments/) if you need to work with a spec closer to production.

With this in place, the changes an AI agent makes don’t move from staging until you choose to push the environment live:

![The MyKinsta Selective Push drop-down menu, showing an option to push an environment to staging.](https://kinsta.com/wp-content/uploads/2026/09/selective-push.png)

Pushing a live environment to staging within MyKinsta.

This gives you granular options to push the database, files, or both together. MyKinsta also creates an automatic backup of the target environment first. The same logic applies to Kinsta’s Automatic Updates too.

A practical way to include staging within your workflow is to clone production to staging before you run an agentic task. Then, run the AI agent within staging and review the result. Finally, selective push lets you approve the changes and send them to production.

## Using the principle of least privilege before an AI agent hits WordPress

Agentic access and permissions work on the same principles as humans. The [Principle of Least Privilege](https://owasp.org/www-community/controls/Least_Privilege_Principle) is a fundamental concept of security:

[QUOTE]An agent or human should only hold the minimum level of permissions and access it needs to carry out a task and nothing more.[/QUOTE]

Kinsta’s [existing roles and permissions](https://kinsta.com/docs/company-settings/user-management/) settings are applicable to AI agents as well as humans:

- **Company Administrator**, which provides full control across your entire Kinsta account. Almost no AI agent needs this role.
- **Company Developer** roles let your agent manage all your sites and DNS.
- **Site Administrator** lets you assign full site access to an agent.
- **Site Developer** is the most appropriate for agentic workflows as it only allows staging-level access.

Assigning roles also means you need to assign API keys to your agents. A [Kinsta API key](https://kinsta.com/docs/kinsta-api/) inherits the access level of the role that generates it. This is a good way to automatically limit the access an AI agent has.

A solid, secure workflow here is to generate API keys on a per-agent or per-workflow basis. You do this through the **Company Settings** > **API Keys** screen within MyKinsta:

![The API Keys screen within MyKinsta showing a drop-down menu for setting an expiry time for an individual API key.](https://kinsta.com/wp-content/uploads/2026/09/create-api-key.png)

Setting an expiry time for a new API key within MyKinsta.

Setting an expiry time gives you a chance to review access. If your workflow changes, you now have a natural way to reassess your access and permissions.

## Why backups should be a big part of your agentic workflow

Because the reasons for failures differ between human and agentic workflows, so does the need for backups. For example, a human pause is natural when carrying out a destructive task. However, because of the need to comply with instructions, an AI agent won’t pause to think or double-check. The fix is to build in a hard requirement.

It means a backup is only a safety net when it sits outside of what could delete it. For instance, the [PocketOS incident](https://www.theguardian.com/technology/2026/apr/29/claude-ai-deletes-firm-database) is as much an architectural issue related to backups as it is a permissions issue. Storing volume-level backups on the volume itself is resolvable in code.

However, only having an [old backup available](https://thenewstack.io/ai-agents-credential-crisis/) to restore your database isn’t possible with Kinsta:

- **Daily automatic backups** give you a baseline regardless of what an agent does.
- **System-generated backups** run before a selective push or update, even when triggered by an agent.
- **Manual backups** let you [create your own restore points](https://kinsta.com/docs/wordpress-hosting/wordpress-backups-and-disaster-recovery/wordpress-backups/#restore-wordpress-backups) (with tags) when you need them.

The Kinsta API lets you build in checks before an AI agent carries out a destructive step:

```
const KINSTA_API_URL = 'https://api.kinsta.com/v2';
const headers = {
  'Content-Type': 'application/json',
  Authorization: `Bearer ${process.env.KINSTA_API_KEY}`
};

const createBackup = async (envId, tag) => {
const resp = await fetch(`${KINSTA_API_URL}/sites/environments/${envId}/manual-backups`, {
method: 'POST',
headers,
body: JSON.stringify({ tag })
});
return resp.json();
};

const pollOperation = async (operationId, intervalMs = 5000, maxAttempts = 12) => {
for (let i = 0; i < maxAttempts; i++) {
const resp = await fetch(`${KINSTA_API_URL}/operations/${operationId}`, { method: 'GET', headers });
const data = await resp.json();
if (data.status === 200) return data;
if (data.status >= 400) throw new Error(`Operation failed: ${data.message}`);
await new Promise(r => setTimeout(r, intervalMs));
}
throw new Error('Operation timed out');
};

const findBackupByTag = async (envId, tag) => {
const resp = await fetch(`${KINSTA_API_URL}/sites/environments/${envId}/backups`, { method: 'GET', headers });
const data = await resp.json();
return data.environment.backups.find(b => b.note === tag) || null;
};

const runAgentTask = async (envId, agentTask) => {
const tag = `pre-agent-action-${Date.now()}`;
const backup = await createBackup(envId, tag);
if (!backup.operation_id) throw new Error(`Backup request failed: ${JSON.stringify(backup)}`);

await pollOperation(backup.operation_id);
const verified = await findBackupByTag(envId, tag);
if (!verified) throw new Error('Backup not found after completion');

return agentTask();
};
```

Here, you send a `POST` request to create a manual backup for an environment. Then, the agent can poll the operation ID and confirm the backup. With a confirmation, the agent can proceed to the destructive step. Building in a step to create a backup when modifying production is as important and non-negotiable as any other security setting.

## How to check the scope of AI agentic workflow within MyKinsta

Using MyKinsta’s information lets you run an audit on what your agents can access. The programmatic option using the [Kinsta API](https://api-docs.kinsta.com/pages/introduction) is near instant if you build it into your instructions. However, the MyKinsta interface gives you a way to run a ten-minute, human-led audit.

### Confirm that staging is your default path

Upfront spot checks give you human eyes on some key pieces of information. There are two areas to check:

- Instances of production environment IDs.
- Kinsta’s Automatic Updates run at the right points in your workflow.

To find your production and staging IDs through MyKinsta, open a site dashboard and look at the URL:

```
https://my.kinsta.com/sites/details/{site_id}/{environment_id}?idCompany={company_id}
```

Use the environment drop-down menu to switch between the environments you want to check. Next, open any config or script that handles your automation and search for the environment ID. If any production IDs show, replace them with your staging ID.

To confirm your Automatic Updates settings, navigate to the **Plugins and themes** screen. Here, click **Change** next to the **Automatic Updates** section:

![The Change Automatic Updates settings screen within MyKinsta showing three options, including Kinsta's premium solution.](https://kinsta.com/wp-content/uploads/2026/09/kinsta-auto-updates.png)

Choosing Kinsta’s premium Automatic Updates option gives you access to rollbacks and visual regression.

[Kinsta’s solution](https://kinsta.com/docs/wordpress-hosting/wordpress-plugins-themes/wordpress-plugins-themes-automatic-updates/) lets you use visual regressions and rollbacks when finding an error. If any of the before-and-after screenshots of your site’s pages look different, Kinsta rolls back to a ‘known’ version. You can adjust the sensitivity of visual regression testing and work with dynamic content too.

### Review what can access your API keys

A straightforward check is to audit your API keys. Depending on the size of your team and the projects you run, there may be many expired or otherwise redundant keys to clear out.

To do this, head to **Company Settings** > **API keys** within MyKinsta. The list doesn’t tell you the access level of each key from the dashboard. It means having clear naming conventions and records is vital.

You want to check three elements:

- Which role a key was generated under.
- The expiry date, which is viewable in the list.
- Whether the key is still in use for an active workflow.

For any API key not active but still within the expiry date, you can click the **Revoke** button to remove it. For expired keys, the button reads **Delete**. Regardless, the action is the same.

You can filter the **User activity** screen in MyKinsta to see [associated activity](https://kinsta.com/changelog/kinsta-api-nov-21-2025/) that uses a specific API key:

![The MyKinsta User activity screen showing a drop-down menu of API keys and associated actions for individual users.](https://kinsta.com/wp-content/uploads/2026/09/user-activity.png)

The User activity screen lets you filter on per-user based on the API key access.

For programmatic checking, there are endpoints for fetching the [activity logs](https://api-docs.kinsta.com/api-reference/activity-logs/get-list-of-company-activity-logs) and [API keys](https://api-docs.kinsta.com/api-reference/api-keys/get-list-of-company-api-keys) for a company.

However, in order to see the access level information for an API key, there needs to be one action for it. So if a key has never been used, you can safely delete the key.

### Check that agentic workflows have a restore point

For your backups, open a site and look at the **Manual** tab within **Backups**:

![The Backups screen within MyKinsta showing manual backups complete with notes and tags.](https://kinsta.com/wp-content/uploads/2026/09/manual-backup.png)

The Backups screen shows you the Notes column, which you use to tag backups with the right workflow.

Here, look for missing or incorrect notes. Then, consider whether any agentic workflow calls the API and [makes a manual backup](https://api-docs.kinsta.com/api-reference/backups/add-a-manual-backup-to-an-environment). If so, make sure you check the operation status before the agent runs a backup.

Also, an agent may trigger backups more than you expect. If your five manual backup slots are full, look at the creation date. This helps you decide if you need to optimize a wasteful backup process.

### Use the activity log to check for rogue actions

Back on the **User activity** screen, confirm that every action traces back to a named user or an API key. You can view an activity log at the company or site level.

For any entry you want to query, click it and use the **Ask Support** button. This lets you message support to ask for further details about the nature of an entry.

![The User activity screen showing one action with the Ask Support dialog box open, ready to query the contents.](https://kinsta.com/wp-content/uploads/2026/09/ask-support.png)

You can ask Kinsta’s support team about user activity directly from the log screens in MyKinsta.

There’s also a programmatic way to [access user activity details](https://kinsta.com/docs/company-settings/activity-log/), which gives you another way to build checks into your workflow. However, human checks here can catch issues an AI agent may miss.

## Guardrails make AI autonomy safe to deploy

MyKinsta’s functionality isn’t specifically for AI security. Staging, user activity logs, automated backups, and permissions all stop agentic workflows from causing catastrophic issues. You can also control the workflow at every step, either through the MyKinsta dashboard or the Kinsta API.

Making your AI agents more trustworthy means giving them the right scope and building guardrails into the process. Human intervention is still necessary, even for the most automated of operations.

Choosing Kinsta’s [high-performance WordPress hosting](https://kinsta.com/wordpress-hosting/) gives you the tools to ensure safe, secure agentic access. [For agencies](https://kinsta.com/wordpress-hosting/agencies/), Kinsta gives the same best-in-class security and support across your entire client base.

Jeremy Holcombe
[Kinsta](https://kinsta.com/)

Senior Editor at Kinsta, WordPress Web Developer, and Content Writer. Outside of all things WordPress, I enjoy the beach, golf, and movies. I also have tall people problems.

- [LinkedIn](https://www.linkedin.com/in/jeremyholcombe/)
