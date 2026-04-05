TITLE = "Softmax and Output Layer Activations"

SECTIONS = [
    {
        "title": "Softmax for Multi-Class Classification",
        "body": """<p>Softmax converts raw network outputs into a proper probability distribution over K classes:</p>
<div class="concept-box">
<p>$$\\text{softmax}(z_i) = \\frac{e^{z_i}}{\\sum_j e^{z_j}}$$</p>
</div>
<h3>Key Properties</h3>
<ul>
<li><strong>Probabilities:</strong> Each output is between 0 and 1</li>
<li><strong>Valid distribution:</strong> All outputs sum to exactly 1</li>
<li><strong>Differentiable:</strong> Works with gradient descent</li>
<li><strong>Order-preserving:</strong> If $z_i > z_j$, then $\\text{softmax}(z_i) > \\text{softmax}(z_j)$</li>
</ul>
<h3>Example</h3>
<p>Network outputs $(z_1, z_2, z_3) = (2.0, 1.0, 0.1)$</p>
<p>After softmax: $(\\approx 0.66, \\approx 0.24, \\approx 0.10)$ — sums to $1.0$, interpretable as class probabilities.</p>"""
    },
    {
        "title": "Softmax + Cross-Entropy: A Powerful Pair",
        "body": """<p>Softmax is almost always paired with cross-entropy loss for multi-class classification:</p>
<div class="concept-box">
<p>$$L = -\\sum_i y_i \\cdot \\log(p_i)$$</p>
<p>where $y_i$ is the true label (one-hot encoded) and $p_i$ is the softmax output.</p>
</div>
<h3>Why This Combination Works So Well</h3>
<ul>
<li><strong>Numerically stable:</strong> Log-softmax is computed in a way that avoids overflow/underflow</li>
<li><strong>Ideal gradient properties:</strong> The gradient is proportional to prediction error: $\\nabla L = (p - y)$</li>
<li><strong>Conceptual fit:</strong> KL divergence between predicted and true probability distributions</li>
</ul>
<p>This is the gold standard for multi-class classification problems.</p>"""
    },
    {
        "title": "Sigmoid for Binary Classification",
        "body": """<p>For binary classification, use sigmoid on a <strong>single</strong> output neuron:</p>
<div class="concept-box">
<p>$$\\sigma(z) = \\frac{1}{1 + e^{-z}}$$</p>
<p>Output $\\approx$ probability of class 1</p>
</div>
<h3>Binary Cross-Entropy Loss</h3>
<p>Pair sigmoid with binary cross-entropy:</p>
<p>$$L = -[y \\cdot \\log(\\sigma(z)) + (1-y) \\cdot \\log(1 - \\sigma(z))]$$</p>
<p>where $y \\in \\{0, 1\\}$.</p>
<div class="worked-example">
<h3>Alternative: Two Outputs with Softmax</h3>
<p>You can also use two output neurons with softmax. This is equivalent to sigmoid, just with different notation. Softmax is more flexible if you later expand to multi-class.</p>
</div>"""
    },
    {
        "title": "Linear Output for Regression",
        "body": """<p>For regression tasks, use <strong>no activation</strong> (identity function):</p>
<div class="concept-box">
<p>$$\\hat{y} = z = Wx + b$$</p>
<p>Network output can be any real value (no bounds).</p>
</div>
<h3>Mean Squared Error Loss</h3>
<p>Pair with MSE loss:</p>
<p>$$L = \\frac{1}{n} \\sum_i (\\hat{y}_i - y_i)^2$$</p>
<h3>Summary Table</h3>
<div class="success-box">
<p><strong>Task:</strong> Binary Classification → <strong>Activation:</strong> Sigmoid → <strong>Loss:</strong> Binary CE</p>
<p><strong>Task:</strong> Multi-Class → <strong>Activation:</strong> Softmax → <strong>Loss:</strong> Cross-Entropy</p>
<p><strong>Task:</strong> Regression → <strong>Activation:</strong> Linear (none) → <strong>Loss:</strong> MSE</p>
<p><strong>Task:</strong> Bounded Regression → <strong>Activation:</strong> Sigmoid or Tanh → <strong>Loss:</strong> MSE</p>
</div>"""
    }
]
