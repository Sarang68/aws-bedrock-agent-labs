# IAM Role for Lambda
resource "aws_iam_role" "lambda_role" {
  name = "${var.project_name}-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })

  tags = {
    Name    = "${var.project_name}-lambda-role"
    Project = var.project_name
  }
}

# Attach basic Lambda execution policy
resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Lambda Function
resource "aws_lambda_function" "weather_tool" {
  filename         = "../lambda/lambda_weather_tool.zip"
  function_name    = "${var.project_name}-weather-tool"
  role            = aws_iam_role.lambda_role.arn
  handler         = "lambda_weather_tool.lambda_handler"
  runtime         = "python3.11"
  timeout         = 30
  memory_size     = 256

  source_code_hash = filebase64sha256("../lambda/lambda_weather_tool.zip")

  environment {
    variables = {
      LOG_LEVEL = "INFO"
    }
  }

  tags = {
    Name    = "${var.project_name}-weather-tool"
    Project = var.project_name
  }
}

# Lambda permission for Bedrock to invoke
resource "aws_lambda_permission" "allow_bedrock" {
  statement_id  = "AllowBedrockInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.weather_tool.function_name
  principal     = "bedrock.amazonaws.com"
  source_account = data.aws_caller_identity.current.account_id
}
