# Learner Guide: C1330 AWS Certified Machine Learning Engineer Associate Training

## Guide Overview

This learner guide provides a step-by-step path through the AWS Certified Machine Learning Engineer Associate labs. The labs are grouped by the MLA-C01 exam domains: Data Preparation for Machine Learning, ML Model Development, Deployment and Orchestration of ML Workflows, and ML Solution Monitoring, Maintenance, and Security.

The course is designed for learners with basic cloud, data, and machine learning knowledge who want practical AWS ML engineering skills.

## Learning Outcomes

By the end of this guide, learners will be able to:

- Ingest, store, transform, and validate ML data on AWS.
- Select data formats, storage services, and transformation tools based on access patterns.
- Engineer features and prepare datasets for training.
- Identify data quality, privacy, compliance, and bias risks.
- Select modeling approaches, SageMaker algorithms, AI services, foundation models, and solution templates.
- Train, tune, evaluate, version, and register ML models.
- Choose deployment infrastructure for real-time, batch, async, and serverless inference.
- Build repeatable ML workflows with SageMaker Pipelines, Step Functions, CI/CD, and IaC concepts.
- Monitor inference, model quality, data drift, infrastructure, cost, and security controls.

## Recommended 3-Day Flow

| Day | Labs | Domain Focus |
| --- | --- | --- |
| Day 1 | Labs 01-03 | Data ingestion, transformation, feature engineering, quality, bias, privacy |
| Day 2 | Labs 04-06 | Modeling approach, training, tuning, registry, evaluation |
| Day 3 | Labs 07-10 | Deployment, workflow orchestration, monitoring, security, capstone |

## Before You Start

### Step 1: Confirm AWS Access

1. Confirm whether you are using your own AWS account or an instructor sandbox.
2. Confirm the AWS Region for all labs.
3. Confirm whether SageMaker Studio is available.
4. Record your learner prefix.

```text
Region: ap-southeast-1
Prefix: learner01
SageMaker Studio: available
```

### Step 2: Configure Tools

1. Install AWS CLI v2.
2. Install Python 3.11.
3. Install Git.
4. Install a code editor.
5. Confirm access to JupyterLab or SageMaker Studio.
6. Review [Lab Tools and Setup](labs/tools.md).

### Step 3: Configure AWS CLI

```bash
aws configure --profile c1330
aws sts get-caller-identity --profile c1330
```

Set environment variables:

```bash
export AWS_PROFILE=c1330
export AWS_REGION=ap-southeast-1
```

For Windows PowerShell:

```powershell
$env:AWS_PROFILE = "c1330"
$env:AWS_REGION = "ap-southeast-1"
```

### Step 4: Use Consistent Resource Names

```text
c1330-<learner-prefix>-<service>-<purpose>
```

Examples:

```text
c1330-learner01-s3-ml-data
c1330-learner01-sm-training
c1330-learner01-pipeline-churn
```

## Domain Study Path

### Data Preparation for Machine Learning

Complete Labs 01-03.

Focus on:

- Data formats such as CSV, JSON, Parquet, ORC, Avro, and RecordIO.
- Ingestion from S3, databases, streams, and feature stores.
- Transformation with Glue, Spark, Data Wrangler, and DataBrew.
- Feature engineering, encoding, scaling, splitting, labeling, and data quality.
- Bias, PII, PHI, masking, anonymization, and encryption.

### ML Model Development

Complete Labs 04-06.

Focus on:

- Choosing between built-in algorithms, custom code, AI services, foundation models, and JumpStart.
- Training concepts such as epoch, batch size, steps, overfitting, underfitting, and regularization.
- Hyperparameter tuning with search strategies.
- Model versioning and SageMaker Model Registry.
- Evaluation metrics such as accuracy, precision, recall, F1 score, ROC-AUC, RMSE, and confusion matrix.

### Deployment and Orchestration of ML Workflows

Complete Labs 07-08.

Focus on:

- Real-time, serverless, asynchronous, and batch inference.
- Endpoint instance selection, autoscaling, blue-green and canary deployment concepts.
- SageMaker Pipelines, Step Functions, EventBridge, CodePipeline, CodeBuild, and IaC.
- Reproducible workflow steps for data, training, evaluation, approval, and deployment.

### ML Solution Monitoring, Maintenance, and Security

Complete Lab 09.

Focus on:

- Model quality, data quality, bias drift, and feature drift.
- CloudWatch metrics, logs, alarms, and dashboards.
- SageMaker Model Monitor and Clarify monitoring concepts.
- Cost optimization, right-sizing, autoscaling, spot training, and cleanup.
- IAM least privilege, encryption, VPC access, secrets, and audit logs.

## Lab Reporting Template

```text
Lab number:
Domain:
Scenario:
AWS services:
Dataset or model:
Design decisions:
Validation evidence:
Monitoring evidence:
Security notes:
Cleanup completed:
Exam notes:
```

## Cleanup Checklist

1. Stop notebooks and Studio apps when finished.
2. Delete SageMaker endpoints that are not required.
3. Delete training jobs only if instructed; otherwise record job names for review.
4. Empty and delete temporary S3 buckets.
5. Delete pipelines, model packages, monitoring schedules, and test alarms.
6. Delete temporary IAM roles, policies, parameters, and secrets.
7. Confirm no billable endpoint remains running.

## References

- [AWS Certified Machine Learning Engineer - Associate Exam Guide](https://docs.aws.amazon.com/pdfs/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01.pdf)
- [AWS Certified Machine Learning Engineer Associate Training](https://www.tertiarycourses.com.sg/aws-certified-machine-learning-engineer-associate-exam-prep.html)
