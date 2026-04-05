TITLE = "Momentum and Adaptive Methods"

SECTIONS = [
    {
        "id": "momentum_basics",
        "title": "Momentum: Adding Inertia",
        "body": """
        <div class="concept-box" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>Problem with vanilla GD:</strong> Oscillates in narrow valleys. Slow descent through flat regions.</p>
            <p><strong>Momentum solution:</strong> Accumulate velocity—past gradients influence future steps.</p>
            <p>$$m \\leftarrow \\beta m + \\nabla L(\\theta)$$</p>
            <p>$$\\theta \\leftarrow \\theta - \\alpha m$$</p>
            <p>where β ≈ 0.9 (typical momentum coefficient), m starts at 0.</p>
            <p><strong>Intuition:</strong> Like a ball rolling downhill—it builds speed in consistent directions.</p>
        </div>
        """
    },
    {
        "id": "nesterov_momentum",
        "title": "Nesterov Accelerated Gradient",
        "body": """
        <div class="worked-example" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>NAG:</strong> Look-ahead variant of momentum—evaluate gradient at θ - αm instead of θ.</p>
            <p>$$m \\leftarrow \\beta m + \\nabla L(\\theta - \\alpha m)$$</p>
            <p>$$\\theta \\leftarrow \\theta - \\alpha m$$</p>
            <p><strong>Benefit:</strong> Slightly better convergence in practice. Less oscillation, faster descent.</p>
            <p>Most modern optimizers (Adam, RMSprop) build on this idea of using past gradient information.</p>
        </div>
        """
    },
    {
        "id": "rmsprop_basics",
        "title": "RMSprop: Per-Parameter Adaptive Learning Rates",
        "body": """
        <div class="success-box" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>RMSprop (Root Mean Square Propagation):</strong> Adapt learning rate per parameter based on gradient history.</p>
            <p>$$s \\leftarrow \\beta s + (1 - \\beta) (\\nabla L(\\theta))^2$$</p>
            <p>$$\\theta \\leftarrow \\theta - \\alpha \\frac{\\nabla L(\\theta)}{\\sqrt{s + \\epsilon}}$$</p>
            <p><strong>Key idea:</strong> Parameters with large consistent gradients get smaller effective learning rates (via division by √s). Noisy parameters get larger rates.</p>
            <p><strong>Effect:</strong> Faster convergence than momentum alone. Handles varying gradient scales well.</p>
        </div>
        """
    },
    {
        "id": "adam_optimizer",
        "title": "Adam: Momentum + Adaptive Learning Rates",
        "body": """
        <div class="success-box" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>Adam (Adaptive Moment Estimation):</strong> Combines momentum (first moment) and RMSprop (second moment).</p>
            <p>$$m \\leftarrow \\beta_1 m + (1 - \\beta_1) \\nabla L(\\theta)$$ (momentum)</p>
            <p>$$s \\leftarrow \\beta_2 s + (1 - \\beta_2) (\\nabla L(\\theta))^2$$ (adaptive rate)</p>
            <p>$$\\theta \\leftarrow \\theta - \\alpha \\frac{m}{\\sqrt{s + \\epsilon}}$$</p>
            <p>Typical defaults: β₁ = 0.9, β₂ = 0.999, ε = 10⁻⁸.</p>
            <p><strong>Why Adam is popular:</strong> Works well across diverse problems with minimal tuning. Default optimizer in most frameworks.</p>
        </div>
        """
    }
]
