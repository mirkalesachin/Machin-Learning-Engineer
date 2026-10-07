# Activity 07 — Train a TensorFlow/Keras Model

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v2.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

## Objective

Use tf.data, a Keras network, early stopping and SavedModel verification.

## Deliverables

- `train_tensorflow.py`
- `requirements.txt`
- `expected_history.csv`
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

### Step 1 — Create a clean virtual environment and install the pinned requirements

Create a clean virtual environment and install the pinned requirements.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Check:** Record the observable result or explain the error before continuing.

### Step 2 — Open train_tensorflow.py and locate shuffle, batch, prefetch, early stopping and the export signature

Open `train_tensorflow.py` and locate `shuffle`, `batch`, `prefetch`, early stopping and the export signature.

**Check:** Record the observable result or explain the error before continuing.

### Step 3 — Run the offline training script on the generated mock dataset

Run the offline training script on the generated mock dataset.

```bash
python3 train_tensorflow.py --epochs 20 --output output/model
```

**Check:** Record the observable result or explain the error before continuing.

### Step 4 — Compare training and validation loss with expected_history.csv and identify the first overfitting epoch

Compare training and validation loss with `expected_history.csv` and identify the first overfitting epoch.

**Check:** Record the observable result or explain the error before continuing.

### Step 5 — Reload the SavedModel and score the included golden example

Reload the SavedModel and score the included golden example.

```bash
python3 train_tensorflow.py --verify-only --output output/model
```

**Check:** Record the observable result or explain the error before continuing.

### Step 6 — Change batch size once, rerun, and record throughput and validation quality rather than selecting by speed alone

Change batch size once, rerun, and record throughput and validation quality rather than selecting by speed alone.

**Check:** Record the observable result or explain the error before continuing.

### Step 7 — Save the model summary, history, evaluation metrics and signature output

Save the model summary, history, evaluation metrics and signature output.

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
