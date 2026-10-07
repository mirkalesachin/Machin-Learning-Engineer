# Lab 4 — Feature Engineering, Feature Store, Labelling and Data Quality

> Course: AWS Certified Machine Learning Engineer Associate Training (TGS-2024049340)  |  Domain 01: Data Preparation for Machine Learning (28%)

## Objective

This lab develops your ability to engineer, store, label and validate features for machine learning (Domain 1: transform, engineer and validate data).

## Scenario

Turn cataloged data into trustworthy features: apply feature-engineering transforms in Data Wrangler, store reusable features in SageMaker Feature Store, review Ground Truth labelling, and validate quality and bias with Glue Data Quality and SageMaker Clarify.

## What you will build

A feature-engineering flow, an online/offline Feature Store design, and feature-engineering, data-quality and bias checklists.

## Architecture / workflow

Engineer features (Data Wrangler)  →  Store features (Feature Store)  →  Label data (Ground Truth)  →  Check quality (Glue DQ)  →  Check bias (Clarify)

## Services used

SageMaker Data Wrangler, Feature Store, Ground Truth, Clarify, AWS Glue, Glue Data Quality, Amazon Athena

## Prerequisites & cost safety

- An AWS account you are authorised to use (trainer-provided sandbox where available); MFA enabled.
- AWS Management Console plus AWS CloudShell or the AWS CLI for the command steps.
- A budget alert configured before you begin; use small datasets and short jobs.
- Delete paid resources (endpoints, training jobs, pipelines, temporary buckets) when a step says to.

## Step-by-step

1. Open SageMaker Data Wrangler (or review its docs) and list transforms: missing-value imputation, normalisation, standardisation, binning and one-hot encoding.
2. Apply a feature-engineering flow to a sample customer-churn dataset and export the prepared features back to S3.
3. Review SageMaker Feature Store and record online vs offline feature-store use cases and feature groups.

   ```bash
   aws sagemaker list-feature-groups
   ```

4. Create (or design) a feature group for the churn features so training and serving read the same definition.

   ```bash
   aws sagemaker describe-feature-group --feature-group-name tgs-mla-churn-features
   ```

5. Review SageMaker Ground Truth labelling jobs for text, image and tabular data, and human-in-the-loop review.

   ```bash
   aws sagemaker list-labeling-jobs
   ```

6. Run (or review) Glue Data Quality rules for nulls, ranges, uniqueness and freshness on the prepared data.
7. Review SageMaker Clarify concepts for pre-training data-bias detection (class imbalance and skew).
8. Create a feature-engineering checklist (imputation, scaling, encoding, leakage avoidance) for the churn dataset.
9. Create a data-quality checklist covering nulls, duplicates, schema mismatch, outliers, class imbalance and data leakage.
10. Save the feature flow, the Feature Store design and all three checklists as lab evidence.

## Evidence to capture

- Screenshots of each console screen and command output.
- The tables, checklists or design notes this lab asks you to produce.
- Any metrics, configuration values or ARNs you created.
- Save everything into your working folder: TGS-2024049340-AWS-MLA-Labs/.

## Troubleshooting

- **Features differ between train and serve** — Use Feature Store so both read the same definition.
- **Skewed classes bias the model** — Detect with Clarify; rebalance or reweight before training.
- **Data-quality rules keep failing** — Fix the source or the transform; re-run Glue Data Quality.

## Acceptance criteria

You can engineer features, store them for reuse in Feature Store, describe Ground Truth labelling, and validate a dataset for quality and bias with Glue Data Quality and Clarify.

## Clean up

Delete any paid resources you created in this lab (endpoints, training/tuning jobs, pipelines, temporary buckets) and confirm in Billing that nothing is still running.
