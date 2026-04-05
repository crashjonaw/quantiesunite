MINDMAP = {
    "concepts": [
        {"title": "Gradient Descent Idea", "points": [
            "Move parameters in the direction that decreases the loss",
            "The gradient \\(\\nabla L\\) points uphill; we step in \\(-\\nabla L\\)",
            "Update rule: \\(\\theta \\leftarrow \\theta - \\eta \\nabla_\\theta L\\)",
        ]},
        {"title": "Variants of Gradient Descent", "points": [
            "Batch GD: use entire dataset per update — stable but slow",
            "Stochastic GD (SGD): one sample per update — noisy but fast",
            "Mini-batch GD: compromise — typical batch sizes 32, 64, 128, 256",
        ]},
        {"title": "Learning Rate", "points": [
            "Too large: loss oscillates or diverges",
            "Too small: convergence is very slow",
            "Learning rate schedules: step decay, cosine annealing, warm-up",
        ]},
        {"title": "Momentum & Adaptive Methods", "points": [
            "Momentum: accumulate velocity \\(v_t = \\beta v_{t-1} + \\nabla L\\)",
            "RMSProp: scale gradients by running average of squared gradients",
            "Adam: combines momentum + RMSProp with bias correction",
            "AdamW: Adam with decoupled weight decay (preferred in practice)",
        ]},
        {"title": "Convergence & Local Minima", "points": [
            "Convex problems have a single global minimum — GD always finds it",
            "Neural networks are non-convex; saddle points are more common than local minima",
            "SGD noise helps escape sharp minima and find flatter, more generalisable solutions",
        ]},
    ],
    "formulas": [
        {"label": "SGD Update", "expr": "\\(\\theta_{t+1} = \\theta_t - \\eta \\nabla_\\theta L(\\theta_t)\\)"},
        {"label": "Momentum", "expr": "\\(v_t = \\beta v_{t-1} + \\nabla L, \\quad \\theta_{t+1} = \\theta_t - \\eta v_t\\)"},
        {"label": "Adam Update", "expr": "\\(m_t = \\beta_1 m_{t-1} + (1-\\beta_1)g_t, \\quad v_t = \\beta_2 v_{t-1} + (1-\\beta_2)g_t^2\\)"},
        {"label": "Adam Corrected", "expr": "\\(\\hat{m}_t = \\frac{m_t}{1-\\beta_1^t}, \\quad \\hat{v}_t = \\frac{v_t}{1-\\beta_2^t}, \\quad \\theta_{t+1} = \\theta_t - \\frac{\\eta\\,\\hat{m}_t}{\\sqrt{\\hat{v}_t}+\\epsilon}\\)"},
    ],
    "tips": [
        "Adam with default hyperparameters (lr=0.001, beta1=0.9, beta2=0.999) is a strong baseline.",
        "If training is unstable, reduce the learning rate before changing the architecture.",
        "Gradient clipping (max norm) prevents exploding gradients, especially in RNNs.",
        "Monitor the loss curve: a smooth decrease indicates healthy training.",
    ],
}
