TITLE = "Multi-Layer Perceptrons"

SECTIONS = [
    {
        "id": "nn_feedforward_architecture",
        "title": "Feedforward Network Architecture",
        "body": '<h2>Stacking Layers for Expressiveness</h2><p>A multi-layer perceptron (MLP) combines multiple artificial neurons into layers, where outputs of one layer become inputs to the next. This hierarchical structure enables learning increasingly abstract features.</p><div class="concept-box"><h3>Layer Computation</h3><p>Hidden layer \\(l\\) transforms the output from layer \\(l-1\\):</p><p>$$\\mathbf{z}^{(l)} = \\mathbf{W}^{(l)} \\mathbf{a}^{(l-1)} + \\mathbf{b}^{(l)}$$</p><p>$$\\mathbf{a}^{(l)} = \\sigma(\\mathbf{z}^{(l)})$$</p><p>Where \\(\\mathbf{W}^{(l)}\\) is the weight matrix and \\(\\mathbf{a}^{(l)}\\) is the activation output.</p></div>'
    },
    {
        "id": "nn_feature_abstraction",
        "title": "Feature Learning and Abstraction",
        "body": '<h2>Hierarchical Feature Representations</h2><p>Each layer learns progressively more abstract features. Early layers capture low-level patterns (edges, textures), while deeper layers combine these into high-level concepts (shapes, objects).</p><div class="worked-example"><h3>Example: Vision Task</h3><p><strong>Layer 1:</strong> Detects edges and gradients</p><p><strong>Layer 2:</strong> Combines edges into simple shapes</p><p><strong>Layer 3:</strong> Recognizes object parts</p><p><strong>Layer 4:</strong> Classifies complete objects</p></div><div class="success-box"><p>This hierarchical learning enables MLPs to solve complex, non-linear problems.</p></div>'
    },
    {
        "id": "nn_network_composition",
        "title": "Composing Simple Units into Complex Functions",
        "body": '<h2>Function Composition as Learning</h2><p>An MLP is a composition of functions: \\(f(\\mathbf{x}) = \\sigma^{(L)} \\circ \\sigma^{(L-1)} \\circ \\cdots \\circ \\sigma^{(1)}(\\mathbf{x})\\)</p><p>Each layer adds expressive power through nonlinear transformations.</p><div class="concept-box"><h3>Depth and Width</h3><p><strong>Deep networks:</strong> Many layers enable learning complex hierarchies with fewer total parameters.</p><p><strong>Wide networks:</strong> Many neurons per layer increase capacity but may overfit.</p></div>'
    },
    {
        "id": "nn_matrix_operations",
        "title": "Vectorized Batch Processing",
        "body": '<h2>Efficient GPU Computation</h2><p>Processing multiple samples simultaneously (batching) enables massive parallelization on GPUs, providing 1000x+ speedups compared to processing samples one at a time.</p><div class="concept-box"><h4>Batch Forward Pass</h4><p>$$\\mathbf{Z}^{(l)} = \\mathbf{X} \\mathbf{W}^{(l)T} + \\mathbf{1}_B \\mathbf{b}^{(l)T}$$</p><p>Where \\(\\mathbf{X}\\) is a \\(B \\times n_{in}\\) matrix containing \\(B\\) samples.</p></div><div class="success-box"><p>Typical batch sizes: 32, 64, 128, or 256 samples per batch.</p></div>'
    }
]
