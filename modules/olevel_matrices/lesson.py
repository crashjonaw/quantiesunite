SECTIONS = [
    {
        "title": "Matrix Notation and Basic Operations",
        "body": """
        <h3>What is a Matrix?</h3>
        <p>A <strong>matrix</strong> is a rectangular array of numbers arranged in rows and columns.</p>

        <h4>Notation and Dimensions</h4>
        <p>A matrix with m rows and n columns is called an m × n matrix (read "m by n").</p>

        <p style="text-align: center;"><strong>A = (</strong><span style="font-size: 1.2em;">
        a₁₁  a₁₂  a₁₃<br/>
        a₂₁  a₂₂  a₂₃<br/>
        a₃₁  a₃₂  a₃₃
        <strong>)</strong></span></p>

        <p>This is a 3 × 3 matrix. Element aᵢⱼ is in row i, column j.</p>

        <div class="example-box">
            <p><strong>Example 1:</strong> Matrix A = <strong>(</strong>
            <span style="font-size: 1.1em;">
            1  2  3<br/>
            4  5  6
            <strong>)</strong></span></p>
            <p>This is a 2 × 3 matrix.</p>
            <ul>
                <li>a₁₁ = 1, a₁₂ = 2, a₁₃ = 3</li>
                <li>a₂₁ = 4, a₂₂ = 5, a₂₃ = 6</li>
            </ul>
        </div>

        <h4>Special Matrix Types</h4>
        <ul>
            <li><strong>Square matrix:</strong> m = n (equal rows and columns)</li>
            <li><strong>Identity matrix (I):</strong> 1s on diagonal, 0s elsewhere</li>
            <li><strong>Zero matrix:</strong> All elements are 0</li>
            <li><strong>Row matrix:</strong> Single row (1 × n)</li>
            <li><strong>Column matrix:</strong> Single column (m × 1)</li>
        </ul>

        <h4>Matrix Addition and Subtraction</h4>
        <p>Add or subtract corresponding elements. Matrices must have the same dimensions.</p>

        <p style="text-align: center;">
        <strong>A + B = (</strong>a₁₁+b₁₁  a₁₂+b₁₂<br/>a₂₁+b₂₁  a₂₂+b₂₂<strong>)</strong>
        </p>

        <div class="example-box">
            <p><strong>Example 2:</strong> Add matrices</p>
            <p><strong>A = (</strong><span style="font-size: 1em;">1  2<br/>3  4<strong>)</strong></span>, <strong>B = (</strong><span style="font-size: 1em;">5  6<br/>7  8<strong>)</strong></span></p>
            <p><strong>A + B = (</strong><span style="font-size: 1em;">6  8<br/>10  12<strong>)</strong></span></p>
        </div>

        <h4>Scalar Multiplication</h4>
        <p>Multiply each element by the scalar.</p>

        <p style="text-align: center;">
        <strong>kA = (</strong>ka₁₁  ka₁₂<br/>ka₂₁  ka₂₂<strong>)</strong>
        </p>

        <div class="example-box">
            <p><strong>Example 3:</strong> Scalar multiplication</p>
            <p><strong>3A = 3 × (</strong><span style="font-size: 1em;">1  2<br/>3  4<strong>) = (</strong><span style="font-size: 1em;">3  6<br/>9  12<strong>)</strong></span></p>
        </div>
        """
    },
    {
        "title": "Matrix Multiplication",
        "body": """
        <h3>Multiplying Matrices</h3>
        <p>Matrix multiplication is more complex than element-wise multiplication.</p>

        <h4>Compatibility</h4>
        <p>To multiply A (m × n) by B (n × p), the number of columns in A must equal the number of rows in B. Result is m × p.</p>

        <h4>The Multiplication Process</h4>
        <p>To find element (i,j) in AB:</p>
        <ol>
            <li>Take row i from matrix A</li>
            <li>Take column j from matrix B</li>
            <li>Multiply corresponding elements and sum</li>
        </ol>

        <div class="example-box">
            <p><strong>Example 4:</strong> Multiply 2×2 matrices</p>
            <p><strong>A = (</strong><span style="font-size: 1em;">1  2<br/>3  4<strong>)</strong></span>, <strong>B = (</strong><span style="font-size: 1em;">2  0<br/>1  2<strong>)</strong></span></p>
            <p><strong>AB:</strong></p>
            <ul>
                <li>(1,1) entry: (1)(2) + (2)(1) = 2 + 2 = 4</li>
                <li>(1,2) entry: (1)(0) + (2)(2) = 0 + 4 = 4</li>
                <li>(2,1) entry: (3)(2) + (4)(1) = 6 + 4 = 10</li>
                <li>(2,2) entry: (3)(0) + (4)(2) = 0 + 8 = 8</li>
            </ul>
            <p><strong>AB = (</strong><span style="font-size: 1em;">4  4<br/>10  8<strong>)</strong></span></p>
        </div>

        <h4>Important Properties</h4>
        <ul>
            <li><strong>Not commutative:</strong> AB ≠ BA (order matters!)</li>
            <li><strong>Associative:</strong> (AB)C = A(BC)</li>
            <li><strong>Distributive:</strong> A(B + C) = AB + AC</li>
            <li><strong>Identity:</strong> AI = IA = A (where I is identity matrix)</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 5:</strong> Show AB ≠ BA</p>
            <p>Using matrices from Example 4:</p>
            <p><strong>BA = (</strong><span style="font-size: 1em;">2  4<br/>7  10<strong>)</strong></span></p>
            <p>This is different from AB = <strong>(</strong><span style="font-size: 1em;">4  4<br/>10  8<strong>)</strong></span></p>
        </div>
        """
    },
    {
        "title": "Determinant and Inverse of 2×2 Matrices",
        "body": """
        <h3>The Determinant</h3>
        <p>For a 2×2 matrix <strong>A = (</strong><span style="font-size: 1em;">a  b<br/>c  d<strong>)</strong></span>, the <strong>determinant</strong> is:</p>

        <p style="text-align: center; font-size: 1.2em;"><strong>det(A) = |A| = ad − bc</strong></p>

        <h4>Properties of Determinants</h4>
        <ul>
            <li>If det(A) = 0, the matrix is singular (non-invertible)</li>
            <li>If det(A) ≠ 0, the matrix is non-singular (invertible)</li>
            <li>det(AB) = det(A) × det(B)</li>
            <li>det(A^T) = det(A) (determinant of transpose)</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 6:</strong> Find the determinant</p>
            <p><strong>A = (</strong><span style="font-size: 1em;">3  2<br/>1  4<strong>)</strong></span></p>
            <p>det(A) = (3)(4) − (2)(1) = 12 − 2 = 10</p>
        </div>

        <h3>The Inverse Matrix</h3>
        <p>For a 2×2 matrix with det(A) ≠ 0:</p>

        <p style="text-align: center; font-size: 1.2em;">
        <strong>A⁻¹ = (1/det(A)) × (</strong><span style="font-size: 1em;">d  −b<br/>−c  a<strong>)</strong></span>
        </p>

        <p>Note: Swap a and d, negate b and c, then multiply by 1/det(A).</p>

        <div class="example-box">
            <p><strong>Example 7:</strong> Find the inverse</p>
            <p><strong>A = (</strong><span style="font-size: 1em;">3  2<br/>1  4<strong>)</strong></span>, det(A) = 10</p>
            <p><strong>A⁻¹ = (1/10) × (</strong><span style="font-size: 1em;">4  −2<br/>−1  3<strong>) = (</strong><span style="font-size: 1em;">0.4  −0.2<br/>−0.1  0.3<strong>)</strong></span></p>
        </div>

        <h4>Verification</h4>
        <p><strong>AA⁻¹ = I</strong> and <strong>A⁻¹A = I</strong></p>

        <h4>Properties of Inverses</h4>
        <ul>
            <li>(A⁻¹)⁻¹ = A</li>
            <li>(AB)⁻¹ = B⁻¹A⁻¹ (note the order!)</li>
            <li>If A is singular (det = 0), no inverse exists</li>
        </ul>
        """
    },
    {
        "title": "Solving Systems Using Matrices",
        "body": """
        <h3>Matrix Form of Linear Equations</h3>
        <p>A system of linear equations can be written as <strong>AX = B</strong>, where:</p>
        <ul>
            <li><strong>A:</strong> Coefficient matrix</li>
            <li><strong>X:</strong> Variable matrix (column vector)</li>
            <li><strong>B:</strong> Constant matrix (column vector)</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 8:</strong> System: 2x + 3y = 7, x − y = 1</p>
            <p>Matrix form: <strong>(</strong><span style="font-size: 1em;">2  3<br/>1  −1<strong>)(</strong><span style="font-size: 1em;">x<br/>y<strong>) = (</strong><span style="font-size: 1em;">7<br/>1<strong>)</strong></span></p>
        </div>

        <h4>Solving Using Matrix Inverse</h4>
        <p>If <strong>AX = B</strong>, then <strong>X = A⁻¹B</strong></p>

        <div class="example-box">
            <p><strong>Example 9:</strong> Solve using matrix inverse</p>
            <p><strong>A = (</strong><span style="font-size: 1em;">2  3<br/>1  −1<strong>)</strong></span>, <strong>B = (</strong><span style="font-size: 1em;">7<br/>1<strong>)</strong></span></p>
            <p>det(A) = (2)(−1) − (3)(1) = −2 − 3 = −5</p>
            <p><strong>A⁻¹ = (−1/5)(</strong><span style="font-size: 1em;">−1  −3<br/>−1  2<strong>) = (</strong><span style="font-size: 1em;">1/5  3/5<br/>1/5  −2/5<strong>)</strong></span></p>
            <p><strong>X = A⁻¹B = (</strong><span style="font-size: 1em;">1/5  3/5<br/>1/5  −2/5<strong>)(</strong><span style="font-size: 1em;">7<br/>1<strong>)</strong></span></p>
            <p><strong>X = (</strong><span style="font-size: 1em;">7/5 + 3/5<br/>7/5 − 2/5<strong>) = (</strong><span style="font-size: 1em;">2<br/>1<strong>)</strong></span></p>
            <p>So x = 2, y = 1</p>
        </div>

        <h4>When Does No Solution Exist?</h4>
        <p>If det(A) = 0, the system either has no solution or infinite solutions. The matrix method cannot be used directly.</p>
        """
    },
    {
        "title": "Geometric Transformations Using Matrices",
        "body": """
        <h3>Representing Transformations as Matrices</h3>
        <p>A 2×2 matrix can represent geometric transformations in the plane.</p>

        <h4>Common Transformation Matrices</h4>
        <ul>
            <li><strong>Rotation by θ (counterclockwise):</strong> <strong>(</strong>cos θ  −sin θ<br/>sin θ  cos θ<strong>)</strong></li>
            <li><strong>Reflection across x-axis:</strong> <strong>(</strong>1  0<br/>0  −1<strong>)</strong></li>
            <li><strong>Reflection across y-axis:</strong> <strong>(</strong>−1  0<br/>0  1<strong>)</strong></li>
            <li><strong>Reflection across y=x:</strong> <strong>(</strong>0  1<br/>1  0<strong>)</strong></li>
            <li><strong>Scaling by factor k:</strong> <strong>(</strong>k  0<br/>0  k<strong>)</strong></li>
            <li><strong>Stretch horizontally by k:</strong> <strong>(</strong>k  0<br/>0  1<strong>)</strong></li>
        </ul>

        <div class="example-box">
            <p><strong>Example 10:</strong> Rotate point (1, 0) by 90° counterclockwise</p>
            <p>Rotation matrix: <strong>(</strong><span style="font-size: 1em;">cos 90°  −sin 90°<br/>sin 90°  cos 90°<strong>) = (</strong><span style="font-size: 1em;">0  −1<br/>1  0<strong>)</strong></span></p>
            <p><strong>(</strong><span style="font-size: 1em;">0  −1<br/>1  0<strong>)(</strong><span style="font-size: 1em;">1<br/>0<strong>) = (</strong><span style="font-size: 1em;">0<br/>1<strong>)</strong></span></p>
            <p>Point (1, 0) rotates to (0, 1) ✓</p>
        </div>

        <h4>Composite Transformations</h4>
        <p>Apply multiple transformations by multiplying matrices.</p>

        <div class="example-box">
            <p><strong>Example 11:</strong> Reflect across y-axis, then rotate 90°</p>
            <p>First apply: <strong>A = (</strong><span style="font-size: 1em;">−1  0<br/>0  1<strong>)</strong></span> (reflect)</p>
            <p>Then apply: <strong>B = (</strong><span style="font-size: 1em;">0  −1<br/>1  0<strong>)</strong></span> (rotate)</p>
            <p>Combined: <strong>BA = (</strong><span style="font-size: 1em;">0  −1<br/>1  0<strong>)(</strong><span style="font-size: 1em;">−1  0<br/>0  1<strong>) = (</strong><span style="font-size: 1em;">0  −1<br/>−1  0<strong>)</strong></span></p>
        </div>

        <h4>Inverse Transformations</h4>
        <p>Use the inverse matrix to reverse a transformation.</p>

        <div class="example-box">
            <p><strong>Example 12:</strong> To reverse a 90° rotation, apply the inverse</p>
            <p>Rotation 90°: <strong>(</strong><span style="font-size: 1em;">0  −1<br/>1  0<strong>)</strong></span></p>
            <p>Rotation −90° (inverse): <strong>(</strong><span style="font-size: 1em;">0  1<br/>−1  0<strong>)</strong></span></p>
        </div>
        """
    }
]
