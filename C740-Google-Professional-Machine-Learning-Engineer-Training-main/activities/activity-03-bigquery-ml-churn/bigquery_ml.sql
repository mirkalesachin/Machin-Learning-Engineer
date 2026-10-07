CREATE OR REPLACE MODEL `<PROJECT_ID>.<DATASET>.churn_model`
OPTIONS(model_type='LOGISTIC_REG', input_label_cols=['churned']) AS
SELECT tenure_months, monthly_spend, support_tickets, churned
FROM `<PROJECT_ID>.<DATASET>.customers`;

SELECT * FROM ML.EVALUATE(MODEL `<PROJECT_ID>.<DATASET>.churn_model`);
SELECT customer_id, predicted_churned, predicted_churned_probs
FROM ML.PREDICT(MODEL `<PROJECT_ID>.<DATASET>.churn_model`, TABLE `<PROJECT_ID>.<DATASET>.customers`);
