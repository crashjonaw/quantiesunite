TITLE = "ReLU Family of Activations"

SECTIONS = [
    {
        "title": "Rectified Linear Unit (ReLU)",
        "body": """<p>ReLU is the most popular activation function for hidden layers. It's simple but highly effective:</p>
<div class="concept-box">
<p><strong>ReLU(z) = max(0, z)</strong></p>
<p>If z > 0: output z</p>
<p>If z ≤ 0: output 0</p>
</div>
<h3>Why ReLU Changed Everything</h3>
<ul>
<li><strong>Gradient:</strong> ReLU'(z) = 1 if z > 0, and 0 if z < 0</li>
<li><strong>Fast:</strong> Just a comparison and multiplication—computationally cheap</li>
<li><strong>No saturation:</strong> For positive values, gradient stays constant at 1</li>
<li><strong>Solves vanishing gradients:</strong> Constant nonzero gradient in positive region enables deep networks to train</li>
</ul>
<p>ReLU made deep learning practical. It's the default choice for modern neural networks.</p>"""
    },
    {
        "title": "The Dead ReLU Problem",
        "body": """<p>ReLU's main drawback: neurons can become "dead" and stop learning entirely.</p>
<div class="warning-box">
<h3>What is a Dead Neuron?</h3>
<p>A dead ReLU neuron outputs 0 for all training inputs because its weights and bias are initialized such that z < 0 always.</p>
<p>Consequences:</p>
<ul>
<li>Activation: always 0</li>
<li>Gradient: always 0</li>
<li>Weight updates: none (stuck)</li>
<li>Result: neuron becomes permanently useless</li>
</ul>
</div>
<p>Dead ReLUs are caused by: high learning rates (overshooting), poor weight initialization, or sparse input data. Monitor for this during training.</p>"""
    },
    {
        "title": "ReLU Variants: Fixing Dead Neurons",
        "body": """<p>Several improvements address the dead ReLU problem while maintaining ReLU's benefits:</p>
<h3>Leaky ReLU</h3>
<div class="concept-box">
<p><strong>Leaky ReLU(z) = z if z > 0, else αz (where α = 0.01)</strong></p>
<p>The small negative slope (α) allows gradients to flow even when z < 0. Weights can still update, preventing dead neurons.</p>
</div>
<h3>Parametric ReLU (PReLU)</h3>
<p>Like Leaky ReLU, but let the network <strong>learn</strong> the slope α during training instead of fixing it.</p>
<h3>ELU (Exponential Linear Unit)</h3>
<div class="concept-box">
<p><strong>ELU(z) = z if z > 0, else α(e^z - 1)</strong></p>
<p>Smoother transition and mean activation closer to zero, aiding optimization.</p>
</div>"""
    },
    {
        "title": "GELU: Modern Alternative",
        "body": """<p>GELU (Gaussian Error Linear Unit) is the state-of-the-art activation for modern models:</p>
<div class="concept-box">
<p><strong>GELU(z) = z · Φ(z)</strong></p>
<p>where Φ(z) is the cumulative distribution function of a standard normal.</p>
</div>
<h3>Advantages</h3>
<ul>
<li><strong>Smooth:</strong> Differentiable everywhere (unlike ReLU's kink)</li>
<li><strong>Nonlinear throughout:</strong> Not just a linear pass-through</li>
<li><strong>Probabilistic interpretation:</strong> Gating based on input distribution</li>
<li><strong>Modern standard:</strong> Used in Transformers and large language models (GPT, BERT)</li>
</ul>
<p>GELU is preferred when smooth activations and state-of-the-art performance matter.</p>"""
    }
]
