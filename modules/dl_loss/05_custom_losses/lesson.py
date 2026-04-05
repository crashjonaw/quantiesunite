TITLE = "Custom Loss Functions"

SECTIONS = [
    {
        "id": "custom_design",
        "title": "Designing Custom Loss Functions",
        "body": "Custom losses align optimization with domain-specific objectives. Define a loss that quantifies what your model should optimize for. Ensure differentiability for backpropagation. Common patterns: weighted sums of base losses, asymmetric penalties for false positives vs false negatives, confidence-weighted losses for uncertainty."
    },
    {
        "id": "custom_contrastive",
        "title": "Contrastive Loss: Learning Representations",
        "body": "Contrastive loss learns similarity between samples. For paired data: L = (1 - Y) * D^2 / 2 + Y * max(margin - D, 0)^2 / 2, where D is distance and Y indicates similarity. Used in metric learning and siamese networks to learn meaningful embeddings where similar samples are close."
    },
    {
        "id": "custom_triplet",
        "title": "Triplet Loss for Metric Learning",
        "body": "Triplet loss uses three samples: anchor (a), positive (p), negative (n). Loss = max(d(a,p) - d(a,n) + margin, 0). It encourages the model to push negatives away and bring positives closer. Used in face recognition and recommendation systems to learn embeddings."
    },
    {
        "id": "custom_weighted",
        "title": "Weighted and Importance-Sampled Losses",
        "body": "Weight individual samples during training: L_weighted = (1/N) * sum(w_i * loss_i). Larger w_i for important samples (hard examples, cost-sensitive tasks). This addresses class imbalance, measurement noise, or task-specific importance. Weighted losses refine the learning signal."
    }
]
