# test_weaviate_connection.py

import os
import weaviate
from weaviate.auth import AuthApiKey
from dotenv import load_dotenv

# Load env
load_dotenv()
WEAVIATE_URL = os.getenv("WEAVIATE_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

print("🔗 Testing connection to Weaviate...")
# try:
client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=AuthApiKey(WEAVIATE_API_KEY)
)
# Ping the cluster
if client.is_ready():
    print("✅ Successfully connected to Weaviate!")
else:
    print("⚠️ Connection failed: Cluster not ready.")
# except Exception as e:
#     print(f"❌ Error: {e}")
