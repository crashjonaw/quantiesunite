TITLE = "Transformer Architecture Overview"

SECTIONS = [
    {
        "id": "tf_motivation",
        "title": "Beyond RNNs: Parallelizable Sequence Modeling",
        "body": '<p>RNNs process sequences step-by-step, making it impossible to parallelize computation across time steps. Transformers break this constraint by allowing all positions to attend to each other simultaneously, enabling massive parallel computation.</p><p><strong>Key insight:</strong> Attention mechanisms replace sequential dependence with direct, parallelizable interactions.</p>'
    },
    {
        "id": "tf_architecture",
        "title": "Transformer Architecture: Encoder-Decoder Framework",
        "body": '<p>The canonical Transformer consists of two main stacks:</p><ul><li><strong>Encoder:</strong> Processes input sequence via stacked layers of multi-head attention and feed-forward networks</li><li><strong>Decoder:</strong> Generates output autoregressively, with access to both self-attention and encoder outputs via cross-attention</li></ul><p>Each stack contains $$N$$ identical layers (typically 6 in the original design).</p>'
    },
    {
        "id": "tf_positional_encoding",
        "title": "Positional Encoding: Injecting Order Without Recurrence",
        "body": '<p>Without recurrence, the model has no inherent sense of position. Positional encodings inject order information directly:</p><p>$$PE_{pos,2i} = \\sin\\left(\\frac{pos}{10000^{2i/d}}\\right)$$</p><p>$$PE_{pos,2i+1} = \\cos\\left(\\frac{pos}{10000^{2i/d}}\\right)$$</p><p>These sinusoidal patterns allow the model to learn relative position information and extrapolate to longer sequences.</p>'
    },
    {
        "id": "tf_first_principles",
        "title": "From First Principles: Sequence-to-Sequence with Attention",
        "body": '<p>Transformers solve the fundamental problem: given a variable-length input sequence, produce a variable-length output where each output element can depend on the entire input. The attention mechanism answers the question: for each output position, which input positions are most relevant?</p>'
    }
]
