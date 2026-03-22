QUIZ = [
    {"id": "q1", "type": "multiple_choice", "question": "RNN hidden state \\(h_t\\) depends on:", "options": ["Only \\(x_t\\)", "Only \\(h_{t-1}\\)", "Both \\(x_t\\) and \\(h_{t-1}\\)", "All previous inputs"], "correct": 2},
    {"id": "q2", "type": "true_false", "question": "Feedforward networks can model long dependencies", "correct": False},
    {"id": "q3", "type": "fill_blank", "question": "RNN weight matrix for hidden-to-hidden: ____", "answer": "W_hh"},
    {"id": "q4", "type": "multiple_choice", "question": "BPTT gradient for \\(h_t\\) involves:", "options": ["Single multiplication", "Product across steps", "Average of gradients", "Max gradient"], "correct": 1},
    {"id": "q5", "type": "true_false", "question": "Vanishing gradient makes learning distant dependencies hard", "correct": True},
    {"id": "q6", "type": "multiple_choice", "question": "Bidirectional RNN best for:", "options": ["Generation", "Full-context classification", "Real-time", "Streaming"], "correct": 1},
    {"id": "q7", "type": "numerical", "question": "Gradient decay factor 0.9 over 10 steps: \\(0.9^{10}\\) ≈ ?", "answer": 0.349, "tolerance": 0.01},
    {"id": "q8", "type": "true_false", "question": "RNN shares weights across time steps", "correct": True}
]