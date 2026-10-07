# Lab 11 — Model Monitoring, Drift and Observability

> Course: AWS Certified Machine Learning Engineer Associate Training (TGS-2024049340)  |  Domain 04: ML Solution Monitoring, Maintenance and Security (24%)

## Objective

This lab develops your ability to monitor a deployed model for drift and observe ML workloads in production (Domain 4: monitor and maintain ML solutions).

## Scenario

Keep a production model healthy: enable endpoint data capture, baseline and schedule SageMaker Model Monitor for the four drift types, wire CloudWatch metrics, logs and alarms, and design the drift-to-retrain loop.

## What you will build

A monitoring design with data capture, baselines, drift schedules, CloudWatch alarms and a drift-to-retrain plan.

## Architecture / workflow

Enable endpoint data capture  →  Baseline the data  →  Schedule Model Monitor  →  Wire CloudWatch alarms  →  Plan drift-triggered retraining

## Services used

SageMaker Model Monitor, SageMaker Clarify, Amazon CloudWatch, AWS CloudTrail, Amazon S3

## Prerequisites & cost safety

- An AWS account you are authorised to use (trainer-provided sandbox where available); MFA enabled.
- AWS Management Console plus AWS CloudShell or the AWS CLI for the command steps.
- A budget alert configured before you begin; use small datasets and short jobs.
- Delete paid resources (endpoints, training jobs, pipelines, temporary buckets) when a step says to.

## Step-by-step

1. Open SageMaker Model Monitor and review the four drift types: data quality, model quality, bias drift and feature-attribution drift.

   ```bash
   aws sagemaker list-monitoring-schedules --max-results 5
   ```

2. Enable data capture on an endpoint so inputs and outputs are logged to S3 for analysis.
3. Create a baseline from training/validation data for the data-quality monitor.
4. Schedule the monitor to compare captured data against the baseline on a schedule.
5. Open CloudWatch and review endpoint metrics, logs, alarms, dashboards and anomaly detection.

   ```bash
   aws cloudwatch describe-alarms --max-records 5
   ```

6. Create a CloudWatch alarm on latency, errors or a drift metric to trigger notification.

   ```bash
   aws cloudwatch put-metric-alarm --alarm-name tgs-mla-latency --namespace AWS/SageMaker --metric-name ModelLatency --threshold 1000 --comparison-operator GreaterThanThreshold --evaluation-periods 1 --period 300 --statistic Average
   ```

7. Open CloudTrail and review audit events for ML API calls for observability.

   ```bash
   aws cloudtrail lookup-events --max-results 5
   ```

8. Create a monitoring checklist for data drift, model quality, latency, errors, cost and security events.
9. Design the drift-to-retrain loop: detect drift → alarm → trigger pipeline → retrain → redeploy.
10. Save the monitoring design, alarm configuration and drift-to-retrain plan as lab evidence.

## Evidence to capture

- Screenshots of each console screen and command output.
- The tables, checklists or design notes this lab asks you to produce.
- Any metrics, configuration values or ARNs you created.
- Save everything into your working folder: TGS-2024049340-AWS-MLA-Labs/.

## Troubleshooting

- **No monitoring data appears** — Enable data capture on the endpoint before scheduling the monitor.
- **Monitor reports constant violations** — Rebuild the baseline from representative recent data.
- **Alarms never fire** — Check the CloudWatch metric, threshold and alarm state configuration.

## Acceptance criteria

You can enable data capture, baseline and schedule Model Monitor for the four drift types, wire CloudWatch alarms, and describe a drift-triggered retraining loop.

## Clean up

Delete any paid resources you created in this lab (endpoints, training/tuning jobs, pipelines, temporary buckets) and confirm in Billing that nothing is still running.
