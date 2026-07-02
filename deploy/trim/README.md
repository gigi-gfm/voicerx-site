# Deploying Trim (weight & nutrition manager)

`trim` is a **static-assets Cloudflare Worker** in the
**Admin@garciafamilymedicine.care** account (same account as `voicerx-tess`).
It serves one file — `public/index.html` — at:

> https://trim.winter-shadow-e82d.workers.dev

*(The exact hostname is `https://trim.<your-account-subdomain>.workers.dev`.
Your account's subdomain is `winter-shadow-e82d`, matching the VoiceRx worker.
The real URL is printed by `wrangler deploy` — use that.)*

There is no server code. To ship a change you re-upload the HTML asset.

## One-time setup

```bash
npm install -g wrangler   # or use: npx wrangler ...
wrangler login            # opens a browser; log in as Admin@garciafamilymedicine.care
```

## Deploy

```bash
cd deploy/trim
wrangler deploy
```

That uploads `public/index.html` and prints the live URL. Give **that URL**
(not the GitHub link) to patients.

## Updating the app

`public/index.html` is a copy of `weight-manager/index.html` (the source of
truth in the repo root). To ship a change: edit `weight-manager/index.html`,
copy it over (`cp weight-manager/index.html deploy/trim/public/index.html`),
then run `wrangler deploy` again.

## What patients get

- A single-page web app — works on phone or desktop, no install, no login.
- **All data stays in the patient's own browser** (localStorage). Nothing is
  uploaded to any server, so no account is needed and no data leaves their
  device. Export/Import buttons let them back up their data as a JSON file.
- Because storage is per-device/per-browser, data does **not** sync across
  devices and is **not** visible to the clinic. If you need clinician-visible
  patient data, that requires a backend — this build intentionally has none.

## Features

- Dashboard: current/goal weight, BMI + category, today's calories
- Weight log with per-entry deltas and notes
- Food log with calories + macros, daily calorie ring and macro breakdown
- Goals: start/goal weight, target date, height, daily calorie target
- Weight-trend chart (goal line + 7-day moving average) and 14-day calorie chart
- Trend projection with ETA vs. target date
- kg/lb and cm/in units with value-preserving conversion
