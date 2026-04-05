TITLE = "Regularization and Batch Normalization"

SECTIONS = [
    {
        "id": "nn_capacity_analysis",
        "title": "Network Capacity and Design Trade-offs",
        "body": '<h2>Balancing Expressiveness and Generalization</h2><p>Network capacity—determined by architecture (depth and width)—controls how complex a function the network can learn. Too much capacity leads to overfitting; too little underfits.</p><div class="concept-box"><h3>Parameter Count</h3><p>Total parameters in a network: $$\\sum_{l=1}^{L} (n_l \\times n_{l-1} + n_l)$$</p><p>Where \\(n_l\\) is the number of neurons in layer \\(l\\).</p></div><div class="worked-example"><h3>Example Architecture</h3><p>Network: 784 → 128 → 64 → 10</p><p><strong>Layer 1:</strong> \\(784 \\times 128 + 128 = 100,480\\) parameters</p><p><strong>Layer 2:</strong> \\(128 \\times 64 + 64 = 8,256\\) parameters</p><p><strong>Layer 3:</strong> \\(64 \\times 10 + 10 = 650\\) parameters</p></div>'
    },
    {
        "id": "nn_regularization_techniques",
        "title": "Regularization Techniques",
        "body": '<h2>Preventing Overfitting</h2><p>Regularization methods add constraints to learning, preventing the network from fitting noise in training data.</p><div class="concept-box"><h3>L1 and L2 Regularization</h3><p><strong>L2 (Weight Decay):</strong> \\(L_{total} = L_{data} + \\lambda \\sum_w w^2\\)</p><p>Penalizes large weights, encouraging simpler solutions.</p><p><strong>L1 Regularization:</strong> \\(L_{total} = L_{data} + \\lambda \\sum_w |w|\\)</p><p>Encourages sparsity (some weights shrink to exactly zero).</p></div><div class="worked-example"><h3>Dropout: A Stochastic Approach</h3><p>During training, randomly zero out neurons with probability \\(p\\) (typically 0.5). This prevents co-adaptation and acts like training an ensemble of networks.</p></div>'
    },
    {
        "id": "nn_batch_normalization",
        "title": "Batch Normalization: Stabilizing Training",
        "body": '<h2>The Covariate Shift Problem</h2><p>As network weights change during training, the distribution of activations shifts, requiring careful learning rate tuning. Batch normalization solves this by normalizing activations.</p><div class="concept-box"><h3>Batch Normalization Formula</h3><p>For a batch of activations \\(\\mathbf{z}\\):</p><p>$$\\hat{\\mathbf{z}} = \\frac{\\mathbf{z} - \\bar{\\mathbf{z}}}{\\sqrt{\\text{Var}(\\mathbf{z}) + \\epsilon}}$$</p><p>$$\\mathbf{z}_{\\text{norm}} = \\gamma \\hat{\\mathbf{z}} + \\beta$$</p><p>Where \\(\\gamma\\) and \\(\\beta\\) are learnable scale and shift parameters.</p></div><div class="success-box"><p><strong>Benefits:</strong> Enables faster learning, reduces sensitivity to weight initialization, acts as a regularizer.</p></div>'
    },
    {
        "id": "nn_architectural_insights",
        "title": "Depth vs Width: Modern Architecture Principles",
        "body": '<h2>Design Principles for Effective Networks</h2><p>Empirical research shows that <strong>deep</strong> networks (many layers) are typically more effective than <strong>wide</strong> networks (many neurons) for the same parameter budget.</p><div class="concept-box"><h3>Why Depth Matters</h3><p>Deep architectures leverage hierarchical feature composition, enabling exponentially more expressive functions with fewer parameters. Depth is the defining characteristic of "deep learning".</p></div><div class="warning-box"><p><strong>Training challenge:</strong> Very deep networks suffer from vanishing/exploding gradients. Solutions include proper initialization, batch normalization, and residual connections.</p></div><div class="success-box"><p>Modern state-of-the-art networks (ResNets, Transformers) are very deep, sometimes with 100+ layers.</p></div>'
    }
]
