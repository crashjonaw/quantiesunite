MINDMAP = {
    "concepts": [
        {"title": "The Chain Rule", "points": [
            "If \\(L = f(g(h(x)))\\), then \\(\\frac{dL}{dx} = \\frac{dL}{df} \\cdot \\frac{df}{dg} \\cdot \\frac{dg}{dh} \\cdot \\frac{dh}{dx}\\)",
            "Backpropagation is the chain rule applied systematically through a computation graph",
            "Each node computes a local gradient; the full gradient is the product along the path",
        ]},
        {"title": "Forward & Backward Pass", "points": [
            "Forward pass: compute activations layer by layer and cache intermediate values",
            "Backward pass: compute gradients from output back to input using cached values",
            "Each layer receives \\(\\frac{\\partial L}{\\partial a^{(l)}}\\) and produces \\(\\frac{\\partial L}{\\partial W^{(l)}}\\) and \\(\\frac{\\partial L}{\\partial a^{(l-1)}}\\)",
        ]},
        {"title": "Computation Graphs", "points": [
            "Represent the forward computation as a directed acyclic graph (DAG)",
            "Nodes are operations (+, *, matmul, activation); edges carry tensors",
            "Automatic differentiation frameworks (PyTorch, TensorFlow) build this graph for you",
        ]},
        {"title": "Gradient Flow Problems", "points": [
            "Vanishing gradients: gradients shrink exponentially through many layers (sigmoid/tanh)",
            "Exploding gradients: gradients grow exponentially — weights diverge",
            "Solutions: ReLU activations, residual connections, batch normalisation, gradient clipping",
        ]},
    ],
    "formulas": [
        {"label": "Chain Rule", "expr": "\\(\\frac{\\partial L}{\\partial W^{(l)}} = \\frac{\\partial L}{\\partial z^{(l)}} \\cdot \\frac{\\partial z^{(l)}}{\\partial W^{(l)}}\\)"},
        {"label": "Weight Gradient", "expr": "\\(\\frac{\\partial L}{\\partial W^{(l)}} = \\delta^{(l)} \\cdot (a^{(l-1)})^T\\)"},
        {"label": "Error Signal", "expr": "\\(\\delta^{(l)} = (W^{(l+1)})^T \\delta^{(l+1)} \\odot \\sigma'(z^{(l)})\\)"},
        {"label": "Bias Gradient", "expr": "\\(\\frac{\\partial L}{\\partial b^{(l)}} = \\delta^{(l)}\\)"},
    ],
    "tips": [
        "Backprop is just the chain rule — nothing more. Understand the chain rule deeply.",
        "Always cache forward-pass activations; they are needed during the backward pass.",
        "If gradients vanish, switch from sigmoid to ReLU and consider skip connections.",
        "Use gradient checking (numerical vs analytical) to verify your backprop implementation.",
    ],
}
