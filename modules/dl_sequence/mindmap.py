MINDMAP = {
    "concepts": [
        {"title": "Sequence-to-Sequence (Seq2Seq)", "points": [
            "Encoder reads input sequence into a context vector; decoder generates output sequence",
            "Originally used stacked LSTMs for both encoder and decoder",
            "The fixed-size context vector is a bottleneck for long sequences",
        ]},
        {"title": "Language Modelling", "points": [
            "Predict the next token given previous tokens: \\(P(w_t | w_1, \\ldots, w_{t-1})\\)",
            "Autoregressive: each generated token feeds back as input for the next step",
            "Perplexity measures model quality: \\(\\text{PPL} = \\exp(-\\frac{1}{N}\\sum \\log P(w_t))\\)",
        ]},
        {"title": "Machine Translation", "points": [
            "Classic application of Seq2Seq with attention",
            "Beam search decoding explores multiple candidate translations simultaneously",
            "BLEU score evaluates translation quality by comparing n-gram overlap",
        ]},
        {"title": "Text Classification & Tagging", "points": [
            "Sentiment analysis: many-to-one — final hidden state → class prediction",
            "Named Entity Recognition (NER): many-to-many — each token gets a label",
            "Part-of-speech tagging: similar to NER, uses bidirectional context",
        ]},
        {"title": "Practical Considerations", "points": [
            "Teacher forcing: use ground-truth tokens as decoder input during training",
            "Scheduled sampling: gradually transition from teacher forcing to model predictions",
            "Padding and masking: handle variable-length sequences in batched training",
        ]},
    ],
    "formulas": [
        {"label": "Language Model", "expr": "\\(P(w_1, \\ldots, w_T) = \\prod_{t=1}^{T} P(w_t | w_1, \\ldots, w_{t-1})\\)"},
        {"label": "Perplexity", "expr": "\\(\\text{PPL} = \\exp\\!\\left(-\\frac{1}{N}\\sum_{t=1}^{N} \\log P(w_t | w_{<t})\\right)\\)"},
        {"label": "BLEU (simplified)", "expr": "\\(\\text{BLEU} = \\text{BP} \\cdot \\exp\\!\\left(\\sum_{n=1}^{4} \\frac{1}{4} \\log p_n\\right)\\)"},
    ],
    "tips": [
        "Teacher forcing speeds up training but can cause exposure bias at inference time.",
        "Beam search with beam width 4-8 usually outperforms greedy decoding.",
        "For modern sequence tasks, Transformers have largely replaced LSTM-based Seq2Seq models.",
        "Always use masking to prevent the model from attending to padding tokens.",
    ],
}
