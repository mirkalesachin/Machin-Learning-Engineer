# Lab 02: Data Transformation and Feature Engineering

## Domain

Data Preparation for Machine Learning

## Objective

Transform raw data into model-ready features using AWS ML and analytics tools.

## Scenario

The churn dataset contains missing values, outliers, categorical columns, and numerical columns that need scaling.

## Tasks

### Task 1: Identify Cleaning Steps

1. Detect missing values.
2. Impute missing numerical values.
3. Treat outliers.
4. Deduplicate records.
5. Standardize date and currency fields.

### Task 2: Engineer Features

| Feature Type | Example Technique |
| --- | --- |
| Numeric | Scaling, normalization, log transform |
| Categorical | One-hot encoding, label encoding |
| Text | Tokenization, embeddings |
| Time-based | Day of week, month, recency |
| Aggregated | Average spend, event count |

### Task 3: Choose AWS Tools

| Need | AWS Tool |
| --- | --- |
| Visual preparation | SageMaker Data Wrangler |
| ETL at scale | AWS Glue or Spark |
| No-code cleaning | AWS Glue DataBrew |
| Feature reuse | SageMaker Feature Store |

### Task 4: Create a Feature Plan

1. List raw columns.
2. List derived features.
3. Define transformations.
4. Identify which features should be reused.
5. Decide whether online or offline feature storage is required.

## Validation

You have completed this lab when you can explain how raw data becomes model-ready features and which AWS tool fits each transformation need.

## Review Questions

1. What is feature engineering?
2. Why should categorical values be encoded?
3. When should Feature Store be used?
4. What is the difference between scaling and normalization?

## Cleanup

Delete temporary Glue jobs, DataBrew projects, Feature Store test groups, and processed files created for this lab.
