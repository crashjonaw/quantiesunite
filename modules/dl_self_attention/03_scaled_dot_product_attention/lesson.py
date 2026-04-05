TITLE = "Scaled Dot-Product Attention"

SECTIONS = [
    {
        "title": "Why Scaling Matters",
        "body": """<p><strong>The Problem: Large Dot Products Collapse Softmax</strong></p>

<p>When dimension d is large, dot products Q K^T become very large in magnitude. This causes softmax to become very "peaked" (nearly one-hot), reducing gradient flow during backprop.</p>

<div class='warning-box'>
<pre class='code-block'>
Without scaling (d=512):
  Q · K typically in range [-500, 500]
  After softmax: values near 0 or 1 (very sharp)
  Gradient of softmax: exp(-large_x) ≈ 0 (vanishing)
  Training unstable, gradients don't flow

With scaling by 1/sqrt(d):
  Q · K / sqrt(512) ≈ Q · K / 22.6
  Range: [-22, 22]  (much smaller)
  After softmax: smoother distribution
  Better gradient flow during backprop
</pre>
</div>

<p><strong>Intuition:</strong> As d grows, dot products grow. Scaling brings them back to a reasonable range for softmax.</p>
    """
    },
    {
        "title": "The Complete Scaled Dot-Product Attention Formula",
        "body": """<p><strong>Official Definition:</strong></p>

<div class='concept-box'>
<pre class='code-block'>
Attention(Q, K, V) = softmax(Q K^T / sqrt(d_k)) V

Where:
  Q: query matrix (shape: batch x n_q x d_k)
  K: key matrix (shape: batch x n_k x d_k)
  V: value matrix (shape: batch x n_k x d_v)
  d_k: dimension of keys (and queries)
  d_v: dimension of values
  sqrt(d_k): scaling factor
  Output: (batch x n_q x d_v)

For self-attention:
  n_q = n_k = sequence_length
  d_k = d_v = d (usually)
</pre>
</div>

<p><strong>Multi-Head Extension:</strong> In practice, multiple heads compute attention in parallel with different projections, then concatenate.</p>

<div class='worked-example'>
<pre class='code-block'>
Single head: d_k = D / num_heads  (reduce dimension per head)

Example with D=512, 8 heads:
  d_k = 512 / 8 = 64 per head
  Head 1: Attention_1 = softmax(Q_1 K_1^T / sqrt(64)) V_1
  Head 2: Attention_2 = softmax(Q_2 K_2^T / sqrt(64)) V_2
  ...
  Head 8: Attention_8 = softmax(Q_8 K_8^T / sqrt(64)) V_8

  output = concat(Attention_1, ..., Attention_8) W_o
  (W_o projects concatenated output back to D dimensions)
</pre>
</div>
    """
    },
    {
        "title": "Computational Efficiency",
        "body": """<p><strong>Why This Design is Efficient:</strong></p>

<div class='success-box'>
<pre class='code-block'>
Advantages of scaled dot-product attention:
  1. Parallelizable: all attention scores computed at once (GPU friendly)
  2. No recurrence: unlike RNNs, no sequential dependency
  3. Matrix operations: leverages optimized BLAS/CUDA kernels
  4. Memory-efficient: fewer intermediate activations than some RNN approaches

Complexity analysis for self-attention:
  Time: O(n^2 d) where n = sequence length, d = embedding dim
  Space: O(n^2) for attention matrix

  Comparison:
  RNN: O(n d) time but sequential, can't parallelize
  CNN: O(n d) but limited context window
  Attention: O(n^2 d) but massively parallel
</pre>
</div>

<p><strong>Modern Implementation Tricks:</strong></p>

<ul>
<li><strong>Flash Attention:</strong> Reorder computation to reduce memory access.</li>
<li><strong>Sparse Attention:</strong> Only attend to nearby or selected positions.</li>
<li><strong>Linear Attention:</strong> Approximate Q K^T V without full O(n^2) matrix.</li>
</ul>
    """
    },
    {
        "title": "Practical Example",
        "body": """<p><strong>Step-By-Step Calculation:</strong></p>

<div class='worked-example'>
<pre class='code-block'>
Small example: 2 tokens, embedding dimension 4

Input: X = [[1, 2, 1, 0],     (token 1)
            [3, 0, 2, 1]]     (token 2)

Learned weights (example values):
W_Q = [[1, 0, 0, 0],          (project to query)
       [0, 1, 0, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 1]]
(same for W_K, W_V for simplicity)

Q = X W_Q = X = [[1, 2, 1, 0],
                 [3, 0, 2, 1]]
K = X W_K = X
V = X W_V = X

Compute Q K^T:
  [1, 2, 1, 0] · [1, 3]^T
  = [[1*1 + 2*0 + 1*2 + 0*1, 1*3 + 2*0 + 1*2 + 0*1],
     [3*1 + 0*0 + 2*2 + 1*1, 3*3 + 0*0 + 2*2 + 1*1]]
  = [[3, 5],
     [8, 14]]

Scale by sqrt(4) = 2:
  scores = [[1.5, 2.5],
            [4.0, 7.0]]

Softmax (per row):
  row 1: exp([1.5, 2.5]) = [4.48, 12.18]
         sum = 16.66
         weights = [0.27, 0.73]
  row 2: exp([4.0, 7.0]) = [54.6, 1097]
         sum = 1151.6
         weights = [0.05, 0.95]

Multiply by V: aggregate token embeddings
  output_1 = 0.27 * [1,2,1,0] + 0.73 * [3,0,2,1]
           = [2.54, 0.54, 1.73, 0.73]
  output_2 = 0.05 * [1,2,1,0] + 0.95 * [3,0,2,1]
           = [2.90, 0.10, 1.95, 0.95]
</pre>
</div>

<p>This example shows how each token's context is updated based on attention weights.</p>
    """
    }
]
