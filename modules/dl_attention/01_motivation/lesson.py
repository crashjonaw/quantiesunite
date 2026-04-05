TITLE = "Motivation for Attention"

SECTIONS = [
    {
        "id": "bottleneck_problem",
        "title": "The Bottleneck Problem in Encoder-Decoder",
        "body": '''<p><strong>First Principles:</strong> In traditional encoder-decoder architectures, the entire source sequence is compressed into a single fixed-size context vector <code>c</code>.</p>

<div class="concept-box">
    <p><strong>The Problem:</strong> A single context vector creates an information bottleneck. No matter how long the source sequence is, all its information must fit into one vector. This is like trying to summarize an entire book in a single sentence.</p>
</div>

<p><strong>Mathematical View:</strong> For a sequence of length <code>T</code>, we compute:</p>
<p class="formula">$$c = \\sum_{t=1}^{T} \\alpha_t h_t$$</p>

<p>where <code>α_t</code> are fixed weights (usually uniform or learned once). But <code>c</code> has constant dimension regardless of <code>T</code>.</p>

<div class="worked-example">
    <p><strong>Example:</strong> Translating "The quick brown fox" requires the same vector size as "The quick brown fox jumps over the lazy dog". But the second sentence has 7x more information to convey!</p>
</div>

<p><strong>Key Insight:</strong> Different output tokens should attend to different parts of the input. The decoder's attention should be dynamic—changing based on what the decoder is currently generating.</p>'''},

    {
        "id": "solution_dynamic_context",
        "title": "Dynamic Context: The Solution",
        "body": '''<p>Instead of a single context vector, we compute a <strong>different context vector for each output step</strong>.</p>

<div class="success-box">
    <p><strong>The Idea:</strong> At each decoding step <code>t</code>, the model learns which parts of the encoder output are most relevant, and uses those to guide its predictions.</p>
</div>

<p><strong>Conceptual Process:</strong></p>
<ol>
    <li>Decoder is about to generate word <code>t</code></li>
    <li>Model scores each encoder output: "How relevant is this to what I need now?"</li>
    <li>Normalize scores to weights (sum to 1)</li>
    <li>Compute context as weighted sum of encoder outputs</li>
    <li>Use context to help generate word <code>t</code></li>
</ol>

<p><strong>Why This Works:</strong> Each output position gets a tailored context vector that highlights the most relevant input positions. For translation, the model can focus on different words at different steps.</p>

<div class="concept-box">
    <p>Attention: <strong>Dynamic context computation</strong> where the model learns what to focus on, when to focus on it, and how much.</p>
</div>'''},

    {
        "id": "why_attention_matters",
        "title": "Why Attention Matters",
        "body": '''<p><strong>Beyond Information Bottleneck:</strong></p>

<ul>
    <li><strong>Interpretability:</strong> Attention weights show which inputs influenced which outputs. We can visualize and understand model decisions.</li>
    <li><strong>Long-Range Dependencies:</strong> Attention directly connects distant positions without going through many intermediate layers.</li>
    <li><strong>Scalability:</strong> The model can handle varying input lengths without architectural changes.</li>
    <li><strong>Gradient Flow:</strong> Gradients can flow directly from output to relevant input positions, improving training.</li>
</ul>

<p><strong>Historical Impact:</strong> Attention mechanisms were the crucial innovation that led to Transformers (Vaswani et al., 2017), which revolutionized NLP and deep learning.</p>'''},

    {
        "id": "from_motivation_to_mechanism",
        "title": "From Motivation to Mechanism",
        "body": '''<p>Now that we understand <strong>why</strong> attention is needed, the next lesson explores <strong>how</strong> it works mathematically.</p>

<div class="concept-box">
    <p><strong>Preview:</strong> We'll formalize attention using three concepts:</p>
    <ul>
        <li><strong>Query:</strong> "What am I looking for?" (decoder state)</li>
        <li><strong>Key:</strong> "What is each input?" (encoder outputs)</li>
        <li><strong>Value:</strong> "What do I retrieve?" (encoder outputs)</li>
    </ul>
</div>

<p>These will lead us to the complete attention formula and its variants.</p>'''
    }
]
