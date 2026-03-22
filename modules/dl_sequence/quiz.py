QUIZ = [
    {"id": "q1", "type": "multiple_choice", "question": "Language model trained on:", "options": ["Classification", "Next token prediction", "Clustering", "Ranking"], "correct": 1},
    {"id": "q2", "type": "fill_blank", "question": "Encoder-decoder bottleneck: single ____ vector", "answer": "context"},
    {"id": "q3", "type": "true_false", "question": "Attention weights always sum to 1", "correct": True},
    {"id": "q4", "type": "multiple_choice", "question": "Beam search width = vocabulary size?", "options": ["Always", "Sometimes", "Never necessary", "In linear complexity"], "correct": 1},
    {"id": "q5", "type": "true_false", "question": "Greedy decoding optimal for generation", "correct": False},
    {"id": "q6", "type": "multiple_choice", "question": "CTC loss handles:", "options": ["Exact alignment", "Variable lengths", "Fixed sequences", "Supervised only"], "correct": 1},
    {"id": "q7", "type": "numerical", "question": "Temperature scaling: softmax(logits/T). Higher T → ?", "answer": 1, "tolerance": 0},
    {"id": "q8", "type": "true_false", "question": "Attention can be computed over all decoder layers", "correct": True}
]