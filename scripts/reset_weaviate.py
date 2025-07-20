import os
import weaviate
from dotenv import load_dotenv
from weaviate.auth import AuthApiKey

# Load environment
load_dotenv()
WEAVIATE_URL = os.getenv("WEAVIATE_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

# Connect to client
auth_config = AuthApiKey(api_key=WEAVIATE_API_KEY)
client = weaviate.Client(url=WEAVIATE_URL, auth_client_secret=auth_config)

CLASS_NAME = "RedditPost"

# Delete class
if client.schema.exists(CLASS_NAME):
    print(f"🧨 Deleting class '{CLASS_NAME}' and all its objects...")
    client.schema.delete_class(CLASS_NAME)
    print("✅ Class deleted.")
else:
    print(f"ℹ️ Class '{CLASS_NAME}' does not exist.")
