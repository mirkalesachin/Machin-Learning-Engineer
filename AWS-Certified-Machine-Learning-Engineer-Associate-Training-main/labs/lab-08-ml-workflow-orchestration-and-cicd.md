# Lab 08: ML Workflow Orchestration and CI/CD

## Domain

Deployment and Orchestration of ML Workflows

## Objective

Design an automated ML workflow from data preparation through model approval and deployment.

## Scenario

The team wants repeatable ML releases. Manual notebook steps must become a controlled pipeline.

## Tasks

### Task 1: Define Workflow Steps

```text
Ingest data
Validate data
Transform features
Train model
Evaluate model
Register model
Approve model
Deploy model
Monitor model
```

### Task 2: Choose Orchestration Services

| Need | AWS Service |
| --- | --- |
| ML pipeline steps | SageMaker Pipelines |
| General workflow | Step Functions |
| CI/CD pipeline | CodePipeline |
| Build and test | CodeBuild |
| Events and schedules | EventBridge |
| Infrastructure as code | CloudFormation, CDK, or SAM |

### Task 3: Add CI/CD Controls

1. Store code in Git.
2. Run unit tests.
3. Validate IaC templates.
4. Package training and inference code.
5. Require approval before production deployment.

### Task 4: Track Reproducibility

1. Record dataset version.
2. Record code commit.
3. Record training parameters.
4. Record model artifact location.
5. Record evaluation metrics.

## Validation

You have completed this lab when you can design a repeatable ML workflow with orchestration, CI/CD, approval, and traceability.

## Review Questions

1. What is SageMaker Pipelines?
2. Why should manual notebook steps be automated?
3. What metadata supports reproducibility?
4. Where should approval occur?

## Cleanup

Delete test pipelines, workflow executions, build projects, event rules, and temporary artifacts created for this lab.
