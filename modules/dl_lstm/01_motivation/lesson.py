TITLE = "Motivation: The Vanishing Gradient Problem in RNNs"

SECTIONS = [
    {
        "title": "The Vanishing Gradient Problem",
        "body": """<div class="concept-box">
<h3>Standard RNN Hidden State Update</h3>
<p>In standard RNNs, the hidden state is updated via:</p>
<p><strong>h<sub>t</sub> = tanh(W<sub>h</sub> h<sub>t-1</sub> + W<sub>x</sub> x<sub>t</sub> + b)</strong></p>
<p>When backpropagating through time (BPTT), we compute gradients for each time step. The gradient with respect to earlier states involves multiplying by the Jacobian repeatedly:</p>
<p><strong>∂h<sub>t</sub>/∂h<sub>1</sub> = ∏<sub>i=2</sub><sup>t</sup> ∂h<sub>i</sub>/∂h<sub>i-1</sub></strong></p>
<p>Since tanh'(·) is bounded (max 1) and W<sub>h</sub> is typically small, these products become exponentially small. This is the <strong>vanishing gradient problem</strong>.</p>
</div>
<div class="warning-box">
<h3>Consequence</h3>
<p>The network cannot learn long-term dependencies. Gradients from distant past states become negligible, making it impossible to capture patterns that span many time steps.</p>
</div>"""
    },
    {
        "title": "Why This Matters: Real-World Impact",
        "body": """<div class="concept-box">
<h3>The Challenge of Long-Range Dependencies</h3>
<p>Consider this sequence:</p>
<p style="font-style: italic;">"The cat sat on the mat. ... [100 steps later] ... The sentence uses the language ___."</p>
<p>A standard RNN struggles to remember "cat" from 100 steps ago because gradients don't flow back that far.</p>
<p>For many real applications—language modeling, speech recognition, time series forecasting—capturing long-range dependencies is essential. Without it, models fail to capture critical patterns that span significant temporal distances.</p>
</div>
<div class="worked-example">
<h3>Why LSTMs Matter</h3>
<p>LSTMs were specifically designed to address this limitation. They allow networks to learn and propagate gradients across much longer sequences, making them essential for modern deep learning.</p>
</div>"""
    },
    {
        "title": "The Solution: Additive State Updates with Gates",
        "body": """<div class="concept-box">
<h3>Core Insight: Addition Instead of Multiplication</h3>
<p>Rather than allowing hidden state to be fully replaced at each step, we can introduce a <strong>cell state</strong> that changes more slowly, with modification controlled by <strong>gates</strong>.</p>
<p>If the cell state changes via <strong>addition</strong> instead of multiplication:</p>
<p><strong>c<sub>t</sub> = f<sub>t</sub> ⊙ c<sub>t-1</sub> + i<sub>t</sub> ⊙ c̃<sub>t</sub></strong></p>
<p>Then the gradient becomes:</p>
<p><strong>∂c<sub>t</sub>/∂c<sub>t-1</sub> = f<sub>t</sub></strong></p>
<p>When the forget gate f<sub>t</sub> ≈ 1, gradients can flow unobstructed through the cell state. This is the core insight of LSTMs and GRUs.</p>
</div>
<div class="success-box">
<h3>Key Takeaway</h3>
<p>The vanishing gradient problem arises from <strong>multiplicative interactions</strong> in standard RNNs. LSTMs solve this by introducing <strong>additive paths</strong> (cell state) with <strong>gating mechanisms</strong> to control information flow. This design preserves gradient flow across long sequences.</p>
</div>"""
    }
]
