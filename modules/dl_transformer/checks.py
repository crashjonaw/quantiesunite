CHECKS = [
    {"section": "tf_motivation", "type": "true_false", "question": "Transformers parallelize across time", "correct": True},
    {"section": "tf_architecture", "type": "fill_blank", "question": "Transformer has ____ and decoder stacks", "answer": "encoder"},
    {"section": "tf_positional_encoding", "type": "true_false", "question": "Positional encodings are learnable parameters", "correct": False},
    {"section": "tf_multihead", "type": "multiple_choice", "question": "Multi-head attention uses:", "options": ["One representation", "Multiple parallel heads", "Sequential attention", "Averaged attention"], "correct": 1},
    {"section": "tf_scaling", "type": "fill_blank", "question": "Scale attention by \\(\\sqrt{____}\\)", "answer": "d_k"},
    {"section": "tf_feedforward", "type": "fill_blank", "question": "Each layer ends with ____ & Norm", "answer": "Add"}
]