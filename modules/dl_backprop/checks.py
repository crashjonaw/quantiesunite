CHECKS = [
    {"section": "bp_chain_rule", "type": "fill_blank", "question": "Chain rule: df/dx = df/dg * dg/____", "answer": "dx"},
    {"section": "bp_computation_graph", "type": "multiple_choice", "question": "Graph nodes represent:", "options": ["Inputs", "Operations", "Weights", "Loss"], "correct": 1},
    {"section": "bp_algorithm", "type": "true_false", "question": "Forward pass needed before backward", "correct": True},
    {"section": "bp_layer_wise", "title": "Gradients flow through ____", "options": ["Forward only", "Backward only", "Entire network", "Single layer"], "correct": 2},
    {"section": "bp_vanishing_gradients", "type": "fill_blank", "question": "Sigmoid derivative max is ____", "answer": "0.25"},
    {"section": "bp_implementation", "type": "true_false", "question": "PyTorch requires manual gradient code", "correct": False}
]