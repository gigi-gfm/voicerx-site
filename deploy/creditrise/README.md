# Deploying CreditRise (DIY credit-repair app)

`creditrise` is a **static-assets Cloudflare Worker**, deployed
**completely separately from VoiceRx**. It serves one file —
`public/index.html` — a self-contained, offline-capable web app.

There is no server code and no backend. Everything the user enters
(profile, scores, disputed items) is stored **only in their browser's
localStorage** — nothing is sent anywhere. To ship a change you
re-upload the HTML asset.

## What it is

A DIY credit-repair companion in the spirit of self-help credit
educators (Nama Wynn–style). It gives the user the legal,
consumer-rights toolkit:

- **Scores** — track all 3 bureau scores (Equifax / Experian /
  TransUnion) and see the change over time.
- **Items** — log every negative account (collections, charge-offs,
  late payments, inquiries) and mark which bureaus report it and where
  each dispute stands.
- **Letters** — generate 5 letter types, auto-filled with the user's
  info and the correct bureau mailing address:
  - Round 1 Dispute (FCRA §611 / 15 U.S.C. §1681i)
  - Debt Validation (FDCPA §809 / 15 U.S.C. §1692g)
  - 609 Information Request
  - Method of Verification
  - Goodwill Letter
- **Plan** — a 7-step DIY repair roadmap.
- **Learn** — plain-English answers on rights, timelines, and strategy.

> **Not legal or financial advice.** CreditRise is an educational
> self-help tool, not a credit-repair organization or law firm. It does
> not guarantee any score change or item removal. Consumers can always
> dispute inaccurate items themselves for free under the FCRA.

## One-time setup

```bash
npm install -g wrangler   # or use: npx wrangler ...
wrangler login            # log in to the Cloudflare account you want to host under
```

## Deploy

```bash
cd deploy/creditrise
wrangler deploy
```

Wrangler prints the live `*.workers.dev` URL after the first deploy.

## Editing

The source of truth is `../../credit-repair/index.html`. After editing
it, copy it into this folder's `public/` before deploying:

```bash
cp ../../credit-repair/index.html public/index.html
wrangler deploy
```
