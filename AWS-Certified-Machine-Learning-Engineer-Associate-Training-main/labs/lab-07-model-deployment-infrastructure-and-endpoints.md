# Lab 07: Model Deployment Infrastructure and Endpoints

## Domain

Deployment and Orchestration of ML Workflows

## Objective

Choose deployment infrastructure and inference patterns for ML models.

## Scenario

The approved churn model must serve predictions for an application. Some predictions are real time, while others can run as nightly batches.

## Tasks

### Task 1: Compare Inference Patterns

| Pattern | Best Fit |
| --- | --- |
| Real-time endpoint | Low-latency online prediction |
| Serverless inference | Intermittent traffic |
| Asynchronous inference | Large payloads or longer processing |
| Batch transform | Offline batch scoring |

### Task 2: Choose Compute

1. Estimate latency requirement.
2. Estimate request volume.
3. Choose instance type or serverless option.
4. Plan autoscaling.
5. Define endpoint monitoring.

### Task 3: Plan Deployment Safety

1. Use model package approval.
2. Deploy to staging first.
3. Use canary or blue-green concepts.
4. Monitor errors and latency.
5. Roll back if alarms trigger.

### Task 4: Define Endpoint Security

1. Use least-privilege IAM.
2. Encrypt model artifacts.
3. Restrict network access when required.
4. Avoid logging sensitive payloads.

## Validation

You have completed this lab when you can select an inference pattern and explain deployment, scaling, monitoring, and security choices.

## Review Questions

1. When is batch transform appropriate?
2. When is serverless inference useful?
3. Why use canary deployment?
4. What should trigger rollback?

## Cleanup

Delete all SageMaker endpoints, endpoint configurations, test models, and temporary artifacts created for this lab.
