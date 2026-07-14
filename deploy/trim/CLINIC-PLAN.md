# Trim — Clinic-viewable (HIPAA-appropriate) build plan

This describes the architecture for turning Trim from a browser-only tool into
a system where **clinicians can view patient weight & nutrition data**. Because
that stores identifiable patient health data on a server, it is **ePHI under
HIPAA** and must be built and operated accordingly.

## Honest scope note — read first

Shipping this code does **not** by itself make the practice "HIPAA compliant."
Code can provide the **technical safeguards**; compliance also requires
organizational and legal work that is *not* code:

- **Signed BAAs** with every vendor that touches PHI (host, database, email/SMS,
  error monitoring, etc.).
- A **security risk assessment**, written policies, workforce training, breach
  notification procedures, and administrative/physical safeguards.

What I can build: authentication, per-patient data isolation, encryption in
transit and at rest, audit logging, session timeouts, least-privilege access,
and the clinician dashboard. What you must do: sign the BAAs, provision the
infrastructure under your practice's account, and complete the compliance
program (ideally with a HIPAA consultant).

## Recommended stack

**Frontend:** keep it as static HTML/JS (works on Cloudflare Pages/Workers, the
stack you already use). The patient app and the clinician dashboard are both
static SPAs that talk to an API.

**Backend + database — two viable paths (this is your cost decision):**

| | Supabase (Team plan) | AWS (RDS + Cognito + Lambda) |
|---|---|---|
| BAA | Yes, on **Team plan** (~$599/mo) | **Free** (accept AWS BAA in Artifact) |
| Est. monthly cost | ~$599+/mo | ~$30–80/mo at small scale |
| Build speed | Fastest — Postgres + Auth + Row-Level Security built in | Slower — more wiring, but I write it |
| Ops burden | Low | Higher (you own more infra) |
| Best when | You want it correct fast and the cost is acceptable | You want low running cost and can accept more setup |

Both give: managed Postgres, encryption at rest, TLS in transit, and are
HIPAA-eligible **with a signed BAA**. Row-Level Security (Supabase) or scoped
IAM/query filters (AWS) enforce that a patient sees only their own rows and a
clinician sees only their practice's patients.

**My recommendation:** if the ~$599/mo is acceptable, **Supabase Team** — it is
the fastest route to a correct, auditable HIPAA-aligned build (auth, RLS, and
audit-friendly Postgres out of the box). If running cost is the priority for a
small practice, **AWS** with the free BAA is materially cheaper and I can build
it — it just takes more setup and you own more ops.

## Architecture

```
Patient phone ──┐
                ├─▶  API (auth + validation + audit)  ──▶  Postgres (RLS)
Clinician web ──┘
```

- **Auth:** email + password with mandatory 2FA for clinicians; magic-link or
  password for patients. Short session timeouts; auto-logout.
- **Roles:** `patient`, `clinician`, `admin`. Enforced at the row level.
- **Data model (first cut):**
  - `profiles` (id, role, name, dob, height, units, clinic_id)
  - `weights` (id, patient_id, date, kg, note, created_at)
  - `foods` (id, patient_id, date, name, cal, protein, carb, fat)
  - `goals` (patient_id, start_kg, goal_kg, target_date, cal_target)
  - `patient_clinician` (patient_id, clinician_id) — who may view whom
  - `audit_log` (id, actor_id, action, subject_patient_id, at, ip) — every
    read/write of PHI is logged
- **Encryption:** TLS everywhere; DB encrypted at rest; secrets in a managed
  secret store (never in the repo).
- **Clinician dashboard:** patient list → per-patient trends, charts, goal
  progress (reuses the existing Trim charts), plus flags (e.g. no weigh-in in N
  days, trending away from goal).
- **Patient app:** the existing Trim UI, but reading/writing the API instead of
  localStorage, so their clinician can see it. Offline-friendly with sync.

## Phased delivery

1. **Foundation:** provision infra (your account), schema, auth, RLS, audit log.
2. **Patient app on the API:** port the current Trim UI from localStorage to the
   backend; add login and sync.
3. **Clinician dashboard:** patient roster + per-patient views and charts.
4. **Hardening:** session timeouts, rate limiting, audit review UI, backups,
   and a pre-launch security review.

Nothing goes live with real patients until the BAAs are signed and step 4 is
done.
