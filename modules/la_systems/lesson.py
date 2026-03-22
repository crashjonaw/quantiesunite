SECTIONS = [
    {
        "title": "Fundamental Definitions: Linear Equations and Systems",
        "body": """
<h3>Linear Equation (First-Principles Definition)</h3>
<p>A <strong>linear equation in n variables</strong> \\(x_1, x_2, \ldots, x_n\\) is an equation of the form:</p>

$$a_1 x_1 + a_2 x_2 + \cdots + a_n x_n = b$$

<p>where \\(a_1, a_2, \ldots, a_n, b \\in \\mathbb{R}\\) (or \\(\\mathbb{C}\\)), and "linear" means each variable appears with exponent exactly 1 (no squares, products, or transcendental functions).</p>

<h3>System of Linear Equations</h3>
<p>A <strong>system of m linear equations in n unknowns</strong> is a collection:</p>

$$\\begin{align}
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n &= b_1 \\\\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n &= b_2 \\\\
&\\vdots \\\\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n &= b_m
\\end{align}$$

<p>A <strong>solution</strong> is a vector \\((x_1^*, x_2^*, \ldots, x_n^*) \\in \\mathbb{R}^n\\) that satisfies <em>all m equations simultaneously</em>.</p>

<div class="example-box">
<h4>Example System</h4>
$$\\begin{align}
2x + 3y &= 8 \\\\
x - y &= 1
\\end{align}$$
<p>A solution would be values of \\(x\\) and \\(y\\) making both equations true. By inspection or solving: \\(x = 2, y = \frac{4}{3}\\) works? Let's check: \\(2(2) + 3(\frac{4}{3}) = 4 + 4 = 8\\) ✓ and \\(2 - \frac{4}{3} = \frac{2}{3} \\neq 1\\) ✗. Solving correctly: from the second equation, \\(x = y + 1\\). Substitute: \\(2(y+1) + 3y = 8\\), so \\(5y + 2 = 8\\), thus \\(y = \frac{6}{5}\\) and \\(x = \frac{11}{5}\\).</p>
</div>

<h3>Matrix Representation</h3>
<p>The system can be written compactly as:</p>

$$A\\mathbf{x} = \\mathbf{b}$$

<p>where \\(A\\) is the \\(m \\times n\\) <strong>coefficient matrix</strong>:</p>

$$A = \\begin{pmatrix}
a_{11} & a_{12} & \\cdots & a_{1n} \\\\
a_{21} & a_{22} & \\cdots & a_{2n} \\\\
\\vdots & \\vdots & \\ddots & \\vdots \\\\
a_{m1} & a_{m2} & \\cdots & a_{mn}
\\end{pmatrix}$$

<p>\\(\\mathbf{x}\\) is the \\(n \\times 1\\) <strong>unknown vector</strong> \\(= \\begin{pmatrix} x_1 \\\\ x_2 \\\\ \\vdots \\\\ x_n \\end{pmatrix}\\), and \\(\\mathbf{b}\\) is the \\(m \\times 1\\) <strong>constant vector</strong> \\(= \\begin{pmatrix} b_1 \\\\ b_2 \\\\ \\vdots \\\\ b_m \\end{pmatrix}\\).</p>

<h3>Geometric Interpretation in 2D</h3>
<p>In the plane \\(\\mathbb{R}^2\\), each linear equation \\(ax + by = c\\) represents a <strong>line</strong>. The solution to a system is the <strong>geometric intersection</strong> of all lines.</p>

<svg viewBox="0 0 400 350" style="border: 1px solid #ccc; margin: 20px 0;">
  <!-- Grid -->
  <g stroke="#e0e0e0" stroke-width="0.5">
    <line x1="0" y1="175" x2="400" y2="175"/>
    <line x1="200" y1="0" x2="200" y2="350"/>
  </g>

  <!-- Line 1: 2x + 3y = 8 (rearrange: y = (8 - 2x)/3) -->
  <line x1="20" y1="56" x2="380" y2="292" stroke="#2563eb" stroke-width="2.5" label="2x + 3y = 8"/>

  <!-- Line 2: x - y = 1 (rearrange: y = x - 1) -->
  <line x1="20" y1="95" x2="380" y2="455" stroke="#dc2626" stroke-width="2.5"/>

  <!-- Intersection point -->
  <circle cx="242" cy="286" r="5" fill="#16a34a" stroke="#000" stroke-width="1"/>

  <!-- Labels and legend -->
  <text x="10" y="20" font-size="12" fill="#2563eb" font-weight="bold">2x + 3y = 8</text>
  <text x="10" y="40" font-size="12" fill="#dc2626" font-weight="bold">x - y = 1</text>
  <text x="250" y="270" font-size="11" fill="#16a34a" font-weight="bold">Solution</text>

  <!-- Axis labels -->
  <text x="370" y="190" font-size="12">x</text>
  <text x="210" y="20" font-size="12">y</text>
</svg>

<div class="concept-box">
<h4>Three Geometric Cases</h4>
<p><strong>Case 1 (Unique Solution):</strong> Lines intersect at a point. One solution.</p>
<p><strong>Case 2 (Infinitely Many):</strong> Lines are identical. Every point on the line is a solution.</p>
<p><strong>Case 3 (No Solution):</strong> Lines are parallel but distinct. No intersection.</p>
</div>
"""
    },
    {
        "title": "Three Possible Outcomes: Existence and Uniqueness",
        "body": """
<h3>The Three Cases</h3>
<p>Every system of linear equations falls into exactly one of three categories:</p>

<div class="steps-container">
<div class="step">
<strong>Case 1: Unique Solution</strong>
<p>The system has exactly one solution \\(\\mathbf{x}^* \\in \\mathbb{R}^n\\). Geometrically (in 2D), two non-parallel lines intersect at a point.</p>
</div>

<div class="step">
<strong>Case 2: Infinitely Many Solutions</strong>
<p>The solution set is infinite, typically an affine subspace (line, plane, etc.). Equations are <em>dependent</em>—not all equations provide independent information.</p>
</div>

<div class="step">
<strong>Case 3: No Solution (Inconsistent)</strong>
<p>The solution set is empty \\(\\emptyset\\). Equations contradict each other (e.g., \\(0 = 1\\)).</p>
</div>
</div>

<h3>Homogeneous Systems</h3>
<p>A system is <strong>homogeneous</strong> if \\(\\mathbf{b} = \\mathbf{0}\\), i.e., \\(A\\mathbf{x} = \\mathbf{0}\\).</p>

<div class="formula-box">
<h4>Key Property of Homogeneous Systems</h4>
<p>Every homogeneous system is <strong>consistent</strong> because \\(\\mathbf{x} = \\mathbf{0}\\) (the <strong>trivial solution</strong>) always satisfies \\(A\\mathbf{0} = \\mathbf{0}\\).</p>
<p>A homogeneous system either has:</p>
<ul>
<li><strong>Only the trivial solution</strong> \\(\\mathbf{0}\\), or</li>
<li><strong>Infinitely many solutions</strong> (including non-trivial ones).</li>
</ul>
</div>

<div class="example-box">
<h4>Homogeneous Example</h4>
$$\\begin{align}
x + 2y - z &= 0 \\\\
2x + 4y - 2z &= 0
\\end{align}$$
<p>The second equation is \\(2 \\times\\) the first, so only one independent equation. Any \\((x, y, z)\\) with \\(x + 2y - z = 0\\) is a solution. The solution set is a 2-dimensional plane through the origin. For instance, \\((1, 0, 1), (0, 1, 2), (-1, 1, 1)\\) are all solutions.</p>
</div>

<h3>Consistency via Rank (Preview)</h3>
<p>The <strong>rank</strong> of a matrix is the dimension of its row space (or column space—they're equal). For the augmented matrix \\([A | \\mathbf{b}]\\) and coefficient matrix \\(A\\):</p>

<div class="formula-box">
<h4>Rouché-Capelli Theorem (Consistency Criterion)</h4>
<p>The system \\(A\\mathbf{x} = \\mathbf{b}\\) is:</p>
<ul>
<li><strong>Consistent</strong> if \\(\\text{rank}(A) = \\text{rank}([A | \\mathbf{b}])\\)</li>
<li><strong>Inconsistent</strong> if \\(\\text{rank}(A) < \\text{rank}([A | \\mathbf{b}])\\)</li>
<li><strong>Unique solution</strong> if \\(\\text{rank}(A) = \\text{rank}([A | \\mathbf{b}]) = n\\)</li>
<li><strong>Infinitely many solutions</strong> if \\(\\text{rank}(A) = \\text{rank}([A | \\mathbf{b}]) < n\\)</li>
</ul>
</div>

<p>(We'll define rank precisely in the next section via row reduction.)</p>

<h3>Example: All Three Cases</h3>
<div class="example-box">
<h4>Case 1 — Unique Solution</h4>
$$\\begin{align}
x + y &= 3 \\\\
x - y &= 1
\\end{align}$$
<p>Adding: \\(2x = 4\\), so \\(x = 2\\). Subtracting: \\(2y = 2\\), so \\(y = 1\\). Solution: \\((2, 1)\\).</p>

<h4>Case 2 — Infinitely Many Solutions</h4>
$$\\begin{align}
x + y &= 3 \\\\
2x + 2y &= 6
\\end{align}$$
<p>The second is \\(2 \\times\\) the first. They represent the same line. Solution: \\(\\{(t, 3-t) : t \\in \\mathbb{R}\\}\\).</p>

<h4>Case 3 — No Solution</h4>
$$\\begin{align}
x + y &= 3 \\\\
x + y &= 5
\\end{align}$$
<p>Subtracting: \\(0 = 2\\), a contradiction. No solution.</p>
</div>
"""
    },
    {
        "title": "Matrix Form and the Augmented Matrix",
        "body": """
<h3>Matrix Notation</h3>
<p>The system \\(a_{11}x_1 + \cdots + a_{1n}x_n = b_1, \ldots\\) can be written:</p>

$$\\begin{pmatrix}
a_{11} & a_{12} & \\cdots & a_{1n} \\\\
\\vdots & \\vdots & \\ddots & \\vdots \\\\
a_{m1} & a_{m2} & \\cdots & a_{mn}
\\end{pmatrix}
\\begin{pmatrix}
x_1 \\\\ \\vdots \\\\ x_n
\\end{pmatrix}
=
\\begin{pmatrix}
b_1 \\\\ \\vdots \\\\ b_m
\\end{pmatrix}$$

<p>In compact form: \\(A\\mathbf{x} = \\mathbf{b}\\).</p>

<h3>The Augmented Matrix</h3>
<p>To solve the system algorithmically, we form the <strong>augmented matrix</strong> \\([A | \\mathbf{b}]\\), combining coefficient and constant vectors:</p>

$$[A | \\mathbf{b}] = \\left[\\begin{array}{cccc|c}
a_{11} & a_{12} & \\cdots & a_{1n} & b_1 \\\\
a_{21} & a_{22} & \\cdots & a_{2n} & b_2 \\\\
\\vdots & \\vdots & \\ddots & \\vdots & \\vdots \\\\
a_{m1} & a_{m2} & \\cdots & a_{mn} & b_m
\\end{array}\\right]$$

<p>The vertical bar is a visual separator; the augmented matrix is still just an \\(m \\times (n+1)\\) matrix.</p>

<h3>Example: From System to Augmented Matrix</h3>
<div class="example-box">
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

<h3>Reversibility and Elementary Operations</h3>
<p>The augmented matrix is a complete encoding of the system. Solving the system means finding equivalent augmented matrices that reveal the solution.</p>

<div class="concept-box">
<h4>Elementary Row Operations (Preview)</h4>
<p>Three reversible transformations on rows:</p>
<ol>
<li><strong>Swap rows:</strong> \\(R_i \\leftrightarrow R_j\\) (reorder equations)</li>
<li><strong>Scale a row:</strong> \\(R_i \\rightarrow cR_i\\) for \\(c \\neq 0\\) (multiply equation by constant)</li>
<li><strong>Add rows:</strong> \\(R_i \\rightarrow R_i + cR_j\\) (add a multiple of one equation to another)</li>
</ol>
<p>These operations preserve the solution set.</p>
</div>
"""
    },
    {
        "title": "Elementary Row Operations and Equivalence",
        "body": """
<h3>The Three Elementary Row Operations</h3>
<p>Given an augmented matrix, we can apply <strong>three types of row operations</strong> that do not change the solution set:</p>

<div class="steps-container">
<div class="step">
<strong>Operation 1 (Row Swap):</strong> Interchange two rows. Notation: \\(R_i \\leftrightarrow R_j\\)
<p>Justification: Reordering equations doesn't change which points satisfy all of them.</p>
</div>

<div class="step">
<strong>Operation 2 (Row Scaling):</strong> Multiply a row by a non-zero constant. Notation: \\(R_i \\rightarrow c \\cdot R_i\\) for \\(c \\neq 0\\)
<p>Justification: If \\(\\mathbf{x}\\) satisfies \\(a_1 x_1 + \cdots + a_n x_n = b\\), it also satisfies \\(ca_1 x_1 + \cdots + ca_n x_n = cb\\).</p>
</div>

<div class="step">
<strong>Operation 3 (Row Addition):</strong> Add a multiple of one row to another. Notation: \\(R_i \\rightarrow R_i + c \\cdot R_j\\)
<p>Justification: If \\(\\mathbf{x}\\) satisfies both equations \\(i\\) and \\(j\\), it satisfies their sum (and any linear combination).</p>
</div>
</div>

<h3>Why These Operations Preserve Solutions</h3>
<p>Each operation is <strong>reversible</strong>:</p>
<ul>
<li>Swap \\(R_i\\) and \\(R_j\\) again to undo a swap.</li>
<li>Multiply by \\(c\\) again to undo scaling by \\(c\\) (since \\(c \\neq 0\\), \\(c^{-1}\\) exists).</li>
<li>Add \\(-c \\cdot R_j\\) to undo adding \\(c \\cdot R_j\\).</li>
</ul>

<p>Thus, row operations are <strong>bijections</strong> (one-to-one and onto transformations) on the set of augmented matrices. Two matrices related by row operations represent systems with <strong>identical solution sets</strong>.</p>

<h3>Row Equivalence</h3>
<div class="concept-box">
<h4>Definition</h4>
<p>Two matrices are <strong>row equivalent</strong> if one can be obtained from the other by a finite sequence of elementary row operations.</p>
</div>

<p><strong>Theorem:</strong> Row-equivalent augmented matrices correspond to equivalent systems (same solution set).</p>

<h3>Example: Using Row Operations</h3>
<div class="example-box">
<p><strong>System:</strong></p>
$$\\begin{align}
2x + 3y &= 7 \\\\
x - y &= 1
\\end{align}$$

<p><strong>Augmented matrix:</strong></p>
$$\\left[\\begin{array}{cc|c}
2 & 3 & 7 \\\\
1 & -1 & 1
\\end{array}\\right]$$

<p><strong>Step 1:</strong> Swap \\(R_1\\) and \\(R_2\\) to get a leading 1:</p>
$$\\left[\\begin{array}{cc|c}
1 & -1 & 1 \\\\
2 & 3 & 7
\\end{array}\\right]$$

<p><strong>Step 2:</strong> \\(R_2 \\rightarrow R_2 - 2R_1\\) to eliminate below the pivot:</p>
$$\\left[\\begin{array}{cc|c}
1 & -1 & 1 \\\\
0 & 5 & 5
\\end{array}\\right]$$

<p><strong>Step 3:</strong> \\(R_2 \\rightarrow \\frac{1}{5}R_2\\) to simplify:</p>
$$\\left[\\begin{array}{cc|c}
1 & -1 & 1 \\\\
0 & 1 & 1
\\end{array}\\right]$$

<p><strong>Step 4 (Back-substitution):</strong> From row 2: \\(y = 1\\). From row 1: \\(x - 1 = 1\\), so \\(x = 2\\).</p>

<p><strong>Solution:</strong> \\((x, y) = (2, 1)\\).</p>
</div>

<h3>Upper Triangular Form</h3>
<p>An augmented matrix is in <strong>upper triangular form</strong> (or <strong>row echelon form</strong>, to be defined precisely in Gaussian Elimination) if:</p>
<ul>
<li>All entries below the diagonal are zero (or near-zero for numerical purposes).</li>
<li>Rows of all zeros (if any) are at the bottom.</li>
<li>Each non-zero row has a leading (pivot) entry to the right of the pivot in the row above.</li>
</ul>

<p>Upper triangular form makes back-substitution straightforward.</p>
"""
    },
    {
        "title": "Homogeneous Systems and the Null Space",
        "body": """
<h3>Definition: Homogeneous Systems</h3>
<p>A system \\(A\\mathbf{x} = \\mathbf{0}\\) (where \\(\\mathbf{b} = \\mathbf{0}\\)) is called <strong>homogeneous</strong>.</p>

<div class="example-box">
<h4>Homogeneous System Example</h4>
$$\\begin{align}
2x + 3y - z &= 0 \\\\
x - y + 2z &= 0 \\\\
3x + 2y &= 0
\\end{align}$$
</div>

<h3>The Trivial Solution</h3>
<p>Every homogeneous system has \\(\\mathbf{x} = \\mathbf{0}\\) as a solution (plug in zeros). This is the <strong>trivial solution</strong>.</p>

<div class="concept-box">
<h4>Key Property</h4>
<p>Every homogeneous system is <strong>consistent</strong>. The question is not whether a solution exists, but whether non-trivial solutions exist.</p>
</div>

<h3>Trivial vs. Non-Trivial Solutions</h3>
<p>A homogeneous system either has:</p>
<ol>
<li><strong>Only the trivial solution:</strong> \\(\\mathbf{x} = \\mathbf{0}\\) is the unique solution.</li>
<li><strong>Non-trivial solutions:</strong> There exist vectors \\(\\mathbf{x} \\neq \\mathbf{0}\\) satisfying \\(A\\mathbf{x} = \\mathbf{0}\\). In this case, there are infinitely many solutions (a subspace of \\(\\mathbb{R}^n\\)).</li>
</ol>

<div class="example-box">
<h4>Case 1: Only Trivial Solution</h4>
$$\\begin{align}
x + 2y &= 0 \\\\
3x + 5y &= 0
\\end{align}$$
<p>From the first: \\(x = -2y\\). Substitute into the second: \\(3(-2y) + 5y = 0\\), so \\(-y = 0\\), thus \\(y = 0\\) and \\(x = 0\\).</p>
<p>Only solution: \\((0, 0)\\).</p>

<h4>Case 2: Non-Trivial Solutions</h4>
$$\\begin{align}
x + 2y - z &= 0 \\\\
2x + 4y - 2z &= 0
\\end{align}$$
<p>The second is \\(2 \\times\\) the first. One independent equation: \\(x + 2y - z = 0\\), so \\(x = -2y + z\\).</p>
<p>General solution: \\((x, y, z) = (-2y + z, y, z) = y(-2, 1, 0) + z(1, 0, 1)\\) for \\(y, z \\in \\mathbb{R}\\).</p>
<p>The solution space is a 2-dimensional plane through the origin, spanned by \\((-2, 1, 0)\\) and \\((1, 0, 1)\\).</p>
</div>

<h3>The Null Space</h3>
<p>The <strong>null space</strong> (or <strong>kernel</strong>) of a matrix \\(A\\), denoted \\(\\text{Null}(A)\\) or \\(\\ker(A)\\), is the set of all vectors \\(\\mathbf{x}\\) satisfying \\(A\\mathbf{x} = \\mathbf{0}\\):</p>

$$\\text{Null}(A) = \\{\\mathbf{x} \\in \\mathbb{R}^n : A\\mathbf{x} = \\mathbf{0}\\}$$

<p>The null space is a <strong>subspace</strong> of \\(\\mathbb{R}^n\\) (we'll study subspaces in detail later).</p>

<h3>General Solution Structure</h3>
<p>For a consistent system \\(A\\mathbf{x} = \\mathbf{b}\\):</p>

<div class="formula-box">
<h4>General Solution Formula</h4>
<p>If \\(\\mathbf{x}_p\\) is a <strong>particular solution</strong> to \\(A\\mathbf{x} = \\mathbf{b}\\), then:</p>

$$\\text{All solutions} = \\mathbf{x}_p + \\text{Null}(A) = \\{\\mathbf{x}_p + \\mathbf{n} : \\mathbf{n} \\in \\text{Null}(A)\\}$$
</div>

<p><strong>Proof:</strong> If \\(\\mathbf{x} = \\mathbf{x}_p + \\mathbf{n}\\) where \\(A\\mathbf{x}_p = \\mathbf{b}\\) and \\(A\\mathbf{n} = \\mathbf{0}\\), then \\(A\\mathbf{x} = A\\mathbf{x}_p + A\\mathbf{n} = \\mathbf{b} + \\mathbf{0} = \\mathbf{b}\\). Conversely, any solution \\(\\mathbf{x}\\) can be written \\(\\mathbf{x}_p + (\\mathbf{x} - \\mathbf{x}_p)\\) where \\(\\mathbf{x} - \\mathbf{x}_p \\in \\text{Null}(A)\\).</p>

<h3>Geometric Interpretation</h3>
<p>The solution set is a <strong>translate</strong> of the null space:</p>
<ul>
<li>If \\(\\text{Null}(A) = \\{\\mathbf{0}\\}\\), the solution is a single point.</li>
<li>If \\(\\text{Null}(A)\\) is a line through the origin, the solution set is a parallel line (not through origin, unless \\(\\mathbf{b} = \\mathbf{0}\\)).</li>
<li>If \\(\\text{Null}(A)\\) is a plane through the origin, the solution set is a parallel plane.</li>
</ul>
"""
    },
    {
        "title": "Applications and Theoretical Summary",
        "body": """
<h3>Application 1: Balancing Chemical Equations</h3>
<p>In chemistry, a chemical equation like \\(C_2H_6 + O_2 \\rightarrow CO_2 + H_2O\\) must be balanced so each element appears the same number of times on both sides.</p>

<div class="example-box">
<h4>Example: Ethane Combustion</h4>
<p>Let the coefficients be \\(aC_2H_6 + bO_2 \\rightarrow cCO_2 + dH_2O\\).</p>

<p><strong>Carbon balance:</strong> \\(2a = c\\)</p>
<p><strong>Hydrogen balance:</strong> \\(6a = 2d\\)</p>
<p><strong>Oxygen balance:</strong> \\(2b = 2c + d\\)</p>

<p>Rearranging as a homogeneous system:</p>
$$\\begin{align}
2a - c &= 0 \\\\
6a - 2d &= 0 \\\\
2b - 2c - d &= 0
\\end{align}$$

<p>Setting \\(a = 1\\) (to get a particular solution): \\(c = 2, d = 3, b = 3\\).</p>

<p><strong>Balanced equation:</strong> \\(C_2H_6 + 3O_2 \\rightarrow 2CO_2 + 3H_2O\\)</p>
</div>

<h3>Application 2: Electrical Networks (Kirchhoff's Laws)</h3>
<p><strong>Kirchhoff's Voltage Law:</strong> The sum of voltages around a closed loop is zero.</p>
<p><strong>Kirchhoff's Current Law:</strong> The sum of currents at a junction is zero.</p>

<p>These laws yield systems of linear equations for unknown currents and voltages.</p>

<h3>Application 3: Least Squares Fitting</h3>
<p>To fit a line \\(y = mx + b\\) to data points \\((x_i, y_i)\\), we minimize the error. The optimal \\(m\\) and \\(b\\) satisfy the <strong>normal equations</strong>, a system of 2 linear equations in 2 unknowns.</p>

<h3>Theoretical Summary</h3>
<div class="concept-box">
<h4>Existence and Uniqueness</h4>
<ul>
<li><strong>Existence:</strong> System \\(A\\mathbf{x} = \\mathbf{b}\\) is consistent iff \\(\\text{rank}(A) = \\text{rank}([A|\\mathbf{b}])\\).</li>
<li><strong>Uniqueness:</strong> If consistent, solution is unique iff \\(\\text{rank}(A) = n\\) (no free variables).</li>
<li><strong>Infinitely many solutions:</strong> If consistent and \\(\\text{rank}(A) < n\\), there are \\(n - \\text{rank}(A)\\) free variables.</li>
</ul>
</div>

<div class="formula-box">
<h4>Rank-Nullity Theorem (Foundation)</h4>
<p>For an \\(m \\times n\\) matrix \\(A\\):</p>

$$\\text{rank}(A) + \\text{nullity}(A) = n$$

<p>where \\(\\text{nullity}(A) = \\dim(\\text{Null}(A))\\) is the number of free variables in solutions to \\(A\\mathbf{x} = \\mathbf{0}\\).</p>
</div>

<h3>Next Steps</h3>
<p>The next topic, <strong>Gaussian Elimination</strong>, systematizes row reduction into an algorithm that:</p>
<ul>
<li>Solves systems reliably and efficiently.</li>
<li>Computes ranks and bases for null spaces.</li>
<li>Detects inconsistency and dependence.</li>
</ul>
"""
    }
]

        <div class='example-box'>
        <p><strong>Example of unique solution:</strong></p>
        <pre class='code-block'>x + y = 3
x - y = 1</pre>
        <p>Augmented matrix: [1  1 | 3]
                         [1 -1 | 1]</p>
        <p>Adding the equations: 2x = 4, so x = 2. Then y = 1. <strong>Unique solution: (2, 1)</strong></p>

        <p><strong>Example of infinitely many solutions:</strong></p>
        <pre class='code-block'>x + y = 2
2x + 2y = 4</pre>
        <p>The second equation is 2× the first, so they're the same constraint. Any (x, y) with x + y = 2 works.</p>

        <p><strong>Example of no solution:</strong></p>
        <pre class='code-block'>x + y = 2
x + y = 3</pre>
        <p>No pair (x, y) can satisfy both equations. <strong>Inconsistent system.</strong></p>
        </div>
        """
    },
    {
        "title": "Geometric Interpretation in 2D and 3D",
        "body": """
        <p>Linear equations have beautiful geometric meanings. Each linear equation defines a geometric object:</p>

        <p><strong>In 2D:</strong> A linear equation ax + by = c defines a <strong>line</strong>. A system of two equations represents two lines.</p>
        <ul>
        <li><strong>Unique solution:</strong> Two lines intersect at exactly one point.</li>
        <li><strong>Infinitely many solutions:</strong> Two lines are identical (coincident).</li>
        <li><strong>No solution:</strong> Two lines are parallel (never meet).</li>
        </ul>

        <p><strong>In 3D:</strong> A linear equation ax + by + cz = d defines a <strong>plane</strong>. A system of three equations represents three planes.</p>
        <ul>
        <li><strong>Unique solution:</strong> Three planes meet at exactly one point.</li>
        <li><strong>Infinitely many solutions:</strong> Planes intersect in a line (1D) or a plane (2D).</li>
        <li><strong>No solution:</strong> Planes don't have a common point (e.g., two parallel planes, or a "wedge" with no center).</li>
        </ul>

        <p><strong>Higher dimensions:</strong> Each equation defines a hyperplane (a (n-1)-dimensional object in n-dimensional space). The same logic applies: the solution is the intersection of these hyperplanes.</p>

        <div class='example-box'>
        <p><strong>Geometric example in 2D:</strong></p>
        <pre class='code-block'>y = x      (line through origin, slope 1)
y = -x + 2 (line with slope -1, y-intercept 2)</pre>
        <p>These lines intersect where x = -x + 2, so 2x = 2, thus x = 1, y = 1. <strong>Unique solution: (1, 1)</strong> = intersection point.</p>

        <p>If we had y = x and y = x + 1, these are parallel (same slope, different intercepts). <strong>No solution.</strong></p>
        </div>

        <p><strong>Rank and the rank theorem:</strong> The number of independent equations determines the dimension of the solution set:</p>
        <ul>
        <li>If rank(A) = rank([A|b]) = n (number of variables), the solution is unique.</li>
        <li>If rank(A) = rank([A|b]) < n, there are infinitely many solutions (dimension n - rank).</li>
        <li>If rank(A) < rank([A|b]), the system is inconsistent (no solution).</li>
        </ul>
        """
    },
    {
        "title": "Homogeneous and Inhomogeneous Systems",
        "body": """
        <p><strong>Homogeneous System:</strong> When b = 0 (all right-hand sides are zero), we have Ax = 0. This system always has at least one solution: <strong>x = 0</strong> (the trivial solution).</p>

        <p>A homogeneous system either has:</p>
        <ul>
        <li><strong>Only the trivial solution x = 0:</strong> When rank(A) = n (full column rank).</li>
        <li><strong>Infinitely many solutions:</strong> When rank(A) < n. The solution space is a subspace of dimension n - rank(A).</li>
        </ul>

        <p><strong>Inhomogeneous System:</strong> When b ≠ 0, we have Ax = b. This system may have:</p>
        <ul>
        <li>No solution (inconsistent)</li>
        <li>Exactly one solution</li>
        <li>Infinitely many solutions</li>
        </ul>

        <p><strong>Key relationship:</strong> If xₚ is a particular solution to Ax = b, and xₕ is any solution to Ax = 0, then xₚ + xₕ is also a solution to Ax = b.</p>
        <p><strong>General solution to Ax = b:</strong> x = xₚ + xₕ, where xₚ is a particular solution and xₕ ranges over all solutions to the homogeneous system Ax = 0.</p>

        <div class='example-box'>
        <p><strong>Homogeneous example:</strong></p>
        <pre class='code-block'>2x + 3y = 0
x - y = 0</pre>
        <p>From the second equation, x = y. Substituting: 2y + 3y = 0, so y = 0. Thus x = 0. <strong>Only the trivial solution: (0, 0)</strong></p>

        <p><strong>Inhomogeneous example:</strong></p>
        <pre class='code-block'>2x + 3y = 7
x - y = 1</pre>
        <p>Particular solution (by inspection): (2, 1). The associated homogeneous system 2x + 3y = 0, x - y = 0 has only the trivial solution. So <strong>unique solution: (2, 1)</strong></p>
        </div>

        <p><strong>Why this matters:</strong> Understanding the structure of solutions (particular + homogeneous) is essential for:</p>
        <ul>
        <li>Solving differential equations</li>
        <li>Understanding linear regression (least squares)</li>
        <li>Analyzing stability and null spaces in applied mathematics</li>
        </ul>
        """
    },
    {
        "title": "Applications and Practical Perspectives",
        "body": """
        <p>Systems of linear equations appear everywhere in applied mathematics, engineering, and science:</p>

        <p><strong>1. Circuit Analysis (Kirchhoff's Laws):</strong> For an electrical circuit, Kirchhoff's voltage law (KVL) and current law (KCL) produce a system of linear equations in unknown currents and voltages.</p>

        <p><strong>2. Network Flow Problems:</strong> In transportation networks, conservation of flow at each node gives linear constraints. Finding feasible flows means solving a system of equations.</p>

        <p><strong>3. Least Squares Regression:</strong> Fitting a line y = mx + b to data points (x₁, y₁), ..., (xₙ, yₙ) reduces to solving a (usually overdetermined) system of equations.</p>

        <p><strong>4. Structural Analysis:</strong> In engineering, equilibrium of forces at each joint gives a system of linear equations in unknown forces.</p>

        <p><strong>5. Polynomial Interpolation:</strong> Finding a polynomial of degree n that passes through n+1 points requires solving a system of linear equations (the Vandermonde system).</p>

        <div class='example-box'>
        <p><strong>Simple regression example:</strong> Fit y = mx + b to points (1, 2) and (2, 3).</p>
        <pre class='code-block'>2 = m(1) + b  →  m + b = 2
3 = m(2) + b  →  2m + b = 3</pre>
        <p>System: m + b = 2 and 2m + b = 3. Subtracting: m = 1. Then b = 1. <strong>Line: y = x + 1</strong></p>
        </div>

        <p><strong>Computational complexity:</strong> Solving an n × n system via Gaussian elimination requires O(n³) operations. For modern applications with millions of variables, specialized algorithms (iterative methods, sparse matrix techniques) are essential.</p>

        <p><strong>Numerical stability:</strong> In practice, floating-point arithmetic introduces errors. Systems with high condition numbers (ill-conditioned) amplify these errors significantly, requiring careful numerical handling.</p>
        """
    }
]
