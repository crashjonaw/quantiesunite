TITLE = "Multi-Head Attention"

SECTIONS = [
    {
        "id": "single_head_limitations",
        "title": "Why Single Attention is Not Enough",
        "body": '''<p><strong>First Principles:</strong> Single-head attention learns one way of matching queries to keys. But different types of relationships require different matching patterns.</p>

<div class="worked-example">
    <p><strong>Example: Translating "The bank near the river"</strong></p>
    <p>When generating the French translation, the model needs to:</p>
    <ul>
        <li>Align word order (positional relationships)</li>
        <li>Match semantic content ("bank" meaning financial institution)</li>
        <li>Handle pronoun references ("the" modifying "bank")</li>
        <li>Understand context from surrounding words</li>
    </ul>
    <p>A single attention pattern might excel at one but miss others.</p>
</div>

<p><strong>Limitation of Single Head:</strong> One scoring function produces one set of weights. These weights try to capture all relationships simultaneously, which is like asking a single camera to film a scene from all angles at once—something has to give.</p>

<div class="concept-box">
    <p><strong>The Solution:</strong> Instead of one attention head, use many (typically 8-16) in parallel. Each head learns to focus on different aspects of the input-output relationship.</p>
</div>

<p><strong>Analogy:</strong> Think of a committee of experts. One expert specializes in syntax, another in semantics, another in style. Each attends to the problem from their perspective, then their insights are combined.</p>'''},

    {
        "id": "multi_head_architecture",
        "title": "Multi-Head Attention Architecture",
        "body": '''<p><strong>Formal Computation:</strong></p>

<p class="formula">$$\\text{MultiHead}(Q, K, V) = \\text{Concat}(\\text{head}_1, ..., \\text{head}_h) W^O$$</p>

<p>where each head is:</p>

<p class="formula">$$\\text{head}_i = \\text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)$$</p>

<p><strong>Components:</strong></p>
<ul>
    <li><code>h:</code> Number of heads (typically 8, 16, or more)</li>
    <li><code>W_i^Q, W_i^K, W_i^V:</code> Learned projection matrices for head i</li>
    <li><code>W^O:</code> Output projection matrix</li>
    <li><code>Concat:</code> Concatenate outputs from all heads</li>
</ul>

<p><strong>Step-by-Step Process (with 2 heads for clarity):</strong></p>

<ol>
    <li><strong>Project:</strong> Transform Q, K, V using head-specific weight matrices
        <ul>
            <li>Head 1: Q' = Q @ W_1^Q, K' = K @ W_1^K, V' = V @ W_1^V</li>
            <li>Head 2: Q'' = Q @ W_2^Q, K'' = K @ W_2^K, V'' = V @ W_2^V</li>
        </ul>
    </li>

    <li><strong>Attention:</strong> Apply scaled dot-product attention to each head
        <ul>
            <li>Head 1 output: Attention(Q', K', V')</li>
            <li>Head 2 output: Attention(Q'', K'', V'')</li>
        </ul>
    </li>

    <li><strong>Concatenate:</strong> Combine outputs
        <ul>
            <li>Concat = [Head1_output || Head2_output]</li>
        </ul>
    </li>

    <li><strong>Project Output:</strong> Apply final linear transformation
        <ul>
            <li>Output = Concat @ W^O</li>
        </ul>
    </li>
</ol>

<div class="worked-example">
    <p><strong>Dimension Example (typical Transformer):</strong></p>
    <p>Hidden dim: 512, Num heads: 8, Head dim: 512/8 = 64</p>
    <p>Input Q, K, V: [batch, seq_len, 512]</p>
    <p>After head-specific projection: [batch, seq_len, 64]</p>
    <p>Attention output per head: [batch, seq_len, 64]</p>
    <p>Concatenated: [batch, seq_len, 512] (all heads' outputs)</p>
    <p>Final output: [batch, seq_len, 512] (after W^O)</p>
</div>

<p><strong>Key Insight:</strong> The total computational work is similar to single-head attention (just distributed across heads), but the model learns much richer patterns.</p>'''},

    {
        "id": "what_heads_learn",
        "title": "What Different Heads Learn",
        "body": '''<p><strong>Empirical Analysis:</strong> Research on trained Transformers shows that different heads specialize:</p>

<div class="concept-box">
    <p><strong>Head Specialization (from Vaswani et al., 2017 and others):</strong></p>
    <ul>
        <li><strong>Positional Heads:</strong> Mostly attend nearby positions (local context)</li>
        <li><strong>Broad Heads:</strong> Attend broadly across the sequence (global context)</li>
        <li><strong>Query Heads:</strong> Attend to specific frequent words (like "the", punctuation)</li>
        <li><strong>Relation Heads:</strong> Capture syntactic or semantic relationships</li>
    </ul>
</div>

<div class="worked-example">
    <p><strong>Attention Visualization Example:</strong></p>
    <p>Sentence: "I saw the dog with the telescope"</p>
    <p>For the word "with":</p>
    <ul>
        <li>Head 1 (positional): Strong attention to adjacent words [dog, the, I]</li>
        <li>Head 2 (relation): Attends to [dog, telescope] (prepositional phrase)</li>
        <li>Head 3 (broad): Weak attention spread across all words</li>
        <li>Head 4 (query): Strong attention to [the, the] (articles)</li>
    </ul>
    <p>Together: Richer understanding of the phrase structure and semantics.</p>
</div>

<p><strong>Not Perfect Separation:</strong> Heads don't have strict specializations. Rather, they discover useful complementary patterns through training. Some redundancy is normal and helps robustness.</p>

<p><strong>Head Importance:</strong> Not all heads are equally important. In many trained models, some heads contribute more to the final output than others. This is why some pruning techniques remove less-important heads without much accuracy loss.</p>'''},

    {
        "id": "advantages_and_tradeoffs",
        "title": "Advantages, Trade-offs, and Design Choices",
        "body": '''<p><strong>Advantages of Multi-Head Attention:</strong></p>

<div class="success-box">
    <ul>
        <li><strong>Richer Representations:</strong> Capture multiple types of relationships simultaneously</li>
        <li><strong>Better Generalization:</strong> Multiple views prevent overfitting to single patterns</li>
        <li><strong>Interpretability:</strong> Can analyze which head captures which pattern</li>
        <li><strong>Implicit Ensemble:</strong> Model has built-in redundancy for robustness</li>
        <li><strong>Empirically Superior:</strong> Multi-head consistently outperforms single-head</li>
    </ul>
</div>

<p><strong>Computational Cost:</strong></p>

<table>
    <tr>
        <th>Aspect</th>
        <th>Single-Head</th>
        <th>Multi-Head (h heads)</th>
    </tr>
    <tr>
        <td><strong>Projections</strong></td>
        <td>3 matrices: Q, K, V</td>
        <td>3h matrices: Q_1...Q_h, K_1...K_h, V_1...V_h</td>
    </tr>
    <tr>
        <td><strong>Attention Computation</strong></td>
        <td>O(n^2 * d)</td>
        <td>O(h * n^2 * d/h) = O(n^2 * d)</td>
    </tr>
    <tr>
        <td><strong>Memory</strong></td>
        <td>O(n^2 * d)</td>
        <td>O(h * n^2 * d/h) = O(n^2 * d)</td>
    </tr>
    <tr>
        <td><strong>Output Projection</strong></td>
        <td>None needed</td>
        <td>W^O: concatenated output</td>
    </tr>
</table>

<div class="concept-box">
    <p><strong>Surprising Fact:</strong> Multi-head attention (with proper dimensioning) has the same computational complexity as single-head attention! Each head operates on lower-dimensional subspaces (d/h instead of d).</p>
</div>

<p><strong>Design Choices:</strong></p>

<ul>
    <li><strong>Number of Heads:</strong>
        <ul>
            <li>Typical: 8, 12, 16 for standard models</li>
            <li>Larger models use more heads (GPT-3 uses 96 heads)</li>
            <li>Trade-off: More heads = finer specialization but harder to coordinate</li>
        </ul>
    </li>

    <li><strong>Head Dimension:</strong>
        <ul>
            <li>Usually: hidden_dim / num_heads</li>
            <li>Example: 512 dims / 8 heads = 64 dims per head</li>
            <li>Ensures total output size matches input size</li>
        </ul>
    </li>

    <li><strong>Initialization:</strong>
        <ul>
            <li>W_i^Q, W_i^K, W_i^V initialized similarly (usually Gaussian)</li>
            <li>W^O initialized to encourage diversity</li>
        </ul>
    </li>
</ul>

<p><strong>Modern Variants:</strong> Researchers have explored:</p>
<ul>
    <li><strong>Grouped Query Attention:</strong> Share key/value across multiple query heads (saves memory)</li>
    <li><strong>Multi-Query Attention:</strong> Single key/value shared by all query heads (extreme compression)</li>
    <li><strong>Sparse Multi-Head Attention:</strong> Each head attends to only a subset of positions</li>
</ul>

<p><strong>Why This Matters:</strong> Multi-head attention is one of the key innovations that made Transformers so effective. By learning multiple attention patterns in parallel, the model gains representational power that single-head architectures cannot match.</p>'''
    }
]
