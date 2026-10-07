# Activity 04 — Design an AutoML Tabular Experiment

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v2.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

## Objective

Create a dataset specification, split plan, budget and evaluation slice gate.

## Deliverables

- `automl_dataset.csv`
- `automl_config.yaml`
- `validate_splits.py`
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

### Step 1 — Profile automl_dataset.csv and confirm the target has no nulls and each split is represented

Profile `automl_dataset.csv` and confirm the target has no nulls and each split is represented.

```bash
python3 validate_splits.py automl_dataset.csv
```

**Check:** Record the observable result or explain the error before continuing.

### Step 2 — Review automl_config.yaml: objective, target, optimization metric, training budget and encryption setting

Review `automl_config.yaml`: objective, target, optimization metric, training budget and encryption setting.

**Check:** Record the observable result or explain the error before continuing.

### Step 3 — Check whether a random split is valid for the event timestamps

Check whether a random split is valid for the event timestamps. Replace it with chronological split logic if future leakage is possible.

**Check:** Record the observable result or explain the error before continuing.

### Step 4 — Define evaluation slices for region, channel and customer tenure

Define evaluation slices for region, channel and customer tenure. Set a minimum sample size for each slice.

**Check:** Record the observable result or explain the error before continuing.

### Step 5 — Estimate training cost from node-hours before starting any AutoML job

Estimate training cost from node-hours before starting any AutoML job. Obtain trainer approval for paid execution.

**Check:** Record the observable result or explain the error before continuing.

### Step 6 — In Vertex AI, create a tabular dataset only if approved; otherwise treat the configuration as a dry-run design exercise

In Vertex AI, create a tabular dataset only if approved; otherwise treat the configuration as a dry-run design exercise.

**Check:** Record the observable result or explain the error before continuing.

### Step 7 — Configure the target column and split column, then compare the console summary with the YAML design

Configure the target column and split column, then compare the console summary with the YAML design.

**Check:** Record the observable result or explain the error before continuing.

### Step 8 — After training, record model evaluation, feature attributions, slice results and training budget used

After training, record model evaluation, feature attributions, slice results and training budget used.

**Check:** Record the observable result or explain the error before continuing.

### Step 9 — Write a go/no-go decision

Write a go/no-go decision. A high aggregate score cannot override a failed critical slice.

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
