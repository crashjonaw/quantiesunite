SECTIONS = [
    {"id": "rnn_motivation", "title": "Why Recurrent Networks: Sequence Dependency", "content": '<p>Feedforward networks ignore order. Sequences have temporal dependencies: \\(x_1, x_2, \\ldots, x_T\\). RNNs maintain hidden state \\(h_t\\).</p>'},
    {"id": "rnn_basic_unit", "title": "The Recurrent Unit: Hidden State Update", "content": '<p>$$h_t = \\sigma(W_{hh} h_{t-1} + W_{xh} x_t + b_h)$$</p><p>$$y_t = W_{hy} h_t + b_y$$</p>'},
    {"id": "rnn_unrolling", "title": "Unrolling Through Time", "content": '<p>Treat sequence as chain of copies. Backprop through time (BPTT) computes gradients across all steps.</p>'},
    {"id": "rnn_bptt", "title": "Backpropagation Through Time", "content": '<p>$$\\frac{\\partial L}{\\partial h_t} = \\frac{\\partial L}{\\partial y_t} \\frac{\\partial y_t}{\\partial h_t} + \\frac{\\partial L}{\\partial h_{t+1}} \\frac{\\partial h_{t+1}}{\\partial h_t}$$</p>'},
    {"id": "rnn_vanishing_exploding", "title": "Vanishing and Exploding Gradients in RNNs", "content": '<p>Gradients multiply \\(\\frac{\\partial h_t}{\\partial h_{t-1}}\\) across T steps. Can vanish (\\times 0.9^T\\)) or explode (\\times 1.1^T\\)).</p>'},
    {"id": "rnn_bidirectional", "title": "Bidirectional RNNs", "content": '<p>Process sequence both forward and backward. Concatenate outputs for full context at each position.</p>'}
]