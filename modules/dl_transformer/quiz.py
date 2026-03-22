QUIZ = [
    {"id": "q1", "type": "true_false", "question": "Transformer requires sequential processing", "correct": False},
    {"id": "q2", "type": "fill_blank", "question": "Position i encoding: sin(i/____)^(2j/d)", "answer": "10000"},
    {"id": "q3", "type": "multiple_choice", "question": "Standard Transformer heads:", "options": ["4", "8", "16", "32"], "correct": 1},
    {"id": "q4", "type": "true_false", "question": "Scaled dot-product prevents gradient overflow", "correct": True},
    {"id": "q5", "type": "fill_blank", "question": "FFN ratio (inner to outer): typically ____x", "answer": "4"},
    {"id": "q6", "type": "multiple_choice", "question": "Layer norm in Transformer:", "options": ["Before attention", "After attention", "Both", "Neither"], "correct": 2},
    {"id": "q7", "type": "numerical", "question": "Query-key dot product scaling: divide by sqrt(d_k). If d_k=64, divide by?", "answer": 8, "tolerance": 0},
    {"id": "q8", "type": "true_false", "question": "Transformer fully replaced RNNs immediately", "correct": False}
]