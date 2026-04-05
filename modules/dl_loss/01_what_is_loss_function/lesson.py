TITLE = "What is a Loss Function?"

SECTIONS = [
    {
        "id": "lf_fundamentals",
        "title": "First Principles: Understanding Loss Functions",
        "body": "A loss function quantifies how far a model's predictions are from the true labels. It is the objective that neural networks minimize during training. The choice of loss function depends on the task: regression, classification, or ranking. Loss functions guide the learning process by providing a scalar signal for optimization."
    },
    {
        "id": "lf_role_training",
        "title": "The Role of Loss Functions in Training",
        "body": "During backpropagation, gradients are computed with respect to the loss. These gradients update model parameters to reduce the loss. A well-designed loss function accelerates convergence and leads to better generalization. Different tasks require different loss functions to capture domain-specific objectives."
    },
    {
        "id": "lf_properties",
        "title": "Key Properties of Loss Functions",
        "body": "Ideal loss functions are: (1) Differentiable for gradient-based optimization, (2) Convex or unimodal for easier optimization, (3) Sensitive to prediction errors, (4) Interpretable and aligned with the task metric. Some loss functions prioritize outliers; others focus on typical cases."
    },
    {
        "id": "lf_intuition",
        "title": "Intuition: Why Minimize Loss?",
        "body": "Minimizing loss is equivalent to finding model parameters that best fit the training data. The loss landscape is multidimensional; optimization algorithms navigate this landscape using gradients. Different loss functions create different landscapes, affecting convergence speed and solution quality."
    }
]
