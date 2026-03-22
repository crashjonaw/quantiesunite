CHECKS = [
    {"section": "lstm_motivation", "type": "true_false", "question": "LSTM solves vanishing gradient problem", "correct": True},
    {"section": "lstm_gates", "type": "multiple_choice", "question": "Forget gate controls:", "options": ["New input", "Previous memory", "Output", "Cell state"], "correct": 1},
    {"section": "lstm_cell_state", "type": "fill_blank", "question": "Cell state updated via ____ (not multiplication)", "answer": "addition"},
    {"section": "lstm_hidden_state", "type": "true_false", "question": "Hidden state = output gate * cell state", "correct": False},
    {"section": "lstm_why_works", "type": "fill_blank", "question": "Cell state gradient via addition preserves ____", "answer": "gradients"},
    {"section": "lstm_variants", "type": "fill_blank", "question": "GRU has ____ gates (fewer than LSTM)", "answer": "2"}
]