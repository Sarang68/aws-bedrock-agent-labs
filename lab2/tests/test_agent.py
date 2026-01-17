

import boto3
import json
import uuid
import sys

# IMPORTANT: Replace these with your actual values
AGENT_ID = "ABCDEFGHIJ"  # Get from AWS Console
AGENT_ALIAS_ID = "TSTALIASID"  # Get from AWS Console

bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name='us-east-1')

def invoke_agent(prompt, session_id=None):
    """
    Invoke the Bedrock Agent
    """
    if not session_id:
        session_id = str(uuid.uuid4())
    
    print(f"Session ID: {session_id}")
    print(f"Prompt: {prompt}")
    print("-" * 80)
    
    try:
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
                text = chunk['bytes'].decode('utf-8')
                completion += text
                print(text, end='', flush=True)
        
        print("\n" + "-" * 80)
        return completion
        
    except Exception as e:
        print(f"Error invoking agent: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        
        if 'ResourceNotFoundException' in str(e):
            print("\n❌ Agent or Alias not found!")
            print("Please update AGENT_ID and AGENT_ALIAS_ID in this script")
        elif 'AccessDeniedException' in str(e):
            print("\n❌ Access denied!")
            print("Check IAM permissions for Bedrock Agent")
        
        raise

def main():
    """Run test scenarios"""
    
    # Check if IDs are set
    if AGENT_ID == "ABCDEFGHIJ" or AGENT_ALIAS_ID == "TSTALIASID":
        print("❌ ERROR: Please update AGENT_ID and AGENT_ALIAS_ID in this script")
        print(f"Current AGENT_ID: {AGENT_ID}")
        print(f"Current AGENT_ALIAS_ID: {AGENT_ALIAS_ID}")
        sys.exit(1)
    
    print("=" * 80)
    print("BEDROCK AGENT TEST SUITE")
    print("=" * 80)
    
    # Test 1: Simple weather query
    print("\n🧪 Test 1: Simple Weather Query")
    invoke_agent("What's the weather like in Seattle?")
    
    # Test 2: Multiple cities
    print("\n🧪 Test 2: Multiple Cities")
    invoke_agent("Can you tell me the weather in New York and Los Angeles?")
    
    # Test 3: Conversational follow-up
    print("\n🧪 Test 3: Conversational Follow-up")
    session = str(uuid.uuid4())
    invoke_agent("What's the weather in Boston?", session)
    invoke_agent("How about Chicago?", session)
    
    print("\n✅ All tests completed!")

if __name__ == "__main__":
    main()
