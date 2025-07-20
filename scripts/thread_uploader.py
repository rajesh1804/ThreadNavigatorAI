import os
import json
import uuid
import weaviate
from dotenv import load_dotenv
from weaviate.auth import AuthApiKey
from sentence_transformers import SentenceTransformer

# ---------------------- 🔐 Load Environment ----------------------
print("🔐 Loading environment variables...")
load_dotenv()
WEAVIATE_URL = os.getenv("WEAVIATE_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

print(f"🌍 Connecting to Weaviate at: {WEAVIATE_URL}")
print(f"🔑 Using API Key (last 4 chars): {WEAVIATE_API_KEY[-4:]}")

auth_config = AuthApiKey(api_key=WEAVIATE_API_KEY)
client = weaviate.Client(url=WEAVIATE_URL, auth_client_secret=auth_config)

# ---------------------- 🧠 Load Embedding Model ----------------------
print("🧠 Loading SentenceTransformer model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------------------- 🧱 Check Schema ----------------------
CLASS_NAME = "RedditPost"
print(f"📚 Checking if '{CLASS_NAME}' schema exists...")

if not client.schema.exists(CLASS_NAME):
    print(f"🧱 Schema '{CLASS_NAME}' not found. Creating now...")
    client.schema.create_class({
        "class": CLASS_NAME,
        "description": "A post or comment in a Reddit-style thread",
        "vectorizer": "none",  # using custom embeddings
        "properties": [
            {"name": "thread_id", "dataType": ["text"]},
            {"name": "text", "dataType": ["text"]},
        ]
    })
    print("✅ Schema created.")
else:
    print("✅ Schema already exists.")

# ---------------------- 📥 Load All Threads ----------------------
THREAD_FILE = "data/threads.json"

print(f"\n📖 Reading thread data from: {THREAD_FILE}")
with open(THREAD_FILE, "r", encoding="utf-8") as f:
    threads = json.load(f)

# ---------------------- 📤 Upload Posts ----------------------
for thread in threads:
    thread_id = thread["thread_id"]
    posts = thread["posts"]

    print(f"\n🚀 Uploading {len(posts)} posts for thread: {thread_id}")

    for i, post in enumerate(posts):
        text = post["text"]
        print(f"\n🔄 Post {i + 1}/{len(posts)}")
        print(f"👤 Author: {post['author']}")
        print(f"📝 Text: {text}")

        embedding = model.encode(text).tolist()
        print(f"🔗 Embedding vector length: {len(embedding)}")

        object_uuid = str(uuid.uuid4())
        client.data_object.create(
            data_object={
                "thread_id": thread_id,
                "text": text
            },
            class_name=CLASS_NAME,
            vector=embedding,
            uuid=object_uuid
        )
        print(f"✅ Uploaded with UUID: {object_uuid}")

print("\n🎉 All threads uploaded successfully!")
