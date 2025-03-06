import json
import boto3

bedrock_client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

model_id = "amazon.nova-lite-v1:0"

prompt1 = "Who was Albert Einstein, and what was his most famous theory?"
prompt2 = "Write a short bedtime story about a friendly dragon who helps lost travelers."
prompt3 = "Summarize this sentence in simple words: 'Photosynthesis is the process by which green plants convert sunlight into energy.'"
prompt4 = "List three easy exercises for beginners to stay fit."
prompt5 = "Why is reading books beneficial for mental health?"

request_body = {
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "text": prompt5
          }
        ]
      }
    ],
    "inferenceConfig": {
        "maxTokens": 1000,
        "temperature": 0.9,
        "topP": 1,
    }
}

response = bedrock_client.invoke_model(modelId=model_id, body=json.dumps(request_body))

result = json.loads(response["body"].read())
generated_text = result["output"]["message"]["content"][0]["text"]

print(generated_text)