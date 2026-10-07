# Activity 16 — Investigate Drift, Bias and an ML Incident

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v2.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

## Objective

Calculate drift and slice metrics, enforce SLOs and produce an incident evidence pack.

## Deliverables

- `baseline.csv`
- `current.csv`
- `monitor.py`
- `incident_template.md`
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

### Step 1 — Inspect baseline.csv and current.csv; identify the monitored feature, outcome, prediction, group and timestamps

Inspect `baseline.csv` and `current.csv`; identify the monitored feature, outcome, prediction, group and timestamps.

**Check:** Record the observable result or explain the error before continuing.

### Step 2 — Run the monitor to calculate PSI, accuracy, group true-positive rates and p95 latency

Run the monitor to calculate PSI, accuracy, group true-positive rates and p95 latency.

```bash
python3 monitor.py --baseline baseline.csv --current current.csv --out monitoring_report.json
```

**Check:** Record the observable result or explain the error before continuing.

### Step 3 — Classify each signal as training-serving skew, data drift, concept drift, bias risk or service degradation

Classify each signal as training-serving skew, data drift, concept drift, bias risk or service degradation.

**Check:** Record the observable result or explain the error before continuing.

### Step 4 — Use persistence and minimum-sample rules before escalating; one noisy window is not sufficient evidence

Use persistence and minimum-sample rules before escalating; one noisy window is not sufficient evidence.

**Check:** Record the observable result or explain the error before continuing.

### Step 5 — Open incident_template.md; complete impact, timeline, affected versions, containment, recovery and actions

Open `incident_template.md`; complete impact, timeline, affected versions, containment, recovery and actions.

**Check:** Record the observable result or explain the error before continuing.

### Step 6 — Choose containment: rollback candidate, disable corrupt feature or scale capacity, and justify it from the evidence

Choose containment: rollback candidate, disable corrupt feature or scale capacity, and justify it from the evidence.

**Check:** Record the observable result or explain the error before continuing.

### Step 7 — Verify logs and screenshots contain no PII, tokens or full prompts

Verify logs and screenshots contain no PII, tokens or full prompts.

**Check:** Record the observable result or explain the error before continuing.

### Step 8 — Create an executive summary and a technical evidence appendix, then peer-review against A4 and A5

Create an executive summary and a technical evidence appendix, then peer-review against A4 and A5.

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
