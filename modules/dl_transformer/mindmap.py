MINDMAP = {
    "concepts": [
        {"title": "Transformer Overview", "points": [
            "Introduced in 'Attention Is All You Need' (Vaswani et al., 2017)",
            "Replaces recurrence entirely with self-attention — enables full parallelisation",
            "Encoder-decoder architecture; each block has attention + feed-forward layers",
        ]},
        {"title": "Encoder Block", "points": [
            "Multi-head self-attention → Add & LayerNorm → Feed-forward → Add & LayerNorm",
            "Self-attention: each token attends to all other tokens in the input",
            "Feed-forward: two linear layers with ReLU/GELU activation in between",
        ]},
        {"title": "Decoder Block", "points": [
            "Masked multi-head self-attention (causal: can only attend to earlier positions)",
            "Cross-attention over encoder output (queries from decoder, keys/values from encoder)",
            "Same feed-forward + residual + LayerNorm structure as encoder",
        ]},
        {"title": "Positional Encoding", "points": [
            "Self-attention is permutation-invariant — order information must be injected",
            "Sinusoidal: \\(PE_{(pos, 2i)} = \\sin(pos / 10000^{2i/d})\\)",
            "Learned positional embeddings are also common (BERT, GPT)",
        ]},
        {"title": "Key Design Choices", "points": [
            "Residual connections: \\(\\text{output} = \\text{LayerNorm}(x + \\text{Sublayer}(x))\\)",
            "Layer normalisation stabilises training in deep stacks",
            "Typical sizes: \\(d_{\\text{model}}\\) = 512 or 768, 6-12 layers, 8-12 heads",
        ]},
    ],
    "formulas": [
        {"label": "Scaled Dot-Product Attention", "expr": "\\(\\text{Attention}(Q,K,V) = \\text{softmax}\\!\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right)V\\)"},
        {"label": "Multi-Head Attention", "expr": "\\(\\text{MultiHead}(Q,K,V) = \\text{Concat}(\\text{head}_1, \\ldots, \\text{head}_h)W^O\\)"},
        {"label": "Each Head", "expr": "\\(\\text{head}_i = \\text{Attention}(QW_i^Q, KW_i^K, VW_i^V)\\)"},
        {"label": "Positional Encoding", "expr": "\\(PE_{(pos,2i)} = \\sin\\!\\left(\\frac{pos}{10000^{2i/d}}\\right), \\quad PE_{(pos,2i+1)} = \\cos\\!\\left(\\frac{pos}{10000^{2i/d}}\\right)\\)"},
        {"label": "Feed-Forward", "expr": "\\(\\text{FFN}(x) = W_2 \\cdot \\text{ReLU}(W_1 x + b_1) + b_2\\)"},
    ],
    "tips": [
        "The scaling factor \\(1/\\sqrt{d_k}\\) prevents dot products from growing too large and saturating softmax.",
        "Pre-norm (LayerNorm before sublayer) often trains more stably than post-norm for deep models.",
        "Transformers need large datasets to outperform RNNs — they have less inductive bias for sequences.",
        "Causal masking in the decoder prevents information leakage from future tokens.",
    ],
}
