# Deploying voicerx-weight-diary (Weekly Weight-Management Diary)

`voicerx-weight-diary` is a **static-assets Cloudflare Worker** in the
**Admin@garciafamilymedicine.care** account, mirroring how `voicerx-tess` is
deployed. It serves one file — `public/index.html` — a self-contained weekly
diary that patients use to log **meals, sleep, and movement/exercise** for
weight management, with an auto-computed **weekly tally**.

There is no server code and **no patient data leaves the device**: everything
is saved in the browser's `localStorage`, keyed per patient name.

## What the page does

- **7 day cards** (Mon–Sun), each logging:
  - **Meals** — breakfast, lunch, dinner, snacks, water, mood/energy, optional weigh-in
  - **Sleep** — hours, quality, bed/wake time
  - **Movement/exercise** — activity, minutes, steps, intensity
- **This Week's Goals** — calorie/portion target, plus sleep / movement / water
  targets set with Dr. Garcia. The tally scores each day against them.
- **Weekly Tally** (auto-calculated): total movement minutes, average sleep,
  average water, average steps, per-goal "X/7 days hit" counts, and
  logging-consistency bars.
- **Notes & Wins for Dr. Garcia** free-text box.
- **Print / Save PDF**, **Save**, **Fill in dates**, and **Clear week** buttons.

## Personalized links (per patient)

The page reads a `?patient=` query parameter, so the clinic can hand each
patient a pre-filled link or QR code:

> https://voicerx-weight-diary.<your-subdomain>.workers.dev/?patient=David%20Martin

Each patient's entries are stored under their own key, so several patients can
safely share one device (e.g. a clinic tablet) without overwriting each other.
Changing the **Patient** field loads that patient's own saved week.

## One-time setup

```bash
npm install -g wrangler   # or use: npx wrangler ...
wrangler login            # log in as Admin@garciafamilymedicine.care
```

## Deploy

```bash
cd deploy/voicerx-weight-diary
wrangler deploy
```

That uploads `public/index.html` and prints the live `workers.dev` URL. Note
the URL the first deploy assigns — reuse it for any QR codes / saved links so
they keep working on later deploys.

## Updating the page

`public/index.html` is the **single source of truth** for the deployed diary.
Edit it, then run `wrangler deploy` again. (The repo root also keeps
`meal-diary-david-martin.html` — an offline single-file copy pre-filled for one
patient; the deployed version is the reusable, any-patient template.)

## Verify after deploy

1. **Loads:** open the URL — the diary renders with empty day cards.
2. **Prefill:** open `…/?patient=David%20Martin` — the Patient field shows
   "David Martin".
3. **Saves:** type into a meal/sleep/movement field, reload — the entry is
   still there.
4. **Tally:** enter sleep hours and movement minutes across a couple of days —
   the Weekly Tally totals/averages and goal counts update live.
5. **Multi-patient:** change the Patient name to another person — the week
   resets to that patient's own (empty) data; switch back and the first
   patient's entries return.
6. **Print:** tap **Print / Save PDF** — confirm a clean, color-correct sheet.
