# Activity 12 — Register and Canary a Model Version

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v2.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

## Objective

Create registry metadata, traffic split, guardrails and rollback evidence.

## Deliverables

- `model_manifest.json`
- `deployment.yaml`
- `canary_metrics.csv`
- `evaluate_canary.py`
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

### Step 1 — Inspect model_manifest.json; verify model version, code SHA, data version, metrics and owner are complete

Inspect `model_manifest.json`; verify model version, code SHA, data version, metrics and owner are complete.

```bash
python3 -m json.tool model_manifest.json
```

**Check:** Record the observable result or explain the error before continuing.

### Step 2 — Review deployment.yaml; locate the champion/candidate traffic split and rollback guardrails

Review `deployment.yaml`; locate the champion/candidate traffic split and rollback guardrails.

**Check:** Record the observable result or explain the error before continuing.

### Step 3 — Run the canary evaluator against canary_metrics.csv

Run the canary evaluator against `canary_metrics.csv`.

```bash
python3 evaluate_canary.py --metrics canary_metrics.csv --config deployment.yaml
```

**Check:** Record the observable result or explain the error before continuing.

### Step 4 — Explain whether the candidate should be promoted, held or rolled back using per-version metrics

Explain whether the candidate should be promoted, held or rolled back using per-version metrics.

**Check:** Record the observable result or explain the error before continuing.

### Step 5 — Change traffic to 25% only after the 10% stage passes; never overwrite prior stage evidence

Change traffic to 25% only after the 10% stage passes; never overwrite prior stage evidence.

**Check:** Record the observable result or explain the error before continuing.

### Step 6 — Simulate a latency breach and confirm the evaluator returns a rollback decision

Simulate a latency breach and confirm the evaluator returns a rollback decision.

```bash
python3 evaluate_canary.py --metrics canary_metrics.csv --config deployment.yaml --simulate-breach
```

**Check:** Record the observable result or explain the error before continuing.

### Step 7 — Record registry ID, immutable artifact checksum, traffic split, decision and rollback test

Record registry ID, immutable artifact checksum, traffic split, decision and rollback test.

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
