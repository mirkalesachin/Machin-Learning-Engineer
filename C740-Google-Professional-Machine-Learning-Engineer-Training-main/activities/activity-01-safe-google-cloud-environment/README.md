# Activity 01 — Create a Safe Google Cloud Training Environment

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v2.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

## Objective

Create a Google account, Cloud project, billing budget, IAM boundary and Cloud Shell workspace.

## Deliverables

- `budget-policy.json`
- `check_environment.sh`
- `iam-role-matrix.csv`
- A completed `evidence/` folder with decision notes and verification output

## Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: a Google account you control and trainer approval to create an isolated training project.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


## Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

## Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


## Detailed step-by-step guide

### Step 1 — Open a private browser window and go to https://accounts.google.com/signup

Open a private browser window and go to `https://accounts.google.com/signup`. Create a dedicated training Google Account or sign in with an approved existing account. Complete identity and recovery checks; do not use a shared password.

**Check:** Record the observable result or explain the error before continuing.

### Step 2 — Go to https://console.cloud.google.com/

Go to `https://console.cloud.google.com/`. Accept the Google Cloud terms when prompted. If the free-trial offer is available and appropriate, review the current terms before entering payment details; free-tier offers can change.

**Check:** Record the observable result or explain the error before continuing.

### Step 3 — Open the project selector, choose New Project, name it pmle-training-<initials>, record the generated project ID, and select the correct organisation or No organisation only if your trainer approves

Open the project selector, choose **New Project**, name it `pmle-training-<initials>`, record the generated project ID, and select the correct organisation or **No organisation** only if your trainer approves.

**Check:** Record the observable result or explain the error before continuing.

### Step 4 — Open Billing and link the training project to the authorised billing account

Open **Billing** and link the training project to the authorised billing account. Billing enables paid services; it does not make all usage free.

**Check:** Record the observable result or explain the error before continuing.

### Step 5 — Open Billing > Budgets & alerts, create a small training budget, and add alert thresholds at 50%, 90% and 100%

Open **Billing > Budgets & alerts**, create a small training budget, and add alert thresholds at 50%, 90% and 100%. Billing alerts do not automatically stop resources.

**Check:** Record the observable result or explain the error before continuing.

### Step 6 — Open IAM & Admin > IAM

Open **IAM & Admin > IAM**. Confirm your user has only the roles required for training. Do not grant Owner to classmates or service accounts.

**Check:** Record the observable result or explain the error before continuing.

### Step 7 — Open APIs & Services > Library and enable Vertex AI, BigQuery, Cloud Storage, Artifact Registry, Cloud Build and Cloud Run APIs

Open **APIs & Services > Library** and enable Vertex AI, BigQuery, Cloud Storage, Artifact Registry, Cloud Build and Cloud Run APIs. Record any enablement error before changing roles.

**Check:** Record the observable result or explain the error before continuing.

### Step 8 — Activate Cloud Shell from the console header

Activate Cloud Shell from the console header. Cloud Shell already includes the Google Cloud CLI and uses your signed-in identity.

```bash
gcloud auth list
```

**Check:** Record the observable result or explain the error before continuing.

### Step 9 — Set and verify project and region variables for this shell session

Set and verify project and region variables for this shell session.

```bash
export PROJECT_ID='<PROJECT_ID>' REGION='asia-southeast1'
gcloud config set project "$PROJECT_ID"
gcloud config set ai/region "$REGION"
```

**Check:** Record the observable result or explain the error before continuing.

### Step 10 — Run the supplied environment checker and save its output as evidence

Run the supplied environment checker and save its output as evidence.

```bash
bash check_environment.sh | tee evidence/activity-01-environment.txt
```

**Check:** Record the observable result or explain the error before continuing.

### Step 11 — Review iam-role-matrix.csv

Review `iam-role-matrix.csv`. For each activity, grant the narrow predefined role only when needed; avoid service-account keys.

**Check:** Record the observable result or explain the error before continuing.

### Step 12 — Record the project ID, billing account alias, budget name, enabled APIs and IAM decision in your activity evidence

Record the project ID, billing account alias, budget name, enabled APIs and IAM decision in your activity evidence. Do not record payment details.

**Check:** Record the observable result or explain the error before continuing.


## Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

## Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

## Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.
