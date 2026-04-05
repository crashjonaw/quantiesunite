TITLE = "Attention Variants: Bahdanau and Luong"

SECTIONS = [
    {
        "id": "historical_context",
        "title": "Historical Development of Attention",
        "body": '''<p><strong>Timeline:</strong> Two key papers defined how we think about attention in sequence-to-sequence models:</p>

<div class="concept-box">
    <p><strong>2014 - Bahdanau et al.:</strong> "Neural Machine Translation by Jointly Learning to Align and Translate"</p>
    <ul>
        <li>First attention mechanism for NMT</li>
        <li>Solved the long-sequence problem in encoder-decoder models</li>
        <li>Introduced the query-key-value framework conceptually</li>
    </ul>
</div>

<div class="concept-box">
    <p><strong>2015 - Luong et al.:</strong> "Effective Approaches to Attention-based Neural Machine Translation"</p>
    <ul>
        <li>Simplified and generalized Bahdanau attention</li>
        <li>Introduced multiple scoring functions systematically</li>
        <li>Provided empirical analysis of attention variants</li>
    </ul>
</div>

<p><strong>Key Insight:</strong> Both papers achieved similar goals (allowing variable-length context) but took different architectural approaches.</p>'''},

    {
        "id": "bahdanau_mechanism",
        "title": "Bahdanau Attention Mechanism",
        "body": '''<p><strong>Original Formulation:</strong> Bahdanau attention was designed for RNN-based encoder-decoder models.</p>

<p><strong>Architecture:</strong></p>
<p>For each decoder timestep t:</p>

<p class="formula">$$\\text{context}_t = \\sum_{s=1}^{S} \\alpha_{t,s} h_s$$</p>

<p>where:</p>
<ul>
    <li><code>h_s:</code> Encoder hidden state at position s</li>
    <li><code>α_t,s:</code> Attention weight (computed below)</li>
    <li><code>context_t:</code> Weighted sum (context vector)</li>
</ul>

<p><strong>Attention Weights Computation:</strong></p>

<p class="formula">$$\\alpha_{t,s} = \\frac{\\exp(\\text{score}_t(s))}{\\sum_{s'=1}^{S} \\exp(\\text{score}_t(s'))}$$</p>

<p>This is softmax over all scores at step t.</p>

<p><strong>Scoring Function (Additive):</strong></p>

<p class="formula">$$\\text{score}_t(s) = v^T \\tanh(W_1 [d_t; h_s])$$</p>

<p>where:</p>
<ul>
    <li><code>d_t:</code> Decoder hidden state at step t (the query)</li>
    <li><code>h_s:</code> Encoder hidden state s (the key)</li>
    <li><code>[d_t; h_s]:</code> Concatenation of decoder and encoder states</li>
    <li><code>W_1:</code> Learned weight matrix [2*hidden_dim x attention_dim]</li>
    <li><code>v:</code> Learned weight vector [attention_dim]</li>
</ul>

<div class="worked-example">
    <p><strong>Concrete Example: Machine Translation</strong></p>
    <p>Input: "bonjour le monde" (French)</p>
    <p>Output: "hello world" (English)</p>
    <p>At decoder step 1 (generating "hello"):</p>
    <ul>
        <li>Decoder state d_1 is initialized (or learned)</li>
        <li>Score each encoder state: [bonjour, le, monde]</li>
        <li>Scores might be: [0.7, 0.2, 0.1] (favoring "bonjour")</li>
        <li>Softmax: [0.57, 0.29, 0.14]</li>
        <li>Context: 0.57*h_bonjour + 0.29*h_le + 0.14*h_monde</li>
    </ul>
    <p>At decoder step 2 (generating "world"):</p>
    <ul>
        <li>New decoder state d_2</li>
        <li>Attention shifts toward later input positions</li>
        <li>Scores might be: [0.2, 0.3, 0.5] (favoring "monde")</li>
        <li>Different context emphasizes "monde"</li>
    </ul>
</div>

<p><strong>Key Characteristics:</strong></p>
<ul>
    <li><strong>Query:</strong> Decoder hidden state</li>
    <li><strong>Keys/Values:</strong> Encoder hidden states</li>
    <li><strong>Scoring:</strong> Additive (nonlinear)</li>
    <li><strong>Context:</strong> Weighted sum of all encoder states</li>
    <li><strong>Fully Differentiable:</strong> All steps support backpropagation</li>
</ul>

<p><strong>Why Concatenation?</strong> Bahdanau concatenates decoder and encoder states before passing through the nonlinear function. This allows the scoring function to consider both simultaneously and learn their interaction pattern.</p>'''},

    {
        "id": "luong_mechanism",
        "title": "Luong Attention Mechanism",
        "body": '''<p><strong>Simplified Formulation:</strong> Luong et al. proposed a cleaner attention mechanism that is easier to implement and understand.</p>

<p><strong>Key Differences from Bahdanau:</strong></p>

<table>
    <tr>
        <th>Aspect</th>
        <th>Bahdanau</th>
        <th>Luong</th>
    </tr>
    <tr>
        <td><strong>Computation</strong></td>
        <td>Before decoder output</td>
        <td>After decoder output</td>
    </tr>
    <tr>
        <td><strong>Scoring</strong></td>
        <td>Additive (tanh)</td>
        <td>Multiple options</td>
    </tr>
    <tr>
        <td><strong>Query</strong></td>
        <td>Decoder state</td>
        <td>Decoder output (after RNN)</td>
    </tr>
    <tr>
        <td><strong>Complexity</strong></td>
        <td>O(d_a) per position</td>
        <td>O(1) to O(d_a) depending on scoring</td>
    </tr>
</table>

<p><strong>Luong Scoring Functions:</strong> Three options (general, multiplicative, additive):</p>

<p><strong>1. General (Dot-Product with Learned Transform):</strong></p>
<p class="formula">$$\\text{score}(d_t, h_s) = d_t^T W_a h_s$$</p>

<p>where <code>W_a:</code> Learned weight matrix [hidden_dim x hidden_dim]</p>

<div class="worked-example">
    <p>Allows rotation and scaling of the decoder state before dot product.</p>
    <p>Less parameters than Bahdanau, more flexible than pure dot-product.</p>
</div>

<p><strong>2. Multiplicative (Pure Dot-Product):</strong></p>
<p class="formula">$$\\text{score}(d_t, h_s) = d_t^T h_s$$</p>

<p>Simplest form. No parameters (beyond scaling).</p>

<p><strong>3. Additive (Like Bahdanau):</strong></p>
<p class="formula">$$\\text{score}(d_t, h_s) = v^T \\tanh(W_1 d_t + W_2 h_s)$$</p>

<p>Note: Bahdanau concatenates before nonlinearity. Luong applies nonlinearity separately to each, then adds.</p>

<p><strong>Full Luong Attention Process:</strong></p>

<p class="formula">$$a_t(s) = \\text{softmax}(\\text{score}(d_t, h_s))$$</p>

<p class="formula">$$c_t = \\sum_s a_t(s) h_s$$</p>

<p class="formula">$$\\tilde{h}_t = \\tanh(W_c [c_t; d_t])$$</p>

<p>The final hidden state combines context and decoder output through a learned gate.</p>

<div class="concept-box">
    <p><strong>Attentional Hidden State:</strong> Luong computes a new <code>~h_t</code> that combines attention context with the decoder's own output. This allows the decoder to incorporate attention information before generating the next token.</p>
</div>'''},

    {
        "id": "comparison_and_impact",
        "title": "Comparing Bahdanau and Luong",
        "body": '''<p><strong>Practical Differences:</strong></p>

<div class="concept-box">
    <p><strong>Bahdanau:</strong> Attention-is-All-You-Need approach</p>
    <ul>
        <li>Attention computed before RNN step</li>
        <li>Context influences what RNN generates</li>
        <li>Strictly additive scoring</li>
        <li>Tends to work better with bidirectional encoders</li>
    </ul>
</div>

<div class="concept-box">
    <p><strong>Luong:</strong> Attention-as-Post-Processing approach</p>
    <ul>
        <li>Attention computed after RNN step</li>
        <li>RNN generates independently, then refine with context</li>
        <li>Flexible scoring functions</li>
        <li>Simpler parameter sharing</li>
    </ul>
</div>

<p><strong>Empirical Findings (Luong et al. 2015):</strong></p>
<ul>
    <li>Both achieve similar final performance</li>
    <li>Luong slightly faster (fewer parameters)</li>
    <li>Bahdanau sometimes converges faster</li>
    <li>Multiplicative scoring is competitive with additive</li>
</ul>

<p><strong>Modern Context:</strong></p>

<div class="success-box">
    <p><strong>Why Transformers Use Multiplicative (Dot-Product):</strong> Transformers adopted Luong's multiplicative scoring because:</p>
    <ul>
        <li>Scales to huge models</li>
        <li>Hardware optimized for matrix multiplication</li>
        <li>Performs well with proper scaling</li>
        <li>Simpler to implement and understand</li>
    </ul>
</div>

<p><strong>Legacy:</strong> While RNN+Attention has been superseded by Transformers, understanding Bahdanau and Luong remains important because:</p>
<ul>
    <li>They introduced core attention concepts</li>
    <li>Same principles apply in modern architectures</li>
    <li>RNNs with attention still used in some applications</li>
    <li>Historical understanding aids deep learning intuition</li>
</ul>'''
    }
]
