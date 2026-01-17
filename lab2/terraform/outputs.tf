output "lambda_function_arn" {
  description = "ARN of the weather Lambda function"
  value       = aws_lambda_function.weather_tool.arn
}

output "lambda_function_name" {
  description = "Name of the weather Lambda function"
  value       = aws_lambda_function.weather_tool.function_name
}

output "bedrock_agent_role_arn" {
  description = "ARN of the Bedrock Agent IAM role"
  value       = aws_iam_role.bedrock_agent_role.arn
}

output "aws_region" {
  description = "AWS region"
  value       = data.aws_region.current.name
}

output "aws_account_id" {
  description = "AWS Account ID"
  value       = data.aws_caller_identity.current.account_id
}
