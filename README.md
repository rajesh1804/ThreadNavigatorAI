---
title: "ThreadNavigatorAI"
emoji: "🧵"
colorFrom: "gray"
colorTo: "indigo"
sdk: streamlit
sdk_version: "1.33.0"
app_file: app.py
pinned: true
---

# 🧵 ThreadNavigatorAI — Reddit-style Summarizer, Moderator & Reply Assistant (Agentic RAG)

[![Built with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red?logo=streamlit)](https://streamlit.io)  
[![Agentic RAG via LangGraph](https://img.shields.io/badge/LangGraph-Agent%20Framework-blueviolet?logo=python)](https://github.com/langchain-ai/langgraph)  
[![Deployed on Hugging Face](https://img.shields.io/badge/Hosted%20on-HuggingFace-orange?logo=huggingface)](https://huggingface.co/spaces/rajesh1804/ThreadNavigatorAI)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 🔍 **ThreadNavigatorAI** is an intelligent Reddit-style assistant that summarizes threads, detects moderation issues, and suggests replies — powered by **LangGraph-based Agent Orchestration + RAG**.

🎯 Built for Reddit, Discord, and social platforms that need smart thread navigation at scale.  
🛠️ Uses only **free-tier tools** (OpenRouter, Weaviate, Streamlit, Hugging Face).

---

## 🧠 What It Solves

_"This thread is messy — what’s the summary, what’s toxic, and how should I respond?"_

Online communities face:
- Too many replies, not enough signal
- Toxic or biased comments
- New users unsure how to engage

ThreadNavigatorAI solves this by:
- 📝 Summarizing the core thread
- 🛡️ Detecting moderation concerns (bias, sarcasm, trolling)
- 💬 Generating helpful replies

---

## 🔧 Key Features

✅ **Multi-agent workflow** (Summarizer, Moderator, Reply Assistant)  
✅ **LangGraph orchestration** with stateful memory and retry logic  
✅ **Vector-based RAG** using Weaviate + Sentence-BERT  
✅ **Manual Evaluation Framework** for recruiters + QA  
✅ **Live LLM Latency Tracking** in UI  
✅ **Streamlit UI with branding, sample queries, and visual appeal**  
✅ **Free-tier deployable** on Hugging Face

---

## 🧠 Agent Workflow Breakdown

> Each user query activates a 3-stage Agentic RAG pipeline orchestrated via LangGraph.

| Agent              | Role                                                                 |
|-------------------|----------------------------------------------------------------------|
| 📝 **Summarizer**     | Uses RAG to summarize key takeaways across the entire thread        |
| 🛡️ **Moderator**      | Flags sarcasm, trolling, biased or off-topic replies               |
| 💬 **Reply Assistant** | Crafts helpful, polite, and context-aware replies for the user     |

All agents share memory via LangGraph's `StateGraph` — allowing responses to influence downstream decisions.

---

## 🖼️ Architecture Overview

<p align="center">
  <img src="https://github.com/rajesh1804/threadnavigatorai/raw/main/assets/threadnavigatorai-architecture.png" alt="Architecture Overview" width="700"/>
</p>

```text
User Query → [LangGraph Agentic Workflow]
              ├──> Summarizer Agent (RAG over thread)
              ├──> Moderator Agent (LLM + heuristics)
              └──> Reply Assistant Agent (LLM response suggestion)

              ↳ Shared Memory + Retry Handling via LangGraph

All backed by:
- Weaviate Vector DB (cloud-hosted)
- Sentence-BERT embeddings
- Mistral-7B (OpenRouter, free-tier)
```

---

## 🧪 Example Flow

> A walkthrough for one simulated thread

**🧵 Thread 002 – Gemini vs ChatGPT**

**Query**:  
> "Summarize this thread and point out any sarcasm or trolling."

**Agent Flow Output**:
- 📝 **Summary**:  
  _Debate between Google’s Gemini and OpenAI’s ChatGPT. Highlights bias and opinions._
- 🛡️ **Moderation Report**:  
  _Detects sarcastic "toaster" comment and subtle trolling in LLM vs AGI debate._
- 💬 **Suggested Reply**:  
  _"Both models have strengths. Let’s stay focused on the facts instead of throwing shade."_

⏱️ **Latency**: 3.2 seconds (displayed in UI)

---

## 🧭 Manual Evaluation Samples

Manually curated QA pairs for demo/testing/evaluation. Integrated directly into the Streamlit UI.

| Thread ID | Scenario | Agent Task |
|-----------|----------|------------|
| thread_001 | Apple M4 chip launch | Sentiment + Summary |
| thread_002 | Gemini vs ChatGPT | Detect sarcasm/trolling |
| thread_003 | Student loan forgiveness | Highlight bias/emotion |
| thread_004 | Apple Vision Pro | Off-topic derailment detection |

Used in UI to demo RAG + LLM + moderation workflows under realistic edge cases.

---

## 🧪 Live Demo

🎯 Try the full agentic flow now on Hugging Face:  
**👉 [ThreadNavigatorAI Demo](https://huggingface.co/spaces/rajesh1804/ThreadNavigatorAI)**

<p align="center">
  <img src="https://github.com/rajesh1804/threadnavigatorai/raw/main/assets/threadnavigatorai-demo.gif" alt="Demo GIF" width="750"/>
</p>

---

## 📁 Project Structure

```bash
ThreadNavigatorAI/
├── app.py                         # Streamlit UI
├── eval_samples.py                # Manual eval dataset
├── scripts/
│   ├── thread_uploader.py         # Uploads simulated Reddit threads to Weaviate
│   ├── summarizer_agent.py        # Summarizer agent logic
│   ├── moderator_agent.py         # Moderator agent logic
│   ├── reply_agent.py             # Reply generator logic
│   └── agent_graph.py             # LangGraph agent orchestration
├── assets/
│   ├── threadnavigatorai-architecture.png
│   └── threadnavigatorai-demo.gif
├── requirements.txt
└── README.md
```

---

## 💼 Why This Project Stands Out

✅ **Agentic RAG + LangGraph orchestration**  
✅ **Evaluation-ready UI with real data**  
✅ **Built like an internal tool for Reddit or Discord moderators**  
✅ **No OpenAI costs — uses OpenRouter free-tier only**  
✅ **Latency, UX, eval — all production-quality**  
✅ **Demonstrates end-to-end agent reasoning + vector retrieval**

> 🎯 Built to impress top-tier AI/ML recruiters, not just LLM hobbyists.

---

## 🧱 CHeckout My Other Projects

| Project               | Description                                                                                       | Skills Showcased                                                                                   | GitHub Repo |
|-----------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------|
| **🛒 GroceryGPT+**      | AI-powered grocery search engine with vector DB, reranking, and typo-tolerant recall              | Semantic search, LLM reranking, Weaviate, Sentence-BERT, OpenRouter                                 | [🔗 Repo](https://github.com/rajesh1804/GroceryGPT) |
| **🚕 RideCastAI**        | Predicts ride fare & ETA with dynamic spatial heatmaps and real-time latency visualization       | Spatio-temporal ML, regression, simulated demand mapping, latency-aware UI                         | [🔗 Repo](https://github.com/rajesh1804/RideCastAI) |
| **🎬 StreamWiseAI**     | Netflix-style movie recommender with a Retention Coach agent and session-aware personalization    | Recommender systems, RAG agent, session memory, fuzzy search, real-time LLM retry handling         | [🔗 Repo](https://github.com/rajesh1804/StreamWiseAI) |

---

## 🚀 Getting Started

```bash
git clone https://github.com/rajesh1804/ThreadNavigatorAI.git
cd ThreadNavigatorAI
pip install -r requirements.txt
```

Create a `.env` file with:

```ini
WEAVIATE_URL=your_cluster_url
WEAVIATE_API_KEY=your_api_key
OPENROUTER_API_KEY=your_openrouter_key
```

Then:

```bash
streamlit run app.py
```

---

## 💡 Skills Demonstrated

✅ LangGraph agent orchestration  
✅ Modular agent design (summarization, moderation, replies)  
✅ Free-tier LLM usage (OpenRouter)  
✅ Weaviate cloud vector DB + RAG over Reddit-style threads  
✅ Manual eval integration in UI  
✅ Latency tracking and real-time feedback  
✅ Streamlit UI with product thinking and branding  
✅ Fully deployable on Hugging Face Spaces

---

## 🧑‍💼 About Me

Built by [**Rajesh Marudhachalam**](https://www.linkedin.com/in/rajesh1804/)  
- AI/ML Engineer UofT CS
- GitHub: [github.com/rajesh1804](https://github.com/rajesh1804)  
- LinkedIn: [linkedin.com/in/rajesh1804](https://www.linkedin.com/in/rajesh1804/)

---

## 🙌 Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph) for stateful agent workflows  
- [OpenRouter](https://openrouter.ai) for free-tier LLM APIs  
- [Weaviate Cloud](https://weaviate.io) for vector storage  
- [Hugging Face Spaces](https://huggingface.co/spaces) for frictionless deployment  
- [Sentence-BERT](https://www.sbert.net) for embeddings  

---

⭐️ *Star this repo if it impressed you. Follow for more elite-level ML + LLM product builds.*
