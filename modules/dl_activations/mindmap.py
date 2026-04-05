MINDMAP = {
    "concepts": [
        {"title": "Why Activations?", "points": [
            "Without non-linear activations, stacked linear layers collapse to a single linear layer",
            "Activations introduce non-linearity so networks can learn complex functions",
            "Choice of activation affects gradient flow, training speed, and final performance",
        ]},
        {"title": "Sigmoid", "points": [
            "\\(\\sigma(x) = \\frac{1}{1+e^{-x}}\\), output in \\((0, 1)\\)",
            "Useful for binary classification output and gating mechanisms (LSTM)",
            "Drawback: saturates for large |x|, causing vanishing gradients; output not zero-centred",
        ]},
        {"title": "Tanh", "points": [
            "\\(\\tanh(x) = \\frac{e^x - e^{-x}}{e^x + e^{-x}}\\), output in \\((-1, 1)\\)",
            "Zero-centred — often converges faster than sigmoid in hidden layers",
            "Still saturates at extremes, leading to vanishing gradients in deep networks",
        ]},
        {"title": "ReLU Family", "points": [
            "ReLU: \\(\\max(0, x)\\) — simple, fast, no saturation for \\(x > 0\\)",
            "Dying ReLU problem: neurons with negative input always output 0 and stop learning",
            "Leaky ReLU: \\(\\max(\\alpha x, x)\\) with small \\(\\alpha\\) (e.g. 0.01) keeps gradient alive",
            "GELU: \\(x \\cdot \\Phi(x)\\) — smooth approximation used in Transformers (BERT, GPT)",
        ]},
        {"title": "Softmax", "points": [
            "Converts a vector of logits into a probability distribution",
            "\\(\\text{softmax}(z_i) = \\frac{e^{z_i}}{\\sum_j e^{z_j}}\\)",
            "Used in the final layer for multi-class classification",
        ]},
    ],
    "formulas": [
        {"label": "Sigmoid", "expr": "\\(\\sigma(x) = \\frac{1}{1 + e^{-x}}, \\quad \\sigma'(x) = \\sigma(x)(1 - \\sigma(x))\\)"},
        {"label": "Tanh", "expr": "\\(\\tanh'(x) = 1 - \\tanh^2(x)\\)"},
        {"label": "ReLU", "expr": "\\(\\text{ReLU}(x) = \\max(0, x), \\quad \\text{ReLU}'(x) = \\begin{cases}1 & x > 0 \\\\ 0 & x \\le 0\\end{cases}\\)"},
        {"label": "Leaky ReLU", "expr": "\\(\\text{LeakyReLU}(x) = \\max(\\alpha x, x)\\)"},
        {"label": "GELU", "expr": "\\(\\text{GELU}(x) = x \\cdot \\Phi(x) \\approx x \\cdot \\sigma(1.702x)\\)"},
        {"label": "Softmax", "expr": "\\(\\text{softmax}(z_i) = \\frac{e^{z_i}}{\\sum_{j} e^{z_j}}\\)"},
    ],
    "tips": [
        "Default choice for hidden layers: ReLU (or GELU for Transformer models).",
        "Use sigmoid only for output gates or binary classification outputs, not hidden layers.",
        "If many neurons die (output always 0), try Leaky ReLU or reduce the learning rate.",
    ],
}
