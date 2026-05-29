# Deploying voicerx-tess (Dr. Tess's dictation page)

`voicerx-tess` is a **static-assets Cloudflare Worker** in the
**Admin@garciafamilymedicine.care** account. It serves one file —
`public/index.html` — at:

> https://voicerx-tess.winter-shadow-e82d.workers.dev

There is no server code. To ship a change you re-upload the HTML asset.

## One-time setup

```bash
npm install -g wrangler   # or use: npx wrangler ...
wrangler login            # opens a browser; log in as Admin@garciafamilymedicine.care
```

## Deploy

```bash
cd deploy/voicerx-tess
wrangler deploy
```

That uploads `public/index.html` and keeps the same workers.dev URL, so the
QR code and Dr. Tess's saved link keep working unchanged.

## Updating the page

`public/index.html` is the **single source of truth** for Dr. Tess's
dictation page. Edit it, then run `wrangler deploy` again.

## Reliability features built into the page

Three layers protect a dictation from being lost:

1. **Screen Wake Lock** — while recording, the page holds the screen on so the
   phone does not auto-lock. This is the fix for the "recording stopped at
   ~2:30" bug: the screen was timing out and the OS suspended the microphone.
2. **Crash-safe recording buffer** — every second of audio is written to the
   browser's IndexedDB *as it records*. If the tab is killed mid-encounter
   (Android memory/battery pressure, an accidental reload, or a crash), the
   audio is not lost. On the next load the page shows a **"Recover unfinished
   recording?"** prompt with the patient name, note type, and length, and lets
   you **Transcribe it** or **Discard** it. The buffer is cleared only after a
   note is produced successfully, so even a failed upload stays recoverable.
3. **Robust copy** — the Copy buttons try the Clipboard API, fall back to the
   legacy method, and as a last resort show the note text pre-selected so it
   can be copied by hand. Copy can no longer silently fail.

### Limits worth knowing
- The wake lock prevents the *automatic* screen timeout. Pressing the power
  button to blank the screen, or switching away from the browser tab, can
  still let the OS suspend the mic. Leave the tab in the foreground, screen on.
- **Battery Saver** mode can ignore wake locks. Keep it off during clinic, or
  keep the phone on a charger.
- Open the page in **Chrome / from the home-screen icon**, not from an in-app
  browser inside Messages/WhatsApp/Gmail (those often break mic + wake lock).

## Verify after deploy

Test on the device Dr. Tess actually uses (Android, in Chrome):

1. **Loads:** open the URL / scan the QR — confirm the dictation page loads.
2. **No cutoff:** record for **4–5 minutes** with the screen left untouched —
   it should keep recording the whole time (Screen Wake Lock).
3. **Recovery:** start a recording, talk ~30s, then **reload the tab** (or
   swipe Chrome closed and reopen). You should get the "Recover unfinished
   recording?" prompt → tap **Transcribe it** → the note appears.
4. **Copy:** generate a note and tap **Copy** — confirm it copies (and that the
   manual fallback box appears if the browser blocks programmatic copy).
