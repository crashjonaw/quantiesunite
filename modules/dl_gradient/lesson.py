SECTIONS = [
    {"id": "gd_loss_surface", "title": "The Loss Surface & Optimization Landscape", "content": '<p>Given parameters \\(\\theta = (w_1, \\ldots, w_n, b)\\), the loss function \\(L(\\theta)\\) measures prediction error.</p><p>$$L(\\theta) = \\frac{1}{N} \\sum_{i=1}^{N} l(f_\\theta(x_i), y_i)$$</p>'},
    {"id": "gd_derivatives", "title": "Partial Derivatives and Gradient Vector", "content": '<p>$$\\nabla L = \\begin{bmatrix} \\frac{\\partial L}{\\partial w_1} \\\\ \\vdots \\\\ \\frac{\\partial L}{\\partial b} \\end{bmatrix}$$</p>'},
    {"id": "gd_algorithm", "title": "Gradient Descent Update Rule", "content": '<p>$$\\theta \\leftarrow \\theta - \\alpha \\nabla L(\\theta)$$</p><p>where \\(\\alpha\\) is the learning rate.</p>'},
    {"id": "gd_convergence", "title": "Convergence Guarantees & Local Minima", "content": '<p>For convex losses, GD converges to global minimum. For nonconvex (neural nets), converges to critical points.</p>'},
    {"id": "gd_variants", "title": "Momentum and Adaptive Learning Rates", "content": '<p>Momentum: $$\\theta \\leftarrow \\theta - \\alpha m + m \\leftarrow \\beta m + \\nabla L$$</p>'},
    {"id": "gd_learning_rates", "title": "Learning Rate Selection and Scheduling", "content": '<p>Learning rate \\(\\alpha\\) critically affects convergence. Too small: slow. Too large: divergence.</p>'}
]