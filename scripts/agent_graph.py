import os
from typing import Dict
from dotenv import load_dotenv
import weaviate
from weaviate.auth import AuthApiKey
from sentence_transformers import SentenceTransformer
from langgraph.graph import StateGraph, END 
from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_fixed
import time

# Load API keys
load_dotenv()
WEAVIATE_URL = os.getenv("WEAVIATE_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize clients
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

weaviate_client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=AuthApiKey(WEAVIATE_API_KEY),
)

llm_client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

# ========== STEP 1: RAG function to retrieve thread context ==========
def retrieve_similar_posts(user_query, thread_id, top_k=5):
    query_embedding = embedding_model.encode(user_query).tolist()

    response = weaviate_client.query.get("RedditPost", ["text", "thread_id"])\
        .with_near_vector({"vector": query_embedding})\
        .with_where({
            "path": ["thread_id"],
            "operator": "Equal",
            "valueText": thread_id
        })\
        .with_limit(top_k)\
        .do()

    posts = [item["text"] for item in response["data"]["Get"]["RedditPost"]]
    print(f"🔍 Retrieved {len(posts)} similar posts from thread {thread_id}.")
    return "\n".join(posts)

# ========== STEP 2: LLM call with retry ==========
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def call_openrouter_llm(prompt):
    response = llm_client.chat.completions.create(
        model="mistralai/mistral-7b-instruct:free",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

# ========== STEP 3: Agents ==========
def summarizer_agent(state):
    thread_id = state["thread_id"]
    user_query = state["user_query"]

    print(f"\n🧠 Summarizer Agent triggered for Thread ID: {thread_id}")
    print(f"🎯 Query: {user_query}")

    context = retrieve_similar_posts(user_query, thread_id)
    prompt = f"""You are a helpful Reddit thread summarizer.
Here is the thread content:\n\n{context}\n\n
Summarize this in 3 bullet points."""

    summary = call_openrouter_llm(prompt)

    return {
        **state,
        "summary": summary,
    }

def moderator_agent(state: Dict) -> Dict:
    thread_id = state["thread_id"]
    user_query = state["user_query"]

    print(f"\n🛡️ Moderator Agent triggered for Thread ID: {thread_id}")

    context = retrieve_similar_posts(user_query, thread_id)

    prompt = f"""You are a Reddit thread moderation assistant.
Here is a thread:\n\n{context}

Your job:
- Flag any comments that are toxic, offensive, or biased.
- Identify any irrelevant or off-topic messages.
- If all is clean, say "✅ All good. No toxic content."

Respond with a concise moderation report."""

    report = call_openrouter_llm(prompt)

    return {
        **state,
        "moderation_report": report,
    }

def reply_assistant_agent(state):
    thread_id = state["thread_id"]
    user_query = state["user_query"]
    summary = state["summary"]

    print(f"\n💬 Reply Assistant Agent triggered for Thread ID: {thread_id}")

    context = retrieve_similar_posts(user_query, thread_id)

    prompt = f"""You are a Reddit assistant that helps users respond to threads.
Here is the thread:\n\n{context}

Thread Summary:\n{summary}

Based on this, generate a helpful, friendly, and non-toxic Reddit-style reply the user can post. Limit to 2–3 sentences."""

    reply = call_openrouter_llm(prompt)

    return {
        **state,
        "reply_suggestion": reply
    }

# ========== STEP 4: LangGraph Orchestration ==========

@retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
def safe_invoke(graph, input_state):
    return graph.invoke(input_state)

def run_graph(thread_id, user_query, verbose=False):
    # Optional: check Weaviate connectivity before graph starts
    if not weaviate_client.is_ready():
        raise RuntimeError("Weaviate cluster not ready. Try again in a few seconds.")

    builder = StateGraph(schema={
        "thread_id": str,
        "user_query": str,
        "summary": str,
        "moderation_report": str,
        "reply_suggestion": str
    })

    builder.add_node("summarizer", summarizer_agent)
    builder.add_node("moderator", moderator_agent)
    builder.add_node("reply_assistant", reply_assistant_agent)

    builder.set_entry_point("summarizer")
    builder.add_edge("summarizer", "moderator")
    builder.add_edge("moderator", "reply_assistant")
    builder.add_edge("reply_assistant", END)

    graph = builder.compile()

    try:
        start = time.time()
        result = safe_invoke(graph, {"thread_id": thread_id, "user_query": user_query})
        latency = round(time.time() - start, 2)
        result["latency"] = latency
        if verbose:
            print("🧪 Final Graph Output:")
            print(result)
        return result
    except Exception as e:
        raise RuntimeError(f"❌ Agent workflow failed: {str(e)}")
