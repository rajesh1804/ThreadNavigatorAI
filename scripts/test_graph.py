from agent_graph import run_graph

response = run_graph(
    thread_id="thread_001",
    user_query="What's the main takeaway from this M4 chip thread?"
)

print("\n📝 Thread Summary:\n")
print(response["summary"])

print("\n🛡️ Moderation Report:\n")
print(response["moderation_report"])

print("\n💬 Reply Suggestion:\n")
print(response["reply_suggestion"])
