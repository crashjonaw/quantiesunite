TITLE = "Regularization (L1, L2)"

SECTIONS = [
    {
        "id": "reg_l2",
        "title": "L2 Regularization (Ridge)",
        "body": "L2 regularization adds a penalty term: L_total = L_data + lambda * sum(w_i^2). It penalizes large weights, encouraging smaller, more distributed weights. This improves generalization by reducing model complexity. Larger lambda increases regularization strength. L2 is differentiable and widely used."
    },
    {
        "id": "reg_l1",
        "title": "L1 Regularization (Lasso)",
        "body": "L1 regularization uses absolute values: L_total = L_data + lambda * sum(|w_i|). It encourages sparsity by pushing small weights to exactly zero, performing feature selection automatically. L1 is robust but non-differentiable at zero. Use L1 when interpretability and sparsity matter."
    },
    {
        "id": "reg_elasticnet",
        "title": "ElasticNet: Combining L1 and L2",
        "body": "ElasticNet blends both penalties: L_total = L_data + lambda1 * sum(|w_i|) + lambda2 * sum(w_i^2). This combines the sparsity of L1 with the smoothness of L2. Tuning two hyperparameters (lambda1, lambda2) provides flexibility for different problems."
    },
    {
        "id": "reg_understanding",
        "title": "Why Regularization Works",
        "body": "Regularization constrains the hypothesis space, preventing overfitting. Smaller weights mean simpler functions with less capacity to memorize noise. During training, the model balances fitting data (low loss) with staying simple (low weight magnitude). This trade-off improves test-time generalization."
    }
]
