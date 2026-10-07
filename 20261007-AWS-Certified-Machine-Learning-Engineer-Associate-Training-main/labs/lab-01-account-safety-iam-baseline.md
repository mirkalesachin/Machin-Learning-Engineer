# Lab 1 — Account Safety and IAM Baseline

> Course: AWS Certified Machine Learning Engineer Associate Training (TGS-2024049340)  |  Domain 01: Data Preparation for Machine Learning (28%)

## Objective

This lab develops your ability to secure an AWS ML workspace with identity, least-privilege IAM and cost guardrails (Domain 1: establish a safe ML foundation).

## Scenario

Set up a safe AWS baseline for ML engineering: confirm identity and Region, review IAM users, roles, groups and least privilege, understand the SageMaker execution role, enable MFA and a budget alert, and review KMS key concepts before any data lands.

## What you will build

A secured AWS ML workspace: verified identity/Region, a least-privilege IAM review, an enabled budget alert and notes on execution roles and KMS.

## Architecture / workflow

Sign in & verify identity/Region  →  Review IAM roles & least privilege  →  Review the SageMaker execution role  →  Enable MFA & a budget alert  →  Review KMS key concepts

## Services used

IAM, AWS KMS, AWS Budgets, Amazon SageMaker AI, AWS CloudShell, AWS CloudTrail

## Prerequisites & cost safety

- An AWS account you are authorised to use (trainer-provided sandbox where available); MFA enabled.
- AWS Management Console plus AWS CloudShell or the AWS CLI for the command steps.
- A budget alert configured before you begin; use small datasets and short jobs.
- Delete paid resources (endpoints, training jobs, pipelines, temporary buckets) when a step says to.

## Step-by-step

1. Sign in to the assigned AWS account and confirm your identity and Region before creating anything.

   ```bash
   aws sts get-caller-identity
   ```

2. Confirm the Region you are working in so every resource is created consistently.

   ```bash
   aws configure list
   ```

3. Review IAM users, groups, roles and attached policies in the account.

   ```bash
   aws iam list-roles --query 'Roles[?contains(RoleName,`SageMaker`)].RoleName'
   ```

4. Review least-privilege access for S3, SageMaker, Glue, Athena, KMS and CloudWatch, and note where each is over- or under-scoped.
5. Review the SageMaker execution-role concept: the role SageMaker assumes to read data from S3 and write model artifacts.

   ```bash
   aws iam get-role --role-name <SageMakerExecutionRole> --query 'Role.AssumeRolePolicyDocument'
   ```

6. Confirm MFA is enabled where permitted for human sign-in.

   ```bash
   aws iam list-mfa-devices
   ```

7. Create (or confirm) a monthly budget alert so a runaway training job or endpoint cannot cause a surprise bill.

   ```bash
   aws budgets describe-budgets --account-id <ACCOUNT_ID>
   ```

8. Review AWS KMS customer-managed-key concepts and how KMS keys protect S3 and SageMaker artifacts.

   ```bash
   aws kms list-keys --query 'Keys[0]'
   ```

9. Review CloudTrail to confirm that ML API calls are being audited in the account.

   ```bash
   aws cloudtrail describe-trails --query 'trailList[0].Name'
   ```

10. Save your identity, Region, IAM least-privilege, execution-role, MFA, budget and KMS notes as lab evidence.

## Evidence to capture

- Screenshots of each console screen and command output.
- The tables, checklists or design notes this lab asks you to produce.
- Any metrics, configuration values or ARNs you created.
- Save everything into your working folder: TGS-2024049340-AWS-MLA-Labs/.

## Troubleshooting

- **Access denied calling an ML API** — Attach a least-privilege policy for that action to your role/user.
- **SageMaker cannot read S3** — Fix the SageMaker execution role's S3 permissions and trust policy.
- **Surprise charges appear** — Enable AWS Budgets alerts and delete idle resources immediately.

## Acceptance criteria

You can verify your identity and Region, explain least-privilege IAM and the SageMaker execution role, and confirm MFA, a budget alert and KMS are in place before any ML data lands.

## Clean up

Delete any paid resources you created in this lab (endpoints, training/tuning jobs, pipelines, temporary buckets) and confirm in Billing that nothing is still running.
