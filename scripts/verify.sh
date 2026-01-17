#!/bin/bash

echo "Verifying deployment..."

# Check Lambda
echo "Lambda functions:"
aws lambda list-functions \
    --query 'Functions[?contains(FunctionName, `bedrock`)].FunctionName' \
    --output table

# Check Bedrock agents
echo -e "\nBedrock agents:"
aws bedrock-agent list-agents \
    --query 'agentSummaries[*].[agentName,agentId,agentStatus]' \
    --output table

echo "✅ Verification complete!"
