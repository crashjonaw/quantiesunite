SECTIONS = [
    {"id": "lf_classification_loss", "title": "Cross-Entropy Loss for Classification", "content": '<p>$$L = -\\frac{1}{N} \\sum_{i=1}^N y_i \\log(\\hat{y}_i) + (1-y_i) \\log(1-\\hat{y}_i)$$</p>'},
    {"id": "lf_regression_loss", "title": "MSE for Regression", "content": '<p>$$L = \\frac{1}{N} \\sum_{i=1}^N (y_i - \\hat{y}_i)^2$$</p>'},
    {"id": "lf_focal_loss", "title": "Focal Loss for Imbalanced Data", "content": '<p>$$L = -\\alpha (1-p_t)^\\gamma \\log(p_t)$$</p><p>Focuses on hard negatives.</p>'},
    {"id": "lf_regularization", "title": "L1 and L2 Regularization", "content": '<p>L2: $$L_{\\text{total}} = L + \\lambda \\sum_i w_i^2$$</p><p>Penalizes large weights, prevents overfitting.</p>'},
    {"id": "lf_dropout", "title": "Dropout: Regularization via Noise", "content": '<p>During training: randomly zero 50% of activations. At test: use all activations (scaled). Prevents co-adaptation.</p>'},
    {"id": "lf_batch_norm", "title": "Batch Normalization", "content": '<p>Normalize activations within each batch. Reduces internal covariate shift, allows higher learning rates.</p>'}
]