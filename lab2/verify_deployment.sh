#!/bin/bash

echo "=========================================="
echo "BEDROCK AGENT DEPLOYMENT VERIFICATION"
echo "=========================================="

# Check Lambda function
echo -e "\n1. Checking Lambda Function..."
aws lambda get-function \
  --function-name bedrock-weather-agent-weather-tool \
  --query 'Configuration.[FunctionName,State,LastUpdateStatus]' \
  --output table

# Check IAM roles
echo -e "\n2. Checking IAM Roles..."
aws iam get-role \
  --role-name bedrock-weather-agent-agent-role \
  --query 'Role.[RoleName,Arn]' \
  --output table

# List Bedrock agents
echo -e "\n3. Checking Bedrock Agents..."
aws bedrock-agent list-agents \
  --query 'agentSummaries[?agentName==`WeatherAssistant`].[agentId,agentName,agentStatus]' \
  --output table

echo -e "\n✅ Verification complete!"
