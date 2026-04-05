TITLE = "Matrix Representation (Ax = b)"

SECTIONS = [
    {
        "title": "Compact Matrix Notation",
        "body": """
<h3>Representing Systems as Matrices</h3>
<p>Instead of writing out all equations, we can express the system compactly as:</p>

$$A\\mathbf{x} = \\mathbf{b}$$

<div class="concept-box">
<p>where:</p>
<ul>
<li>\\(A\\) is the \\(m \\times n\\) <strong>coefficient matrix</strong></li>
<li>\\(\\mathbf{x}\\) is the \\(n \\times 1\\) <strong>unknown vector</strong></li>
<li>\\(\\mathbf{b}\\) is the \\(m \\times 1\\) <strong>constant vector</strong></li>
</ul>
</div>

<h4>Explicit Forms</h4>

<p><strong>Coefficient matrix A:</strong></p>
$$A = \\begin{pmatrix}
a_{11} & a_{12} & \\cdots & a_{1n} \\\\
a_{21} & a_{22} & \\cdots & a_{2n} \\\\
\\vdots & \\vdots & \\ddots & \\vdots \\\\
a_{m1} & a_{m2} & \\cdots & a_{mn}
\\end{pmatrix}$$

<p><strong>Unknown vector:</strong></p>
$$\\mathbf{x} = \\begin{pmatrix} x_1 \\\\ x_2 \\\\ \\vdots \\\\ x_n \\end{pmatrix}$$

<p><strong>Constant vector:</strong></p>
$$\\mathbf{b} = \\begin{pmatrix} b_1 \\\\ b_2 \\\\ \\vdots \\\\ b_m \\end{pmatrix}$$

<div class="success-box">
<h4>Benefit of Matrix Form</h4>
<p>Matrix notation is compact, powerful, and enables efficient computation. Algorithms (like Gaussian elimination) operate directly on matrices.</p>
</div>
"""
    },
    {
        "title": "The Augmented Matrix",
        "body": """
<h3>Definition: Augmented Matrix</h3>
<p>The <strong>augmented matrix</strong> \\([A | \\mathbf{b}]\\) combines the coefficient matrix and constant vector:</p>

$$[A | \\mathbf{b}] = \\left[\\begin{array}{cccc|c}
a_{11} & a_{12} & \\cdots & a_{1n} & b_1 \\\\
a_{21} & a_{22} & \\cdots & a_{2n} & b_2 \\\\
\\vdots & \\vdots & \\ddots & \\vdots & \\vdots \\\\
a_{m1} & a_{m2} & \\cdots & a_{mn} & b_m
\\end{array}\\right]$$

<p>The vertical bar is a visual separator; it's still an \\(m \\times (n+1)\\) matrix mathematically.</p>

<div class="concept-box">
<h4>Why Augmented Matrices?</h4>
<p>The augmented matrix is a <em>complete encoding</em> of the system. We can perform row operations on it to solve the system without explicitly writing equations every time.</p>
</div>

<div class="worked-example">
<h4>Example: Building an Augmented Matrix</h4>
<p><strong>System:</strong></p>
$$\\begin{align}
2x + 3y - z &= 5 \\\\
x - y + 2z &= 3 \\\\
3x + 2y &= 1
\\end{align}$$

<p><strong>Coefficient matrix A:</strong></p>
$$A = \\begin{pmatrix}
2 & 3 & -1 \\\\
1 & -1 & 2 \\\\
3 & 2 & 0
\\end{pmatrix}$$

<p><strong>Constant vector b:</strong></p>
$$\\mathbf{b} = \\begin{pmatrix} 5 \\\\ 3 \\\\ 1 \\end{pmatrix}$$

<p><strong>Augmented matrix [A|b]:</strong></p>
$$\\left[\\begin{array}{ccc|c}
2 & 3 & -1 & 5 \\\\
1 & -1 & 2 & 3 \\\\
3 & 2 & 0 & 1
\\end{array}\\right]$$
</div>

<div class="warning-box">
<h4>Common Mistake</h4>
<p>Do not forget the last column (the constant vector \\(\\mathbf{b}\\)). The augmented matrix must include all terms from each equation, including the right-hand side.</p>
</div>
"""
    },
    {
        "title": "Elementary Row Operations",
        "body": """
<h3>The Three Elementary Row Operations</h3>
<p>We can manipulate the augmented matrix using three types of operations that <em>preserve the solution set</em>:</p>

<div class="concept-box">
<h4>Operation 1: Row Swap</h4>
<p><strong>Notation:</strong> \\(R_i \\leftrightarrow R_j\\)</p>
<p>Interchange two rows. Mathematically, this just reorders the equations, so the solution set stays the same.</p>

<h4>Operation 2: Row Scaling</h4>
<p><strong>Notation:</strong> \\(R_i \\rightarrow c \\cdot R_i\\) (where \\(c \\neq 0\\))</p>
<p>Multiply a row by a non-zero constant. If \\(x\\) satisfies \\(a_1 x_1 + \\cdots + a_n x_n = b\\), it also satisfies \\(ca_1 x_1 + \\cdots + ca_n x_n = cb\\).</p>

<h4>Operation 3: Row Addition</h4>
<p><strong>Notation:</strong> \\(R_i \\rightarrow R_i + c \\cdot R_j\\)</p>
<p>Add a multiple of one row to another. If \\(x\\) satisfies both equations \\(i\\) and \\(j\\), it satisfies their sum.</p>
</div>

<div class="worked-example">
<h4>Example: Using Row Operations</h4>
<p><strong>Original system:</strong></p>
$$\\begin{align}
2x + 3y &= 7 \\\\
x - y &= 1
\\end{align}$$

<p><strong>Augmented matrix:</strong></p>
$$\\left[\\begin{array}{cc|c}
2 & 3 & 7 \\\\
1 & -1 & 1
\\end{array}\\right]$$

<p><strong>Step 1:</strong> \\(R_1 \\leftrightarrow R_2\\) (swap rows to get a leading 1)</p>
$$\\left[\\begin{array}{cc|c}
1 & -1 & 1 \\\\
2 & 3 & 7
\\end{array}\\right]$$

<p><strong>Step 2:</strong> \\(R_2 \\rightarrow R_2 - 2R_1\\) (eliminate below the pivot)</p>
$$\\left[\\begin{array}{cc|c}
1 & -1 & 1 \\\\
0 & 5 & 5
\\end{array}\\right]$$

<p><strong>Step 3:</strong> \\(R_2 \\rightarrow \\frac{1}{5}R_2\\) (simplify)</p>
$$\\left[\\begin{array}{cc|c}
1 & -1 & 1 \\\\
0 & 1 & 1
\\end{array}\\right]$$

<p><strong>Back-substitution:</strong> From row 2: \\(y = 1\\). From row 1: \\(x - 1 = 1\\), so \\(x = 2\\).</p>

<p><strong>Solution:</strong> \\((x, y) = (2, 1)\\)</p>
</div>

<div class="success-box">
<h4>Row Equivalence</h4>
<p>Two matrices are <strong>row equivalent</strong> if one can be obtained from the other by a sequence of row operations. Row-equivalent augmented matrices represent systems with identical solution sets.</p>
</div>
"""
    }
]
