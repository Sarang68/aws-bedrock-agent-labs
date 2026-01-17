cd ~/aws-agent-labs/lab2/lambda

# Create the Lambda function file
cat > lambda_weather_tool.py << 'EOF'
import json
import random
from datetime import datetime

def lambda_handler(event, context):
    """
    Weather tool for Bedrock Agent
    Handles weather queries for cities
    """
    
    print(f"Received event: {json.dumps(event)}")
    
    # Extract request details
    action_group = event.get('actionGroup', '')
    api_path = event.get('apiPath', '')
    http_method = event.get('httpMethod', '')
    parameters = event.get('parameters', [])
    
    # Convert parameters list to dict
    params = {p['name']: p['value'] for p in parameters}
    
    print(f"Action Group: {action_group}")
    print(f"API Path: {api_path}")
    print(f"Parameters: {params}")
    
    # Handle weather request
    if api_path == '/weather':
        city = params.get('city', 'Unknown')
        
        # Simulated weather data (in production, call real weather API)
        weather_conditions = ['Sunny', 'Cloudy', 'Rainy', 'Partly Cloudy', 'Snowy']
        weather_data = {
            'city': city,
            'temperature': random.randint(50, 85),
            'condition': random.choice(weather_conditions),
            'humidity': random.randint(30, 80),
            'wind_speed': random.randint(0, 20),
            'timestamp': datetime.now().isoformat()
        }
        
        # Format response for Bedrock Agent
        response_body = {
            'application/json': {
                'body': json.dumps(weather_data)
            }
        }
        
        action_response = {
            'actionGroup': action_group,
            'apiPath': api_path,
            'httpMethod': http_method,
            'httpStatusCode': 200,
            'responseBody': response_body
        }
        
        print(f"Response: {json.dumps(action_response)}")
        
        return {
            'messageVersion': '1.0',
            'response': action_response
        }
    
    # Handle unknown paths
    else:
        error_response = {
            'actionGroup': action_group,
            'apiPath': api_path,
            'httpMethod': http_method,
            'httpStatusCode': 404,
            'responseBody': {
                'application/json': {
                    'body': json.dumps({'error': f'Unknown API path: {api_path}'})
                }
            }
        }
        
        return {
            'messageVersion': '1.0',
            'response': error_response
        }
EOF

echo "Lambda function created: lambda_weather_tool.py"
