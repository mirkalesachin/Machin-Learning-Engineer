# Lab 2 — S3 ML Data Lake and Data Formats

> Course: AWS Certified Machine Learning Engineer Associate Training (TGS-2024049340)  |  Domain 01: Data Preparation for Machine Learning (28%)

## Objective

This lab develops your ability to structure and secure an S3 data lake for ML and choose the right data format (Domain 1: data ingestion and storage).

## Scenario

Build the storage foundation for ML: create an encrypted S3 data lake with raw, prepared, features, training, models and monitoring prefixes, apply Block Public Access, lifecycle rules and storage classes, and compare the data formats used across ML workflows.

## What you will build

A secure, encrypted S3 ML data lake with six lifecycle prefixes and a data-format comparison table.

## Architecture / workflow

Create an encrypted S3 bucket  →  Enable Block Public Access  →  Add ML lifecycle prefixes  →  Set storage-class lifecycle rules  →  Compare data formats

## Services used

Amazon S3, AWS KMS, S3 Lifecycle, Amazon SageMaker AI

## Prerequisites & cost safety

- An AWS account you are authorised to use (trainer-provided sandbox where available); MFA enabled.
- AWS Management Console plus AWS CloudShell or the AWS CLI for the command steps.
- A budget alert configured before you begin; use small datasets and short jobs.
- Delete paid resources (endpoints, training jobs, pipelines, temporary buckets) when a step says to.

## Step-by-step

1. Create the ML data-lake bucket (only if your trainer permits), using a globally unique name.

   ```bash
   aws s3 mb s3://tgs-mla-<your-initials>-datalake --region ap-southeast-1
   ```

2. Enable default encryption on the bucket (SSE-S3 or SSE-KMS) so all objects are encrypted at rest.

   ```bash
   aws s3api put-bucket-encryption --bucket tgs-mla-<id>-datalake --server-side-encryption-configuration '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"aws:kms"}}]}'
   ```

3. Keep Block Public Access enabled on the bucket to prevent accidental exposure of training data.

   ```bash
   aws s3api put-public-access-block --bucket tgs-mla-<id>-datalake --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
   ```

4. Create the ML lifecycle prefixes so raw, prepared, feature, training, model and monitoring data are separated.

   ```bash
   for p in raw prepared features training models monitoring; do aws s3api put-object --bucket tgs-mla-<id>-datalake --key $p/; done
   ```

5. Upload small sample CSV and JSON files to raw/ (if permitted) and review object metadata and storage class.

   ```bash
   aws s3 cp sample.csv s3://tgs-mla-<id>-datalake/raw/
   ```

6. Review S3 storage classes and add a lifecycle rule that transitions old raw data to Standard-IA then Glacier.

   ```bash
   aws s3api put-bucket-lifecycle-configuration --bucket tgs-mla-<id>-datalake --lifecycle-configuration file://lifecycle.json
   ```

7. Build a comparison table of CSV, JSON, Parquet, ORC, Avro and RecordIO and note the best format for analytics, streaming and training.
8. Note why columnar formats (Parquet/ORC) suit analytics and large-scale training while RecordIO-protobuf suits several built-in algorithms.
9. Confirm the bucket enforces encryption and blocks public access, and record the KMS key that protects it.

   ```bash
   aws s3api get-bucket-encryption --bucket tgs-mla-<id>-datalake
   ```

10. Save your S3 structure, encryption, lifecycle and data-format notes as lab evidence.

## Evidence to capture

- Screenshots of each console screen and command output.
- The tables, checklists or design notes this lab asks you to produce.
- Any metrics, configuration values or ARNs you created.
- Save everything into your working folder: TGS-2024049340-AWS-MLA-Labs/.

## Troubleshooting

- **Bucket name already exists** — S3 names are globally unique — add your initials/date.
- **Access denied on PutObject** — Attach a least-privilege S3 policy to your role/execution role.
- **Objects not encrypted** — Set default bucket encryption; existing objects must be re-copied.

## Acceptance criteria

You can navigate the encrypted S3 data lake with its six prefixes, explain storage-class lifecycle, and justify a data-format choice for analytics, streaming and SageMaker training.

## Clean up

Delete any paid resources you created in this lab (endpoints, training/tuning jobs, pipelines, temporary buckets) and confirm in Billing that nothing is still running.
