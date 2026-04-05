TITLE = "From Attention to Self-Attention"

SECTIONS = [
    {
        "title": "Cross-Attention: The Foundation",
        "body": """<p><strong>Attention</strong> allows a decoder to focus on relevant parts of an encoder output. In sequence-to-sequence models:</p>

<div class='concept-box'>
<pre class='code-block'>
Cross-attention (seq2seq):
  Decoder attends to encoder output
  Q (query): from decoder hidden state
  K (key): from encoder output
  V (value): from encoder output

Intuition:
  Decoder "asks" (query): what should I generate next?
  Encoder "answers" (key/value): here are my outputs
  Decoder selects relevant parts via attention weights
</pre>
</div>

<p><strong>Attention Mechanism Formula:</strong></p>

<div class='worked-example'>
<pre class='code-block'>
Attention(Q, K, V) = softmax(Q K^T / sqrt(d)) V

Where:
  Q: query matrix (batch, tgt_len, d)
  K: key matrix (batch, src_len, d)
  V: value matrix (batch, src_len, d)
  d: dimension of each head
  softmax: normalization (row-wise)
</pre>
</div>

<p>For each query position, we compute a weighted sum of all values, where weights come from query-key similarities.</p>
    """
    },
    {
        "title": "Self-Attention: Attending Within a Sequence",
        "body": """<p><strong>Self-Attention</strong> is attention where Q, K, and V all come from the <em>same sequence</em>. Each position attends to all other positions in the same sequence.</p>

<div class='concept-box'>
<pre class='code-block'>
Self-attention:
  All of Q, K, V from same input sequence X
  Each position i "looks at" all positions j
  Learns which other positions are relevant

Example: sentence "The cat sat"
  Token "sat" creates query from its embedding
  Computes attention over all 3 words
  Might learn: "cat" is relevant (subject) ≈ 0.6
               "sat" is self ≈ 0.2
               "The" is article ≈ 0.2
</pre>
</div>

<p><strong>Why Self-Attention Instead of Cross-Attention?</strong></p>

<ul>
<li><strong>No Encoder:</strong> Single sequence processed by itself, no separate encoder step.</li>
<li><strong>Bidirectional Context:</strong> Each position sees both past and future (in BERT-like models).</li>
<li><strong>Parallel Processing:</strong> Unlike RNNs, all positions computed simultaneously.</li>
<li><strong>Long-Range Dependencies:</strong> Every position can directly attend to every other position.</li>
</ul>
    """
    },
    {
        "title": "Self-Attention Computation",
        "body": """<p><strong>Step-by-Step Self-Attention:</strong></p>

<div class='worked-example'>
<pre class='code-block'>
Input: X = [x_1, x_2, ..., x_n]  (word embeddings, shape: n x d)

For each position i:
  Query:  Q_i = W_Q x_i          (learnable projection, shape: d)
  Key:    K_j = W_K x_j          (for all j, shape: n x d)
  Value:  V_j = W_V x_j          (for all j, shape: n x d)

Attention at position i:
  score_{i,j} = Q_i · K_j / sqrt(d)  (compatibility, shape: n)
  weights_i = softmax(scores_i)       (distribution, sum to 1)
  output_i = sum_j weights_i[j] V_j   (weighted combination)
</pre>
</div>

<p><strong>Matrix Form (Efficient Implementation):</strong></p>

<div class='concept-box'>
<pre class='code-block'>
Q = X W_Q        (all queries at once, shape: n x d)
K = X W_K        (all keys, shape: n x d)
V = X W_V        (all values, shape: n x d)

Attention(Q, K, V) = softmax(Q K^T / sqrt(d)) V

Components:
  Q K^T: n x n matrix (all position pairs)
  softmax: normalize each row (sum to 1)
  multiply by V: combine values
  output shape: n x d
</pre>
</div>

<p>This matrix form allows batched GPU computation, much faster than loop-based version.</p>
    """
    }
]
