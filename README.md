# Build generative AI applications on Amazon Bedrock with the AWS SDK for Python (Boto3) 

## Solution Overview
This solution demonstrates how to use an AWS SDK for Python script to invoke Anthropic’s Claude 3 Sonnet model on Amazon Bedrock. The model generates responses based on given prompts.

## Architecture Diagram
![image](https://github.com/user-attachments/assets/854009cd-4ba0-409f-8127-22bf5e1c0bc1)


---

## Steps to Set Up

### 1. Create an IAM User
Amazon Bedrock requires proper authentication and authorization. To create an IAM user:
1. Sign in to the AWS Management Console.
2. Navigate to IAM (Identity & Access Management).
3. Click **Users** in the left sidebar.
4. Click **Create User** and provide a username.
5. Click **Next: Permissions** and attach the **AmazonBedrockFullAccess** policy or create a custom policy with necessary permissions.
6. Click **Next: Review**, then **Create User**.

### 2. Create IAM User's Access Key
If you didn't download the access key earlier, generate a new one:
1. Open **IAM > Users** in the AWS Console.
2. Select the created user.
3. Go to the **Security Credentials** tab.
4. Click **Create Access Key** and save the Access Key ID and Secret Access Key.

### 3. Install and Configure AWS CLI
**Installation:**
- Windows: [Download AWS CLI](https://aws.amazon.com/cli/)
- Mac/Linux: Install via package manager

**Configuration:**
```sh
aws configure
```
Enter:
- AWS Access Key ID
- AWS Secret Access Key
- Default region name (e.g., `us-east-1`)
- Default output format (`json`, `table`, or `text`)

### 4. Set Up Python Environment
Ensure Python is installed:
```sh
python --version
```
If not installed, download from [Python.org](https://www.python.org/).

### 5. Create Project Directory

### 6. Install Boto3 SDK
```sh
pip install boto3
```

### 7. Create and Configure `main.py`
Inside your project directory, create a `main.py` file.

### 8. Import Required Libraries
```python
import json
import boto3
```

### 9. Initialize Amazon Bedrock Client
```python
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)
```

### 10. Define the Model ID
```python
model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
```

### 11. Prepare the Input Prompt & Model Parameters
```python
payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 500,
    "temperature": 0.9,
    "top_k": 250,
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
```

### 12. Invoke the AI Model
```python
response = bedrock_client.invoke_model(
    modelId=model_id,
    body=json.dumps(payload)
)
```

### 13. Process & Print the Model's Response
```python
result = json.loads(response["body"].read())
print(result['content'][0]['text'])
```

### Example Execution & Output
Run:
```sh
python main.py
```
Expected Output:
```sh
Hello! As an AI language model, I don't have feelings, but I'm here to assist you. How can I help today?
```

---

## Model Comparison: Claude 3 Sonnet vs. Amazon Nova Lite vs. Amazon Titan Text Lite

| Prompt | Claude 3 Sonnet | Amazon Nova Lite | Amazon Titan Text Lite | Best Model |
|--------|----------------|------------------|------------------------|------------|
| Albert Einstein | Most detailed, explains relativity well | Structured and accurate but less depth | Basic overview, lacks accuracy | Claude Sonnet 3 |
| Bedtime Story | Creative and engaging | Best structured, emotionally engaging | Declined request | Amazon Nova Lite |
| Summarization | Simplest and most effective | Similar to Claude, slightly less concise | Overcomplicates response | Claude Sonnet 3 |
| Beginner Exercises | Well-explained but general | Best structured, detailed breakdowns | Exercises may be too advanced | Amazon Nova Lite |
| Reading Benefits | Most detailed, covers scientific reasoning | Well-structured, slightly fewer benefits | Basic, some questionable claims | Claude Sonnet 3 |

---

## Sample Prompts

```sh
prompt1 = "Who was Albert Einstein, and what was his most famous theory?"
prompt2 = "Write a short bedtime story about a friendly dragon who helps lost travelers."
prompt3 = "Summarize this sentence in simple words: 'Photosynthesis is the process by which green plants convert sunlight into energy.'"
prompt4 = "List three easy exercises for beginners to stay fit."
prompt5 = "Why is reading books beneficial for mental health?"
```

---

## Conclusion
This guide provides a step-by-step approach to integrating Claude 3 Sonnet on Amazon Bedrock using Python and Boto3. It also compares performance with other Amazon Bedrock models.

For any issues, please refer to the [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/).

