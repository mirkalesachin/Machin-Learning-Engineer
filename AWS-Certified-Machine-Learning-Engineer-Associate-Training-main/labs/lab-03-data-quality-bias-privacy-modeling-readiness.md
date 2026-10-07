# Lab 03: Data Quality, Bias, Privacy, and Modeling Readiness

## Domain

Data Preparation for Machine Learning

## Objective

Validate data integrity, reduce bias risks, and prepare datasets for model training.

## Scenario

Before training a model, the team must confirm that the dataset is complete, balanced, privacy-safe, and split correctly.

## Tasks

### Task 1: Define Data Quality Checks

| Check | Example |
| --- | --- |
| Completeness | Required fields are not null |
| Validity | Values are within accepted ranges |
| Uniqueness | Customer ID is not duplicated unexpectedly |
| Consistency | Date formats are standardized |
| Freshness | Data is recent enough for training |

### Task 2: Identify Bias Risks

1. Check class imbalance.
2. Check representation across important groups.
3. Check label quality.
4. Identify selection bias.
5. Document mitigation options.

### Task 3: Protect Sensitive Data

1. Identify PII or PHI.
2. Mask or anonymize sensitive fields.
3. Encrypt data at rest.
4. Restrict access with IAM.
5. Record data residency constraints.

### Task 4: Prepare Modeling Splits

1. Shuffle the dataset when appropriate.
2. Split into training, validation, and test sets.
3. Avoid leakage from future data.
4. Store split metadata for repeatability.

## Validation

You have completed this lab when you can define quality checks, bias checks, privacy controls, and repeatable dataset splits.

## Review Questions

1. What is class imbalance?
2. Why is data leakage harmful?
3. Which AWS service can help analyze bias?
4. Why should split metadata be retained?

## Cleanup

Delete temporary datasets, quality jobs, bias reports, and test outputs created for this lab.
