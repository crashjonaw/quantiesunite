TITLE = "Attention Mechanism: Query, Key, Value"

SECTIONS = [
    {
        "id": "the_three_components",
        "title": "The Three Components: Query, Key, Value",
        "body": '''<p><strong>First Principles:</strong> Attention is a retrieval mechanism inspired by associative memory. To retrieve information, we need:</p>

<div class="concept-box">
    <p><strong>1. Query (Q):</strong> What are we looking for? Usually the decoder's current hidden state.</p>
    <p>Dimension: <code>[hidden_dim]</code> or <code>[batch, 1, hidden_dim]</code></p>
</div>

<div class="concept-box">
    <p><strong>2. Keys (K):</strong> What information is available? Usually the encoder's outputs.</p>
    <p>Dimension: <code>[batch, seq_len, hidden_dim]</code></p>
</div>

<div class="concept-box">
    <p><strong>3. Values (V):</strong> What do we retrieve? Often the same as keys, but can differ.</p>
    <p>Dimension: <code>[batch, seq_len, hidden_dim]</code> or <code>[batch, seq_len, value_dim]</code></p>
</div>

<p><strong>Analogy:</strong> Think of a library:</p>
<ul>
    <li><strong>Query:</strong> Your search term</li>
    <li><strong>Keys:</strong> Book titles and summaries</li>
    <li><strong>Values:</strong> The actual book contents</li>
</ul>

<p>You search (query) through titles (keys) to decide which books to read (values).</p>'''},

    {
        "id": "attention_formula",
        "title": "The Attention Formula",
        "body": '''<p><strong>Complete Attention Computation:</strong></p>

<p class="formula">$$\\text{Attention}(Q, K, V) = \\text{softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right) V$$</p>

<p>Let us break this down step by step:</p>

<p><strong>Step 1: Score Computation</strong></p>
<p class="formula">$$\\text{scores} = Q K^T$$</p>

<p>We compute the similarity between the query and each key. For a single query <code>[hidden_dim]</code> and keys <code>[seq_len, hidden_dim]</code>, this produces <code>[seq_len]</code> scores.</p>

<div class="worked-example">
    <p><strong>Example Computation:</strong></p>
    <p>Query: <code>[1, 2, 3]</code> (decoder state)</p>
    <p>Key 1: <code>[1, 1, 1]</code> (first input)</p>
    <p>Key 2: <code>[2, 2, 2]</code> (second input)</p>
    <p>Score 1: <code>1*1 + 2*1 + 3*1 = 6</code></p>
    <p>Score 2: <code>1*2 + 2*2 + 3*2 = 12</code></p>
    <p>Scores: <code>[6, 12]</code></p>
</div>

<p><strong>Step 2: Scaling</strong></p>
<p class="formula">$$\\text{scaled\\_scores} = \\frac{\\text{scores}}{\\sqrt{d_k}}$$</p>

<p>where <code>d_k</code> is the dimension of the keys (usually <code>hidden_dim</code>). This prevents scores from growing too large and causing gradient problems.</p>

<p><strong>Step 3: Normalize with Softmax</strong></p>
<p class="formula">$$\\text{weights} = \\text{softmax}(\\text{scaled\\_scores})$$</p>

<p>Softmax converts scores into probabilities that sum to 1. Each weight represents "how much to attend to this position".</p>

<div class="concept-box">
    <p><strong>Why softmax?</strong> It ensures weights are positive and sum to 1, making the context vector a proper weighted average of values. It's differentiable everywhere, enabling backpropagation.</p>
</div>

<p><strong>Step 4: Weighted Sum of Values</strong></p>
<p class="formula">$$\\text{context} = \\sum_{i=1}^{n} \\text{weights}_i \\cdot V_i$$</p>

<p>The final context vector is a weighted combination of values, where important positions get higher weight.</p>

<div class="worked-example">
    <p><strong>Continuing the Example:</strong></p>
    <p>Scores: <code>[6, 12]</code> (with scale factor ≈ 1.3 for hidden_dim=3)</p>
    <p>Scaled: <code>[4.6, 9.2]</code></p>
    <p>Softmax: <code>[0.01, 0.99]</code> (approximately)</p>
    <p>Values: V1=<code>[1,0,0]</code>, V2=<code>[0,1,0]</code></p>
    <p>Context: <code>0.01*[1,0,0] + 0.99*[0,1,0] ≈ [0.01, 0.99, 0]</code></p>
</div>'''},

    {
        "id": "batched_attention",
        "title": "Batch and Sequence Dimensions",
        "body": '''<p><strong>Real Implementation:</strong> In practice, we process multiple queries (all decoder steps) and all keys/values simultaneously.</p>

<p><strong>Dimensions:</strong></p>
<ul>
    <li><code>Q: [batch_size, query_len, hidden_dim]</code> (all decoder steps)</li>
    <li><code>K: [batch_size, key_len, hidden_dim]</code> (all encoder outputs)</li>
    <li><code>V: [batch_size, key_len, hidden_dim]</code> (all encoder outputs)</li>
</ul>

<p><strong>Matrix Multiplication:</strong></p>
<p class="formula">$$Q K^T: [\\text{batch}, \\text{query\\_len}, \\text{hidden\\_dim}] \\times [\\text{batch}, \\text{hidden\\_dim}, \\text{key\\_len}] = [\\text{batch}, \\text{query\\_len}, \\text{key\\_len}]$$</p>

<p>This produces a 2D attention matrix for each batch element: <code>query_len x key_len</code>.</p>

<p><strong>Row <code>i</code> of the attention matrix:</strong> How much each query position attends to each key position.</p>

<div class="concept-box">
    <p><strong>Key Insight:</strong> Attention is parallelizable. All queries and all keys are processed together in O(1) wall-clock time (ignoring the softmax), unlike sequential RNNs.</p>
</div>'''},

    {
        "id": "self_attention",
        "title": "Self-Attention: Query, Key, Value from Same Source",
        "body": '''<p><strong>Special Case:</strong> When Q, K, and V all come from the same input sequence, we have <strong>self-attention</strong>.</p>

<div class="worked-example">
    <p><strong>Example:</strong> In a Transformer encoder, each word attends to all words in the same sentence (including itself).</p>
    <p>Input: "I am learning attention"</p>
    <p>Position 1 ("I"):</p>
    <ul>
        <li>Query from position 1 embedding</li>
        <li>Keys from all 4 positions</li>
        <li>Values from all 4 positions</li>
    </ul>
    <p>Output: Position 1's updated representation considering all words.</p>
</div>

<p><strong>Cross-Attention:</strong> When Q comes from decoder and K, V from encoder, we have <strong>cross-attention</strong> (the original attention for machine translation).</p>

<p><strong>Why Self-Attention is Powerful:</strong></p>
<ul>
    <li>Each position can directly see all other positions</li>
    <li>Relationships are learned end-to-end</li>
    <li>Enables parallel processing of sequences</li>
    <li>Forms the foundation of modern Transformers</li>
</ul>'''
    }
]
