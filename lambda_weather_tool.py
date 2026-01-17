# lambda_weather_tool.py
import json

def lambda_handler(event, context):
    """
    Weather tool for Bedrock Agent
    """
    action = event.get('actionGroup', '')
    api_path = event.get('apiPath', '')
    parameters = event.get('parameters', [])
    
    # Extract parameters
    params = {p['name']: p['value'] for p in parameters}
    
    if api_path == '/weather':
        city = params.get('city', 'Unknown')
        # Simulated weather data
        weather_data = {
            'city': city,
            'temperature': 72,
            'condition': 'Sunny',
            'humidity': 45
        }
        
        response_body = {
            'application/json': {
                'body': json.dumps(weather_data)
            }
        }
        
        return {
            'messageVersion': '1.0',
            'response': {
                'actionGroup': action,
                'apiPath': api_path,
                'httpMethod': 'GET',
                'httpStatusCode': 200,
                'responseBody': response_body
            }
        }
