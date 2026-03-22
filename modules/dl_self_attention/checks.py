CHECKS = [
    {
        "q": "What is the difference between self-attention and cross-attention?",
        "a": "Self-attention: Q, K, V from same sequence (each position attends to all in sequence). Cross-attention: Q from one, K/V from another (decoder attends to encoder).",
        "hint": "Self = within sequence. Cross = between two sequences."
    },
    {
        "q": "What problem does positional encoding solve?",
        "a": "Self-attention is permutation-invariant (order doesn't matter). Positional encoding adds position info so model learns word order.",
        "hint": "Without position encoding, \"cat dog\" and \"dog cat\" look same to attention. Position encoding differentiates them."
    },
    {
        "q": "Why is multi-head attention better than single-head?",
        "a": "Different heads learn different relationships (syntax, semantics, discourse, etc.). Combined, they capture richer patterns than single head.",
        "hint": "Head 1: local syntax. Head 2: semantic. Head 3: long-range. Together: better."
    },
    {
        "q": "What is the computational complexity of self-attention and why?",
        "a": "O(n²) where n = sequence length. QKᵀ is n×n matrix, softmax is n², memory is O(n²). Long sequences become infeasible.",
        "hint": "Attention matrix: all pairs of positions. n × n = quadratic."
    },
    {
        "q": "What does residual connection do in Transformer block?",
        "a": "Enables deep stacking: gradient can bypass layers. Without it, deep transformers hard to train (vanishing gradients).",
        "hint": "Skip connection: output = input + (attention/feedforward output). Gradient has direct path."
    }
]
