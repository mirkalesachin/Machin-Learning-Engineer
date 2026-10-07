# Activity 13 — Serve a Model on Cloud Run

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v2.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

## Objective

Package a Flask prediction API, test its contract and analyze load-test results.

## Deliverables

- `app.py`
- `Dockerfile`
- `requirements.txt`
- `test_api.py`
- `load_results.csv`
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

### Step 1 — Create a virtual environment and install pinned dependencies

Create a virtual environment and install pinned dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Check:** Record the observable result or explain the error before continuing.

### Step 2 — Run the Flask service locally and verify /health before using /predict

Run the Flask service locally and verify `/health` before using `/predict`.

```bash
python3 app.py
```

**Check:** Record the observable result or explain the error before continuing.

### Step 3 — In another terminal, run the API contract tests

In another terminal, run the API contract tests.

```bash
python3 test_api.py --base-url http://127.0.0.1:8080
```

**Check:** Record the observable result or explain the error before continuing.

### Step 4 — Build the container and run the same health and prediction tests against it

Build the container and run the same health and prediction tests against it.

```bash
docker build -t pmle-api:v8 .
docker run --rm -p 8080:8080 pmle-api:v8
```

**Check:** Record the observable result or explain the error before continuing.

### Step 5 — Inspect load_results.csv; plot QPS against p95 latency and identify saturation

Inspect `load_results.csv`; plot QPS against p95 latency and identify saturation.

**Check:** Record the observable result or explain the error before continuing.

### Step 6 — Draft a Cloud Run deployment with authenticated ingress, min/max instances and region

Draft a Cloud Run deployment with authenticated ingress, min/max instances and region.

**Check:** Record the observable result or explain the error before continuing.

### Step 7 — Deploy only if approved, then record revision ID and image digest

Deploy only if approved, then record revision ID and image digest.

**Check:** Record the observable result or explain the error before continuing.

### Step 8 — Test one invalid schema and confirm the service returns a controlled 4xx response without secrets

Test one invalid schema and confirm the service returns a controlled 4xx response without secrets.

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
