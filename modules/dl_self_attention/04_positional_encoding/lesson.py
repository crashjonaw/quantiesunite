TITLE = "Positional Encoding"

SECTIONS = [
    {
        "title": "The Problem: Self-Attention is Permutation-Invariant",
        "body": """<p><strong>Self-attention treats all positions symmetrically.</strong> Without explicit position information, the model doesn't inherently understand word order.</p>

<div class='warning-box'>
<pre class='code-block'>
Problem:
  Input: "The cat sat"  (embeddings: [e_the, e_cat, e_sat])
  Input: "Sat cat the"  (embeddings: [e_sat, e_cat, e_the])

  Self-attention depends only on values and dot products
  Permuting positions changes Q, K, V order but not the mechanism
  Model could learn wrong structure (position information missing)

Why it matters:
  Position 0 might mean "article" (start)
  Position 1 might mean "subject" (noun)
  Position 2 might mean "verb" (action)

  Without knowing position, model can't use these patterns
</pre>
</div>

<p><strong>Solution:</strong> Add position information to embeddings explicitly.</p>
    """
    },
    {
        "title": "Sinusoidal Positional Encoding",
        "body": """<p><strong>Original Transformer Approach:</strong> Use sine and cosine functions of different frequencies.</p>

<div class='concept-box'>
<pre class='code-block'>
Formula:
  PE(pos, 2i) = sin(pos / 10000^(2i / d))
  PE(pos, 2i+1) = cos(pos / 10000^(2i / d))

Where:
  pos: position in sequence (0, 1, 2, ..., n-1)
  i: dimension index (0, 1, 2, ..., d/2 - 1)
  d: total embedding dimension
  2i, 2i+1: pairs of sine/cosine for each dimension

Pattern:
  Low dimensions (i small): high frequency, changes fast
  High dimensions (i large): low frequency, changes slow
  Creates position-dependent signal
</pre>
</div>

<p><strong>Intuition with Example (d=4):</strong></p>

<div class='worked-example'>
<pre class='code-block'>
d = 4, frequencies: 1, 1/100

pos=0:
  PE[0] = sin(0 / 1) = 0
  PE[1] = cos(0 / 1) = 1
  PE[2] = sin(0 / 100) = 0
  PE[3] = cos(0 / 100) = 1
  PE(0) = [0, 1, 0, 1]

pos=1:
  PE[0] = sin(1 / 1) ≈ 0.841
  PE[1] = cos(1 / 1) ≈ 0.540
  PE[2] = sin(1 / 100) ≈ 0.010
  PE[3] = cos(1 / 100) ≈ 0.9999
  PE(1) = [0.841, 0.540, 0.010, 0.9999]

pos=2:
  PE[0] = sin(2 / 1) ≈ 0.909
  PE[1] = cos(2 / 1) ≈ -0.416
  PE[2] = sin(2 / 100) ≈ 0.020
  PE[3] = cos(2 / 100) ≈ 0.9998
  PE(2) = [0.909, -0.416, 0.020, 0.9998]

Each position has unique encoding!
Nearby positions: similar (dimension 2,3 change slowly)
Distant positions: more different overall
</pre>
</div>

<p><strong>Key Property:</strong> Sinusoidal encoding generalizes to sequences longer than training. No retraining needed for longer inputs.</p>
    """
    },
    {
        "title": "Adding Position to Embeddings",
        "body": """<p><strong>In Practice:</strong> Positional encoding is added element-wise to token embeddings.</p>

<div class='worked-example'>
<pre class='code-block'>
Token embedding: e_i (shape: d)
Positional encoding: PE(i) (shape: d)
Input to attention: x_i = e_i + PE(i)

Full sequence:
  X = [e_1 + PE(1), e_2 + PE(2), ..., e_n + PE(n)]

Flow:
  1. Tokenize input
  2. Look up token embeddings
  3. Add positional encodings (broadcast addition)
  4. Pass to transformer blocks
  5. Self-attention now has position awareness
</pre>
</div>

<p><strong>Learned Positional Embeddings (Alternative):</strong></p>

<div class='worked-example'>
<pre class='code-block'>
Instead of fixed sinusoidal, learn position embeddings:

pos_embed = nn.Embedding(max_seq_len, d)

In forward pass:
  positions = torch.arange(seq_len)
  pos_encodings = pos_embed(positions)  (shape: seq_len x d)
  x = token_embeddings + pos_encodings

Pros:
  - Task-specific learning
  - Can be fine-tuned for domain

Cons:
  - Fixed sequence length at training
  - Doesn't generalize to longer sequences
  - Need to retrain for different max lengths
</pre>
</div>

<p><strong>Which is Better?</strong> Sinusoidal is more general; learned works well in practice when sequence length is fixed and data is abundant.</p>
    """
    },
    {
        "title": "Relative Position Encoding",
        "body": """<p><strong>Modern Approaches:</strong> Explicit relative position representations.</p>

<div class='concept-box'>
<pre class='code-block'>
Relative Position Encoding (ALiBi, RoPE):
  Encode distance between positions, not absolute position
  Modify attention scores directly based on offset

Example (ALiBi - Attention with Linear Biases):
  score_{i,j} = Q_i · K_j / sqrt(d) + penalty * |i - j|

  penalty: learned weight for each head
  encourages lower weights for distant positions
  still allows long-range when important

Advantages:
  - Relative distance is more meaningful than absolute position
  - Handles variable sequence lengths naturally
  - Better inductive bias for language
</pre>
</div>

<p><strong>RoPE (Rotary Position Embeddings):</strong> Recent method that rotates Q and K vectors based on position, encoding relative positions naturally.</p>
    """
    }
]
