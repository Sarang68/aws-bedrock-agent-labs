# AWS Bedrock Agentic AI Labs

Complete hands-on lab series for building production-ready AI agents on AWS using Bedrock, Lambda, Step Functions, and more.

## 🎯 Purpose

This repository contains practical labs designed for interview preparation and hands-on learning of AWS agentic AI development. Each lab builds progressively from basic concepts to production-ready systems.

## 📚 Lab Series

### **Lab 1: Bedrock Fundamentals**
- Basic model invocation
- Prompt engineering basics
- Understanding inference profiles

**Status**: ✅ Complete  
**Duration**: 30 minutes

### **Lab 2: Building Your First Agent**
- Create Bedrock Agent
- Lambda function as agent tool
- Infrastructure as Code with Terraform
- OpenAPI schema integration

**Status**: ✅ Complete  
**Duration**: 1-2 hours

### **Lab 3: Knowledge Bases & RAG** (Coming Soon)
- Create Bedrock Knowledge Base
- Vector search implementation
- RAG patterns

**Status**: 🚧 In Progress  
**Duration**: 2 hours

### **Lab 4: Advanced Prompting** (Coming Soon)
- ReAct (Reasoning + Acting)
- Chain-of-Thought
- Tree-of-Thought

### **Lab 5: Serverless Orchestration** (Coming Soon)
- Step Functions workflows
- Multi-step agent orchestration
- Error handling patterns

### **Lab 6: Guardrails & Safety** (Coming Soon)
- Bedrock Guardrails
- Content filtering
- Evaluation frameworks

### **Lab 7: Event-Driven Architecture** (Coming Soon)
- EventBridge integration
- Async workflows
- Monitoring & alerting

### **Lab 8: Production System** (Coming Soon)
- Complete production architecture
- End-to-end integration
- Best practices

## 🚀 Quick Start

### Prerequisites

- AWS Account with appropriate permissions
- AWS CLI installed and configured
- Python 3.9+
- Terraform 1.0+
- Git

### Setup
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/aws-agent-labs.git
cd aws-agent-labs

# Run setup script
./setup.sh

# Or manual setup:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure AWS credentials
aws configure
```

### Enable Bedrock Model Access

**IMPORTANT**: Before running any labs, you must enable model access:

1. Go to [AWS Bedrock Console](https://console.aws.amazon.com/bedrock)
2. Click "Model access" in left sidebar
3. Click "Manage model access"
4. Enable: Claude 3.5 Sonnet, Claude 3 Haiku
5. Save changes and wait ~1 minute

### Run Labs
```bash
# Lab 1: Basic invocation
cd lab1
python3 lab1_basic_invoke.py

# Lab 2: Deploy agent
cd lab2/terraform
terraform init
terraform apply
# Then follow lab2/README.md for agent creation
```

## 📖 Documentation

- [Architecture Overview](docs/architecture.md)
- [Setup Guide](docs/setup.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Best Practices](docs/best-practices.md)
- [Cost Optimization](docs/cost-optimization.md)

## 🏗️ Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                        User Request                         │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    Bedrock Agent                            │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Foundation Model (Claude 3.5 Sonnet)              │    │
│  └────────────────────────────────────────────────────┘    │
└────┬─────────────────────────┬──────────────────────────────┘
     │                         │
     │ Tool Calls              │ Knowledge Retrieval
     ▼                         ▼
┌─────────────────┐      ┌──────────────────┐
│ Lambda Functions│      │ Knowledge Base   │
│  - Weather      │      │  - OpenSearch    │
│  - Calculator   │      │  - S3 Documents  │
│  - Custom APIs  │      │  - Vector Search │
└─────────────────┘      └──────────────────┘
```

## 💰 Cost Considerations

**Estimated costs for completing all labs**: $5-10

- Bedrock API calls: ~$2-5
- Lambda invocations: <$1
- OpenSearch Serverless: ~$2-3
- S3 storage: <$0.50

**Cost optimization tips**:
- Always run `terraform destroy` after labs
- Use Haiku model for testing (cheaper)
- Delete unused S3 buckets
- Monitor CloudWatch for unexpected usage

## 🛠️ Tech Stack

- **AWS Bedrock**: Foundation models & agents
- **AWS Lambda**: Serverless compute for tools
- **AWS Step Functions**: Workflow orchestration
- **AWS EventBridge**: Event-driven triggers
- **Amazon S3**: Document storage
- **OpenSearch Serverless**: Vector database
- **Terraform**: Infrastructure as Code
- **Python**: Primary programming language

## 🧪 Testing
```bash
# Run all tests
pytest

# Run specific lab tests
pytest lab2/tests/

# Run with coverage
pytest --cov=shared
```

## 📝 Project Structure
```
aws-agent-labs/
├── lab1/                   # Bedrock basics
│   ├── README.md
│   └── *.py
├── lab2/                   # First agent
│   ├── lambda/            # Lambda functions
│   ├── terraform/         # IaC
│   ├── tests/             # Test scripts
│   └── README.md
├── shared/                # Shared utilities
│   ├── utils/
│   │   └── bedrock_client.py
│   └── config/
│       └── settings.py
├── scripts/               # Helper scripts
│   ├── deploy.sh
│   └── cleanup.sh
├── docs/                  # Documentation
└── requirements.txt
```

## 🤝 Contributing

This is a learning project, but suggestions welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Contact

**Author**: Sarang  
**Purpose**: Senior Software Engineer Interview Preparation  
**Focus**: AWS Agentic AI Development

## 📄 License

MIT License - Feel free to use for learning and interview prep!

## 🙏 Acknowledgments

- AWS Bedrock documentation
- Anthropic Claude documentation
- AWS Samples repository
- Community contributions

## ⚠️ Important Notes

- **Never commit AWS credentials** to Git
- Always use `.gitignore` for sensitive files
- Run `terraform destroy` after each lab to avoid costs
- Enable Bedrock model access before starting
- Review IAM permissions for security

## 🎓 Learning Resources

- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Anthropic Prompt Engineering](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [AWS Lambda Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

## 🚦 Status

- Lab 1: ✅ Complete
- Lab 2: ✅ Complete
- Lab 3-8: 🚧 In Development

Last Updated: January 2025
