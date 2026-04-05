TITLE = "Applications and Theoretical Summary"

SECTIONS = [
    {
        "title": "Application 1: Balancing Chemical Equations",
        "body": """
<h3>The Problem</h3>
<p>In chemistry, a chemical equation like \\(C_2H_6 + O_2 \\rightarrow CO_2 + H_2O\\) must be balanced so each element appears the same number of times on both sides.</p>

<div class="worked-example">
<h4>Example: Ethane Combustion</h4>
<p>Let the balanced equation be: \\(aC_2H_6 + bO_2 \\rightarrow cCO_2 + dH_2O\\)</p>

<p><strong>Element balances (homogeneous system):</strong></p>
<ul>
<li><strong>Carbon:</strong> \\(2a = c\\)</li>
<li><strong>Hydrogen:</strong> \\(6a = 2d\\)</li>
<li><strong>Oxygen:</strong> \\(2b = 2c + d\\)</li>
</ul>

<p><strong>Rearranged as a system:</strong></p>
$$\\begin{align}
2a - c &= 0 \\\\
6a - 2d &= 0 \\\\
2b - 2c - d &= 0
\\end{align}$$

<p>This is a homogeneous system. To get a <em>unique</em> equation, we set one coefficient to 1 (e.g., \\(a = 1\\)):</p>
<ul>
<li>From equation 1: \\(c = 2(1) = 2\\)</li>
<li>From equation 2: \\(d = 3(1) = 3\\)</li>
<li>From equation 3: \\(2b = 2(2) + 3 = 7\\), so \\(b = 3.5\\)</li>
</ul>

<p>To avoid fractions, multiply all coefficients by 2:</p>

<p><strong>Balanced equation:</strong> \\(\\boxed{C_2H_6 + 3O_2 \\rightarrow 2CO_2 + 3H_2O}\\)</p>

<p><strong>Verification:</strong> C: \\(2 = 2\\) ✓, H: \\(6 = 6\\) ✓, O: \\(6 + 2 = 8\\) ✓</p>
</div>

<div class="success-box">
<h4>Why This Works</h4>
<p>Chemical balance constraints form a system of linear equations. Solving this system yields the correct coefficients. The flexibility in homogeneous systems allows us to scale the entire solution to get integer coefficients.</p>
</div>
"""
    },
    {
        "title": "Application 2: Electrical Networks (Kirchhoff's Laws)",
        "body": """
<h3>Circuit Analysis</h3>
<p>Electrical networks involve unknown currents flowing through resistors and voltage sources. We can find these currents by setting up systems of linear equations using Kirchhoff's laws.</p>

<div class="concept-box">
<h4>Kirchhoff's Laws</h4>
<ul>
<li><strong>Kirchhoff's Voltage Law (KVL):</strong> The sum of voltages around any closed loop is zero.</li>
<li><strong>Kirchhoff's Current Law (KCL):</strong> The sum of currents at any junction is zero (current conservation).</li>
</ul>
</div>

<div class="worked-example">
<h4>Example: Simple Circuit</h4>
<p>Consider a circuit with two loops, two resistors (\\(R_1, R_2\\)), two voltage sources (\\(V_1, V_2\\)), and unknown currents \\(I_1, I_2\\).</p>

<p><strong>Applying KVL to each loop:</strong></p>
<ul>
<li>Loop 1: \\(V_1 - I_1 R_1 - (I_1 - I_2)R_3 = 0\\)</li>
<li>Loop 2: \\(V_2 - I_2 R_2 - (I_2 - I_1)R_3 = 0\\)</li>
</ul>

<p><strong>Rearranged as a linear system:</strong></p>
$$\\begin{align}
(R_1 + R_3)I_1 - R_3 I_2 &= V_1 \\\\
-R_3 I_1 + (R_2 + R_3)I_2 &= V_2
\\end{align}$$

<p>Solving this system yields \\(I_1\\) and \\(I_2\\), the currents in each loop.</p>
</div>

<div class="success-box">
<h4>Power of Linear Systems</h4>
<p>Despite the apparent complexity of circuits, the voltage-current relationships are linear, making systems of linear equations the perfect tool for circuit analysis.</p>
</div>
"""
    },
    {
        "title": "Application 3: Least Squares Fitting",
        "body": """
<h3>The Problem: Fitting Data to a Model</h3>
<p>Given experimental data points \\((x_i, y_i)\\), we often want to fit a line \\(y = mx + b\\) to minimize error.</p>

<div class="worked-example">
<h4>Linear Regression</h4>
<p>Data points: \\((1, 2), (2, 3), (3, 5), (4, 6)\\)</p>

<p>We want to find \\(m\\) and \\(b\\) that best fit this data. The <strong>normal equations</strong> (from calculus) yield a system of 2 linear equations in 2 unknowns:</p>

$$\\begin{align}
n \\cdot b + (\\sum x_i) \\cdot m &= \\sum y_i \\\\
(\\sum x_i) \\cdot b + (\\sum x_i^2) \\cdot m &= \\sum x_i y_i
\\end{align}$$

<p>For the given data: \\(n = 4\\), \\(\\sum x_i = 10\\), \\(\\sum y_i = 16\\), \\(\\sum x_i^2 = 30\\), \\(\\sum x_i y_i = 50\\).</p>

$$\\begin{align}
4b + 10m &= 16 \\\\
10b + 30m &= 50
\\end{align}$$

<p>Solving: \\(b = 0.5\\), \\(m = 1.5\\). Best-fit line: \\(y = 1.5x + 0.5\\)</p>
</div>

<div class="success-box">
<h4>Least Squares Method</h4>
<p>The normal equations always form a system of linear equations. Solving them gives the coefficients that minimize the sum of squared errors—a fundamental technique in statistics and machine learning.</p>
</div>
"""
    },
    {
        "title": "Theoretical Summary: Existence and Uniqueness",
        "body": """
<h3>Fundamental Theorems</h3>

<div class="formula-box">
<h4>Existence (Consistency)</h4>
<p>The system \\(A\\mathbf{x} = \\mathbf{b}\\) <strong>is consistent</strong> (has at least one solution) iff:</p>
$$\\text{rank}(A) = \\text{rank}([A | \\mathbf{b}])$$
</div>

<div class="formula-box">
<h4>Uniqueness</h4>
<p>If the system is consistent, the solution is <strong>unique</strong> iff:</p>
$$\\text{rank}(A) = n \\quad (\\text{where } n = \\text{number of unknowns})$$
</div>

<div class="formula-box">
<h4>Infinitely Many Solutions</h4>
<p>If the system is consistent and:</p>
$$\\text{rank}(A) < n$$
<p>then there are <strong>infinitely many solutions</strong>. The number of free variables is \\(n - \\text{rank}(A)\\).</p>
</div>

<h3>The Rank-Nullity Theorem</h3>
<div class="concept-box">
<h4>Fundamental Relationship</h4>
<p>For an \\(m \\times n\\) matrix \\(A\\):</p>

$$\\text{rank}(A) + \\text{nullity}(A) = n$$

<p>where \\(\\text{nullity}(A) = \\dim(\\text{Null}(A))\\) is the dimension of the null space (the number of free variables in \\(A\\mathbf{x} = \\mathbf{0}\\)).</p>
</div>

<div class="worked-example">
<h4>Example: Counting Degrees of Freedom</h4>
<p>For a \\(5 \\times 10\\) system (5 equations, 10 unknowns):</p>
<ul>
<li>\\(\\text{rank}(A) \\leq 5\\) (at most 5 independent equations)</li>
<li>\\(\\text{nullity}(A) = 10 - \\text{rank}(A) \\geq 5\\) (at least 5 free variables)</li>
<li>If \\(\\text{rank}(A) = 3\\), then \\(\\text{nullity}(A) = 7\\) (7 free variables, infinitely many solutions)</li>
</ul>
</div>

<h3>Summary Table</h3>
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
<tr >
<th style="padding: 10px; text-align: left">Condition</th>
<th style="padding: 10px; text-align: left">Solution Type</th>
</tr>
<tr >
<td style="padding: 10px;">rank(A) < rank([A|b])</td>
<td style="padding: 10px;"><strong>Inconsistent:</strong> No solutions</td>
</tr>
<tr >
<td style="padding: 10px;">rank(A) = rank([A|b]) = n</td>
<td style="padding: 10px;"><strong>Unique solution</strong></td>
</tr>
<tr >
<td style="padding: 10px;">rank(A) = rank([A|b]) < n</td>
<td style="padding: 10px;"><strong>Infinitely many solutions</strong></td>
</tr>
</table>

<div class="success-box">
<h4>Next Steps in Linear Algebra</h4>
<p>Building on this foundation:</p>
<ul>
<li><strong>Gaussian Elimination:</strong> Systematic algorithm to compute rank and solve systems</li>
<li><strong>Vector Spaces and Subspaces:</strong> Abstract study of solution structures</li>
<li><strong>Eigenvalues and Eigenvectors:</strong> Special solutions to \\(A\\mathbf{x} = \\lambda \\mathbf{x}\\)</li>
<li><strong>Matrix Decompositions:</strong> LU, QR, SVD for efficient computation</li>
</ul>
</div>
"""
    }
]
