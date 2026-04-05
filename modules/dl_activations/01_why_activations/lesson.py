TITLE = "Why Activation Functions"

SECTIONS = [
    {
        "title": "The Linearity Problem",
        "body": """<p>Without activation functions, neural networks are just stacked linear transformations. If you compose linear functions, the result is still linear:</p>
<div class="concept-box">
<p><strong>Layer 1:</strong> y₁ = W₁x + b₁</p>
<p><strong>Layer 2:</strong> y₂ = W₂y₁ + b₂ = W₂(W₁x + b₁) + b₂ = (W₂W₁)x + (W₂b₁ + b₂)</p>
<p><strong>Result:</strong> Still a linear function of input x</p>
</div>
<p>A linear network <strong>cannot</strong> learn nonlinear patterns like curves, non-straight decision boundaries, or complex feature interactions. This is the fundamental limitation that activation functions solve.</p>"""
    },
    {
        "title": "Introducing Nonlinearity",
        "body": """<p>Activation functions introduce nonlinearity into neural networks. This enables three critical capabilities:</p>
<div class="success-box">
<h3>Universal Approximation</h3>
<p>Sufficiently deep networks with nonlinear activations can approximate any continuous function.</p>
</div>
<div class="success-box">
<h3>Hierarchical Feature Learning</h3>
<p>Hidden layers learn hierarchical, nonlinear combinations of inputs—not just reweighting raw inputs.</p>
</div>
<div class="success-box">
<h3>Complex Decision Boundaries</h3>
<p>Networks can learn curved, nonlinear boundaries between classes instead of just straight lines.</p>
</div>"""
    },
    {
        "title": "Mathematical Foundation",
        "body": """<p>An activation function σ(z) transforms each neuron's pre-activation value z:</p>
<div class="concept-box">
<p><strong>a = σ(z) = σ(Wx + b)</strong></p>
</div>
<p>The nonlinearity comes entirely from the function σ. Common choices include:</p>
<ul>
<li><strong>Sigmoid:</strong> Smooth, bounded outputs</li>
<li><strong>Tanh:</strong> Zero-centered alternative to sigmoid</li>
<li><strong>ReLU:</strong> Modern choice, simple and effective</li>
</ul>
<p>Without σ (or if σ is linear), stacking layers produces only a linear transformation—no matter how deep the network.</p>"""
    }
]
