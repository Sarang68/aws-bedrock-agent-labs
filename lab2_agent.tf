# lab2_agent.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# Lambda Function
resource "aws_lambda_function" "weather_tool" {
  filename         = "lambda_weather_tool.zip"
  function_name    = "bedrock-agent-weather-tool"
  role            = aws_iam_role.lambda_role.arn
  handler         = "lambda_weather_tool.lambda_handler"
  runtime         = "python3.11"
  source_code_hash = filebase64sha256("lambda_weather_tool.zip")
}

# IAM Role for Lambda
resource "aws_iam_role" "lambda_role" {
  name = "bedrock-agent-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# Lambda permissions
resource "aws_lambda_permission" "allow_bedrock" {
  statement_id  = "AllowBedrockInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.weather_tool.function_name
  principal     = "bedrock.amazonaws.com"
}

# Bedrock Agent Role
resource "aws_iam_role" "bedrock_agent_role" {
  name = "bedrock-agent-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "bedrock.amazonaws.com"
      }
    }]
  })
}

# Bedrock Agent Policy
resource "aws_iam_role_policy" "bedrock_agent_policy" {
  name = "bedrock-agent-policy"
  role = aws_iam_role.bedrock_agent_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "bedrock:InvokeModel"
        ]
        Resource = "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-5-sonnet-20241022-v2:0"
      },
      {
        Effect = "Allow"
        Action = [
          "lambda:InvokeFunction"
        ]
        Resource = aws_lambda_function.weather_tool.arn
      }
    ]
  })
}

output "lambda_arn" {
  value = aws_lambda_function.weather_tool.arn
}

output "agent_role_arn" {
  value = aws_iam_role.bedrock_agent_role.arn
}
