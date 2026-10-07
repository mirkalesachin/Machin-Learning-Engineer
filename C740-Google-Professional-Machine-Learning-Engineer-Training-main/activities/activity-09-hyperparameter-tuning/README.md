# Activity 09 — Analyze Vertex AI Hyperparameter Trials

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v2.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

## Objective

Define a Vizier-style search space and select a trial using quality and cost evidence.

## Deliverables

- `trials.csv`
- `tuning_config.yaml`
- `select_trial.py`
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

### Step 1 — Review tuning_config.yaml; identify search distributions, objective direction, maximum trials and parallel trials

Review `tuning_config.yaml`; identify search distributions, objective direction, maximum trials and parallel trials.

**Check:** Record the observable result or explain the error before continuing.

### Step 2 — Inspect trials.csv for status, objective, duration and cost

Inspect `trials.csv` for status, objective, duration and cost. Exclude failed trials from the quality ranking but retain them for reliability analysis.

**Check:** Record the observable result or explain the error before continuing.

### Step 3 — Run the selector with the default quality floor and cost ceiling

Run the selector with the default quality floor and cost ceiling.

```bash
python3 select_trial.py --input trials.csv --min-auc 0.82 --max-cost 25
```

**Check:** Record the observable result or explain the error before continuing.

### Step 4 — Calculate marginal quality gain from the third to the fifth completed trial

Calculate marginal quality gain from the third to the fifth completed trial.

**Check:** Record the observable result or explain the error before continuing.

### Step 5 — Identify whether the best validation trial is likely over-searched and state why an untouched test set is required

Identify whether the best validation trial is likely over-searched and state why an untouched test set is required.

**Check:** Record the observable result or explain the error before continuing.

### Step 6 — Change the cost ceiling and explain the selected-trial change using evidence

Change the cost ceiling and explain the selected-trial change using evidence.

**Check:** Record the observable result or explain the error before continuing.

### Step 7 — Draft a final retraining configuration using the selected parameters and no tuning-only callbacks

Draft a final retraining configuration using the selected parameters and no tuning-only callbacks.

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
