TITLE = "Cross-Entropy and Classification Losses"

SECTIONS = [
    {
        "id": "clf_crossentropy",
        "title": "Cross-Entropy Loss Fundamentals",
        "body": "Cross-entropy measures the difference between true and predicted probability distributions. For binary classification: L = -(1/N) * sum(y_i * log(y_hat_i) + (1 - y_i) * log(1 - y_hat_i)). It penalizes confident wrong predictions heavily, making it effective for classification."
    },
    {
        "id": "clf_multiclass",
        "title": "Categorical Cross-Entropy (Multiclass)",
        "body": "For K-class problems, categorical cross-entropy is: L = -(1/N) * sum(sum_k(y_ik * log(y_hat_ik))). Each sample has one true label (one-hot encoded). The loss sums negative log-probabilities across all classes. Use softmax activation with this loss for multiclass classification."
    },
    {
        "id": "clf_focal",
        "title": "Focal Loss for Class Imbalance",
        "body": "Focal loss addresses class imbalance: L = -(1/N) * sum(alpha * (1 - p_t)^gamma * log(p_t)). The focusing parameter gamma downweights easy examples, directing learning toward hard negatives. This is crucial when classes are heavily imbalanced (e.g., 99% negative, 1% positive)."
    },
    {
        "id": "clf_bce_vs_ce",
        "title": "Binary Cross-Entropy vs Categorical Cross-Entropy",
        "body": "Use binary cross-entropy for binary classification (1 neuron output, sigmoid activation). Use categorical cross-entropy for multiclass (K neurons, softmax activation). Both measure probability divergence. The choice depends on output architecture and problem structure."
    }
]
