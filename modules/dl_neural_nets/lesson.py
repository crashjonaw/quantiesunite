SECTIONS = [
    {
        "id": "nn_biological_inspiration",
        "title": "The Biological Neuron & Mathematical Abstraction",
        "content": '<h2>From Biology to Mathematics</h2><p>A biological neuron receives inputs via dendrites, processes them in the soma, and transmits outputs via the axon.</p><div class="concept-box"><h3>The Artificial Neuron</h3><p>An artificial neuron computes a weighted sum of inputs plus bias, then applies an activation function:</p><p>\\(z = \\sum_{i=1}^{n} w_i x_i + b\\)</p><p>\\(a = \\sigma(z)\\)</p></div>'
    },
    {
        "id": "nn_feedforward_architecture",
        "title": "Feedforward Network Architecture",
        "content": '<h2>Stacking Layers</h2><div class="formula-box"><h4>Layer Computation</h4><p>$$\\mathbf{z}^{(l)} = \\mathbf{W}^{(l)} \\mathbf{a}^{(l-1)} + \\mathbf{b}^{(l)}$$</p><p>$$\\mathbf{a}^{(l)} = \\sigma(\\mathbf{z}^{(l)})$$</p></div>'
    },
    {
        "id": "nn_universal_approximation",
        "title": "Universal Approximation Theorem",
        "content": '<h2>Network Expressive Power</h2><div class="success-box"><p>A single hidden layer with nonlinear activation can approximate any continuous function on a compact domain.</p></div>'
    },
    {
        "id": "nn_matrix_operations",
        "title": "Vectorized Batch Processing",
        "content": '<h2>Efficient GPU Computation</h2><div class="formula-box"><h4>Batch Forward Pass</h4><p>$$\\mathbf{Z}^{(l)} = \\mathbf{X} \\mathbf{W}^{(l)T} + \\mathbf{1}_B \\mathbf{b}^{(l)T}$$</p><p>Process B samples simultaneously for \\(10^3-10^6\\times\\) speedup.</p></div>'
    },
    {
        "id": "nn_initialization",
        "title": "Weight Initialization Schemes",
        "content": '<h2>Xavier and He Initialization</h2><div class="formula-box"><h4>He Initialization for ReLU</h4><p>$$\\mathbf{W} \\sim \\mathcal{N}(0, \\frac{2}{n_{in}})$$</p></div>'
    },
    {
        "id": "nn_capacity_analysis",
        "title": "Network Capacity and Design",
        "content": '<h2>Depth vs Width Trade-offs</h2><p>Total parameters: $$\\sum_{l=1}^{L} (n_l \\times n_{l-1} + n_l)$$</p>'
    }
]