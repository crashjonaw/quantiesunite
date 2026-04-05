TITLE = "Masked Self-Attention"

SECTIONS = [
    {
        "title": "Why Masking is Needed",
        "body": """<p><strong>Two Scenarios Require Different Masking Strategies:</strong></p>

<div class='concept-box'>
<pre class='code-block'>
Scenario 1: Encoder (Bidirectional, like BERT)
  "The cat sat"
  Position 0 (the): attends to [the, cat, sat]  (all positions)
  Position 1 (cat): attends to [the, cat, sat]  (all positions)
  Position 2 (sat): attends to [the, cat, sat]  (all positions)
  No masking needed - can see full context both directions

Scenario 2: Decoder (Autoregressive, like GPT)
  "The cat sat"
  Position 0 (the): can only attend to [the]  (itself)
  Position 1 (cat): can only attend to [the, cat]  (past + self)
  Position 2 (sat): can only attend to [the, cat, sat]  (all past + self)
  CANNOT attend to future - information not available during generation
  Need causal masking!
</pre>
</div>

<p>In autoregressive generation, position t doesn't "know" what comes after it yet. Masking enforces causality.</p>
    """
    },
    {
        "title": "Causal Masking in Detail",
        "body": """<p><strong>Implementation: Set Future Scores to Negative Infinity</strong></p>

<div class='worked-example'>
<pre class='code-block'>
Before masking:
  scores = Q K^T = [[2, 1, 3],
                    [4, 2, 1],
                    [1, 5, 2]]

Causal mask (lower triangular):
  mask = [[1, 0, 0],
          [1, 1, 0],
          [1, 1, 1]]
  1 = keep (attend), 0 = mask (don't attend)

Apply mask (set masked positions to -infinity):
  masked_scores = [[ 2, -inf, -inf],
                   [ 4,  2, -inf],
                   [ 1,  5,   2]]

Softmax (per row):
  row 0: exp([2, -inf, -inf]) = [7.4, 0, 0]
         softmax: [1, 0, 0]  (attends only to self)
  row 1: exp([4, 2, -inf]) = [54.6, 7.4, 0]
         softmax: [0.88, 0.12, 0]  (attends to past)
  row 2: exp([1, 5, 2]) = [2.7, 148.4, 7.4]
         softmax: [0.01, 0.96, 0.05]  (attends to all past + self)

Key: -inf becomes 0 after softmax (no contribution)
</pre>
</div>

<p><strong>Formula:</strong></p>

<div class='concept-box'>
<pre class='code-block'>
Masked attention:
  masked_scores = scores + mask * (-infinity)
  Attention = softmax(masked_scores / sqrt(d)) V

Mask construction (lower triangular):
  mask[i, j] = 0 if j > i (future position)
             = 1 if j <= i (past or current)

Effect:
  softmax(-inf) = 0
  Attention to future positions: 0 weight
  Only past positions contribute to output
</pre>
</div>
    """
    },
    {
        "title": "Padding Masking",
        "body": """<p><strong>Additional Masking for Sequences of Different Lengths:</strong></p>

<p>In batched processing, sequences are padded to same length. We don't want attention to padding tokens.</p>

<div class='worked-example'>
<pre class='code-block'>
Batch with variable lengths:
  Sequence 1: "The cat" (length 2)
  Sequence 2: "A dog runs fast" (length 4)

Padded:
  Sequence 1: [the, cat, pad, pad]
  Sequence 2: [a, dog, runs, fast]

Without masking:
  "cat" might attend to padding (irrelevant, should be 0)
  Wastes attention and confuses model

Padding mask:
  Sequence 1: [1, 1, 0, 0]  (1=real, 0=padding)
  Sequence 2: [1, 1, 1, 1]

Apply masking:
  Set attention scores for padding positions to -infinity
  After softmax, padding positions get 0 weight
  Real tokens only attend to real tokens
</pre>
</div>

<p><strong>Combined Masking:</strong> For decoder-only (autoregressive), combine both causal + padding masks.</p>

<div class='concept-box'>
<pre class='code-block'>
Combined mask = causal_mask AND padding_mask
  (both conditions must be satisfied to attend)

Implementation:
  mask = padding_mask[:, None, :] & causal_mask[None, :, :]
  (broadcasting: batch dimension compatible)
  masked_scores = scores + (1 - mask.float()) * (-infinity)
</pre>
</div>
    """
    },
    {
        "title": "Practical Example: Decoder During Training vs Generation",
        "body": """<p><strong>Training Phase (All Positions Available):</strong></p>

<div class='worked-example'>
<pre class='code-block'>
Training sequence: "The cat sat"

Self-attention with causal mask:
  Position 0 (the):
    Can attend to: [the]
    weights: [1.0, 0, 0]
    output: context from token 0 only

  Position 1 (cat):
    Can attend to: [the, cat]
    weights: [0.3, 0.7, 0]
    output: blend of token 0 and 1

  Position 2 (sat):
    Can attend to: [the, cat, sat]
    weights: [0.1, 0.6, 0.3]
    output: blend of all three tokens

Teacher forcing: all positions computed in parallel!
Loss computed on all positions simultaneously
</pre>
</div>

<p><strong>Generation Phase (Auto-regressive, One Token at a Time):</strong></p>

<div class='worked-example'>
<pre class='code-block'>
Generate "The"
  Input: [the]
  Attention: position 0 attends to [the]
  Output: representation of "the"
  Predict next token

Generate "cat"
  Input: [the, cat]
  Attention: position 1 attends to [the, cat]
  Output: context-aware representation of "cat"
  Predict next token

Generate "sat"
  Input: [the, cat, sat]
  Attention: position 2 attends to [the, cat, sat]
  Output: context-aware representation of "sat"
  Predict next token

Note: Masking enforces causality (same as training)
But generation is slower (sequential, not parallel)
</pre>
</div>

<p><strong>Key Insight:</strong> Causal masking during training ensures the decoder learns the same conditional probabilities it will use during generation.</p>
    """
    }
]
