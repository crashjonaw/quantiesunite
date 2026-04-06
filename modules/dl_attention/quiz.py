QUIZ = [
    {"id": "q1", "type": "multiple_choice", "question": "Attention context size:", "options": ["Fixed", "Dynamic per step", "Random", "Shrinking"], "correct": 1},
    {"id": "q2", "type": "fill_blank", "question": "Attention output: \\(c = \\sum_i \\alpha_i \\underline{\\hspace{1cm}}\\)", "answer": "v_i"},
    {"id": "q3", "type": "true_false", "question": "Attention weights sum to 1", "correct": True},
    {"id": "q4", "type": "multiple_choice", "question": "Additive attention matrix W shape:", "options": ["(hidden_dim, 1)", "(hidden_dim, hidden_dim)", "(1, hidden_dim)", "(hidden_dim, 2*hidden_dim)"], "correct": 3},
    {"id": "q5", "type": "true_false", "question": "Hard attention easier to optimize", "correct": False},
    {"id": "q6", "type": "multiple_choice", "question": "Attention computation: query * __", "options": ["Values", "Keys", "Positions", "Gradients"], "correct": 1},
    {"id": "q7", "type": "numerical", "question": "Softmax([0, 1, 0]) first element ≈?", "answer": 0.211, "tolerance": 0.01},
    {"id": "q8", "type": "true_false", "question": "Attention allows model to interpret decisions", "correct": True}
]