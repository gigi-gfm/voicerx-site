# voicerx-weight-tracker — Clinician Weight Tracker (multi-patient)

An installable **clinician app** for keeping track of your weight-management
patients' **meals, sleep, and movement/exercise**. You hold a roster of
patients; each patient has a weekly diary, an auto-computed weekly tally, and
weight/movement trends over time.

**All data lives on this one device** (browser `localStorage`) — nothing is
uploaded and there is no server. Keep the device passcode-protected and use the
built-in **Back up** regularly.

Deployed like `voicerx-tess`: a **static-assets Cloudflare Worker** in the
**Admin@garciafamilymedicine.care** account.

## What it does

**Roster screen**
- Searchable list of patients with avatar, last-log recency, week count,
  latest weight and change since start.
- **＋ Add patient** (name, DOB, MRN, starting weight, height, and weekly
  goals: calorie/portion plan, sleep, movement, water).
- Tools: **Import a patient's shared week**, **Back up all data**, **Restore
  from a backup file**, **Add to home screen**, **Erase everything**.

**Patient screen**
- **Diary tab** — per-day cards (Mon–Sun): breakfast/lunch/dinner/snacks,
  water, mood, weigh-in, sleep (hours/quality/times), movement
  (activity/minutes/steps/intensity). Move between weeks with **‹ / ›**; each
  week is stored separately.
- **Summary tab** — weekly tally (total movement, avg sleep/water/steps,
  per-goal "X/7 days hit", consistency bars), plus weight trend
  (start/latest/change) and movement-by-week bars.
- **⚙** edit patient & goals (or delete the patient and all their logs).
- **🖨** print/PDF the current patient's week.

## Patients can send you their diary (option 3)

The patient app (`voicerx-weight-app`) has a **📤 Send my diary to the clinic**
button. It opens the phone's share sheet (email / message / AirDrop) with a
small `.json` file, or downloads it if sharing isn't available.

To bring it in here: **Import a patient's shared week** → pick that file. The
tracker matches the patient by name (creating them if new), merges their weeks,
and updates their goals/starting weight. Re-importing the same patient updates
rather than duplicates.

File formats understood by **Import / Restore**:
- a single patient's diary export `{ profile, weeks }` (from the patient app)
- a full tracker backup `{ patients: [ { …, weeks } ] }` (from **Back up all data**)

## One-time setup

```bash
npm install -g wrangler   # or use: npx wrangler ...
wrangler login            # log in as Admin@garciafamilymedicine.care
```

## Deploy

```bash
cd deploy/voicerx-weight-tracker
wrangler deploy
```

Uploads everything in `public/` and prints the live `workers.dev` URL.

> When you change the page, also bump the `CACHE` version in `public/sw.js`
> (e.g. `vrx-weight-tracker-v2`) so the installed app updates on next launch.

## Verify after deploy

1. **Loads & installs:** open the URL; confirm the **Add to home screen** flow.
2. **Add patient:** create one, enter goals — it appears on the roster.
3. **Log & persist:** open the patient, enter meals/sleep/movement, go back and
   reopen — entries persist; the roster shows latest weight / last log.
4. **Tally & trends:** the **Summary** tab reflects entries and goals; add a
   second week to see trends.
5. **Import:** from the patient app tap **Send my diary to the clinic**, save
   the file, then here tap **Import a patient's shared week** and pick it —
   that patient's weeks appear.
6. **Backup/restore:** **Back up all data**, then **Erase everything**, then
   **Restore** the file — your roster returns.
7. **Offline:** install, enable Airplane Mode, reopen — it still works.

## Files

- `public/index.html` — the whole app (roster + patient diary/summary + logic)
- `public/manifest.webmanifest` — PWA manifest
- `public/sw.js` — service worker (offline app-shell cache)
- `public/icon.svg` — app icon

## The three related artifacts

- **`voicerx-weight-tracker` (this app)** — for the **clinician**: track all
  patients on your device, import what patients send you.
- **`voicerx-weight-app`** — for **patients**: their own diary, with **Send my
  diary to the clinic**.
- **`voicerx-weight-diary`** + root `meal-diary-david-martin.html` — simpler
  single-week, print-first versions.
