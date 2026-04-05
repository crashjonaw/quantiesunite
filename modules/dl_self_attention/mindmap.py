MINDMAP = {
    "concepts": [
        {"title": "Self-Attention", "points": [
            "Each token in a sequence attends to every other token (including itself)",
            "Q, K, V are all derived from the same input: \\(Q = XW^Q,\\; K = XW^K,\\; V = XW^V\\)",
            "Captures long-range dependencies in a single operation — no recurrence needed",
            "Computational cost: \\(O(n^2 d)\\) where \\(n\\) is sequence length and \\(d\\) is dimension",
        ]},
        {"title": "Scaled Dot-Product Attention", "points": [
            "Score: \\(\\frac{QK^T}{\\sqrt{d_k}}\\) — scaling prevents softmax saturation",
            "Weights: \\(\\text{softmax}(\\text{scores})\\) — each row sums to 1",
            "Output: weighted combination of value vectors",
        ]},
        {"title": "Multi-Head Attention", "points": [
            "Run \\(h\\) attention heads in parallel, each with different learned projections",
            "Each head: \\(d_k = d_v = d_{\\text{model}} / h\\)",
            "Concatenate heads and project: \\(\\text{MultiHead} = \\text{Concat}(\\text{head}_1, \\ldots, \\text{head}_h)W^O\\)",
            "Different heads can learn different relationship types (syntax, semantics, position)",
        ]},
        {"title": "Masking", "points": [
            "Padding mask: ignore padding tokens (set attention score to \\(-\\infty\\))",
            "Causal mask: prevent attending to future tokens (upper triangular mask)",
            "Both are applied before softmax",
        ]},
        {"title": "Efficient Attention Variants", "points": [
            "Linear attention: approximate softmax to reduce \\(O(n^2)\\) to \\(O(n)\\)",
            "Sparse attention (Longformer, BigBird): attend only to local + global tokens",
            "Flash Attention: hardware-aware exact attention with reduced memory I/O",
        ]},
    ],
    "formulas": [
        {"label": "Self-Attention", "expr": "\\(\\text{Attention}(Q,K,V) = \\text{softmax}\\!\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right)V\\)"},
        {"label": "Projections", "expr": "\\(Q = XW^Q, \\quad K = XW^K, \\quad V = XW^V\\)"},
        {"label": "Multi-Head Output", "expr": "\\(\\text{MultiHead}(X) = \\text{Concat}(\\text{head}_1, \\ldots, \\text{head}_h)W^O\\)"},
        {"label": "Head Dimension", "expr": "\\(d_k = d_v = \\frac{d_{\\text{model}}}{h}\\)"},
        {"label": "Causal Mask", "expr": "\\(\\text{score}_{ij} = -\\infty \\text{ if } j > i\\)"},
    ],
    "tips": [
        "Multi-head attention is not more expensive than single-head: total computation is the same because \\(d_k = d_{\\text{model}} / h\\).",
        "Attention weights are a useful diagnostic: visualise them to understand what the model learns.",
        "For very long sequences (>4096 tokens), consider sparse or linear attention variants.",
        "The number of heads is a hyperparameter: 8 or 12 heads is standard for base-size models.",
    ],
}
