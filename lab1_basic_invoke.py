# lab1_basic_invoke.py
import boto3
import json

bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')

def invoke_claude(prompt):
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })
    
    response = bedrock_runtime.invoke_model(
        # FIXED: Use inference profile instead of direct model ID
        modelId='us.anthropic.claude-3-5-sonnet-20241022-v2:0',
        body=body
    )
    
    response_body = json.loads(response['body'].read())
    return response_body['content'][0]['text']

# Test
result = invoke_claude("Explain what an AI agent is in one sentence.")
print(result)
# lab1_prompt_engineering.py

class PromptTemplates:
    @staticmethod
    def task_decomposition(task):
        return f"""You are a task planning agent. Break down this task into actionable steps:

Task: {task}

Provide a numbered list of steps with clear dependencies."""

    @staticmethod
    def reasoning_chain(question, context):
        return f"""Think through this step-by-step:

Context: {context}
Question: {question}

Use this format:
1. Understanding: [Restate the problem]
2. Analysis: [Break down key components]
3. Reasoning: [Apply logical steps]
4. Conclusion: [Final answer]"""

# Test both templates
print(invoke_claude(PromptTemplates.task_decomposition(
    "Build a customer support automation system"
)))
# lab1_prompt_engineering.py

class PromptTemplates:
    @staticmethod
    def task_decomposition(task):
        return f"""You are a task planning agent. Break down this task into actionable steps:

Task: {task}

Provide a numbered list of steps with clear dependencies."""

    @staticmethod
    def reasoning_chain(question, context):
        return f"""Think through this step-by-step:

Context: {context}
Question: {question}

Use this format:
1. Understanding: [Restate the problem]
2. Analysis: [Break down key components]
3. Reasoning: [Apply logical steps]
4. Conclusion: [Final answer]"""

# Test both templates
print(invoke_claude(PromptTemplates.task_decomposition(
    "Build a customer support automation system"
)))
