import streamlit as st
from scripts.agent_graph import run_graph
from scripts.eval_samples import sample_options
import time

# ------------------ Streamlit Page Config ------------------
st.set_page_config(page_title="ThreadNavigatorAI", layout="wide")

# ------------------ Branding Header ------------------
st.markdown("""
# 🧵 ThreadNavigatorAI
**Navigate Reddit-style threads using LLM agents**
""")
# st.image("assets/banner_threadnavigatorai.png", width=600)

# ------------------ Sidebar: Product Framing ------------------
with st.sidebar:
    st.markdown("## 💡 Why ThreadNavigatorAI?")
    st.markdown("""
Reddit-style discussions are noisy:
- 😒 Sarcasm, trolling, off-topic replies
- 🤯 Difficult to summarize or moderate

### ✅ This app solves that:
- 🧠 Smart summarization using LLM agents
- 🛡️ Moderation for bias, trolling, and tone
- 💬 Personalized reply suggestions

### ⚙️ Built With:
- 🧠 LangGraph (Agent Orchestration)
- 🌐 OpenRouter (LLMs like Mistral)
- 🧾 Weaviate (Semantic Memory)
- 🖥️ Streamlit (Free-tier UI)
    """)
    st.markdown("---")
    st.caption("Made by [Rajesh](https://github.com/rajesh1804) | Powered by OpenRouter + LangGraph")

# ------------------ Try Demo Button ------------------
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

st.markdown("---")

# ------------------ Dual Column Layout ------------------
col1, col2 = st.columns([1, 1])

# ------------------ 🧠 Agent Workflow Section ------------------
with col1:
    st.subheader("🧠 Run Agentic Workflow")

    thread_id = st.selectbox("📂 Choose a thread", [
        "thread_001", "thread_002", "thread_003", "thread_004"])

    query = st.text_input("💬 Ask a question about the thread", 
                          placeholder="e.g. What's the main takeaway? Any bias?")

    if st.button("🚀 Analyze Thread") and thread_id and query:
        with st.spinner("Running LangGraph pipeline..."):
            try:
                start_time = time.time()
                result = run_graph(thread_id=thread_id, user_query=query)
                latency = round(time.time() - start_time, 2)

                st.success("✅ Analysis Complete!")
                st.markdown("### 📝 Smart Summary")
                st.markdown(result["summary"])

                st.markdown("### 🛡️ Moderation Report")
                st.markdown(result["moderation_report"])

                st.markdown("### 💬 Suggested Reply")
                st.markdown(result["reply_suggestion"])

                st.markdown("### ⏱️ Latency")
                st.success(f"{latency} seconds")

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.caption("💡 Enter a question and click Analyze Thread")

# ------------------ 🧪 Manual Evaluation Section ------------------
with col2:
    st.subheader("🧪 Manual Evaluation Samples")

    sample_label = st.selectbox("🧾 Choose an evaluation case", list(sample_options.keys()))

    if st.button("🧪 Run Sample Evaluation"):
        selected_case = sample_options[sample_label]
        thread_id = selected_case["thread_id"]
        user_query = selected_case["query"]
        expected_output = selected_case["expected"]

        with st.spinner("Evaluating with agents..."):
            try:
                start_time = time.time()
                response = run_graph(thread_id=thread_id, user_query=user_query)
                latency = round(time.time() - start_time, 2)

                st.markdown("### 📥 Sample Input")
                st.code(f"Thread ID: {thread_id}\nQuery: {user_query}", language="text")

                st.markdown("### ✅ Model Output")
                st.markdown(response.get("summary", "No summary returned."))

                st.markdown("### 🎯 Expected Behavior")
                st.info(expected_output)

                st.markdown("### ⏱️ Latency")
                st.success(f"{latency} seconds")

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")