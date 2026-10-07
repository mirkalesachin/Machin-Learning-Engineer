# Lab 3 — Batch and Streaming Ingestion with Glue, Athena and Kinesis

> Course: AWS Certified Machine Learning Engineer Associate Training (TGS-2024049340)  |  Domain 01: Data Preparation for Machine Learning (28%)

## Objective

This lab develops your ability to design batch and streaming ingestion into the ML data lake and query it in place (Domain 1: ingest and catalog data).

## Scenario

Land data into the lake two ways: crawl and catalog batch data with AWS Glue and query it with Athena, and design a near-real-time streaming path with the Kinesis family (Data Streams, Firehose, MSK) into S3, then compare batch and streaming trade-offs.

## What you will build

A cataloged batch dataset queryable in Athena plus a streaming-ingestion design and a batch-vs-streaming comparison.

## Architecture / workflow

Crawl raw/ with Glue  →  Catalog the schema  →  Query in Athena  →  Design a Kinesis streaming path  →  Compare batch vs streaming

## Services used

AWS Glue, Glue Data Catalog, Amazon Athena, Kinesis Data Streams, Kinesis Data Firehose, Amazon MSK, Amazon S3

## Prerequisites & cost safety

- An AWS account you are authorised to use (trainer-provided sandbox where available); MFA enabled.
- AWS Management Console plus AWS CloudShell or the AWS CLI for the command steps.
- A budget alert configured before you begin; use small datasets and short jobs.
- Delete paid resources (endpoints, training jobs, pipelines, temporary buckets) when a step says to.

## Step-by-step

1. Open AWS Glue and review crawlers, jobs, the Data Catalog and Glue Data Quality.

   ```bash
   aws glue get-databases --query 'DatabaseList[].Name'
   ```

2. Run a Glue crawler over the raw/ prefix to infer schema and populate the Data Catalog.

   ```bash
   aws glue start-crawler --name tgs-mla-raw-crawler
   ```

3. Confirm the cataloged table and its columns before querying.

   ```bash
   aws glue get-tables --database-name tgs_mla_db --query 'TableList[].Name'
   ```

4. Query the cataloged raw data with Athena to confirm the schema and profile the data.

   ```bash
   aws athena start-query-execution --query-string 'SELECT * FROM raw_customers LIMIT 10' --result-configuration OutputLocation=s3://tgs-mla-<id>-datalake/athena/
   ```

5. Review a Glue ETL job pattern that converts raw CSV/JSON to columnar Parquet in prepared/.
6. Review the Kinesis family — Data Streams, Data Firehose and Amazon MSK — and where each fits.

   ```bash
   aws kinesis list-streams
   ```

7. Design a streaming path: producers → Kinesis Data Streams or Firehose → S3 raw/ → Glue crawler → Catalog.

   ```bash
   aws firehose list-delivery-streams
   ```

8. Note how Managed Service for Apache Flink can compute streaming features in flight.
9. Build a batch-vs-streaming comparison across latency, services, typical use and where data lands.
10. Save the cataloged schema, an Athena query result, the streaming design and the comparison as lab evidence.

## Evidence to capture

- Screenshots of each console screen and command output.
- The tables, checklists or design notes this lab asks you to produce.
- Any metrics, configuration values or ARNs you created.
- Save everything into your working folder: TGS-2024049340-AWS-MLA-Labs/.

## Troubleshooting

- **Crawler finds no tables** — Point the crawler at the correct S3 prefix and re-run it.
- **Athena query fails** — Set an S3 query-result location and confirm the Glue table exists.
- **Streaming data not landing in S3** — Check the Firehose delivery stream's IAM role and S3 destination.

## Acceptance criteria

You can catalog and query batch data with Glue and Athena, design a Kinesis streaming path into the lake, and justify batch vs streaming from latency and use-case requirements.

## Clean up

Delete any paid resources you created in this lab (endpoints, training/tuning jobs, pipelines, temporary buckets) and confirm in Billing that nothing is still running.
