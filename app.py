import streamlit as st
from scripts.agent_graph import run_graph
from scripts.eval_samples import sample_options
import time

# ------------------ Streamlit Config ------------------
st.set_page_config(page_title="ThreadNavigatorAI", layout="centered")

# ------------------ Branding Header ------------------
st.markdown("""
# 🧵 ThreadNavigatorAI
**Navigate Reddit-style threads using LLM agents.**
""")
# st.image("https://raw.githubusercontent.com/rajesh1804/ThreadNavigatorAI/main/assets/banner_threadnavigatorai.png", use_column_width=True)

# ------------------ Sidebar: What this app does ------------------
with st.sidebar:
    st.markdown("## 🧠 What is ThreadNavigatorAI?")
    st.markdown("""
- 🤖 AI-powered Reddit-style thread summarizer  
- 🛡️ Moderates for sarcasm, trolling, bias, off-topic  
- 💬 Suggests personalized replies  
- 🔁 Built using LangGraph (Agentic RAG), OpenRouter, and Weaviate  
- 🚀 Deployed on Hugging Face Spaces (Free Tier)
    """)
    st.markdown("---")
    st.markdown("Made by [Rajesh](https://github.com/rajesh1804) | Powered by OpenRouter + LangGraph")

# ------------------ Problem Framing ------------------
st.markdown("""
### 💡 Why ThreadNavigatorAI?

Reddit-style threads are chaotic.  
Trolling, sarcasm, off-topic comments — it's easy to lose the signal in the noise.

**ThreadNavigatorAI** uses **agentic LLM pipelines** to:
- Summarize long threads smartly
- Detect moderation-worthy content
- Suggest intelligent follow-up replies

""")

# ------------------ 🔥 Instant Demo ------------------
if st.button("🔥 Try Smart Demo"):
    thread_id = "thread_002"
    query = "Summarize this thread and point out any sarcasm or trolling"
    with st.spinner("Running LangGraph agents..."):
        try:
            start_time = time.time()
            result = run_graph(thread_id=thread_id, user_query=query)
            latency = round(time.time() - start_time, 2)

            st.success("✅ Demo Complete!")

            st.subheader("📝 Smart Summary")
            st.markdown(result["summary"])

            st.subheader("🛡️ Moderation Report")
            st.markdown(result["moderation_report"])

            st.subheader("💬 Suggested Reply")
            st.markdown(result["reply_suggestion"])

            st.subheader("⏱️ Latency")
            st.success(f"{latency} seconds")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# ------------------ 🧵 Full Agent Workflow ------------------
st.markdown("---")
st.subheader("🧠 Run Agentic Workflow on Any Thread")

thread_id = st.selectbox("📂 Choose a thread", ["thread_001", "thread_002", "thread_003", "thread_004"])

query = st.text_input("💬 Ask your question about the thread",
                      placeholder="e.g. What's the main takeaway? Any bias?")

submit = st.button("🚀 Analyze Thread")

if submit and thread_id and query:
    with st.spinner("Running LangGraph agent pipeline..."):
        try:
            start_time = time.time()
            result = run_graph(thread_id=thread_id, user_query=query)
            latency = round(time.time() - start_time, 2)

            st.success("✅ Analysis Complete!")

            st.subheader("📝 Smart Summary")
            st.markdown(result["summary"])

            st.subheader("🛡️ Moderation Report")
            st.markdown(result["moderation_report"])

            st.subheader("💬 Suggested Reply")
            st.markdown(result["reply_suggestion"])

            st.subheader("⏱️ Latency")
            st.success(f"{latency} seconds")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
else:
    st.caption("💡 Enter a query and click the button to generate results.")

# ------------------ 🧪 Manual Evaluation Samples ------------------
st.markdown("---")
st.subheader("🧪 Manual Evaluation Samples")

sample_label = st.selectbox("🧾 Choose an evaluation case", list(sample_options.keys()))

if st.button("🧪 Run Sample Evaluation"):
    selected_case = sample_options[sample_label]
    thread_id = selected_case["thread_id"]
    user_query = selected_case["query"]
    expected_output = selected_case["expected"]

    with st.spinner("Evaluating agent outputs..."):
        start_time = time.time()
        response = run_graph(thread_id=thread_id, user_query=user_query)
        latency = round(time.time() - start_time, 2)

    st.markdown("### 📥 Sample Input")
    st.write(f"**Thread ID:** `{thread_id}`\n\n**Query:** {user_query}")

    st.markdown("### ✅ Model Output")
    st.write(response.get("summary", "No summary available."))

    st.markdown("### 🎯 Expected Behavior")
    st.info(expected_output)

    st.markdown("### ⏱️ Latency")
    st.success(f"{latency} seconds")
