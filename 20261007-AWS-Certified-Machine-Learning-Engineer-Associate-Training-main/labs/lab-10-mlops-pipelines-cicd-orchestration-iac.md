# Lab 10 — MLOps Pipelines, CI/CD, Orchestration and IaC

> Course: AWS Certified Machine Learning Engineer Associate Training (TGS-2024049340)  |  Domain 03: Deployment and Orchestration of ML Workflows (22%)

## Objective

This lab develops your ability to design an automated, gated ML workflow from data to monitored production (Domain 3: orchestrate ML workflows).

## Scenario

Automate the ML lifecycle: compare SageMaker Pipelines, Step Functions, CodePipeline and EventBridge, design an end-to-end pipeline with approval and rollback gates, and identify where Infrastructure as Code and version control fit.

## What you will build

An end-to-end MLOps pipeline design with approval, failure paths, rollback, CI/CD and IaC touchpoints.

## Architecture / workflow

Define the pipeline steps  →  Add a condition & register step  →  Add a human approval gate  →  Wire CI/CD and event triggers  →  Provision with IaC

## Services used

SageMaker Pipelines, AWS Step Functions, CodePipeline, CodeBuild, EventBridge, CloudFormation/CDK

## Prerequisites & cost safety

- An AWS account you are authorised to use (trainer-provided sandbox where available); MFA enabled.
- AWS Management Console plus AWS CloudShell or the AWS CLI for the command steps.
- A budget alert configured before you begin; use small datasets and short jobs.
- Delete paid resources (endpoints, training jobs, pipelines, temporary buckets) when a step says to.

## Step-by-step

1. Open SageMaker Pipelines and review steps: processing, training, tuning, condition, register model and callback.

   ```bash
   aws sagemaker list-pipelines --max-results 5
   ```

2. Open Step Functions and review state-machine workflow orchestration for ML.

   ```bash
   aws stepfunctions list-state-machines --max-results 5
   ```

3. Open CodePipeline and CodeBuild and review CI/CD build/test/deploy concepts for ML.

   ```bash
   aws codepipeline list-pipelines
   ```

4. Open EventBridge and review event-driven triggers (e.g. new data arriving, model approved).

   ```bash
   aws events list-rules --limit 5
   ```

5. Build a comparison table for SageMaker Pipelines, Step Functions, CodePipeline and EventBridge.
6. Design an ML pipeline with ingest, validate, feature-engineering, train, tune, evaluate, register, approve, deploy and monitor steps.
7. Add failure paths, retries and a rollback path to the pipeline.
8. Add a human approval gate for model promotion before deployment.
9. Identify where IaC (CloudFormation, CDK or SageMaker project templates) provisions the pipeline, and where version control and artifact storage are used.

   ```bash
   aws cloudformation list-stacks --query 'StackSummaries[0:5].StackName'
   ```

10. Save the pipeline design, the orchestrator comparison and the CI/CD/IaC touchpoints as lab evidence.

## Evidence to capture

- Screenshots of each console screen and command output.
- The tables, checklists or design notes this lab asks you to produce.
- Any metrics, configuration values or ARNs you created.
- Save everything into your working folder: TGS-2024049340-AWS-MLA-Labs/.

## Troubleshooting

- **A pipeline step fails midway** — Add retries and inspect that step's CloudWatch logs.
- **A bad model reaches production** — Add a condition step and a human approval gate before deploy.
- **Environment drifts between runs** — Provision with CloudFormation/CDK and pin versions.

## Acceptance criteria

You can describe an automated ML workflow that moves models from development to production safely, with CI/CD, approval, retries, rollback and Infrastructure as Code.

## Clean up

Delete any paid resources you created in this lab (endpoints, training/tuning jobs, pipelines, temporary buckets) and confirm in Billing that nothing is still running.
