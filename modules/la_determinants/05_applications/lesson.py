TITLE = "Applications and Connections to Linear Algebra"

SECTIONS = [
    {
        "title": "Geometric and Computational Applications",
        "body": """
        <p><strong>Applications of determinants:</strong></p>
        <ul>
        <li><strong>Volume and area:</strong> $|\\det(A)|$ is the volume scaling factor of the linear transformation $\\mathbf{x} \\mapsto A\\mathbf{x}$.</li>
        <li><strong>Change of variables in integrals:</strong> $\\int f(A\\mathbf{x})\\, d\\mathbf{x} = \\frac{1}{|\\det(A)|} \\int f(\\mathbf{x})\\, d\\mathbf{x}$ (Jacobian determinant).</li>
        <li><strong>Characteristic polynomial:</strong> $\\det(A - \\lambda I) = 0$ determines eigenvalues of $A$.</li>
        <li><strong>Stability analysis:</strong> Determinant of Jacobian matrix indicates stability of equilibria in dynamical systems.</li>
        </ul>

        <div class='concept-box'>
        <p><strong>Determinant as Volume Scaling:</strong></p>
        <p>For a linear transformation $T(\\mathbf{x}) = A\\mathbf{x}$, the determinant $|\\det(A)|$ gives the factor by which $T$ scales volumes of regions in $\\mathbb{R}^n$.</p>
        </div>
        """
    },
    {
        "title": "Linear Independence and Eigenvalue Product",
        "body": """
        <p><strong>Determinant and linear independence:</strong> For a square matrix $A$:</p>
        <ul>
        <li><strong>$\\det(A) \\neq 0 \\iff$ columns are linearly independent $\\iff \\text{rank}(A) = n$</strong></li>
        <li><strong>$\\det(A) = 0 \\iff$ columns are linearly dependent $\\iff \\text{rank}(A) < n$</strong></li>
        </ul>

        <p>The same equivalences hold for rows (since $\\det(A^T) = \\det(A)$).</p>

        <p><strong>Eigenvalue interpretation:</strong> For a matrix with eigenvalues $\\lambda_1, \\lambda_2, \\ldots, \\lambda_n$:</p>
        <p>$$\\det(A) = \\lambda_1 \\cdot \\lambda_2 \\cdot \\ldots \\cdot \\lambda_n \\quad \\text{(product of eigenvalues)}$$</p>

        <p>So $\\det(A) = 0$ means at least one eigenvalue is $0$.</p>

        <div class='worked-example'>
        <p><strong>Example: Linear independence check using determinant</strong></p>
        <pre class='code-block'>Vectors $\\mathbf{v}_1 = [1, 2]$, $\\mathbf{v}_2 = [3, 6]$

Form matrix $$A = \\begin{bmatrix} 1 & 3 \\\\ 2 & 6 \\end{bmatrix}$$

$$\\det(A) = 1(6) - 3(2) = 0$$

Since $\\det(A) = 0$, the vectors are linearly dependent.
Indeed: $\\mathbf{v}_2 = 3\\mathbf{v}_1$, so they're scalar multiples.</pre>

        <p><strong>Example: Eigenvalue product</strong></p>
        <pre class='code-block'>If $A$ has eigenvalues $\\lambda_1 = 2$, $\\lambda_2 = -3$, $\\lambda_3 = 4$, then:
$$\\det(A) = 2 \\cdot (-3) \\cdot 4 = -24$$</pre>
        </div>

        <p><strong>Determinant and matrix condition:</strong> The determinant quantifies how close a matrix is to being singular. A small determinant (relative to matrix size) indicates near-singularity and potential numerical instability in computations.</p>

        <div class='concept-box'>
        <p><strong>Summary: Key Roles of the Determinant</strong></p>
        <ul>
        <li>Invertibility of the matrix</li>
        <li>Linear dependence of rows/columns</li>
        <li>Volume scaling of the linear transformation</li>
        <li>Product of eigenvalues</li>
        <li>Indicator of numerical stability and conditioning</li>
        </ul>

        <p>The determinant is one of the most important quantities in linear algebra, appearing in theory and applications across mathematics, physics, and engineering.</p>
        </div>
        """
    }
]
