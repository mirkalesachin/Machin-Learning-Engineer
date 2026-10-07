# Lab 01: ML Data Ingestion and Storage on AWS

## Domain

Data Preparation for Machine Learning

## Objective

Select AWS storage and ingestion patterns for machine learning datasets.

## Scenario

A team needs to prepare customer churn data for ML modeling. Data arrives as CSV exports, JSON application events, and streaming click events.

## Tasks

### Task 1: Compare Data Sources

| Source | AWS Service Option | Notes |
| --- | --- | --- |
| Object files | S3 | Common ML data lake storage |
| Relational data | RDS or Aurora | Use extracts or connectors |
| NoSQL data | DynamoDB | Export or stream changes |
| Streaming events | Kinesis, MSK, or managed Flink | Use for near-real-time data |

### Task 2: Choose Data Formats

1. Choose CSV for simple interchange.
2. Choose JSON for semi-structured records.
3. Choose Parquet or ORC for analytics and columnar access.
4. Choose RecordIO when the training algorithm requires it.
5. Record the cost and performance tradeoffs.

### Task 3: Design an S3 Layout

```text
s3://c1330-learner01-ml-data/raw/
s3://c1330-learner01-ml-data/processed/
s3://c1330-learner01-ml-data/features/
s3://c1330-learner01-ml-data/training/
```

### Task 4: Plan Ingestion

1. Define batch ingestion.
2. Define streaming ingestion.
3. Identify validation checks before data lands in the training zone.
4. Decide whether SageMaker Data Wrangler or Glue should prepare the data.

## Validation

You have completed this lab when you can justify storage, format, and ingestion decisions for ML data.

## Review Questions

1. Why is Parquet useful for analytics workloads?
2. When should streaming ingestion be used?
3. What is the purpose of raw and processed zones?
4. Which AWS service can catalog datasets?

## Cleanup

Delete any temporary buckets, files, and test streams created for this lab.
