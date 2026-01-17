# Troubleshooting Guide

## Common Issues

### 1. Bedrock ValidationException

**Error**: 
```
Invocation of model ID ... with on-demand throughput isn't supported
```

**Solution**:
Use inference profile instead:
```python
modelId='us.anthropic.claude-3-5-sonnet-20241022-v2:0'
```

### 2. Terraform State Lock

**Error**:
```
Error: Error locking state: Error acquiring the state lock
```

**Solution**:
```bash
# Remove lock file
rm .terraform.tfstate.lock.info

# Or force unlock
terraform force-unlock LOCK_ID
```

### 3. Lambda Permission Denied

**Error**:
```
User: ... is not authorized to perform: lambda:InvokeFunction
```

**Solution**:
Add Lambda permission:
```bash
aws lambda add-permission \
    --function-name FUNCTION_NAME \
    --statement-id AllowBedrockInvoke \
    --action lambda:InvokeFunction \
    --principal bedrock.amazonaws.com
```

### 4. Agent Not Found

**Error**:
```
ResourceNotFoundException: Agent AGENT_ID not found
```

**Solution**:
1. Verify agent exists in console
2. Check region matches
3. Ensure agent is "Prepared"
4. Verify alias exists

### 5. Cost Overruns

**Prevention**:
```bash
# Set billing alerts
aws budgets create-budget \
    --account-id ACCOUNT_ID \
    --budget file://budget.json

# Always cleanup
terraform destroy
aws bedrock-agent delete-agent --agent-id ID
```

## Getting Help

1. Check CloudWatch Logs
2. Enable trace in agent invocation
3. Test Lambda functions directly
4. Verify IAM permissions
