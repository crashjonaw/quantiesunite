TITLE = "Transpose and Special Matrices"

SECTIONS = [
    {
        "title": "The Transpose Operation",
        "body": """
        <div class="concept-box">
        <p><strong>Transpose Definition:</strong> The transpose of an \\(m \\times n\\) matrix \\(\\mathbf{A}\\), denoted \\(\\mathbf{A}^T\\), is the \\(n \\times m\\) matrix obtained by swapping rows and columns:</p>
        <p>$$(\\mathbf{A}^T)_{ij} = a_{ji}$$</p>
        </div>

        <p><strong>Properties of transpose:</strong></p>
        <ul>
        <li>\\((\\mathbf{A}^T)^T = \\mathbf{A}\\) (double transpose is the original)</li>
        <li>\\((\\mathbf{A} + \\mathbf{B})^T = \\mathbf{A}^T + \\mathbf{B}^T\\)</li>
        <li>\\((c\\mathbf{A})^T = c\\mathbf{A}^T\\)</li>
        <li>\\((\\mathbf{AB})^T = \\mathbf{B}^T \\mathbf{A}^T\\) (order reverses!)</li>
        <li>\\((\\mathbf{A}^{-1})^T = (\\mathbf{A}^T)^{-1}\\) (if \\(\\mathbf{A}\\) is invertible)</li>
        </ul>

        <div class="worked-example">
        <p><strong>Example: Transpose Computation</strong></p>
        <p>$$\\mathbf{A} = \\begin{pmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\end{pmatrix}, \\quad \\mathbf{A}^T = \\begin{pmatrix} 1 & 4 \\\\ 2 & 5 \\\\ 3 & 6 \\end{pmatrix}$$</p>
        </div>

        <div class="warning-box">
        <p><strong>Order matters in \\((\\mathbf{AB})^T = \\mathbf{B}^T\\mathbf{A}^T\\):</strong> Notice the order reversal! This is not \\((\\mathbf{AB})^T = \\mathbf{A}^T\\mathbf{B}^T\\). The order of multiplication reverses when you transpose a product.</p>
        </div>
        """
    },
    {
        "title": "Symmetric and Skew-Symmetric Matrices",
        "body": """
        <div class="concept-box">
        <p><strong>Symmetric matrices:</strong> A square matrix \\(\\mathbf{A}\\) is symmetric if \\(\\mathbf{A}^T = \\mathbf{A}\\) (equivalently, \\(a_{ij} = a_{ji}\\) for all \\(i, j\\)). Symmetric matrices are crucial in mathematics and applications (covariance matrices, Hessians in optimization, etc.).</p>
        </div>

        <div class="concept-box">
        <p><strong>Skew-symmetric matrices:</strong> \\(\\mathbf{A}\\) is skew-symmetric if \\(\\mathbf{A}^T = -\\mathbf{A}\\). All diagonal entries must be 0 (since \\(a_{ii} = -a_{ii}\\) implies \\(a_{ii} = 0\\)).</p>
        </div>

        <div class="worked-example">
        <p><strong>Example: Symmetric and Skew-symmetric Matrices</strong></p>
        <p>$$\\mathbf{S} = \\begin{pmatrix} 1 & 2 & 3 \\\\ 2 & 5 & 4 \\\\ 3 & 4 & 6 \\end{pmatrix} \\text{ is symmetric because } \\mathbf{S}^T = \\mathbf{S}$$</p>
        <p>$$\\mathbf{K} = \\begin{pmatrix} 0 & 2 & -3 \\\\ -2 & 0 & 1 \\\\ 3 & -1 & 0 \\end{pmatrix} \\text{ is skew-symmetric because } \\mathbf{K}^T = -\\mathbf{K}$$</p>
        </div>

        <div class="success-box">
        <p><strong>Decomposition:</strong> Any matrix can be uniquely written as \\(\\mathbf{A} = \\mathbf{S} + \\mathbf{K}\\) where \\(\\mathbf{S}\\) is symmetric and \\(\\mathbf{K}\\) is skew-symmetric. This decomposition reveals the underlying structure.</p>
        </div>
        """
    },
    {
        "title": "Special Matrix Forms",
        "body": """
        <p><strong>Special matrix forms:</strong></p>
        <ul>
        <li><strong>Diagonal matrix:</strong> All off-diagonal entries are 0: \\(\\text{diag}(d_1, d_2, \\ldots, d_n)\\)</li>
        <li><strong>Upper triangular:</strong> All entries below the diagonal are 0</li>
        <li><strong>Lower triangular:</strong> All entries above the diagonal are 0</li>
        <li><strong>Orthogonal matrix:</strong> \\(\\mathbf{A}^T \\mathbf{A} = \\mathbf{I}\\) (rows and columns are orthonormal)</li>
        </ul>

        <div class="success-box">
        <p><strong>Why these forms matter:</strong> These special structures enable efficient algorithms. Triangular systems are easy to solve (\\(O(n^2)\\) instead of \\(O(n^3)\\)), and orthogonal matrices preserve geometry (distances, angles).</p>
        </div>

        <p><strong>Useful identities:</strong></p>
        <ul>
        <li>For any matrix \\(\\mathbf{A}\\), both \\(\\mathbf{A}^T\\mathbf{A}\\) and \\(\\mathbf{A}\\mathbf{A}^T\\) are symmetric matrices.</li>
        <li>\\(\\mathbf{A} + \\mathbf{A}^T\\) is always symmetric; \\(\\mathbf{A} - \\mathbf{A}^T\\) is always skew-symmetric.</li>
        </ul>
        """
    }
]
