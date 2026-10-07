# Lab 04: Modeling Approach and Algorithm Selection

## Domain

ML Model Development

## Objective

Choose the right modeling approach, AWS AI service, or SageMaker capability for business requirements.

## Scenario

A company has several AI needs: predict churn, classify support tickets, extract text from images, translate messages, and summarize documents.

## Tasks

### Task 1: Map Problems to Approaches

| Requirement | Possible Approach |
| --- | --- |
| Predict churn | Supervised classification |
| Forecast demand | Time series forecasting |
| Group customers | Clustering |
| Extract image labels | Rekognition or computer vision model |
| Translate text | Amazon Translate |
| Summarize documents | Amazon Bedrock foundation model |

### Task 2: Choose SageMaker Options

1. Use built-in algorithms when they match the problem.
2. Use script mode for custom frameworks.
3. Use JumpStart for prebuilt models and templates.
4. Use Bedrock for foundation model use cases.
5. Use managed AI services for common tasks when custom training is not required.

### Task 3: Consider Interpretability

1. Identify who needs to understand predictions.
2. Choose simpler models when explainability is required.
3. Plan feature importance analysis.
4. Document model selection tradeoffs.

### Task 4: Include Cost

1. Estimate training cost.
2. Estimate inference cost.
3. Compare managed service versus custom model cost.
4. Record assumptions.

## Validation

You have completed this lab when you can choose an AWS modeling option based on data, business need, interpretability, and cost.

## Review Questions

1. When should a managed AI service be used?
2. What is SageMaker JumpStart?
3. Why does interpretability matter?
4. How can cost affect model selection?

## Cleanup

Delete temporary notebooks, model artifacts, and experiment outputs created for this lab.
