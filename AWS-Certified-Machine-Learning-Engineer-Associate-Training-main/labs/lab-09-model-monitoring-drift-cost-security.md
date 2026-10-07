# Lab 09: Model Monitoring, Drift, Cost, and Security

## Domain

ML Solution Monitoring, Maintenance, and Security

## Objective

Design monitoring, maintenance, cost optimization, and security controls for ML solutions.

## Scenario

The churn model is deployed. The team must detect model drift, monitor infrastructure, control cost, and secure ML resources.

## Tasks

### Task 1: Define Monitoring Signals

| Signal | Example |
| --- | --- |
| Model quality | Accuracy, F1, prediction distribution |
| Data quality | Missing values, schema drift |
| Bias drift | Changes in subgroup performance |
| Infrastructure | CPU, memory, latency, errors |
| Cost | Endpoint hours, training cost, storage |

### Task 2: Choose Monitoring Tools

1. Use SageMaker Model Monitor for data and model quality monitoring.
2. Use SageMaker Clarify for bias and explainability monitoring.
3. Use CloudWatch metrics, logs, dashboards, and alarms.
4. Use CloudTrail for audit evidence.

### Task 3: Optimize Cost

1. Delete idle endpoints.
2. Right-size endpoint instances.
3. Use autoscaling.
4. Use batch transform for offline scoring.
5. Consider spot training where appropriate.

### Task 4: Secure ML Resources

1. Apply least-privilege IAM.
2. Encrypt S3 buckets and model artifacts.
3. Use KMS keys where required.
4. Store secrets outside code.
5. Restrict network access for sensitive workloads.

## Validation

You have completed this lab when you can design monitoring schedules, alarms, cost controls, and security controls for an ML workload.

## Review Questions

1. What is data drift?
2. Which service monitors SageMaker model quality?
3. Why should idle endpoints be deleted?
4. Which service records API activity?

## Cleanup

Delete monitoring schedules, endpoints, dashboards, alarms, temporary roles, and test outputs created for this lab.
