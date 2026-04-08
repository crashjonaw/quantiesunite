TITLE = "Matrix Inverse"

SECTIONS = [
    {
        "title": "Invertibility and Existence",
        "body": """
        <div class="concept-box">
        <p><strong>Matrix Inverse Definition:</strong> For a square matrix \\(\\mathbf{A}\\), the inverse \\(\\mathbf{A}^{-1}\\) (if it exists) is a matrix such that:</p>
        <p>$$\\mathbf{A}\\mathbf{A}^{-1} = \\mathbf{A}^{-1}\\mathbf{A} = \\mathbf{I}$$</p>
        </div>

        <p><strong>When does an inverse exist?</strong> A square matrix \\(\\mathbf{A}\\) is <strong>invertible (nonsingular)</strong> if and only if:</p>
        <ul>
        <li>\\(\\det(\\mathbf{A}) \\neq 0\\), OR</li>
        <li>\\(\\text{rank}(\\mathbf{A}) = n\\) (full rank), OR</li>
        <li>The only solution to \\(\\mathbf{A}\\mathbf{x} = \\mathbf{0}\\) is \\(\\mathbf{x} = \\mathbf{0}\\)</li>
        </ul>

        <div class="success-box">
        <p><strong>Equivalence:</strong> These three conditions are equivalent for square matrices. If one holds, they all hold.</p>
        </div>

        <div class="warning-box">
        <p><strong>Not all square matrices are invertible:</strong> A singular (non-invertible) matrix has \\(\\det(\\mathbf{A}) = 0\\) and maps some non-zero vector to zero. Its inverse doesn't exist.</p>
        </div>
        """
    },
    {
        "title": "Computing the Inverse",
        "body": """
        <p><strong>Methods for computing the inverse:</strong></p>
        <ol>
        <li><strong>Gauss-Jordan elimination:</strong> Form \\([\\mathbf{A} \\mid \\mathbf{I}]\\) and reduce to \\([\\mathbf{I} \\mid \\mathbf{A}^{-1}]\\)</li>
        <li><strong>Adjugate formula:</strong> \\(\\mathbf{A}^{-1} = \\frac{1}{\\det(\\mathbf{A})} \\cdot \\text{adj}(\\mathbf{A})\\) (practical only for small matrices)</li>
        <li><strong>LU decomposition:</strong> Factor \\(\\mathbf{A} = \\mathbf{LU}\\), then solve column-by-column</li>
        </ol>

        <div class="worked-example">
        <p><strong>Example: Find \\(\\mathbf{A}^{-1}\\) using Gauss-Jordan</strong></p>
        <p>$$\\mathbf{A} = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}$$</p>
        <p>Form \\([\\mathbf{A} \\mid \\mathbf{I}]\\):</p>
        <p>$$\\left(\\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\\\ 3 & 4 & 0 & 1 \\end{array}\\right)$$</p>
        <p>\\(R_2 - 3R_1 \\to R_2\\):</p>
        <p>$$\\left(\\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\\\ 0 & -2 & -3 & 1 \\end{array}\\right)$$</p>
        <p>\\(R_2 / (-2) \\to R_2\\):</p>
        <p>$$\\left(\\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\\\ 0 & 1 & \\frac{3}{2} & -\\frac{1}{2} \\end{array}\\right)$$</p>
        <p>\\(R_1 - 2R_2 \\to R_1\\):</p>
        <p>$$\\left(\\begin{array}{cc|cc} 1 & 0 & -2 & 1 \\\\ 0 & 1 & \\frac{3}{2} & -\\frac{1}{2} \\end{array}\\right)$$</p>
        <p>$$\\therefore \\mathbf{A}^{-1} = \\begin{pmatrix} -2 & 1 \\\\ \\frac{3}{2} & -\\frac{1}{2} \\end{pmatrix}$$</p>
        <p>Verify: \\(\\mathbf{A}\\mathbf{A}^{-1} = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}\\begin{pmatrix} -2 & 1 \\\\ \\frac{3}{2} & -\\frac{1}{2} \\end{pmatrix} = \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix}\\) ✓</p>
        </div>
        """
    },
    {
        "title": "Properties and Practical Notes",
        "body": """
        <p><strong>Properties of inverses:</strong></p>
        <ul>
        <li>\\((\\mathbf{A}^{-1})^{-1} = \\mathbf{A}\\)</li>
        <li>\\((\\mathbf{AB})^{-1} = \\mathbf{B}^{-1}\\mathbf{A}^{-1}\\) (order reverses!)</li>
        <li>\\((\\mathbf{A}^T)^{-1} = (\\mathbf{A}^{-1})^T\\)</li>
        <li>\\((c\\mathbf{A})^{-1} = \\frac{1}{c}\\mathbf{A}^{-1}\\) for scalar \\(c \\neq 0\\)</li>
        <li>\\(\\det(\\mathbf{A}^{-1}) = \\frac{1}{\\det(\\mathbf{A})}\\)</li>
        </ul>

        <div class="warning-box">
        <p><strong>Numerical stability:</strong> Computing explicit inverses can be numerically unstable. For solving \\(\\mathbf{Ax} = \\mathbf{b}\\), it's better to use Gaussian elimination or LU decomposition directly rather than computing \\(\\mathbf{A}^{-1}\\) and multiplying.</p>
        </div>

        <div class="success-box">
        <p><strong>Practical insight:</strong> To solve \\(\\mathbf{Ax} = \\mathbf{b}\\):</p>
        <ol>
        <li><strong>Avoid:</strong> \\(\\mathbf{x} = \\mathbf{A}^{-1}\\mathbf{b}\\) (unstable, expensive)</li>
        <li><strong>Prefer:</strong> Gaussian elimination (stable, \\(O(n^3)\\))</li>
        <li><strong>For multiple b:</strong> Use LU decomposition once, then solve efficiently</li>
        </ol>
        </div>
        """
    }
]
