# Lab 7 — Automatic Model Tuning, Experiments and Model Registry

> Course: AWS Certified Machine Learning Engineer Associate Training (TGS-2024049340)  |  Domain 02: ML Model Development (26%)

## Objective

This lab develops your ability to run repeatable tuning, track experiments and version-control models (Domain 2: tune and manage models).

## Scenario

Make model development repeatable: design an Automatic Model Tuning plan and compare search strategies, track trials with SageMaker Experiments, and version models through the Model Registry with an approval workflow.

## What you will build

A tuning plan, an experiment-tracking scheme and a model-versioning workflow from training job to approved model package.

## Architecture / workflow

Define the objective metric  →  Choose a search strategy  →  Tune with AMT  →  Track trials in Experiments  →  Register & approve the model

## Services used

SageMaker Automatic Model Tuning, SageMaker Experiments, SageMaker Model Registry, Amazon S3

## Prerequisites & cost safety

- An AWS account you are authorised to use (trainer-provided sandbox where available); MFA enabled.
- AWS Management Console plus AWS CloudShell or the AWS CLI for the command steps.
- A budget alert configured before you begin; use small datasets and short jobs.
- Delete paid resources (endpoints, training jobs, pipelines, temporary buckets) when a step says to.

## Step-by-step

1. Open Automatic Model Tuning and compare random search, grid search, Bayesian optimisation and Hyperband.
2. Create a tuning plan for a sample classification model: objective metric, hyperparameters, ranges, stopping condition and cost limit.

   ```bash
   aws sagemaker create-hyper-parameter-tuning-job --cli-input-json file://tuning.json
   ```

3. Launch (or review) a small tuning job and watch the best training job emerge.

   ```bash
   aws sagemaker describe-hyper-parameter-tuning-job --hyper-parameter-tuning-job-name tgs-mla-tune --query 'BestTrainingJob.TrainingJobName'
   ```

4. Open SageMaker Experiments and record how trials, parameters and metrics are tracked for reproducibility.

   ```bash
   aws sagemaker list-experiments --max-results 5
   ```

5. Compare candidate trials by the objective metric and select the best model.
6. Open the Model Registry and create a model package group for the model.

   ```bash
   aws sagemaker create-model-package-group --model-package-group-name tgs-mla-churn
   ```

7. Register a trained model version with metrics and metadata in the group.

   ```bash
   aws sagemaker list-model-packages --model-package-group-name tgs-mla-churn
   ```

8. Set the model version's approval status to gate promotion to deployment.

   ```bash
   aws sagemaker update-model-package --model-package-arn <arn> --model-approval-status Approved
   ```

9. Design the model-versioning workflow from training to tuning to registered, approved package.
10. Save the tuning plan, the experiment-tracking scheme and the versioning workflow as lab evidence.

## Evidence to capture

- Screenshots of each console screen and command output.
- The tables, checklists or design notes this lab asks you to produce.
- Any metrics, configuration values or ARNs you created.
- Save everything into your working folder: TGS-2024049340-AWS-MLA-Labs/.

## Troubleshooting

- **Tuning is too expensive** — Cap max/parallel jobs and narrow the hyperparameter ranges.
- **Best trial is hard to find** — Track runs in SageMaker Experiments and sort by the objective metric.
- **Wrong model reaches deploy** — Gate promotion with a Model Registry approval status.

## Acceptance criteria

You can define a tuning plan, track trials in Experiments, and register and approve a model version in the Model Registry as a repeatable workflow.

## Clean up

Delete any paid resources you created in this lab (endpoints, training/tuning jobs, pipelines, temporary buckets) and confirm in Billing that nothing is still running.
