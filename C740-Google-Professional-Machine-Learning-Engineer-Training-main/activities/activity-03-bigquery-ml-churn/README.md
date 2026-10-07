# Activity 03 — Train and Evaluate a BigQuery ML Churn Model

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v2.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

## Objective

Run SQL-defined logistic regression, evaluation and batch prediction on mock customer data.

## Deliverables

- `customers.csv`
- `bigquery_ml.sql`
- `evaluate_metrics.py`
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

### Step 1 — Inspect customers.csv; identify the label, entity key and any feature that could leak the outcome

Inspect `customers.csv`; identify the label, entity key and any feature that could leak the outcome.

```bash
python3 - <<'PY'
import pandas as pd
df=pd.read_csv('customers.csv'); print(df.head()); print(df.isna().sum())
PY
```

**Check:** Record the observable result or explain the error before continuing.

### Step 2 — Open bigquery_ml.sql and replace <PROJECT_ID> and <DATASET> without changing the point-in-time split

Open `bigquery_ml.sql` and replace `<PROJECT_ID>` and `<DATASET>` without changing the point-in-time split.

**Check:** Record the observable result or explain the error before continuing.

### Step 3 — Create the dataset in the same approved region as the training project

Create the dataset in the same approved region as the training project.

```bash
bq --location=asia-southeast1 mk --dataset "$PROJECT_ID:pmle_lab"
```

**Check:** Record the observable result or explain the error before continuing.

### Step 4 — Load the CSV using the declared schema or autodetect only after inspecting types

Load the CSV using the declared schema or autodetect only after inspecting types.

```bash
bq load --autodetect --source_format=CSV pmle_lab.customers customers.csv
```

**Check:** Record the observable result or explain the error before continuing.

### Step 5 — Run the CREATE MODEL statement and record the BigQuery job ID and bytes processed

Run the `CREATE MODEL` statement and record the BigQuery job ID and bytes processed.

```bash
bq query --use_legacy_sql=false < bigquery_ml.sql
```

**Check:** Record the observable result or explain the error before continuing.

### Step 6 — Query ML.EVALUATE and save accuracy, precision, recall, F1, log loss and ROC AUC

Query `ML.EVALUATE` and save accuracy, precision, recall, F1, log loss and ROC AUC.

**Check:** Record the observable result or explain the error before continuing.

### Step 7 — Run evaluate_metrics.py to compare the supplied confusion matrices at three thresholds

Run `evaluate_metrics.py` to compare the supplied confusion matrices at three thresholds.

```bash
python3 evaluate_metrics.py
```

**Check:** Record the observable result or explain the error before continuing.

### Step 8 — Choose a threshold using the stated false-negative cost, not accuracy alone, and document the rationale

Choose a threshold using the stated false-negative cost, not accuracy alone, and document the rationale.

**Check:** Record the observable result or explain the error before continuing.

### Step 9 — Run ML.PREDICT for the holdout rows and check that no post-outcome feature enters the model

Run `ML.PREDICT` for the holdout rows and check that no post-outcome feature enters the model.

**Check:** Record the observable result or explain the error before continuing.

### Step 10 — Delete the model and dataset during cleanup if the trainer does not require them for a later activity

Delete the model and dataset during cleanup if the trainer does not require them for a later activity.

```bash
bq rm -f -m pmle_lab.churn_model
```

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
