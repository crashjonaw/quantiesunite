TITLE = "Linear Independence and Span"

SECTIONS = [
    {
        "title": "Linear Combinations",
        "body": """
        <div class='concept-box'>
        <p><strong>Linear Combination:</strong> A vector $\\mathbf{v}$ is a linear combination of vectors $\\{\\mathbf{v}_1, \\mathbf{v}_2, \\ldots, \\mathbf{v}_k\\}$ if:</p>
        <p>$$\\mathbf{v} = c_1 \\mathbf{v}_1 + c_2 \\mathbf{v}_2 + \\cdots + c_k \\mathbf{v}_k$$</p>
        <p>for some scalars $c_1, c_2, \\ldots, c_k \\in F$.</p>
        </div>

        <p><strong>Interpretation:</strong> We're asking whether $\\mathbf{v}$ can be "built" from the given vectors using addition and scalar multiplication.</p>

        <p><strong>Key Question:</strong> Given vectors $\\mathbf{v}_1, \\mathbf{v}_2, \\ldots, \\mathbf{v}_k$, what vectors can we reach?</p>
        <p>Answer: All their linear combinations.</p>

        <div class='worked-example'>
        <p><strong>Example in $\\mathbb{R}^2$:</strong></p>
        <p>Let $\\mathbf{v}_1 = [1, 0]$ and $\\mathbf{v}_2 = [0, 1]$. What linear combinations can we form?</p>
        <p>$$c_1[1, 0] + c_2[0, 1] = [c_1, c_2]$$</p>
        <p>By varying $c_1$ and $c_2$, we can reach any point $(x, y)$ in $\\mathbb{R}^2$.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example in $\\mathbb{R}^3$:</strong></p>
        <p>Let $\\mathbf{v}_1 = [1, 0, 0]$ and $\\mathbf{v}_2 = [0, 1, 0]$. Linear combinations are:</p>
        <p>$$c_1[1, 0, 0] + c_2[0, 1, 0] = [c_1, c_2, 0]$$</p>
        <p>We can only reach points in the $xy$-plane, not all of $\\mathbb{R}^3$.</p>
        </div>
        """
    },
    {
        "title": "Span of a Set",
        "body": """
        <div class='concept-box'>
        <p><strong>Span:</strong> The span of a set $S = \\{\\mathbf{v}_1, \\mathbf{v}_2, \\ldots, \\mathbf{v}_k\\}$ is the set of all linear combinations:</p>
        <p>$$\\text{span}(S) = \\{c_1 \\mathbf{v}_1 + c_2 \\mathbf{v}_2 + \\cdots + c_k \\mathbf{v}_k : c_1, c_2, \\ldots, c_k \\in F\\}$$</p>
        </div>

        <p><strong>Notation:</strong> Sometimes written as $\\text{span}\\{\\mathbf{v}_1, \\mathbf{v}_2, \\ldots, \\mathbf{v}_k\\}$ or $[\\mathbf{v}_1, \\mathbf{v}_2, \\ldots, \\mathbf{v}_k]$.</p>

        <p><strong>Key Property:</strong> $\\text{span}(S)$ is always a subspace of $V$.</p>

        <div class='success-box'>
        <p><strong>Proof that $\\text{span}(S)$ is a subspace:</strong></p>
        <ol>
        <li>Zero element: $\\mathbf{0} = 0 \\cdot \\mathbf{v}_1 + 0 \\cdot \\mathbf{v}_2 + \\cdots + 0 \\cdot \\mathbf{v}_k \\in \\text{span}(S)$. ✓</li>
        <li>Closed under addition: If $\\mathbf{u} = \\sum c_i \\mathbf{v}_i$ and $\\mathbf{w} = \\sum d_i \\mathbf{v}_i$, then
           $\\mathbf{u} + \\mathbf{w} = \\sum (c_i + d_i) \\mathbf{v}_i \\in \\text{span}(S)$. ✓</li>
        <li>Closed under scalar multiplication: If $\\mathbf{u} = \\sum c_i \\mathbf{v}_i$ and $k \\in F$, then
           $k\\mathbf{u} = \\sum (kc_i) \\mathbf{v}_i \\in \\text{span}(S)$. ✓</li>
        </ol>
        </div>

        <p><strong>Spanning Set:</strong> If $\\text{span}(S) = V$, we say $S$ is a <strong>spanning set</strong> (or generating set) for $V$.</p>

        <div class='worked-example'>
        <p><strong>Example: Span in $\\mathbb{R}^3$</strong></p>
        <p>Let $\\mathbf{v}_1 = [1, 0, 0]$, $\\mathbf{v}_2 = [0, 1, 0]$, $\\mathbf{v}_3 = [0, 0, 1]$.</p>
        <p>$\\text{span}\\{\\mathbf{v}_1, \\mathbf{v}_2, \\mathbf{v}_3\\} = \\{[x, y, z] : x, y, z \\in \\mathbb{R}\\} = \\mathbb{R}^3$</p>
        <p>This set spans $\\mathbb{R}^3$.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Non-Spanning Set</strong></p>
        <p>Let $\\mathbf{v}_1 = [1, 0, 0]$, $\\mathbf{v}_2 = [0, 1, 0]$.</p>
        <p>$\\text{span}\\{\\mathbf{v}_1, \\mathbf{v}_2\\} = \\{[x, y, 0] : x, y \\in \\mathbb{R}\\} \\neq \\mathbb{R}^3$</p>
        <p>For instance, $[0, 0, 1]$ cannot be written as $c_1[1, 0, 0] + c_2[0, 1, 0]$.</p>
        </div>
        """
    },
    {
        "title": "Linear Dependence and Independence",
        "body": """
        <p><strong>Motivation:</strong> When we have many vectors, some might be "redundant"—expressible in terms of others.</p>

        <div class='concept-box'>
        <p><strong>Linearly Dependent:</strong> A set $\\{\\mathbf{v}_1, \\mathbf{v}_2, \\ldots, \\mathbf{v}_k\\}$ is linearly dependent if there exist scalars $c_1, c_2, \\ldots, c_k$ (not all zero) such that:</p>
        <p>$$c_1 \\mathbf{v}_1 + c_2 \\mathbf{v}_2 + \\cdots + c_k \\mathbf{v}_k = \\mathbf{0}$$</p>
        </div>

        <div class='concept-box'>
        <p><strong>Linearly Independent:</strong> A set $\\{\\mathbf{v}_1, \\mathbf{v}_2, \\ldots, \\mathbf{v}_k\\}$ is linearly independent if the only scalars satisfying</p>
        <p>$$c_1 \\mathbf{v}_1 + c_2 \\mathbf{v}_2 + \\cdots + c_k \\mathbf{v}_k = \\mathbf{0}$$</p>
        <p>are $c_1 = c_2 = \\cdots = c_k = 0$ (the trivial solution).</p>
        </div>

        <p><strong>Intuition:</strong> Linearly independent vectors are "genuinely different"—none is redundant.</p>

        <div class='worked-example'>
        <p><strong>Example: Linearly Dependent</strong></p>
        <p>In $\\mathbb{R}^2$, are $\\mathbf{v}_1 = [1, 2]$, $\\mathbf{v}_2 = [2, 4]$ linearly independent?</p>
        <p>Notice $\\mathbf{v}_2 = 2\\mathbf{v}_1$, so:</p>
        <p>$$2 \\cdot [1, 2] + (-1) \\cdot [2, 4] = [2, 4] - [2, 4] = [0, 0]$$</p>
        <p>Non-trivial solution exists ($c_1 = 2$, $c_2 = -1$). Therefore, the set is <strong>linearly dependent</strong>.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Linearly Independent</strong></p>
        <p>In $\\mathbb{R}^2$, are $\\mathbf{v}_1 = [1, 0]$, $\\mathbf{v}_2 = [0, 1]$ linearly independent?</p>
        <p>Suppose $c_1[1, 0] + c_2[0, 1] = [0, 0]$:</p>
        <p>$$[c_1, c_2] = [0, 0]$$</p>
        <p>This forces $c_1 = 0$ and $c_2 = 0$. Only trivial solution exists. Therefore, the set is <strong>linearly independent</strong>.</p>
        </div>

        <p><strong>Single Vector:</strong> A set $\\{\\mathbf{v}\\}$ is linearly independent if and only if $\\mathbf{v} \\neq \\mathbf{0}$.</p>

        <p><strong>Important Facts:</strong></p>
        <ul>
        <li>If a set contains the zero vector, it's automatically linearly dependent</li>
        <li>If a set contains repeated vectors, it's automatically linearly dependent</li>
        <li>If one vector is a scalar multiple of another, the set is linearly dependent</li>
        </ul>
        """
    },
    {
        "title": "Testing Independence in \\(\\mathbb{R}^n\\)",
        "body": """
        <p><strong>Method: Row Reduction</strong></p>

        <p>To test if vectors $\\mathbf{v}_1, \\mathbf{v}_2, \\ldots, \\mathbf{v}_k$ in $\\mathbb{R}^n$ are linearly independent:</p>
        <ol>
        <li>Form a matrix $A$ with $\\mathbf{v}_1, \\mathbf{v}_2, \\ldots, \\mathbf{v}_k$ as columns</li>
        <li>Compute $\\text{RREF}(A)$</li>
        <li>If every column has a pivot, the vectors are linearly independent</li>
        <li>If any column has no pivot (free variable), they're linearly dependent</li>
        </ol>

        <div class='worked-example'>
        <p><strong>Example 1: Check Independence</strong></p>
        <p>Are $\\mathbf{v}_1 = [1, 2, 1]$, $\\mathbf{v}_2 = [2, 4, 2]$, $\\mathbf{v}_3 = [1, 1, 1]$ independent in $\\mathbb{R}^3$?</p>
        <p>Form matrix and reduce:</p>
        <pre class='code-block'>$$A = \\begin{bmatrix} 1 & 2 & 1 \\\\ 2 & 4 & 2 \\\\ 1 & 1 & 1 \\end{bmatrix} \\xrightarrow{R_2 - 2R_1,\\; R_3 - R_1} \\begin{bmatrix} 1 & 2 & 1 \\\\ 0 & 0 & 0 \\\\ 0 & -1 & 0 \\end{bmatrix}$$

After row swapping to get to RREF:
$$\\begin{bmatrix} 1 & 2 & 1 \\\\ 0 & -1 & 0 \\\\ 0 & 0 & 0 \\end{bmatrix} \\to \\begin{bmatrix} 1 & 0 & 1 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 0 \\end{bmatrix}$$</pre>
        <p>Column 3 has no pivot. So $c_3$ is a free variable, meaning there's a non-trivial solution.</p>
        <p><strong>Conclusion:</strong> The vectors are <strong>linearly dependent</strong>.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example 2: Square Matrix - Use Determinant</strong></p>
        <p>Are $\\mathbf{v}_1 = [1, 2, 0]$, $\\mathbf{v}_2 = [0, 1, 1]$, $\\mathbf{v}_3 = [1, 0, 2]$ independent?</p>
        <p>Form matrix $A$ with these as columns:</p>
        <pre class='code-block'>$$A = \\begin{bmatrix} 1 & 0 & 1 \\\\ 2 & 1 & 0 \\\\ 0 & 1 & 2 \\end{bmatrix}$$

$$\\det(A) = 1(1 \\cdot 2 - 0 \\cdot 1) - 0 + 1(2 \\cdot 1 - 1 \\cdot 0) = 1(2) + 1(2) = 4 \\neq 0$$</pre>
        <p>Non-zero determinant means full rank, so <strong>linearly independent</strong>.</p>
        </div>

        <p><strong>Quick Fact:</strong> For $n$ vectors in $\\mathbb{R}^n$, they're independent $\\iff \\det([\\mathbf{v}_1 \\; \\mathbf{v}_2 \\; \\cdots \\; \\mathbf{v}_n]) \\neq 0$.</p>
        """
    }
]
