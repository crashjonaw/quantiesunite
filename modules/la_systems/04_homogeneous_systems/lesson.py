TITLE = "Homogeneous Systems and the Null Space"

SECTIONS = [
    {
        "title": "What is a Homogeneous System?",
        "body": """
<h3>Definition</h3>
<p>A system \\(A\\mathbf{x} = \\mathbf{0}\\) (where \\(\\mathbf{b} = \\mathbf{0}\\)) is called <strong>homogeneous</strong>.</p>

<div class="worked-example">
<h4>Example: Homogeneous System</h4>
$$\\begin{align}
2x + 3y - z &= 0 \\\\
x - y + 2z &= 0 \\\\
3x + 2y &= 0
\\end{align}$$

<p>All right-hand sides are zero. This is homogeneous.</p>
</div>

<h3>The Trivial Solution</h3>
<div class="concept-box">
<h4>Key Property of Homogeneous Systems</h4>
<p>Every homogeneous system has \\(\\mathbf{x} = \\mathbf{0}\\) as a solution (the <strong>trivial solution</strong>). Plugging in all zeros:</p>
$$A\\mathbf{0} = \\mathbf{0}$$
<p>This is always true!</p>
</div>

<p><strong>Consequence:</strong> Every homogeneous system is <em>consistent</em>. The question is not whether solutions exist, but whether <em>non-trivial</em> solutions exist.</p>

<div class="success-box">
<h4>Homogeneous vs. Non-Homogeneous</h4>
<p>A non-homogeneous system \\(A\\mathbf{x} = \\mathbf{b}\\) (with \\(\\mathbf{b} \\neq \\mathbf{0}\\) may be inconsistent. A homogeneous system never is.</p>
</div>
"""
    },
    {
        "title": "Trivial and Non-Trivial Solutions",
        "body": """
<h3>Two Possibilities</h3>
<p>A homogeneous system either has:</p>

<div class="concept-box">
<h4>Case 1: Only the Trivial Solution</h4>
<p>\\(\\mathbf{x} = \\mathbf{0}\\) is the unique solution. This happens when \\(\\text{rank}(A) = n\\) (the coefficient matrix has full rank).</p>

<h4>Case 2: Non-Trivial Solutions</h4>
<p>There exist vectors \\(\\mathbf{x} \\neq \\mathbf{0}\\) satisfying \\(A\\mathbf{x} = \\mathbf{0}\\). In this case, there are <em>infinitely many</em> solutions (a subspace of \\(\\mathbb{R}^n\\)). This happens when \\(\\text{rank}(A) < n\\).</p>
</div>

<div class="worked-example">
<h4>Case 1: Only Trivial Solution</h4>
$$\\begin{align}
x + 2y &= 0 \\\\
3x + 5y &= 0
\\end{align}$$

<p>From the first: \\(x = -2y\\). Substitute into the second: \\(3(-2y) + 5y = 0\\), so \\(-y = 0\\), thus \\(y = 0\\) and \\(x = 0\\).</p>
<p><strong>Only solution:</strong> \\((0, 0)\\)</p>

<h4>Case 2: Non-Trivial Solutions</h4>
$$\\begin{align}
x + 2y - z &= 0 \\\\
2x + 4y - 2z &= 0
\\end{align}$$

<p>The second is \\(2 \\times\\) the first. Only one independent equation: \\(x + 2y - z = 0\\), so \\(x = -2y + z\\).</p>
<p><strong>General solution:</strong> \\((x, y, z) = (-2y + z, y, z) = y(-2, 1, 0) + z(1, 0, 1)\\) for \\(y, z \\in \\mathbb{R}\\)</p>
<p>The solution space is 2-dimensional, spanned by \\(\\mathbf{v}_1 = (-2, 1, 0)\\) and \\(\\mathbf{v}_2 = (1, 0, 1)\\).</p>
<p>Examples of non-trivial solutions: \\((-2, 1, 0)\\), \\((1, 0, 1)\\), \\((-1, 1, 1)\\), etc.</p>
</div>

<div class="warning-box">
<h4>Important Distinction</h4>
<p>Non-trivial solutions exist when the system is <em>underdetermined</em>: fewer independent equations than unknowns (\\(\\text{rank}(A) < n\\)).</p>
</div>
"""
    },
    {
        "title": "The Null Space and General Solutions",
        "body": """
<h3>Introducing the Null Space</h3>
<p>The <strong>null space</strong> (or <strong>kernel</strong>) of a matrix \\(A\\), denoted \\(\\text{Null}(A)\\) or \\(\\ker(A)\\), is the set of <em>all</em> solutions to \\(A\\mathbf{x} = \\mathbf{0}\\):</p>

$$\\text{Null}(A) = \\{\\mathbf{x} \\in \\mathbb{R}^n : A\\mathbf{x} = \\mathbf{0}\\}$$

<div class="concept-box">
<h4>Key Property: The Null Space is a Subspace</h4>
<p>The null space is a <strong>subspace</strong> of \\(\\mathbb{R}^n\\). This means:</p>
<ul>
<li>It contains the origin \\(\\mathbf{0}\\)</li>
<li>It is closed under addition: if \\(\\mathbf{u}, \\mathbf{v} \\in \\text{Null}(A)\\), then \\(\\mathbf{u} + \\mathbf{v} \\in \\text{Null}(A)\\)</li>
<li>It is closed under scalar multiplication: if \\(\\mathbf{v} \\in \\text{Null}(A)\\) and \\(c \\in \\mathbb{R}\\), then \\(c\\mathbf{v} \\in \\text{Null}(A)\\)</li>
</ul>
</div>

<h3>General Solution Structure</h3>
<p>For a <em>consistent</em> system \\(A\\mathbf{x} = \\mathbf{b}\\):</p>

<div class="formula-box">
<h4>Solution Formula</h4>
<p>If \\(\\mathbf{x}_p\\) is a <strong>particular solution</strong> to \\(A\\mathbf{x} = \\mathbf{b}\\), then:</p>

$$\\text{All solutions} = \\mathbf{x}_p + \\text{Null}(A)$$

<p>That is: \\(\\{\\mathbf{x}_p + \\mathbf{n} : \\mathbf{n} \\in \\text{Null}(A)\\}\\)</p>
</div>

<div class="worked-example">
<h4>Example: Using Particular + Null Space</h4>
$$\\begin{align}
x + 2y - z &= 5 \\\\
2x + 4y - 2z &= 10
\\end{align}$$

<p><strong>Step 1:</strong> Note that equation 2 is \\(2 \\times\\) equation 1. Only one independent equation: \\(x + 2y - z = 5\\).</p>

<p><strong>Step 2:</strong> Find a particular solution. Set \\(y = 0, z = 0\\): then \\(x = 5\\). So \\(\\mathbf{x}_p = (5, 0, 0)\\) is a particular solution.</p>

<p><strong>Step 3:</strong> Solve \\(A\\mathbf{x} = \\mathbf{0}\\) (the homogeneous version): \\(x + 2y - z = 0\\), so \\(x = -2y + z\\).</p>
<p>General solution to homogeneous system:</p>
$$\\mathbf{n} = y(-2, 1, 0) + z(1, 0, 1)$$

<p><strong>Step 4:</strong> Combine:</p>
$$\\mathbf{x} = (5, 0, 0) + y(-2, 1, 0) + z(1, 0, 1) = (5 - 2y + z, y, z)$$

<p><strong>Verification:</strong> \\(x + 2y - z = (5 - 2y + z) + 2y - z = 5\\) ✓</p>
</div>

<h3>Geometric Interpretation</h3>
<p>The solution set to \\(A\\mathbf{x} = \\mathbf{b}\\) is a <strong>translate</strong> of the null space:</p>
<ul>
<li>If \\(\\text{Null}(A) = \\{\\mathbf{0}\\}\\), the solution is a single point.</li>
<li>If \\(\\text{Null}(A)\\) is a line through the origin, the solution set is a parallel line.</li>
<li>If \\(\\text{Null}(A)\\) is a plane through the origin, the solution set is a parallel plane.</li>
</ul>
"""
    }
]
