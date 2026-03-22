QUIZ = [
    {"id": "q1", "type": "multiple_choice", "question": "Backprop uses chain rule to:", "options": ["Compute loss", "Compute gradients", "Initialize weights", "Select activation"], "correct": 1},
    {"id": "q2", "type": "true_false", "question": "Must compute forward pass before backward", "correct": True},
    {"id": "q3", "type": "fill_blank", "question": "Gradient of loss w.r.t. weight w: dL/dw", "answer": "gradient"},
    {"id": "q4", "type": "multiple_choice", "question": "Vanishing gradient problem occurs with:", "options": ["ReLU", "Sigmoid in deep nets", "Linear activation", "Batch norm"], "correct": 1},
    {"id": "q5", "type": "true_false", "question": "Exploding gradients always bad", "correct": False},
    {"id": "q6", "type": "multiple_choice", "question": "Autodiff computes gradients via:", "options": ["Numerical approximation", "Symbolic manipulation", "Automatic differentiation", "Manual coding"], "correct": 2},
    {"id": "q7", "type": "numerical", "question": "Sigmoid: s(0.5) ≈ ?", "answer": 0.622, "tolerance": 0.01},
    {"id": "q8", "type": "true_false", "question": "Gradient accumulates along all paths in computation graph", "correct": True}
]