# Lab 1: Bedrock Fundamentals

Learn the basics of invoking AWS Bedrock models and prompt engineering.

## Objectives

- Understand Bedrock inference profiles
- Basic model invocation
- Create reusable prompt templates
- Handle API errors

## Prerequisites

- AWS CLI configured
- Bedrock model access enabled
- Python 3.9+
- boto3 installed

## Files

- `lab1_basic_invoke.py` - Basic model invocation
- `lab1_prompt_engineering.py` - Prompt templates

## Quick Start
```bash
cd lab1
python3 lab1_basic_invoke.py
```

## Expected Output
```
An AI agent is a software system that can perceive its environment, make decisions, and take actions autonomously to achieve specific goals.
```

## Troubleshooting

### ValidationException: Invocation of model ID not supported

**Solution**: Update to use inference profile:
```python
modelId='us.anthropic.claude-3-5-sonnet-20241022-v2:0'
```

### AccessDeniedException

**Solution**: Enable model access in Bedrock console.

## Next Steps

Proceed to [Lab 2](../lab2/README.md) to build your first agent.
