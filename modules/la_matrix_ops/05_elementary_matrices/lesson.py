TITLE = "Elementary Matrices"

SECTIONS = [
    {
        "title": "What Are Elementary Matrices?",
        "body": """
        <div class="concept-box">
        <p><strong>Elementary Matrix Definition:</strong> An elementary matrix $E$ is a matrix obtained by performing a single elementary row operation on the identity matrix $I$.</p>
        </div>

        <p><strong>The three types of elementary row operations:</strong></p>
        <ul>
        <li><strong>Type 1 (Row Swap):</strong> Swap two rows</li>
        <li><strong>Type 2 (Row Scaling):</strong> Multiply a row by a nonzero scalar</li>
        <li><strong>Type 3 (Row Addition):</strong> Add a multiple of one row to another</li>
        </ul>

        <div class="concept-box">
        <p><strong>Key Property:</strong> Multiplying a matrix $A$ on the left by an elementary matrix $E$ (i.e., computing $EA$) performs the same row operation on $A$ that was performed on $I$ to create $E$.</p>
        </div>

        <div class="worked-example">
        <p><strong>Example: Row Swap Elementary Matrix</strong></p>
        <div class="code-block">To swap rows 1 and 2 in a $3 \\times 3$ matrix, apply row swap to $I_3$:

$$E = \\begin{bmatrix} 0 & 1 & 0 \\\\ 1 & 0 & 0 \\\\ 0 & 0 & 1 \\end{bmatrix}$$

If $$A = \\begin{bmatrix} a & b & c \\\\ d & e & f \\\\ g & h & i \\end{bmatrix}$$

Then $$EA = \\begin{bmatrix} d & e & f \\\\ a & b & c \\\\ g & h & i \\end{bmatrix}$$ (rows 1 and 2 swapped)</div>
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

        <p><strong>The LU Decomposition Connection:</strong> If we reduce $A$ to upper triangular form $U$ without row swaps using elementary matrices $E_1, E_2, \\ldots, E_k$, then:</p>
        <div class="code-block">$$E_k E_{k-1} \\cdots E_2 E_1 A = U$$
$$A = (E_1^{-1} E_2^{-1} \\cdots E_{k-1}^{-1} E_k^{-1}) U = LU$$</div>

        <div class="worked-example">
        <p><strong>Example: LU Decomposition via Elementary Matrices</strong></p>
        <div class="code-block">For Gaussian elimination on $A$:
$$E_2 E_1 A = U$$

Where $E_1$ is "row 2 $- 2 \\cdot$ row 1" and $E_2$ is a scaling operation.

Then: $A = E_1^{-1} E_2^{-1} U = LU$

This shows how Gaussian elimination systematically builds both $L$ and $U$.</div>
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
        <li><strong>Row swap:</strong> Start with $I$, swap two rows</li>
        <li><strong>Row scaling:</strong> Start with $I$, replace diagonal entry with the scalar</li>
        <li><strong>Row addition:</strong> Start with $I$, place the multiplier in the appropriate off-diagonal position</li>
        </ul>

        <div class="worked-example">
        <p><strong>Example: Row Addition Elementary Matrix ($3 \\times 3$)</strong></p>
        <div class="code-block">To add 2 times row 1 to row 2:

$$E = \\begin{bmatrix} 1 & 0 & 0 \\\\ 2 & 1 & 0 \\\\ 0 & 0 & 1 \\end{bmatrix}$$

The 2 appears in position $(2,1)$ because we're adding 2 times row 1 to row 2.</div>
        </div>

        <p><strong>Finding Inverses of Elementary Matrices:</strong></p>
        <ul>
        <li><strong>Row swap:</strong> $E^T = E^{-1}$ (swap is self-inverse)</li>
        <li><strong>Row scaling by $c$:</strong> Scale the same row by $1/c$ instead</li>
        <li><strong>Row addition by $c$:</strong> Use $-c$ instead of $c$</li>
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

        <p><strong>1. LU Decomposition ($A = LU$):</strong> $L$ is lower triangular, $U$ is upper triangular. Built from elementary row operations.</p>

        <p><strong>2. QR Decomposition ($A = QR$):</strong> $Q$ has orthonormal columns, $R$ is upper triangular. Uses Gram-Schmidt or Householder reflections (which are also based on elementary operations).</p>

        <p><strong>3. Eigenvalue Decomposition ($A = PDP^{-1}$):</strong> $D$ is diagonal (eigenvalues), $P$ contains eigenvectors. Reveals fundamental structure of $A$.</p>

        <p><strong>4. Singular Value Decomposition ($A = U\\Sigma V^T$):</strong> $U$ and $V$ have orthonormal columns, $\\Sigma$ is diagonal. Universal decomposition; works for any matrix shape.</p>

        <p><strong>5. Cholesky Decomposition ($A = LL^T$):</strong> For symmetric positive definite matrices. More efficient than LU.</p>
        </div>

        <p><strong>Applications of matrix operations:</strong></p>
        <ul>
        <li><strong>Linear transformations:</strong> Multiplication by a matrix represents a linear map between vector spaces.</li>
        <li><strong>Least squares regression:</strong> Minimize $\\|A\\mathbf{x} - \\mathbf{b}\\|^2$ by solving $A^T A \\mathbf{x} = A^T \\mathbf{b}$.</li>
        <li><strong>Image compression:</strong> Use SVD to find low-rank approximations.</li>
        <li><strong>Computer graphics:</strong> Rotation, scaling, and projection matrices transform 3D coordinates.</li>
        <li><strong>Markov chains:</strong> Transition matrices model probabilistic systems.</li>
        <li><strong>Adjacency matrices:</strong> Represent graphs and networks; powers count paths.</li>
        </ul>

        <div class="worked-example">
        <p><strong>Example: Solving $A\\mathbf{x} = \\mathbf{b}$ using LU decomposition</strong></p>
        <div class="code-block">If $A = LU$, then $A\\mathbf{x} = \\mathbf{b}$ becomes $LU\\mathbf{x} = \\mathbf{b}$.
Let $\\mathbf{y} = U\\mathbf{x}$. Then:
1. Solve $L\\mathbf{y} = \\mathbf{b}$ (forward substitution)
2. Solve $U\\mathbf{x} = \\mathbf{y}$ (back substitution)

This is more efficient than computing $A^{-1}$ when solving multiple systems with the same $A$.</div>
        </div>

        <div class="success-box">
        <p><strong>Computational efficiency:</strong> Modern numerical libraries (LAPACK, NumPy) compute decompositions using optimized algorithms. For large matrices, sparse matrix techniques and iterative methods are essential.</p>
        </div>
        """
    }
]
