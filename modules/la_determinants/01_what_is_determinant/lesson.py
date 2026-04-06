TITLE = "What is a Determinant?"

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

        <div class='worked-example'>
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
        """
    },
    {
        "title": "Geometric Interpretation",
        "body": """
        <p><strong>Geometric interpretation:</strong> The absolute value of the determinant is the volume of the parallelepiped (3D) or parallelogram (2D) spanned by the column vectors. The sign indicates orientation (whether the transformation preserves or reverses orientation).</p>

        <p><strong>Key fact:</strong> \(det(A) = 0\) if and only if the columns are linearly dependent (the matrix is singular/non-invertible). If \(det(A) \neq 0\), the matrix is invertible.</p>

        <div class='concept-box'>
        <p><strong>Invertibility Criterion:</strong></p>
        <p>A square matrix A is invertible if and only if \(det(A) \neq 0\).</p>
        </div>
        """
    }
]
