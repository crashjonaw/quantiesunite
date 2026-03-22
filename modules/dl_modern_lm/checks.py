CHECKS = [
    {
        "q": "What's the difference between MLM and CLM pre-training objectives?",
        "a": "MLM (BERT): predict masked tokens using bidirectional context. CLM (GPT): predict next token from past only. MLM better for understanding, CLM better for generation.",
        "hint": "MLM = mask and predict. CLM = next token. Different strengths."
    },
    {
        "q": "What is tokenization and why use subword units instead of whole words?",
        "a": "Tokenization converts text to tokens. Subword (BPE, WordPiece) balances: covers most words (smaller vocab than word-level) while handling rare/OOV words (unlike char-level).",
        "hint": "Word-level: huge vocab. Char-level: too granular. Subword: sweet spot."
    },
    {
        "q": "How does fine-tuning enable transfer learning with small datasets?",
        "a": "Pre-training on large corpus learns general language knowledge. Fine-tuning on small labeled data adapts to specific task. Leverages pre-trained weights, needs fewer task examples.",
        "hint": "Pre-train: general knowledge. Fine-tune: task adaptation. Fast, data-efficient."
    },
    {
        "q": "What are scaling laws and what do they imply?",
        "a": "Performance improves predictably with model size (Loss ≈ α N^(-β)). Implies bigger models better (if scaled with data), but compute requirements grow. Trade-off: quality vs cost.",
        "hint": "Bigger model + more data = better performance, predictably. But expensive."
    },
    {
        "q": "What is RLHF and why is it important for modern LLMs?",
        "a": "Reinforcement Learning from Human Feedback: train reward model on human preferences, optimize language model against it. Aligns model with human values, improves instruction-following.",
        "hint": "RLHF = human preferences → better models. Crucial for assistant-like behavior."
    }
]
