TITLE = "Encoder and Decoder Blocks"

SECTIONS = [
    {
        "id": "tf_encoder",
        "title": "The Encoder: Context Representation",
        "body": '<p>The encoder processes the entire input sequence and produces rich contextual representations. Each position can attend to all other positions in the input.</p><p><strong>Encoder operations (per layer):</strong></p><ul><li>Self-attention: attend to all input positions</li><li>Feed-forward: position-wise transformations</li><li>Residual connections and layer norm</li></ul><p>The encoder output is a sequence of vectors with the same length as the input, each representing the input from the perspective of that position with full context.</p>'
    },
    {
        "id": "tf_decoder",
        "title": "The Decoder: Autoregressive Generation",
        "body": '<p>The decoder generates output one token at a time, with a crucial constraint: each position can only attend to earlier positions (causal masking). This enforces the autoregressive property where future information is hidden.</p><p><strong>Decoder operations (per layer):</strong></p><ul><li>Masked self-attention: attend to previous and current positions only</li><li>Cross-attention: attend to encoder outputs</li><li>Feed-forward: position-wise transformations</li><li>Residual connections and layer norm</li></ul>'
    },
    {
        "id": "tf_causal_masking",
        "title": "Causal Masking: Preventing Information Leakage",
        "body": '<p>During decoding, setting attention weights to zero for future positions forces the model to predict output_i using only outputs 1 to i. This is implemented by masking attention logits with negative infinity before softmax.</p><p>$$\\text{Attention}(Q, K, V) = \\text{softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}} + M\\right)V$$</p><p>Where M is a lower-triangular mask (0 for valid positions, $$-\\infty$$ for masked positions). This constraint enables autoregressive generation while maintaining the full Transformer architecture.</p>'
    },
    {
        "id": "tf_cross_attention_mechanism",
        "title": "Cross-Attention: Connecting Encoder and Decoder",
        "body": '<p>While decoder self-attention is masked, cross-attention is not. The decoder queries the entire encoder output:</p><p>$$\\text{CrossAttention}(Q_{decoder}, K_{encoder}, V_{encoder})$$</p><p>This allows the decoder to freely attend to all encoder positions when deciding what to generate next. The decoder learns which parts of the input are most relevant for generating each output token.</p>'
    }
]
