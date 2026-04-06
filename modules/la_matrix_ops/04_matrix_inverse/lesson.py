TITLE = "Matrix Inverse"

SECTIONS = [
    {
        "title": "Invertibility and Existence",
        "body": """
        <div class="concept-box">
        <p><strong>Matrix Inverse Definition:</strong> For a square matrix A, the inverse A⁻¹ (if it exists) is a matrix such that:</p>
        <div class="code-block">AA⁻¹ = A⁻¹A = I</div>
        </div>

        <p><strong>When does an inverse exist?</strong> A square matrix A is <strong>invertible (nonsingular)</strong> if and only if:</p>
        <ul>
        <li>\(\det(A) \neq 0\), OR</li>
        <li>\(\text{rank}(A) = n\) (full rank), OR</li>
        <li>The only solution to Ax = 0 is x = 0 (A has trivial nullspace)</li>
        </ul>

        <div class="success-box">
        <p><strong>Equivalence:</strong> These three conditions are equivalent for square matrices. If one holds, they all hold.</p>
        </div>

        <div class="warning-box">
        <p><strong>Not all square matrices are invertible:</strong> A singular (non-invertible) matrix has \(\det(A) = 0\) and maps some non-zero vector to zero. Its inverse doesn't exist.</p>
        </div>
        """
    },
    {
        "title": "Computing the Inverse",
        "body": """
        <p><strong>Methods for computing the inverse:</strong></p>
        <ol>
        <li><strong>Gauss-Jordan elimination:</strong> Form [A | I] and reduce to [I | A⁻¹]</li>
        <li><strong>Adjugate formula:</strong> A⁻¹ = (1/det(A)) · adj(A) (practical only for small matrices)</li>
        <li><strong>LU decomposition:</strong> Factor A = LU, solve LA⁻¹ = U⁻¹ (or compute column-by-column)</li>
        </ol>

        <div class="worked-example">
        <p><strong>Example: Find A⁻¹ using Gauss-Jordan</strong></p>
        <div class="code-block">A = [1  2]
    [3  4]

Form [A | I]:
[1  2 | 1  0]
[3  4 | 0  1]

R₂ - 3R₁ → R₂:
[1  2 | 1  0]
[0 -2 | -3 1]

R₂ / (-2) → R₂:
[1  2 | 1   0]
[0  1 | 3/2 -1/2]

R₁ - 2R₂ → R₁:
[1  0 | -2   1]
[0  1 | 3/2 -1/2]

Therefore, A⁻¹ = [-2    1  ]
                  [3/2 -1/2]

Verify: AA⁻¹ = [1  2][-2    1  ] = [1  0] ✓
              [3  4][3/2 -1/2]   [0  1]</div>
        </div>
        """
    },
    {
        "title": "Properties and Practical Notes",
        "body": """
        <p><strong>Properties of inverses:</strong></p>
        <ul>
        <li><strong>(A⁻¹)⁻¹ = A</strong></li>
        <li><strong>(AB)⁻¹ = B⁻¹A⁻¹</strong> (order reverses!)</li>
        <li><strong>(Aᵀ)⁻¹ = (A⁻¹)ᵀ</strong></li>
        <li><strong>\((cA)^{-1} = (1/c)A^{-1}\)</strong> for scalar \(c \neq 0\)</li>
        <li><strong>det(A⁻¹) = 1/det(A)</strong></li>
        </ul>

        <div class="warning-box">
        <p><strong>Numerical stability:</strong> Computing explicit inverses can be numerically unstable. For solving Ax = b, it's better to use Gaussian elimination or LU decomposition directly rather than computing A⁻¹ and multiplying.</p>
        </div>

        <div class="success-box">
        <p><strong>Practical insight:</strong> To solve Ax = b:</p>
        <ol>
        <li><strong>Avoid:</strong> x = A⁻¹b (unstable, expensive)</li>
        <li><strong>Prefer:</strong> Gaussian elimination (stable, \(O(n^3)\))</li>
        <li><strong>For multiple b:</strong> Use LU decomposition once, then solve efficiently</li>
        </ol>
        </div>
        """
    }
]
