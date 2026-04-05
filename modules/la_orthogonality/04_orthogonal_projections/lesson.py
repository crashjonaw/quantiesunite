TITLE = "Orthogonal Projections"

SECTIONS = [
    {
        "title": "Projection onto a Vector",
        "body": """
        <p><strong>Definition:</strong> The orthogonal projection of vector $\\mathbf{v}$ onto a nonzero vector $\\mathbf{u}$ is:</p>

        <div class='concept-box'>
        $$\\text{proj}_\\mathbf{u}(\\mathbf{v}) = \\frac{\\mathbf{v} \\cdot \\mathbf{u}}{||\\mathbf{u}||^2} \\mathbf{u}$$
        </div>

        <p><strong>Geometric Interpretation:</strong> This is the "shadow" of $\\mathbf{v}$ cast onto the line through $\\mathbf{u}$. The projection:</p>
        <ul>
        <li>Lies on the line through $\\mathbf{u}$</li>
        <li>Is closest to $\\mathbf{v}$ among all points on that line</li>
        <li>Is obtained by scaling $\\mathbf{u}$ by the dot product ratio</li>
        </ul>

        <p><strong>The Perpendicular Component:</strong> After projection, the "leftover" part is orthogonal to $\\mathbf{u}$:</p>

        <div class='concept-box'>
        $$\\mathbf{v}_{\\perp} = \\mathbf{v} - \\text{proj}_\\mathbf{u}(\\mathbf{v})$$
        </div>

        <p>We can always decompose: $\\mathbf{v} = \\text{proj}_\\mathbf{u}(\\mathbf{v}) + \\mathbf{v}_{\\perp}$ where $\\mathbf{v}_{\\perp} \\perp \\mathbf{u}$.</p>

        <div class='worked-example'>
        <p><strong>Example:</strong> Project $\\mathbf{v} = [3, 4]$ onto $\\mathbf{u} = [1, 0]$.</p>
        <pre>proj_u(v) = (v · u / ||u||²) u
           = (3 · 1 + 4 · 0) / (1² + 0²) [1, 0]
           = 3 / 1 [1, 0]
           = [3, 0]

Perpendicular: v_⊥ = [3, 4] - [3, 0] = [0, 4]

Check: [3, 0] · [0, 4] = 0 ✓ (orthogonal)</pre>
        </div>
        """
    },
    {
        "title": "Projection onto a Subspace",
        "body": """
        <p><strong>General Case:</strong> If $W$ is a subspace with orthonormal basis $\\{\\mathbf{u}_1, \\mathbf{u}_2, \\ldots, \\mathbf{u}_k\\}$, the orthogonal projection of $\\mathbf{v}$ onto $W$ is:</p>

        <div class='concept-box'>
        $$\\text{proj}_W(\\mathbf{v}) = (\\mathbf{v} \\cdot \\mathbf{u}_1)\\mathbf{u}_1 + (\\mathbf{v} \\cdot \\mathbf{u}_2)\\mathbf{u}_2 + \\cdots + (\\mathbf{v} \\cdot \\mathbf{u}_k)\\mathbf{u}_k$$
        </div>

        <p><strong>With Non-Orthonormal Basis:</strong> If the basis is orthogonal but not orthonormal, use:</p>

        <div class='concept-box'>
        $$\\text{proj}_W(\\mathbf{v}) = \\sum_{i=1}^{k} \\frac{\\mathbf{v} \\cdot \\mathbf{w}_i}{||\\mathbf{w}_i||^2} \\mathbf{w}_i$$
        </div>

        <p><strong>Key Properties:</strong></p>
        <ul>
        <li>$\\text{proj}_W(\\mathbf{v}) \\in W$ (the projection lies in the subspace)</li>
        <li>$\\mathbf{v} - \\text{proj}_W(\\mathbf{v}) \\in W^\\perp$ (the residual is orthogonal to $W$)</li>
        <li>$\\text{proj}_W(\\text{proj}_W(\\mathbf{v})) = \\text{proj}_W(\\mathbf{v})$ (projecting twice gives the same result)</li>
        <li>$||\\text{proj}_W(\\mathbf{v})||^2 + ||\\mathbf{v} - \\text{proj}_W(\\mathbf{v})||^2 = ||\\mathbf{v}||^2$ (Pythagorean theorem)</li>
        </ul>

        <p><strong>Geometric Insight:</strong> The projection is the point in $W$ closest to $\\mathbf{v}$. If you're looking for the best approximation to $\\mathbf{v}$ using elements of $W$, orthogonal projection gives it.</p>

        <div class='worked-example'>
        <p><strong>Example:</strong> Project $\\mathbf{v} = [1, 1, 1]$ onto the subspace $W$ spanned by $\\mathbf{u}_1 = [1, 0, 0]$ and $\\mathbf{u}_2 = [0, 1, 0]$ (the $xy$-plane).</p>
        <pre>Orthonormal basis: {[1, 0, 0], [0, 1, 0]}

proj_W(v) = (v · u₁)u₁ + (v · u₂)u₂
          = 1·[1, 0, 0] + 1·[0, 1, 0]
          = [1, 1, 0]

Residual: v - proj_W(v) = [1, 1, 1] - [1, 1, 0] = [0, 0, 1]

Check orthogonality:
[1, 1, 0] · [0, 0, 1] = 0 ✓</pre>
        </div>
        """
    },
    {
        "title": "Best Approximation and Distance to Subspaces",
        "body": """
        <p><strong>Best Approximation Theorem:</strong> For a subspace $W$ and any vector $\\mathbf{v}$, the orthogonal projection $\\text{proj}_W(\\mathbf{v})$ minimizes the distance to $W$:</p>

        <div class='concept-box'>
        $$||\\mathbf{v} - \\text{proj}_W(\\mathbf{v})|| = \\min_{\\mathbf{w} \\in W} ||\\mathbf{v} - \\mathbf{w}||$$
        </div>

        <p>In other words, among all vectors in $W$, the projection is the closest to $\\mathbf{v}$.</p>

        <p><strong>Distance Formula:</strong> The distance from $\\mathbf{v}$ to the subspace $W$ is:</p>

        <div class='concept-box'>
        $$d(\\mathbf{v}, W) = ||\\mathbf{v} - \\text{proj}_W(\\mathbf{v})||$$
        </div>

        <p><strong>Why This Matters:</strong> In applications, we often want the best approximation to some quantity using available constraints. Projection provides this automatically.</p>

        <p><strong>Applications:</strong></p>
        <ul>
        <li><strong>Data compression:</strong> Project data onto lower-dimensional subspace</li>
        <li><strong>Denoising:</strong> Remove noise by projecting onto a "clean" subspace</li>
        <li><strong>Constraint satisfaction:</strong> Find the point in a subspace closest to a target</li>
        </ul>

        <div class='success-box'>
        <p><strong>Fundamental Principle:</strong> Orthogonal projection solves many "best fit" problems. Whenever you want the best approximation subject to constraints that form a subspace, use projection.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example:</strong> Find the distance from $\\mathbf{v} = [1, 1, 1]$ to the line through $\\mathbf{u} = [1, 0, 0]$.</p>
        <pre>proj_u(v) = (v · u / ||u||²) u = (1 / 1) [1, 0, 0] = [1, 0, 0]

Distance: ||v - proj_u(v)|| = ||[1, 1, 1] - [1, 0, 0]||
                             = ||[0, 1, 1]||
                             = √(0² + 1² + 1²)
                             = √2</pre>
        </div>
        """
    }
]
