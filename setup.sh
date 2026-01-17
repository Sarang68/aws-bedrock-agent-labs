#!/bin/bash

set -e

echo "=========================================="
echo "AWS BEDROCK AGENT LABS - SETUP"
echo "=========================================="

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python
echo -e "\n${YELLOW}Checking Python...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Python 3 is not installed. Please install Python 3.9+${NC}"
    exit 1
fi
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo -e "${GREEN}✓ Python ${PYTHON_VERSION} found${NC}"

# Check AWS CLI
echo -e "\n${YELLOW}Checking AWS CLI...${NC}"
if ! command -v aws &> /dev/null; then
    echo -e "${RED}AWS CLI is not installed${NC}"
    echo "Install: https://aws.amazon.com/cli/"
    exit 1
fi
AWS_VERSION=$(aws --version)
echo -e "${GREEN}✓ ${AWS_VERSION}${NC}"

# Check Terraform
echo -e "\n${YELLOW}Checking Terraform...${NC}"
if ! command -v terraform &> /dev/null; then
    echo -e "${YELLOW}⚠ Terraform not found (needed for Lab 2+)${NC}"
    echo "Install: https://www.terraform.io/downloads"
else
    TERRAFORM_VERSION=$(terraform --version | head -n1)
    echo -e "${GREEN}✓ ${TERRAFORM_VERSION}${NC}"
fi

# Create virtual environment
echo -e "\n${YELLOW}Creating virtual environment...${NC}"
if [ -d "venv" ]; then
    echo "Virtual environment already exists"
else
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
fi

# Activate virtual environment
echo -e "\n${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate

# Install requirements
echo -e "\n${YELLOW}Installing Python packages...${NC}"
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo -e "${GREEN}✓ Packages installed${NC}"

# Check AWS credentials
echo -e "\n${YELLOW}Checking AWS credentials...${NC}"
if aws sts get-caller-identity &> /dev/null; then
    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    REGION=$(aws configure get region)
    echo -e "${GREEN}✓ AWS credentials configured${NC}"
    echo "  Account: ${ACCOUNT_ID}"
    echo "  Region: ${REGION}"
else
    echo -e "${RED}✗ AWS credentials not configured${NC}"
    echo "Run: aws configure"
    exit 1
fi

# Check Bedrock access
echo -e "\n${YELLOW}Checking Bedrock access...${NC}"
if aws bedrock list-foundation-models --region us-east-1 &> /dev/null; then
    echo -e "${GREEN}✓ Bedrock API accessible${NC}"
else
    echo -e "${RED}✗ Cannot access Bedrock API${NC}"
    echo "Check IAM permissions"
fi

# Create shared utilities
echo -e "\n${YELLOW}Setting up shared utilities...${NC}"
mkdir -p shared/utils shared/config
touch shared/__init__.py
touch shared/utils/__init__.py
touch shared/config/__init__.py

cat > shared/utils/bedrock_client.py << 'PYTHON'
"""Reusable Bedrock client with correct model IDs"""
import boto3
import json
from botocore.exceptions import ClientError

class BedrockClient:
    MODELS = {
        'sonnet-3.5': 'us.anthropic.claude-3-5-sonnet-20241022-v2:0',
        'haiku-3.5': 'us.anthropic.claude-3-5-haiku-20241022-v1:0',
    }
    
    def __init__(self, region='us-east-1'):
        self.bedrock_runtime = boto3.client('bedrock-runtime', region_name=region)
    
    def invoke(self, prompt, model='sonnet-3.5', max_tokens=1024, temperature=1.0):
        model_id = self.MODELS.get(model)
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature
        })
        
        response = self.bedrock_runtime.invoke_model(
            modelId=model_id,
            body=body
        )
        
        response_body = json.loads(response['body'].read())
        return response_body['content'][0]['text']
PYTHON

echo -e "${GREEN}✓ Shared utilities created${NC}"

# Summary
echo -e "\n=========================================="
echo -e "${GREEN}SETUP COMPLETE!${NC}"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Enable Bedrock model access:"
echo "   https://console.aws.amazon.com/bedrock"
echo ""
echo "2. Start with Lab 1:"
echo "   cd lab1"
echo "   python3 lab1_basic_invoke.py"
echo ""
echo "3. Read the documentation:"
echo "   cat README.md"
echo ""
echo -e "${YELLOW}Remember to activate venv:${NC}"
echo "   source venv/bin/activate"
echo ""

