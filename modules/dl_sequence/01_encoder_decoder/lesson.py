TITLE = "Encoder-Decoder Architecture"

SECTIONS = [
    {
        "id": "encoder_structure",
        "title": "Encoder: Processing Input Sequence",
        "body": "<p>The encoder is an RNN (LSTM, GRU) that reads the entire input sequence and produces a fixed-size context vector. For sequence \\(x_1, x_2, \\ldots, x_T\\), the encoder computes hidden states \\(h_t\\) at each step, with the final state \\(h_T\\) serving as the initial context.</p><p>Mathematical form: \\(h_t = \\text{RNN}(x_t, h_{t-1})\\)</p><p>The context vector \\(c = h_T\\) encodes the entire input meaning into a single representation.</p>"
    },
    {
        "id": "decoder_generation",
        "title": "Decoder: Generating Output Sequence",
        "body": "<p>The decoder is another RNN initialized with the encoder's context vector. It generates output tokens one at a time, using previously generated tokens as input.</p><p>At step \\(t\\), the decoder computes: \\(y_t = \\arg\\max P(y_t | y_1, \\ldots, y_{t-1}, c)\\)</p><p>This allows variable-length outputs and flexible generation strategies.</p>"
    },
    {
        "id": "bottleneck_limitation",
        "title": "The Information Bottleneck",
        "body": "<p>A key limitation: all input information must compress into a single context vector \\(c\\). This creates a bottleneck for long sequences, where important early information may be forgotten.</p><p>For machine translation of long sentences, the fixed context may lose crucial source-language details. This motivates the use of attention mechanisms to preserve access to all encoder states.</p>"
    },
    {
        "id": "training_objective",
        "title": "Training Loss and Optimization",
        "body": "<p>The encoder-decoder is trained end-to-end to minimize the negative log-likelihood of the target sequence:</p><p>\\(L = -\\sum_{t=1}^{M} \\log P(y_t | y_1, \\ldots, y_{t-1}, c)\\)</p><p>Backpropagation flows through both decoder and encoder. Early stopping or curriculum learning can stabilize training.</p>"
    }
]
