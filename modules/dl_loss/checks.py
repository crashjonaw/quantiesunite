CHECKS = [
    {"section": "lf_classification_loss", "type": "true_false", "question": "Cross-entropy sums log probabilities", "correct": True},
    {"section": "lf_regression_loss", "type": "fill_blank", "question": "MSE loss is proportional to squared ____", "answer": "error"},
    {"section": "lf_focal_loss", "type": "true_false", "question": "Focal loss helpful for class imbalance", "correct": True},
    {"section": "lf_regularization", "type": "multiple_choice", "question": "L2 regularization term is:", "options": ["Sum w_i", "Sum w_i^2", "Sum |w_i|", "Max w_i"], "correct": 1},
    {"section": "lf_dropout", "type": "fill_blank", "question": "Dropout zeros __% of activations", "answer": "50"},
    {"section": "lf_batch_norm", "type": "true_false", "question": "Batch norm computed per sample", "correct": False}
]