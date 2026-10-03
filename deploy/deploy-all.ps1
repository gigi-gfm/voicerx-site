#!/usr/bin/env pwsh
# ─────────────────────────────────────────────────────────────────────────────
# Deploy VoiceRx static-asset Workers to Cloudflare, one after another.
#
# Usage (PowerShell), from anywhere:
#   .\deploy\deploy-all.ps1                         # deploys the two weight apps
#   .\deploy\deploy-all.ps1 voicerx-weight-tracker  # deploy just one
#   .\deploy\deploy-all.ps1 -All                    # every folder with a wrangler.toml
#
# Prereqs:
#   npm install -g wrangler
#   wrangler login        (as Admin@garciafamilymedicine.care)
#   ...or set $env:CLOUDFLARE_API_TOKEN before running.
# ─────────────────────────────────────────────────────────────────────────────
param(
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]]$Apps,
  [switch]$All
)

$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path

# Default set: the two weight-management apps (does NOT touch voicerx-tess).
if (-not $Apps -or $Apps.Count -eq 0) {
  $Apps = @('voicerx-weight-tracker', 'voicerx-weight-app')
}
if ($All) {
  $Apps = Get-ChildItem -Path $here -Directory |
    Where-Object { Test-Path (Join-Path $_.FullName 'wrangler.toml') } |
    ForEach-Object { $_.Name }
}

if (-not (Get-Command wrangler -ErrorAction SilentlyContinue)) {
  Write-Host "wrangler not found. Install it with:  npm install -g wrangler" -ForegroundColor Red
  exit 1
}

Write-Host "Cloudflare account:" -ForegroundColor Cyan
wrangler whoami
Write-Host "(If that shows 'not authenticated', run 'wrangler login' or set CLOUDFLARE_API_TOKEN, then re-run.)" -ForegroundColor DarkGray

$failed = @()
foreach ($app in $Apps) {
  $dir = Join-Path $here $app
  if (-not (Test-Path (Join-Path $dir 'wrangler.toml'))) {
    Write-Host "Skipping $app - no wrangler.toml at $dir" -ForegroundColor Yellow
    continue
  }
  Write-Host "`n=== Deploying $app ===" -ForegroundColor Green
  Push-Location $dir
  try {
    wrangler deploy
    if ($LASTEXITCODE -ne 0) { $failed += $app }
  } finally {
    Pop-Location
  }
}

Write-Host ""
if ($failed.Count -gt 0) {
  Write-Host ("Done, but these failed: " + ($failed -join ', ')) -ForegroundColor Red
  exit 1
}
Write-Host "All deploys complete. Note each printed *.workers.dev URL above." -ForegroundColor Green
