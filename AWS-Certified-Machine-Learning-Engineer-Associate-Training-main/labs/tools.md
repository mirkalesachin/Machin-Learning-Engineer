# Lab Tools and Setup

## Required Tools

- AWS account or instructor-provided sandbox
- AWS CLI v2
- Python 3.11
- JupyterLab or SageMaker Studio access
- Git
- Visual Studio Code or equivalent editor

## AWS CLI Setup

```bash
aws configure --profile c1330
aws sts get-caller-identity --profile c1330
```

Set default variables:

```bash
export AWS_PROFILE=c1330
export AWS_REGION=ap-southeast-1
```

For Windows PowerShell:

```powershell
$env:AWS_PROFILE = "c1330"
$env:AWS_REGION = "ap-southeast-1"
```

## Suggested Python Packages

```bash
pip install boto3 pandas numpy scikit-learn matplotlib sagemaker
```

Use managed SageMaker environments when available.

## Naming Standard

```text
c1330-<learner-prefix>-<service>-<purpose>
```

## Cost Control

1. Use the assigned Region only.
2. Stop notebooks and Studio apps when finished.
3. Delete endpoints after deployment labs.
4. Use small datasets and small instance types unless instructed.
5. Empty temporary S3 buckets before deleting them.

## Offline Completion

If live AWS access is unavailable:

1. Complete the design tables.
2. Draft expected commands or notebook steps.
3. Explain service choices.
4. Complete validation and review questions.
5. Record exam decision points.
