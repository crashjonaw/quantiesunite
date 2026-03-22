SECTIONS = [
    {
        "title": "Pre-training Objectives: MLM vs CLM",
        "body": """<p><strong>Language Models</strong> learn probability distribution over text. Two main pre-training approaches:</p>

<p><strong>1. Masked Language Modeling (MLM, BERT):</strong></p>
<div class='example-box'>
<pre class='code-block'>
Objective: predict masked tokens using context

Training:
  Input: "The [MASK] sat on the mat"
  Target: predict "cat"
  Loss: cross-entropy(predicted, "cat")

Bidirectional context: model sees both left and right
  [MASK] attends to "The" and "sat" and "on" and "the" and "mat"

Pre-training: random 15% tokens replaced with [MASK]
Fine-tuning: task-specific layers on top (classification, tagging)

Advantages:
  - Bidirectional: use full context
  - Strong for understanding tasks (NER, classification, Q&A)
  - [MASK] token allows flexible completion

Limitations:
  - Pre-training/fine-tuning mismatch: [MASK] not in fine-tuning
  - Not ideal for generation (no left-to-right modeling)
</pre>
</div>

<p><strong>2. Causal Language Modeling (CLM, GPT):</strong></p>
<div class='example-box'>
<pre class='code-block'>
Objective: predict next token given past tokens

Training:
  Input: "The cat"
  Target: predict "sat"
  Loss: cross-entropy(predicted, "sat")

Unidirectional: model only sees past (causal masking)

Pre-training: same as fine-tuning (no mismatch)
Fine-tuning: in-context learning or prompt-based

Advantages:
  - Natural for language generation (auto-regressive)
  - No pre-train/fine-train mismatch
  - Enables few-shot learning (provide examples in prompt)
  - Same objective throughout

Limitations:
  - Unidirectional: doesn't use future context
  - Weaker for classification tasks (doesn't see right context)
</pre>
</div>"""
    },
    {
        "title": "Tokenization and Vocabulary",
        "body": """<p><strong>Tokenization</strong> converts text to tokens (usually subword units).</p>

<p><strong>Character-level:</strong> Too granular, hard to learn meaningful patterns.</p>
<p><strong>Word-level:</strong> Simple but huge vocabulary, rare words problematic.</p>
<p><strong>Subword (BPE, WordPiece, SentencePiece):</strong> Sweet spot.</p>

<div class='example-box'>
<pre class='code-block'>
Byte Pair Encoding (BPE):
  1. Start with character vocabulary
  2. Iteratively merge most frequent adjacent pairs
  3. Stop at desired vocab size

Example:
  Corpus: "hello", "world"
  Chars: h,e,l,o,w,r,d
  Merge l+l → ll: "helo", "world"
  Merge h+e → he: "helo" → "hlo", "world"
  ...
  Result: ["he", "ll", "o", "w", "or", "ld"]

WordPiece (BERT):
  Similar, but greedily merges to maximize likelihood
  Used in BERT, maintains subword boundaries with ##

SentencePiece:
  Directly operates on characters/bytes
  Language-agnostic, good for multilingual

Example (BERT WordPiece):
  "unbelievable" → ["un", "##believ", "##able"]
  "quickly" → ["quick", "##ly"]
</pre>
</div>

<p><strong>Vocabulary Size Trade-off:</strong></p>
<ul>
<li>Small vocab (5K): each token = multiple subwords, longer sequences, harder to learn semantics.</li>
<li>Large vocab (50K): covers more words, shorter sequences, more parameters, slower.</li>
<li>Typical: 30K-50K for English.</li>
</ul>"""
    },
    {
        "title": "Fine-tuning and Transfer Learning",
        "body": """<p><strong>Pre-training:</strong> Large unlabeled data, general language understanding.</p>
<p><strong>Fine-tuning:</strong> Small labeled data, task-specific adaptation.</p>

<div class='example-box'>
<pre class='code-block'>
Pre-training (MLM/CLM on Wikipedia, BookCorpus, etc.):
  Learn general knowledge: syntax, semantics, world knowledge

Fine-tuning (on task-specific data):
  Classification: add linear layer on [CLS] token
  Tagging: linear layer per token
  Generation: continue generation from prompt

Example (sentiment classification):
  Pre-trained BERT: 110M parameters
  Add: linear layer (768 → 2 classes)
  Fine-tune: on 10K labeled reviews, 3 epochs
  Result: 96% accuracy with minimal data

Transfer learning benefits:
  - Leverage large pre-training corpus
  - Faster convergence (weights already good)
  - Better performance with small labeled data
  - Fewer parameters to learn (only task-specific layer)
</pre>
</div>

<p><strong>Fine-tuning Strategies:</strong></p>
<ul>
<li><strong>Full fine-tuning:</strong> Update all pre-trained weights (default, best performance).</li>
<li><strong>Adapter modules:</strong> Add small trainable modules between layers, freeze rest (parameter efficient).</li>
<li><strong>LoRA:</strong> Low-rank adaptation: update low-rank factorization of weight changes (very efficient).</li>
<li><strong>Prompt tuning:</strong> Learn soft prompts (continuous embeddings) instead of discrete words (emerging).</li>
</ul>"""
    },
    {
        "title": "Scaling Laws and Emergence",
        "body": """<p><strong>Scaling Laws:</strong> Performance improves predictably with size (parameters, data, compute).</p>

<div class='example-box'>
<pre class='code-block'>
Chinchilla scaling laws (DeepMind):
  Loss ≈ α N^(-β) + ε

Where:
  N: number of parameters
  β ≈ 0.07 (small exponent)

Empirically: optimal compute allocation ≈ 20x ratio
  For N parameters: train on 20N tokens

Examples:
  GPT-2: 1.5B params → decent results
  GPT-3: 175B params → strong few-shot
  GPT-4: ~1.7T params (rumored) → reasoning, coding

Key insight: need massive data and compute to scale
  10B params → 200B tokens
  100B params → 2T tokens
</pre>
</div>

<p><strong>Emergence:</strong> Capabilities suddenly appear at scale (not continuous).</p>

<div class='example-box'>
<pre class='code-block'>
Small models: can't do:
  - Reasoning (need to solve step-by-step)
  - Few-shot learning (can't generalize from examples)
  - Code generation (syntax errors)

Large models (100B+): suddenly can:
  - Reason: "I need to think step-by-step"
  - Few-shot: "Here are examples. Now do this new one."
  - Code: mostly correct generation

Not fully understood: why does scale suddenly unlock abilities?
Theories:
  - Phase transitions in learning dynamics
  - Mixture of experts: more capacity → specialize
  - Compositionality: large models form modular structure
</p>

<p><strong>Practical Implications:</strong></p>
<ul>
<li>Bigger ≠ always better (inference cost, latency).</li>
<li>Smaller models with clever training (distillation) can be competitive.</li>
<li>Scaling saturates: performance improvements slow at very large scale.</li>
<li>Data quality matters: 1T clean tokens > 10T low-quality.</li>
</ul>"""
    },
    {
        "title": "BERT, GPT, and Modern Architectures",
        "body": """<p><strong>BERT (Encoder-only):</strong></p>
<ul>
<li>Pre-training: MLM + Next Sentence Prediction (NSP).</li>
<li>Architecture: 12/24 transformer layers.</li>
<li>Bidirectional: full context.</li>
<li>Fine-tuning: classification, tagging, Q&A, semantic similarity.</li>
<li>Limitation: can't generate text (no left-to-right bias).</li>
</ul>

<p><strong>GPT Series (Decoder-only):</strong></p>
<ul>
<li>Pre-training: CLM (next-token prediction).</li>
<li>GPT-2 (2019): 1.5B, showed few-shot ability.</li>
<li>GPT-3 (2020): 175B, in-context learning, zero-shot impressive.</li>
<li>GPT-4 (2023): multimodal, stronger reasoning.</li>
<li>Strength: generation, few-shot, reasoning (with chain-of-thought).</li>
</ul>

<p><strong>T5 (Encoder-Decoder):</strong></p>
<ul>
<li>Unified text-to-text framework: all tasks as seq2seq.</li>
<li>Pre-training: denoising objective (random span corruption).</li>
<li>Versatile: translation, summarization, Q&A, tagging.</li>
<li>Good balance between understanding (encoder) and generation (decoder).</li>
</ul>

<p><strong>Recent Models (2023+):</strong></p>
<ul>
<li><strong>LLaMA:</strong> Open-source, efficient, good scaling.</li>
<li><strong>Mistral:</strong> Sparse experts, fast inference.</li>
<li><strong>Llama 2:</strong> Improved RLHF training, instruction-tuned.</li>
<li><strong>Claude:</strong> Constitutional AI, long context (100K tokens).</li>
<li><strong>Gemini:</strong> Multimodal (text, image, audio, video).</li>
</ul>

<p><strong>RLHF (Reinforcement Learning from Human Feedback):</strong></p>
<div class='example-box'>
<pre class='code-block'>
1. Supervised fine-tuning (SFT): train on high-quality examples
2. Reward model: train model to predict human preference
3. RL training: use reward to optimize policy (language model)

Process:
  - Generate multiple responses
  - Have humans rank them
  - Train reward model: output quality score
  - Use RL (PPO) to maximize expected reward

Result: model aligns with human preferences, better instruction-following
</pre>
</div>"""
    },
    {
        "title": "Challenges and Future Directions",
        "body": """<p><strong>Current Limitations:</strong></p>

<ul>
<li><strong>Context Length:</strong> Fixed training length (2K-200K tokens). Can't handle very long documents. Solutions: retrieval, sliding windows, sparse attention.</li>
<li><strong>Knowledge Cutoff:</strong> Training data has cutoff date. No real-time updates. Solutions: retrieval augmentation, fine-tuning on new data.</li>
<li><strong>Hallucination:</strong> Confident but false outputs. Solutions: grounding to facts, better training data, RLHF.</li>
<li><strong>Reasoning:</strong> Multi-step reasoning limited. Solutions: chain-of-thought, external tools.</li>
<li><strong>Compute:</strong> Training and inference expensive. Solutions: distillation, quantization, efficient architectures.</li>
</ul>

<p><strong>Emerging Research:</strong></p>

<ul>
<li><strong>Mixture of Experts (MoE):</strong> Route inputs to specialized sub-networks, sparse computation.</li>
<li><strong>Memory Augmentation:</strong> Combine LLMs with external memory/retrieval.</li>
<li><strong>Multimodal Models:</strong> Text + image + audio + video in unified framework.</li>
<li><strong>Tool Use:</strong> LLMs interact with tools (calculators, APIs, search engines).</li>
<li><strong>Interpretability:</strong> Understanding how LLMs work, mechanistic explanations.</li>
<li><strong>Efficiency:</strong> Smaller, faster models via distillation, pruning, quantization.</li>
</ul>

<p><strong>Beyond Transformers:</strong></p>

<ul>
<li><strong>State Space Models (Mamba, S4):</strong> Linear complexity, alternative to attention.</li>
<li><strong>Hybrid Architectures:</strong> Combine transformers with RNNs/CNNs.</li>
<li><strong>Implicit Representations:</strong> Neural fields, continuous representations.</li>
</ul>

<p><strong>Ethical and Societal Concerns:</strong></p>

<ul>
<li>Bias and fairness: models reflect training data biases.</li>
<li>Misinformation: can generate convincing false content.</li>
<li>Privacy: training data may contain personal information.</li>
<li>Accessibility: compute requirements limit who can build models.</li>
<li>Alignment: ensuring models behave as intended.</li>
</ul>"""
    }
]
