TITLE = "Forward and Backward Pass"

SECTIONS = [
    {
        "id": "forward_pass_definition",
        "title": "The Forward Pass",
        "body": """
<div class="concept-box formula-box">
    <h3 class="accent-heading">Forward Propagation</h3>
    <p>The forward pass computes the network's output and loss:</p>
    <ol>
        <li>Start with input data x</li>
        <li>Apply each layer's transformation sequentially</li>
        <li>Compute predictions ŷ</li>
        <li>Calculate loss L = Loss(ŷ, y_true)</li>
    </ol>
    <p style="font-size: 0.95em; margin-top: 12px;">The forward pass must be computed before the backward pass. All intermediate activations and values must be stored for use in backpropagation.</p>
</div>
"""
    },
    {
        "id": "backward_pass_definition",
        "title": "The Backward Pass",
        "body": """
<div class="concept-box formula-box">
    <h3 class="accent-heading">Backpropagation</h3>
    <p>The backward pass computes gradients with respect to all parameters:</p>
    <ol>
        <li>Start with ∂L/∂ŷ (gradient of loss w.r.t. output)</li>
        <li>Apply chain rule sequentially, layer by layer, going backward</li>
        <li>Compute ∂L/∂w for all weights and ∂L/∂b for all biases</li>
        <li>Optionally compute ∂L/∂x to pass to previous layers</li>
    </ol>
    <p style="font-size: 0.95em; margin-top: 12px;">Backprop efficiently reuses stored intermediate values from the forward pass.</p>
</div>
"""
    },
    {
        "id": "forward_backward_example",
        "title": "Complete Example",
        "body": """
<div class="worked-example formula-box">
    <h3 class="accent-heading">Two-Layer Network</h3>
    <p><strong>Network:</strong> x → [Linear+ReLU] → h → [Linear] → ŷ</p>
    <p><strong>Forward pass:</strong></p>
    <pre style="padding: 12px; border-radius: 4px; overflow-x: auto">
z1 = w1 @ x + b1
h = max(0, z1)          # ReLU activation
z2 = w2 @ h + b2
ŷ = z2                   # For simplicity, linear output
L = (ŷ - y_true)²
    </pre>
    <p><strong>Backward pass:</strong></p>
    <pre style="padding: 12px; border-radius: 4px; overflow-x: auto">
∂L/∂z2 = 2(ŷ - y_true)
∂L/∂w2 = (∂L/∂z2) @ h.T
∂L/∂h = w2.T @ (∂L/∂z2)
∂L/∂z1 = (∂L/∂h) ⊙ (z1 > 0)  # ReLU derivative
∂L/∂w1 = (∂L/∂z1) @ x.T
    </pre>
</div>
"""
    },
    {
        "id": "memory_and_efficiency",
        "title": "Memory and Efficiency",
        "body": """
<div class="warning-box formula-box">
    <h3 style="color: #f85149;">Important Considerations</h3>
    <p><strong>Memory cost:</strong> The forward pass stores activations for all layers. Deep networks can consume significant memory.</p>
    <p><strong>Trade-off:</strong> We can recompute activations during backprop instead of storing them (gradient checkpointing), trading compute for memory.</p>
    <p><strong>Time complexity:</strong> Backprop takes roughly the same time as one forward pass, making a training step ≈ 2× forward computation time.</p>
</div>
"""
    }
]
