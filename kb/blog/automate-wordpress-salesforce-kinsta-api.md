---
url: "https://kinsta.com/blog/automate-wordpress-salesforce-kinsta-api/"
title: "How to automate WordPress go-live from Salesforce using the Kinsta API"
tier: "blog"
product: "blog"
product_label: "Blog (secondary - never outranks docs)"
subsection:
section: ["Resource Center", "Blog", "API", "How to automate WordPress go-live from Salesforce using the Kinsta API"]
kinsta_last_updated: "2026-06-19T10:48:58+00:00"
sitemap_lastmod: "2026-06-19T10:48:58"
fetched_at: "2026-10-07T22:42:26Z"
sha256: "2114113f8ff3c0c974b5f66f6c255dd480e3dffed45276cfe222d59552d06ea6"
body_chars: 19649
extracted_with: "main article"
status: "live"
---

# How to automate WordPress go-live from Salesforce using the Kinsta API

**Section:** Resource Center > Blog > API > How to automate WordPress go-live from Salesforce using the Kinsta API
**Product:** Blog (secondary - never outranks docs)
**Source:** https://kinsta.com/blog/automate-wordpress-salesforce-kinsta-api/
**Kinsta last updated:** 2026-06-19T10:48:58+00:00

## On this page

- [What you need before you start](#what-you-need-before-you-start)
- [How to automate WordPress go-live from Salesforce using the Kinsta API](#how-to-automate-wordpress-go-live-from-salesforce-using-the-kinsta-api)
  - [1. Set up a Named Credential](#1-set-up-a-named-credential)
    - [Setting user permissions](#setting-user-permissions)
  - [2. Create a Record-Triggered Flow on the Opportunity object](#2-create-a-record-triggered-flow-on-the-opportunity-object)
  - [3. Configure the async path, and add an HTTP Callout action](#3-configure-the-async-path-and-add-an-http-callout-action)
  - [4. Setting a request body within Flow Builder](#4-setting-a-request-body-within-flow-builder)
  - [5. Build the Node.js middleware](#5-build-the-nodejs-middleware)
  - [6. Create a manual backup of the staging environment](#6-create-a-manual-backup-of-the-staging-environment)
  - [7. Push staging to production and monitor the completion](#7-push-staging-to-production-and-monitor-the-completion)
- [Automating your agency’s deployment workflow with Salesforce and Kinsta](#automating-your-agencys-deployment-workflow-with-salesforce-and-kinsta)

---

Author
:   [Joel Olawanle](https://kinsta.com/blog/author/joelolawanle/ "Posts by Joel Olawanle")

Updated
:   June 19, 2026

Preferred source
:   [![](https://kinsta.com/wp-content/themes/kinsta/images/icon-google.svg)Add as a preferred source on Google](https://google.com/preferences/source?q=kinsta.com)

![](https://kinsta.com/wp-content/uploads/2026/04/how-to-automate-wordpress-go-live-from-salesforce-using-the-kinsta-api-1024x512.png)

When a deal closes in Salesforce, the site it represents still depends on a separate set of manual steps to go live. A [developer](https://kinsta.com/blog/types-of-developers/) has to find the right client site in [MyKinsta](https://kinsta.com/mykinsta/), create a backup, and [push staging to production](https://kinsta.com/docs/wordpress-hosting/staging-environment/), all at the right moment.

Using the [Kinsta API](https://kinsta.com/docs/kinsta-api/), you can connect these two parts of the workflow so that deal approval automatically triggers the launch. Instead of relying on someone to carry out each step, the process runs as soon as the opportunity reaches the target stage.

It’s a straightforward setup: fire a batch of MyKinsta tasks when a [Salesforce Opportunity](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunity.htm) updates, and remove the need for manual intervention after deployment. Meanwhile, your client gets a faster path from approval to a live site, without waiting on handoffs between teams.

## What you need before you start

To follow this tutorial, you need a [Kinsta account](https://kinsta.com/signup/wp/) with a WordPress site that has both a [staging environment](https://kinsta.com/docs/wordpress-hosting/staging-environment/) and a live environment, a Salesforce account with access to [Flow Builder](https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/build-a-record-triggered-flow), and [Node.js](https://kinsta.com/blog/what-is-node-js/) installed locally for the middleware.

To authenticate with the Kinsta API, navigate to **Your name** > **Company settings** > **API Keys** in [MyKinsta](https://my.kinsta.com/) and click **Create API Key**.

![The MyKinsta dashboard showing the API Keys screen that includes two existing API keys, along with a button to create a new one.](https://kinsta.com/wp-content/uploads/2026/04/api-keys-2.png)

The MyKinsta dashboard showing the API Keys screen.

Give the key a name, set an expiry, and click **Generate**. The key only displays once, so copy it before you close the modal. Store it in a `.env` file at the project root alongside your **Company ID**, which you find under **Company settings** > **Billing Details**:

```
KINSTA_API_KEY=your_api_key_here
KINSTA_COMPANY_ID=your_company_id_here
```

You also need a custom text field on the Salesforce Opportunity object to store the Kinsta site ID for each client project. Head to **Setup** > **Object Manager**, then to **Opportunity** > **Fields and Relationships**.

![The Fields and Relationship within Salesforce Setup options pages.](https://kinsta.com/wp-content/uploads/2026/04/new-fields-relationships.png)

The Fields and Relationship within Salesforce Setup options pages.

Here, add a **Field Label**, and Salesforce generates a **Field Name** that you need to note down. Set the **Length** to **255** and save your changes.

The site ID is a UUID that Kinsta assigns at creation. It appears in the MyKinsta URL when you open a site, or you can retrieve it once by calling `GET /sites` with your API key in place:

```
https://my.kinsta.com/sites/details/hyut4927-d324-4044-b794-67ap0rbf20bj/…
```

You use the site ID in a custom field on each Opportunity to trigger the entire workflow.

## How to automate WordPress go-live from Salesforce using the Kinsta API

On the Salesforce side, a [Record-Triggered Flow](https://admin.salesforce.com/blog/2023/what-is-a-record-triggered-flow) monitors the Opportunity stage and fires an HTTP callout the moment the stage transitions.

The Node.js middleware receives the site ID, calls the Kinsta API to back up the staging environment, waits for that operation to complete, then pushes staging to production. Most of the work takes place in Salesforce to ensure the right permissions and access are set.

### 1. Set up a Named Credential

Salesforce has an efficient way to store API keys. It involves an External Credential, which holds the actual secret, and a [Named Credential](https://developer.salesforce.com/docs/platform/named-credentials/guide/get-started.html), which defines the endpoint URL and connects to it.

Within Salesforce, open the **Setup** screen from the home menu:

![Setup icon alongside a number of other toolbar options.](https://kinsta.com/wp-content/uploads/2026/04/setup-icon.png)

Setup icon alongside a number of other toolbar options.

Here, search for **Named Credentials**, open the **External Credentials** tab, and click **New**. Give it a name and a label, then set the authentication protocol to **Custom**. This lets you define a Bearer token header rather than using a managed OAuth flow.

After you save it, scroll to **Principals** and click **New**. Give the principal a name, such as `KinstaKey,` and enter the Kinsta API key as its value.

![Fields for a name, label, and authentication protocol.](https://kinsta.com/wp-content/uploads/2026/04/new-credential.png)

Fields for a name, label, and authentication protocol.

Now, add a **Custom Header** with the name `Authorization` and a value referencing the principal, so that every outbound callout includes the API key as a Bearer token.

![The New Named Credential screen showing a name, label, and URL field along with authentication options.](https://kinsta.com/wp-content/uploads/2026/04/new-named.png)

The New Named Credential screen showing different fields along with auth options.

With the External Credential saved, go to the **Named Credentials** tab, click **New**, set the URL to your middleware endpoint, fill in the required fields, and select the **External Credential** under the **Authentication** section.

#### Setting user permissions

You also need to enable a [Permission Set](https://help.salesforce.com/s/articleView?id=platform.perm_sets_overview.htm&language=en_US&type=5) for the External Credential’s Principal, which grants your user profile the necessary credentials to call the Kinsta API. To do this, head to **Setup** > **Permission Sets** and click **New**.

Here, give it a name and save it, then reopen the Permission Set and click to edit the **External Credential Principal Access** screen. You should move the External Credential principal to the enabled list:

![The External Credential Principal Access screen showing an item moved from one disabled list to the enabled list.](https://kinsta.com/wp-content/uploads/2026/04/edit-principal-access.png)

The External Credential Principal Access screen showing a disabled and enabled list.

Finally, save your changes, head back to the Permission Set, and click **Manage Assignments** within the top toolbar:

![The Manage Assignments link in the Salesforce toolbar.](https://kinsta.com/wp-content/uploads/2026/04/manage-assignments-link.png)

The Manage Assignments link in the Salesforce toolbar.

On this screen, use **Add Assignment** to connect to your user profile and enable access to the Kinsta API.

### 2. Create a Record-Triggered Flow on the Opportunity object

Next, open the Salesforce App Launcher, then search for **Flows** on the screen you come to, click **New**, and select **Record-Triggered Flow**.

![Record-Triggered Flow option alongside other choices to build automations.](https://kinsta.com/wp-content/uploads/2026/04/record-trigger-flow.png)

Record-Triggered Flow option alongside other choices to build automations.

Once the Flow Builder opens, set the following options:

- Choose **Opportunity** as the object.
- Set the trigger to fire when a record is updated.
- Pick **All Conditions Are Met (AND)** from the **Condition Requirements** menu.
- Within the new fields that display, choose **Stage** for the **Field**, the **Equals** operator, and **Closed Won** for the **Value**.
- Under **When to Run the Flow for Updated Records**, select **Only when a record is updated to meet the condition requirements**.

Running the flow based on record updates prevents the deployment from firing more than once. Without it, the flow runs on every subsequent save after the stage has changed.

![Flow Builder screen showing completed fields for a new record-triggered flow.](https://kinsta.com/wp-content/uploads/2026/04/flow-builder.png)

Flow Builder screen showing completed fields for a new record-triggered flow.

Finally, under **Optimize the Flow For**, select **Actions and Related Records** then toggle the **Add Asynchronous Path** switch that makes the callout possible and displays the two new ‘paths’.

### 3. Configure the async path, and add an HTTP Callout action

Salesforce does not permit HTTP callouts within an open trigger transaction. Any callout must go on the **Run Asynchronously** path. Actions placed on this path run after the triggering transaction commits.

![Flow Builder showing two paths for Run Immediately and Run Asynchronously.](https://kinsta.com/wp-content/uploads/2026/04/async-paths.png)

Flow Builder showing two paths for Run Immediately and Run Asynchronously.

On the **Run Asynchronously** path, add an **Action** element, and select **Create HTTP Callout** at the bottom of the right-hand panel.

![The Salesforce Flow Builder Search Actions panel showing different ways to interact with the Action element on the Run Asynchronous path.](https://kinsta.com/wp-content/uploads/2026/04/async-action.png)

The Flow Builder Search Actions panel showing interactions with the Action element on a path.

For the callout, give it a name and point the URL at your middleware endpoint, using `/go-live` as the slug. You can use a URL placeholder until the middleware is deployed. For local development, [ngrok](https://ngrok.com/) exposes your local port with a public URL. Also, select the Named Credential here.

Once you click **Next**, assign a `POST` method and give the callout a label. Clicking through, you need to offer an example JSON request and response. For the request, use the following:

```
{
  "site_id": "fbab4927-e354-4044-b226-29ac0fbd20ca"
}
```

If you select **Connect with Sample Response** on the next panel, you can use the **Connect** button to test the connection so far. However, this displays a 502 error until you write the middleware. For now, click Use Example Response and add the following:

```
{
  "message": "Received"
}
```

Later, come back and connect if you wish to test the connection further.

### 4. Setting a request body within Flow Builder

You have to do some manual work in order to set up the request body for the Action. The first step is to choose **New Resource** from the **Set Request Body** drop-down menu:

![Flow Builder showing the Set Request Body drop-down menu for an Action.](https://kinsta.com/wp-content/uploads/2026/04/new-resource.png)

Flow Builder showing the Set Request Body drop-down menu for an Action.

Here, enter a name (such as `requestBody`), save it, then select it as the **Value** for the request body. Next, add an **Assignment** element in the Flow Builder, give it a label and a name, then add the following within the **Set Variable Values** drop-down menus:

- **Variable:** `site_id`
- **Operator:** Equals
- **Value:** Scroll through the **Triggering Opportunity** submenu until you reach the **Kinsta Site ID**.

Completing this means the Salesforce setup is done. Next is to begin to build the Node app.

### 5. Build the Node.js middleware

With the flow configured, the middleware is where the Kinsta API calls live. Start a new Node.js project and install the dependencies:

```
npm init -y
npm install express dotenv
```

[Express.js](https://kinsta.com/blog/what-is-express-js/) handles the routing and request parsing. `dotenv` loads the `.env` file so your API key is available at runtime without appearing in your source code. Next, create `app.js` at the project root:

```
// app.js
const express = require('express');
require('dotenv').config();
const app = express();
app.use(express.json());

const KINSTA_API_URL = 'https://api.kinsta.com/v2';

const headers = {
  'Content-Type': 'application/json',
  Authorization: `Bearer ${process.env.KINSTA_API_KEY}`
};

app.post('/go-live', async (req, res) => {
  const { site_id } = req.body;
  if (!site_id) {
    return res.status(400).json({ message: 'site_id is required' });
  }
  // Kinsta API calls added in the steps below
  res.status(200).json({ message: 'Received' });
});

app.listen(3000, () => console.log('Middleware running on port 3000'));
```

The `headers` constant handles Bearer token authentication for every Kinsta API request in the application. Note that the Company ID, when needed for endpoints such as `GET /sites`, passes as a query parameter (not in the Authorization header). The `require('dotenv').config()` call at the top ensures the key loads from `.env` before anything else runs.

Before [creating a backup](https://kinsta.com/docs/wordpress-hosting/wordpress-backups/), the middleware needs the environment IDs for both staging and live. Add a `getEnvironments` function below the `headers` constant:

```
const getEnvironments = async (siteId) => {
  const resp = await fetch(
    `${KINSTA_API_URL}/sites/${siteId}/environments`,
    { method: 'GET', headers }
  );

  const data = await resp.json();
  return data.site.environments;
};
```

This calls `GET /sites/{siteId}/environments` and returns the full environments array.

### 6. Create a manual backup of the staging environment

[Pushing an environment](https://kinsta.com/docs/wordpress-hosting/wordpress-push-environments/) to production overwrites the live site. Creating a backup first means there is a restore point if the push surfaces a conflict that testing in staging did not catch.

Here, add a `createBackup` function below `getEnvironments`:

```
const createBackup = async (envId) => {
  const resp = await fetch(
    `${KINSTA_API_URL}/sites/environments/${envId}/manual-backups`,
    {
      method: 'POST',
      headers,
      body: JSON.stringify({ tag: 'pre-launch-backup' })
    }
  );

  const data = await resp.json();
  return data;
};
```

Kinsta processes the backup asynchronously and returns `202 Accepted` with an `operation_id` rather than a completed result:

```
{
  "operation_id": "backups:add-manual-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Adding a manual backup to environment in progress",
  "status": 202
}
```

To pause execution until the backup is complete before the push runs, add a `pollOperation` function underneath `createBackup`:

```
const pollOperation = async (operationId, intervalMs = 5000, maxAttempts = 12) => {
  for (let attempt = 0; attempt < maxAttempts; attempt++) {
    await new Promise(resolve => setTimeout(resolve, intervalMs));
    const resp = await fetch(
      `${KINSTA_API_URL}/operations/${operationId}`,
      { method: 'GET', headers }
    );
    const data = await resp.json();
    if (data.status === 200) return data;
    if (data.status >= 400) throw new Error(`Operation failed: ${data.message}`);
  }
  throw new Error('Operation timed out');
};
```

The loop checks every five seconds, covering up to a minute of processing time. A `200` status from the operations endpoint means the backup is complete and the push can proceed.

### 7. Push staging to production and monitor the completion

With the backup confirmed, add a `pushToProduction` function below `pollOperation`:

```
const pushToProduction = async (siteId, stagingEnvId, liveEnvId) => {
  const resp = await fetch(
    `${KINSTA_API_URL}/sites/${siteId}/environments`,
    {
      method: 'PUT',
      headers,
      body: JSON.stringify({
        source_env_id: stagingEnvId,
        target_env_id: liveEnvId,
        push_db: true,
        push_files: true,
        run_search_and_replace: true
      })
    }
  );
  const data = await resp.json();
  return data;
};
```

The `source_env_id` and `target_env_id` parameters identify where each environment pushes to. The `run_search_and_replace` flag updates hardcoded domain references in the database after the push. Without it, any staging domain references in the database persist on the live site after the push completes.

The push also returns `202 Accepted` with an `operation_id`. Passing that to `pollOperation` confirms completion. Finally, update the route handler to call all functions in sequence:

```
app.post('/go-live', async (req, res) => {
  const { site_id } = req.body;
  if (!site_id) {
    return res.status(400).json({ message: 'site_id is required' });
  }
  try {
    const environments = await getEnvironments(site_id);
    const stagingEnv = environments.find(env => env.name === 'staging');
    const liveEnv = environments.find(env => env.name === 'live');
    const backup = await createBackup(stagingEnv.id);
    await pollOperation(backup.operation_id);
    const push = await pushToProduction(site_id, stagingEnv.id, liveEnv.id);
    await pollOperation(push.operation_id);
    console.log(`Go-live complete for site ${site_id}`);
    res.status(200).json({ message: 'Go-live complete' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Go-live failed', error: err.message });
  }
});
```

Once you save your changes, update the Named Credential with the actual middleware URL if necessary, then **Activate** the flow. Next, run it with `node app.js` and move an Opportunity to the target stage in Salesforce.

![MyKinsta dashboard showing a staging site being pushed live.](https://kinsta.com/wp-content/uploads/2026/04/mykinsta-push.png)

MyKinsta dashboard showing a staging site being pushed live.

The site would go live without requiring a login to MyKinsta. You might also consider that with Salesforce’s [Headless 360](https://www.salesforce.com/news/stories/salesforce-headless-360-announcement/), you could run much of this outside the GUI, via the CLI, or as an MCP.

## Automating your agency’s deployment workflow with Salesforce and Kinsta

You can close the loop between the Kinsta API and Salesforce through a middleware Node app. Once you change the stage of an Opportunity in Salesforce, MyKinsta automatically takes a backup, pushes it to production, and confirms it without any manual steps.

When the middleware is ready for production, [Sevalla](https://sevalla.com/) is a deployment target built for exactly this kind of Node.js service. You push the project to a Git provider, connect the repository, add the environment variables, and update the Salesforce HTTP Callout URL to the live middleware address.

For agencies building automation across a client portfolio, Kinsta’s [Agency Partner Program](https://kinsta.com/agency-partner-program/) provides the infrastructure partnership and dedicated support that make this kind of work sustainable at scale.

Joel Olawanle
[Kinsta](https://kinsta.com/)

Joel is a Frontend developer working at Kinsta as a Technical Editor. He is a passionate teacher with love for open source and has written over 300 technical articles majorly around JavaScript and it's frameworks.

- [Website](https://joelolawanle.com/)
- [LinkedIn](https://www.linkedin.com/in/olawanlejoel/)
- [Twitter](https://twitter.com/olawanle_joel)
- [YouTube](https://www.youtube.com/@joelolawanle)
