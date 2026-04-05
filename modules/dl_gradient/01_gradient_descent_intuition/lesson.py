TITLE = "Gradient Descent Intuition"

SECTIONS = [
    {
        "id": "gd_loss_surface",
        "title": "The Loss Surface & Optimization Landscape",
        "body": """
        <div class="concept-box" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p>Given parameters θ = (w₁, …, wₙ, b), the loss function L(θ) measures prediction error across the entire dataset.</p>
            <p>$$L(\\theta) = \\frac{1}{N} \\sum_{i=1}^{N} l(f_\\theta(x_i), y_i)$$</p>
            <p><strong>Key insight:</strong> The loss surface is high-dimensional. Our goal is to find the valley (minimum) in this landscape.</p>
        </div>
        """
    },
    {
        "id": "gd_derivatives",
        "title": "Partial Derivatives and Gradient Vector",
        "body": """
        <div class="concept-box" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p>The gradient vector points in the direction of steepest ascent of the loss function.</p>
            <p>$$\\nabla L = \\begin{bmatrix} \\frac{\\partial L}{\\partial w_1} \\\\ \\vdots \\\\ \\frac{\\partial L}{\\partial b} \\end{bmatrix}$$</p>
            <p><strong>First principles:</strong> Each partial derivative tells us how much the loss changes when we adjust that parameter slightly.</p>
        </div>
        """
    },
    {
        "id": "gd_algorithm",
        "title": "Gradient Descent Update Rule",
        "body": """
        <div class="worked-example" style="padding: 16px; margin: 12px 0; border-radius: 6px">
            <p>To minimize loss, move opposite the gradient direction:</p>
            <p>$$\\theta \\leftarrow \\theta - \\alpha \\nabla L(\\theta)$$</p>
            <p>where α (alpha) is the learning rate—controlling step size.</p>
            <p><strong>Intuition:</strong> Like descending a hill by always stepping downward. The gradient shows us which way is down.</p>
        </div>
        """
    },
    {
        "id": "gd_convergence",
        "title": "Convergence Guarantees & Local Minima",
        "body": """
        <div class="warning-box" style="border-left: 4px solid #fd7e14; padding: 16px; margin: 12px 0; border-radius: 6px">
            <p><strong>For convex losses:</strong> GD converges to the global minimum—guaranteed.</p>
            <p><strong>For nonconvex losses (neural networks):</strong> GD converges to a critical point, which may be a local minimum, saddle point, or plateau.</p>
            <p>Despite this, GD often finds surprisingly good solutions in practice for deep learning.</p>
        </div>
        """
    }
]
