# Google Professional Machine Learning Engineer Training — Learner Guide

**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Training provider:** Tertiary Infotech Academy Pte Ltd · UEN 201200696W

> This Learner Guide contains the detailed step-by-step procedures. The slide deck is mechanism-led and intentionally omits click-by-click instructions.

## Document Version Control Record

| Version | Release date | Summary of changes | Author |
|---|---|---|---|
| 7.0 | Legacy release | Original 89-slide course deck and legacy topic coverage. | Tertiary Infotech Academy |
| 8.0 | 12 September 2026 | Rebuilt against the current six-domain Google PMLE exam guide; 415-slide visual deck; 16 self-contained Activities; detailed Google Cloud account/Console setup; current Vertex AI, BigQuery ML, TensorFlow, serving, MLOps, responsible AI and monitoring content. | Dr Alfred Ang |

## Course Learning Outcomes

- LO1: Assess and draft Google Cloud solution specifications to meet expected business machine learning requirements.
- LO2: Develop implementation plans and resolve issues for Google Cloud machine learning solutions.
- LO3: Develop and review processes for metrics associated with Google Cloud machine learning solution implementation.

## How to Use This Guide

1. Read the relevant domain mechanism before its Activity.
2. Work from the Activity folder so relative paths are predictable.
3. Use mock data first. Execute paid Google Cloud resources only with trainer approval.
4. Preserve evidence: configuration, job/revision ID, metrics, decision and cleanup result.
5. Never place credentials, service-account keys, personal data or production prompts in the evidence pack.

## Current Google PMLE Exam Domains

The course follows the official Google Cloud Professional Machine Learning Engineer exam guide current on the release date. Approximate weights total about 101% because Google publishes rounded values.

- **Domain 1 — Architecting low-code AI solutions (~13%)**. Legacy coverage: Topics 1–3: GCP fundamentals, Google ML services, ML workflow.
- **Domain 2 — Collaborating to manage data and models (~16%)**. Legacy coverage: Topics 1, 3 and 5: big data, data quality, feature engineering.
- **Domain 3 — Scaling prototypes into ML models (~21%)**. Legacy coverage: Topics 4–6: TensorFlow, feature engineering, enterprise ML.
- **Domain 4 — Serving and scaling models (~20%)**. Legacy coverage: Topics 6–7: batch/online prediction, production systems.
- **Domain 5 — Automating and orchestrating ML pipelines (~18%)**. Legacy coverage: Topic 8: MLOps, CI/CD and repeatable workflows.
- **Domain 6 — Monitoring AI solutions (~13%)**. Legacy coverage: Topics 6–8: testing, monitoring, troubleshooting and MLOps.

## Technical Reference Chapters

## Domain 1 — Architecting low-code AI solutions (~13%)

Topics 1–3: GCP fundamentals, Google ML services, ML workflow.

### BigQuery ML model selection

**Mechanism flow**

Business question → BigQuery table → CREATE MODEL → ML.EVALUATE → ML.PREDICT

**Service or method decision**

- **Logistic regression** — binary outcome with calibrated probability
- **Boosted trees** — non-linear tabular relationships
- **ARIMA_PLUS** — forecasting with seasonality

**Runnable configuration pattern**

```text
CREATE OR REPLACE MODEL `ml.churn`
OPTIONS(model_type='LOGISTIC_REG', input_label_cols=['churned']) AS
SELECT * EXCEPT(customer_id) FROM `ml.customer_features`;
```

**Metric:** Precision–recall trade-off  
**Formula/decision rule:** `precision = TP/(TP+FP); recall = TP/(TP+FN)`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| High accuracy, poor recall | class imbalance | use PR AUC and class weights |
| Query cost spike | unbounded scans | partition, cluster and select columns |
| Leakage | post-outcome feature | point-in-time feature review |

**Evidence chain**

- SQL text and job ID
- ML.EVALUATE result
- confusion matrix
- model metadata and labels

**Exam-style decision case**

A retailer needs churn scores from 40 TB already in BigQuery with no custom serving code.

**Best decision:** Use BigQuery ML; keep training and scoring beside governed data and batch predictions.

**Related practical:** Activity 03

### AutoML tabular workflow

**Mechanism flow**

Schema → Target → Train split → Budget → Evaluate → Register

**Service or method decision**

- **AutoML** — strong baseline and limited ML engineering capacity
- **Custom training** — custom loss or architecture
- **BigQuery ML** — SQL team and warehouse-resident data

**Runnable configuration pattern**

```text
gcloud ai models upload --region=$REGION --display-name=churn-automl \
+  --container-image-uri=$PREDICTION_IMAGE --artifact-uri=$MODEL_DIR
```

**Metric:** Training budget curve  
**Formula/decision rule:** `marginal gain = metric(t)-metric(t-1)`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Invalid target | nulls or unsupported label | profile and clean label |
| Weak validation | random split on temporal data | use time-aware split |
| Over-budget | no stopping criterion | cap node hours and monitor marginal gain |

**Evidence chain**

- dataset schema
- split manifest
- training budget
- evaluation slices
- registered model version

**Exam-style decision case**

A lending team needs a governed risk baseline quickly, but predictions must be explainable by segment.

**Best decision:** Start with AutoML tabular, require slice metrics and feature attributions before deployment.

**Related practical:** Activity 04

### Google Cloud AI APIs

**Mechanism flow**

Content → Auth → API request → Structured response → Human review

**Service or method decision**

- **Document AI** — forms, invoices and OCR structure
- **Vision API** — labels, OCR and image properties
- **Translate API** — managed multilingual translation

**Runnable configuration pattern**

```text
curl -s -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
+  -H 'Content-Type: application/json' \
+  "https://vision.googleapis.com/v1/images:annotate" -d @request.json
```

**Metric:** API confidence threshold  
**Formula/decision rule:** `review_rate = count(score < threshold)/N`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| 403 | API disabled or IAM missing | enable API; grant narrow role |
| 429 | quota exhausted | backoff, batch, request quota |
| Low confidence | domain mismatch | human review or custom model |

**Evidence chain**

- request JSON
- HTTP status
- operation ID
- confidence distribution
- review log

**Exam-style decision case**

An insurer must extract line items from varied claim forms and retain reviewer evidence.

**Best decision:** Use Document AI processor plus confidence-based human review; do not build OCR from scratch.

**Related practical:** Activity 05

### Model Garden and foundation model selection

**Mechanism flow**

Task → Constraints → Candidate models → Evaluation set → Endpoint

**Service or method decision**

- **Gemini managed model** — multimodal and managed operations
- **Open model** — weight control or special license needs
- **Specialized API** — narrow commodity capability

**Runnable configuration pattern**

```text
MODEL_ID='gemini-2.5-flash'
P95_MS=850
MAX_COST_PER_1K=0.020
SAFETY='BLOCK_MEDIUM_AND_ABOVE'
```

**Metric:** Utility score  
**Formula/decision rule:** `0.45*quality - 0.25*cost - 0.20*latency + 0.10*availability`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Benchmark mismatch | public task differs | use production-like eval set |
| License risk | terms not reviewed | legal and model-card review |
| Region gap | model unavailable | confirm region before design |

**Evidence chain**

- candidate matrix
- model card
- evaluation dataset
- quality/cost/latency report
- approval record

**Exam-style decision case**

A support assistant must ground answers in policy PDFs with sub-second median response.

**Best decision:** Evaluate managed Gemini candidates on groundedness, latency and cost; select by measured SLOs.

**Related practical:** Activity 02

### Gemini tuning with BigQuery

**Mechanism flow**

Curate examples → Split → Tune → Evaluate → Publish

**Service or method decision**

- **Prompt only** — behavior adjustable with instructions
- **Supervised tuning** — stable style/task examples
- **RAG** — facts change and citations matter

**Runnable configuration pattern**

```text
SELECT input_text, output_text
FROM `genai.tuning_examples`
WHERE approved = TRUE AND split IN ('TRAIN','VALIDATION');
```

**Metric:** Tuning generalization gap  
**Formula/decision rule:** `gap = train_score - validation_score`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Memorization | duplicates or tiny set | deduplicate and widen validation |
| Unsafe output | bad examples | curation and safety eval |
| No gain | task is knowledge-bound | use RAG instead |

**Evidence chain**

- approved tuning table
- data lineage
- base/tuned comparison
- safety results
- versioned endpoint

**Exam-style decision case**

A legal drafting model must follow a house style, while statute facts remain retrieval-grounded.

**Best decision:** Tune for stable style and use RAG for changing legal facts; evaluate each separately.

**Related practical:** Activity 04

### Prompt and context engineering

**Mechanism flow**

System instruction → Retrieved context → User task → Tool call → Grounded answer

**Service or method decision**

- **Few-shot** — stable pattern with representative examples
- **RAG** — current private knowledge
- **Tool use** — actions or authoritative calculations

**Runnable configuration pattern**

```text
SYSTEM='Use only supplied context; cite source_id.'
CONTEXT_TOP_K=5
TEMPERATURE=0.1
MAX_OUTPUT_TOKENS=800
```

**Metric:** Groundedness by retrieval depth  
**Formula/decision rule:** `grounded = supported_claims / total_claims`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Hallucination | context missing or ignored | abstain and require citations |
| Prompt injection | untrusted retrieved text | isolate instructions from data |
| Context bloat | too many chunks | rerank and cap tokens |

**Evidence chain**

- prompt template
- retrieval trace
- tool-call log
- citation coverage
- red-team cases

**Exam-style decision case**

An internal HR assistant must answer only from approved policies and refuse missing-policy questions.

**Best decision:** Use RAG with instruction/data separation, citation checks, and a tested abstention path.

**Related practical:** Activity 02

### Responsible low-code design

**Mechanism flow**

Stakeholders → Harms → Slices → Controls → Monitoring → Appeal

**Service or method decision**

- **Human-in-loop** — high-impact or uncertain decisions
- **Human-on-loop** — automated low-risk with review
- **Automated** — reversible, validated low-harm tasks

**Runnable configuration pattern**

```text
slices = ['region','age_band','channel']
max_tpr_gap = 0.05
min_group_n = 100
require_appeal = True
```

**Metric:** Equal opportunity gap  
**Formula/decision rule:** `max(TPR_group)-min(TPR_group)`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Hidden disparity | aggregate-only metric | slice evaluation |
| Automation bias | no override | human authority and appeal |
| Purpose creep | reused prediction | use limitation and review |

**Evidence chain**

- impact assessment
- slice metrics
- data card
- human-review SOP
- appeal and incident log

**Exam-style decision case**

A model prioritizes public-service cases where false negatives have unequal community impact.

**Best decision:** Require human review, group metrics, documented thresholds and a usable appeal process.

**Related practical:** Activity 16

### Cost, latency and availability architecture

**Mechanism flow**

Demand → SLO → Capacity model → Region → Caching → Fallback

**Service or method decision**

- **Batch** — large volume without immediate response
- **Online endpoint** — predictable low latency
- **Serverless** — bursty stateless inference

**Runnable configuration pattern**

```text
target_p95_ms: 300
min_replicas: 2
max_replicas: 20
cache_ttl_s: 900
regional_failover: true
```

**Metric:** Capacity headroom  
**Formula/decision rule:** `headroom = 1 - peak_qps/max_qps`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Tail latency | cold starts or saturation | min replicas and load test |
| High cost | oversized accelerator | profile and right-size |
| Regional outage | single region | tested fallback design |

**Evidence chain**

- SLO
- load-test curve
- cost estimate
- quota check
- failover test evidence

**Exam-style decision case**

A recommendation API sees 10x campaign bursts and must sustain 99.9% monthly availability.

**Best decision:** Use autoscaled online serving with minimum warm capacity, cached features and tested regional fallback.

**Related practical:** Activity 02

## Domain 2 — Collaborating to manage data and models (~16%)

Topics 1, 3 and 5: big data, data quality, feature engineering.

### Data organization by modality

**Mechanism flow**

Sources → Landing zone → Curated tables → Feature views → Training snapshots

**Service or method decision**

- **BigQuery** — structured analytics and SQL
- **Cloud Storage** — large unstructured objects
- **BigLake** — governed access across lakes and warehouses

**Runnable configuration pattern**

```text
gsutil -m cp data/images/*.jpg gs://$BUCKET/raw/images/
bq load --autodetect --source_format=CSV ml.customers gs://$BUCKET/raw/customers.csv
```

**Metric:** Freshness lag  
**Formula/decision rule:** `lag = ingestion_time - event_time`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Schema drift | producer changed fields | contract checks |
| Duplicate entities | weak keys | deduplicate by event id |
| Training skew | mutable source | snapshot and version |

**Evidence chain**

- bucket layout
- table schema
- partition stats
- snapshot timestamp
- lineage graph

**Exam-style decision case**

A multimodal claims model uses PDFs, images and tabular policy history from three teams.

**Best decision:** Land objects in Cloud Storage, curated entities in BigQuery, and bind a point-in-time training manifest.

**Related practical:** Activity 06

### Preprocessing tool selection

**Mechanism flow**

Volume → Transform → Latency → State → Runner → Output

**Service or method decision**

- **pandas/sklearn** — fits memory and iteration speed matters
- **Dataflow** — managed Beam batch/stream pipelines
- **Spark** — existing distributed Spark ecosystem

**Runnable configuration pattern**

```text
with beam.Pipeline(options=opts) as p:
  rows = p | beam.io.ReadFromText(uri)
  clean = rows | beam.Map(validate_and_transform)
  clean | beam.io.WriteToBigQuery(table)
```

**Metric:** Throughput vs workers  
**Formula/decision rule:** `records_per_s = processed / elapsed_s`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| OOM | in-memory transform too large | distributed runner |
| Late data | watermark misconfigured | event-time windows |
| Hot key | skewed grouping | fan-out or rekey |

**Evidence chain**

- data profile
- runner graph
- worker metrics
- dead-letter table
- reconciliation count

**Exam-style decision case**

A 2 TB daily feed joins clickstream windows and must finish before a 06:00 training job.

**Best decision:** Use Dataflow batch with autoscaling, dead-letter handling and a measured completion SLO.

**Related practical:** Activity 06

### Feature engineering and selection

**Mechanism flow**

Raw columns → Transforms → Candidate features → Selection → Validated matrix

**Service or method decision**

- **Standardization** — linear and distance models
- **Vocabulary/embedding** — high-cardinality text
- **Cross feature** — known interaction with bounded cardinality

**Runnable configuration pattern**

```text
preprocess = ColumnTransformer([
 ('num', StandardScaler(), numeric),
 ('cat', OneHotEncoder(handle_unknown='ignore'), categorical)])
```

**Metric:** Validation AUC by feature set  
**Formula/decision rule:** `lift = AUC_candidate - AUC_baseline`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Leakage | future value encoded | time-aware review |
| Cardinality blow-up | unbounded categories | hash or vocabulary cap |
| Train/serve mismatch | duplicate code | shared transform artifact |

**Evidence chain**

- feature definitions
- fit statistics
- selection report
- schema signature
- unit tests

**Exam-style decision case**

A fraud model sees merchant IDs never observed during training and drifts by region.

**Best decision:** Use unknown-safe categorical encoding, region slices and versioned preprocessing artifacts.

**Related practical:** Activity 06

### Feature Store architecture

**Mechanism flow**

Batch sources → Feature pipeline → Offline store → Online store → Entity lookup → Model

**Service or method decision**

- **Offline features** — training and batch scoring
- **Online features** — low-latency current values
- **Embedding retrieval** — nearest-neighbor similarity

**Runnable configuration pattern**

```text
entity_id: customer_id
feature_view: customer_realtime
features: [txn_count_1h, spend_7d, risk_score]
online_ttl: 3600
```

**Metric:** Online feature freshness  
**Formula/decision rule:** `freshness = now - feature_timestamp`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Stale feature | pipeline lag | freshness alert |
| Wrong entity | key mismatch | contract and lookup test |
| Point-in-time leak | latest-value join | as-of join |

**Evidence chain**

- feature registry
- entity schema
- materialization job
- freshness dashboard
- point-in-time test

**Exam-style decision case**

A real-time fraud endpoint needs 50 ms feature lookups and reproducible historical training values.

**Best decision:** Use online and offline feature paths with one definition and explicit point-in-time correctness tests.

**Related practical:** Activity 11

### Privacy and sensitive-data controls

**Mechanism flow**

Discover → Classify → Minimize → Protect → Authorize → Audit

**Service or method decision**

- **DLP inspection** — discover PII at scale
- **Tokenization** — retain joins without clear identifiers
- **Aggregation** — reduce re-identification risk

**Runnable configuration pattern**

```text
gcloud dlp jobs create inspect pii-scan --location=global \
+  --storage-config-file=storage.json --inspect-config-file=inspect.json
```

**Metric:** PII exposure rate  
**Formula/decision rule:** `exposure = unprotected_sensitive_fields / sensitive_fields`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Open bucket | inherited broad role | least privilege and policy scan |
| PII in notebook | local export | managed storage and VPC controls |
| Log leakage | payload logging | redact before logging |

**Evidence chain**

- DLP findings
- classification tags
- IAM policy
- encryption key record
- audit log query

**Exam-style decision case**

A healthcare team shares a training dataset across projects while patient identifiers must not leave a boundary.

**Best decision:** De-identify, tokenize approved join keys, restrict perimeters and verify access in audit logs.

**Related practical:** Activity 01

### Secure Workbench and Colab Enterprise

**Mechanism flow**

Identity → Network → Runtime → Repository → Artifact store → Shutdown

**Service or method decision**

- **Workbench managed notebook** — integrated Vertex AI and controlled project
- **Colab Enterprise** — managed collaborative notebooks
- **Local notebook** — only for non-sensitive lightweight work

**Runnable configuration pattern**

```text
disable_public_ip: true
service_account: ml-dev@$PROJECT.iam.gserviceaccount.com
idle_shutdown_minutes: 60
repository: approved-ml-repo
```

**Metric:** Idle compute waste  
**Formula/decision rule:** `waste = idle_instance_hours / total_instance_hours`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Credential sprawl | user keys in cells | service account and ADC |
| Data exfiltration | public egress | private IP and perimeter |
| Cost leak | notebook left on | idle shutdown |

**Evidence chain**

- runtime configuration
- IAM binding
- network route
- repository commit
- shutdown event

**Exam-style decision case**

A regulated analytics team needs collaborative GPUs without public IPs or downloaded service-account keys.

**Best decision:** Use managed notebooks with private networking, attached least-privilege identity and idle shutdown.

**Related practical:** Activity 01

### Experiment tracking and lineage

**Mechanism flow**

Run config → Dataset version → Training job → Metrics → Artifact → Registry

**Service or method decision**

- **Vertex AI Experiments** — managed run comparison
- **ML Metadata** — pipeline lineage
- **Git + manifest** — code and configuration provenance

**Runnable configuration pattern**

```text
run.log_params({'lr':0.001,'batch_size':128,'data_uri':DATA_URI})
run.log_metrics({'val_auc':0.842,'val_loss':0.391})
```

**Metric:** Validation AUC by run  
**Formula/decision rule:** `best = argmax(metric subject to fairness and latency gates)`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Unrepeatable run | missing dataset version | immutable URI and manifest |
| Metric cherry-pick | no primary metric | pre-register gates |
| Artifact orphan | manual upload | pipeline metadata |

**Evidence chain**

- commit SHA
- dataset URI
- parameter set
- metrics
- model artifact checksum

**Exam-style decision case**

Two teams report different best models because they trained on mutable tables and recorded only accuracy.

**Best decision:** Bind runs to immutable data and code, predefine metrics, and compare through one experiment tracker.

**Related practical:** Activity 09

### Predictive and gen AI evaluation

**Mechanism flow**

Task rubric → Gold set → Automated metrics → Slice review → Human review → Release gate

**Service or method decision**

- **Classification metrics** — labeled predictive outcomes
- **LLM-as-judge** — scaled rubric scoring with calibration
- **Human evaluation** — high-stakes nuance and preference

**Runnable configuration pattern**

```text
rubric = {'groundedness':0.35,'correctness':0.35,'safety':0.20,'style':0.10}
release_if = 'score>=0.82 and safety_violations==0'
```

**Metric:** Evaluation agreement  
**Formula/decision rule:** `agreement = matching_ratings / reviewed_items`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Judge bias | uncalibrated model judge | human calibration sample |
| Contamination | eval in tuning set | holdout governance |
| Aggregate masking | no slices | report by task and risk |

**Evidence chain**

- rubric version
- gold-set manifest
- metric results
- reviewer adjudication
- release decision

**Exam-style decision case**

A gen-AI summarizer improves ROUGE but starts omitting critical contraindications in one document type.

**Best decision:** Use risk-weighted rubric, document-type slices and human adjudication; block release on critical omissions.

**Related practical:** Activity 16

## Domain 3 — Scaling prototypes into ML models (~21%)

Topics 4–6: TensorFlow, feature engineering, enterprise ML.

### Model type and product decision

**Mechanism flow**

Task → Data → Constraints → Baseline → Candidate → Decision

**Service or method decision**

- **ARIMA_PLUS** — interpretable time-series forecast
- **DNN** — large nonlinear supervised task
- **LLM** — language generation or reasoning

**Runnable configuration pattern**

```text
decision = {'task':'forecast','horizon_days':30,'need_intervals':True,
            'product':'BigQuery ML ARIMA_PLUS'}
```

**Metric:** Decision utility  
**Formula/decision rule:** `utility = quality - cost_penalty - latency_penalty - risk_penalty`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Over-complex model | baseline omitted | establish simple baseline |
| Wrong metric | business loss ignored | map metric to decision |
| Unclear ownership | product mismatch | operating-model review |

**Evidence chain**

- requirements matrix
- baseline result
- candidate benchmark
- risk review
- architecture decision record

**Exam-style decision case**

A planner needs 30-day demand intervals from structured history and must explain seasonality.

**Best decision:** Choose ARIMA_PLUS in BigQuery ML before a DNN; validate interval coverage and holiday effects.

**Related practical:** Activity 02

### Training data ingestion

**Mechanism flow**

Source → Validation → Shard → Cache → Worker pool → Checkpoint

**Service or method decision**

- **Cloud Storage shards** — images, text and TFRecord
- **BigQuery export** — warehouse-managed tabular data
- **Streaming ingest** — continuous examples with later snapshot

**Runnable configuration pattern**

```text
gcloud storage cp gs://$BUCKET/manifests/train-*.jsonl ./manifests/
python validate_manifest.py --schema schema.json --input manifests/
```

**Metric:** Input pipeline utilization  
**Formula/decision rule:** `utilization = data_wait_free_step_time / total_step_time`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Workers starve | tiny unshuffled files | shard and parallel-read |
| Corrupt examples | no validation | fail-fast schema checks |
| Nonrepeatable split | random at runtime | persist split manifest |

**Evidence chain**

- manifest
- schema report
- shard counts
- input throughput
- checkpoint URI

**Exam-style decision case**

A vision job uses 12 million images and GPUs idle while workers open millions of tiny files.

**Best decision:** Create balanced shards, parallel reads and prefetch; measure accelerator utilization and input wait.

**Related practical:** Activity 10

### TensorFlow and Keras training

**Mechanism flow**

tf.data → Preprocess → Keras model → Fit → Evaluate → SavedModel

**Service or method decision**

- **Sequential API** — single-input linear stack
- **Functional API** — multi-input or branching graph
- **Subclassing** — custom behavior requiring code control

**Runnable configuration pattern**

```text
ds = tf.data.Dataset.from_tensor_slices((X,y)).shuffle(10000).batch(128).prefetch(tf.data.AUTOTUNE)
model.fit(ds, epochs=20, callbacks=[early_stop])
```

**Metric:** Validation loss  
**Formula/decision rule:** `stop when val_loss fails to improve for patience epochs`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Overfit | training continues after val plateau | early stopping |
| Slow input | no prefetch | AUTOTUNE pipeline |
| Serving failure | custom op missing | export and load test |

**Evidence chain**

- model summary
- training history
- validation metrics
- SavedModel signature
- reload test

**Exam-style decision case**

A tabular neural network improves training loss but validation loss rises after epoch 12.

**Best decision:** Use early stopping and regularization, then verify the exported signature with held-out examples.

**Related practical:** Activity 07

### Vertex AI custom training

**Mechanism flow**

Package/container → Artifact Registry → CustomJob → Worker pool → GCS output → Model Registry

**Service or method decision**

- **Prebuilt container** — supported framework and conventional entry point
- **Custom container** — system packages or custom runtime
- **Custom training package** — Python package on managed image

**Runnable configuration pattern**

```text
gcloud ai custom-jobs create --region=$REGION --display-name=churn-train \
+ --config=config/custom_job.yaml
```

**Metric:** Training cost per successful run  
**Formula/decision rule:** `cost_success = total_job_cost / successful_jobs`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Module not found | package omitted dependency | lock and build image |
| Permission denied | training SA lacks access | least-privilege roles |
| No artifact | wrong AIP_MODEL_DIR | write to managed output URI |

**Evidence chain**

- image digest
- custom job spec
- service account
- Cloud Logging trace
- artifact checksum

**Exam-style decision case**

A sklearn pipeline requires a native library unavailable in Vertex prebuilt images.

**Best decision:** Use a custom container pinned by digest and test it locally before CustomJob submission.

**Related practical:** Activity 08

### Hyperparameter tuning

**Mechanism flow**

Search space → Trials → Objective → Early stop → Best trial → Retrain

**Service or method decision**

- **Grid** — small discrete exhaustive space
- **Random** — broad mixed space
- **Bayesian/Vizier** — expensive trials with guided search

**Runnable configuration pattern**

```text
metric_spec: {val_auc: maximize}
parameters:
- {parameterId: learning_rate, doubleValueSpec: {minValue: 0.0001, maxValue: 0.1, scaleType: UNIT_LOG_SCALE}}
```

**Metric:** Best objective by trial  
**Formula/decision rule:** `best_n = max(metric_1...metric_n)`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Wrong objective | metric name mismatch | emit exact metric |
| Budget waste | poor trials run fully | early stopping |
| Overfit to validation | too many searches | final untouched test |

**Evidence chain**

- search-space spec
- trial logs
- objective series
- best parameters
- test-set confirmation

**Exam-style decision case**

A DNN training run costs $80; the team needs learning rate, depth and dropout optimization.

**Best decision:** Use Vizier/Bayesian search with log-scaled learning rate, early stopping and an untouched final test.

**Related practical:** Activity 09

### Foundation model fine-tuning

**Mechanism flow**

Task fit → Data curation → Adapter/tune → Safety eval → Quality eval → Deploy

**Service or method decision**

- **Prompt/RAG** — knowledge or instruction gap
- **Adapter tuning** — task style with modest data
- **Full fine-tune** — rarely justified; high control and cost

**Runnable configuration pattern**

```text
train.jsonl: {'input_text':'...','output_text':'...'}
validation.jsonl: {'input_text':'...','output_text':'...'}
max_duplicate_rate: 0.01
```

**Metric:** Quality vs training examples  
**Formula/decision rule:** `gain = tuned_score - base_score`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Catastrophic behavior | poor examples | curate and safety-gate |
| No factual freshness | tuning used for knowledge | use retrieval |
| Sensitive memorization | PII in examples | DLP and dedup |

**Evidence chain**

- data approval
- base/tuned eval
- safety red-team
- training lineage
- deployment rollback

**Exam-style decision case**

A service needs consistent structured incident summaries but incident facts change every minute.

**Best decision:** Tune structure/style only; retrieve live facts and block memorization-prone sensitive examples.

**Related practical:** Activity 16

### CPU, GPU and TPU selection

**Mechanism flow**

Profile → Ops → Memory → Precision → Throughput → Cost

**Service or method decision**

- **CPU** — small classical models and irregular control flow
- **GPU** — broad deep-learning ecosystem
- **TPU** — large TensorFlow/JAX workloads optimized for matrix ops

**Runnable configuration pattern**

```text
acceleratorType: NVIDIA_TESLA_T4
acceleratorCount: 2
machineSpec: {machineType: n1-standard-16}
replicaCount: 1
```

**Metric:** Examples per dollar  
**Formula/decision rule:** `efficiency = examples_per_second / hourly_cost`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| OOM | batch/model exceeds memory | gradient accumulation or larger device |
| Low utilization | input bottleneck | profile pipeline |
| Quota error | accelerator unavailable | reserve quota or alternate region |

**Evidence chain**

- profiler trace
- memory peak
- throughput test
- quota record
- cost benchmark

**Exam-style decision case**

A transformer fits on one GPU but throughput misses the nightly window by 3x.

**Best decision:** Profile first; compare larger GPU and data-parallel options by examples per dollar and deadline.

**Related practical:** Activity 10

### Distributed training

**Mechanism flow**

Sharded data → Workers → All-reduce → Optimizer → Checkpoint → Restart

**Service or method decision**

- **Data parallel** — replicate model; split batches
- **Model parallel** — split model too large for one device
- **Parameter server** — asynchronous large-scale pattern

**Runnable configuration pattern**

```text
python -m torch.distributed.run --nproc_per_node=4 train.py \
+  --backend nccl --checkpoint_uri gs://$BUCKET/checkpoints
```

**Metric:** Scaling efficiency  
**Formula/decision rule:** `efficiency = speedup / worker_count`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Hang | rank/network mismatch | validate rendezvous and ports |
| Divergence | effective batch changed | scale learning rate |
| Lost work | no frequent checkpoint | checkpoint to durable GCS |

**Evidence chain**

- worker-pool spec
- rank logs
- throughput curve
- checkpoint list
- restart test

**Exam-style decision case**

An ImageNet job must scale from 1 to 8 GPUs and survive preemptible worker loss.

**Best decision:** Use torchrun data parallelism, durable checkpoints and measure scaling efficiency before adding workers.

**Related practical:** Activity 10

## Domain 4 — Serving and scaling models (~20%)

Topics 6–7: batch/online prediction, production systems.

### Batch versus online inference

**Mechanism flow**

Input contract → Preprocess → Model → Postprocess → Sink → SLA

**Service or method decision**

- **Batch prediction** — asynchronous high-volume jobs
- **Online endpoint** — interactive low-latency requests
- **Streaming** — continuous events with bounded delay

**Runnable configuration pattern**

```text
gcloud ai batch-prediction-jobs create --region=$REGION --model=$MODEL_ID \
+ --jsonl-request=gcsSource.uris=gs://$BUCKET/requests.jsonl \
+ --jsonl-output=gcsDestination.outputUriPrefix=gs://$BUCKET/predictions/
```

**Metric:** Cost per 1,000 predictions  
**Formula/decision rule:** `cost_1k = total_serving_cost / predictions * 1000`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Timeout | online used for huge payload | batch job |
| Stale output | batch schedule late | freshness SLO |
| Duplicate score | retries not idempotent | request IDs |

**Evidence chain**

- request schema
- job ID
- input/output counts
- latency distribution
- cost report

**Exam-style decision case**

Marketing needs 50 million nightly scores; the UI needs only the latest stored score.

**Best decision:** Use batch prediction to a governed table; serve the stored score rather than 50 million online calls.

**Related practical:** Activity 12

### Prebuilt and custom serving containers

**Mechanism flow**

Artifact → Container → Health route → Predict route → Endpoint → Probe

**Service or method decision**

- **Prebuilt** — supported framework and signature
- **Custom** — custom dependencies or server
- **Cloud Run container** — portable stateless HTTP serving

**Runnable configuration pattern**

```text
FROM python:3.11-slim
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py model.joblib ./
CMD ["gunicorn","-b",":8080","app:app"]
```

**Metric:** Container startup time  
**Formula/decision rule:** `startup = ready_timestamp - instance_start`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| CrashLoop | bad command or missing file | local container smoke test |
| Unhealthy | wrong probe path/port | implement health route |
| ABI error | runtime mismatch | pin base image and wheels |

**Evidence chain**

- Dockerfile
- image digest
- SBOM
- health response
- prediction contract test

**Exam-style decision case**

An XGBoost model requires custom preprocessing and a native package not in prebuilt serving images.

**Best decision:** Build a minimal custom image, pin the digest, generate an SBOM and probe health/predict routes.

**Related practical:** Activity 13

### Model Registry and versioning

**Mechanism flow**

Train → Evaluate → Register → Alias → Deploy → Retire

**Service or method decision**

- **Version** — immutable model artifact generation
- **Alias** — movable label such as champion
- **Lineage** — data/code/run relation

**Runnable configuration pattern**

```text
model_labels = {'git_sha':GIT_SHA,'data_version':DATA_VER,'owner':'risk-ml'}
model_alias = 'candidate'
```

**Metric:** Rollback time  
**Formula/decision rule:** `MTTR = restore_time - incident_start`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Unknown model | manual file copied | registry-only deployment |
| Wrong alias | unreviewed promotion | approval gate |
| No rollback | old version deleted | retain validated prior version |

**Evidence chain**

- registry version
- labels
- evaluation report
- promotion approval
- rollback drill

**Exam-style decision case**

A model release must be traceable to code and data, and rollback must finish within 15 minutes.

**Best decision:** Register immutable versions with lineage labels; promote aliases only after gates and drill rollback.

**Related practical:** Activity 12

### Canary and A/B rollout

**Mechanism flow**

Baseline → Candidate → Traffic split → Guardrails → Decision → Promote/Rollback

**Service or method decision**

- **Canary** — risk-limited technical validation
- **A/B** — compare user/business outcomes
- **Shadow** — observe candidate without affecting users

**Runnable configuration pattern**

```text
trafficSplit:
  deployedModels:
    champion: 90
    candidate: 10
rollback_if: 'p95_ms > 300 or error_rate > 0.01'
```

**Metric:** Canary error rate  
**Formula/decision rule:** `error_rate = failed_requests / total_requests`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Biased sample | non-random routing | stable random assignment |
| Slow rollback | manual process | automated guardrail |
| Metric dilution | aggregate traffic | per-version metrics |

**Evidence chain**

- traffic config
- version-tagged logs
- guardrail dashboard
- decision record
- rollback event

**Exam-style decision case**

A new ranking model improves offline NDCG but has unknown tail latency at peak traffic.

**Best decision:** Start with shadow then 10% canary; gate on version-specific latency, errors and business metric.

**Related practical:** Activity 12

### Inference preprocessing and postprocessing

**Mechanism flow**

Validate request → Transform → Predict → Calibrate → Business rule → Response

**Service or method decision**

- **In-container transform** — tight coupling and low latency
- **Pipeline transform** — shared batch/online code
- **Feature Store** — central online feature retrieval

**Runnable configuration pattern**

```text
assert request['schema_version']=='3'
x = transformer.transform([request['features']])
p = calibrator.predict_proba(x)[0,1]
return {'risk':float(p),'model_version':VERSION}
```

**Metric:** Training-serving skew  
**Formula/decision rule:** `skew = distance(train_feature, serving_feature)`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Shape error | schema changed | versioned contract |
| Probability drift | calibrator omitted | bundle postprocessor |
| Silent default | missing feature filled | reject or explicit missingness |

**Evidence chain**

- JSON schema
- transform checksum
- golden request
- prediction diff test
- response version

**Exam-style decision case**

The same raw input scores 0.22 offline and 0.71 online after a preprocessing refactor.

**Best decision:** Compare transformation artifacts and golden requests; deploy preprocessing with the model version.

**Related practical:** Activity 13

### Public and private endpoints

**Mechanism flow**

Client → DNS → Identity → Network path → Endpoint → Audit

**Service or method decision**

- **Public endpoint** — internet path with IAM/auth controls
- **Private Service Connect** — private VPC consumption
- **Cloud Run ingress** — service-to-service serverless

**Runnable configuration pattern**

```text
ingress: internal
authentication: iam
psc_network: projects/$PROJECT/global/networks/ml-vpc
log_requests: metadata_only
```

**Metric:** Unauthorized request rate  
**Formula/decision rule:** `denied / total requests`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| 403 | caller identity lacks invoke | grant narrow invoker |
| No route | PSC/DNS misconfigured | validate endpoint and DNS |
| Data leak | payload logs | metadata-only logging |

**Evidence chain**

- network diagram
- IAM policy
- DNS resolution
- connectivity test
- audit log

**Exam-style decision case**

A bank model endpoint must be reachable from two VPCs and never expose public ingress.

**Best decision:** Use private connectivity, service identities and end-to-end connectivity plus audit tests.

**Related practical:** Activity 12

### Autoscaling and serving hardware

**Mechanism flow**

Load test → Concurrency → Replica floor → Scale signal → Accelerator → SLO

**Service or method decision**

- **CPU autoscale** — lightweight model and variable demand
- **GPU endpoint** — high-throughput deep learning
- **Edge** — connectivity or privacy requires local inference

**Runnable configuration pattern**

```text
minReplicaCount: 2
maxReplicaCount: 12
targetCpuUtilization: 60
acceleratorType: NVIDIA_TESLA_T4
```

**Metric:** p95 latency by QPS  
**Formula/decision rule:** `p95 = percentile(latency_ms,95)`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Cold-start spike | scale from zero | warm floor |
| Queue growth | concurrency too high | capacity test |
| GPU idle | small batches | dynamic batching or CPU |

**Evidence chain**

- load script
- QPS/latency curve
- replica timeline
- utilization
- capacity decision

**Exam-style decision case**

A vision API must handle 5–80 QPS with p95 below 300 ms and control GPU cost.

**Best decision:** Benchmark CPU/GPU, set a warm floor and autoscale from measured saturation—not guesses.

**Related practical:** Activity 13

### Cloud Run and GKE serving

**Mechanism flow**

Image → Registry → Runtime → Service/Deployment → Autoscale → Observe

**Service or method decision**

- **Cloud Run** — stateless HTTP, rapid ops, bursty load
- **GKE** — custom networking, sidecars, accelerators or orchestration
- **Vertex endpoint** — managed ML deployment and monitoring

**Runnable configuration pattern**

```text
gcloud run deploy churn-api --image=$IMAGE --region=$REGION \
+ --no-allow-unauthenticated --min=1 --max=20 --cpu=2 --memory=2Gi
```

**Metric:** Request latency  
**Formula/decision rule:** `latency = response_time - request_time`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Revision not ready | port or startup failure | read revision logs |
| OOM kill | memory limit | profile and right-size |
| 5xx burst | downstream saturation | timeouts and circuit breaker |

**Evidence chain**

- image digest
- deployment YAML/command
- revision ID
- load-test output
- logs and metrics

**Exam-style decision case**

A scikit-learn API is stateless and bursty; a future GPU version may need custom scheduling.

**Best decision:** Deploy CPU baseline to Cloud Run; use GKE only when its control requirements become real.

**Related practical:** Activity 13

## Domain 5 — Automating and orchestrating ML pipelines (~18%)

Topic 8: MLOps, CI/CD and repeatable workflows.

### Pipeline component contracts

**Mechanism flow**

Ingest → Validate → Transform → Train → Evaluate → Deploy gate

**Service or method decision**

- **Artifact input** — versioned file/model output
- **Parameter** — small configuration value
- **Metric** — numeric gate and comparison

**Runnable configuration pattern**

```text
@component
def evaluate(model: Input[Model], metrics: Output[Metrics]):
    score = run_eval(model.path)
    metrics.log_metric('auc', score)
```

**Metric:** Pipeline pass rate  
**Formula/decision rule:** `passes / scheduled_runs`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Hidden dependency | component reads global path | declare input |
| Cache poison | mutable URI | immutable artifact |
| Wrong deploy | gate not wired | explicit conditional |

**Evidence chain**

- component spec
- input/output schema
- compiled pipeline
- artifact URI
- gate result

**Exam-style decision case**

A pipeline retrains successfully but deploys a model evaluated on the previous run's dataset.

**Best decision:** Make data/model/metrics explicit artifacts and wire deployment to the current evaluation output.

**Related practical:** Activity 14

### Vertex AI Pipelines and Kubeflow

**Mechanism flow**

Python DSL → Compile → Submit → Metadata → Cache → Schedule

**Service or method decision**

- **Vertex AI Pipelines** — managed KFP execution
- **Kubeflow on GKE** — cluster-level control
- **Local runner** — component unit testing only

**Runnable configuration pattern**

```text
compiler.Compiler().compile(pipeline_func=training_pipeline, package_path='pipeline.json')
aiplatform.PipelineJob(display_name='churn', template_path='pipeline.json').run()
```

**Metric:** Cached step savings  
**Formula/decision rule:** `saved = uncached_duration - cached_duration`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Compile error | type mismatch | typed component contracts |
| Permission failure | pipeline SA incomplete | role matrix |
| Unexpected cache | inputs unchanged but code changed | version component/image |

**Evidence chain**

- pipeline JSON
- service account
- run graph
- metadata lineage
- schedule config

**Exam-style decision case**

A weekly training pipeline must be reproducible, inspectable and rerun only changed components.

**Best decision:** Use Vertex AI Pipelines with versioned components, managed metadata and deliberate caching.

**Related practical:** Activity 14

### Cloud Composer and Airflow

**Mechanism flow**

DAG → Sensors → Data job → ML pipeline → SLA → Notification

**Service or method decision**

- **Composer** — cross-service scheduling and dependencies
- **Vertex schedule** — simple pipeline cadence
- **Cloud Scheduler** — single HTTP/event trigger

**Runnable configuration pattern**

```text
with DAG('weekly_ml', schedule='0 2 * * 1', catchup=False) as dag:
    wait_data >> launch_dataflow >> run_vertex_pipeline >> verify_slo
```

**Metric:** DAG SLA misses  
**Formula/decision rule:** `miss_rate = missed_runs / scheduled_runs`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Backfill storm | catchup enabled | set catchup deliberately |
| Stuck sensor | polling resource | deferrable sensor |
| Duplicate run | non-idempotent task | run IDs and idempotency |

**Evidence chain**

- DAG code
- run ID
- task logs
- SLA miss
- notification ticket

**Exam-style decision case**

Training waits for three upstream data products and must notify owners when the freshness SLA fails.

**Best decision:** Use Composer for cross-team dependencies; keep ML logic inside the versioned Vertex pipeline.

**Related practical:** Activity 14

### Ray on Vertex AI

**Mechanism flow**

Driver → Cluster → Tasks/actors → Object store → Autoscale → Result

**Service or method decision**

- **Ray** — distributed Python workloads and tuning
- **Dataflow** — Beam data processing
- **CustomJob** — bounded training job

**Runnable configuration pattern**

```text
@ray.remote
def score_shard(uri):
    return score(load(uri))
results = ray.get([score_shard.remote(u) for u in shard_uris])
```

**Metric:** Distributed task throughput  
**Formula/decision rule:** `throughput = completed_tasks / minute`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Object-store pressure | large returned objects | write artifacts externally |
| Task retries | non-idempotent side effect | idempotent tasks |
| Cluster idle | no teardown | job-scoped cluster policy |

**Evidence chain**

- cluster spec
- Ray job ID
- task timeline
- object-store metrics
- result manifest

**Exam-style decision case**

A Python-native embedding job fans out 20,000 independent shards and aggregates a manifest.

**Best decision:** Use Ray tasks with external artifact writes, idempotent retries and explicit cluster teardown.

**Related practical:** Activity 14

### Training-serving preprocessing parity

**Mechanism flow**

Source schema → Transform graph → Training → Export → Serving → Golden test

**Service or method decision**

- **tf.Transform** — TensorFlow preprocessing graph
- **Sklearn Pipeline** — classical Python models
- **Feature Store** — central shared features

**Runnable configuration pattern**

```text
expected = offline_pipeline.transform(golden)
actual = requests.post(endpoint, json=golden).json()['features']
np.testing.assert_allclose(actual, expected, rtol=1e-6)
```

**Metric:** Golden feature max error  
**Formula/decision rule:** `max_abs(actual-expected)`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Skew | two transform implementations | one exported graph |
| Schema mismatch | independent contracts | versioned schema |
| Silent rounding | different dtypes | assert tolerances |

**Evidence chain**

- transform artifact
- schema version
- golden input
- offline/online diff
- test result

**Exam-style decision case**

A category vocabulary updates in training, but the online service keeps last month's mapping.

**Best decision:** Version and deploy the transformation with the model; block rollout on golden parity tests.

**Related practical:** Activity 11

### Retraining policy

**Mechanism flow**

Signal → Eligibility → Trigger → Train → Compare → Promote

**Service or method decision**

- **Schedule** — stable cadence and predictable data
- **Drift trigger** — distribution changes matter
- **Performance trigger** — labels arrive and business metric degrades

**Runnable configuration pattern**

```text
trigger_if = {'psi_gt':0.2,'auc_drop_gt':0.03,'min_new_labels':10000}
cooldown_hours = 72
require_human_approval = True
```

**Metric:** AUC over time  
**Formula/decision rule:** `drop = baseline_auc - current_auc`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Retrain loop | no cooldown | minimum interval |
| Bad labels | freshness mistaken for quality | label validation |
| Auto-promote harm | single metric | multi-gate approval |

**Evidence chain**

- trigger event
- data-quality report
- candidate/champion comparison
- approval
- promotion log

**Exam-style decision case**

Labels arrive weekly; data drift is common but only some drift reduces business performance.

**Best decision:** Trigger on performance with enough fresh labels; use drift as investigation, not automatic proof.

**Related practical:** Activity 16

### CI/CD/CT with Cloud Build

**Mechanism flow**

Commit → Test → Build image → Compile pipeline → Evaluate → Promote

**Service or method decision**

- **CI** — unit, contract and security tests
- **CD** — deploy validated artifacts
- **CT** — retrain from governed triggers

**Runnable configuration pattern**

```text
steps:
- name: python:3.11
  entrypoint: pytest
- name: gcr.io/cloud-builders/docker
  args: ['build','-t','$IMAGE','.']
images: ['$IMAGE']
```

**Metric:** Change failure rate  
**Formula/decision rule:** `failed_deployments / deployments`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Mutable latest | tag reused | deploy digest |
| Test gap | only code unit tests | data/model/contract tests |
| Privilege escalation | broad build SA | least-privilege build identity |

**Evidence chain**

- commit SHA
- test report
- image digest
- provenance/SBOM
- deployment approval

**Exam-style decision case**

A training image passes local tests but production deploys a different dependency set.

**Best decision:** Build once in Cloud Build, lock dependencies, attest the digest and deploy that exact artifact.

**Related practical:** Activity 15

### Pipeline governance and reproducibility

**Mechanism flow**

Policy → Template → Execution → Metadata → Review → Retention

**Service or method decision**

- **Org policy** — prevent forbidden resource settings
- **Template** — approved repeatable architecture
- **Policy-as-code** — automated configuration gate

**Runnable configuration pattern**

```text
required_labels = ['owner','data_classification','model_risk']
forbidden = ['public_ip','default_service_account']
retention_days = 365
```

**Metric:** Reproducible run rate  
**Formula/decision rule:** `reproduced_within_tolerance / audited_runs`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Missing owner | labels optional | admission check |
| Data unavailable | retention too short | align lineage retention |
| Environment drift | manual runtime | versioned container |

**Evidence chain**

- policy result
- template version
- run metadata
- artifact retention
- audit replay

**Exam-style decision case**

An auditor selects a six-month-old prediction and asks which code, data and model produced it.

**Best decision:** Retain end-to-end lineage, immutable artifacts and policy evidence long enough for replay.

**Related practical:** Activity 15

## Domain 6 — Monitoring AI solutions (~13%)

Topics 6–8: testing, monitoring, troubleshooting and MLOps.

### AI security and Model Armor

**Mechanism flow**

Input → Detect → Sanitize → Model → Output filter → Audit

**Service or method decision**

- **Regex/DLP** — known sensitive patterns
- **Safety filters** — harm categories
- **Model Armor** — managed prompt/response protection

**Runnable configuration pattern**

```text
blocked_patterns = ['ignore previous instructions','BEGIN PRIVATE KEY']
scan_prompt = True
scan_response = True
log_payload = False
```

**Metric:** Attack success rate  
**Formula/decision rule:** `successful_attacks / red_team_attempts`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Indirect injection | retrieved document contains commands | treat context as data |
| Exfiltration | model reveals secret | minimize context and output scan |
| Log exposure | payload retained | redaction and access control |

**Evidence chain**

- threat model
- red-team corpus
- filter config
- blocked event
- incident review

**Exam-style decision case**

A grounded assistant retrieves a document that instructs the model to reveal system prompts.

**Best decision:** Separate instructions from untrusted context, scan inputs/outputs and test indirect injections.

**Related practical:** Activity 16

### Responsible AI and bias monitoring

**Mechanism flow**

Outcome → Protected slices → Metric → Threshold → Review → Mitigation

**Service or method decision**

- **Demographic parity** — selection rates where appropriate
- **Equal opportunity** — true-positive rates
- **Calibration** — probabilities match outcomes

**Runnable configuration pattern**

```text
monitor_slices = ['region','age_band']
max_tpr_gap = 0.05
min_sample = 200
escalate_to = 'model-risk-committee'
```

**Metric:** True-positive-rate gap  
**Formula/decision rule:** `max(TPR)-min(TPR)`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Small slice noise | insufficient N | confidence bounds/min sample |
| Proxy feature | correlated attribute | causal/domain review |
| Metric conflict | one fairness metric only | risk-specific metric set |

**Evidence chain**

- slice definition
- metric with intervals
- threshold policy
- review minutes
- mitigation outcome

**Exam-style decision case**

Approval rates are stable overall but qualified applicants in one region see falling true-positive rate.

**Best decision:** Alert on slice TPR gap with sample safeguards and require model-risk review before threshold changes.

**Related practical:** Activity 16

### Explainability and feature attribution

**Mechanism flow**

Prediction → Baseline → Attributions → Global summary → Slice review → Action

**Service or method decision**

- **Local attribution** — explain one prediction
- **Global importance** — aggregate model behavior
- **Counterfactual** — what feasible change alters outcome

**Runnable configuration pattern**

```text
explanation_spec = {'method':'sampled_shapley','sampled_shapley_attribution':{'path_count':20}}
```

**Metric:** Attribution drift  
**Formula/decision rule:** `distance(current_attributions, baseline_attributions)`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Causal claim | attribution mistaken for cause | state limitation |
| Unstable rank | correlated features | group and test stability |
| Sensitive proxy | unexpected importance | investigate governance |

**Evidence chain**

- explanation config
- local plot
- global ranking
- slice comparison
- review action

**Exam-style decision case**

A credit model keeps AUC, but postcode suddenly becomes the top feature after a data release.

**Best decision:** Investigate attribution drift and proxy risk; do not accept stable accuracy as proof of safety.

**Related practical:** Activity 16

### Data drift, skew and concept drift

**Mechanism flow**

Baseline → Current window → Statistic → Threshold → Diagnosis → Response

**Service or method decision**

- **Training-serving skew** — training vs serving pipeline mismatch
- **Data drift** — input distribution changes
- **Concept drift** — relationship between input and outcome changes

**Runnable configuration pattern**

```text
psi = sum((current_pct - base_pct) * log(current_pct/base_pct))
alert_if = 'psi > 0.2 for 2 windows'
```

**Metric:** Population stability index  
**Formula/decision rule:** `PSI = sum((A-E)*ln(A/E))`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| False drift | seasonality | seasonal baseline |
| Skew | transform version differs | parity test |
| Concept drift | inputs stable but errors rise | label-based performance monitor |

**Evidence chain**

- baseline version
- window definition
- drift statistic
- alert
- diagnosis and disposition

**Exam-style decision case**

A fraud feature distribution shifts every holiday, but loss rises only after a new payment channel launch.

**Best decision:** Use seasonal baselines; distinguish benign data drift from labeled concept drift before retraining.

**Related practical:** Activity 16

### Gen AI evaluation in production

**Mechanism flow**

Sample → Safety scan → Groundedness → Task quality → Human audit → Feedback

**Service or method decision**

- **Continuous eval** — sample production traffic
- **Synthetic red team** — probe rare attacks
- **Human audit** — calibrate nuanced risk

**Runnable configuration pattern**

```text
sample_rate = 0.02
metrics = ['groundedness','instruction_following','safety']
critical_violation_budget = 0
```

**Metric:** Grounded answer rate  
**Formula/decision rule:** `grounded_answers / evaluated_answers`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Privacy leak | raw prompts in eval set | redact and restrict |
| Judge drift | judge model changed | version and calibrate |
| Silent regression | no release baseline | champion comparison |

**Evidence chain**

- sampling policy
- redacted eval set
- judge version
- human agreement
- incident linkage

**Exam-style decision case**

A support assistant remains fluent but citations increasingly fail to support its claims.

**Best decision:** Continuously score groundedness, audit samples and block releases that regress against the champion.

**Related practical:** Activity 16

### SLOs, logs and alerts

**Mechanism flow**

User journey → SLI → SLO → Error budget → Alert → Runbook

**Service or method decision**

- **Availability** — successful valid responses
- **Latency** — p95/p99 per request class
- **Quality** — validated prediction or grounded response

**Runnable configuration pattern**

```text
slo:
  availability: 0.999
  p95_latency_ms: 300
  quality_floor: 0.82
alert_on_burn_rate: true
```

**Metric:** Error-budget burn  
**Formula/decision rule:** `burn = observed_error_rate / allowed_error_rate`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Alert storm | symptom alerts duplicate | burn-rate aggregation |
| No context | logs lack version | structured version fields |
| Green infra/red users | only CPU monitored | user-centric quality SLI |

**Evidence chain**

- SLI query
- SLO policy
- version-tagged log
- burn alert
- runbook execution

**Exam-style decision case**

Infrastructure is healthy, yet users receive stale predictions for six hours after a failed batch.

**Best decision:** Add freshness and quality SLIs, not just infrastructure metrics; page on error-budget burn.

**Related practical:** Activity 16

### Incident troubleshooting

**Mechanism flow**

Detect → Triage → Contain → Diagnose → Recover → Learn

**Service or method decision**

- **Rollback** — new version caused regression
- **Scale** — capacity saturation
- **Disable feature** — upstream corruption

**Runnable configuration pattern**

```text
incident_id: ML-2026-0912
model_version: candidate-17
start: 14:05Z
containment: rollback_to_champion
owner: ml-platform
```

**Metric:** Mean time to recovery  
**Formula/decision rule:** `MTTR = sum(recovery_duration)/incident_count`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Slow triage | no version tags | structured logs |
| Repeat issue | no action owner | postmortem with due dates |
| Evidence loss | ephemeral logs | central retention |

**Evidence chain**

- timeline
- impact estimate
- version and data IDs
- containment command
- postmortem actions

**Exam-style decision case**

p95 latency triples immediately after a new model version receives 20% traffic.

**Best decision:** Compare per-version metrics, roll back the candidate, preserve traces, then reproduce under load.

**Related practical:** Activity 16

### Cost and performance optimization

**Mechanism flow**

Measure → Attribute → Profile → Change → Load test → Approve

**Service or method decision**

- **Right-size** — remove unused CPU/memory/accelerator
- **Batching** — amortize inference overhead
- **Quantization** — trade small quality loss for speed/cost

**Runnable configuration pattern**

```text
baseline = {'p95_ms':280,'cost_1k':0.42,'auc':0.846}
candidate = {'p95_ms':170,'cost_1k':0.24,'auc':0.842}
max_auc_loss = 0.005
```

**Metric:** Cost per 1,000 predictions  
**Formula/decision rule:** `total_cost / prediction_count * 1000`

**Failure diagnosis**

| Observable symptom | Likely mechanism | Control or verification |
|---|---|---|
| Cheap but worse | quality not gated | multi-objective gate |
| Benchmark bias | toy load | production traffic shape |
| Hidden egress | cross-region path | co-locate services |

**Evidence chain**

- billing labels
- profiler trace
- quality comparison
- load test
- architecture decision

**Exam-style decision case**

Quantization halves cost but reduces AUC by 0.004 and improves p95 latency by 110 ms.

**Best decision:** Accept only if the documented quality tolerance is 0.005 and slice/edge-case gates also pass.

**Related practical:** Activity 16


## Detailed Activity Guides

The following sections reproduce the current learner-facing Activity guides. Each Activity folder also contains a same-basename PDF plus the mock data, scripts and configuration needed to complete it.

### Activity 01 — Create a Safe Google Cloud Training Environment

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Create a Google account, Cloud project, billing budget, IAM boundary and Cloud Shell workspace.

#### Deliverables

- `budget-policy.json`
- `check_environment.sh`
- `iam-role-matrix.csv`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: a Google account you control and trainer approval to create an isolated training project.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Open a private browser window and go to https://accounts.google.com/signup

Open a private browser window and go to `https://accounts.google.com/signup`. Create a dedicated training Google Account or sign in with an approved existing account. Complete identity and recovery checks; do not use a shared password.

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Go to https://console.cloud.google.com/

Go to `https://console.cloud.google.com/`. Accept the Google Cloud terms when prompted. If the free-trial offer is available and appropriate, review the current terms before entering payment details; free-tier offers can change.

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — Open the project selector, choose New Project, name it pmle-training-<initials>, record the generated project ID, and select the correct organisation or No organisation only if your trainer approves

Open the project selector, choose **New Project**, name it `pmle-training-<initials>`, record the generated project ID, and select the correct organisation or **No organisation** only if your trainer approves.

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Open Billing and link the training project to the authorised billing account

Open **Billing** and link the training project to the authorised billing account. Billing enables paid services; it does not make all usage free.

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — Open Billing > Budgets & alerts, create a small training budget, and add alert thresholds at 50%, 90% and 100%

Open **Billing > Budgets & alerts**, create a small training budget, and add alert thresholds at 50%, 90% and 100%. Billing alerts do not automatically stop resources.

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — Open IAM & Admin > IAM

Open **IAM & Admin > IAM**. Confirm your user has only the roles required for training. Do not grant Owner to classmates or service accounts.

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Open APIs & Services > Library and enable Vertex AI, BigQuery, Cloud Storage, Artifact Registry, Cloud Build and Cloud Run APIs

Open **APIs & Services > Library** and enable Vertex AI, BigQuery, Cloud Storage, Artifact Registry, Cloud Build and Cloud Run APIs. Record any enablement error before changing roles.

**Check:** Record the observable result or explain the error before continuing.

##### Step 8 — Activate Cloud Shell from the console header

Activate Cloud Shell from the console header. Cloud Shell already includes the Google Cloud CLI and uses your signed-in identity.

```bash
gcloud auth list
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 9 — Set and verify project and region variables for this shell session

Set and verify project and region variables for this shell session.

```bash
export PROJECT_ID='<PROJECT_ID>' REGION='asia-southeast1'
gcloud config set project "$PROJECT_ID"
gcloud config set ai/region "$REGION"
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 10 — Run the supplied environment checker and save its output as evidence

Run the supplied environment checker and save its output as evidence.

```bash
bash check_environment.sh | tee evidence/activity-01-environment.txt
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 11 — Review iam-role-matrix.csv

Review `iam-role-matrix.csv`. For each activity, grant the narrow predefined role only when needed; avoid service-account keys.

**Check:** Record the observable result or explain the error before continuing.

##### Step 12 — Record the project ID, billing account alias, budget name, enabled APIs and IAM decision in your activity evidence

Record the project ID, billing account alias, budget name, enabled APIs and IAM decision in your activity evidence. Do not record payment details.

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


### Activity 02 — Draft an ML Architecture Decision Record

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Convert business volume, latency, security and explainability needs into a service decision.

#### Deliverables

- `requirements.csv`
- `architecture_decision.py`
- `expected_decision.json`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Open requirements.csv and identify the business volume, freshness, latency, availability, privacy and explainability requirements

Open `requirements.csv` and identify the business volume, freshness, latency, availability, privacy and explainability requirements.

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Run the architecture evaluator to score BigQuery ML, AutoML and custom training options

Run the architecture evaluator to score BigQuery ML, AutoML and custom training options.

```bash
python3 architecture_decision.py --requirements requirements.csv --out decision.json
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — Compare decision.json with expected_decision.json; investigate any difference instead of overwriting it

Compare `decision.json` with `expected_decision.json`; investigate any difference instead of overwriting it.

```bash
python3 -m json.tool decision.json
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Draft an Architecture Decision Record with context, options, measurable drivers, selected service, rejected options and consequences

Draft an Architecture Decision Record with context, options, measurable drivers, selected service, rejected options and consequences.

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — Add a capacity calculation for peak QPS, 30% headroom and data growth over two years

Add a capacity calculation for peak QPS, 30% headroom and data growth over two years.

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — Add security controls for identity, encryption, network path, PII and audit logging

Add security controls for identity, encryption, network path, PII and audit logging.

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Add testable acceptance criteria: p95 latency, quality floor, error rate, cost ceiling and rollback time

Add testable acceptance criteria: p95 latency, quality floor, error rate, cost ceiling and rollback time.

**Check:** Record the observable result or explain the error before continuing.

##### Step 8 — Peer-review the decision against the documented acceptance criteria and save the review notes

Peer-review the decision against the documented acceptance criteria and save the review notes.

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


### Activity 03 — Train and Evaluate a BigQuery ML Churn Model

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Run SQL-defined logistic regression, evaluation and batch prediction on mock customer data.

#### Deliverables

- `customers.csv`
- `bigquery_ml.sql`
- `evaluate_metrics.py`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Inspect customers.csv; identify the label, entity key and any feature that could leak the outcome

Inspect `customers.csv`; identify the label, entity key and any feature that could leak the outcome.

```bash
python3 - <<'PY'
import pandas as pd
df=pd.read_csv('customers.csv'); print(df.head()); print(df.isna().sum())
PY
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Open bigquery_ml.sql and replace <PROJECT_ID> and <DATASET> without changing the point-in-time split

Open `bigquery_ml.sql` and replace `<PROJECT_ID>` and `<DATASET>` without changing the point-in-time split.

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — Create the dataset in the same approved region as the training project

Create the dataset in the same approved region as the training project.

```bash
bq --location=asia-southeast1 mk --dataset "$PROJECT_ID:pmle_lab"
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Load the CSV using the declared schema or autodetect only after inspecting types

Load the CSV using the declared schema or autodetect only after inspecting types.

```bash
bq load --autodetect --source_format=CSV pmle_lab.customers customers.csv
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — Run the CREATE MODEL statement and record the BigQuery job ID and bytes processed

Run the `CREATE MODEL` statement and record the BigQuery job ID and bytes processed.

```bash
bq query --use_legacy_sql=false < bigquery_ml.sql
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — Query ML.EVALUATE and save accuracy, precision, recall, F1, log loss and ROC AUC

Query `ML.EVALUATE` and save accuracy, precision, recall, F1, log loss and ROC AUC.

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Run evaluate_metrics.py to compare the supplied confusion matrices at three thresholds

Run `evaluate_metrics.py` to compare the supplied confusion matrices at three thresholds.

```bash
python3 evaluate_metrics.py
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 8 — Choose a threshold using the stated false-negative cost, not accuracy alone, and document the rationale

Choose a threshold using the stated false-negative cost, not accuracy alone, and document the rationale.

**Check:** Record the observable result or explain the error before continuing.

##### Step 9 — Run ML.PREDICT for the holdout rows and check that no post-outcome feature enters the model

Run `ML.PREDICT` for the holdout rows and check that no post-outcome feature enters the model.

**Check:** Record the observable result or explain the error before continuing.

##### Step 10 — Delete the model and dataset during cleanup if the trainer does not require them for a later activity

Delete the model and dataset during cleanup if the trainer does not require them for a later activity.

```bash
bq rm -f -m pmle_lab.churn_model
```

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


### Activity 04 — Design an AutoML Tabular Experiment

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Create a dataset specification, split plan, budget and evaluation slice gate.

#### Deliverables

- `automl_dataset.csv`
- `automl_config.yaml`
- `validate_splits.py`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Profile automl_dataset.csv and confirm the target has no nulls and each split is represented

Profile `automl_dataset.csv` and confirm the target has no nulls and each split is represented.

```bash
python3 validate_splits.py automl_dataset.csv
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Review automl_config.yaml: objective, target, optimization metric, training budget and encryption setting

Review `automl_config.yaml`: objective, target, optimization metric, training budget and encryption setting.

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — Check whether a random split is valid for the event timestamps

Check whether a random split is valid for the event timestamps. Replace it with chronological split logic if future leakage is possible.

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Define evaluation slices for region, channel and customer tenure

Define evaluation slices for region, channel and customer tenure. Set a minimum sample size for each slice.

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — Estimate training cost from node-hours before starting any AutoML job

Estimate training cost from node-hours before starting any AutoML job. Obtain trainer approval for paid execution.

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — In Vertex AI, create a tabular dataset only if approved; otherwise treat the configuration as a dry-run design exercise

In Vertex AI, create a tabular dataset only if approved; otherwise treat the configuration as a dry-run design exercise.

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Configure the target column and split column, then compare the console summary with the YAML design

Configure the target column and split column, then compare the console summary with the YAML design.

**Check:** Record the observable result or explain the error before continuing.

##### Step 8 — After training, record model evaluation, feature attributions, slice results and training budget used

After training, record model evaluation, feature attributions, slice results and training budget used.

**Check:** Record the observable result or explain the error before continuing.

##### Step 9 — Write a go/no-go decision

Write a go/no-go decision. A high aggregate score cannot override a failed critical slice.

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


### Activity 05 — Compare Pretrained Google Cloud AI APIs

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Prepare Vision, Document AI and Natural Language requests and interpret mock responses.

#### Deliverables

- `vision_request.json`
- `mock_vision_response.json`
- `api_selector.py`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Inspect vision_request.json and identify the feature type, image source and maximum results

Inspect `vision_request.json` and identify the feature type, image source and maximum results.

```bash
python3 -m json.tool vision_request.json
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Inspect mock_vision_response.json; list detected labels, confidence scores and the response field holding errors

Inspect `mock_vision_response.json`; list detected labels, confidence scores and the response field holding errors.

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — Run the selector for three scenarios and record the recommended managed API or custom-model path

Run the selector for three scenarios and record the recommended managed API or custom-model path.

```bash
python3 api_selector.py
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Prepare an authenticated REST command using gcloud auth print-access-token; do not store the token

Prepare an authenticated REST command using `gcloud auth print-access-token`; do not store the token.

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — If the trainer approves live use, enable the chosen API and send only the supplied non-sensitive sample

If the trainer approves live use, enable the chosen API and send only the supplied non-sensitive sample.

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — Interpret 403, 429 and low-confidence responses separately: authorization, quota and model fit are different problems

Interpret 403, 429 and low-confidence responses separately: authorization, quota and model fit are different problems.

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Design a confidence-based human-review queue and calculate the expected review rate from the mock response set

Design a confidence-based human-review queue and calculate the expected review rate from the mock response set.

**Check:** Record the observable result or explain the error before continuing.

##### Step 8 — Save the request, redacted response, operation ID, cost estimate and decision note

Save the request, redacted response, operation ID, cost estimate and decision note.

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


### Activity 06 — Build a Data Quality and Feature Pipeline

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Validate schema, repair missing values, encode features and preserve a training manifest.

#### Deliverables

- `transactions.csv`
- `build_features.py`
- `feature_schema.json`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Profile transactions.csv for types, nulls, duplicates, impossible values and label balance

Profile `transactions.csv` for types, nulls, duplicates, impossible values and label balance.

```bash
python3 build_features.py --input transactions.csv --profile-only
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Read feature_schema.json and confirm each field's type, allowed range and missing-value policy

Read `feature_schema.json` and confirm each field's type, allowed range and missing-value policy.

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — Run the feature builder to create a deterministic train/validation/test split and manifest

Run the feature builder to create a deterministic train/validation/test split and manifest.

```bash
python3 build_features.py --input transactions.csv --out-dir output
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Inspect the rejected-row report

Inspect the rejected-row report. Correct source data rules rather than silently dropping all failures.

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — Check that category encoding handles unknown values and that fitted statistics use training rows only

Check that category encoding handles unknown values and that fitted statistics use training rows only.

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — Verify entity IDs do not appear as predictive numeric features

Verify entity IDs do not appear as predictive numeric features.

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Compare split timestamps and confirm no future event contributes to an earlier example

Compare split timestamps and confirm no future event contributes to an earlier example.

**Check:** Record the observable result or explain the error before continuing.

##### Step 8 — Record row-count reconciliation, schema signature and output checksums

Record row-count reconciliation, schema signature and output checksums.

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


### Activity 07 — Train a TensorFlow/Keras Model

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Use tf.data, a Keras network, early stopping and SavedModel verification.

#### Deliverables

- `train_tensorflow.py`
- `requirements.txt`
- `expected_history.csv`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Create a clean virtual environment and install the pinned requirements

Create a clean virtual environment and install the pinned requirements.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Open train_tensorflow.py and locate shuffle, batch, prefetch, early stopping and the export signature

Open `train_tensorflow.py` and locate `shuffle`, `batch`, `prefetch`, early stopping and the export signature.

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — Run the offline training script on the generated mock dataset

Run the offline training script on the generated mock dataset.

```bash
python3 train_tensorflow.py --epochs 20 --output output/model
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Compare training and validation loss with expected_history.csv and identify the first overfitting epoch

Compare training and validation loss with `expected_history.csv` and identify the first overfitting epoch.

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — Reload the SavedModel and score the included golden example

Reload the SavedModel and score the included golden example.

```bash
python3 train_tensorflow.py --verify-only --output output/model
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — Change batch size once, rerun, and record throughput and validation quality rather than selecting by speed alone

Change batch size once, rerun, and record throughput and validation quality rather than selecting by speed alone.

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Save the model summary, history, evaluation metrics and signature output

Save the model summary, history, evaluation metrics and signature output.

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


### Activity 08 — Package a Vertex AI Custom Training Job

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Build a reproducible training package and container with managed output paths.

#### Deliverables

- `train.py`
- `Dockerfile`
- `custom_job.yaml`
- `requirements.txt`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Inspect train.py, requirements.txt, Dockerfile and custom_job.yaml; trace each file to the managed job lifecycle

Inspect `train.py`, `requirements.txt`, `Dockerfile` and `custom_job.yaml`; trace each file to the managed job lifecycle.

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Run the training entry point locally and confirm it writes to the AIP_MODEL_DIR fallback

Run the training entry point locally and confirm it writes to the `AIP_MODEL_DIR` fallback.

```bash
python3 train.py --data-uri mock://customers --epochs 3
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — Build the container locally with a versioned tag; do not use latest as deployment evidence

Build the container locally with a versioned tag; do not use `latest` as deployment evidence.

```bash
docker build -t pmle-train:v8 .
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Run the container with a mounted output directory and verify the model artifact appears

Run the container with a mounted output directory and verify the model artifact appears.

```bash
docker run --rm -v "$PWD/output:/model" -e AIP_MODEL_DIR=/model pmle-train:v8
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — Replace project and Artifact Registry placeholders only if a live push is approved

Replace project and Artifact Registry placeholders only if a live push is approved.

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — Validate the worker-pool machine type, service account and artifact output permissions in custom_job.yaml

Validate the worker-pool machine type, service account and artifact output permissions in `custom_job.yaml`.

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Submit the job only with trainer approval; record job ID, image digest and log link

Submit the job only with trainer approval; record job ID, image digest and log link.

**Check:** Record the observable result or explain the error before continuing.

##### Step 8 — Diagnose a supplied missing-dependency failure and propose a pinned dependency fix

Diagnose a supplied missing-dependency failure and propose a pinned dependency fix.

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


### Activity 09 — Analyze Vertex AI Hyperparameter Trials

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Define a Vizier-style search space and select a trial using quality and cost evidence.

#### Deliverables

- `trials.csv`
- `tuning_config.yaml`
- `select_trial.py`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Review tuning_config.yaml; identify search distributions, objective direction, maximum trials and parallel trials

Review `tuning_config.yaml`; identify search distributions, objective direction, maximum trials and parallel trials.

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Inspect trials.csv for status, objective, duration and cost

Inspect `trials.csv` for status, objective, duration and cost. Exclude failed trials from the quality ranking but retain them for reliability analysis.

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — Run the selector with the default quality floor and cost ceiling

Run the selector with the default quality floor and cost ceiling.

```bash
python3 select_trial.py --input trials.csv --min-auc 0.82 --max-cost 25
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Calculate marginal quality gain from the third to the fifth completed trial

Calculate marginal quality gain from the third to the fifth completed trial.

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — Identify whether the best validation trial is likely over-searched and state why an untouched test set is required

Identify whether the best validation trial is likely over-searched and state why an untouched test set is required.

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — Change the cost ceiling and explain the selected-trial change using evidence

Change the cost ceiling and explain the selected-trial change using evidence.

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Draft a final retraining configuration using the selected parameters and no tuning-only callbacks

Draft a final retraining configuration using the selected parameters and no tuning-only callbacks.

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


### Activity 10 — Plan Distributed PyTorch GPU Training

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Configure torchrun-style workers, checkpoints and scaling-efficiency diagnostics.

#### Deliverables

- `train_distributed.py`
- `Dockerfile`
- `worker_pool.yaml`
- `scaling_results.csv`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Read worker_pool.yaml and map chief, worker replicas, machine types, accelerator count and checkpoint URI

Read `worker_pool.yaml` and map chief, worker replicas, machine types, accelerator count and checkpoint URI.

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Inspect train_distributed.py; locate process-group initialization, distributed sampler, all-reduce behavior and checkpoint save

Inspect `train_distributed.py`; locate process-group initialization, distributed sampler, all-reduce behavior and checkpoint save.

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — Run the local two-process smoke test without GPUs

Run the local two-process smoke test without GPUs.

```bash
python3 -m torch.distributed.run --standalone --nproc_per_node=2 train_distributed.py --epochs 2
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Inspect scaling_results.csv and calculate speedup and scaling efficiency for 1, 2, 4 and 8 workers

Inspect `scaling_results.csv` and calculate speedup and scaling efficiency for 1, 2, 4 and 8 workers.

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — Explain why 8 workers may reduce efficiency even while throughput increases

Explain why 8 workers may reduce efficiency even while throughput increases.

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — Design a checkpoint interval from the observed failure rate and checkpoint write time

Design a checkpoint interval from the observed failure rate and checkpoint write time.

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Build the custom container only if Docker is available; record the image digest

Build the custom container only if Docker is available; record the image digest.

```bash
docker build -t pmle-torchrun:v8 .
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 8 — Propose a GPU/TPU/CPU choice using examples per dollar, framework support and quota

Propose a GPU/TPU/CPU choice using examples per dollar, framework support and quota.

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


### Activity 11 — Verify Feature Store Point-in-Time Parity

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Model offline/online feature definitions and detect stale or leaked features.

#### Deliverables

- `offline_features.csv`
- `online_features.csv`
- `check_parity.py`
- `feature_view.yaml`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Inspect feature_view.yaml and identify the entity key, feature names, online TTL and source timestamp

Inspect `feature_view.yaml` and identify the entity key, feature names, online TTL and source timestamp.

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Run the parity checker on the offline and online snapshots

Run the parity checker on the offline and online snapshots.

```bash
python3 check_parity.py --offline offline_features.csv --online online_features.csv
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — Separate point-in-time leakage from stale online values; they require different fixes

Separate point-in-time leakage from stale online values; they require different fixes.

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Trace a mismatched entity through key normalization and timestamp selection

Trace a mismatched entity through key normalization and timestamp selection.

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — Set a freshness SLO and specify the monitoring window and alert persistence

Set a freshness SLO and specify the monitoring window and alert persistence.

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — Create a golden entity lookup and assert identical transformed values for batch and online paths

Create a golden entity lookup and assert identical transformed values for batch and online paths.

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Record mismatches, root cause, remediation and the feature-definition version

Record mismatches, root cause, remediation and the feature-definition version.

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


### Activity 12 — Register and Canary a Model Version

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Create registry metadata, traffic split, guardrails and rollback evidence.

#### Deliverables

- `model_manifest.json`
- `deployment.yaml`
- `canary_metrics.csv`
- `evaluate_canary.py`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Inspect model_manifest.json; verify model version, code SHA, data version, metrics and owner are complete

Inspect `model_manifest.json`; verify model version, code SHA, data version, metrics and owner are complete.

```bash
python3 -m json.tool model_manifest.json
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Review deployment.yaml; locate the champion/candidate traffic split and rollback guardrails

Review `deployment.yaml`; locate the champion/candidate traffic split and rollback guardrails.

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — Run the canary evaluator against canary_metrics.csv

Run the canary evaluator against `canary_metrics.csv`.

```bash
python3 evaluate_canary.py --metrics canary_metrics.csv --config deployment.yaml
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Explain whether the candidate should be promoted, held or rolled back using per-version metrics

Explain whether the candidate should be promoted, held or rolled back using per-version metrics.

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — Change traffic to 25% only after the 10% stage passes; never overwrite prior stage evidence

Change traffic to 25% only after the 10% stage passes; never overwrite prior stage evidence.

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — Simulate a latency breach and confirm the evaluator returns a rollback decision

Simulate a latency breach and confirm the evaluator returns a rollback decision.

```bash
python3 evaluate_canary.py --metrics canary_metrics.csv --config deployment.yaml --simulate-breach
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Record registry ID, immutable artifact checksum, traffic split, decision and rollback test

Record registry ID, immutable artifact checksum, traffic split, decision and rollback test.

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


### Activity 13 — Serve a Model on Cloud Run

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Package a Flask prediction API, test its contract and analyze load-test results.

#### Deliverables

- `app.py`
- `Dockerfile`
- `requirements.txt`
- `test_api.py`
- `load_results.csv`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Create a virtual environment and install pinned dependencies

Create a virtual environment and install pinned dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Run the Flask service locally and verify /health before using /predict

Run the Flask service locally and verify `/health` before using `/predict`.

```bash
python3 app.py
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — In another terminal, run the API contract tests

In another terminal, run the API contract tests.

```bash
python3 test_api.py --base-url http://127.0.0.1:8080
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Build the container and run the same health and prediction tests against it

Build the container and run the same health and prediction tests against it.

```bash
docker build -t pmle-api:v8 .
docker run --rm -p 8080:8080 pmle-api:v8
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — Inspect load_results.csv; plot QPS against p95 latency and identify saturation

Inspect `load_results.csv`; plot QPS against p95 latency and identify saturation.

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — Draft a Cloud Run deployment with authenticated ingress, min/max instances and region

Draft a Cloud Run deployment with authenticated ingress, min/max instances and region.

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Deploy only if approved, then record revision ID and image digest

Deploy only if approved, then record revision ID and image digest.

**Check:** Record the observable result or explain the error before continuing.

##### Step 8 — Test one invalid schema and confirm the service returns a controlled 4xx response without secrets

Test one invalid schema and confirm the service returns a controlled 4xx response without secrets.

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


### Activity 14 — Compile a Vertex AI Pipeline

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Connect validate, transform, train, evaluate and conditional deployment components.

#### Deliverables

- `pipeline.py`
- `pipeline_spec.json`
- `component_contracts.yaml`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Read component_contracts.yaml and identify explicit inputs, outputs, artifacts and metrics for every component

Read `component_contracts.yaml` and identify explicit inputs, outputs, artifacts and metrics for every component.

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Open pipeline.py; trace validate, transform, train, evaluate and conditional deploy dependencies

Open `pipeline.py`; trace validate, transform, train, evaluate and conditional deploy dependencies.

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — Run the local compiler to produce compiled_pipeline.json

Run the local compiler to produce `compiled_pipeline.json`.

```bash
python3 pipeline.py --compile compiled_pipeline.json
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Compare the compiled graph with pipeline_spec.json; confirm deployment consumes the current evaluation artifact

Compare the compiled graph with `pipeline_spec.json`; confirm deployment consumes the current evaluation artifact.

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — Change the quality threshold, recompile and inspect the parameter diff

Change the quality threshold, recompile and inspect the parameter diff.

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — Explain which components may be cached and which must rerun after a data-version change

Explain which components may be cached and which must rerun after a data-version change.

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Design the pipeline service-account role matrix and reject default broad identities

Design the pipeline service-account role matrix and reject default broad identities.

**Check:** Record the observable result or explain the error before continuing.

##### Step 8 — Record compiled checksum, component versions and expected lineage path

Record compiled checksum, component versions and expected lineage path.

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


### Activity 15 — Design an ML CI/CD/CT Release

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Create Cloud Build gates, artifact provenance and a model card release record.

#### Deliverables

- `cloudbuild.yaml`
- `release_gate.py`
- `model_card.md`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Inspect cloudbuild.yaml; classify each step as CI, CD or CT and identify the artifact passed forward

Inspect `cloudbuild.yaml`; classify each step as CI, CD or CT and identify the artifact passed forward.

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Run the release gate on the supplied model metrics

Run the release gate on the supplied model metrics.

```bash
python3 release_gate.py --auc 0.846 --p95-ms 170 --fairness-gap 0.03
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — Run a failing case and confirm promotion is blocked with a clear reason

Run a failing case and confirm promotion is blocked with a clear reason.

```bash
python3 release_gate.py --auc 0.79 --p95-ms 410 --fairness-gap 0.09
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Open model_card.md and complete intended use, out-of-scope use, data, metrics, slices, limitations and owner

Open `model_card.md` and complete intended use, out-of-scope use, data, metrics, slices, limitations and owner.

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — Add dependency lock, unit test, data-contract test, container scan and provenance to the release evidence

Add dependency lock, unit test, data-contract test, container scan and provenance to the release evidence.

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — Specify which identity Cloud Build uses and the narrow roles it needs

Specify which identity Cloud Build uses and the narrow roles it needs.

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Create a rollback plan referencing the previous registry version and its tested endpoint configuration

Create a rollback plan referencing the previous registry version and its tested endpoint configuration.

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


### Activity 16 — Investigate Drift, Bias and an ML Incident

**Course:** Google Professional Machine Learning Engineer Training  
**Course code:** C740  
**Version:** v8.0 · 12 September 2026  
**Evidence:** activity artifacts and acceptance checks

#### Objective

Calculate drift and slice metrics, enforce SLOs and produce an incident evidence pack.

#### Deliverables

- `baseline.csv`
- `current.csv`
- `monitor.py`
- `incident_template.md`
- A completed `evidence/` folder with decision notes and verification output

#### Prerequisites

- Python 3.11 or later and a terminal; Docker only where the activity explicitly uses it.
- For optional live Google Cloud steps: the safe training project created in Activity 01.
- Start in this activity folder so relative paths and cleanup commands remain scoped.


#### Safety, cost and privacy

- Use a training project that contains no production or personal data.
- Replace every placeholder such as `<PROJECT_ID>` and `<REGION>` before a cloud command.
- Do not paste API keys or service-account JSON into notebooks, scripts or screenshots.
- Prefer Cloud Shell and Application Default Credentials. Never commit `.env` or credentials.
- Verify the result against the acceptance checklist, then run the cleanup section.

#### Evidence to retain

Create an `evidence/` folder locally. Save command output, job or revision IDs, metric tables,
screenshots without secrets, and a short decision note. Use filenames that include the activity
number and date. Evidence is part of the learning outcome, not an optional extra.


#### Detailed step-by-step guide

##### Step 1 — Inspect baseline.csv and current.csv; identify the monitored feature, outcome, prediction, group and timestamps

Inspect `baseline.csv` and `current.csv`; identify the monitored feature, outcome, prediction, group and timestamps.

**Check:** Record the observable result or explain the error before continuing.

##### Step 2 — Run the monitor to calculate PSI, accuracy, group true-positive rates and p95 latency

Run the monitor to calculate PSI, accuracy, group true-positive rates and p95 latency.

```bash
python3 monitor.py --baseline baseline.csv --current current.csv --out monitoring_report.json
```

**Check:** Record the observable result or explain the error before continuing.

##### Step 3 — Classify each signal as training-serving skew, data drift, concept drift, bias risk or service degradation

Classify each signal as training-serving skew, data drift, concept drift, bias risk or service degradation.

**Check:** Record the observable result or explain the error before continuing.

##### Step 4 — Use persistence and minimum-sample rules before escalating; one noisy window is not sufficient evidence

Use persistence and minimum-sample rules before escalating; one noisy window is not sufficient evidence.

**Check:** Record the observable result or explain the error before continuing.

##### Step 5 — Open incident_template.md; complete impact, timeline, affected versions, containment, recovery and actions

Open `incident_template.md`; complete impact, timeline, affected versions, containment, recovery and actions.

**Check:** Record the observable result or explain the error before continuing.

##### Step 6 — Choose containment: rollback candidate, disable corrupt feature or scale capacity, and justify it from the evidence

Choose containment: rollback candidate, disable corrupt feature or scale capacity, and justify it from the evidence.

**Check:** Record the observable result or explain the error before continuing.

##### Step 7 — Verify logs and screenshots contain no PII, tokens or full prompts

Verify logs and screenshots contain no PII, tokens or full prompts.

**Check:** Record the observable result or explain the error before continuing.

##### Step 8 — Create an executive summary and a technical evidence appendix, then peer-review against the documented acceptance criteria

Create an executive summary and a technical evidence appendix, then peer-review against the documented acceptance criteria.

**Check:** Record the observable result or explain the error before continuing.


#### Acceptance checklist

- [ ] Every required artifact exists and opens without error.
- [ ] Results are tied to the supplied mock data or an approved training project.
- [ ] The conclusion cites metrics, IDs or command output rather than opinion alone.
- [ ] No credentials, tokens, personal data or unredacted sensitive prompts are present.
- [ ] Cleanup is completed or the retained resource is documented with an owner and expiry.

#### Troubleshooting

| Symptom | Likely cause | Corrective action |
|---|---|---|
| `403 PERMISSION_DENIED` | API disabled, wrong project, or IAM role missing | Verify `gcloud config get-value project`, API state and the least-privilege role. |
| `429 RESOURCE_EXHAUSTED` | Quota or rate limit reached | Stop retries, inspect quota, add exponential backoff, and ask the trainer before increasing quota. |
| Region/location mismatch | Dataset, bucket, model or endpoint uses another location | Recreate only the training resource in one approved region; do not copy sensitive data casually. |
| Result differs from expected | Data, dependency or configuration version drifted | Compare file hashes, pinned versions and parameters; retain the diff as evidence. |

#### Cleanup

Stop local processes and remove only resources created for this activity. For live cloud work,
use the Console resource views and activity evidence to verify deletion. Do not delete a shared
project, dataset, bucket, registry or endpoint unless the trainer identifies it as disposable.


## Source Register

| Authority | Source |
|---|---|
| content_source | reference/Master Trainer Slides - Google Professional Machine Learning Engineer Training - v7.pptx |
| design_source | Current Tertiary all-white house design with editable mechanism diagrams and native charts |
| exam_guide | https://cloud.google.com/learn/certification/guides/machine-learning-engineer |
| course_page | https://www.tertiarycourses.com.sg/google-professional-machine-learning-engineer-training.html |
| pipeline_guide | https://tutorialsdojo.com/a-beginners-guide-to-the-machine-learning-pipeline-on-gcp/ |
| gcp_setup | https://www.kdnuggets.com/5-steps-google-cloud-platform |
| deployment | https://dvquys.com/posts/deploy-ml-gcp/ |
| gcp_tutorial_pdf | https://deepgraphlearning.github.io/coursewebsite/assets/files/GCP%20tutorial.pdf |
| deployment_video | https://www.techtarget.com/searchcloudcomputing/video/How-to-deploy-machine-learning-models-on-Googles-AI-Platform |
| course_reference | https://www.udemy.com/course/machine-learning-on-google-cloud-platform/ |
| vertex_sample | https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/training/sdk_pytorch_torchrun_custom_container_training_imagenet.ipynb |
| gke_reference | https://github.com/Shreyjain203/Machine-Learning-Model-to-Production-Website-using-GKE |
| gpu_reference | https://github.com/JiahongChen/Set-up-deep-learning-frameworks-with-GPU-on-Google-Cloud-Platform |
| gpu_instance_reference | https://github.com/seem/blog/blob/main/tils/how-to-setup-a-gpu-instance-on-google-cloud-platform.qmd |
