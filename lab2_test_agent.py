# lab2_test_agent.py
import boto3
import uuid

bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name='us-east-1')

AGENT_ID = "YOUR_AGENT_ID"  # Replace with your agent ID
AGENT_ALIAS_ID = "YOUR_ALIAS_ID"  # Replace with alias ID

def invoke_agent(prompt, session_id=None):
    if not session_id:
        session_id = str(uuid.uuid4())
    
    response = bedrock_agent_runtime.invoke_agent(
        agentId=AGENT_ID,
        agentAliasId=AGENT_ALIAS_ID,
        sessionId=session_id,
        inputText=prompt
    )
    
    # Stream the response
    completion = ""
    for event in response.get('completion', []):
        chunk = event.get('chunk', {})
        if 'bytes' in chunk:
            completion += chunk['bytes'].decode('utf-8')
    
    return completion

# Test
print(invoke_agent("What's the weather like in Seattle?"))
