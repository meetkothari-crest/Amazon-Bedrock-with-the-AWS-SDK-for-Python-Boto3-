# Build generative AI applications on Amazon Bedrock with the AWS SDK for Python (Boto3)

## Solution Overview
- The solution uses an AWS SDK for Python script. It invokes Anthropic’s Claude 3 Sonnet on Amazon Bedrock. The model generates output based on a given prompt.
- The diagram below shows the basic solution architecture.
  
![image](https://github.com/user-attachments/assets/d56efb8a-785a-4905-ba8b-5d4d02c12a4c)

## Steps
1. Create an IAM user
2. Create IAM User's Access key
3. Install [AWSCLI](https://awscli.amazonaws.com/AWSCLIV2.msi) and Configure it Using your Access key ID and Secret access key.

Run this command:
```bash
aws configure
```
> **Note:** Make sure you have Python Installed in your system.

4. Open IDE and Create a directory
5. Install latest boto3

```bash
pip install boto3
```
6. Create a main.py file in root directory (Not in venv directory)
7. Put below code in main.py

```bash
# Import the required libraries:
import json
import boto3

# Set up the Amazon Bedrock client
bedrock_client = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1"
)

# Define the model ID
model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

# Prepare the input prompt.
prompt = "Hello, How are you?"

payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 200,
    "temperature": 0.9,
    "top_k": 250,
    "top_p": 1,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                }
            ]
        }
    ]
}

# Invoke the Amazon Bedrock model
response = bedrock_client.invoke_model(
    modelId=model_id,
    body=json.dumps(payload)
)

# Process the response
result = json.loads(response["body"].read())
generated_text = "".join([output["text"] for output in result["content"]])
print(f"Response: {generated_text}")
```

8. Run main.py file

```bash
python main.py
```

## Response

```
Response: Hello! As an AI language model, I don't have feelings, but I'm operating properly and ready to assist 
you with any questions or tasks you may have. How can I help you today?
```

