# Deploying VoiceRx for Dr. Tess

This static Cloudflare Worker serves `public/index.html` at:
https://voicerx-tess.winter-shadow-e82d.workers.dev

The Cloudflare account is Admin@garciafamilymedicine.care. The separate VoiceRx API handles transcription, note formatting, and cloud notes. Its source is not in this directory. Existing provider settings remain in browser storage; new devices need the provider's account setup. No default access token is embedded in this page.

## Deploy

After authorized Cloudflare login:

```bash
cd deploy/voicerx-tess
npx wrangler deploy
```

A GitHub commit does not deploy this worker automatically. Keep the current production asset available for rollback before deploying. This directory's `public/index.html` is the frontend source to deploy.

## Direct recording

Record → Stop → transcription → draft note is the primary workflow. Audio upload is an optional fallback under Other ways to add audio.

- Distinguishes microphone permission, missing-device, and startup errors.
- Chooses a supported MediaRecorder format and requests screen wake lock.
- Serializes device recovery snapshots and waits for the final audio chunk.
- Offers playback, download, and retry after a failed transcription.
- Retains recovery audio until the transcript is saved locally; attempts cloud saving too.
- Preserves unfinished recovery sessions when recovery is declined.
- Reuses a pending transcription job on retry to avoid unnecessary uploads.
- Locks patient fields while recording or holding unfinished audio.
- Contains no application recording-duration cutoff. Browser memory, storage, operating-system behavior, and transcription-service limits still apply.

Keep the recording tab in the foreground. Wake lock cannot guarantee background recording or capture during operating-system interruptions.

## Verification

Run from the repository root:

```bash
node --test tests/direct-recording.test.cjs
```

These tests exercise application logic with simulated microphone events and API responses, using fictional content. They do not validate physical microphone capture or the deployed API.

Before clinical use, verify on Dr. Tess's device with a fictional encounter:

1. Confirm provider connection and microphone permission.
2. Record 4–5 minutes without touching the screen; check the timer and stop.
3. Listen to playback, confirm both speakers are audible, and review the transcript and draft note.
4. Verify interruption/recovery and retry on a failed connection.
5. Confirm the saved note belongs to the entered patient and copies into the chart correctly.

Deployment and device verification remain outstanding until explicitly recorded as completed.
