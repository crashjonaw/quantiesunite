SECTIONS = [
    {
        "title": "Definition of a Vector Space and Axioms",
        "body": """
        <p><strong>Vector Space:</strong> A vector space V over a field F (usually ℝ or ℂ) is a set equipped with two operations—addition (u + v) and scalar multiplication (c·v)—satisfying 10 axioms:</p>

        <p><strong>Closure axioms:</strong></p>
        <ul>
        <li>(A1) Closure under addition: If u, v ∈ V, then u + v ∈ V</li>
        <li>(A2) Closure under scalar multiplication: If v ∈ V and c ∈ F, then c·v ∈ V</li>
        </ul>

        <p><strong>Addition axioms:</strong></p>
        <ul>
        <li>(A3) Associativity: (u + v) + w = u + (v + w)</li>
        <li>(A4) Commutativity: u + v = v + u</li>
        <li>(A5) Zero element: There exists 0 ∈ V such that v + 0 = v for all v ∈ V</li>
        <li>(A6) Inverse: For each v ∈ V, there exists -v ∈ V such that v + (-v) = 0</li>
        </ul>

        <p><strong>Scalar multiplication axioms:</strong></p>
        <ul>
        <li>(A7) Associativity: (cd)v = c(dv)</li>
        <li>(A8) Distributivity over vector addition: c(u + v) = cu + cv</li>
        <li>(A9) Distributivity over scalar addition: (c + d)v = cv + dv</li>
        <li>(A10) Identity: 1v = v</li>
        </ul>

        <p><strong>Examples of vector spaces:</strong></p>
        <ul>
        <li><strong>ℝⁿ:</strong> All n-tuples of real numbers with component-wise operations.</li>
        <li><strong>Mₘₓₙ(ℝ):</strong> All m × n matrices with matrix addition and scalar multiplication.</li>
        <li><strong>Pₙ(ℝ):</strong> Polynomials of degree ≤ n with real coefficients.</li>
        <li><strong>C(ℝ):</strong> All continuous functions from ℝ to ℝ.</li>
        <li><strong>Trivial space {0}:</strong> Contains only the zero vector.</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Verify ℝ² is a vector space</strong></p>
        <pre class='code-block'>V = ℝ² = {(x, y) : x, y ∈ ℝ}
Operations: (x₁, y₁) + (x₂, y₂) = (x₁ + x₂, y₁ + y₂)
           c(x, y) = (cx, cy)

Zero element: 0 = (0, 0)
Additive inverse: -(x, y) = (-x, -y)

All 10 axioms are satisfied. ℝ² is a vector space.</pre>
        </div>

        <p><strong>Consequences of the axioms:</strong> Several important facts follow from the axioms:</p>
        <ul>
        <li>The zero element is unique</li>
        <li>Each element has a unique additive inverse</li>
        <li>0v = 0 for all v ∈ V (zero scalar times any vector gives zero vector)</li>
        <li>c·0 = 0 for all c ∈ F</li>
        <li>(-1)v = -v (negative one times v is the additive inverse)</li>
        </ul>
        """
    },
    {
        "title": "Subspaces, Span, and Linear Independence",
        "body": """
        <p><strong>Subspace:</strong> A subset W of a vector space V is a subspace if:</p>
        <ol>
        <li>0 ∈ W (contains the zero vector)</li>
        <li>Closed under addition: If u, v ∈ W, then u + v ∈ W</li>
        <li>Closed under scalar multiplication: If v ∈ W and c ∈ F, then cv ∈ W</li>
        </ol>

        <p>Conditions 2 and 3 can be combined: If u, v ∈ W and c, d ∈ F, then cu + dv ∈ W.</p>

        <p><strong>Linear Combination:</strong> A vector v is a linear combination of vectors {v₁, v₂, ..., vₖ} if:</p>
        <pre class='code-block'>v = c₁v₁ + c₂v₂ + ... + cₖvₖ</pre>

        <p>for some scalars c₁, c₂, ..., cₖ.</p>

        <p><strong>Span:</strong> The span of a set S = {v₁, v₂, ..., vₖ} is the set of all linear combinations:</p>
        <pre class='code-block'>span(S) = {c₁v₁ + c₂v₂ + ... + cₖvₖ : c₁, c₂, ..., cₖ ∈ F}</pre>

        <p>Key fact: span(S) is a subspace of V.</p>

        <p><strong>Linear Dependence and Independence:</strong> A set {v₁, v₂, ..., vₖ} is:</p>
        <ul>
        <li><strong>Linearly dependent:</strong> If there exist scalars c₁, c₂, ..., cₖ (not all zero) such that c₁v₁ + c₂v₂ + ... + cₖvₖ = 0</li>
        <li><strong>Linearly independent:</strong> If c₁v₁ + c₂v₂ + ... + cₖvₖ = 0 only when c₁ = c₂ = ... = cₖ = 0</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Subspace check</strong></p>
        <pre class='code-block'>W = {(x, y, z) ∈ ℝ³ : x + 2y - z = 0}

Is W a subspace of ℝ³?
1. Zero element: (0, 0, 0) satisfies 0 + 2(0) - 0 = 0. ✓
2. Closed under addition: If (x₁, y₁, z₁), (x₂, y₂, z₂) ∈ W, then
   (x₁ + x₂) + 2(y₁ + y₂) - (z₁ + z₂) = (x₁ + 2y₁ - z₁) + (x₂ + 2y₂ - z₂) = 0 + 0 = 0 ✓
3. Closed under scalar multiplication: If (x, y, z) ∈ W and c ∈ ℝ, then
   (cx) + 2(cy) - (cz) = c(x + 2y - z) = c·0 = 0 ✓

W is a subspace.</pre>

        <p><strong>Example: Linear dependence</strong></p>
        <pre class='code-block'>In ℝ², are v₁ = [1, 2], v₂ = [3, 6] linearly independent?

Suppose c₁[1, 2] + c₂[3, 6] = [0, 0]
Then [c₁ + 3c₂, 2c₁ + 6c₂] = [0, 0]
From the first component: c₁ = -3c₂
This has non-trivial solutions (e.g., c₁ = 3, c₂ = -1).

The vectors are linearly dependent (v₂ = 3v₁).</pre>
        </div>

        <p><strong>Span interpretation:</strong> span({v₁, v₂, ..., vₖ}) is the smallest subspace containing all vᵢ. Every element of the span can be reached via linear combinations.</p>
        """
    },
    {
        "title": "Basis and Dimension",
        "body": """
        <p><strong>Basis:</strong> A set B = {v₁, v₂, ..., vₙ} is a basis for a vector space V if:</p>
        <ol>
        <li>B is linearly independent</li>
        <li>B spans V: span(B) = V</li>
        </ol>

        <p><strong>Key properties:</strong></p>
        <ul>
        <li>Every vector v ∈ V can be written <strong>uniquely</strong> as v = c₁v₁ + c₂v₂ + ... + cₙvₙ</li>
        <li>The scalars c₁, c₂, ..., cₙ are the <strong>coordinates</strong> of v with respect to B</li>
        <li>Every basis of V has the same number of elements (dimension is well-defined)</li>
        </ul>

        <p><strong>Dimension:</strong> The dimension of V, denoted dim(V), is the number of vectors in any basis of V.</p>

        <p><strong>Examples of dimensions:</strong></p>
        <ul>
        <li>dim(ℝⁿ) = n</li>
        <li>dim(Mₘₓₙ(ℝ)) = mn</li>
        <li>dim(Pₙ(ℝ)) = n + 1</li>
        <li>dim({0}) = 0</li>
        <li>dim(C(ℝ)) = ∞</li>
        </ul>

        <p><strong>Standard bases:</strong></p>
        <ul>
        <li>For ℝⁿ: e₁ = [1, 0, ..., 0], e₂ = [0, 1, ..., 0], ..., eₙ = [0, 0, ..., 1]</li>
        <li>For Mₘₓₙ: Eᵢⱼ = matrix with 1 at position (i, j) and 0s elsewhere</li>
        <li>For Pₙ(ℝ): {1, x, x², ..., xⁿ}</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Basis for a subspace</strong></p>
        <pre class='code-block'>W = {(x, y, z) ∈ ℝ³ : x + 2y - z = 0}

From the constraint: z = x + 2y
So vectors in W have the form (x, y, x + 2y) = x(1, 0, 1) + y(0, 1, 2)

B = {(1, 0, 1), (0, 1, 2)} is a basis for W.
Check: linearly independent? Only c₁(1, 0, 1) + c₂(0, 1, 2) = (0, 0, 0) if c₁ = c₂ = 0. ✓
Span? Every (x, y, x+2y) ∈ W is a linear combination of these two vectors. ✓

dim(W) = 2</pre>
        </div>

        <p><strong>Dimension and rank connection:</strong> For an m × n matrix A:</p>
        <ul>
        <li>rank(A) = dimension of the column space (column space is the span of columns)</li>
        <li>rank(A) = dimension of the row space</li>
        <li>dim(nullspace of A) = n - rank(A)</li>
        </ul>

        <p><strong>Rank-Nullity Theorem:</strong> For an m × n matrix A:</p>
        <pre class='code-block'>rank(A) + nullity(A) = n
where nullity(A) = dim(null space of A)</pre>
        """
    },
    {
        "title": "Row Space, Column Space, and Null Space",
        "body": """
        <p><strong>Fundamental subspaces of an m × n matrix A:</strong></p>

        <p><strong>1. Column Space (Range):</strong> Col(A) = span of columns of A. This is a subspace of ℝᵐ.</p>
        <p>rank(A) = dim(Col(A))</p>

        <p><strong>2. Row Space:</strong> Row(A) = span of rows of A. This is a subspace of ℝⁿ.</p>
        <p>rank(A) = dim(Row(A)) = rank(Aᵀ)</p>

        <p><strong>3. Null Space (Kernel):</strong> Null(A) = {x ∈ ℝⁿ : Ax = 0}. This is a subspace of ℝⁿ.</p>
        <p>nullity(A) = dim(Null(A)) = n - rank(A)</p>

        <p><strong>4. Left Null Space:</strong> Null(Aᵀ) = {y ∈ ℝᵐ : Aᵀy = 0}. This is a subspace of ℝᵐ.</p>
        <p>dim(Null(Aᵀ)) = m - rank(A)</p>

        <p><strong>Key relationships:</strong></p>
        <ul>
        <li>Row(A) and Null(A) are orthogonal complements in ℝⁿ (Chapter on Orthogonality)</li>
        <li>Col(A) and Null(Aᵀ) are orthogonal complements in ℝᵐ</li>
        <li>Col(A) = Row(Aᵀ)</li>
        <li>Null(A) = Null(Rref(A))</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Finding bases for fundamental subspaces</strong></p>
        <pre class='code-block'>A = [1  2 -1]
    [2  4 -2]

Step 1: Reduce to RREF
R₂ - 2R₁ → R₂:
[1  2 -1]
[0  0  0]

RREF: A and its RREF have the same null space and row space.

Col(A): The first column is a pivot column, so a basis for Col(A) is {[1, 2]ᵀ}
Rank(A) = 1

Row(A): The nonzero row [1 2 -1] is a basis for Row(A)

Null(A): Solve Ax = 0. Free variables: x₂ = s, x₃ = t
From x₁ + 2x₂ - x₃ = 0: x₁ = -2s + t
General solution: x = [-2s + t, s, t] = s[-2, 1, 0] + t[1, 0, 1]
Basis for Null(A): {[-2, 1, 0], [1, 0, 1]}
nullity(A) = 2

Check: rank + nullity = 1 + 2 = 3 ✓</pre>
        </div>

        <p><strong>Computing null space from RREF:</strong> If the RREF of A has free variables corresponding to columns j₁, j₂, ..., for each free variable, set it to 1 (other free variables to 0) and solve for dependent variables. This gives a basis vector for the null space.</p>

        <p><strong>Applications:</strong> The fundamental subspaces are essential for understanding:</p>
        <ul>
        <li>Solvability of Ax = b (b must be in Col(A))</li>
        <li>Solution structure for Ax = 0 (parametrized by free variables)</li>
        <li>Least squares problems (projection onto Col(A))</li>
        </ul>
        """
    },
    {
        "title": "Coordinate Systems and Change of Basis",
        "body": """
        <p><strong>Coordinates with respect to a basis:</strong> If B = {v₁, v₂, ..., vₙ} is a basis for V and v ∈ V, the <strong>coordinate vector</strong> [v]_B is:</p>
        <pre class='code-block'>[v]_B = [c₁, c₂, ..., cₙ]ᵀ where v = c₁v₁ + c₂v₂ + ... + cₙvₙ</pre>

        <p>The coordinate vector is unique because the basis representation is unique.</p>

        <p><strong>Change of Basis Formula:</strong> If B and B' are two bases for V, the change of basis matrix P (from B to B') is constructed with columns being the coordinates of B' vectors with respect to B:</p>
        <pre class='code-block'>P = [column coords of b'₁ with respect to B | ... | column coords of b'ₙ with respect to B]</pre>

        <p>The relationship between coordinates is:</p>
        <pre class='code-block'>[v]_{B'} = P^{-1} [v]_B</pre>

        <p>or equivalently:</p>
        <pre class='code-block'>[v]_B = P [v]_{B'}</pre>

        <div class='example-box'>
        <p><strong>Example: Change of basis in ℝ²</strong></p>
        <pre class='code-block'>Standard basis B = {e₁ = [1, 0], e₂ = [0, 1]}
New basis B' = {v₁ = [1, 1], v₂ = [1, -1]}

Express B' in terms of B:
[1, 1] = 1·[1, 0] + 1·[0, 1], so [v₁]_B = [1, 1]ᵀ
[1, -1] = 1·[1, 0] + (-1)·[0, 1], so [v₂]_B = [1, -1]ᵀ

Change of basis matrix P:
P = [1  1]
    [1 -1]

For a vector u with [u]_B = [2, 3]ᵀ (i.e., u = 2e₁ + 3e₂ = [2, 3]):
[u]_{B'} = P^{-1} [u]_B

P^{-1} = (1/(-2)) [-1 -1] = [1/2  1/2]
                [−1  1]   [1/2 -1/2]

[u]_{B'} = [1/2  1/2] [2] = [5/2]
           [1/2 -1/2] [3]   [-1/2]

Verify: u = (5/2)[1, 1] + (-1/2)[1, -1] = [5/2 - 1/2, 5/2 + 1/2] = [2, 3] ✓</pre>
        </div>

        <p><strong>Applications of change of basis:</strong></p>
        <ul>
        <li><strong>Diagonalization:</strong> Choose the basis of eigenvectors to make a linear transformation diagonal</li>
        <li><strong>Simplification:</strong> Some bases make computations easier (e.g., orthonormal bases for projections)</li>
        <li><strong>Principal component analysis (PCA):</strong> Change to basis of eigenvectors to simplify data</li>
        </ul>
        """
    }
]
