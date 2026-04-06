TITLE = "Properties of Determinants and Row Operations"

SECTIONS = [
    {
        "title": "Fundamental Properties of Determinants",
        "body": """
        <p><strong>Fundamental properties of determinants:</strong></p>

        <p><strong>1. Multiplicativity:</strong> \(det(AB) = det(A) \cdot det(B)\). For square matrices, the determinant of a product is the product of determinants.</p>

        <p><strong>2. Transpose:</strong> \(det(A^T) = det(A)\). The determinant of the transpose equals the original.</p>

        <p><strong>3. Invertibility:</strong> A is invertible iff \(det(A) \neq 0\). And \(det(A^{-1}) = 1/det(A)\).</p>

        <p><strong>4. Determinant of scalar multiple:</strong> \(det(cA) = c^n \cdot det(A)\) for an \(n \times n\) matrix (each of n rows is scaled).</p>

        <div class='concept-box'>
        <p><strong>Special Determinants:</strong></p>
        <ul>
        <li><strong>Identity matrix I:</strong> \(det(I) = 1\)</li>
        <li><strong>Diagonal matrix:</strong> \(det(diag(d_1, \ldots, d_n)) = d_1 \cdot d_2 \cdot \ldots \cdot d_n\) (product of diagonal entries)</li>
        <li><strong>Triangular matrix:</strong> \(det\) = product of diagonal entries</li>
        <li><strong>Singular matrix:</strong> \(det(A) = 0\) (not invertible)</li>
        </ul>
        </div>
        """
    },
    {
        "title": "Row Operations and Determinant Calculation",
        "body": """
        <p><strong>Effect of row operations on determinant:</strong></p>

        <ul>
        <li><strong>Row swap (R<sub>i</sub> ↔ R<sub>j</sub>):</strong> det → -det (sign change)</li>
        <li><strong>Row scaling (cR<sub>i</sub> → R<sub>i</sub>):</strong> det → c·det (multiply by scalar c)</li>
        <li><strong>Row addition (R<sub>i</sub> + cR<sub>j</sub> → R<sub>i</sub>):</strong> det → det (unchanged)</li>
        </ul>

        <p><strong>Why this matters for Gaussian elimination:</strong> When converting A to REF via row operations, we can track the determinant. If A is row-reduced to an upper triangular U, then:</p>
        <pre class='code-block'>\(det(A)\) = (sign factor) × (product of diagonal entries of U)</pre>

        <p>The sign factor accounts for row swaps (each swap multiplies by -1).</p>

        <div class='worked-example'>
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
        """
    }
]
