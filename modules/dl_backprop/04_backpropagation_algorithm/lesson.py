TITLE = "Backpropagation Algorithm"

SECTIONS = [
    {
        "id": "algorithm_overview",
        "title": "Algorithm Overview",
        "body": """
<div class="concept-box formula-box">
    <h3 class="accent-heading">Backpropagation in Steps</h3>
    <p><strong>Goal:</strong> Compute ∂L/∂w for all weights in the network.</p>
    <ol>
        <li><strong>Forward pass:</strong> Compute and store all intermediate activations</li>
        <li><strong>Backward pass:</strong> Start from loss, apply chain rule layer-by-layer</li>
        <li><strong>Gradient accumulation:</strong> Sum gradients when multiple paths converge</li>
        <li><strong>Parameter update:</strong> Use computed gradients with optimizer (e.g., SGD, Adam)</li>
    </ol>
    <p style="font-size: 0.95em; margin-top: 12px;">This algorithm is efficient because gradients are computed in reverse topological order, reusing intermediate results.</p>
</div>
"""
    },
    {
        "id": "layer_wise_gradient_flow",
        "title": "Layer-wise Gradient Flow",
        "body": """
<div class="concept-box formula-box">
    <h3 class="accent-heading">General Gradient Computation</h3>
    <p>For a typical layer: output = activation(z), where z = W @ input + b</p>
    <p style="margin-top: 12px;">Gradients flow as:</p>
    <p>$$\\frac{\\partial L}{\\partial \\mathbf{z}} = \\frac{\\partial L}{\\partial \\text{output}} \\odot \\sigma'(\\mathbf{z})$$</p>
    <p style="margin-top: 12px;">$$\\frac{\\partial L}{\\partial \\mathbf{W}} = \\frac{\\partial L}{\\partial \\mathbf{z}} \\otimes \\mathbf{input}^T$$</p>
    <p style="margin-top: 12px;">$$\\frac{\\partial L}{\\partial \\mathbf{b}} = \\sum_i \\frac{\\partial L}{\\partial \\mathbf{z}_i}$$</p>
    <p style="font-size: 0.95em; margin-top: 12px;">where ⊙ denotes element-wise multiplication and ⊗ denotes outer product.</p>
</div>
"""
    },
    {
        "id": "pseudocode",
        "title": "Pseudocode",
        "body": """
<div class="worked-example formula-box">
    <h3 class="accent-heading">Algorithm Pseudocode</h3>
    <pre style="padding: 12px; border-radius: 4px; overflow-x: auto; font-size: 0.9em">
# Forward pass
activations = []
a = x_input
for layer in network.layers:
    a = layer.forward(a)
    activations.append(a)
loss = compute_loss(a, y_true)

# Backward pass
gradient = gradient_of_loss(y_true)  # ∂L/∂output
for i in range(len(network.layers)-1, -1, -1):
    layer = network.layers[i]
    prev_activation = activations[i-1]

    # Compute gradient w.r.t. z (pre-activation)
    dz = gradient * layer.activation_derivative()

    # Compute gradient w.r.t. weights and biases
    dW = dz @ prev_activation.T / batch_size
    db = mean(dz, axis=0)

    # Propagate gradient to previous layer
    gradient = layer.weights.T @ dz

    # Update parameters
    layer.weights -= learning_rate * dW
    layer.biases -= learning_rate * db
    </pre>
</div>
"""
    },
    {
        "id": "why_backprop_works",
        "title": "Why Backpropagation Works",
        "body": """
<div class="success-box formula-box">
    <h3 class="accent-heading">Efficiency and Correctness</h3>
    <p><strong>Correctness:</strong> Backprop is just the chain rule applied systematically to a computational graph.</p>
    <p><strong>Efficiency:</strong> Computing all gradients takes O(1) the cost of the forward pass, rather than O(parameters) separate forward passes (numerical differentiation).</p>
    <p style="margin-top: 12px;">This makes training large neural networks feasible. Without backprop, modern deep learning wouldn't exist.</p>
</div>
"""
    }
]
