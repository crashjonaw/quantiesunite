MINDMAP = {
    "concepts": [
        {"title": "Pre-training & Fine-tuning Paradigm", "points": [
            "Pre-train on massive unlabelled text to learn general language representations",
            "Fine-tune on a small labelled dataset for the specific downstream task",
            "Transfer learning: pre-trained knowledge transfers to new tasks with less data",
        ]},
        {"title": "BERT (Bidirectional Encoder Representations)", "points": [
            "Encoder-only Transformer; processes all tokens bidirectionally",
            "Pre-training objectives: Masked Language Model (MLM) + Next Sentence Prediction (NSP)",
            "MLM: mask 15% of tokens; predict the masked tokens from surrounding context",
            "Fine-tune by adding a task-specific head (classification, QA, NER)",
        ]},
        {"title": "GPT (Generative Pre-trained Transformer)", "points": [
            "Decoder-only Transformer; autoregressive (left-to-right) generation",
            "Pre-training objective: next-token prediction (causal language modelling)",
            "Scaling laws: performance improves predictably with more data, parameters, and compute",
            "GPT-3/4 demonstrate in-context learning — perform tasks from a few prompt examples",
        ]},
        {"title": "Key Techniques", "points": [
            "Tokenisation: BPE (Byte-Pair Encoding) or SentencePiece for subword vocabularies",
            "Positional embeddings: learned (BERT, GPT) or RoPE (rotary, LLaMA)",
            "Layer normalisation and residual connections in every block",
            "KV-cache: store past key/value tensors to speed up autoregressive inference",
        ]},
        {"title": "Alignment & Safety", "points": [
            "RLHF (Reinforcement Learning from Human Feedback) aligns outputs with human preferences",
            "Instruction tuning: fine-tune on prompt-response pairs to follow instructions",
            "Constitutional AI and DPO as alternatives to RLHF",
        ]},
    ],
    "formulas": [
        {"label": "Causal LM Objective", "expr": "\\(L = -\\sum_{t=1}^{T} \\log P(w_t | w_1, \\ldots, w_{t-1}; \\theta)\\)"},
        {"label": "MLM Objective", "expr": "\\(L = -\\sum_{t \\in \\text{masked}} \\log P(w_t | w_{\\backslash t}; \\theta)\\)"},
        {"label": "Scaling Law", "expr": "\\(L(N) \\propto N^{-\\alpha}\\) where \\(N\\) is number of parameters"},
        {"label": "Perplexity", "expr": "\\(\\text{PPL} = \\exp(L / T)\\)"},
    ],
    "tips": [
        "BERT excels at understanding tasks (classification, QA); GPT excels at generation tasks.",
        "Larger models are more sample-efficient: they learn more from less fine-tuning data.",
        "Use a low learning rate (e.g., 2e-5) when fine-tuning pre-trained models to avoid catastrophic forgetting.",
        "For production, consider distillation (e.g., DistilBERT) to reduce model size while retaining most performance.",
    ],
}
