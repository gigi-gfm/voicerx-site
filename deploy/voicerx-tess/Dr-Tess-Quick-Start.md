# VoiceRx — direct recording for Dr. Tess

Open https://voicerx-tess.winter-shadow-e82d.workers.dev in your browser.
These instructions describe the direct-recording update; they take effect after deployment.

1. Confirm Dr. Tess's account is connected in Settings.
2. Enter the patient's name, visit date, complaint, pronouns, language, and note type.
3. Tap **Record encounter**. Allow microphone access when asked.
4. Keep VoiceRx open and the screen on during the encounter. The timer and recording indicator show when capture is active.
5. Tap **Stop recording**. VoiceRx transcribes the audio and prepares a draft note automatically.
6. Review and correct the transcript and draft before copying the note into the patient chart.

No separate recording app or manual file upload is required for this workflow.

If transcription fails, use the playback controls to check the recording, then **Retry transcription**. Retry checks an existing transcription job when available. You can also download the captured audio. The page reports whether a recovery copy was saved on this device; if storage fails, keep the tab open.

After reopening VoiceRx, accept the recovery prompt to restore an unfinished recording. Declining the prompt does not delete it. Choosing **+ New** asks before leaving an untranscribed recording.

A browser or operating system can interrupt microphone access when switching apps, locking the screen, or receiving a call. A screen wake lock is requested when supported, but uninterrupted background recording is not guaranteed. If interrupted, review the captured audio before retrying.

Notes are cached on this device and cloud saving is attempted. A cloud-sync failure is reported; verify the final note is saved in the patient chart.
