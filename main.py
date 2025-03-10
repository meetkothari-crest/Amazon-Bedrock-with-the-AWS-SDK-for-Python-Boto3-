import json
import boto3

# Initialize the Amazon Bedrock client for invoking AI models
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

# Define the model ID for the Claude 3 Sonnet model
model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

# Prepare the input prompt and model parameters
payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 500,  # Limits the response length
    "temperature": 0.9,  # Controls response randomness
    "top_k": 250,  # Restricts sampling to top-k tokens
    "top_p": 1,  # Controls diversity in token selection
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Hello, How are you?"
                }
            ]
        }
    ]
}

# Invoke the model and get the response
response = bedrock_client.invoke_model(
    modelId=model_id,
    body=json.dumps(payload)
)

# Process and print the model's response
result = json.loads(response["body"].read())
print(result['content'][0]['text'])