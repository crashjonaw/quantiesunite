TITLE = "Transpose and Special Matrices"

SECTIONS = [
    {
        "title": "The Transpose Operation",
        "body": """
        <div class="concept-box">
        <p><strong>Transpose Definition:</strong> The transpose of an m × n matrix A, denoted Aᵀ, is the n × m matrix obtained by swapping rows and columns:</p>
        <div class="code-block">(Aᵀ)ᵢⱼ = aⱼᵢ</div>
        </div>

        <p><strong>Properties of transpose:</strong></p>
        <ul>
        <li><strong>(Aᵀ)ᵀ = A</strong> (double transpose is the original)</li>
        <li><strong>(A + B)ᵀ = Aᵀ + Bᵀ</strong></li>
        <li><strong>(cA)ᵀ = cAᵀ</strong></li>
        <li><strong>(AB)ᵀ = BᵀAᵀ</strong> (order reverses!)</li>
        <li><strong>(A⁻¹)ᵀ = (Aᵀ)⁻¹</strong> (if A is invertible)</li>
        </ul>

        <div class="worked-example">
        <p><strong>Example: Transpose Computation</strong></p>
        <div class="code-block">A = [1  2  3]        Aᵀ = [1  4]
    [4  5  6]              [2  5]
                           [3  6]</div>
        </div>

        <div class="warning-box">
        <p><strong>Order matters in (AB)ᵀ = BᵀAᵀ:</strong> Notice the order reversal! This is not (AB)ᵀ = AᵀBᵀ. The order of multiplication reverses when you transpose a product.</p>
        </div>
        """
    },
    {
        "title": "Symmetric and Skew-Symmetric Matrices",
        "body": """
        <div class="concept-box">
        <p><strong>Symmetric matrices:</strong> A square matrix A is symmetric if Aᵀ = A (equivalently, aᵢⱼ = aⱼᵢ for all i, j). Symmetric matrices are crucial in mathematics and applications (covariance matrices, Hessians in optimization, etc.).</p>
        </div>

        <div class="concept-box">
        <p><strong>Skew-symmetric matrices:</strong> A is skew-symmetric if Aᵀ = -A. All diagonal entries must be 0 (since aᵢᵢ = -aᵢᵢ implies aᵢᵢ = 0).</p>
        </div>

        <div class="worked-example">
        <p><strong>Example: Symmetric and Skew-symmetric Matrices</strong></p>
        <div class="code-block">S = [1  2  3]  is symmetric because Sᵀ = [1  2  3] = S
    [2  5  4]                            [2  5  4]
    [3  4  6]                            [3  4  6]

K = [0   2  -3]  is skew-symmetric because Kᵀ = [0  -2   3]  = -K
    [-2  0   1]                               [2   0  -1]
    [3  -1   0]                               [-3  1   0]</div>
        </div>

        <div class="success-box">
        <p><strong>Decomposition:</strong> Any matrix can be uniquely written as A = S + K where S is symmetric and K is skew-symmetric. This decomposition reveals the underlying structure.</p>
        </div>
        """
    },
    {
        "title": "Special Matrix Forms",
        "body": """
        <p><strong>Special matrix forms:</strong></p>
        <ul>
        <li><strong>Diagonal matrix:</strong> All off-diagonal entries are 0: diag(d₁, d₂, ..., dₙ)</li>
        <li><strong>Upper triangular:</strong> All entries below the diagonal are 0</li>
        <li><strong>Lower triangular:</strong> All entries above the diagonal are 0</li>
        <li><strong>Orthogonal matrix:</strong> Aᵀ A = I (rows and columns are orthonormal)</li>
        </ul>

        <div class="success-box">
        <p><strong>Why these forms matter:</strong> These special structures enable efficient algorithms. Triangular systems are easy to solve (\(O(n^2)\) instead of \(O(n^3)\)), and orthogonal matrices preserve geometry (distances, angles).</p>
        </div>

        <p><strong>Useful identities:</strong></p>
        <ul>
        <li>For any matrix A, both AᵀA and AAᵀ are symmetric matrices.</li>
        <li>A + Aᵀ is always symmetric; A - Aᵀ is always skew-symmetric.</li>
        </ul>
        """
    }
]
