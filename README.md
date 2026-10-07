# Machin-Learning-Engineer
AWS Certified Machine Learning Engineer Associate Training
Course: AWS Certified Machine Learning Engineer Associate Training
Course Code: TGS-2024049340
Status: WSQ-funded course
Duration: 3 days · 24 hours (22 learning hours + 2 assessment hours)
Funding: Up to 70% course-fee funding, subject to current eligibility and terms
View course details and register

Hands-on AWS Certified Machine Learning Engineer Associate labs for learners preparing for the AWS Certified Machine Learning Engineer - Associate (MLA-C01) exam. The three-day course covers data preparation, ingestion, feature engineering, data quality, model development, training, debugging, tuning, evaluation, deployment, orchestration, monitoring, security, cost optimization, and exam-style review across twelve self-contained labs — exactly four labs per day.

Courseware
Item	Description
Slide Deck (v14)	courseware/AWS Certified Machine Learning Engineer Associate Training-v14.pptx (+ PDF) — 156-slide concept-led WSQ deck aligned to the twelve labs and the four MLA-C01 exam domains, with domain deep-dives and scenario exam-decision patterns.
Lesson Plan	courseware/LP-AWS Certified Machine Learning Engineer Associate Training.docx (+ PDF) — 3-day schedule (24 course hours) with four unique labs per day and per-activity slide references matching the deck.
Learner Guide	courseware/LG-AWS Certified Machine Learning Engineer Associate Training.docx (+ PDF), mirrored by LG-AWS Certified Machine Learning Engineer Associate Training.md.
Lab Guide	Twelve labs grouped by training day and MLA-C01 exam domain.
Tools Reference	Recommended AWS tools, cost-safety notes, and learner setup checklist.
Superseded versions are retained in courseware/archive/; the repository carries one live version (v14) only.

Duration
The official registration page lists 3 days / 24 hours. The LMS-TMS edit-data stores trainingHours=22. These reconcile as 22 learning hours + Written Assessment 1h + Case Study 1h = 24 scheduled course hours across 3 days (each day 9:30 am – 6:30 pm, 8 scheduled hours excluding the 1-hour lunch).

How to Use
Create or use an AWS account provided by your trainer.
Create a working folder named TGS-2024049340-AWS-MLA-Labs.
Complete the labs in sequence because later labs reuse S3, SageMaker, IAM, model registry, endpoints, monitoring, and pipeline concepts.
Record screenshots, notebooks, SQL snippets, feature notes, model metrics, and configuration notes for each lab.
Delete paid resources when the lab asks you to clean up.
Lab Catalogue
Day 1 — Domain 1: Data Preparation for Machine Learning (28%)
Lab	Title	Focus
Lab 1	Account Safety and IAM Baseline	Identity, least-privilege IAM, SageMaker execution role, MFA, budgets, KMS
Lab 2	S3 ML Data Lake and Data Formats	Encrypted S3 lake, prefixes, Block Public Access, lifecycle, CSV/JSON/Parquet/ORC
Lab 3	Batch and Streaming Ingestion with Glue, Athena and Kinesis	Glue crawlers/catalog, Athena, Kinesis Data Streams/Firehose/MSK
Lab 4	Feature Engineering, Feature Store, Labelling and Data Quality	Data Wrangler, Feature Store, Ground Truth, Glue Data Quality, Clarify
Day 2 — Domain 2: ML Model Development (26%)
Lab	Title	Focus
Lab 5	Modelling Approach, Algorithms and Managed AI Services	Algorithm selection, built-ins, JumpStart, Bedrock, Rekognition, Comprehend
Lab 6	SageMaker Training Jobs and Debugger	Training config, input modes, regularization, Debugger, Profiler, Spot
Lab 7	Automatic Model Tuning, Experiments and Model Registry	AMT strategies, Experiments, Model Registry, approval workflow
Lab 8	Model Evaluation, Metrics, Bias and Explainability	Confusion matrix, F1, ROC/AUC, Clarify bias, SHAP, acceptance criteria
Day 3 — Domain 3: Deployment & Orchestration (22%) + Domain 4: Monitoring, Security & Maintenance (24%)
Lab	Title	Focus
Lab 9	Deployment Options, Endpoints, Batch Transform and Auto Scaling	Real-time/serverless/async endpoints, batch transform, auto scaling, rollback
Lab 10	MLOps Pipelines, CI/CD, Orchestration and IaC	SageMaker Pipelines, Step Functions, CodePipeline, EventBridge, CloudFormation/CDK
Lab 11	Model Monitoring, Drift and Observability	Model Monitor, data capture, drift types, CloudWatch alarms, CloudTrail
Lab 12	Security, Governance, Cost Optimisation and Exam Review	IAM, KMS, VPC, Macie, governance, cost levers, lab-to-domain map, timed review
Assessment
Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book (knowledge, traces to course slides).
Case Study (CS) — applied AWS ML scenario, 1 hour, open book (traces to the twelve labs).
Both instruments run on Day 3. Assessment papers are confidential and are not published to GitHub.

Public and Private Materials
This public repository contains the current learner-safe slide deck, Learner Guide, Lesson Plan, lab instructions, and supporting course assets. Assessment papers and answer keys, legacy reference decks, local QA renders, credentials, build tooling, and archived courseware remain private and are excluded from GitHub.

Provider
Tertiary Infotech Academy Pte Ltd · UEN 201200696W
Course registration and current funding details

Reference
AWS Certified Machine Learning Engineer - Associate exam guide: https://docs.aws.amazon.com/pdfs/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01.pdf
Course registration: https://www.tertiarycourses.com.sg/wsq-aws-certified-machine-learning-engineer-associate-training.html
AWS Documentation: https://docs.aws.amazon.com/
Amazon SageMaker AI documentation: https://docs.aws.amazon.com/sagemaker/
Free Tools Used
AWS Free Tier eligible services where possible
AWS Management Console
Amazon SageMaker AI
Amazon S3
AWS Glue
Amazon Athena
Amazon CloudWatch
AWS Step Functions
AWS Pricing Calculator
