MINDMAP = {
    "concepts": [
        {"title": "Recurrence Idea", "points": [
            "Process sequences one step at a time, maintaining a hidden state",
            "The hidden state \\(h_t\\) is a summary of all inputs seen so far",
            "Same weights are shared (tied) across all time steps",
        ]},
        {"title": "Vanilla RNN", "points": [
            "Update: \\(h_t = \\tanh(W_{hh} h_{t-1} + W_{xh} x_t + b)\\)",
            "Output: \\(y_t = W_{hy} h_t + b_y\\)",
            "Simple but suffers from vanishing/exploding gradients on long sequences",
        ]},
        {"title": "Backpropagation Through Time (BPTT)", "points": [
            "Unroll the RNN across time steps and apply standard backprop",
            "Gradients flow backward through all time steps — chain of matrix multiplications",
            "Truncated BPTT limits how far back gradients flow to manage cost and stability",
        ]},
        {"title": "Sequence Tasks", "points": [
            "Many-to-one: sequence → single output (e.g., sentiment classification)",
            "One-to-many: single input → sequence (e.g., image captioning)",
            "Many-to-many: sequence → sequence (e.g., translation, tagging)",
        ]},
        {"title": "Bidirectional RNN", "points": [
            "Run two RNNs: one forward, one backward over the sequence",
            "Concatenate hidden states: \\(h_t = [\\overrightarrow{h_t}; \\overleftarrow{h_t}]\\)",
            "Captures context from both past and future — useful for classification tasks",
        ]},
    ],
    "formulas": [
        {"label": "Hidden State", "expr": "\\(h_t = \\tanh(W_{hh} h_{t-1} + W_{xh} x_t + b_h)\\)"},
        {"label": "Output", "expr": "\\(y_t = W_{hy} h_t + b_y\\)"},
        {"label": "Gradient Through Time", "expr": "\\(\\frac{\\partial L}{\\partial h_t} = \\frac{\\partial L}{\\partial h_{t+1}} \\cdot W_{hh}^T \\cdot \\text{diag}(\\tanh'(z_t))\\)"},
    ],
    "tips": [
        "Vanilla RNNs struggle with sequences longer than ~20 steps — use LSTMs or GRUs instead.",
        "Gradient clipping (e.g., max norm 5) is essential for stable RNN training.",
        "Use bidirectional RNNs when you have access to the full sequence at inference time.",
    ],
}
