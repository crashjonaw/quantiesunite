TITLE = "SGD and Mini-Batch Gradient Descent"

SECTIONS = [
    {
        "id": "batch_gd",
        "title": "Batch Gradient Descent",
        "body": """
        <div class="concept-box" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>Batch GD:</strong> Compute gradient using the entire dataset.</p>
            <p>$$\\theta \\leftarrow \\theta - \\alpha \\nabla L(\\theta) = \\theta - \\alpha \\frac{1}{N} \\sum_{i=1}^{N} \\nabla l_i(\\theta)$$</p>
            <p><strong>Advantages:</strong> Stable, deterministic, follows true gradient direction.</p>
            <p><strong>Disadvantages:</strong> Expensive for large datasets. Must load all data into memory.</p>
        </div>
        """
    },
    {
        "id": "sgd_stochastic",
        "title": "Stochastic Gradient Descent (SGD)",
        "body": """
        <div class="worked-example" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>SGD:</strong> Update parameters using gradient from a single random sample.</p>
            <p>$$\\theta \\leftarrow \\theta - \\alpha \\nabla l_i(\\theta)$$</p>
            <p>where i is chosen uniformly at random from {1, …, N}.</p>
            <p><strong>Key insight:</strong> ∇lᵢ(θ) is a noisy estimate of the true gradient ∇L(θ), but unbiased in expectation.</p>
            <p><strong>Advantages:</strong> Fast iterations, memory-efficient, natural regularization from noise.</p>
            <p><strong>Disadvantages:</strong> High variance, noisier path to convergence.</p>
        </div>
        """
    },
    {
        "id": "minibatch_gd",
        "title": "Mini-Batch Gradient Descent",
        "body": """
        <div class="success-box" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>Mini-batch GD (most common):</strong> Update using gradient from a small batch B of samples.</p>
            <p>$$\\theta \\leftarrow \\theta - \\alpha \\frac{1}{|B|} \\sum_{i \\in B} \\nabla l_i(\\theta)$$</p>
            <p><strong>Typical batch sizes:</strong> 32, 64, 128, 256 samples.</p>
            <p><strong>Why mini-batch?</strong></p>
            <ul >
                <li>Balance: More stable than SGD, faster than full batch</li>
                <li>Hardware: Vectorized operations are efficient at modest batch sizes</li>
                <li>Generalization: Batch noise helps escape sharp minima</li>
            </ul>
        </div>
        """
    },
    {
        "id": "epoch_iteration",
        "title": "Epochs and Iterations",
        "body": """
        <div class="concept-box" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>Iteration:</strong> One gradient update using one mini-batch.</p>
            <p><strong>Epoch:</strong> One complete pass through the entire dataset.</p>
            <p><strong>Example:</strong> Dataset with 10,000 samples, batch size 100:</p>
            <ul >
                <li>100 iterations = 1 epoch</li>
                <li>Training for 10 epochs = 1,000 iterations</li>
            </ul>
            <p>We typically train for multiple epochs until loss plateaus or validation accuracy stops improving.</p>
        </div>
        """
    }
]
