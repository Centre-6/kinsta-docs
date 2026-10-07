---
url: "https://kinsta.com/docs/wordpress-hosting/site-management/cron-jobs/"
title: "Site Management - Cron Jobs"
tier: "docs"
product: "wordpress-hosting"
product_label: "Managed WordPress Hosting"
subsection: "site-management"
section: []
kinsta_last_updated: "January 20, 2025"
sitemap_lastmod: "2025-01-20T18:03:24+00:00"
fetched_at: "2026-10-07T22:38:29Z"
sha256: "0057b8058f5bab6083bb1c8bdf9145bb62c4f59861536bc80bd33d4d3cbd45ff"
body_chars: 5122
extracted_with: "main article"
status: "live"
---

# Site Management - Cron Jobs

**Product:** Managed WordPress Hosting
**Source:** https://kinsta.com/docs/wordpress-hosting/site-management/cron-jobs/
**Kinsta last updated:** January 20, 2025

## On this page

- [How to write a server cron](#how-to-write-a-server-cron)
- [How to add a server cron](#how-to-add-a-server-cron)
- [Kinsta policies on server cron jobs](#kinsta-policies-on-server-cron-jobs)

---

Kinsta’s container-based infrastructure means that every site runs in a private container with its own crontab. This means that at Kinsta, we allow our users to add real server cron jobs to each site container.

If you’d rather use the WordPress built-in cron system, please see our article on [how to create and modify a WordPress cron job](https://kinsta.com/blog/wordpress-cron-job/).

## How to write a server cron

A task added to crontab consists of two parts:

1. A series of numbers and asterisks defining how frequently the cron should run.
2. A command to be executed on the server.

When writing a cron, you’ll need to determine those two factors: the command that needs to be executed and how frequently it should be scheduled.

There are several reasons you might want to run a cron job on your site container. Examples include:

- Scanning your site for broken links and generating a report.
- Scheduling future-dated posts to ensure they are published on time.
- Creating user activity logs.
- Generating and emailing sales activity reports.
- Sending password expiry notifications to users.

To perform these tasks, you need a custom PHP script placed in your WordPress root directory or a secure folder. The script handles the required processes and executes them on the server. The cron job executes the scripts automatically at a specific time and interval.

The cron expression determines when and how often the cron job runs. It is made up of the following five fields:

- `*` Minute (0-59)
- `*` Hour (0-23)
- `*` Day of the month (1-31)
- `*` Month (1-2)
- `*` Day of the week (0-6)

For example, if you want to run a script every Sunday at 2 am, you would need to add the following cron command:

Copy

```
0 2 * * 0 php /path-to-your-script/script-name.php >/dev/null 2>&1
```

If you want to work out the crontab syntax yourself, the [crontab documentation from The Open Group](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/crontab.html) is a great place to learn and see some practical examples. There is a lot of support available online about how to format your expression, such as [Crontab Generator](https://crontab-generator.org/) or [Cronitor](https://crontab.guru/). The following are some common examples of how to format your expression:

- to run the cron job every 30 minutes, use `*/30 * * * *` note that `*/30` ensures the process runs every 30 minutes (12:00, 12:30, etc.); if you use `30` without the `*/` it will only run at minute 30 (12:30, 13:30, etc.).
- to run the cron job every hour, use `0 * * * *`
- to run the cron job every day at 12:00 AM, use `0 0 * * *`
- to run the cron job at 12:00 AM, on Fridays only, use `0 0 * * 5`
- to run the cron job at 12:00 AM on the first day of every month, use `0 0 1 * *`

## How to add a server cron

Once you have the cron job ready to add to the container, you have two options:

- Add the job to the crontab yourself.
- Ask our Support team to upload the job to the crontab for you.

To upload the job yourself,

1. [Access your site container over SSH](https://kinsta.com/docs/wordpress-hosting/connect-to-ssh/)
2. Run the following command:  

   Copy

   ```
   crontab -e
   ```
3. Select your [text editor of choice](https://kinsta.com/blog/best-text-editors/) (select nano if you’re unsure).
4. Paste your cron command **at the end of the file**.
5. Then close the file. You’ll see a message like this confirming that the crontab has been updated: `crontab: installing new crontab`.

![Run crontab -e and then select your preferred text editor.](https://kinsta.com/wp-content/uploads/2018/07/Screen-Shot-2018-07-03-at-3.21.41-PM.png)

Run crontab -e and then select your preferred text editor.

If you aren’t comfortable using SSH, you can open a new chat with our Support team and ask us to add the job to your site’s crontab.

## Kinsta policies on server cron jobs

- **Kinsta’s support of server cron jobs is limited to uploading the cron job exactly as you provide it to the container crontab or editing cron jobs as you direct.** If you need assistance writing the command that will be executed by crontab, you will need to work with a qualified developer to write the cron job.
- **The minimum cron job interval is 5 minutes.** Please do not upload server cron jobs that will run more frequently than every 5 minutes. If you ask our Support team to add a cron that runs more frequently than every 5 minutes, we will suggest that the interval be increased to 5 minutes. If you need a cron to run more often, you’ll need a [dedicated server](https://kinsta.com/docs/wordpress-hosting/wordpress-getting-started/dedicated-server/) to do so. On a dedicated server, you can run cron jobs every minute.
- **Please do not edit or move the jobs at the top of the crontab.** These jobs are added by our System Engineering team and must remain at the top of the file.
- **Please add your custom server cron jobs to the bottom of the crontab file.** If you add your custom server cron jobs at the top of the file, our maintenance scripts, staging system, or backup system may overwrite your custom server cron jobs.
