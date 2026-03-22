QUIZ = [
    {
        "question": "What is the main advantage of MLM (BERT) over CLM (GPT) for classification?",
        "answer": "MLM uses bidirectional context (sees left and right), better for understanding tasks",
        "explanation": "BERT can attend to full context when predicting masked token. GPT only sees left context, weaker for classification."
    },
    {
        "question": "Why do modern models use subword tokenization?",
        "answer": "Balance between vocabulary size (not huge like word-level) and granularity (not too fine like character-level)",
        "explanation": "Subword handles rare words without character-level fragmentation, and keeps vocabulary manageable."
    },
    {
        "question": "What is the pre-train/fine-train mismatch in BERT?",
        "answer": "Pre-training uses [MASK] tokens, but fine-tuning doesn't. Model trained on something it won't see later.",
        "explanation": "BERT addresses with masking strategy (sometimes replace with random token, sometimes keep it), but mismatch remains. GPT avoids this."
    },
    {
        "question": "What does in-context learning mean?",
        "answer": "Learning from examples in the prompt without updating weights. Model uses context examples to infer task.",
        "explanation": "GPT-3: provide examples and new question in prompt, model generates answer. No fine-tuning needed."
    },
    {
        "question": "Why do larger language models show emergent capabilities?",
        "answer": "At certain scale (~100B+ params), suddenly able to do reasoning, few-shot learning, code generation. Not fully understood.",
        "explanation": "Phase transition: below threshold can't do these, above threshold suddenly can. Possibly from mixture of experts or compositionality."
    }
]
