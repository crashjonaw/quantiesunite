TITLE = "Learning Rate and Convergence"

SECTIONS = [
    {
        "id": "lr_impact",
        "title": "Learning Rate: The Critical Hyperparameter",
        "body": """
        <div class="concept-box" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>Learning rate α:</strong> Controls the step size in the gradient descent update.</p>
            <p>$$\\theta \\leftarrow \\theta - \\alpha \\nabla L(\\theta)$$</p>
            <p>From first principles: α multiplies the gradient. Small α = small steps. Large α = large steps.</p>
            <p><strong>The goldilocks zone:</strong> We need α "just right"—not too small, not too large.</p>
        </div>
        """
    },
    {
        "id": "lr_too_small",
        "title": "Too Small Learning Rate",
        "body": """
        <div class="warning-box" style="border-left: 4px solid #fd7e14; padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>Problem:</strong> Extremely slow convergence.</p>
            <ul >
                <li>Steps are tiny, requiring thousands of iterations</li>
                <li>Training becomes impractical (computational cost)</li>
                <li>May get stuck in plateaus due to numerical precision limits</li>
            </ul>
            <p><strong>Example:</strong> α = 10⁻⁸ on a problem that needs α = 10⁻³.</p>
        </div>
        """
    },
    {
        "id": "lr_too_large",
        "title": "Too Large Learning Rate",
        "body": """
        <div class="warning-box" style="border-left: 4px solid #fd7e14; padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>Problem:</strong> Divergence or wild oscillation.</p>
            <ul >
                <li>Steps overshoot the minimum, bouncing across the valley</li>
                <li>Loss can explode (NaN, infinity)</li>
                <li>Training crashes or produces useless parameters</li>
            </ul>
            <p><strong>Example:</strong> α = 1.0 on a problem that needs α = 10⁻³.</p>
        </div>
        """
    },
    {
        "id": "lr_convergence_analysis",
        "title": "Convergence Rate and Conditions",
        "body": """
        <div class="worked-example" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>For quadratic loss:</strong> Convergence rate depends on eigenvalues of the Hessian (second derivative matrix).</p>
            <p>Optimal learning rate: $$\\alpha_{opt} = \\frac{2}{\\lambda_{max} + \\lambda_{min}}$$</p>
            <p>In practice: Learning rates in [0.001, 0.1] work for many problems. Start with α = 0.01 and adjust.</p>
            <p><strong>Key takeaway:</strong> The loss should decrease monotonically (or nearly so). If it spikes up, reduce α.</p>
        </div>
        """
    }
]
