SECTIONS = [
    {
        "title": "Matrix Notation and Basic Operations",
        "body": """
        <h3>What is a Matrix?</h3>
        <p>A <strong>matrix</strong> is a rectangular array of numbers arranged in rows and columns.</p>

        <h4>Notation and Dimensions</h4>
        <p>A matrix with m rows and n columns is called an m × n matrix (read "m by n").</p>

        <p>$$\\mathbf{A} = \\begin{pmatrix} a_{11} & a_{12} & a_{13} \\\\ a_{21} & a_{22} & a_{23} \\\\ a_{31} & a_{32} & a_{33} \\end{pmatrix}$$</p>

        <p>This is a 3 × 3 matrix. Element \\(a_{ij}\\) is in row \\(i\\), column \\(j\\).</p>

        <div class="example-box">
            <p><strong>Example 1:</strong></p>
            <p>$$\\mathbf{A} = \\begin{pmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\end{pmatrix}$$</p>
            <p>This is a 2 × 3 matrix.</p>
            <ul>
                <li>\\(a_{11} = 1,\\ a_{12} = 2,\\ a_{13} = 3\\)</li>
                <li>\\(a_{21} = 4,\\ a_{22} = 5,\\ a_{23} = 6\\)</li>
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

        <p>$$\\mathbf{A} + \\mathbf{B} = \\begin{pmatrix} a_{11}+b_{11} & a_{12}+b_{12} \\\\ a_{21}+b_{21} & a_{22}+b_{22} \\end{pmatrix}$$</p>

        <div class="example-box">
            <p><strong>Example 2:</strong> Add matrices</p>
            <p>$$\\mathbf{A} = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}, \\quad \\mathbf{B} = \\begin{pmatrix} 5 & 6 \\\\ 7 & 8 \\end{pmatrix}$$</p>
            <p>$$\\mathbf{A} + \\mathbf{B} = \\begin{pmatrix} 6 & 8 \\\\ 10 & 12 \\end{pmatrix}$$</p>
        </div>

        <h4>Scalar Multiplication</h4>
        <p>Multiply each element by the scalar.</p>

        <p>$$k\\mathbf{A} = \\begin{pmatrix} ka_{11} & ka_{12} \\\\ ka_{21} & ka_{22} \\end{pmatrix}$$</p>

        <div class="example-box">
            <p><strong>Example 3:</strong> Scalar multiplication</p>
            <p>$$3\\mathbf{A} = 3 \\times \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix} = \\begin{pmatrix} 3 & 6 \\\\ 9 & 12 \\end{pmatrix}$$</p>
        </div>
        """
    },
    {
        "title": "Matrix Multiplication",
        "body": """
        <h3>Multiplying Matrices</h3>
        <p>Matrix multiplication is more complex than element-wise multiplication.</p>

        <h4>Compatibility</h4>
        <p>To multiply \\(\\mathbf{A}\\) (m × n) by \\(\\mathbf{B}\\) (n × p), the number of columns in \\(\\mathbf{A}\\) must equal the number of rows in \\(\\mathbf{B}\\). Result is m × p.</p>

        <h4>The Multiplication Process</h4>
        <p>To find element (i,j) in \\(\\mathbf{AB}\\):</p>
        <ol>
            <li>Take row i from matrix \\(\\mathbf{A}\\)</li>
            <li>Take column j from matrix \\(\\mathbf{B}\\)</li>
            <li>Multiply corresponding elements and sum</li>
        </ol>

        <div class="example-box">
            <p><strong>Example 4:</strong> Multiply 2×2 matrices</p>
            <p>$$\\mathbf{A} = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}, \\quad \\mathbf{B} = \\begin{pmatrix} 2 & 0 \\\\ 1 & 2 \\end{pmatrix}$$</p>
            <p><strong>\\(\\mathbf{AB}\\):</strong></p>
            <ul>
                <li>(1,1) entry: (1)(2) + (2)(1) = 2 + 2 = 4</li>
                <li>(1,2) entry: (1)(0) + (2)(2) = 0 + 4 = 4</li>
                <li>(2,1) entry: (3)(2) + (4)(1) = 6 + 4 = 10</li>
                <li>(2,2) entry: (3)(0) + (4)(2) = 0 + 8 = 8</li>
            </ul>
            <p>$$\\mathbf{AB} = \\begin{pmatrix} 4 & 4 \\\\ 10 & 8 \\end{pmatrix}$$</p>
        </div>

        <h4>Important Properties</h4>
        <ul>
            <li><strong>Not commutative:</strong> \\(\\mathbf{AB} \\neq \\mathbf{BA}\\) (order matters!)</li>
            <li><strong>Associative:</strong> \\((\\mathbf{AB})\\mathbf{C} = \\mathbf{A}(\\mathbf{BC})\\)</li>
            <li><strong>Distributive:</strong> \\(\\mathbf{A}(\\mathbf{B} + \\mathbf{C}) = \\mathbf{AB} + \\mathbf{AC}\\)</li>
            <li><strong>Identity:</strong> \\(\\mathbf{AI} = \\mathbf{IA} = \\mathbf{A}\\)</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 5:</strong> Show \\(\\mathbf{AB} \\neq \\mathbf{BA}\\)</p>
            <p>Using matrices from Example 4:</p>
            <p>$$\\mathbf{BA} = \\begin{pmatrix} 2 & 4 \\\\ 7 & 10 \\end{pmatrix}$$</p>
            <p>This is different from \\(\\mathbf{AB} = \\begin{pmatrix} 4 & 4 \\\\ 10 & 8 \\end{pmatrix}\\)</p>
        </div>
        """
    },
    {
        "title": "Determinant and Inverse of 2×2 Matrices",
        "body": """
        <h3>The Determinant</h3>
        <p>For a 2×2 matrix \\(\\mathbf{A} = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}\\), the <strong>determinant</strong> is:</p>

        <p>$$\\det(\\mathbf{A}) = |\\mathbf{A}| = ad - bc$$</p>

        <h4>Properties of Determinants</h4>
        <ul>
            <li>If \\(\\det(\\mathbf{A}) = 0\\), the matrix is singular (non-invertible)</li>
            <li>If \\(\\det(\\mathbf{A}) \\neq 0\\), the matrix is non-singular (invertible)</li>
            <li>\\(\\det(\\mathbf{AB}) = \\det(\\mathbf{A}) \\times \\det(\\mathbf{B})\\)</li>
            <li>\\(\\det(\\mathbf{A}^T) = \\det(\\mathbf{A})\\)</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 6:</strong> Find the determinant</p>
            <p>$$\\mathbf{A} = \\begin{pmatrix} 3 & 2 \\\\ 1 & 4 \\end{pmatrix}$$</p>
            <p>$$\\det(\\mathbf{A}) = (3)(4) - (2)(1) = 12 - 2 = 10$$</p>
        </div>

        <h3>The Inverse Matrix</h3>
        <p>For a 2×2 matrix with \\(\\det(\\mathbf{A}) \\neq 0\\):</p>

        <p>$$\\mathbf{A}^{-1} = \\frac{1}{\\det(\\mathbf{A})} \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}$$</p>

        <p>Note: Swap \\(a\\) and \\(d\\), negate \\(b\\) and \\(c\\), then multiply by \\(\\frac{1}{\\det(\\mathbf{A})}\\).</p>

        <div class="example-box">
            <p><strong>Example 7:</strong> Find the inverse</p>
            <p>$$\\mathbf{A} = \\begin{pmatrix} 3 & 2 \\\\ 1 & 4 \\end{pmatrix}, \\quad \\det(\\mathbf{A}) = 10$$</p>
            <p>$$\\mathbf{A}^{-1} = \\frac{1}{10} \\begin{pmatrix} 4 & -2 \\\\ -1 & 3 \\end{pmatrix} = \\begin{pmatrix} 0.4 & -0.2 \\\\ -0.1 & 0.3 \\end{pmatrix}$$</p>
        </div>

        <h4>Verification</h4>
        <p>\\(\\mathbf{A}\\mathbf{A}^{-1} = \\mathbf{I}\\) and \\(\\mathbf{A}^{-1}\\mathbf{A} = \\mathbf{I}\\)</p>

        <h4>Properties of Inverses</h4>
        <ul>
            <li>\\((\\mathbf{A}^{-1})^{-1} = \\mathbf{A}\\)</li>
            <li>\\((\\mathbf{AB})^{-1} = \\mathbf{B}^{-1}\\mathbf{A}^{-1}\\) (note the order!)</li>
            <li>If \\(\\mathbf{A}\\) is singular (det = 0), no inverse exists</li>
        </ul>
        """
    },
    {
        "title": "Solving Systems Using Matrices",
        "body": """
        <h3>Matrix Form of Linear Equations</h3>
        <p>A system of linear equations can be written as \\(\\mathbf{AX} = \\mathbf{B}\\), where:</p>
        <ul>
            <li><strong>A:</strong> Coefficient matrix</li>
            <li><strong>X:</strong> Variable matrix (column vector)</li>
            <li><strong>B:</strong> Constant matrix (column vector)</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 8:</strong> System: \\(2x + 3y = 7\\), \\(x - y = 1\\)</p>
            <p>Matrix form:</p>
            <p>$$\\begin{pmatrix} 2 & 3 \\\\ 1 & -1 \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\end{pmatrix} = \\begin{pmatrix} 7 \\\\ 1 \\end{pmatrix}$$</p>
        </div>

        <h4>Solving Using Matrix Inverse</h4>
        <p>If \\(\\mathbf{AX} = \\mathbf{B}\\), then \\(\\mathbf{X} = \\mathbf{A}^{-1}\\mathbf{B}\\)</p>

        <div class="example-box">
            <p><strong>Example 9:</strong> Solve using matrix inverse</p>
            <p>$$\\mathbf{A} = \\begin{pmatrix} 2 & 3 \\\\ 1 & -1 \\end{pmatrix}, \\quad \\mathbf{B} = \\begin{pmatrix} 7 \\\\ 1 \\end{pmatrix}$$</p>
            <p>$$\\det(\\mathbf{A}) = (2)(-1) - (3)(1) = -2 - 3 = -5$$</p>
            <p>$$\\mathbf{A}^{-1} = \\frac{1}{-5} \\begin{pmatrix} -1 & -3 \\\\ -1 & 2 \\end{pmatrix} = \\begin{pmatrix} \\frac{1}{5} & \\frac{3}{5} \\\\ \\frac{1}{5} & -\\frac{2}{5} \\end{pmatrix}$$</p>
            <p>$$\\mathbf{X} = \\mathbf{A}^{-1}\\mathbf{B} = \\begin{pmatrix} \\frac{1}{5} & \\frac{3}{5} \\\\ \\frac{1}{5} & -\\frac{2}{5} \\end{pmatrix} \\begin{pmatrix} 7 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 2 \\\\ 1 \\end{pmatrix}$$</p>
            <p>So \\(x = 2,\\ y = 1\\)</p>
        </div>

        <h4>When Does No Solution Exist?</h4>
        <p>If \\(\\det(\\mathbf{A}) = 0\\), the system either has no solution or infinite solutions. The matrix method cannot be used directly.</p>
        """
    },
    {
        "title": "Geometric Transformations Using Matrices",
        "body": """
        <h3>Representing Transformations as Matrices</h3>
        <p>A 2×2 matrix can represent geometric transformations in the plane.</p>

        <h4>Common Transformation Matrices</h4>
        <ul>
            <li><strong>Rotation by \\(\\theta\\) (counterclockwise):</strong> \\(\\begin{pmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \\end{pmatrix}\\)</li>
            <li><strong>Reflection across x-axis:</strong> \\(\\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix}\\)</li>
            <li><strong>Reflection across y-axis:</strong> \\(\\begin{pmatrix} -1 & 0 \\\\ 0 & 1 \\end{pmatrix}\\)</li>
            <li><strong>Reflection across y = x:</strong> \\(\\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}\\)</li>
            <li><strong>Scaling by factor k:</strong> \\(\\begin{pmatrix} k & 0 \\\\ 0 & k \\end{pmatrix}\\)</li>
            <li><strong>Stretch horizontally by k:</strong> \\(\\begin{pmatrix} k & 0 \\\\ 0 & 1 \\end{pmatrix}\\)</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 10:</strong> Rotate point (1, 0) by 90° counterclockwise</p>
            <p>Rotation matrix:</p>
            <p>$$\\begin{pmatrix} \\cos 90° & -\\sin 90° \\\\ \\sin 90° & \\cos 90° \\end{pmatrix} = \\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix}$$</p>
            <p>$$\\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix} \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 1 \\end{pmatrix}$$</p>
            <p>Point (1, 0) rotates to (0, 1) ✓</p>
        </div>

        <h4>Composite Transformations</h4>
        <p>Apply multiple transformations by multiplying matrices.</p>

        <div class="example-box">
            <p><strong>Example 11:</strong> Reflect across y-axis, then rotate 90°</p>
            <p>First apply: \\(\\mathbf{A} = \\begin{pmatrix} -1 & 0 \\\\ 0 & 1 \\end{pmatrix}\\) (reflect)</p>
            <p>Then apply: \\(\\mathbf{B} = \\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix}\\) (rotate)</p>
            <p>$$\\mathbf{BA} = \\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix} \\begin{pmatrix} -1 & 0 \\\\ 0 & 1 \\end{pmatrix} = \\begin{pmatrix} 0 & -1 \\\\ -1 & 0 \\end{pmatrix}$$</p>
        </div>

        <h4>Inverse Transformations</h4>
        <p>Use the inverse matrix to reverse a transformation.</p>

        <div class="example-box">
            <p><strong>Example 12:</strong> To reverse a 90° rotation, apply the inverse</p>
            <p>Rotation 90°: \\(\\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix}\\)</p>
            <p>Rotation −90° (inverse): \\(\\begin{pmatrix} 0 & 1 \\\\ -1 & 0 \\end{pmatrix}\\)</p>
        </div>
        """
    }
]
