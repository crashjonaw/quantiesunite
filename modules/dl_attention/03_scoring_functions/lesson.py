TITLE = "Scoring Functions: Computing Attention Scores"

SECTIONS = [
    {
        "id": "alignment_scores",
        "title": "Alignment Scores: Matching Queries to Keys",
        "body": '''<p><strong>First Principles:</strong> Attention scores measure <em>how well</em> a query matches a key. Different scoring functions encode different notions of "matching".</p>

<div class="concept-box">
    <p><strong>Why Multiple Functions?</strong> The choice of scoring function affects:</p>
    <ul>
        <li>What patterns the model can learn</li>
        <li>Computational efficiency</li>
        <li>Convergence speed during training</li>
        <li>Performance on downstream tasks</li>
    </ul>
</div>

<p><strong>Formal Definition:</strong> A scoring function takes a query <code>q</code> and key <code>k</code> and returns a scalar:</p>
<p class="formula">$$\\text{score}(q, k) \\in \\mathbb{R}$$</p>

<p>Higher scores indicate stronger alignment. The softmax normalizes scores into attention weights.</p>'''},

    {
        "id": "dot_product_scoring",
        "title": "Dot-Product (Multiplicative) Scoring",
        "body": '''<p><strong>Simplest Scoring Function:</strong> Direct dot product of query and key.</p>

<p class="formula">$$\\text{score}(q, k) = q \\cdot k = \\sum_{i=1}^{d} q_i k_i$$</p>

<p><strong>Properties:</strong></p>
<ul>
    <li><strong>Computational Cost:</strong> O(d) where d is hidden dimension. Very efficient.</li>
    <li><strong>Gradient Flow:</strong> Straightforward backpropagation.</li>
    <li><strong>Interpretability:</strong> High score when q and k are aligned in the same direction.</li>
</ul>

<div class="worked-example">
    <p><strong>Example:</strong></p>
    <p>Query: <code>[1, 0, 0]</code></p>
    <p>Key 1: <code>[2, 0, 0]</code> → Score = 1*2 + 0*0 + 0*0 = 2</p>
    <p>Key 2: <code>[1, 1, 0]</code> → Score = 1*1 + 0*1 + 0*0 = 1</p>
    <p>Key 3: <code>[0, 1, 1]</code> → Score = 1*0 + 0*1 + 0*1 = 0</p>
    <p>Key 1 best matches the query.</p>
</div>

<p><strong>Mathematical Insight:</strong> Dot product of normalized vectors equals cosine similarity. If q and k are unit vectors:</p>
<p class="formula">$$q \\cdot k = \\cos(\\theta)$$</p>

<p>where \(\\theta\) is the angle between them.</p>

<p><strong>Why Scaling?</strong> When d is large, dot products can become very large, causing softmax to produce near-zero or near-one weights (saturation). The scaling factor <code>1/√d</code> prevents this:</p>
<p class="formula">$$\\text{score}(q, k) = \\frac{q \\cdot k}{\\sqrt{d}}$$</p>

<div class="warning-box">
    <p><strong>Without Scaling:</strong> If q and k have magnitude ~√d, their dot product is ~d. With d=512 (typical), scores reach hundreds, making softmax almost binary.</p>
    <p><strong>With Scaling:</strong> Scores stay around [0, 1], keeping softmax output diffuse and learnable.</p>
</div>'''},

    {
        "id": "additive_scoring",
        "title": "Additive (Bahdanau) Scoring",
        "body": '''<p><strong>More Complex Scoring:</strong> Learn a nonlinear similarity function using a neural network.</p>

<p class="formula">$$\\text{score}(q, k) = v^T \\tanh(W_q q + W_k k)$$</p>

<p><strong>Components:</strong></p>
<ul>
    <li><code>W_q, W_k:</code> Learned weight matrices [hidden_dim x attention_dim]</li>
    <li><code>tanh:</code> Nonlinear activation function</li>
    <li><code>v:</code> Learned projection vector [attention_dim]</li>
</ul>

<p><strong>Process:</strong></p>
<ol>
    <li>Project query: <code>q' = W_q * q</code> [attention_dim]</li>
    <li>Project key: <code>k' = W_k * k</code> [attention_dim]</li>
    <li>Add: <code>combined = q' + k'</code></li>
    <li>Apply nonlinearity: <code>hidden = tanh(combined)</code></li>
    <li>Project to scalar: <code>score = v^T * hidden</code></li>
</ol>

<div class="worked-example">
    <p><strong>Example with attention_dim=2, hidden_dim=3:</strong></p>
    <p>Query: <code>[1, 2, 3]</code></p>
    <p>Key: <code>[0.5, 1, 1.5]</code></p>
    <p>W_q: <code>[[1, 0], [0, 1], [1, 1]]</code></p>
    <p>W_k: <code>[[1, 0], [0, 1], [0, 0]]</code></p>
    <p>q' = W_q @ q = <code>[1, 2]</code> + <code>[3]</code> = <code>[4, 5]</code></p>
    <p>k' = W_k @ k = <code>[0.5, 1]</code></p>
    <p>combined = <code>[4.5, 6]</code></p>
    <p>hidden = tanh(<code>[4.5, 6]</code>) ≈ <code>[1, 1]</code> (tanh saturates)</p>
    <p>score = v @ <code>[1, 1]</code> (depends on v)</p>
</div>

<p><strong>Advantages over Dot-Product:</strong></p>
<ul>
    <li>Can learn more complex similarity patterns</li>
    <li>Nonlinearity captures non-linear relationships</li>
</ul>

<p><strong>Disadvantages:</strong></p>
<ul>
    <li>More parameters (W_q, W_k, v)</li>
    <li>Slightly higher computational cost</li>
    <li>More prone to overfitting on small datasets</li>
</ul>

<p><strong>Historical Note:</strong> Called "Bahdanau attention" after the 2014 paper that introduced it for neural machine translation.</p>'''},

    {
        "id": "comparison_and_choice",
        "title": "When to Use Which Scoring Function",
        "body": '''<p><strong>Practical Comparison:</strong></p>

<table>
    <tr>
        <th>Aspect</th>
        <th>Dot-Product</th>
        <th>Additive</th>
    </tr>
    <tr>
        <td><strong>Complexity</strong></td>
        <td>O(d)</td>
        <td>O(d * a) where a = attention_dim</td>
    </tr>
    <tr>
        <td><strong>Parameters</strong></td>
        <td>0</td>
        <td>d*a + a*d + a = ~2*d*a</td>
    </tr>
    <tr>
        <td><strong>Expressiveness</strong></td>
        <td>Linear in q, k</td>
        <td>Nonlinear</td>
    </tr>
    <tr>
        <td><strong>GPU Friendly</strong></td>
        <td>Yes (matrix mult)</td>
        <td>Slightly less</td>
    </tr>
    <tr>
        <td><strong>When Used</strong></td>
        <td>Transformers (BERT, GPT)</td>
        <td>RNN+Attention (older)</td>
    </tr>
</table>

<div class="concept-box">
    <p><strong>Modern Practice:</strong> Dot-product attention is preferred because:</p>
    <ul>
        <li>Highly optimized on GPUs</li>
        <li>Simpler to understand and debug</li>
        <li>Works equally well in practice</li>
        <li>Nonlinearity can come from other layers</li>
    </ul>
</div>

<p><strong>When to Consider Additive:</strong></p>
<ul>
    <li>Low-dimensional hidden states where nonlinearity helps</li>
    <li>Small-scale models where exact expressiveness matters</li>
    <li>Tasks requiring very precise alignment patterns</li>
</ul>

<p><strong>Other Scoring Functions:</strong> Researchers have explored variants like multiplicative-additive, learned scaling factors, and attention with gating mechanisms. But dot-product and additive remain the most common.</p>'''
    }
]
