# Lab 12 — Security, Governance, Cost Optimisation and Exam Review

> Course: AWS Certified Machine Learning Engineer Associate Training (TGS-2024049340)  |  Domain 04: ML Solution Monitoring, Maintenance and Security (24%)

## Objective

This lab develops your ability to secure, govern and cost-optimise ML in production and map every lab to the exam domains (Domain 4: secure, govern and optimise ML solutions).

## Scenario

Finish production-ready and exam-ready: apply IAM, KMS, VPC and data-protection controls, add governance with the Model Registry, Model Cards and lineage, build a cost-optimisation checklist, then map every lab to the four MLA-C01 domains and complete a timed practice set.

## What you will build

Security, governance and cost-optimisation checklists, a lab-to-domain map and a timed practice-exam score with a weak-topic plan.

## Architecture / workflow

Apply IAM/KMS/VPC controls  →  Protect PII/PHI data  →  Add governance & lineage  →  Build the cost checklist  →  Map labs to domains & practise

## Services used

IAM, AWS KMS, Amazon VPC, Amazon Macie, SageMaker Model Registry/Model Cards, AWS Budgets, Cost Explorer

## Prerequisites & cost safety

- An AWS account you are authorised to use (trainer-provided sandbox where available); MFA enabled.
- AWS Management Console plus AWS CloudShell or the AWS CLI for the command steps.
- A budget alert configured before you begin; use small datasets and short jobs.
- Delete paid resources (endpoints, training jobs, pipelines, temporary buckets) when a step says to.

## Step-by-step

1. Review IAM least privilege, resource policies and SageMaker execution roles for ML security.
2. Review KMS encryption, VPC endpoints, private subnets and network isolation for SageMaker.
3. Review data classification, masking, anonymisation, PII/PHI handling and data residency, and Amazon Macie for PII discovery.

   ```bash
   aws macie2 get-findings-filter --id <id> 2>/dev/null || echo 'review Macie in the console'
   ```

4. Review governance: Model Registry approval, Model Cards, ML lineage tracking and the Model Dashboard.
5. Create a security checklist covering identity, encryption, network isolation, secrets and audit.
6. Create a cost-optimisation checklist: instance choice, endpoint auto scaling, serverless inference, batch transform, spot training, storage class and stopping idle notebooks.

   ```bash
   aws ce get-cost-and-usage --time-period Start=2026-08-01,End=2026-08-31 --granularity MONTHLY --metrics UnblendedCost
   ```

7. Map each of the twelve labs to the four MLA-C01 exam domains.
8. Complete a timed 30-question practice set and mark weak topics by domain.
9. Review the scenario exam-decision patterns across all four domains.
10. Clean up any temporary resources and save the checklists, lab-to-domain map and weak-topic plan as final evidence.

## Evidence to capture

- Screenshots of each console screen and command output.
- The tables, checklists or design notes this lab asks you to produce.
- Any metrics, configuration values or ARNs you created.
- Save everything into your working folder: TGS-2024049340-AWS-MLA-Labs/.

## Troubleshooting

- **Access is over-permissive** — Tighten IAM to least privilege and use scoped execution roles.
- **PII found in a training set** — Detect with Macie/Comprehend; mask, anonymise and encrypt with KMS.
- **Surprise ML bill** — Set Budgets and alarms; delete idle endpoints and notebooks.

## Acceptance criteria

You can secure, govern and cost-optimise an AWS ML workload, map each of the twelve labs to an exam domain, and produce a scored practice set with a weak-topic revision plan.

## Clean up

Delete any paid resources you created in this lab (endpoints, training/tuning jobs, pipelines, temporary buckets) and confirm in Billing that nothing is still running.
