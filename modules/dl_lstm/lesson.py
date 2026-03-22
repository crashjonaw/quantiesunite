SECTIONS = [
    {"id": "lstm_motivation", "title": "LSTM: Long Short-Term Memory Architecture", "content": '<p>LSTM solves RNN vanishing gradient via gate mechanisms. Maintains cell state \\(c_t\\) separate from hidden state \\(h_t\\).</p>'},
    {"id": "lstm_gates", "title": "Forget, Input, and Output Gates", "content": '<p>Forget: $$f_t = \\sigma(W_f [h_{t-1}, x_t] + b_f)$$</p><p>Input: $$i_t = \\sigma(W_i [h_{t-1}, x_t] + b_i)$$</p><p>Output: $$o_t = \\sigma(W_o [h_{t-1}, x_t] + b_o)$$</p>'},
    {"id": "lstm_cell_state", "title": "Cell State Update", "content": '<p>$$\\tilde{c}_t = \\tanh(W_c [h_{t-1}, x_t] + b_c)$$</p><p>$$c_t = f_t \\odot c_{t-1} + i_t \\odot \\tilde{c}_t$$</p>'},
    {"id": "lstm_hidden_state", "title": "Hidden State Output", "content": '<p>$$h_t = o_t \\odot \\tanh(c_t)$$</p>'},
    {"id": "lstm_why_works", "title": "Why LSTM Solves Vanishing Gradients", "content": '<p>Cell state changes via addition (forget gate weight \\(f_t\\)), not multiplication. Gradient: $$\\frac{\\partial c_t}{\\partial c_{t-1}} = f_t \\approx 1$$, maintaining gradient flow.</p>'},
    {"id": "lstm_variants", "title": "GRU and Other LSTM Variants", "content": '<p>GRU: 2 gates (reset, update), simpler than LSTM. Peephole LSTM: gates see cell state. Coupled-input-forget: fewer parameters.</p>'}
]