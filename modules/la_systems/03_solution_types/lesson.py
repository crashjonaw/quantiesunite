TITLE = "Solution Types: Unique, Infinite, or None"

SECTIONS = [
    {
        "title": "The Three Possible Outcomes",
        "body": """
<h3>Fundamental Theorem</h3>
<p>Every system of linear equations falls into exactly one of three categories:</p>

<div class="concept-box">
<h4>Case 1: Unique Solution</h4>
<p>The system has exactly one solution \\(\\mathbf{x}^* \\in \\mathbb{R}^n\\).</p>
<p><strong>Geometric (2D):</strong> Two non-parallel lines intersect at a point.</p>

<h4>Case 2: Infinitely Many Solutions</h4>
<p>The solution set is infinite, typically an affine subspace (line, plane, etc.). The equations are <em>dependent</em>—not all equations provide independent information.</p>
<p><strong>Geometric (2D):</strong> Two identical lines.</p>

<h4>Case 3: No Solution (Inconsistent)</h4>
<p>The solution set is empty \\(\\emptyset\\). The equations contradict each other.</p>
<p><strong>Geometric (2D):</strong> Two parallel but distinct lines.</p>
</div>

<div class="worked-example">
<h4>Example: All Three Cases</h4>

<p><strong>Case 1 — Unique Solution</strong></p>
$$\\begin{align}
x + y &= 3 \\\\
x - y &= 1
\\end{align}$$
<p>Adding: \\(2x = 4\\), so \\(x = 2\\). Subtracting: \\(2y = 2\\), so \\(y = 1\\).</p>
<p><strong>Solution:</strong> \\((2, 1)\\) (unique)</p>

<p><strong>Case 2 — Infinitely Many Solutions</strong></p>
$$\\begin{align}
x + y &= 3 \\\\
2x + 2y &= 6
\\end{align}$$
<p>The second equation is \\(2 \\times\\) the first. They represent the same line.</p>
<p><strong>General solution:</strong> \\((x, y) = (t, 3 - t)\\) for \\(t \\in \\mathbb{R}\\) (infinitely many)</p>

<p><strong>Case 3 — No Solution</strong></p>
$$\\begin{align}
x + y &= 3 \\\\
x + y &= 5
\\end{align}$$
<p>Subtracting: \\(0 = 2\\), a contradiction!</p>
<p><strong>Solution set:</strong> \\(\\emptyset\\) (no solution, inconsistent)</p>
</div>
"""
    },
    {
        "title": "The Rouché-Capelli Theorem: Consistency Criterion",
        "body": """
<h3>Using Rank to Determine Solution Type</h3>
<p>The <strong>rank</strong> of a matrix is the dimension of its row space (or column space—they're equal). For an augmented matrix \\([A | \\mathbf{b}]\\) and coefficient matrix \\(A\\):</p>

<div class="concept-box">
<h4>Rouché-Capelli Theorem</h4>
<p>For system \\(A\\mathbf{x} = \\mathbf{b}\\):</p>

<ul>
<li><strong>Consistent (has solutions)</strong> iff \\(\\text{rank}(A) = \\text{rank}([A | \\mathbf{b}])\\)</li>
<li><strong>Inconsistent (no solutions)</strong> iff \\(\\text{rank}(A) < \\text{rank}([A | \\mathbf{b}])\\)</li>
<li><strong>Unique solution</strong> iff \\(\\text{rank}(A) = \\text{rank}([A | \\mathbf{b}]) = n\\) (where \\(n\\) = number of unknowns)</li>
<li><strong>Infinitely many solutions</strong> iff \\(\\text{rank}(A) = \\text{rank}([A | \\mathbf{b}]) < n\\)</li>
</ul>
</div>

<h4>Intuition</h4>
<p><strong>Free variables:</strong> When \\(\\text{rank}(A) < n\\), we have \\(n - \\text{rank}(A)\\) free variables. Each free variable allows the solution set to "spread out" in one dimension, creating infinitely many solutions.</p>

<div class="warning-box">
<h4>Important Observation</h4>
<p>If \\(\\text{rank}(A) < \\text{rank}([A | \\mathbf{b}])\\), it means the augmented matrix has an equation of the form \\(0 = c\\) where \\(c \\neq 0\\). This is impossible, so the system is inconsistent.</p>
</div>

<div class="worked-example">
<h4>Example: Using Rank</h4>
<p><strong>System:</strong></p>
$$\\begin{align}
x + 2y + z &= 4 \\\\
2x + 4y + 2z &= 8 \\\\
x + y + z &= 3
\\end{align}$$

<p><strong>Augmented matrix:</strong></p>
$$\\left[\\begin{array}{ccc|c}
1 & 2 & 1 & 4 \\\\
2 & 4 & 2 & 8 \\\\
1 & 1 & 1 & 3
\\end{array}\\right]$$

<p>After row reduction: \\(\\text{rank}(A) = 2\\), \\(\\text{rank}([A|\\mathbf{b}]) = 2\\).</p>
<p>Since ranks are equal and \\(2 < 3\\), the system is <strong>consistent with infinitely many solutions</strong> (1 free variable).</p>
</div>
"""
    },
    {
        "title": "Understanding Dependent vs. Independent Equations",
        "body": """
<h3>Linear Dependence and Independence</h3>
<p>Equations in a system can be <strong>dependent</strong> (redundant) or <strong>independent</strong> (providing new information).</p>

<div class="concept-box">
<h4>Dependent Equations</h4>
<p>One equation is a scalar multiple (or linear combination) of another. Example:</p>
$$\\begin{align}
2x + 3y &= 6 \\\\
4x + 6y &= 12
\\end{align}$$
<p>The second is exactly \\(2 \\times\\) the first. They provide the same information.</p>

<h4>Independent Equations</h4>
<p>No equation is a linear combination of the others. Example:</p>
$$\\begin{align}
x + y &= 3 \\\\
x - y &= 1
\\end{align}$$
<p>Neither is a multiple of the other; they provide distinct constraints.</p>
</div>

<div class="success-box">
<h4>Rank and Independence</h4>
<p>The rank equals the number of independent equations (or rows) in the system. More independent equations = higher rank = stronger constraints.</p>
</div>

<div class="worked-example">
<h4>Example: Identifying Dependence</h4>
$$\\begin{align}
3x - 2y &= 5 \\\\
6x - 4y &= 10 \\\\
x + y &= 2
\\end{align}$$

<p>Equations 1 and 2: Equation 2 is \\(2 \\times\\) Equation 1 (dependent).</p>
<p>Equation 3: Independent of the first two.</p>
<p>Only 2 independent equations, so \\(\\text{rank}(A) = 2\\).</p>
</div>
"""
    }
]
