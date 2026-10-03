# voicerx-weight-app — Weight Diary (installable app for all patients)

A self-contained **installable web app (PWA)** you can hand to every
weight-management patient. It tracks the three things together — **meals,
sleep, and movement/exercise** — week over week, with an auto-computed weekly
tally and simple trends. It installs to the phone's home screen, works
**offline**, and keeps **all data on the patient's own device** (browser
`localStorage`). Nothing is uploaded; there is no server code.

Deployed the same way as `voicerx-tess`: a **static-assets Cloudflare Worker**
in the **Admin@garciafamilymedicine.care** account.

## What the patient gets

**Diary tab** — one card per day (Mon–Sun):
- **Meals**: breakfast, lunch, dinner, snacks
- **Water** (glasses), mood/energy, optional daily weigh-in
- **Sleep**: hours, quality, bed/wake time
- **Movement/exercise**: activity, minutes, steps, intensity

Move between weeks with the **‹ / ›** arrows — each week is saved separately,
so it's an ongoing diary, not a one-week sheet. Today's card is highlighted.

**Summary tab** — the **Weekly Tally** (total movement minutes, avg sleep, avg
water, avg steps, and "X/7 days hit goal" against the patient's goals) plus
logging-consistency bars, a **weight trend** (start → latest → change), and a
**movement-by-week** bar chart.

**Me tab** — name, starting weight/height, and weekly goals (calorie/portion
plan, sleep, movement, water) set with Dr. Garcia. Also: **Add to home
screen**, **Print/Save PDF**, **Export backup (JSON)**, and **Erase all data**.

## Installing on a phone

- **Android (Chrome):** open the URL → an **Add to home screen** prompt
  appears (or use the button on the **Me** tab / browser menu).
- **iPhone (Safari):** Share → **Add to Home Screen**.

Once installed it opens full-screen like a native app and works with no signal.

## Optional personalized link

The page accepts `?patient=Name`, so a handout/QR can pre-fill the name the
first time the app is opened:

> https://voicerx-weight-app.<your-subdomain>.workers.dev/?patient=David%20Martin

(After that the name is saved on the device; the parameter is only used if no
name is set yet.)

## One-time setup

```bash
npm install -g wrangler   # or use: npx wrangler ...
wrangler login            # log in as Admin@garciafamilymedicine.care
```

## Deploy

```bash
cd deploy/voicerx-weight-app
wrangler deploy
```

This uploads everything in `public/` and prints the live `workers.dev` URL.
Note that URL and reuse it for any QR codes / saved links.

> Bumping the cache: when you change the page, also bump the `CACHE` version in
> `public/sw.js` (e.g. `vrx-weight-diary-v2`) so installed apps pick up the new
> version on next launch.

## Verify after deploy

1. **Loads & installs:** open the URL; on Android confirm the install prompt /
   **Add to home screen** button works.
2. **Offline:** install it, turn on Airplane Mode, reopen — it still loads.
3. **Logs & persists:** enter meals/sleep/movement, close and reopen — entries
   are still there.
4. **Tally:** on **Summary**, totals/averages and "X/7 hit goal" reflect what
   you entered (set goals on **Me** first).
5. **Weeks:** tap **›** to next week — it's empty; tap **‹** back — your data
   returns. Trends on **Summary** show more than one week once logged.
6. **Print:** **Print/Save PDF** produces a clean week sheet.

## Files

- `public/index.html` — the whole app (UI + logic), single source of truth
- `public/manifest.webmanifest` — PWA manifest (name, icons, standalone)
- `public/sw.js` — service worker (offline app-shell cache)
- `public/icon.svg` — app icon (navy tile, orange heart + pulse)

> Related: `deploy/voicerx-weight-diary/` is the simpler single-week,
> print-first version, and the repo root `meal-diary-david-martin.html` is an
> offline single-file copy pre-filled for one patient. **This app
> (`voicerx-weight-app`) is the one to give to all patients.**
