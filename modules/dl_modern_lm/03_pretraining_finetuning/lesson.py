TITLE = "Pre-training and Fine-tuning"

SECTIONS = [
    {
        "title": "Pre-training: Learning General Language Understanding",
        "body": """Pre-training learns general linguistic knowledge from massive unlabeled text. Models learn syntax, semantics, factual knowledge, and reasoning.

Pre-training corpora (billions of tokens):
- Wikipedia: 6GB, structured knowledge
- BookCorpus: 74GB, long-form writing
- Common Crawl: terabytes, web text (noisy)
- CodeSearchNet, GitHub: code and documentation
- Domain-specific corpora: medical texts, scientific papers, etc.

Objectives (as discussed in architectures):
- MLM (BERT): mask and predict
- CLM (GPT): next token prediction
- Denoising (T5): corrupt and reconstruct

What models learn:
After pre-training, models capture: grammatical structure (subject-verb agreement), semantic relationships (similar words grouped), factual knowledge (Paris is capital of France), world understanding (physics, biology), multilingual semantics (if trained on multiple languages).

Training details:
- Large batch size (256-1024), long training (days to months)
- Multiple epochs over corpus
- Learning rate schedules (warm-up, decay)
- Large computational cost: thousands of TPUs/GPUs

Output: general-purpose model, not specialized for any task. Weights contain compressed knowledge of training distribution."""
    },
    {
        "title": "Fine-tuning: Adapting to Specific Tasks",
        "body": """Fine-tuning adapts pre-trained model to downstream tasks using small labeled dataset. Transfer learning: reuse pre-trained weights, learn task-specific patterns.

Fine-tuning pipeline:
1. Start with pre-trained weights (e.g., BERT-base: 110M parameters)
2. Add task-specific layer (linear classifier for classification)
3. Train on labeled task data (100s-1000s of examples)
4. Update all or subset of pre-trained weights

Task-specific adaptations:
Classification: add linear layer on [CLS] token (BERT) or last hidden state (GPT)
Tagging: add linear layer per token position
Generation: continue from prompt (GPT) or use encoder context (T5)
Question-answering: predict span start/end in context

Example (sentiment classification):
Pre-trained BERT: 110M parameters, trained on 3B words
Dataset: 10K labeled reviews
Fine-tune: 3 epochs, learning rate 2e-5
Result: 96% accuracy on test set

Transfer learning benefits:
- Leverage massive pre-training corpus (model has already learned structure)
- Faster convergence: weights start good, need fewer updates
- Better generalization: don't overfit on small dataset
- Few-shot learning: can work with very small datasets (10-100 examples)
- Fewer parameters to tune: only task-specific layer is new"""
    },
    {
        "title": "Fine-tuning Strategies",
        "body": """Different strategies trade off performance vs computational cost and efficiency.

Full fine-tuning:
Update all pre-trained parameters. Default approach, best performance.
Cost: requires memory for gradients of all parameters, slow training.
When to use: large labeled dataset (10K+), need best accuracy.

Parameter-efficient fine-tuning:
Keep pre-trained weights frozen, only train small task-specific module.

Adapter modules: insert small trainable networks between transformer layers (0.3-3% parameters). Achieves 95-98% of full fine-tuning performance.

Low-Rank Adaptation (LoRA): add trainable low-rank matrices to weight updates. 0.1% additional parameters. Avoids matrix multiplication with large weights, only with low-rank matrices.
Advantage: very fast training, minimal memory overhead, can switch between tasks quickly.

Prefix tuning: learn soft prompts (continuous embeddings) prepended to input. Task parameters are continuous vectors, not discrete tokens.
Advantage: minimal parameter overhead, interpretable as learned prompts.

Prompt tuning: learn soft prompt only, freeze model entirely. Most parameter-efficient.
Limitation: requires very good prompts, may need more in-context examples.

Performance comparison:
Full fine-tuning: 100% baseline, highest cost
LoRA: 98-99% accuracy, 10x faster, 1000x less memory
Adapter: 96-98% accuracy, 5x faster, 100x less memory
Prefix: 94-97% accuracy, 1x speed (overhead), minimal parameters
Prompt: 85-95% accuracy, 1x speed, no training

Choice depends on: budget (compute, memory), dataset size, performance requirements."""
    },
    {
        "title": "In-context Learning and Few-shot Adaptation",
        "body": """In-context learning: model learns tasks from examples in prompt, without weight updates. Large language models (GPT-3+) exhibit strong in-context learning.

Mechanism:
Model uses attention over its own generated output and prompt. Attends to examples in context, infers pattern, applies to new input. No gradient updates needed.

Example (sentiment classification):
Prompt:
"Review: 'Great movie!' → Positive
Review: 'Worst film ever.' → Negative
Review: 'Pretty good, not amazing.' → ?"

GPT-3 output: "Neutral" or "Mixed"

Zero-shot: no examples, just task description
"Classify sentiment: 'Pretty good movie'" → relies on pre-training knowledge

One-shot: 1 example
"Review: 'Great!' → Positive. Review: 'Pretty good' → ?"

Few-shot: 2-10 examples
More examples → better performance (scaling effect)

Advantages:
- No fine-tuning needed (instant)
- Can change tasks by changing prompt
- Works with complex tasks (reasoning, code generation)

Limitations:
- Limited by context window (2K-200K tokens)
- Performance varies with example selection
- Not suitable for very large labeled datasets (fine-tuning still better)
- Requires large models (100B+) to work well

Trade-off: convenience (no training) vs accuracy (fine-tuning typically better with labeled data)."""
    }
]
