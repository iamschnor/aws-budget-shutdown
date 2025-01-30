# AWS Budget Shutdown Setup Guide

## Step 1: Create an AWS Budget
1. Go to AWS Billing → Budgets.
2. Click **Create Budget** → Select **Cost Budget**.
3. Set a monthly budget (e.g., $50).
4. Add an **SNS notification** for 80% and 100% usage.
5. Click **Create Budget**.

## Step 2: Set Up an SNS Topic
1. Go to **AWS SNS Console** → Create Topic.
2. Name it `AWSBudgetAlert`.
3. Add an **email subscription**.
4. **Update SNS Policy** to allow AWS Budgets to send messages.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "budgets.amazonaws.com"
      },
      "Action": "SNS:Publish",
      "Resource": "arn:aws:sns:YOUR_REGION:YOUR_ACCOUNT_ID:AWSBudgetAlert"
    }
  ]
}
