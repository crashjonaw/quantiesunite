TITLE = "Cofactor Expansion and General n×n Determinants"

SECTIONS = [
    {
        "title": "Minors, Cofactors, and Laplace Expansion",
        "body": """
        <p><strong>Minors and Cofactors:</strong> For an $n \\times n$ matrix $A$:</p>

        <p><strong>Minor $M_{ij}$:</strong> The determinant of the $(n-1) \\times (n-1)$ submatrix obtained by deleting row $i$ and column $j$.</p>

        <p><strong>Cofactor $C_{ij}$:</strong> The signed minor: $C_{ij} = (-1)^{i+j} M_{ij}$. The sign alternates in a checkerboard pattern.</p>

        <p><strong>Cofactor Expansion (Laplace Expansion):</strong> The determinant of $A$ can be computed by expanding along any row or column:</p>
        <pre class='code-block'>Expanding along row i:
$$\\det(A) = \\sum_{j} a_{ij} C_{ij} = \\sum_{j} a_{ij} (-1)^{i+j} M_{ij}$$

Expanding along column j:
$$\\det(A) = \\sum_{i} a_{ij} C_{ij} = \\sum_{i} a_{ij} (-1)^{i+j} M_{ij}$$</pre>

        <p><strong>Why this matters:</strong> Cofactor expansion reduces an $n \\times n$ determinant to $n$ determinants of size $(n-1) \\times (n-1)$, which can be computed recursively.</p>

        <p><strong>Computational complexity:</strong> For a general $n \\times n$ matrix, cofactor expansion has $O(n!)$ complexity—impractical for large $n$. Gaussian elimination is $O(n^3)$ and preferred.</p>
        """
    },
    {
        "title": "Examples and the Adjugate Matrix",
        "body": """
        <div class='worked-example'>
        <p><strong>Example: Cofactor expansion along the first row</strong></p>
        <pre class='code-block'>$$A = \\begin{bmatrix} 1 & 0 & 2 \\\\ 3 & 1 & 4 \\\\ 2 & 1 & 3 \\end{bmatrix}$$

$$\\det(A) = 1 \\cdot M_{11} - 0 \\cdot M_{12} + 2 \\cdot M_{13}$$

$$M_{11} = \\det\\begin{pmatrix} 1 & 4 \\\\ 1 & 3 \\end{pmatrix} = 1 \\cdot 3 - 4 \\cdot 1 = -1$$

$$M_{13} = \\det\\begin{pmatrix} 3 & 1 \\\\ 2 & 1 \\end{pmatrix} = 3 \\cdot 1 - 1 \\cdot 2 = 1$$

$$\\det(A) = 1 \\cdot (-1) - 0 + 2 \\cdot (1) = -1 + 2 = 1$$</pre>
        </div>

        <p><strong>Adjugate matrix:</strong> The matrix of cofactors (transposed) is called the adjugate (or adjoint) matrix:</p>
        <pre class='code-block'>$$\\text{adj}(A) = \\begin{bmatrix} C_{11} & C_{21} & \\cdots & C_{n1} \\\\ C_{12} & C_{22} & \\cdots & C_{n2} \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ C_{1n} & C_{2n} & \\cdots & C_{nn} \\end{bmatrix}$$</pre>

        <p>This is used in the inverse formula: $A^{-1} = \\frac{1}{\\det(A)} \\cdot \\text{adj}(A)$ (practical only for small matrices).</p>

        <div class='concept-box'>
        <p><strong>Matrix Inverse via Adjugate:</strong></p>
        <p>If $\\det(A) \\neq 0$, then $A^{-1} = \\frac{1}{\\det(A)} \\cdot \\text{adj}(A)$.</p>
        </div>
        """
    }
]
