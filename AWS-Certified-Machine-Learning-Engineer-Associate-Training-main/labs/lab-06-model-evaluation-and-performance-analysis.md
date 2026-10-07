# Lab 06: Model Evaluation and Performance Analysis

## Domain

ML Model Development

## Objective

Evaluate model performance and decide whether a model is ready for deployment.

## Scenario

Two churn models have completed training. You must compare metrics, identify performance risks, and recommend which model should be approved.

## Tasks

### Task 1: Select Metrics

| Problem Type | Example Metrics |
| --- | --- |
| Classification | Accuracy, precision, recall, F1, ROC-AUC |
| Regression | MAE, MSE, RMSE, R-squared |
| Ranking | NDCG, precision at K |
| Forecasting | MAPE, RMSE |

### Task 2: Interpret Confusion Matrix

1. Identify true positives.
2. Identify false positives.
3. Identify true negatives.
4. Identify false negatives.
5. Decide which error is more costly.

### Task 3: Check Model Fit

1. Compare training and validation metrics.
2. Identify overfitting.
3. Identify underfitting.
4. Recommend tuning or feature changes.

### Task 4: Explain Model Behavior

1. Review feature importance.
2. Identify unexpected drivers.
3. Check subgroup performance.
4. Document risks before approval.

## Validation

You have completed this lab when you can select evaluation metrics, interpret confusion matrix outcomes, and recommend approval or retraining.

## Review Questions

1. When is recall more important than precision?
2. What does overfitting look like?
3. Why compare subgroup performance?
4. What should be documented before model approval?

## Cleanup

Delete temporary reports, evaluation outputs, and unused model artifacts created for this lab.
