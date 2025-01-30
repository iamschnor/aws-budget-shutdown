# AWS Budget Shutdown Automation 🚀

This project helps automate AWS cost control by setting up:
- AWS Budgets to track spending.
- AWS SNS for budget alerts.
- AWS Lambda to stop paid services (EC2) when budget limits are reached.

## 🔧 Setup Guide
1. **Create an AWS Budget** and set alerts.
2. **Create an SNS Topic** and link it to AWS Budgets.
3. **Deploy an AWS Lambda Function** to stop EC2 instances.
4. **Link Lambda to SNS** for automatic execution.

## 🛠️ Prerequisites
- AWS Account
- IAM permissions for SNS, Lambda, and EC2

## 🎯 How It Works
1. AWS Budgets sends an alert to SNS when the limit is reached.
2. SNS triggers the Lambda function.
3. Lambda stops all running EC2 instances.

✅ **Check out the full setup guide in `setup_guide.md`.**
