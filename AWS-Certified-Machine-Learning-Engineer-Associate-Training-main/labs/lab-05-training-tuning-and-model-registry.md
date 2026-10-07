# Lab 05: Training, Tuning, and Model Registry

## Domain

ML Model Development

## Objective

Plan model training, hyperparameter tuning, model versioning, and registration with SageMaker.

## Scenario

The churn model has a baseline algorithm. The team needs repeatable training, tuning, and model approval before deployment.

## Tasks

### Task 1: Define Training Inputs

1. Training dataset location.
2. Validation dataset location.
3. Algorithm or training script.
4. Compute instance type.
5. Output artifact location.

### Task 2: Tune Hyperparameters

| Concept | Example |
| --- | --- |
| Search strategy | Random search or Bayesian optimization |
| Objective metric | Validation F1 score |
| Early stopping | Stop weak jobs early |
| Limits | Maximum jobs and parallel jobs |

### Task 3: Reduce Overfitting

1. Use validation data.
2. Apply regularization.
3. Reduce unnecessary features.
4. Use early stopping.
5. Compare training and validation metrics.

### Task 4: Register the Model

1. Create a model package group.
2. Register model artifacts and metrics.
3. Add approval status.
4. Record model version.
5. Link training data and code version.

## Validation

You have completed this lab when you can explain training jobs, tuning jobs, overfitting controls, and Model Registry use.

## Review Questions

1. What is a hyperparameter?
2. Why use validation data?
3. What is SageMaker Model Registry?
4. How does early stopping reduce cost?

## Cleanup

Delete tuning jobs, unused model artifacts, model package groups, and temporary S3 outputs if instructed.
