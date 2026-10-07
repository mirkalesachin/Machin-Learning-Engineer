# Lab 6 — SageMaker Training Jobs and Debugger

> Course: AWS Certified Machine Learning Engineer Associate Training (TGS-2024049340)  |  Domain 02: ML Model Development (26%)

## Objective

This lab develops your ability to configure, run and debug a SageMaker training job efficiently (Domain 2: train models).

## Scenario

Run the training step end to end: configure input channels, instance, container and execution role, understand the training knobs and regularisation, choose input modes and cost options, and use SageMaker Debugger and Profiler to catch training problems early.

## What you will build

A configured, running training job plus Debugger/Profiler findings and a training-configuration checklist.

## Architecture / workflow

Configure the training job  →  Choose input mode & instance  →  Launch a script-mode job  →  Watch Debugger rules  →  Review Profiler & cost

## Services used

SageMaker Training, SageMaker Debugger, SageMaker Profiler, Amazon S3, Managed Spot training

## Prerequisites & cost safety

- An AWS account you are authorised to use (trainer-provided sandbox where available); MFA enabled.
- AWS Management Console plus AWS CloudShell or the AWS CLI for the command steps.
- A budget alert configured before you begin; use small datasets and short jobs.
- Delete paid resources (endpoints, training jobs, pipelines, temporary buckets) when a step says to.

## Step-by-step

1. Open SageMaker Training and review input channels, output path, instance type, container image and execution role.

   ```bash
   aws sagemaker list-training-jobs --max-results 5
   ```

2. Record the meaning of epoch, batch size, learning rate, steps and early stopping.
3. Compare input modes — File, Pipe and FastFile — and when each reduces start time or disk use.
4. Launch a small sample training job (script mode) and watch its status to completion.

   ```bash
   aws sagemaker describe-training-job --training-job-name tgs-mla-demo-train --query 'TrainingJobStatus'
   ```

5. Review regularisation techniques — L1, L2, dropout, pruning and feature selection — and how they curb overfitting.
6. Enable SageMaker Debugger built-in rules (vanishing gradients, overfitting, loss-not-decreasing) on the job.

   ```bash
   aws sagemaker describe-training-job --training-job-name tgs-mla-demo-train --query 'DebugRuleEvaluationStatuses'
   ```

7. Review the SageMaker Profiler report to spot GPU/CPU under-utilisation and I/O bottlenecks.
8. Review Managed Spot training and checkpointing to cut training cost on interruptible jobs.
9. Create a training-configuration checklist (channels, instance, container, role, hyperparameters, monitoring).
10. Save the training-job configuration, Debugger/Profiler findings and the checklist as lab evidence.

## Evidence to capture

- Screenshots of each console screen and command output.
- The tables, checklists or design notes this lab asks you to produce.
- Any metrics, configuration values or ARNs you created.
- Save everything into your working folder: TGS-2024049340-AWS-MLA-Labs/.

## Troubleshooting

- **Training job fails to start** — Check the execution role, input channels and instance limits.
- **Validation loss diverges** — Lower the learning rate; add regularisation and early stopping.
- **Job is slow / GPU under-used** — Use the Profiler to find I/O or utilisation bottlenecks.

## Acceptance criteria

You can configure and launch a SageMaker training job, apply regularisation and cost options, and use Debugger and the Profiler to diagnose training problems.

## Clean up

Delete any paid resources you created in this lab (endpoints, training/tuning jobs, pipelines, temporary buckets) and confirm in Billing that nothing is still running.
