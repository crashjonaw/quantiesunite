TITLE = "Training Transformers and Pre-training Objectives"

SECTIONS = [
    {
        "id": "tf_supervised_training",
        "title": "Supervised Sequence-to-Sequence Training",
        "body": '<p>In supervised settings (e.g., machine translation), Transformers are trained with paired input-output sequences. The decoder generates output autoregressively with teacher forcing: at each step, the true previous output is provided as input.</p><p><strong>Loss function:</strong> Cross-entropy between predicted and true next tokens, summed across all output positions.</p><p>During inference, predictions replace ground truth, enabling free generation but risking error accumulation (exposure bias).</p>'
    },
    {
        "id": "tf_pretraining",
        "title": "Pre-training: Masked Language Modeling and Causal LM",
        "body": '<p><strong>Masked Language Modeling (BERT-style):</strong> Randomly mask 15% of input tokens and train the encoder to predict them bidirectionally. The model learns rich contextual representations.</p><p><strong>Causal Language Modeling (GPT-style):</strong> Decoder-only Transformer trained to predict the next token given previous tokens. Simple but effective for both understanding and generation.</p><p>$$L = -\\sum_{t=1}^{T} \\log p(x_t | x_1, ..., x_{t-1})$$</p><p>Pre-training on massive unlabeled corpora produces powerful representations that transfer to downstream tasks.</p>'
    },
    {
        "id": "tf_optimization",
        "title": "Optimization: Warm-up and Scheduling",
        "body": '<p>Transformers are sensitive to initialization and learning rate. Training typically uses:</p><ul><li><strong>Learning rate warm-up:</strong> Gradually increase learning rate over the first steps to stabilize training</li><li><strong>Inverse square root schedule:</strong> Decay learning rate as $$lr = \\frac{1}{\\sqrt{\\max(step, warmup\\_steps)}}$$</li><li><strong>Optimizer:</strong> Adam with default hyperparameters works well; some use SGD with momentum</li></ul><p>Batch size, gradient accumulation, and mixed precision (FP16) also critically affect training dynamics and scalability.</p>'
    },
    {
        "id": "tf_convergence",
        "title": "Scaling Laws and Training Efficiency",
        "body": '<p>Transformers exhibit predictable scaling laws: loss decreases as a power law with model size, dataset size, and compute budget. Larger models generalize better and learn faster.</p><p>Key insights for efficient training:</p><ul><li>Use lower precision (FP16) without significant accuracy loss</li><li>Parallelize across GPUs/TPUs via data parallelism or model parallelism</li><li>Pre-train on diverse data to maximize downstream transfer</li><li>Fine-tune efficiently with parameter-efficient methods (LoRA, adapters)</li></ul>'
    }
]
