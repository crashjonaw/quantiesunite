TITLE = "Sigmoid and Hyperbolic Tangent"

SECTIONS = [
    {
        "title": "The Sigmoid Function",
        "body": """<p>The sigmoid function is one of the earliest and most intuitive activation functions:</p>
<div class="concept-box">
<p><strong>\(\\sigma(z) = 1 / (1 + e^{-z})\)</strong></p>
</div>
<h3>Key Properties</h3>
<ul>
<li><strong>Range:</strong> (0, 1) — always outputs probabilities</li>
<li><strong>Smooth:</strong> Differentiable everywhere</li>
<li><strong>Derivative:</strong> \(\\sigma'(z) = \\sigma(z)(1 - \\sigma(z))\)</li>
<li><strong>Maximum slope:</strong> \(\\sigma'(0) = 0.25\) at \(z=0\)</li>
</ul>
<p><strong>Best use:</strong> Binary classification output layer. Hidden layers should generally avoid sigmoid.</p>"""
    },
    {
        "title": "The Vanishing Gradient Problem",
        "body": """<p>Sigmoid's greatest weakness: when z is large or small, the gradient becomes vanishingly small.</p>
<div class="warning-box">
<h3>The Problem</h3>
<p>At \(z = 5\): \(\\sigma'(5) \\approx 0.0066\)</p>
<p>At \(z = -5\): \(\\sigma'(-5) \\approx 0.0066\)</p>
<p>In deep networks, these small gradients multiply across many layers:</p>
<p><strong>\(0.0066^{10} \\approx 10^{-25}\)</strong></p>
</div>
<p>The gradient becomes so small that weights barely update. The network effectively stops learning. This is why sigmoid is rarely used for hidden layers in modern deep networks.</p>"""
    },
    {
        "title": "Hyperbolic Tangent (tanh)",
        "body": """<p>Tanh improves upon sigmoid in key ways:</p>
<div class="concept-box">
<p><strong>tanh(z) = (e^z - e^(-z)) / (e^z + e^(-z)) = 2/(1 + e^(-2z)) - 1</strong></p>
</div>
<h3>Advantages over Sigmoid</h3>
<ul>
<li><strong>Range:</strong> (-1, 1) instead of (0, 1)</li>
<li><strong>Zero-centered:</strong> Outputs centered around 0, improving optimization</li>
<li><strong>Stronger gradient:</strong> tanh'(0) = 1 (vs sigmoid's 0.25)</li>
<li><strong>Better for hidden layers:</strong> Balanced weight updates</li>
</ul>
<p>However, tanh still suffers from vanishing gradients in very deep networks, which is why ReLU has become the modern standard.</p>"""
    }
]
