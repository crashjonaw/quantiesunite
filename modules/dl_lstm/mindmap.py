MINDMAP = {
    "concepts": [
        {"title": "Why LSTM?", "points": [
            "Designed to solve the vanishing gradient problem in vanilla RNNs",
            "Introduces a cell state \\(c_t\\) that acts as long-term memory",
            "Gates control what information to keep, forget, or output",
        ]},
        {"title": "Forget Gate", "points": [
            "Decides what to discard from the cell state",
            "\\(f_t = \\sigma(W_f [h_{t-1}, x_t] + b_f)\\)",
            "Output near 0 = forget; near 1 = keep",
        ]},
        {"title": "Input Gate & Candidate", "points": [
            "Input gate: \\(i_t = \\sigma(W_i [h_{t-1}, x_t] + b_i)\\)",
            "Candidate cell: \\(\\tilde{c}_t = \\tanh(W_c [h_{t-1}, x_t] + b_c)\\)",
            "Cell update: \\(c_t = f_t \\odot c_{t-1} + i_t \\odot \\tilde{c}_t\\)",
        ]},
        {"title": "Output Gate", "points": [
            "\\(o_t = \\sigma(W_o [h_{t-1}, x_t] + b_o)\\)",
            "Hidden state: \\(h_t = o_t \\odot \\tanh(c_t)\\)",
            "The hidden state is the LSTM's output at each time step",
        ]},
        {"title": "GRU (Gated Recurrent Unit)", "points": [
            "Simplified LSTM with two gates instead of three (reset and update)",
            "No separate cell state — merges cell and hidden state",
            "Fewer parameters, often comparable performance to LSTM",
        ]},
    ],
    "formulas": [
        {"label": "Forget Gate", "expr": "\\(f_t = \\sigma(W_f [h_{t-1}, x_t] + b_f)\\)"},
        {"label": "Input Gate", "expr": "\\(i_t = \\sigma(W_i [h_{t-1}, x_t] + b_i)\\)"},
        {"label": "Candidate Cell", "expr": "\\(\\tilde{c}_t = \\tanh(W_c [h_{t-1}, x_t] + b_c)\\)"},
        {"label": "Cell State Update", "expr": "\\(c_t = f_t \\odot c_{t-1} + i_t \\odot \\tilde{c}_t\\)"},
        {"label": "Output Gate", "expr": "\\(o_t = \\sigma(W_o [h_{t-1}, x_t] + b_o)\\)"},
        {"label": "Hidden State", "expr": "\\(h_t = o_t \\odot \\tanh(c_t)\\)"},
    ],
    "tips": [
        "Initialise the forget gate bias to 1 so the LSTM defaults to remembering at the start of training.",
        "LSTMs handle sequences of 100-500 steps well; for longer, consider Transformers.",
        "GRUs are a good drop-in replacement when you need fewer parameters or faster training.",
        "Stack multiple LSTM layers for deeper sequence models; 2-3 layers is common.",
    ],
}
