# Lab 5 — Modelling Approach, Algorithms and Managed AI Services

> Course: AWS Certified Machine Learning Engineer Associate Training (TGS-2024049340)  |  Domain 02: ML Model Development (26%)

## Objective

This lab develops your ability to choose an AWS modelling approach based on data, outcome, cost and operations (Domain 2: select a modelling approach).

## Scenario

Decide how to solve an ML problem before training: match problem types to approaches and compare SageMaker built-in algorithms, script-mode custom frameworks, JumpStart, Amazon Bedrock foundation models and managed AI services, then build a model/service selection matrix.

## What you will build

A model/service selection matrix for five business scenarios with cost and interpretability notes.

## Architecture / workflow

List the ML problem types  →  Map each to an algorithm/service  →  Compare built-in vs script vs BYOC  →  Review JumpStart & Bedrock  →  Score with a selection matrix

## Services used

Amazon SageMaker AI, SageMaker JumpStart, Amazon Bedrock, Rekognition, Comprehend, Textract, Translate, Transcribe

## Prerequisites & cost safety

- An AWS account you are authorised to use (trainer-provided sandbox where available); MFA enabled.
- AWS Management Console plus AWS CloudShell or the AWS CLI for the command steps.
- A budget alert configured before you begin; use small datasets and short jobs.
- Delete paid resources (endpoints, training jobs, pipelines, temporary buckets) when a step says to.

## Step-by-step

1. List the common ML problem types: classification, regression, clustering, forecasting, anomaly detection, NLP and computer vision.
2. Review SageMaker built-in algorithm categories and when each is a good fit.
3. Review script mode for custom frameworks such as TensorFlow, PyTorch and scikit-learn, and Bring Your Own Container.
4. Open SageMaker JumpStart and browse prebuilt models and solution templates you can deploy or fine-tune.

   ```bash
   aws sagemaker list-models --max-results 5
   ```

5. Open Amazon Bedrock and review foundation-model use cases (text generation, summarisation, RAG) if available.

   ```bash
   aws bedrock list-foundation-models --query 'modelSummaries[0:5].modelId'
   ```

6. Review managed AI services: Rekognition, Comprehend, Textract, Translate and Transcribe, and their standard tasks.
7. Build a model/service selection table for five business scenarios, capturing data type, expected output, candidate service, interpretability need, cost and operational complexity.
8. Identify when a managed AI service is better than training a custom model.
9. Identify when a SageMaker training job is the more appropriate choice.
10. Save the selection matrix and the cost/interpretability notes as lab evidence.

## Evidence to capture

- Screenshots of each console screen and command output.
- The tables, checklists or design notes this lab asks you to produce.
- Any metrics, configuration values or ARNs you created.
- Save everything into your working folder: TGS-2024049340-AWS-MLA-Labs/.

## Troubleshooting

- **Unsure which algorithm fits** — Match the problem type first (class/reg/cluster/forecast), then data size.
- **AI service accuracy too low for the domain** — Fine-tune (JumpStart/Bedrock) or train a custom model.
- **Options hard to compare** — Add cost, interpretability and ops columns to the selection matrix.

## Acceptance criteria

You can choose an AWS modelling approach for a given business outcome and justify it against data, cost, interpretability and operational requirements.

## Clean up

Delete any paid resources you created in this lab (endpoints, training/tuning jobs, pipelines, temporary buckets) and confirm in Billing that nothing is still running.
