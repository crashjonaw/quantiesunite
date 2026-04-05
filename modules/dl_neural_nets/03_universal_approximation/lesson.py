TITLE = "Universal Approximation Theorem"

SECTIONS = [
    {
        "id": "nn_universal_approximation",
        "title": "Network Expressive Power",
        "body": '<h2>What Can Neural Networks Represent?</h2><p>A fundamental question in deep learning: given enough neurons and appropriate activation functions, what functions can a neural network represent?</p><div class="success-box"><h3>Universal Approximation Theorem</h3><p>A single hidden layer with a nonlinear activation function and sufficient neurons can approximate any continuous function on a compact domain to arbitrary precision.</p><p>Mathematically: for any continuous function \\(f: [0,1]^n \\to \\mathbb{R}\\) and any \\(\\epsilon > 0\\), there exists a network with one hidden layer such that \\(|f(\\mathbf{x}) - \\text{network}(\\mathbf{x})| < \\epsilon\\) for all \\(\\mathbf{x} \\in [0,1]^n\\).</p></div>'
    },
    {
        "id": "nn_approximation_proof_sketch",
        "title": "Intuition Behind Universal Approximation",
        "body": '<h2>Why Does It Work?</h2><p>The key insight is that neurons with nonlinear activations can create narrow "bumps" in high-dimensional space. By superposing many such bumps, we can approximate any smooth function.</p><div class="concept-box"><h3>The Geometric Intuition</h3><p>Each neuron with sigmoid activation acts as a smooth threshold. Multiple neurons create overlapping threshold regions that collectively approximate complex boundaries.</p></div><div class="worked-example"><h3>Simple Example: XOR Function</h3><p>A network with 1 input layer (2 neurons), 1 hidden layer (2 neurons), and 1 output neuron can learn the XOR function:</p><p><strong>Hidden layer:</strong> Creates two diagonal decision boundaries</p><p><strong>Output layer:</strong> Combines them logically to separate the four regions</p></div>'
    },
    {
        "id": "nn_approximation_limitations",
        "title": "Practical Limitations of Universal Approximation",
        "body": '<h2>Theory vs. Practice</h2><p>While universal approximation is a powerful theoretical guarantee, it has important practical limitations.</p><div class="warning-box"><h3>The Catch</h3><p>Universal approximation says a network CAN approximate any function—but it says nothing about:</p><p><strong>1. Sample complexity:</strong> How many training samples are needed?</p><p><strong>2. Computational feasibility:</strong> How many neurons are actually needed?</p><p><strong>3. Learnability:</strong> Can gradient descent find the right solution?</p></div><div class="concept-box"><h3>The Role of Depth</h3><p>While one hidden layer suffices theoretically, <strong>deep networks</strong> can represent functions with exponentially fewer parameters. This is why depth is crucial in practice.</p></div>'
    }
]
