# Lab 10: Capstone: MLA-C01 Readiness Scenario

## Domain

Capstone

## Objective

Design an end-to-end AWS ML engineering solution and complete an MLA-C01 readiness review.

## Scenario

A company wants to build a customer churn prediction solution. The solution must ingest data, transform features, train and tune a model, evaluate performance, deploy inference, monitor drift, control costs, and secure resources.

## Tasks

### Task 1: Capture Requirements

The solution must:

1. Ingest batch and optional streaming data.
2. Store raw, processed, feature, and training data.
3. Validate data quality and privacy.
4. Engineer reusable features.
5. Train and tune a model.
6. Register the model.
7. Deploy real-time or batch inference.
8. Automate workflow steps.
9. Monitor quality, drift, cost, and infrastructure.
10. Secure data, models, and access.

### Task 2: Select Services

| Requirement | AWS Service Choice |
| --- | --- |
| Object storage | S3 |
| ETL and catalog | Glue |
| Visual data prep | SageMaker Data Wrangler |
| Feature reuse | SageMaker Feature Store |
| Bias analysis | SageMaker Clarify |
| Training and tuning | SageMaker Training and AMT |
| Model versioning | SageMaker Model Registry |
| Deployment | SageMaker endpoints or batch transform |
| Workflow | SageMaker Pipelines or Step Functions |
| Monitoring | Model Monitor, CloudWatch, CloudTrail |
| Security | IAM, KMS, VPC controls, Secrets Manager |

### Task 3: Present the Workflow

```text
Ingest data
Validate and transform data
Create features
Train and tune model
Evaluate model
Register and approve model
Deploy inference
Monitor quality and drift
Optimize cost
Secure and audit resources
```

### Task 4: Complete Readiness Checklist

| Topic | Status |
| --- | --- |
| Data formats and storage |  |
| Glue, Data Wrangler, DataBrew |  |
| Feature engineering and Feature Store |  |
| Data quality, bias, and privacy |  |
| Algorithm and AI service selection |  |
| Training, tuning, and registry |  |
| Evaluation metrics |  |
| Deployment patterns |  |
| Pipelines and CI/CD |  |
| Monitoring, drift, cost, and security |  |

## Validation

You have completed this lab when you can connect every design decision to an MLA-C01 domain and explain the complete ML lifecycle on AWS.

## Review Questions

1. Which services prepare data for modeling?
2. Which services support training and model versioning?
3. Which deployment option fits offline scoring?
4. Which controls secure model artifacts and data?

## Cleanup

Delete all capstone resources created in the AWS account, including endpoints, pipelines, model packages, monitoring schedules, buckets, logs, alarms, roles, and test artifacts.
