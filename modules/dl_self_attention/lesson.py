SECTIONS = [
    {
        "title": "Self-Attention: Attending Within a Sequence",
        "body": """<p><strong>Self-Attention</strong> lets each position attend to all other positions in the same sequence, capturing dependencies.</p>

<div class='example-box'>
<pre class='code-block'>
Cross-attention (seq2seq):
  Decoder attends to encoder
  Q from decoder, K/V from encoder

Self-attention:
  Within single sequence
  Q, K, V all from same sequence
  Position i creates query, attends to all positions j

Example: sentence "The cat sat"
  Token "sat": query formed from "sat"
  Attends to "The" (subject), "cat" (subject), "sat" (self)
  Weights show relevance: "cat" ≈ 0.6, "The" ≈ 0.2, "sat" ≈ 0.2
</pre>
</div>

<p><strong>Self-Attention Computation:</strong></p>
<div class='example-box'>
<pre class='code-block'>
Input sequence: X = [x₁, x₂, ..., xₙ]  (embeddings)

For each position i:
  Qᵢ = W_Q xᵢ    (query)
  Kⱼ = W_K xⱼ    (key, for all j)
  Vⱼ = W_V xⱼ    (value, for all j)

Attention for position i:
  sᵢⱼ = Qᵢ · Kⱼ / √d  (score: how much i should attend to j)
  αᵢⱼ = softmax(sᵢⱼ)
  oᵢ = Σⱼ αᵢⱼ Vⱼ     (output: weighted sum of values)

Matrix form (efficient):
  Q = X W_Q    (all queries)
  K = X W_K    (all keys)
  V = X W_V    (all values)
  Attention(Q,K,V) = softmax(QKᵀ / √d) V
</pre>
</div>

<p><strong>Key Advantages of Self-Attention:</strong></p>
<ul>
<li>Parallel: compute all positions simultaneously (unlike RNN sequential).</li>
<li>Long-range: all positions attend to all others (better than RNN with vanishing gradients).</li>
<li>Efficient: matrix operations on GPU.</li>
<li>Flexible: weights learned, adapt to task.</li>
</ul>"""
    },
    {
        "title": "Multi-Head Self-Attention",
        "body": """<p><strong>Multi-Head Attention:</strong> h parallel self-attention heads, outputs concatenated.</p>

<div class='example-box'>
<pre class='code-block'>
Single head: learns one type of relationship
Multiple heads: learn complementary relationships simultaneously

head₁ = attention(Q₁, K₁, V₁)
head₂ = attention(Q₂, K₂, V₂)
...
head_h = attention(Qₕ, Kₕ, Vₕ)

Output = concat(head₁, head₂, ..., head_h) @ W_O

Where:
  Qᵢ = X W_Q^(i)  (each head has own weights)
  Kᵢ = X W_K^(i)
  Vᵢ = X W_V^(i)
  W_O: projection to combine heads
</pre>
</div>

<p><strong>Transformer Block:</strong></p>
<div class='example-box'>
<pre class='code-block'>
Transformer layer:
  1. Input: X
  2. Self-attention: MultiHeadAttention(X, X, X)
  3. Add & Norm: LayerNorm(X + attention_output)
  4. Feed-forward: Linear → ReLU → Linear
  5. Add & Norm: LayerNorm(norm1 + ff_output)
  6. Output: normalized result

Key elements:
  - Residual connections (skip paths): enables deep stacking
  - Layer normalization: stabilizes training
  - Feed-forward: non-linearity (2-layer MLP per position)
</pre>
</div>

<p><strong>Why Multi-Head Works:</strong></p>
<ul>
<li>Head 1: might focus on nearby words (local syntax).</li>
<li>Head 2: might focus on distant semantics.</li>
<li>Head 3: might focus on discourse structure.</li>
<li>Combined: richer representation than single head.</li>
</ul>"""
    },
    {
        "title": "Positional Encoding: Capturing Word Order",
        "body": """<p><strong>Problem:</strong> Self-attention is permutation-invariant (word order not built-in). Need explicit position information.</p>

<p><strong>Solution: Positional Encoding</strong> adds position info to embeddings.</p>

<div class='example-box'>
<pre class='code-block'>
Sinusoidal positional encoding (original Transformer):
  PE(pos, 2i)   = sin(pos / 10000^(2i/d))
  PE(pos, 2i+1) = cos(pos / 10000^(2i/d))

Where:
  pos: position in sequence (0, 1, 2, ...)
  i: dimension index
  d: embedding dimension

Intuition:
  Different frequencies for different dimensions
  Higher dimensions: slower change (longer-range positions distinguishable)
  Lower dimensions: faster change (nearby positions distinguishable)

Example (d=4):
  pos=0: [sin(0), cos(0), sin(0), cos(0)] = [0, 1, 0, 1]
  pos=1: [sin(1), cos(1), sin(1/100), cos(1/100)] ≈ [0.84, 0.54, 0.01, 0.99]
  pos=2: different pattern...

Relative position differences encoded: Transformer can learn relative ordering.
</pre>
</div>

<p><strong>Positional Embeddings (Alternative):</strong> Learn position embeddings as parameters.</p>

<div class='example-box'>
<pre class='code-block'>
# Learned positional encoding
position_embedding = nn.Embedding(max_seq_len, embedding_dim)

# Forward pass
embeddings = token_embeddings + position_embedding(positions)

Pros: Learned for task
Cons: Fixed sequence length, need to re-train for longer sequences

Sinusoidal: generalizes to longer lengths, no retraining needed
</pre>
</div>"""
    },
    {
        "title": "Efficiency and Limitations",
        "body": """<p><strong>Computational Complexity:</strong></p>

<div class='example-box'>
<pre class='code-block'>
Self-attention: O(n²) in sequence length n
  QKᵀ: (n × d) × (d × n) = O(n² d)
  Softmax and weighted sum: O(n²)

Memory: O(n²) for attention matrices

Example:
  n = 512 (short): 262K attention scores, manageable
  n = 4096 (medium): 16M attention scores, slow
  n = 65536 (long): 4B attention scores, infeasible

RNN: O(n) sequential, can't parallelize
Attention: O(n²) but parallel-able
</pre>
</div>

<p><strong>Solutions for Long Sequences:</strong></p>

<ul>
<li><strong>Sparse Attention:</strong> Attention only to nearby/selected positions, not all.</li>
<li><strong>Linear Attention:</strong> Approximations with complexity O(n).</li>
<li><strong>Hierarchical:</strong> Chunk sequence, attention within chunks.</li>
<li><strong>Local Attention:</strong> Sliding window of fixed size.</li>
<li><strong>Learnable Routing:</strong> Dynamic selection of important positions.</li>
</ul>

<p><strong>Transformer Limitations:</strong></p>

<ul>
<li><strong>Quadratic Memory:</strong> Long sequences infeasible.</li>
<li><strong>No Inherent Inductive Bias:</strong> Unlike CNNs (locality) or RNNs (sequentiality). Needs more data.</li>
<li><strong>Positional Encoding:</strong> Sinusoidal works but not optimal. Learned embeds don't generalize.</li>
<li><strong>Context Length:</strong> Fixed during training, inference. Extrapolation hard.</li>
</ul>

<p><strong>Active Research Areas:</strong></p>
<ul>
<li>Efficient transformers (Linformers, Performers, etc.).</li>
<li>Better positional encodings (ALiBi, RoPE).</li>
<li>Long-context methods (Retrieval-augmented, chunking).</li>
</ul>"""
    },
    {
        "title": "Transformer Architecture in Practice",
        "body": """<p><strong>Encoder-Only Transformer (BERT):</strong></p>
<ul>
<li>Stack of transformer blocks.</li>
<li>Bidirectional: each token attends to all others (including future).</li>
<li>Pre-training: masked language modeling (predict masked tokens).</li>
<li>Fine-tuning: classification, tagging, etc.</li>
</ul>

<p><strong>Decoder-Only Transformer (GPT):</strong></p>
<ul>
<li>Stack of transformer blocks with causal masking.</li>
<li>Unidirectional: token attends to past only.</li>
<li>Pre-training: next-token prediction (language modeling).</li>
<li>Auto-regressive generation: one token at a time.</li>
</ul>

<p><strong>Encoder-Decoder Transformer (T5):</strong></p>
<ul>
<li>Encoder: bidirectional, processes input fully.</li>
<li>Decoder: causal, generates output token-by-token.</li>
<li>Encoder output attended by decoder (cross-attention).</li>
<li>Seq2seq tasks: translation, summarization, Q&A.</li>
</ul>

<p><strong>PyTorch nn.Transformer:</strong></p>
<div class='example-box'>
<pre class='code-block'>
import torch
import torch.nn as nn

transformer = nn.Transformer(
    d_model=512,        # embedding dimension
    nhead=8,            # num attention heads
    num_encoder_layers=6,
    num_decoder_layers=6,
    dim_feedforward=2048,
    dropout=0.1
)

# Encoder: (src_len, batch, d_model)
src = torch.randn(20, 32, 512)
# Decoder: (tgt_len, batch, d_model)
tgt = torch.randn(25, 32, 512)

output = transformer(src, tgt)  # (tgt_len, batch, d_model)
</pre>
</div>"""
    }
]
