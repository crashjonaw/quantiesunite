MINDMAP = {
    "concepts": [
        {"title": "The Perceptron", "points": [
            "Simplest neural unit: weighted sum of inputs plus bias, then threshold",
            "Output: \\(y = \\sigma(w \\cdot x + b)\\) where \\(\\sigma\\) is an activation",
            "Can learn linearly separable functions (AND, OR) but not XOR",
        ]},
        {"title": "Multi-Layer Networks (MLPs)", "points": [
            "Stack layers: input → hidden layer(s) → output",
            "Each layer applies \\(z = Wx + b\\), then \\(a = \\sigma(z)\\)",
            "Hidden layers let the network learn non-linear decision boundaries",
            "Universal approximation theorem: one hidden layer can approximate any continuous function",
        ]},
        {"title": "Forward Pass", "points": [
            "Data flows input → layer 1 → layer 2 → … → output",
            "At each layer: linear transform then non-linear activation",
            "Final layer activation depends on task: softmax (classification), linear (regression)",
        ]},
        {"title": "Weight Initialisation", "points": [
            "Zero init causes symmetry — all neurons learn the same thing",
            "Xavier/Glorot init: \\(W \\sim \\mathcal{N}(0, \\frac{2}{n_{in}+n_{out}})\\)",
            "He init for ReLU networks: \\(W \\sim \\mathcal{N}(0, \\frac{2}{n_{in}})\\)",
        ]},
        {"title": "Training Overview", "points": [
            "Forward pass → compute loss → backward pass (gradients) → update weights",
            "Repeat over mini-batches; one pass through the dataset = one epoch",
            "Learning rate controls step size; too large diverges, too small stalls",
        ]},
    ],
    "formulas": [
        {"label": "Neuron Output", "expr": "\\(a = \\sigma(Wx + b)\\)"},
        {"label": "Softmax", "expr": "\\(\\text{softmax}(z_i) = \\frac{e^{z_i}}{\\sum_j e^{z_j}}\\)"},
        {"label": "Xavier Init", "expr": "\\(W \\sim \\mathcal{N}\\!\\left(0,\\; \\frac{2}{n_{\\text{in}} + n_{\\text{out}}}\\right)\\)"},
        {"label": "He Init", "expr": "\\(W \\sim \\mathcal{N}\\!\\left(0,\\; \\frac{2}{n_{\\text{in}}}\\right)\\)"},
    ],
    "tips": [
        "Start with a small network and add capacity only if underfitting.",
        "Always normalise your input data — it speeds up training and improves stability.",
        "Use He initialisation when using ReLU; Xavier when using tanh or sigmoid.",
    ],
}
