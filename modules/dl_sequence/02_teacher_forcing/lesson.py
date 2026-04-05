TITLE = "Teacher Forcing and Decoding Strategies"

SECTIONS = [
    {
        "id": "teacher_forcing_concept",
        "title": "Teacher Forcing: Training with Ground Truth",
        "body": "<p>During training, the decoder uses ground truth tokens from the target sequence as input, rather than its own predictions. At step \\(t\\), the decoder receives \\(y_{t-1}^{\\text{true}}\\) from the data.</p><p>This accelerates training convergence and provides stable gradient flow. The model learns to map correct contexts to correct outputs.</p>"
    },
    {
        "id": "exposure_bias",
        "title": "Exposure Bias Problem",
        "body": "<p>At inference time, the decoder uses its own predictions as input: \\(y_{t-1}^{\\text{pred}}\\). These differ from ground truth, creating a mismatch called exposure bias.</p><p>Errors accumulate: a wrong token at step \\(t\\) propagates errors to step \\(t+1\\), potentially cascading through the sequence.</p><p>Teacher forcing trains on ground truth but tests on predictions, harming generalization.</p>"
    },
    {
        "id": "scheduled_sampling",
        "title": "Scheduled Sampling and Mixing Strategies",
        "body": "<p>To bridge the gap, scheduled sampling randomly switches between ground truth and predicted tokens during training. Early epochs use mostly ground truth; later epochs increase predicted token usage.</p><p>This gradually exposes the model to its own errors during training, reducing the train-test discrepancy.</p><p>Alternative: use predicted tokens with a fixed probability \\(\\epsilon\\) throughout training.</p>"
    },
    {
        "id": "autoregressive_inference",
        "title": "Autoregressive Inference and Greedy Decoding",
        "body": "<p>At inference, greedy decoding selects the highest-probability token at each step: \\(y_t = \\arg\\max P(y_t | y_1, \\ldots, y_{t-1}, c)\\)</p><p>This is fast and deterministic but often suboptimal. Local greedy choices may prevent globally better sequences.</p><p>More sophisticated decoding strategies (beam search, sampling) explore multiple hypotheses to find better outputs.</p>"
    }
]
