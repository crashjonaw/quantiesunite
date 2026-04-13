TITLE = "Subspaces"

SECTIONS = [
    {
        "title": "Subspace Definition and Criterion",
        "body": """
        <div class='concept-box'>
        <p><strong>Subspace:</strong> A subset W of a vector space V is a subspace of V if W is itself a vector space under the same operations as V.</p>
        </div>

        <p>Rather than checking all 10 axioms for W, we only need to verify three conditions:</p>

        <div class='concept-box'>
        <p><strong>Subspace Test:</strong> A subset W ⊆ V is a subspace if and only if:</p>
        <ol>
        <li><strong>Zero element:</strong> 0 ∈ W</li>
        <li><strong>Closed under addition:</strong> If u, v ∈ W, then u + v ∈ W</li>
        <li><strong>Closed under scalar multiplication:</strong> If v ∈ W and c ∈ F, then cv ∈ W</li>
        </ol>
        </div>

        <p><strong>Why only three conditions?</strong> Once W is closed under the operations and contains 0, all other axioms (associativity, commutativity, etc.) are inherited from V. The axioms hold in V, so they hold in any subset!</p>

        <p><strong>Equivalent formulation:</strong> Conditions (2) and (3) can be combined into one:</p>
        <div class='warning-box'>
        <p>W is a subspace if and only if:</p>
        <ol>
        <li>0 ∈ W</li>
        <li>For all u, v ∈ W and c, d ∈ F: cu + dv ∈ W</li>
        </ol>
        </div>
        """
    },
    {
        "title": "Examples and Non-Examples",
        "body": """
        <p><strong>Example 1: Trivial Subspaces</strong></p>
        <div class='worked-example'>
        <p>Every vector space V has two trivial subspaces:</p>
        <ul>
        <li><strong>{0}:</strong> The zero subspace (contains only the zero element)</li>
        <li><strong>V itself:</strong> The whole space is a subspace of itself</li>
        </ul>
        <p>These are often uninteresting; we focus on proper subspaces (0 ⊂ W ⊂ V).</p>
        </div>

        <p><strong>Example 2: Lines Through Origin in ℝ²</strong></p>
        <div class='worked-example'>
        <p>Let W = {(x, y) ∈ ℝ² : y = mx} (a line through origin with slope m).</p>
        <p><strong>Is W a subspace?</strong></p>
        <ol>
        <li>Zero element: (0, 0) satisfies 0 = m·0. ✓</li>
        <li>Closed under addition: If (x₁, mx₁), (x₂, mx₂) ∈ W, then
           (x₁ + x₂, m(x₁ + x₂)) ∈ W. ✓</li>
        <li>Closed under scalar multiplication: If (x, mx) ∈ W and c ∈ ℝ, then
           (cx, mcx) ∈ W. ✓</li>
        </ol>
        <p><strong>Conclusion:</strong> W is a subspace.</p>
        </div>

        <p><strong>Example 3: Planes Through Origin in ℝ³</strong></p>
        <div class='worked-example'>
        <p>Let W = {(x, y, z) ∈ ℝ³ : ax + by + cz = 0} (plane through origin).</p>
        <p><strong>Is W a subspace?</strong></p>
        <ol>
        <li>Zero element: 0 + 0 + 0 = 0. ✓</li>
        <li>Closed under addition: If (x₁, y₁, z₁), (x₂, y₂, z₂) ∈ W, then
           a(x₁+x₂) + b(y₁+y₂) + c(z₁+z₂) = (ax₁+by₁+cz₁) + (ax₂+by₂+cz₂) = 0 + 0 = 0. ✓</li>
        <li>Closed under scalar multiplication: If (x, y, z) ∈ W and k ∈ ℝ, then
           a(kx) + b(ky) + c(kz) = k(ax+by+cz) = k·0 = 0. ✓</li>
        </ol>
        <p><strong>Conclusion:</strong> W is a subspace.</p>
        </div>

        <p><strong>Non-Example 1: Line NOT Through Origin</strong></p>
        <div class='warning-box'>
        <p>Let W = {(x, y) ∈ ℝ² : y = x + 1} (line with y-intercept 1).</p>
        <p><strong>Why is W NOT a subspace?</strong></p>
        <p>Zero element: (0, 0) does NOT satisfy 0 = 0 + 1. ✗</p>
        <p><strong>Intuition:</strong> Subspaces must pass through the origin!</p>
        </div>

        <p><strong>Non-Example 2: Set With "OR" instead of "AND"</strong></p>
        <div class='warning-box'>
        <p>Let W = {(x, y) ∈ ℝ² : xy = 0} (points on the axes).</p>
        <p><strong>Why is W NOT a subspace?</strong></p>
        <p>Closed under addition? \((1, 0) \in W\) and \((0, 1) \in W\), but \((1, 0) + (0, 1) = (1, 1) \notin W\) (product is \(1 \\neq 0\)). ✗</p>
        </div>
        """
    },
    {
        "title": "Solution Sets of Homogeneous Linear Systems",
        "body": """
        <p><strong>Key Fact:</strong> For any matrix A, the solution set of Ax = 0 is a subspace.</p>

        <div class='worked-example'>
        <p><strong>Example: Null Space</strong></p>
        <p>Let A = \\(\\begin{bmatrix} 1 & 2 & -1 \\\\ 2 & 4 & -2 \\end{bmatrix}\\)</p>
        <p>Solve Ax = 0:</p>
        <pre class='code-block'>x₁ + 2x₂ - x₃ = 0
2x₁ + 4x₂ - 2x₃ = 0  [second equation is 2× first]

Free variables: x₂ = s, x₃ = t
From first equation: x₁ = -2s + t

General solution: x = s[-2, 1, 0]ᵀ + t[1, 0, 1]ᵀ</pre>
        <p><strong>Solution set:</strong> W = {s[-2, 1, 0]ᵀ + t[1, 0, 1]ᵀ : s, t ∈ ℝ}</p>
        <p>This is a subspace of ℝ³ (it's the null space of A).</p>
        </div>

        <p><strong>Why Solution Sets Are Subspaces:</strong></p>
        <ol>
        <li>Zero element: A·0 = 0, so 0 is always a solution. ✓</li>
        <li>Closed under addition: If Ax = 0 and Ay = 0, then A(x + y) = Ax + Ay = 0 + 0 = 0. ✓</li>
        <li>Closed under scalar multiplication: If Ax = 0 and c ∈ ℝ, then A(cx) = c(Ax) = c·0 = 0. ✓</li>
        </ol>

        <p><strong>Contrast:</strong> The solution set of \(Ax = b\) (\(b \\neq 0\)) is NOT a subspace—it doesn't contain 0.</p>
        """
    },
    {
        "title": "Intersection and Union of Subspaces",
        "body": """
        <p><strong>Property 1: Intersection of Subspaces</strong></p>
        <div class='success-box'>
        <p>If W₁ and W₂ are subspaces of V, then W₁ ∩ W₂ is also a subspace of V.</p>
        </div>

        <p><strong>Proof:</strong> Let W = W₁ ∩ W₂.</p>
        <ol>
        <li>0 ∈ W₁ and 0 ∈ W₂ (both are subspaces), so 0 ∈ W₁ ∩ W₂. ✓</li>
        <li>If u, v ∈ W, then u, v ∈ W₁ and u, v ∈ W₂. Since W₁ and W₂ are subspaces, u + v ∈ W₁ and u + v ∈ W₂, so u + v ∈ W. ✓</li>
        <li>Similar argument for scalar multiplication. ✓</li>
        </ol>

        <p><strong>Property 2: Union of Subspaces (Usually NOT a subspace)</strong></p>
        <div class='warning-box'>
        <p>If W₁ and W₂ are subspaces, W₁ ∪ W₂ is usually NOT a subspace.</p>
        <p><strong>Counterexample:</strong></p>
        <p>In ℝ², let W₁ = {(x, 0)} (x-axis) and W₂ = {(0, y)} (y-axis).</p>
        <p>Both are subspaces, but (1, 0) ∈ W₁ and (0, 1) ∈ W₂, yet (1, 0) + (0, 1) = (1, 1) ∉ W₁ ∪ W₂.</p>
        </div>

        <p><strong>Instead: Sum of Subspaces</strong></p>
        <div class='concept-box'>
        <p>For subspaces W₁, W₂ of V, the <strong>sum</strong> is defined as:</p>
        <pre class='code-block'>W₁ + W₂ = {w₁ + w₂ : w₁ ∈ W₁, w₂ ∈ W₂}</pre>
        <p>This IS always a subspace of V (contains all vectors you can build by combining elements from each).</p>
        </div>
        """
    }
]
