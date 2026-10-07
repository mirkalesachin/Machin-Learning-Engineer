# Lab 9 — Deployment Options, Endpoints, Batch Transform and Auto Scaling

> Course: AWS Certified Machine Learning Engineer Associate Training (TGS-2024049340)  |  Domain 03: Deployment and Orchestration of ML Workflows (22%)

## Objective

This lab develops your ability to select and operate SageMaker inference infrastructure for a workload (Domain 3: deploy models).

## Scenario

Choose the right inference pattern: compare real-time endpoints, serverless inference, asynchronous inference and batch transform, understand endpoint configuration, auto scaling and safe delivery, and select infrastructure for several workloads.

## What you will build

An inference-option comparison table with use-case deployment choices and an auto-scaling and rollback checklist.

## Architecture / workflow

Pick the inference pattern  →  Create the endpoint config  →  Deploy the model  →  Register auto scaling  →  Verify metrics, then clean up

## Services used

SageMaker Inference, real-time & serverless endpoints, Batch Transform, Application Auto Scaling, CloudWatch

## Prerequisites & cost safety

- An AWS account you are authorised to use (trainer-provided sandbox where available); MFA enabled.
- AWS Management Console plus AWS CloudShell or the AWS CLI for the command steps.
- A budget alert configured before you begin; use small datasets and short jobs.
- Delete paid resources (endpoints, training jobs, pipelines, temporary buckets) when a step says to.

## Step-by-step

1. Open SageMaker Inference and review model artifact, container image, endpoint configuration and endpoint concepts.

   ```bash
   aws sagemaker list-endpoints --max-results 5
   ```

2. Review real-time endpoints (low, steady latency), serverless inference (spiky traffic) and asynchronous inference (large payloads).
3. Review batch transform for offline scoring of a whole dataset.

   ```bash
   aws sagemaker create-transform-job --cli-input-json file://batch-transform.json
   ```

4. Create an endpoint config and deploy a model to a real-time endpoint (sample model).

   ```bash
   aws sagemaker create-endpoint --endpoint-name tgs-mla-rt --endpoint-config-name tgs-mla-cfg
   ```

5. Register auto scaling on the endpoint using invocations-per-instance as the target metric.

   ```bash
   aws application-autoscaling register-scalable-target --service-namespace sagemaker --resource-id endpoint/tgs-mla-rt/variant/AllTraffic --scalable-dimension sagemaker:variant:DesiredInstanceCount --min-capacity 1 --max-capacity 4
   ```

6. Review blue/green, canary and shadow deployment and how deployment guardrails auto-roll-back on alarms.
7. Build an inference-option comparison table across latency, throughput, payload size, traffic pattern, cost, scaling and complexity.
8. Choose a deployment option for online fraud scoring, nightly batch scoring, image processing and bursty chatbot requests.
9. Identify where CloudWatch metrics and logs are collected for the endpoint.

   ```bash
   aws cloudwatch list-metrics --namespace AWS/SageMaker --metric-name Invocations
   ```

10. Delete the endpoint when finished and save the comparison and operations checklist as lab evidence.

   ```bash
   aws sagemaker delete-endpoint --endpoint-name tgs-mla-rt
   ```


## Evidence to capture

- Screenshots of each console screen and command output.
- The tables, checklists or design notes this lab asks you to produce.
- Any metrics, configuration values or ARNs you created.
- Save everything into your working folder: TGS-2024049340-AWS-MLA-Labs/.

## Troubleshooting

- **Endpoint stuck 'Creating' or fails** — Check the container/model artifact and the CloudWatch logs.
- **Latency spikes under load** — Enable auto scaling on the invocations-per-instance target.
- **Forgot to remove the endpoint** — Delete the endpoint and config to stop hourly charges.

## Acceptance criteria

You can select a SageMaker deployment option from latency, traffic, payload and cost requirements, and configure auto scaling and a rollback path for an endpoint.

## Clean up

Delete any paid resources you created in this lab (endpoints, training/tuning jobs, pipelines, temporary buckets) and confirm in Billing that nothing is still running.
