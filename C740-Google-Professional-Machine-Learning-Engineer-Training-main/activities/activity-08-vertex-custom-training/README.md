# Activity 08 — Package a Vertex AI Custom Training Job

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v2.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

## Objective

Build a reproducible training package and container with managed output paths.

## Deliverables

- `train.py`
- `Dockerfile`
- `custom_job.yaml`
- `requirements.txt`
- A completed `evidence/` folder with decision notes and verification output

## Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
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

### Step 1 — Inspect train.py, requirements.txt, Dockerfile and custom_job.yaml; trace each file to the managed job lifecycle

Inspect `train.py`, `requirements.txt`, `Dockerfile` and `custom_job.yaml`; trace each file to the managed job lifecycle.

**Check:** Record the observable result or explain the error before continuing.

### Step 2 — Run the training entry point locally and confirm it writes to the AIP_MODEL_DIR fallback

Run the training entry point locally and confirm it writes to the `AIP_MODEL_DIR` fallback.

```bash
python3 train.py --data-uri mock://customers --epochs 3
```

**Check:** Record the observable result or explain the error before continuing.

### Step 3 — Build the container locally with a versioned tag; do not use latest as deployment evidence

Build the container locally with a versioned tag; do not use `latest` as deployment evidence.

```bash
docker build -t pmle-train:v8 .
```

**Check:** Record the observable result or explain the error before continuing.

### Step 4 — Run the container with a mounted output directory and verify the model artifact appears

Run the container with a mounted output directory and verify the model artifact appears.

```bash
docker run --rm -v "$PWD/output:/model" -e AIP_MODEL_DIR=/model pmle-train:v8
```

**Check:** Record the observable result or explain the error before continuing.

### Step 5 — Replace project and Artifact Registry placeholders only if a live push is approved

Replace project and Artifact Registry placeholders only if a live push is approved.

**Check:** Record the observable result or explain the error before continuing.

### Step 6 — Validate the worker-pool machine type, service account and artifact output permissions in custom_job.yaml

Validate the worker-pool machine type, service account and artifact output permissions in `custom_job.yaml`.

**Check:** Record the observable result or explain the error before continuing.

### Step 7 — Submit the job only with trainer approval; record job ID, image digest and log link

Submit the job only with trainer approval; record job ID, image digest and log link.

**Check:** Record the observable result or explain the error before continuing.

### Step 8 — Diagnose a supplied missing-dependency failure and propose a pinned dependency fix

Diagnose a supplied missing-dependency failure and propose a pinned dependency fix.

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
