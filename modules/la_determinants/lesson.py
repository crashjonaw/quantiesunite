SECTIONS = [
    {
        "title": "Determinants of 2×2 and 3×3 Matrices",
        "body": """
        <p>The <strong>determinant</strong> of a square matrix is a single number that encodes crucial information about the matrix: invertibility, eigenvalues, volume scaling, and more.</p>

        <p><strong>2×2 Determinant:</strong> For a matrix A = [[a, b], [c, d]], the determinant is:</p>
        <pre class='code-block'>det(A) = ad - bc</pre>

        <p>This is the area of the parallelogram spanned by the column vectors [a, c] and [b, d].</p>

        <p><strong>3×3 Determinant (Sarrus' rule or cofactor expansion):</strong> For A = [[a, b, c], [d, e, f], [g, h, i]]:</p>
        <pre class='code-block'>det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)</pre>

        <p>This can be computed as:</p>
        <pre class='code-block'>det(A) = a·det([e, f], [h, i]) - b·det([d, f], [g, i]) + c·det([d, e], [g, h])</pre>

        <p>Expanding along the first row. Notice the pattern of signs: +, -, +, -, ... (alternating checkerboard pattern).</p>

        <div class='example-box'>
        <p><strong>Example: 2×2 determinant</strong></p>
        <pre class='code-block'>A = [3  2]
    [1  4]

det(A) = 3·4 - 2·1 = 12 - 2 = 10</pre>

        <p><strong>Example: 3×3 determinant</strong></p>
        <pre class='code-block'>A = [1  2  3]
    [0  4  5]
    [1  0  6]

det(A) = 1·det([4, 5], [0, 6]) - 2·det([0, 5], [1, 6]) + 3·det([0, 4], [1, 0])
       = 1·(4·6 - 5·0) - 2·(0·6 - 5·1) + 3·(0·0 - 4·1)
       = 1·24 - 2·(-5) + 3·(-4)
       = 24 + 10 - 12
       = 22</pre>
        </div>

        <p><strong>Geometric interpretation:</strong> The absolute value of the determinant is the volume of the parallelepiped (3D) or parallelogram (2D) spanned by the column vectors. The sign indicates orientation (whether the transformation preserves or reverses orientation).</p>

        <p><strong>Key fact:</strong> det(A) = 0 if and only if the columns are linearly dependent (the matrix is singular/non-invertible). If det(A) ≠ 0, the matrix is invertible.</p>
        """
    },
    {
        "title": "Cofactor Expansion and General n×n Determinants",
        "body": """
        <p><strong>Minors and Cofactors:</strong> For an n × n matrix A:</p>

        <p><strong>Minor Mᵢⱼ:</strong> The determinant of the (n-1) × (n-1) submatrix obtained by deleting row i and column j.</p>

        <p><strong>Cofactor Cᵢⱼ:</strong> The signed minor: Cᵢⱼ = (-1)^(i+j) Mᵢⱼ. The sign alternates in a checkerboard pattern.</p>

        <p><strong>Cofactor Expansion (Laplace Expansion):</strong> The determinant of A can be computed by expanding along any row or column:</p>
        <pre class='code-block'>Expanding along row i:
det(A) = Σⱼ aᵢⱼ Cᵢⱼ = Σⱼ aᵢⱼ (-1)^(i+j) Mᵢⱼ

Expanding along column j:
det(A) = Σᵢ aᵢⱼ Cᵢⱼ = Σᵢ aᵢⱼ (-1)^(i+j) Mᵢⱼ</pre>

        <p><strong>Why this matters:</strong> Cofactor expansion reduces an n × n determinant to n determinants of size (n-1) × (n-1), which can be computed recursively.</p>

        <p><strong>Computational complexity:</strong> For a general n × n matrix, cofactor expansion has O(n!) complexity—impractical for large n. Gaussian elimination is O(n³) and preferred.</p>

        <div class='example-box'>
        <p><strong>Example: Cofactor expansion along the first row</strong></p>
        <pre class='code-block'>A = [1  0  2]
    [3  1  4]
    [2  1  3]

det(A) = 1·M₁₁ - 0·M₁₂ + 2·M₁₃

M₁₁ = det([1, 4], [1, 3]) = 1·3 - 4·1 = -1
M₁₃ = det([3, 1], [2, 1]) = 3·1 - 1·2 = 1

det(A) = 1·(-1) - 0 + 2·(1) = -1 + 2 = 1</pre>
        </div>

        <p><strong>Adjugate matrix:</strong> The matrix of cofactors (transposed) is called the adjugate (or adjoint) matrix:</p>
        <pre class='code-block'>adj(A) = [C₁₁  C₂₁  ...  Cₙ₁]ᵀ
            [C₁₂  C₂₂  ...  Cₙ₂]
            [...  ...  ...  ...]
            [C₁ₙ  C₂ₙ  ...  Cₙₙ]</pre>

        <p>This is used in the inverse formula: A⁻¹ = (1/det(A)) · adj(A) (practical only for small matrices).</p>
        """
    },
    {
        "title": "Properties of Determinants and Row Operations",
        "body": """
        <p><strong>Fundamental properties of determinants:</strong></p>

        <p><strong>1. Multiplicativity:</strong> det(AB) = det(A)·det(B). For square matrices, the determinant of a product is the product of determinants.</p>

        <p><strong>2. Transpose:</strong> det(Aᵀ) = det(A). The determinant of the transpose equals the original.</p>

        <p><strong>3. Invertibility:</strong> A is invertible iff det(A) ≠ 0. And det(A⁻¹) = 1/det(A).</p>

        <p><strong>4. Determinant of scalar multiple:</strong> det(cA) = cⁿ·det(A) for an n × n matrix (each of n rows is scaled).</p>

        <p><strong>Effect of row operations on determinant:</strong></p>

        <ul>
        <li><strong>Row swap (Rᵢ ↔ Rⱼ):</strong> det → -det (sign change)</li>
        <li><strong>Row scaling (cRᵢ → Rᵢ):</strong> det → c·det (multiply by scalar c)</li>
        <li><strong>Row addition (Rᵢ + cRⱼ → Rᵢ):</strong> det → det (unchanged)</li>
        </ul>

        <p><strong>Why this matters for Gaussian elimination:</strong> When converting A to REF via row operations, we can track the determinant. If A is row-reduced to an upper triangular U, then:</p>
        <pre class='code-block'>det(A) = (sign factor) × (product of diagonal entries of U)</pre>

        <p>The sign factor accounts for row swaps (each swap multiplies by -1).</p>

        <div class='example-box'>
        <p><strong>Example: Computing determinant via row reduction</strong></p>
        <pre class='code-block'>A = [2  4  1]
    [0  3  2]
    [1  1  1]

R₁ ↔ R₃ (row swap, so det → -det):
[1  1  1]
[0  3  2]
[2  4  1]

R₃ - 2R₁ → R₃:
[1  1  1]
[0  3  2]
[0  2 -1]

R₂ ↔ R₃ (row swap, so det → -det again, total -(-1) = +1):
[1  1  1]
[0  2 -1]
[0  3  2]

R₃ - (3/2)R₂ → R₃:
[1  1  1]
[0  2 -1]
[0  0 7/2]

The matrix is now upper triangular.
det(upper triangular) = 1·2·(7/2) = 7
Accounting for row swaps: det(A) = (-1)² · 7 = 7</pre>
        </div>

        <p><strong>Special matrices:</strong></p>
        <ul>
        <li><strong>Identity matrix I:</strong> det(I) = 1</li>
        <li><strong>Diagonal matrix:</strong> det(diag(d₁, ..., dₙ)) = d₁·d₂·...·dₙ (product of diagonal entries)</li>
        <li><strong>Triangular matrix:</strong> det = product of diagonal entries</li>
        <li><strong>Singular matrix:</strong> det(A) = 0 (not invertible)</li>
        </ul>
        """
    },
    {
        "title": "Cramer's Rule and Applications",
        "body": """
        <p><strong>Cramer's Rule:</strong> For a system Ax = b where A is n × n and det(A) ≠ 0 (unique solution), the solution is:</p>
        <pre class='code-block'>xⱼ = det(Aⱼ) / det(A)</pre>

        <p>where Aⱼ is the matrix obtained by replacing the j-th column of A with the vector b.</p>

        <p><strong>When to use Cramer's Rule:</strong></p>
        <ul>
        <li><strong>Advantage:</strong> Elegant formula; useful for theoretical work and small systems (n ≤ 3).</li>
        <li><strong>Disadvantage:</strong> Computationally expensive for large n (requires n+1 determinant computations). Gaussian elimination is O(n³) vs. Cramer's O(n!) with cofactor expansion.</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Solve using Cramer's Rule</strong></p>
        <pre class='code-block'>System: 2x + y = 5
        x - y = 1

A = [2  1]    b = [5]
    [1 -1]        [1]

det(A) = 2(-1) - 1(1) = -3

A₁ (replace column 1 with b):
A₁ = [5  1]
     [1 -1]
det(A₁) = 5(-1) - 1(1) = -6

x = det(A₁)/det(A) = -6/(-3) = 2

A₂ (replace column 2 with b):
A₂ = [2  5]
     [1  1]
det(A₂) = 2(1) - 5(1) = -3

y = det(A₂)/det(A) = -3/(-3) = 1

Solution: (x, y) = (2, 1)</pre>
        </div>

        <p><strong>Applications of determinants:</strong></p>
        <ul>
        <li><strong>Volume and area:</strong> |det(A)| is the volume scaling factor of the linear transformation x ↦ Ax.</li>
        <li><strong>Change of variables in integrals:</strong> ∫ f(Ax) dx = (1/|det(A)|) ∫ f(x) dx (Jacobian determinant).</li>
        <li><strong>Characteristic polynomial:</strong> det(A - λI) = 0 determines eigenvalues of A.</li>
        <li><strong>Stability analysis:</strong> Determinant of Jacobian matrix indicates stability of equilibria in dynamical systems.</li>
        </ul>
        """
    },
    {
        "title": "Connection to Linear Independence and Rank",
        "body": """
        <p><strong>Determinant and linear independence:</strong> For a square matrix A:</p>
        <ul>
        <li><strong>det(A) ≠ 0 ⟺ columns are linearly independent ⟺ rank(A) = n</strong></li>
        <li><strong>det(A) = 0 ⟺ columns are linearly dependent ⟺ rank(A) < n</strong></li>
        </ul>

        <p>The same equivalences hold for rows (since det(Aᵀ) = det(A)).</p>

        <p><strong>Determinant as a measure of singularity:</strong> The determinant quantifies how close a matrix is to being singular. A small determinant (relative to matrix size) indicates near-singularity and potential numerical instability in computations.</p>

        <p><strong>Condition number and determinant:</strong> The condition number κ(A) = ||A|| · ||A⁻¹|| is not directly the determinant, but for well-scaled matrices, small |det(A)| often correlates with large κ(A), both indicating ill-conditioning.</p>

        <p><strong>Eigenvalue interpretation:</strong> For a matrix with eigenvalues λ₁, λ₂, ..., λₙ:</p>
        <pre class='code-block'>det(A) = λ₁ · λ₂ · ... · λₙ (product of eigenvalues)</pre>

        <p>So det(A) = 0 means at least one eigenvalue is 0.</p>

        <div class='example-box'>
        <p><strong>Example: Linear independence check using determinant</strong></p>
        <pre class='code-block'>Vectors v₁ = [1, 2], v₂ = [3, 6]

Form matrix A = [1  3]
              [2  6]

det(A) = 1(6) - 3(2) = 0

Since det(A) = 0, the vectors are linearly dependent.
Indeed: v₂ = 3v₁, so they're scalar multiples.</pre>

        <p><strong>Example: Eigenvalue product</strong></p>
        <pre class='code-block'>If A has eigenvalues λ₁ = 2, λ₂ = -3, λ₃ = 4, then:
det(A) = 2·(-3)·4 = -24</pre>
        </div>

        <p><strong>Summary:</strong> The determinant is a fundamental invariant that captures:</p>
        <ul>
        <li>Invertibility of the matrix</li>
        <li>Linear dependence of rows/columns</li>
        <li>Volume scaling of the linear transformation</li>
        <li>Product of eigenvalues</li>
        </ul>

        <p>It is one of the most important quantities in linear algebra, appearing in theory and applications across mathematics, physics, and engineering.</p>
        """
    }
]
