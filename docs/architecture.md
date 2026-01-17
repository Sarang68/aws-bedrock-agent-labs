# Architecture Overview

## System Components

### Layer 1: User Interface
- AWS Console (testing)
- API Gateway (production)
- Custom applications

### Layer 2: Orchestration
- Bedrock Agents
- Step Functions
- EventBridge

### Layer 3: Compute
- Lambda Functions
- EC2 (if needed)

### Layer 4: Data
- S3 (documents)
- OpenSearch (vectors)
- DynamoDB (state)

### Layer 5: Foundation Models
- Bedrock (Claude models)
- Inference profiles

## Data Flow

1. User request → Agent
2. Agent analyzes → Determines tools needed
3. Agent invokes → Lambda functions
4. Agent synthesizes → Final response
5. Response → User

## Security

- IAM roles and policies
- VPC endpoints (optional)
- Encryption at rest and in transit
- Guardrails for content filtering
