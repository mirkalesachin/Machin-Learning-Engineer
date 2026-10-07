# Lab 8 — Model Evaluation, Metrics, Bias and Explainability

> Course: AWS Certified Machine Learning Engineer Associate Training (TGS-2024049340)  |  Domain 02: ML Model Development (26%)

## Objective

This lab develops your ability to choose metrics, interpret results and check bias and explainability before approval (Domain 2: evaluate model performance).

## Scenario

Decide whether a model is fit to promote: compare classification and regression metrics, diagnose overfitting/underfitting and leakage, review Clarify bias and SHAP explainability, and write an evaluation and acceptance checklist.

## What you will build

An evaluation plan and model-acceptance checklist with metric thresholds and bias/explainability checks.

## Architecture / workflow

Split train/validation/test  →  Compute metrics (confusion matrix)  →  Diagnose over/underfitting  →  Check bias & SHAP (Clarify)  →  Set acceptance thresholds

## Services used

SageMaker Clarify, SageMaker training/evaluation, Amazon S3, Model Cards

## Prerequisites & cost safety

- An AWS account you are authorised to use (trainer-provided sandbox where available); MFA enabled.
- AWS Management Console plus AWS CloudShell or the AWS CLI for the command steps.
- A budget alert configured before you begin; use small datasets and short jobs.
- Delete paid resources (endpoints, training jobs, pipelines, temporary buckets) when a step says to.

## Step-by-step

1. Build a table of classification metrics: accuracy, precision, recall, F1 score, ROC AUC and the confusion matrix.
2. Add regression metrics: MAE, MSE, RMSE and R-squared, and note when each is preferred.
3. Review what overfitting and underfitting look like across training and validation metrics.
4. Review class imbalance and data-leakage examples and how they distort metrics.
5. Open SageMaker Clarify (or its docs) and record pre- and post-training bias metrics.

   ```bash
   aws sagemaker list-processing-jobs --name-contains clarify --max-results 5
   ```

6. Review feature-importance and SHAP-value concepts for model explainability, and Model Cards for documentation.
7. Design an evaluation plan for a binary classification model with a train/validation/test split strategy.
8. Define minimum acceptable metrics and the approval criteria for promoting the model.
9. Define the bias, fairness and explainability checks that must pass before approval.
10. Save the evaluation plan and acceptance checklist as lab evidence.

## Evidence to capture

- Screenshots of each console screen and command output.
- The tables, checklists or design notes this lab asks you to produce.
- Any metrics, configuration values or ARNs you created.
- Save everything into your working folder: TGS-2024049340-AWS-MLA-Labs/.

## Troubleshooting

- **High accuracy but poor real performance** — Data is likely imbalanced or leaking — use F1 and recheck features.
- **Metrics differ sharply train vs test** — Overfitting — regularise, add data or simplify the model.
- **Model unfair across groups** — Use Clarify bias metrics and mitigate before approval.

## Acceptance criteria

You can select appropriate metrics, interpret evaluation results, check bias and explainability, and decide whether a model is ready for approval or needs more data preparation or tuning.

## Clean up

Delete any paid resources you created in this lab (endpoints, training/tuning jobs, pipelines, temporary buckets) and confirm in Billing that nothing is still running.
