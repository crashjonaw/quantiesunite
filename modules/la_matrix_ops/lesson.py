SECTIONS = [
    {
        "title": "Matrix Addition and Scalar Multiplication",
        "body": """
        <p><strong>Matrix Addition:</strong> Two matrices \\(\\mathbf{A}\\) and \\(\\mathbf{B}\\) of the same dimensions (m × n) can be added element-wise to produce a matrix \\(\\mathbf{C}\\) of the same dimension:</p>
        <p>$$\\text{If } \\mathbf{A} = [a_{ij}] \\text{ and } \\mathbf{B} = [b_{ij}], \\text{ then } \\mathbf{C} = \\mathbf{A} + \\mathbf{B} = [a_{ij} + b_{ij}]$$</p>

        <p><strong>Properties of matrix addition:</strong></p>
        <ul>
        <li><strong>Commutative:</strong> \\(\\mathbf{A} + \\mathbf{B} = \\mathbf{B} + \\mathbf{A}\\)</li>
        <li><strong>Associative:</strong> \\((\\mathbf{A} + \\mathbf{B}) + \\mathbf{C} = \\mathbf{A} + (\\mathbf{B} + \\mathbf{C})\\)</li>
        <li><strong>Identity element:</strong> \\(\\mathbf{A} + \\mathbf{0} = \\mathbf{A}\\)</li>
        <li><strong>Inverse element:</strong> \\(\\mathbf{A} + (-\\mathbf{A}) = \\mathbf{0}\\)</li>
        </ul>

        <p><strong>Scalar Multiplication:</strong> Multiplying a matrix \\(\\mathbf{A}\\) by a scalar \\(c\\) produces a matrix where every element is multiplied by \\(c\\):</p>
        <p>$$c\\mathbf{A} = [c \\cdot a_{ij}]$$</p>

        <p><strong>Properties of scalar multiplication:</strong></p>
        <ul>
        <li><strong>Distributive over addition (matrices):</strong> \\(c(\\mathbf{A} + \\mathbf{B}) = c\\mathbf{A} + c\\mathbf{B}\\)</li>
        <li><strong>Distributive over addition (scalars):</strong> \\((c + d)\\mathbf{A} = c\\mathbf{A} + d\\mathbf{A}\\)</li>
        <li><strong>Associative:</strong> \\((cd)\\mathbf{A} = c(d\\mathbf{A})\\)</li>
        <li><strong>Identity:</strong> \\(1\\mathbf{A} = \\mathbf{A}\\)</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example:</strong></p>
        <p>$$\\mathbf{A} = \\begin{pmatrix} 1 & 2 \\\\ 4 & 5 \\end{pmatrix}, \\quad \\mathbf{B} = \\begin{pmatrix} 3 & 0 \\\\ 2 & 1 \\end{pmatrix}$$</p>
        <p>$$\\mathbf{A} + \\mathbf{B} = \\begin{pmatrix} 1+3 & 2+0 \\\\ 4+2 & 5+1 \\end{pmatrix} = \\begin{pmatrix} 4 & 2 \\\\ 6 & 6 \\end{pmatrix}$$</p>
        <p>$$2\\mathbf{A} = \\begin{pmatrix} 2 & 4 \\\\ 8 & 10 \\end{pmatrix}$$</p>
        <p>$$\\mathbf{A} + 2\\mathbf{B} = \\begin{pmatrix} 1 & 2 \\\\ 4 & 5 \\end{pmatrix} + \\begin{pmatrix} 6 & 0 \\\\ 4 & 2 \\end{pmatrix} = \\begin{pmatrix} 7 & 2 \\\\ 8 & 7 \\end{pmatrix}$$</p>
        </div>

        <p><strong>Vector spaces of matrices:</strong> The set of all m × n matrices with addition and scalar multiplication forms a vector space. This is fundamental to linear algebra—it allows us to apply all vector space concepts (subspaces, span, linear independence, etc.) to matrices.</p>
        """
    },
    {
        "title": "Matrix Multiplication: The Row-Column Rule",
        "body": """
        <p><strong>Matrix Multiplication:</strong> If \\(\\mathbf{A}\\) is \\(m \\times p\\) and \\(\\mathbf{B}\\) is \\(p \\times n\\), the product \\(\\mathbf{C} = \\mathbf{AB}\\) is an \\(m \\times n\\) matrix where:</p>
        <p>$$c_{ij} = \\sum_{k=1}^{p} a_{ik} b_{kj} \\quad \\text{(dot product of row } i \\text{ of } \\mathbf{A} \\text{ with column } j \\text{ of } \\mathbf{B}\\text{)}$$</p>

        <p><strong>Key requirement:</strong> The number of columns in \\(\\mathbf{A}\\) must equal the number of rows in \\(\\mathbf{B}\\).</p>

        <p><strong>Geometric intuition:</strong> Each entry \\(c_{ij}\\) is the dot product of row \\(i\\) of \\(\\mathbf{A}\\) with column \\(j\\) of \\(\\mathbf{B}\\). This measures how "aligned" that row and column are.</p>

        <div class='example-box'>
        <p><strong>Example: \\(2 \\times 3\\) times \\(3 \\times 2\\) = \\(2 \\times 2\\)</strong></p>
        <p>$$\\mathbf{A} = \\begin{pmatrix} 1 & 2 & 3 \\\\ 6 & 7 & 8 \\end{pmatrix}, \\quad \\mathbf{B} = \\begin{pmatrix} 4 & 5 \\\\ 0 & 1 \\\\ 2 & 3 \\end{pmatrix}$$</p>
        <p>$$\\mathbf{C} = \\mathbf{AB} = \\begin{pmatrix} c_{11} & c_{12} \\\\ c_{21} & c_{22} \\end{pmatrix}$$</p>
        <p>\\(c_{11} = (1)(4) + (2)(0) + (3)(2) = 10\\)</p>
        <p>\\(c_{12} = (1)(5) + (2)(1) + (3)(3) = 16\\)</p>
        <p>\\(c_{21} = (6)(4) + (7)(0) + (8)(2) = 40\\)</p>
        <p>\\(c_{22} = (6)(5) + (7)(1) + (8)(3) = 61\\)</p>
        <p>$$\\mathbf{C} = \\begin{pmatrix} 10 & 16 \\\\ 40 & 61 \\end{pmatrix}$$</p>
        </div>

        <p><strong>Properties of matrix multiplication:</strong></p>
        <ul>
        <li><strong>Associative:</strong> \\((\\mathbf{AB})\\mathbf{C} = \\mathbf{A}(\\mathbf{BC})\\)</li>
        <li><strong>Distributive (left):</strong> \\(\\mathbf{A}(\\mathbf{B} + \\mathbf{C}) = \\mathbf{AB} + \\mathbf{AC}\\)</li>
        <li><strong>Distributive (right):</strong> \\((\\mathbf{A} + \\mathbf{B})\\mathbf{C} = \\mathbf{AC} + \\mathbf{BC}\\)</li>
        <li><strong>NOT commutative:</strong> Generally \\(\\mathbf{AB} \\neq \\mathbf{BA}\\)</li>
        <li><strong>Identity:</strong> \\(\\mathbf{I}_m \\mathbf{A} = \\mathbf{A} = \\mathbf{A} \\mathbf{I}_n\\)</li>
        </ul>

        <p><strong>Computational complexity:</strong> Multiplying an \\(m \\times p\\) matrix by a \\(p \\times n\\) matrix requires \\(mnp\\) scalar multiplications. For square matrices, this is \\(O(n^3)\\). Strassen's algorithm achieves \\(O(n^{2.807})\\), but is rarely used in practice.</p>
        """
    },
    {
        "title": "Transpose, Symmetric Matrices, and Special Forms",
        "body": """
        <p><strong>Transpose:</strong> The transpose of an \\(m \\times n\\) matrix \\(\\mathbf{A}\\), denoted \\(\\mathbf{A}^T\\), is the \\(n \\times m\\) matrix obtained by swapping rows and columns:</p>
        <p>$$(\\mathbf{A}^T)_{ij} = a_{ji}$$</p>

        <p><strong>Properties of transpose:</strong></p>
        <ul>
        <li>\\((\\mathbf{A}^T)^T = \\mathbf{A}\\)</li>
        <li>\\((\\mathbf{A} + \\mathbf{B})^T = \\mathbf{A}^T + \\mathbf{B}^T\\)</li>
        <li>\\((c\\mathbf{A})^T = c\\mathbf{A}^T\\)</li>
        <li>\\((\\mathbf{AB})^T = \\mathbf{B}^T \\mathbf{A}^T\\) (order reverses!)</li>
        <li>\\((\\mathbf{A}^{-1})^T = (\\mathbf{A}^T)^{-1}\\) (if \\(\\mathbf{A}\\) is invertible)</li>
        </ul>

        <p><strong>Symmetric matrices:</strong> A square matrix \\(\\mathbf{A}\\) is symmetric if \\(\\mathbf{A}^T = \\mathbf{A}\\) (equivalently, \\(a_{ij} = a_{ji}\\) for all \\(i, j\\)). Symmetric matrices are crucial in mathematics and applications (covariance matrices, Hessians in optimization, etc.).</p>

        <p><strong>Skew-symmetric matrices:</strong> \\(\\mathbf{A}\\) is skew-symmetric if \\(\\mathbf{A}^T = -\\mathbf{A}\\). All diagonal entries must be 0 (since \\(a_{ii} = -a_{ii}\\) implies \\(a_{ii} = 0\\)).</p>

        <p><strong>Special matrix forms:</strong></p>
        <ul>
        <li><strong>Diagonal matrix:</strong> All off-diagonal entries are 0: \\(\\text{diag}(d_1, d_2, \\ldots, d_n)\\)</li>
        <li><strong>Upper triangular:</strong> All entries below the diagonal are 0</li>
        <li><strong>Lower triangular:</strong> All entries above the diagonal are 0</li>
        <li><strong>Orthogonal matrix:</strong> \\(\\mathbf{A}^T \\mathbf{A} = \\mathbf{I}\\) (rows and columns are orthonormal)</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Transpose and symmetry</strong></p>
        <p>$$\\mathbf{A} = \\begin{pmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\end{pmatrix}, \\quad \\mathbf{A}^T = \\begin{pmatrix} 1 & 4 \\\\ 2 & 5 \\\\ 3 & 6 \\end{pmatrix}$$</p>
        <p>$$\\mathbf{S} = \\begin{pmatrix} 1 & 2 & 3 \\\\ 2 & 5 & 4 \\\\ 3 & 4 & 6 \\end{pmatrix} \\text{ is symmetric because } \\mathbf{S}^T = \\mathbf{S}$$</p>
        <p>$$\\mathbf{K} = \\begin{pmatrix} 0 & 2 & -3 \\\\ -2 & 0 & 1 \\\\ 3 & -1 & 0 \\end{pmatrix} \\text{ is skew-symmetric because } \\mathbf{K}^T = -\\mathbf{K}$$</p>
        </div>

        <p><strong>Useful identities:</strong></p>
        <ul>
        <li>For any matrix \\(\\mathbf{A}\\), both \\(\\mathbf{A}^T\\mathbf{A}\\) and \\(\\mathbf{A}\\mathbf{A}^T\\) are symmetric matrices.</li>
        <li>\\(\\mathbf{A} + \\mathbf{A}^T\\) is always symmetric; \\(\\mathbf{A} - \\mathbf{A}^T\\) is always skew-symmetric.</li>
        <li>Any matrix can be uniquely written as \\(\\mathbf{A} = \\mathbf{S} + \\mathbf{K}\\) where \\(\\mathbf{S}\\) is symmetric and \\(\\mathbf{K}\\) is skew-symmetric.</li>
        </ul>
        """
    },
    {
        "title": "Matrix Invertibility and the Inverse",
        "body": """
        <p><strong>Matrix Inverse:</strong> For a square matrix \\(\\mathbf{A}\\), the inverse \\(\\mathbf{A}^{-1}\\) (if it exists) is a matrix such that:</p>
        <p>$$\\mathbf{A}\\mathbf{A}^{-1} = \\mathbf{A}^{-1}\\mathbf{A} = \\mathbf{I}$$</p>

        <p><strong>When does an inverse exist?</strong> A square matrix \\(\\mathbf{A}\\) is <strong>invertible (nonsingular)</strong> if and only if:</p>
        <ul>
        <li>\\(\\det(\\mathbf{A}) \\neq 0\\), OR</li>
        <li>\\(\\text{rank}(\\mathbf{A}) = n\\) (full rank), OR</li>
        <li>The only solution to \\(\\mathbf{A}\\mathbf{x} = \\mathbf{0}\\) is \\(\\mathbf{x} = \\mathbf{0}\\)</li>
        </ul>

        <p>These three conditions are equivalent for square matrices.</p>

        <p><strong>Computing the inverse:</strong> There are several methods:</p>
        <ol>
        <li><strong>Gauss-Jordan elimination:</strong> Form \\([\\mathbf{A} \\mid \\mathbf{I}]\\) and reduce to \\([\\mathbf{I} \\mid \\mathbf{A}^{-1}]\\)</li>
        <li><strong>Adjugate formula:</strong> \\(\\mathbf{A}^{-1} = \\frac{1}{\\det(\\mathbf{A})} \\cdot \\text{adj}(\\mathbf{A})\\) (practical only for small matrices)</li>
        <li><strong>LU decomposition:</strong> Factor \\(\\mathbf{A} = \\mathbf{LU}\\), then solve column-by-column</li>
        </ol>

        <p><strong>Properties of inverses:</strong></p>
        <ul>
        <li>\\((\\mathbf{A}^{-1})^{-1} = \\mathbf{A}\\)</li>
        <li>\\((\\mathbf{AB})^{-1} = \\mathbf{B}^{-1}\\mathbf{A}^{-1}\\) (order reverses!)</li>
        <li>\\((\\mathbf{A}^T)^{-1} = (\\mathbf{A}^{-1})^T\\)</li>
        <li>\\((c\\mathbf{A})^{-1} = \\frac{1}{c}\\mathbf{A}^{-1}\\) for scalar \\(c \\neq 0\\)</li>
        <li>\\(\\det(\\mathbf{A}^{-1}) = \\frac{1}{\\det(\\mathbf{A})}\\)</li>
        </ul>

        <div class='example-box'>
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

        <p><strong>Practical notes:</strong> Computing inverses explicitly is often unnecessary. To solve \\(\\mathbf{A}\\mathbf{x} = \\mathbf{b}\\), use Gaussian elimination or other methods rather than computing \\(\\mathbf{A}^{-1}\\) and multiplying. This is more efficient and numerically more stable.</p>
        """
    },
    {
        "title": "Matrix Decompositions and Applications",
        "body": """
        <p><strong>Common matrix decompositions:</strong> Breaking down matrices into simpler forms reveals structure and enables efficient computation.</p>

        <p><strong>1. LU Decomposition (\\(\\mathbf{A} = \\mathbf{LU}\\)):</strong> \\(\\mathbf{L}\\) is lower triangular, \\(\\mathbf{U}\\) is upper triangular. Useful for solving systems and computing determinants.</p>

        <p><strong>2. QR Decomposition (\\(\\mathbf{A} = \\mathbf{QR}\\)):</strong> \\(\\mathbf{Q}\\) has orthonormal columns, \\(\\mathbf{R}\\) is upper triangular. Used in least squares and numerical solving.</p>

        <p><strong>3. Eigenvalue Decomposition (\\(\\mathbf{A} = \\mathbf{PDP}^{-1}\\)):</strong> \\(\\mathbf{D}\\) is diagonal (eigenvalues), \\(\\mathbf{P}\\) contains eigenvectors. Reveals fundamental structure of \\(\\mathbf{A}\\).</p>

        <p><strong>4. Singular Value Decomposition (\\(\\mathbf{A} = \\mathbf{U}\\mathbf{\\Sigma}\\mathbf{V}^T\\)):</strong> \\(\\mathbf{U}\\) and \\(\\mathbf{V}\\) have orthonormal columns, \\(\\mathbf{\\Sigma}\\) is diagonal. Universal decomposition; works for any matrix shape.</p>

        <p><strong>5. Cholesky Decomposition (\\(\\mathbf{A} = \\mathbf{LL}^T\\)):</strong> For symmetric positive definite matrices. More efficient than LU.</p>

        <p><strong>Applications of matrix operations:</strong></p>
        <ul>
        <li><strong>Linear transformations:</strong> Multiplication by a matrix represents a linear map between vector spaces.</li>
        <li><strong>Least squares regression:</strong> Minimize \\(\\|\\mathbf{Ax} - \\mathbf{b}\\|^2\\) by solving \\(\\mathbf{A}^T\\mathbf{A}\\mathbf{x} = \\mathbf{A}^T\\mathbf{b}\\).</li>
        <li><strong>Image compression:</strong> Use SVD to find low-rank approximations.</li>
        <li><strong>Computer graphics:</strong> Rotation, scaling, and projection matrices transform 3D coordinates.</li>
        <li><strong>Markov chains:</strong> Transition matrices model probabilistic systems.</li>
        <li><strong>Adjacency matrices:</strong> Represent graphs and networks; powers count paths.</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Solving \\(\\mathbf{Ax} = \\mathbf{b}\\) using LU decomposition</strong></p>
        <p>If \\(\\mathbf{A} = \\mathbf{LU}\\), then \\(\\mathbf{Ax} = \\mathbf{b}\\) becomes \\(\\mathbf{LUx} = \\mathbf{b}\\).</p>
        <p>Let \\(\\mathbf{y} = \\mathbf{Ux}\\). Then:</p>
        <ol>
        <li>Solve \\(\\mathbf{Ly} = \\mathbf{b}\\) (forward substitution)</li>
        <li>Solve \\(\\mathbf{Ux} = \\mathbf{y}\\) (back substitution)</li>
        </ol>
        <p>This is more efficient than computing \\(\\mathbf{A}^{-1}\\) when solving multiple systems with the same \\(\\mathbf{A}\\).</p>

        <p><strong>Example: Powers of matrices and adjacency</strong></p>
        <p>For a directed graph with adjacency matrix \\(\\mathbf{A}\\):</p>
        <ul>
        <li>\\(\\mathbf{A}^2\\) gives the number of 2-step paths between vertices</li>
        <li>\\(\\mathbf{A}^n\\) gives the number of n-step paths</li>
        <li>\\((\\mathbf{I} - \\mathbf{A})^{-1} = \\sum_{n=0}^{\\infty} \\mathbf{A}^n\\) sums all path lengths (if it converges)</li>
        </ul>
        </div>

        <p><strong>Computational efficiency:</strong> Modern numerical libraries (LAPACK, NumPy) compute decompositions using optimized algorithms. For large matrices, sparse matrix techniques and iterative methods are essential.</p>
        """
    }
]
