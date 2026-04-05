MINDMAP = {
    "concepts": [
        {"title": "Motivation for Attention", "points": [
            "Seq2Seq bottleneck: compressing entire input into one fixed vector loses information",
            "Attention lets the decoder look at all encoder hidden states at each step",
            "The decoder learns which parts of the input are relevant for each output token",
        ]},
        {"title": "Attention Mechanism (Bahdanau)", "points": [
            "Compute alignment scores: \\(e_{ij} = a(s_{i-1}, h_j)\\) using a small neural network",
            "Normalise with softmax to get attention weights: \\(\\alpha_{ij} = \\text{softmax}(e_{ij})\\)",
            "Context vector: \\(c_i = \\sum_j \\alpha_{ij} h_j\\) — weighted sum of encoder states",
        ]},
        {"title": "Luong Attention Variants", "points": [
            "Dot-product: \\(e_{ij} = s_i^T h_j\\) — simplest and fastest",
            "General: \\(e_{ij} = s_i^T W_a h_j\\) — adds a learnable weight matrix",
            "Concat: \\(e_{ij} = v_a^T \\tanh(W_a [s_i; h_j])\\) — most expressive but slowest",
        ]},
        {"title": "Attention as Query-Key-Value", "points": [
            "Query (Q): what we are looking for (decoder state)",
            "Key (K): what we compare against (encoder states)",
            "Value (V): what we retrieve (encoder states, often same as K)",
            "Score = similarity(Q, K); output = weighted sum of V",
        ]},
    ],
    "formulas": [
        {"label": "Alignment Score", "expr": "\\(e_{ij} = a(s_{i-1}, h_j)\\)"},
        {"label": "Attention Weights", "expr": "\\(\\alpha_{ij} = \\frac{\\exp(e_{ij})}{\\sum_k \\exp(e_{ik})}\\)"},
        {"label": "Context Vector", "expr": "\\(c_i = \\sum_{j=1}^{T_x} \\alpha_{ij} h_j\\)"},
        {"label": "Dot-Product Score", "expr": "\\(e_{ij} = s_i^T h_j\\)"},
        {"label": "General Score", "expr": "\\(e_{ij} = s_i^T W_a h_j\\)"},
    ],
    "tips": [
        "Visualise attention weights as a heatmap to interpret what the model focuses on.",
        "Dot-product attention is preferred for speed; concat attention is more expressive.",
        "Attention removes the information bottleneck and dramatically improves long-sequence performance.",
    ],
}
