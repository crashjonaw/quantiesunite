CHECKS = [
    {"section": "af_why_nonlinearity", "type": "true_false", "question": "Stacking linear layers = nonlinear function", "correct": False},
    {"section": "af_sigmoid", "type": "multiple_choice", "question": "Sigmoid range is:", "options": ["(-inf,inf)", "(0,1)", "(-1,1)", "(0,inf)"], "correct": 1},
    {"section": "af_tanh", "type": "true_false", "question": "Tanh is zero-centered", "correct": True},
    {"section": "af_relu", "type": "fill_blank", "question": "ReLU(z) = max(0, __)", "answer": "z"},
    {"section": "af_advanced", "type": "fill_blank", "question": "Leaky ReLU slope for z<0 is typically ____", "answer": "0.01"},
    {"section": "af_selection", "type": "true_false", "question": "Use sigmoid for all layers", "correct": False}
]