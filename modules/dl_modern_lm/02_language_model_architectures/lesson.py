TITLE = "Language Model Architectures: MLM vs CLM"

SECTIONS = [
    {
        "title": "Masked Language Modeling (MLM)",
        "body": """Masked Language Modeling is a bidirectional pre-training objective. Randomly mask (replace) tokens in input and predict them from context.

How it works:
1. Take input text: "The cat sat on the mat"
2. Randomly mask 15% of tokens: "The [MASK] sat on the [MASK]"
3. Model predicts masked tokens using full context (left AND right)
4. Loss: cross-entropy between predicted distribution and actual token

Bidirectional context:
The [MASK] token attends to both "The" (left) and "sat" (right). Model sees complete sentence context. Enables attending to all surrounding words.

Masking strategy details:
- 80% of time: replace with [MASK] token
- 10% of time: replace with random token (forces robustness)
- 10% of time: keep original (helps grounding)
This prevents model from just looking for [MASK] indicator.

Advantages:
- Bidirectional: uses full context, powerful for understanding
- Strong for classification, tagging, question-answering tasks
- Flexible: [MASK] token allows arbitrary token prediction

Limitations:
- Pre-training/fine-tuning mismatch: [MASK] appears during pre-training but not during fine-tuning. Model trained on something it won't see.
- Not ideal for generation: no left-to-right bias, model can't naturally generate sequences word-by-word
- Generation requires different inference (iterative masking or decoder module)"""
    },
    {
        "title": "Causal Language Modeling (CLM)",
        "body": """Causal Language Modeling predicts next token from past tokens only. Natural left-to-right autoregressive objective.

How it works:
1. Take input text: "The cat sat on"
2. Model predicts next token: "the"
3. Loss: cross-entropy(predicted_logits, "the")
4. At inference: auto-regressively generate one token, append, repeat

Causal masking:
Attention is masked so position i only attends to positions 0...i-1. Model cannot see future tokens. Forces left-to-right processing.

Key insight: pre-training objective matches inference perfectly. Same task during pre-training and fine-tuning/inference.

Advantages:
- Natural for generation: auto-regressive generation matches training
- No pre-train/fine-train mismatch: same objective throughout
- Enables in-context learning: provide examples in prompt, model infers task
- Few-shot learning: "Here are examples... Now do this" works naturally

Limitations:
- Unidirectional: cannot use future context. Weaker for tasks needing bidirectional understanding
- Classification tasks: model only sees left context, misses right context cues
- Question answering: may not see full question before generating answer

Trade-off: CLM sacrifices understanding for natural generation."""
    },
    {
        "title": "Encoder-Decoder Architectures",
        "body": """Encoder-Decoder combines bidirectional encoding with autoregressive decoding. Separate modules: encoder understands input, decoder generates output.

Structure:
Encoder: processes input (left and right context), produces contextual representations
Cross-attention: decoder attends to encoder outputs
Decoder: generates output token-by-token, attends to encoder context and its own past

Example (T5): "translate English to French: hello world"
Encoder: encodes input with bidirectional attention
Decoder: generates "bonjour le monde" autoregressively, attending to encoder outputs

Advantages:
- Best of both worlds: encoder is bidirectional (understands), decoder is autoregressive (generates)
- Versatile: can handle any seq2seq task (translation, summarization, Q&A, tagging)
- Strong for structured outputs: decoder can attend to encoder for grounding

Pre-training objectives:
- T5: denoising objective. Corrupt input (drop random spans), learn to reconstruct
- Unified text-to-text: all tasks formulated as seq2seq
- Example: "Summarize: [article] → [summary]", "Translate EN→FR: [en] → [fr]"

Limitations:
- More complex: two separate models to train
- Higher inference cost: encode once (cheap), decode many times (expensive)
- Less natural for pure generation (needs input to encode)

T5 is prominent example: unified approach, strong performance across tasks."""
    },
    {
        "title": "Bidirectional vs Unidirectional Trade-off",
        "body": """Architecture choice determines model capabilities and limitations.

Bidirectional (Encoder-only like BERT):
Sees full context. Powerful for understanding, classification, tagging.
Cannot generate autoregressively (no causal mask).
Tasks: sentiment classification, NER, semantic similarity, question-answering (given context).
Inference: process entire input once, extract features.

Unidirectional (Decoder-only like GPT):
Sees only past. Natural for generation, few-shot learning, in-context reasoning.
Weaker for understanding (can't see future context).
Tasks: language generation, instruction-following, few-shot learning, reasoning.
Inference: generate token-by-token, auto-regressively.

Encoder-Decoder (like T5):
Encoder is bidirectional, decoder is unidirectional. Combines strengths.
Good for all tasks, but more complex.
Inference: encode input once, decode output many times.

Practical choices:
- Need to classify/understand: use encoder-only (BERT)
- Need to generate/reason: use decoder-only (GPT)
- Need both bidirectional understanding and generation: use encoder-decoder (T5)
- Don't need generation: encoder-only is most efficient (single forward pass)"""
    }
]
