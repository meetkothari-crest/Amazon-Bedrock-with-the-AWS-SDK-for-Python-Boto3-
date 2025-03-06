import json
import boto3

bedrock_client = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1"
)

model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

prompt1 = "Who was Albert Einstein, and what was his most famous theory?"
prompt2 = "Write a short bedtime story about a friendly dragon who helps lost travelers."
prompt3 = "Summarize this sentence in simple words: 'Photosynthesis is the process by which green plants convert sunlight into energy.'"
prompt4 = "List three easy exercises for beginners to stay fit."
prompt5 = "Why is reading books beneficial for mental health?"

payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 1000,
    "temperature": 0.9,
    "top_p": 1,
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

response = bedrock_client.invoke_model(
    modelId=model_id,
    body=json.dumps(payload)
)

result = json.loads(response["body"].read())
print(result['content'][0]['text'])