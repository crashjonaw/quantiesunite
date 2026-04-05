TITLE = "Feed-Forward Networks and Layer Normalization"

SECTIONS = [
    {
        "id": "tf_feedforward",
        "title": "Position-Wise Feed-Forward Networks",
        "body": '<p>After attention, each position is processed independently through an identical feed-forward network:</p><p>$$\\text{FFN}(x) = \\max(0, xW_1 + b_1)W_2 + b_2$$</p><p>This is a two-layer network with a ReLU activation. The inner dimension is typically 4 times the model dimension (e.g., 2048 for $$d_{model} = 512$$).</p><p><strong>Why position-wise?</strong> The same weights apply to every position, but positions are processed in parallel. This adds nonlinearity and allows the model to learn position-specific transformations.</p>'
    },
    {
        "id": "tf_residual",
        "title": "Residual Connections: Learning Incremental Updates",
        "body": '<p>Each sub-layer (attention or FFN) uses a residual connection:</p><p>$$\\text{Output} = \\text{SubLayer}(x) + x$$</p><p>This allows gradients to flow directly through the network and lets layers learn incremental updates rather than complete transformations. Without residuals, deep networks are much harder to train.</p>'
    },
    {
        "id": "tf_normalization",
        "title": "Layer Normalization: Stabilizing Training",
        "body": '<p>Layer norm is applied after each residual connection:</p><p>$$\\text{LayerNorm}(x) = \\gamma \\odot \\frac{x - \\mu}{\\sqrt{\\sigma^2 + \\epsilon}} + \\beta$$</p><p>Where normalization is computed across the feature dimension (not batch). This stabilizes activations, prevents internal covariate shift, and makes training more stable at higher learning rates.</p><p><strong>Placement:</strong> Pre-norm (before sub-layer) or post-norm (after residual) both work, with subtle training dynamics differences.</p>'
    },
    {
        "id": "tf_layer_structure",
        "title": "Complete Layer Structure",
        "body": '<p>A single Transformer layer combines all components:</p><p>1. Multi-head self-attention → residual connection → layer norm</p><p>2. Position-wise feed-forward → residual connection → layer norm</p><p>Stacking N of these layers creates the encoder or decoder. The final representation after all layers is then ready for task-specific output layers (e.g., softmax for classification).</p>'
    }
]
