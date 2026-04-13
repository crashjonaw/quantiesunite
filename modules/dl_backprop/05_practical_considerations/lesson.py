TITLE = "Practical Considerations"

SECTIONS = [
    {
        "id": "vanishing_gradients",
        "title": "Vanishing Gradient Problem",
        "body": """
<div class="warning-box formula-box">
    <h3 style="color: #f85149;">The Vanishing Gradient Problem</h3>
    <p>In deep networks, gradients can become exponentially small:</p>
    <p>$$\\frac{\\partial L}{\\partial w^{(1)}} = \\frac{\\partial L}{\\partial w^{(L)}} \\prod_{l=1}^{L-1} \\sigma'(z^{(l)})$$</p>
    <p>For sigmoid: \(\\sigma'(z) \\leq 0.25\). Over 20 layers: \((0.25)^{20} \\approx 10^{-13}\)</p>
    <p style="margin-top: 12px;"><strong>Result:</strong> Early layers receive tiny gradients and learn slowly or not at all.</p>
</div>
"""
    },
    {
        "id": "exploding_gradients",
        "title": "Exploding Gradient Problem",
        "body": """
<div class="warning-box formula-box">
    <h3 style="color: #f85149;">The Exploding Gradient Problem</h3>
    <p>Conversely, gradients can explode when activation derivatives are large:</p>
    <p>If \(\\sigma'(z) > 1\) in many layers, products grow exponentially:</p>
    <p>$$\\prod_{l=1}^{L} \\sigma'(z^{(l)}) \\approx 2^L \\to \\infty$$</p>
    <p style="margin-top: 12px;"><strong>Result:</strong> Parameters receive huge gradient updates, causing instability and NaN values (numerical overflow).</p>
</div>
"""
    },
    {
        "id": "solutions",
        "title": "Solutions and Best Practices",
        "body": """
<div class="success-box formula-box">
    <h3 class="accent-heading">Techniques to Mitigate Issues</h3>
    <p><strong>For vanishing gradients:</strong></p>
    <ul>
        <li>Use ReLU or other activations with larger derivatives</li>
        <li>Employ residual connections (skip connections)</li>
        <li>Use batch normalization to keep activations in stable ranges</li>
        <li>Use LSTM/GRU in RNNs to maintain gradients through time</li>
    </ul>
    <p><strong>For exploding gradients:</strong></p>
    <ul>
        <li>Gradient clipping: cap gradient norms before updates</li>
        <li>Weight initialization: careful schemes (Xavier, He initialization)</li>
        <li>Batch normalization: stabilizes gradient flow</li>
    </ul>
</div>
"""
    },
    {
        "id": "autodiff_frameworks",
        "title": "Automatic Differentiation in Modern Frameworks",
        "body": """
<div class="concept-box formula-box">
    <h3 class="accent-heading">From Theory to Practice</h3>
    <p>Modern frameworks (PyTorch, TensorFlow) implement backpropagation via automatic differentiation:</p>
    <ul>
        <li>Users write the forward pass; backward is automatic</li>
        <li>Frameworks build computation graphs and apply chain rule automatically</li>
        <li>GPU acceleration makes large-scale training feasible</li>
    </ul>
    <p style="margin-top: 12px;"><strong>Key insight:</strong> Understanding backprop principles helps debug training issues and design better architectures.</p>
</div>
"""
    }
]
