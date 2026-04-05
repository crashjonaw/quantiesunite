TITLE = "Query, Key, Value in Self-Attention"

SECTIONS = [
    {
        "title": "Conceptual Framework: Q, K, V",
        "body": """<p><strong>Three Linear Projections per Token:</strong> Self-attention uses three learned transformations on the same input.</p>

<div class='concept-box'>
<pre class='code-block'>
Given input embedding x_i:

Query (Q):   Q_i = W_Q x_i
  Role: "What am I looking for?"
  Represents position i's question to the sequence

Key (K):    K_j = W_K x_j
  Role: "What information do I have?"
  Represents position j's content/features

Value (V):  V_j = W_V x_j
  Role: "What should I contribute?"
  Represents position j's actual information to aggregate

Separate weights: W_Q, W_K, W_V are learned independently
  Each has shape: d x d (d = embedding dimension)
  Allows queries, keys, values to be distinct representations
</pre>
</div>

<p>The key insight: <strong>not all tokens contribute equally</strong>. Q and K determine which positions matter via attention weights, and V determines what gets aggregated.</p>
    """
    },
    {
        "title": "Query-Key Matching: Computing Attention Scores",
        "body": """<p><strong>Dot Product Similarity:</strong> Queries match against keys to measure relevance.</p>

<div class='worked-example'>
<pre class='code-block'>
Similarity score between position i and j:
  score_{i,j} = Q_i · K_j

Interpretation:
  High score: position j is relevant to position i's query
  Low score: position j is not relevant

Example with d=4 dimensions:
  Q_2 = [0.5, -0.2, 1.0, 0.3]     (query from position 2)
  K_1 = [1.0, 0.1, 0.8, -0.5]     (key from position 1)
  score = 0.5*1.0 + (-0.2)*0.1 + 1.0*0.8 + 0.3*(-0.5)
        = 0.5 - 0.02 + 0.8 - 0.15
        = 1.13
</pre>
</div>

<p><strong>Computing All Scores (Matrix Form):</strong></p>

<div class='concept-box'>
<pre class='code-block'>
For a sequence of length n:
  scores = Q K^T

Shape analysis:
  Q: (n x d)
  K: (n x d)
  K^T: (d x n)
  scores: (n x n)  <- all position pairs!

scores[i, j] = Q_i · K_j  (dot product at row i, col j)
</pre>
</div>

<p>The matrix Q K^T efficiently computes all n^2 pairwise similarities in one operation.</p>
    """
    },
    {
        "title": "Value Aggregation: Building Context-Aware Output",
        "body": """<p><strong>From Scores to Weights to Output:</strong> Attention scores are normalized into weights, which aggregate values.</p>

<div class='worked-example'>
<pre class='code-block'>
Step 1: Scale scores by 1/sqrt(d)
  scaled_scores = scores / sqrt(d)
  (prevents exploding dot products when d is large)

Step 2: Convert to weights via softmax
  weights_i = softmax(scaled_scores_i)
  (row i sums to 1, all positive, interpretable as probabilities)

Step 3: Aggregate values using weights
  output_i = sum_j weights_i[j] * V_j
  (weighted combination of all values)

Example with 3 tokens:
  weights = [0.1, 0.6, 0.3]  (position i attends 60% to position 2)
  values = [v_1, v_2, v_3]   (shape: 3 x d each)
  output = 0.1*v_1 + 0.6*v_2 + 0.3*v_3
</pre>
</div>

<p><strong>Full Self-Attention Formula:</strong></p>

<div class='concept-box'>
<pre class='code-block'>
output = softmax(Q K^T / sqrt(d)) V

Order of operations:
  1. Q K^T: compute all pairwise similarities (n x n)
  2. / sqrt(d): scale for numerical stability
  3. softmax: convert to probability distributions (per row)
  4. multiply by V: aggregate values (n x d output)
</pre>
</div>

<p>Each output position is a context-aware combination of all input values, weighted by learned relevance.</p>
    """
    }
]
