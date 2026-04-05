TITLE = "Choosing Activation Functions"

SECTIONS = [
    {
        "title": "Hidden Layer Activation Selection",
        "body": """<p><strong>ReLU is the default choice for hidden layers</strong>—use it unless you have a specific reason not to.</p>
<h3>Why ReLU Wins</h3>
<div class="success-box">
<ul>
<li><strong>Fast:</strong> Computationally cheap (just max(0, z))</li>
<li><strong>Gradient-friendly:</strong> No vanishing gradients for positive inputs</li>
<li><strong>Sparse:</strong> Many neurons output 0, aiding generalization</li>
<li><strong>Proven:</strong> Well-studied, stable, works across problem types</li>
</ul>
</div>
<h3>When to Consider Alternatives</h3>
<div class="concept-box">
<p><strong>Dead ReLU problem?</strong> Use Leaky ReLU, ELU, or PReLU</p>
<p><strong>Want smooth activation?</strong> Use ELU or GELU</p>
<p><strong>Building a Transformer?</strong> GELU is the modern standard</p>
<p><strong>Legacy/constrained system?</strong> Tanh or Sigmoid (rare in new code)</p>
</div>"""
    },
    {
        "title": "Output Layer Activations by Task",
        "body": """<p>The output activation must match your task type:</p>
<div class="worked-example">
<h3>Binary Classification</h3>
<p><strong>Activation:</strong> Sigmoid → outputs in (0, 1)</p>
<p><strong>Loss:</strong> Binary cross-entropy</p>
<p><strong>Interpretation:</strong> Probability of positive class</p>
</div>
<div class="worked-example">
<h3>Multi-Class Classification (K > 2 classes)</h3>
<p><strong>Activation:</strong> Softmax → outputs sum to 1</p>
<p><strong>Loss:</strong> Cross-entropy</p>
<p><strong>Interpretation:</strong> Probability distribution over K classes</p>
</div>
<div class="worked-example">
<h3>Regression (Unbounded Output)</h3>
<p><strong>Activation:</strong> Linear (none)</p>
<p><strong>Loss:</strong> Mean squared error</p>
<p><strong>Interpretation:</strong> Any real number</p>
</div>
<div class="worked-example">
<h3>Bounded Regression</h3>
<p><strong>Activation:</strong> Sigmoid (output in [0,1]) or Tanh (output in [-1,1])</p>
<p><strong>Loss:</strong> Mean squared error</p>
<p><strong>Interpretation:</strong> Value constrained to a range</p>
</div>"""
    },
    {
        "title": "Architecture-Specific Guidance",
        "body": """<p>Different architectures have different conventions:</p>
<h3>CNNs (Computer Vision)</h3>
<div class="success-box">
<p><strong>Hidden layers:</strong> ReLU</p>
<p><strong>Output:</strong> Sigmoid (binary) or Softmax (multi-class)</p>
<p>Simple, fast, works well for image data.</p>
</div>
<h3>RNNs (Sequences, Time Series)</h3>
<div class="success-box">
<p><strong>Hidden layers:</strong> Tanh or use LSTM/GRU (built-in gates)</p>
<p><strong>Output:</strong> Task-dependent</p>
<p>Tanh's zero-centering helps with gradient flow over long sequences.</p>
</div>
<h3>Transformers (LLMs, Modern)</h3>
<div class="success-box">
<p><strong>Hidden layers:</strong> GELU or SwiGLU</p>
<p><strong>Output:</strong> Softmax (next-token prediction)</p>
<p>GELU is the modern standard for state-of-the-art models (GPT, BERT, etc.)</p>
</div>
<h3>Autoencoders</h3>
<div class="success-box">
<p><strong>Match output activation to data range:</strong></p>
<p>• Images [0,1]: Sigmoid</p>
<p>• Normalized data [-1,1]: Tanh</p>
<p>• Unbounded: Linear</p>
</div>"""
    },
    {
        "title": "Practical Debugging Guide",
        "body": """<h3>Problem: Training Loss Doesn't Decrease</h3>
<div class="warning-box">
<p><strong>Likely cause:</strong> Using sigmoid/tanh in a deep network → vanishing gradients</p>
<p><strong>Fix:</strong> Switch to ReLU. If still stuck, add batch normalization or layer normalization.</p>
</div>
<h3>Problem: Many Neurons Output Zero</h3>
<div class="warning-box">
<p><strong>Likely cause:</strong> Dead ReLU neurons from high learning rate or poor initialization</p>
<p><strong>Fix:</strong> Reduce learning rate, switch to Leaky ReLU, or reinitialize weights.</p>
</div>
<h3>Problem: NaN or Inf in Outputs</h3>
<div class="warning-box">
<p><strong>Likely cause:</strong> Unbounded activations (ReLU, linear) with exploding values</p>
<p><strong>Fix:</strong> Add layer normalization, use activation bounds (Sigmoid/Tanh), or reduce learning rate.</p>
</div>
<h3>Quick Decision Flowchart</h3>
<div class="concept-box">
<p>1. Hidden layers? → Start with <strong>ReLU</strong></p>
<p>2. Training slow? → Try <strong>Leaky ReLU</strong> or <strong>GELU</strong></p>
<p>3. Binary output? → <strong>Sigmoid</strong></p>
<p>4. Multi-class output? → <strong>Softmax</strong></p>
<p>5. Regression? → <strong>Linear (none)</strong></p>
</div>"""
    }
]
