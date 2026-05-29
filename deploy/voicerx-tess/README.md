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
dictation page. It is her real production page (provider login / Bearer-token
auth, pronoun selection, multi-note types, after-visit summaries, and the
existing IndexedDB audio snapshot + recovery). Edit it, then run
`wrangler deploy` again.

> History note: an older backup copy was briefly deployed by mistake and rolled
> back. The live page was captured and patched directly, so this file now
> matches what Dr. Tess actually uses.

## Reliability features

1. **Screen Wake Lock** *(added)* — while recording, the page holds the screen
   on so the phone does not auto-lock. This is the fix for the "recording
   stopped at ~2:30" bug: the screen was timing out and the OS suspended the
   microphone. Re-acquired automatically when the tab regains focus.
2. **No recording time limit** *(changed)* — recording continues until Stop is
   tapped (the old 60-minute auto-stop was removed). A gentle "still recording"
   reminder appears every 30 minutes.
3. **Crash-safe recording** *(already in the page)* — audio is snapshotted to
   IndexedDB every few seconds and on interruption (phone call, lost mic, OS
   suspend), and offered for recovery on reopen.
4. **Robust copy** *(added)* — the Copy buttons try the Clipboard API, fall back
   to the legacy method, and as a last resort show the text pre-selected so it
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
5. **Auth + pronouns:** stop a short recording and confirm a note is produced
   (no "Unauthorized") and that it uses the pronouns selected for the patient.
