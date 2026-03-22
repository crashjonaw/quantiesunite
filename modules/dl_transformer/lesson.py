SECTIONS = [
    {"id": "tf_motivation", "title": "Beyond RNNs: Parallelizable Sequence Modeling", "content": '<p>RNNs process sequentially; cannot parallelize across time. Transformers process all positions simultaneously via attention.</p>'},
    {"id": "tf_architecture", "title": "Transformer Architecture: Encoder-Decoder", "content": '<p>Encoder: stack of multi-head attention + feed-forward layers. Decoder: similar, but can attend to encoder outputs.</p>'},
    {"id": "tf_positional_encoding", "title": "Positional Encoding", "content": '<p>Since no recurrence, add positional information: $$PE_{pos,2i} = \\sin(pos / 10000^{2i/d})$$</p><p>$$PE_{pos,2i+1} = \\cos(pos / 10000^{2i/d})$$</p>'},
    {"id": "tf_multihead", "title": "Multi-Head Self-Attention", "content": '<p>Multiple attention heads in parallel, each learning different representations. Concatenate and project.</p>'},
    {"id": "tf_scaling", "title": "Scaled Dot-Product Attention", "content": '<p>$$\\text{Attention}(Q, K, V) = \\text{softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right) V$$</p><p>Scale by \\(\\sqrt{d_k}\\) to prevent saturation.</p>'},
    {"id": "tf_feedforward", "title": "Feed-Forward and Residual Connections", "content": '<p>Each layer: Attention → Add & Norm → FFN → Add & Norm. Residual paths ease gradient flow.</p>'}
]