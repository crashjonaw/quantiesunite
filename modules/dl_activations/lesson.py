SECTIONS = [
    {"id": "af_why_nonlinearity", "title": "Why Nonlinearity is Essential", "content": '<p>Without activation functions, stacking linear layers gives only linear composition. Nonlinearity enables universal approximation.</p>'},
    {"id": "af_sigmoid", "title": "Sigmoid Activation", "content": '<p>$$\\sigma(z) = \\frac{1}{1 + e^{-z}}$$</p><p>Range: (0,1). Derivative: \\(\\sigma\'(z) = \\sigma(z)(1-\\sigma(z))\\)</p>'},
    {"id": "af_tanh", "title": "Hyperbolic Tangent", "content": '<p>$$\\tanh(z) = \\frac{e^z - e^{-z}}{e^z + e^{-z}}$$</p><p>Range: (-1,1). Zero-centered, stronger gradients than sigmoid.</p>'},
    {"id": "af_relu", "title": "Rectified Linear Unit (ReLU)", "content": '<p>$$\\text{ReLU}(z) = \\max(0, z)$$</p><p>Fast, sparse activation, addresses vanishing gradient problem.</p>'},
    {"id": "af_advanced", "title": "Advanced Activations: Leaky ReLU, ELU, GELU", "content": '<p>Leaky ReLU: \\(\\text{LeakyReLU}(z) = \\max(0.01z, z)\\) prevents dead neurons.</p>'},
    {"id": "af_selection", "title": "Choosing Activation Functions", "content": '<p>ReLU for hidden layers (fast, no saturation). Sigmoid/softmax for classification output.</p>'}
]