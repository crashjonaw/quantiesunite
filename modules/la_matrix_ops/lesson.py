SECTIONS = [
    {
        "title": "Matrix Addition and Scalar Multiplication",
        "body": """
        <p><strong>Matrix Addition:</strong> Two matrices A and B of the same dimensions (m × n) can be added element-wise to produce a matrix C of the same dimension:</p>
        <pre class='code-block'>If A = [aᵢⱼ] and B = [bᵢⱼ], then C = A + B = [aᵢⱼ + bᵢⱼ]</pre>

        <p><strong>Properties of matrix addition:</strong></p>
        <ul>
        <li><strong>Commutative:</strong> A + B = B + A</li>
        <li><strong>Associative:</strong> (A + B) + C = A + (B + C)</li>
        <li><strong>Identity element:</strong> A + 0 = A (where 0 is the zero matrix)</li>
        <li><strong>Inverse element:</strong> A + (-A) = 0</li>
        </ul>

        <p><strong>Scalar Multiplication:</strong> Multiplying a matrix A by a scalar c produces a matrix where every element is multiplied by c:</p>
        <pre class='code-block'>cA = [caᵢⱼ]</pre>

        <p><strong>Properties of scalar multiplication:</strong></p>
        <ul>
        <li><strong>Distributive over addition (matrices):</strong> c(A + B) = cA + cB</li>
        <li><strong>Distributive over addition (scalars):</strong> (c + d)A = cA + dA</li>
        <li><strong>Associative:</strong> (cd)A = c(dA)</li>
        <li><strong>Identity:</strong> 1A = A</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example:</strong></p>
        <pre class='code-block'>A = [1  2]    B = [3  0]
    [4  5]        [2  1]

A + B = [1+3  2+0] = [4  2]
        [4+2  5+1]   [6  6]

2A = [2·1  2·2] = [2  4]
     [2·4  2·5]   [8 10]

A + 2B = [1  2] + [6  0] = [7  2]
         [4  5]   [4  2]   [8  7]</pre>
        </div>

        <p><strong>Vector spaces of matrices:</strong> The set of all m × n matrices with addition and scalar multiplication forms a vector space. This is fundamental to linear algebra—it allows us to apply all vector space concepts (subspaces, span, linear independence, etc.) to matrices.</p>
        """
    },
    {
        "title": "Matrix Multiplication: The Row-Column Rule",
        "body": """
        <p><strong>Matrix Multiplication:</strong> If A is m × p and B is p × n, the product C = AB is an m × n matrix where:</p>
        <pre class='code-block'>cᵢⱼ = Σₖ₌₁ᵖ aᵢₖ bₖⱼ  (dot product of row i of A with column j of B)</pre>

        <p><strong>Key requirement:</strong> The number of columns in A must equal the number of rows in B. If A is m × p and B is p × n, then AB is m × n.</p>

        <p><strong>Geometric intuition:</strong> Each entry cᵢⱼ is the dot product of row i of A with column j of B. This measures how "aligned" that row and column are.</p>

        <div class='example-box'>
        <p><strong>Example: 2×3 times 3×2 = 2×2</strong></p>
        <pre class='code-block'>A = [1  2  3]    B = [4  5]
    [6  7  8]        [0  1]
                      [2  3]

C = AB = [c₁₁  c₁₂]
         [c₂₁  c₂₂]

c₁₁ = row 1 of A · col 1 of B = (1)(4) + (2)(0) + (3)(2) = 4 + 0 + 6 = 10
c₁₂ = row 1 of A · col 2 of B = (1)(5) + (2)(1) + (3)(3) = 5 + 2 + 9 = 16
c₂₁ = row 2 of A · col 1 of B = (6)(4) + (7)(0) + (8)(2) = 24 + 0 + 16 = 40
c₂₂ = row 2 of A · col 2 of B = (6)(5) + (7)(1) + (8)(3) = 30 + 7 + 24 = 61

C = [10  16]
    [40  61]</pre>
        </div>

        <p><strong>Properties of matrix multiplication:</strong></p>
        <ul>
        <li><strong>Associative:</strong> (AB)C = A(BC)</li>
        <li><strong>Distributive (left):</strong> A(B + C) = AB + AC</li>
        <li><strong>Distributive (right):</strong> (A + B)C = AC + BC</li>
        <li><strong>NOT commutative:</strong> Generally AB ≠ BA (even if both products are defined)</li>
        <li><strong>Identity:</strong> If A is m × n, then IₘA = A = AIₙ, where Iₘ and Iₙ are identity matrices</li>
        </ul>

        <p><strong>Computational complexity:</strong> Multiplying an m × p matrix by a p × n matrix requires mnp scalar multiplications. For square matrices, this is O(n³). Strassen's algorithm achieves O(n^2.807), but is rarely used in practice.</p>
        """
    },
    {
        "title": "Transpose, Symmetric Matrices, and Special Forms",
        "body": """
        <p><strong>Transpose:</strong> The transpose of an m × n matrix A, denoted Aᵀ, is the n × m matrix obtained by swapping rows and columns:</p>
        <pre class='code-block'>(Aᵀ)ᵢⱼ = aⱼᵢ</pre>

        <p><strong>Properties of transpose:</strong></p>
        <ul>
        <li><strong>(Aᵀ)ᵀ = A</strong> (double transpose is the original)</li>
        <li><strong>(A + B)ᵀ = Aᵀ + Bᵀ</strong></li>
        <li><strong>(cA)ᵀ = cAᵀ</strong></li>
        <li><strong>(AB)ᵀ = BᵀAᵀ</strong> (order reverses!)</li>
        <li><strong>(A⁻¹)ᵀ = (Aᵀ)⁻¹</strong> (if A is invertible)</li>
        </ul>

        <p><strong>Symmetric matrices:</strong> A square matrix A is symmetric if Aᵀ = A (equivalently, aᵢⱼ = aⱼᵢ for all i, j). Symmetric matrices are crucial in mathematics and applications (covariance matrices, Hessians in optimization, etc.).</p>

        <p><strong>Skew-symmetric matrices:</strong> A is skew-symmetric if Aᵀ = -A. All diagonal entries must be 0 (since aᵢᵢ = -aᵢᵢ implies aᵢᵢ = 0).</p>

        <p><strong>Special matrix forms:</strong></p>
        <ul>
        <li><strong>Diagonal matrix:</strong> All off-diagonal entries are 0: diag(d₁, d₂, ..., dₙ)</li>
        <li><strong>Upper triangular:</strong> All entries below the diagonal are 0</li>
        <li><strong>Lower triangular:</strong> All entries above the diagonal are 0</li>
        <li><strong>Orthogonal matrix:</strong> Aᵀ A = I (rows and columns are orthonormal)</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Transpose and symmetry</strong></p>
        <pre class='code-block'>A = [1  2  3]        Aᵀ = [1  4]
    [4  5  6]              [2  5]
                           [3  6]

S = [1  2  3]  is symmetric because Sᵀ = [1  2  3] = S
    [2  5  4]                            [2  5  4]
    [3  4  6]                            [3  4  6]

K = [0   2  -3]  is skew-symmetric because Kᵀ = [0  -2   3]  = -K
    [-2  0   1]                               [2   0  -1]
    [3  -1   0]                               [-3  1   0]</pre>
        </div>

        <p><strong>Useful identities:</strong></p>
        <ul>
        <li>For any matrix A, both AᵀA and AAᵀ are symmetric matrices.</li>
        <li>A + Aᵀ is always symmetric; A - Aᵀ is always skew-symmetric.</li>
        <li>Any matrix can be uniquely written as A = S + K where S is symmetric and K is skew-symmetric.</li>
        </ul>
        """
    },
    {
        "title": "Matrix Invertibility and the Inverse",
        "body": """
        <p><strong>Matrix Inverse:</strong> For a square matrix A, the inverse A⁻¹ (if it exists) is a matrix such that:</p>
        <pre class='code-block'>AA⁻¹ = A⁻¹A = I</pre>

        <p><strong>When does an inverse exist?</strong> A square matrix A is <strong>invertible (nonsingular)</strong> if and only if:</p>
        <ul>
        <li>det(A) ≠ 0, OR</li>
        <li>rank(A) = n (full rank), OR</li>
        <li>The only solution to Ax = 0 is x = 0 (A has trivial nullspace)</li>
        </ul>

        <p>These three conditions are equivalent for square matrices.</p>

        <p><strong>Computing the inverse:</strong> There are several methods:</p>
        <ol>
        <li><strong>Gauss-Jordan elimination:</strong> Form [A | I] and reduce to [I | A⁻¹]</li>
        <li><strong>Adjugate formula:</strong> A⁻¹ = (1/det(A)) · adj(A) (practical only for small matrices)</li>
        <li><strong>LU decomposition:</strong> Factor A = LU, solve LA⁻¹ = U⁻¹ (or compute column-by-column)</li>
        </ol>

        <p><strong>Properties of inverses:</strong></p>
        <ul>
        <li><strong>(A⁻¹)⁻¹ = A</strong></li>
        <li><strong>(AB)⁻¹ = B⁻¹A⁻¹</strong> (order reverses!)</li>
        <li><strong>(Aᵀ)⁻¹ = (A⁻¹)ᵀ</strong></li>
        <li><strong>(cA)⁻¹ = (1/c)A⁻¹</strong> for scalar c ≠ 0</li>
        <li><strong>det(A⁻¹) = 1/det(A)</strong></li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Find A⁻¹ using Gauss-Jordan</strong></p>
        <pre class='code-block'>A = [1  2]
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
              [3  4][3/2 -1/2]   [0  1]</pre>
        </div>

        <p><strong>Practical notes:</strong> Computing inverses explicitly is often unnecessary. To solve Ax = b, use Gaussian elimination or other methods rather than computing A⁻¹ and multiplying. This is more efficient and numerically more stable.</p>
        """
    },
    {
        "title": "Matrix Decompositions and Applications",
        "body": """
        <p><strong>Common matrix decompositions:</strong> Breaking down matrices into simpler forms reveals structure and enables efficient computation.</p>

        <p><strong>1. LU Decomposition (A = LU):</strong> L is lower triangular, U is upper triangular. Useful for solving systems and computing determinants.</p>

        <p><strong>2. QR Decomposition (A = QR):</strong> Q has orthonormal columns, R is upper triangular. Used in least squares and numerical solving.</p>

        <p><strong>3. Eigenvalue Decomposition (A = PDP⁻¹):</strong> D is diagonal (eigenvalues), P contains eigenvectors. Reveals fundamental structure of A.</p>

        <p><strong>4. Singular Value Decomposition (A = UΣVᵀ):</strong> U and V have orthonormal columns, Σ is diagonal. Universal decomposition; works for any matrix shape.</p>

        <p><strong>5. Cholesky Decomposition (A = LLᵀ):</strong> For symmetric positive definite matrices. More efficient than LU.</p>

        <p><strong>Applications of matrix operations:</strong></p>
        <ul>
        <li><strong>Linear transformations:</strong> Multiplication by a matrix represents a linear map between vector spaces.</li>
        <li><strong>Least squares regression:</strong> Minimize ||Ax - b||² by solving AᵀAx = Aᵀb.</li>
        <li><strong>Image compression:</strong> Use SVD to find low-rank approximations.</li>
        <li><strong>Computer graphics:</strong> Rotation, scaling, and projection matrices transform 3D coordinates.</li>
        <li><strong>Markov chains:</strong> Transition matrices model probabilistic systems.</li>
        <li><strong>Adjacency matrices:</strong> Represent graphs and networks; powers count paths.</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Solving Ax = b using LU decomposition</strong></p>
        <pre class='code-block'>If A = LU, then Ax = b becomes LUx = b.
Let y = Ux. Then:
1. Solve Ly = b (forward substitution)
2. Solve Ux = y (back substitution)

This is more efficient than computing A⁻¹ when solving multiple systems with the same A.</pre>

        <p><strong>Example: Powers of matrices and adjacency</strong></p>
        <pre class='code-block'>For a directed graph with adjacency matrix A:
A² gives the number of 2-step paths between vertices
Aⁿ gives the number of n-step paths
(I - A)⁻¹ (if it exists) sums all path lengths: Σₙ₌₀^∞ Aⁿ</pre>
        </div>

        <p><strong>Computational efficiency:</strong> Modern numerical libraries (LAPACK, NumPy) compute decompositions using optimized algorithms. For large matrices, sparse matrix techniques and iterative methods are essential.</p>
        """
    }
]
