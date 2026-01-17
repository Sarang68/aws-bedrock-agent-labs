import boto3
import json

lambda_client = boto3.client('lambda', region_name='us-east-1')

FUNCTION_NAME = "bedrock-weather-agent-weather-tool"

def test_lambda():
    """Test Lambda function directly"""
    
    # Simulate Bedrock Agent event
    test_event = {
        "actionGroup": "WeatherActions",
        "apiPath": "/weather",
        "httpMethod": "GET",
        "parameters": [
            {
                "name": "city",
                "type": "string",
                "value": "San Francisco"
            }
        ]
    }
    
    print("Testing Lambda function directly...")
    print(f"Event: {json.dumps(test_event, indent=2)}")
    
    response = lambda_client.invoke(
        FunctionName=FUNCTION_NAME,
        InvocationType='RequestResponse',
        Payload=json.dumps(test_event)
    )
    
    result = json.loads(response['Payload'].read())
    print(f"\nLambda Response:")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    test_lambda()
