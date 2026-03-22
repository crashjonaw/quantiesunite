CHECKS = [
    {"section": "rnn_motivation", "type": "fill_blank", "question": "RNNs maintain ____ state across time steps", "answer": "hidden"},
    {"section": "rnn_basic_unit", "type": "true_false", "question": "RNN hidden state depends on previous state", "correct": True},
    {"section": "rnn_unrolling", "type": "multiple_choice", "question": "Unrolled RNN is essentially:", "options": ["Parallel network", "Deep feedforward", "Skip connections", "Recursive function"], "correct": 1},
    {"section": "rnn_bptt", "type": "fill_blank", "question": "BPTT stands for Backprop Through ____", "answer": "Time"},
    {"section": "rnn_vanishing_exploding", "type": "true_false", "question": "RNNs can suffer vanishing gradients", "correct": True},
    {"section": "rnn_bidirectional", "type": "true_false", "question": "BiRNN requires future information at each step", "correct": True}
]