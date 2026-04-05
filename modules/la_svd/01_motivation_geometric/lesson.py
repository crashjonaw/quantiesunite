TITLE = "Motivation and Geometric Interpretation"

SECTIONS = [
    {
        "title": "What is Singular Value Decomposition?",
        "body": """
        <p><strong>Singular Value Decomposition (SVD):</strong> Any $m \\times n$ matrix $A$ can be factored as:</p>
        <p>$$A = U\\Sigma V^T$$</p>

        <p>where:</p>
        <ul>
        <li>$U$ is an $m \\times m$ orthogonal matrix (left singular vectors)</li>
        <li>$\\Sigma$ is an $m \\times n$ diagonal matrix with $\\sigma_1 \\geq \\sigma_2 \\geq \\cdots \\geq \\sigma_r > 0$ (singular values)</li>
        <li>$V$ is an $n \\times n$ orthogonal matrix (right singular vectors)</li>
        <li>$r = \\text{rank}(A)$</li>
        </ul>

        <p><strong>Key advantages of SVD:</strong></p>
        <ul>
        <li><strong>Universal:</strong> The SVD exists for any matrix (unlike eigendecomposition which requires square matrices)</li>
        <li><strong>Real values:</strong> Singular values $\\sigma_i$ are always non-negative and real</li>
        <li><strong>Rank information:</strong> $\\text{rank}(A)$ = number of nonzero singular values</li>
        <li><strong>Orthonormal bases:</strong> $U$ and $V$ provide orthonormal bases for fundamental subspaces of $A$</li>
        </ul>

        <div class='concept-box'>
        <p><strong>Fundamental subspaces from SVD:</strong></p>
        <ul>
        <li>First $r$ columns of $U$: orthonormal basis for $\\text{Col}(A)$ (column space)</li>
        <li>Last $m - r$ columns of $U$: orthonormal basis for $\\text{Null}(A^T)$ (left nullspace)</li>
        <li>First $r$ columns of $V$: orthonormal basis for $\\text{Row}(A)$ (row space)</li>
        <li>Last $n - r$ columns of $V$: orthonormal basis for $\\text{Null}(A)$ (nullspace)</li>
        </ul>
        </div>
        """
    },
    {
        "title": "Geometric Interpretation",
        "body": """
        <p><strong>Linear transformations as three steps:</strong> Any linear transformation $A: \\mathbb{R}^n \\to \\mathbb{R}^m$ decomposes into three simple geometric operations:</p>

        <ol>
        <li><strong>$V^T$:</strong> Rotation (or reflection) in $\\mathbb{R}^n$ that aligns axes with principal directions</li>
        <li><strong>$\\Sigma$:</strong> Scaling: stretch/shrink along each axis by $\\sigma_1, \\sigma_2, \\ldots, \\sigma_n$ (no mixing)</li>
        <li><strong>$U$:</strong> Rotation (or reflection) in $\\mathbb{R}^m$ to align with the output space</li>
        </ol>

        <p>Mathematically: $A$ = (rotation in output space) $\\times$ (scaling) $\\times$ (rotation in input space)</p>

        <p><strong>Singular values as stretching factors:</strong> The singular value $\\sigma_j$ tells us how much the transformation stretches vectors in the $j$-th principal direction. If $\\sigma_1 = 10$ and $\\sigma_2 = 1$, the transformation stretches along direction $\\mathbf{v}_1$ much more than direction $\\mathbf{v}_2$.</p>

        <div class='worked-example'>
        <p><strong>Example: SVD of a $2 \\times 2$ matrix</strong></p>
        <pre class='code-block'>$$A = \\begin{bmatrix} 1 & 0 \\\\ 0 & 2 \\end{bmatrix}$$

$$A^T A = \\begin{bmatrix} 1 & 0 \\\\ 0 & 2 \\end{bmatrix} \\begin{bmatrix} 1 & 0 \\\\ 0 & 2 \\end{bmatrix} = \\begin{bmatrix} 1 & 0 \\\\ 0 & 4 \\end{bmatrix}$$

Eigenvalues of $A^T A$: $\\lambda_1 = 4$, $\\lambda_2 = 1$
Eigenvectors ($V$): $\\mathbf{v}_1 = [0, 1]^T$, $\\mathbf{v}_2 = [1, 0]^T$

Singular values: $\\sigma_1 = \\sqrt{4} = 2$, $\\sigma_2 = \\sqrt{1} = 1$

Left singular vectors:
$\\mathbf{u}_1 = \\frac{1}{\\sigma_1} A\\mathbf{v}_1 = \\frac{1}{2} A[0, 1]^T = \\frac{1}{2}[0, 2]^T = [0, 1]^T$
$\\mathbf{u}_2 = \\frac{1}{\\sigma_2} A\\mathbf{v}_2 = \\frac{1}{1} A[1, 0]^T = [1, 0]^T$

$$U = \\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix} \\quad \\Sigma = \\begin{bmatrix} 2 & 0 \\\\ 0 & 1 \\end{bmatrix} \\quad V = \\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix}$$

Check: $U\\Sigma V^T = A$ ✓</pre>
        </div>

        <p><strong>Interpretation of this example:</strong> The transformation $A$ stretches the $y$-axis by factor 2 ($\\sigma_1 = 2$) and the $x$-axis by factor 1 ($\\sigma_2 = 1$). The matrix is already aligned with the coordinate axes, so $U$ and $V$ are just reorderings.</p>

        <div class='success-box'>
        <p><strong>Why this matters:</strong> SVD reveals the hidden "shape" of a linear transformation. Every matrix, no matter how complicated, can be understood as: align axes, scale, rotate. This geometric understanding makes many applications possible.</p>
        </div>
        """
    }
]
