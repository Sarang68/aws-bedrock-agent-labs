# Detailed Setup Guide

## Prerequisites Installation

### macOS
```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.11

# Install AWS CLI
brew install awscli

# Install Terraform
brew install terraform
```

### Windows

1. Install Python: https://www.python.org/downloads/
2. Install AWS CLI: https://aws.amazon.com/cli/
3. Install Terraform: https://www.terraform.io/downloads

### Linux
```bash
# Python
sudo apt-get update
sudo apt-get install python3.11 python3-pip

# AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Terraform
wget https://releases.hashicorp.com/terraform/1.6.0/terraform_1.6.0_linux_amd64.zip
unzip terraform_1.6.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/
```

## AWS Configuration

### 1. Create IAM User

1. Go to AWS Console → IAM
2. Create user with programmatic access
3. Attach policies:
   - `AmazonBedrockFullAccess`
   - `AWSLambda_FullAccess`
   - `IAMFullAccess` (for role creation)
   - `AmazonS3FullAccess`

### 2. Configure AWS CLI
```bash
aws configure
# AWS Access Key ID: [your key]
# AWS Secret Access Key: [your secret]
# Default region: us-east-1
# Default output: json
```

### 3. Enable Bedrock Models

**CRITICAL**: Must be done in AWS Console

1. https://console.aws.amazon.com/bedrock
2. Model access
3. Enable Claude models
4. Wait for approval
