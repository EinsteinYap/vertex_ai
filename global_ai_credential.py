# run these lines directly , or if not install, please pip install it. 
from google.auth.transport.requests import Request
from google.oauth2 import service_account

# add your own key from google cloud's IAM & Admin , select Service accounts and create the key.
api_key_path = "../vertex_ai_test_key.json"

credentials = service_account.Credentials.from_service_account_file(
    api_key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

PROJECT_ID = "dependable-star-469404-k3"
REGION = "us-central1"

import vertexai

vertexai.init(project=PROJECT_ID, location=REGION, credentials=credentials)

# ✅ Print success message
print("✅ Successfully connected to Vertex AI!")
print(f"Project ID: {PROJECT_ID}")
print(f"Region: {REGION}")
