sample_options = {
    "Thread 001 – Apple M4 chip": {
        "thread_id": "thread_001",
        "query": "Summarize this thread and tell me the general sentiment.",
        "expected": "Mentions excitement over M4 performance, slight skepticism about benchmarks, and price-related hopes."
    },
    "Thread 002 – Gemini vs ChatGPT": {
        "thread_id": "thread_002",
        "query": "Summarize this thread and point out any sarcasm or trolling.",
        "expected": "Mentions rivalry between Gemini and ChatGPT. Detects sarcastic 'toaster' comment as trolling."
    },
    "Thread 003 – Student loan forgiveness": {
        "thread_id": "thread_003",
        "query": "Summarize this thread and highlight any biased or emotional responses.",
        "expected": "Mentions polarized views. Notes emotional comment from 'taxpayer1' and off-topic financial product suggestion."
    },
    "Thread 004 – Apple Vision Pro": {
        "thread_id": "thread_004",
        "query": "Summarize this thread and detect any trolling or off-topic derailments.",
        "expected": "Mentions hype and skepticism around Vision Pro. Flags 'Steam Deck' comparison as off-topic."
    }
}
