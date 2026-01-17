import boto3
import json
import uuid

AGENT_ID = "YOUR_AGENT_ID_HERE"
AGENT_ALIAS_ID = "YOUR_ALIAS_ID_HERE"

bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name='us-east-1')

def invoke_with_trace(prompt):
    """Invoke agent with trace enabled to see tool calls"""
    
    session_id = str(uuid.uuid4())
    
    response = bedrock_agent_runtime.invoke_agent(
        agentId=AGENT_ID,
        agentAliasId=AGENT_ALIAS_ID,
        sessionId=session_id,
        inputText=prompt,
        enableTrace=True  # This shows tool invocations
    )
    
    print(f"Prompt: {prompt}\n")
    
    for event in response.get('completion', []):
        # Check for trace events
        if 'trace' in event:
            trace = event['trace']['trace']
            print("TRACE EVENT:")
            print(json.dumps(trace, indent=2, default=str))
            print("-" * 80)
        
        # Check for chunks
        if 'chunk' in event and 'bytes' in event['chunk']:
            text = event['chunk']['bytes'].decode('utf-8')
            print(text, end='', flush=True)
    
    print("\n")

if __name__ == "__main__":
    invoke_with_trace("What's the weather in Miami?")
