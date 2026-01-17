# Lab 2: Building Your First Bedrock Agent

Create a complete Bedrock Agent with Lambda function tools using Terraform.

## Objectives

- Deploy Lambda function as agent tool
- Create Bedrock Agent with action groups
- Use Terraform for infrastructure
- Test agent with multiple queries

## Architecture
```
User → Bedrock Agent → Lambda (Weather Tool) → Response
```

## Files Structure
```
lab2/
├── lambda/
│   ├── lambda_weather_tool.py      # Lambda function
│   ├── weather_api_schema.json     # OpenAPI schema
│   └── lambda_weather_tool.zip     # Deployment package
├── terraform/
│   ├── main.tf                     # Terraform config
│   ├── lambda.tf                   # Lambda resources
│   ├── bedrock_agent_role.tf       # IAM roles
│   └── outputs.tf                  # Output values
└── tests/
    ├── test_agent.py               # Agent tests
    ├── test_lambda_direct.py       # Lambda tests
    └── test_agent_with_trace.py    # Trace debugging
```

## Step-by-Step Deployment

### 1. Package Lambda
```bash
cd lab2/lambda
zip lambda_weather_tool.zip lambda_weather_tool.py
```

### 2. Deploy Infrastructure
```bash
cd ../terraform
terraform init
terraform plan
terraform apply
```

### 3. Create Agent (AWS Console)

See [detailed instructions](../../docs/create-bedrock-agent.md)

### 4. Test Agent
```bash
cd ../tests
# Update AGENT_ID and AGENT_ALIAS_ID in test_agent.py
python3 test_agent.py
```

## Expected Output
```
🧪 Test 1: Simple Weather Query
Session ID: abc-123-def
Prompt: What's the weather like in Seattle?
--------------------------------------------------------------------------------
Let me check the weather in Seattle for you. According to the current data, 
Seattle is experiencing Sunny conditions with a temperature of 72°F. 
The humidity is at 45% and wind speed is 8 mph.
```

## Troubleshooting

### Agent not found
```bash
# Verify agent exists
aws bedrock-agent list-agents
```

### Lambda invocation failed
```bash
# Check Lambda logs
aws logs tail /aws/lambda/bedrock-weather-agent-weather-tool --follow
```

## Cost

- Lambda: ~$0.20 per 1M requests
- Bedrock API: ~$3 per 1M input tokens
- **Estimated lab cost**: <$1

## Cleanup
```bash
cd terraform
terraform destroy
# Delete agent in AWS Console
```

## Next Steps

Proceed to [Lab 3](../lab3/README.md) for Knowledge Bases.
