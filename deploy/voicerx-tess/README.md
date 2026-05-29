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

## Verify after deploy

1. Open the URL on the target iPhone — confirm the dictation page loads.
2. Record for **3+ minutes** with the screen left untouched — it should no
   longer cut off (Screen Wake Lock keeps the phone awake).
3. Generate a note and tap **Copy** — confirm it copies (and that the manual
   fallback box appears if the browser blocks programmatic copy).
