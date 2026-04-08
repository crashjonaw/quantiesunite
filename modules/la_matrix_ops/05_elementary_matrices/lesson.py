TITLE = "Elementary Matrices"

SECTIONS = [
    {
        "title": "What Are Elementary Matrices?",
        "body": """
        <div class="concept-box">
        <p><strong>Elementary Matrix Definition:</strong> An elementary matrix \\(\\mathbf{E}\\) is a matrix obtained by performing a single elementary row operation on the identity matrix \\(\\mathbf{I}\\).</p>
        </div>

        <p><strong>The three types of elementary row operations:</strong></p>
        <ul>
        <li><strong>Type 1 (Row Swap):</strong> Swap two rows</li>
        <li><strong>Type 2 (Row Scaling):</strong> Multiply a row by a nonzero scalar</li>
        <li><strong>Type 3 (Row Addition):</strong> Add a multiple of one row to another</li>
        </ul>

        <div class="concept-box">
        <p><strong>Key Property:</strong> Multiplying a matrix \\(\\mathbf{A}\\) on the left by an elementary matrix \\(\\mathbf{E}\\) (i.e., computing \\(\\mathbf{EA}\\)) performs the same row operation on \\(\\mathbf{A}\\) that was performed on \\(\\mathbf{I}\\) to create \\(\\mathbf{E}\\).</p>
        </div>

        <div class="worked-example">
        <p><strong>Example: Row Swap Elementary Matrix</strong></p>
        <p>To swap rows 1 and 2 in a \\(3 \\times 3\\) matrix, apply the row swap to \\(\\mathbf{I}_3\\):</p>
        <p>$$\\mathbf{E} = \\begin{pmatrix} 0 & 1 & 0 \\\\ 1 & 0 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$$</p>
        <p>If \\(\\mathbf{A} = \\begin{pmatrix} a & b & c \\\\ d & e & f \\\\ g & h & i \\end{pmatrix}\\), then:</p>
        <p>$$\\mathbf{EA} = \\begin{pmatrix} d & e & f \\\\ a & b & c \\\\ g & h & i \\end{pmatrix} \\quad \\text{(rows 1 and 2 swapped)}$$</p>
        </div>

        <div class="success-box">
        <p><strong>Invertibility:</strong> Every elementary matrix is invertible! The inverse is also elementary (the operation that undoes the original operation).</p>
        </div>
        """
    },
    {
        "title": "Elementary Matrices and Gaussian Elimination",
        "body": """
        <div class="concept-box">
        <p><strong>Connection to Gaussian Elimination:</strong> Gaussian elimination is a sequence of elementary row operations. Each operation corresponds to left-multiplication by an elementary matrix.</p>
        </div>

        <p><strong>The LU Decomposition Connection:</strong> If we reduce \\(\\mathbf{A}\\) to upper triangular form \\(\\mathbf{U}\\) without row swaps using elementary matrices \\(\\mathbf{E}_1, \\mathbf{E}_2, \\ldots, \\mathbf{E}_k\\), then:</p>
        <p>$$\\mathbf{E}_k \\mathbf{E}_{k-1} \\cdots \\mathbf{E}_2 \\mathbf{E}_1 \\mathbf{A} = \\mathbf{U}$$</p>
        <p>$$\\mathbf{A} = (\\mathbf{E}_1^{-1} \\mathbf{E}_2^{-1} \\cdots \\mathbf{E}_{k-1}^{-1} \\mathbf{E}_k^{-1}) \\mathbf{U} = \\mathbf{LU}$$</p>

        <div class="worked-example">
        <p><strong>Example: LU Decomposition via Elementary Matrices</strong></p>
        <p>For Gaussian elimination on \\(\\mathbf{A}\\):</p>
        <p>$$\\mathbf{E}_2 \\mathbf{E}_1 \\mathbf{A} = \\mathbf{U}$$</p>
        <p>Where \\(\\mathbf{E}_1\\) is "row 2 \\(- 2 \\cdot\\) row 1" and \\(\\mathbf{E}_2\\) is a scaling operation.</p>
        <p>Then: \\(\\mathbf{A} = \\mathbf{E}_1^{-1} \\mathbf{E}_2^{-1} \\mathbf{U} = \\mathbf{LU}\\)</p>
        <p>This shows how Gaussian elimination systematically builds both \\(\\mathbf{L}\\) and \\(\\mathbf{U}\\).</p>
        </div>

        <div class="success-box">
        <p><strong>Why this matters:</strong> Understanding that row operations correspond to matrix multiplication provides deep insight into why Gaussian elimination works and how to decompose matrices efficiently.</p>
        </div>
        """
    },
    {
        "title": "Computing with Elementary Matrices",
        "body": """
        <p><strong>Computing Elementary Matrices:</strong></p>
        <ul>
        <li><strong>Row swap:</strong> Start with \\(\\mathbf{I}\\), swap two rows</li>
        <li><strong>Row scaling:</strong> Start with \\(\\mathbf{I}\\), replace diagonal entry with the scalar</li>
        <li><strong>Row addition:</strong> Start with \\(\\mathbf{I}\\), place the multiplier in the appropriate off-diagonal position</li>
        </ul>

        <div class="worked-example">
        <p><strong>Example: Row Addition Elementary Matrix (\\(3 \\times 3\\))</strong></p>
        <p>To add 2 times row 1 to row 2:</p>
        <p>$$\\mathbf{E} = \\begin{pmatrix} 1 & 0 & 0 \\\\ 2 & 1 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$$</p>
        <p>The 2 appears in position \\((2,1)\\) because we're adding 2 times row 1 to row 2.</p>
        </div>

        <p><strong>Finding Inverses of Elementary Matrices:</strong></p>
        <ul>
        <li><strong>Row swap:</strong> \\(\\mathbf{E}^T = \\mathbf{E}^{-1}\\) (swap is self-inverse)</li>
        <li><strong>Row scaling by \\(c\\):</strong> Scale the same row by \\(1/c\\) instead</li>
        <li><strong>Row addition by \\(c\\):</strong> Use \\(-c\\) instead of \\(c\\)</li>
        </ul>

        <div class="success-box">
        <p><strong>First Principles:</strong> Elementary matrices formalize the intuition that row operations are just multiplication. This transforms geometric/algorithmic intuition (row operations) into algebraic machinery (matrix multiplication), enabling powerful theoretical and computational results.</p>
        </div>
        """
    },
    {
        "title": "Applications to Matrix Decompositions",
        "body": """
        <div class="concept-box">
        <p><strong>Matrix Decompositions and Applications:</strong></p>

        <p><strong>1. LU Decomposition (\\(\\mathbf{A} = \\mathbf{LU}\\)):</strong> \\(\\mathbf{L}\\) is lower triangular, \\(\\mathbf{U}\\) is upper triangular. Built from elementary row operations.</p>

        <p><strong>2. QR Decomposition (\\(\\mathbf{A} = \\mathbf{QR}\\)):</strong> \\(\\mathbf{Q}\\) has orthonormal columns, \\(\\mathbf{R}\\) is upper triangular. Uses Gram-Schmidt or Householder reflections.</p>

        <p><strong>3. Eigenvalue Decomposition (\\(\\mathbf{A} = \\mathbf{PDP}^{-1}\\)):</strong> \\(\\mathbf{D}\\) is diagonal (eigenvalues), \\(\\mathbf{P}\\) contains eigenvectors. Reveals fundamental structure of \\(\\mathbf{A}\\).</p>

        <p><strong>4. Singular Value Decomposition (\\(\\mathbf{A} = \\mathbf{U\\Sigma V}^T\\)):</strong> \\(\\mathbf{U}\\) and \\(\\mathbf{V}\\) have orthonormal columns, \\(\\mathbf{\\Sigma}\\) is diagonal. Universal decomposition; works for any matrix shape.</p>

        <p><strong>5. Cholesky Decomposition (\\(\\mathbf{A} = \\mathbf{LL}^T\\)):</strong> For symmetric positive definite matrices. More efficient than LU.</p>
        </div>

        <p><strong>Applications of matrix operations:</strong></p>
        <ul>
        <li><strong>Linear transformations:</strong> Multiplication by a matrix represents a linear map between vector spaces.</li>
        <li><strong>Least squares regression:</strong> Minimize \\(\\|\\mathbf{Ax} - \\mathbf{b}\\|^2\\) by solving \\(\\mathbf{A}^T\\mathbf{Ax} = \\mathbf{A}^T\\mathbf{b}\\).</li>
        <li><strong>Image compression:</strong> Use SVD to find low-rank approximations.</li>
        <li><strong>Computer graphics:</strong> Rotation, scaling, and projection matrices transform 3D coordinates.</li>
        <li><strong>Markov chains:</strong> Transition matrices model probabilistic systems.</li>
        <li><strong>Adjacency matrices:</strong> Represent graphs and networks; powers count paths.</li>
        </ul>

        <div class="worked-example">
        <p><strong>Example: Solving \\(\\mathbf{Ax} = \\mathbf{b}\\) using LU decomposition</strong></p>
        <p>If \\(\\mathbf{A} = \\mathbf{LU}\\), then \\(\\mathbf{Ax} = \\mathbf{b}\\) becomes \\(\\mathbf{LUx} = \\mathbf{b}\\).</p>
        <p>Let \\(\\mathbf{y} = \\mathbf{Ux}\\). Then:</p>
        <ol>
        <li>Solve \\(\\mathbf{Ly} = \\mathbf{b}\\) (forward substitution)</li>
        <li>Solve \\(\\mathbf{Ux} = \\mathbf{y}\\) (back substitution)</li>
        </ol>
        <p>This is more efficient than computing \\(\\mathbf{A}^{-1}\\) when solving multiple systems with the same \\(\\mathbf{A}\\).</p>
        </div>

        <div class="success-box">
        <p><strong>Computational efficiency:</strong> Modern numerical libraries (LAPACK, NumPy) compute decompositions using optimized algorithms. For large matrices, sparse matrix techniques and iterative methods are essential.</p>
        </div>
        """
    }
]
