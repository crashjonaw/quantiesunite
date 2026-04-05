MINDMAP = {
    "concepts": [
        {"title": "Role of the Loss Function", "points": [
            "Quantifies how far predictions are from ground truth",
            "Gradients of the loss drive weight updates during backpropagation",
            "Different tasks need different losses: regression vs classification",
        ]},
        {"title": "Regression Losses", "points": [
            "MSE (Mean Squared Error): \\(\\frac{1}{n}\\sum(y_i - \\hat{y}_i)^2\\) — penalises large errors heavily",
            "MAE (Mean Absolute Error): \\(\\frac{1}{n}\\sum|y_i - \\hat{y}_i|\\) — robust to outliers",
            "Huber loss: quadratic for small errors, linear for large — best of both",
        ]},
        {"title": "Classification Losses", "points": [
            "Binary Cross-Entropy: \\(-[y\\log\\hat{y} + (1-y)\\log(1-\\hat{y})]\\)",
            "Categorical Cross-Entropy: \\(-\\sum_c y_c \\log \\hat{y}_c\\) for multi-class",
            "Cross-entropy + softmax is numerically stable when combined (log-softmax trick)",
        ]},
        {"title": "Regularisation", "points": [
            "Prevents overfitting by penalising model complexity",
            "L2 (Ridge / weight decay): adds \\(\\lambda \\sum w_i^2\\) to loss — shrinks weights",
            "L1 (Lasso): adds \\(\\lambda \\sum |w_i|\\) to loss — encourages sparsity",
            "Dropout: randomly zero out neurons during training (typically p=0.1 to 0.5)",
        ]},
        {"title": "Other Techniques", "points": [
            "Early stopping: halt training when validation loss stops improving",
            "Batch normalisation: normalise layer inputs — acts as mild regulariser",
            "Data augmentation: expand training set to reduce overfitting",
        ]},
    ],
    "formulas": [
        {"label": "MSE", "expr": "\\(L = \\frac{1}{n}\\sum_{i=1}^{n}(y_i - \\hat{y}_i)^2\\)"},
        {"label": "Binary Cross-Entropy", "expr": "\\(L = -\\frac{1}{n}\\sum_{i=1}^{n}[y_i \\log \\hat{y}_i + (1-y_i)\\log(1-\\hat{y}_i)]\\)"},
        {"label": "Categorical Cross-Entropy", "expr": "\\(L = -\\sum_{c=1}^{C} y_c \\log \\hat{y}_c\\)"},
        {"label": "L2 Regularisation", "expr": "\\(L_{\\text{total}} = L_{\\text{data}} + \\lambda \\sum_i w_i^2\\)"},
        {"label": "L1 Regularisation", "expr": "\\(L_{\\text{total}} = L_{\\text{data}} + \\lambda \\sum_i |w_i|\\)"},
    ],
    "tips": [
        "Use cross-entropy for classification and MSE for regression as default choices.",
        "Combine L2 regularisation with dropout for strong generalisation in deep networks.",
        "Monitor validation loss alongside training loss to detect overfitting early.",
        "Label smoothing (softening one-hot targets) can improve generalisation in classification.",
    ],
}
