#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# Deploy VoiceRx static-asset Workers to Cloudflare, one after another.
#
# Usage, from anywhere:
#   ./deploy/deploy-all.sh                          # deploys the two weight apps
#   ./deploy/deploy-all.sh voicerx-weight-tracker   # deploy just one
#   ./deploy/deploy-all.sh --all                    # every folder with a wrangler.toml
#
# Prereqs:
#   npm install -g wrangler
#   wrangler login        (as Admin@garciafamilymedicine.care)
#   ...or export CLOUDFLARE_API_TOKEN before running.
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

apps=("$@")
if [ "${1:-}" = "--all" ]; then
  apps=()
  for d in "$here"/*/; do
    [ -f "${d}wrangler.toml" ] && apps+=("$(basename "$d")")
  done
elif [ ${#apps[@]} -eq 0 ]; then
  # Default set: the two weight-management apps (does NOT touch voicerx-tess).
  apps=(voicerx-weight-tracker voicerx-weight-app)
fi

command -v wrangler >/dev/null 2>&1 || {
  echo "wrangler not found. Install it with:  npm install -g wrangler" >&2; exit 1; }

echo "Cloudflare account:"
wrangler whoami || echo "(not authenticated — run 'wrangler login' or set CLOUDFLARE_API_TOKEN, then re-run)"

failed=()
for app in "${apps[@]}"; do
  dir="$here/$app"
  if [ ! -f "$dir/wrangler.toml" ]; then
    echo "Skipping $app — no wrangler.toml at $dir"
    continue
  fi
  echo
  echo "=== Deploying $app ==="
  ( cd "$dir" && wrangler deploy ) || failed+=("$app")
done

echo
if [ ${#failed[@]} -gt 0 ]; then
  echo "Done, but these failed: ${failed[*]}" >&2
  exit 1
fi
echo "All deploys complete. Note each printed *.workers.dev URL above."
