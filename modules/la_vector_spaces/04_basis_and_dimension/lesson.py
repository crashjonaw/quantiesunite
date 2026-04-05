TITLE = "Basis and Dimension"

SECTIONS = [
    {
        "title": "Basis Definition and Properties",
        "body": """
        <div class='concept-box'>
        <p><strong>Basis:</strong> A set B = {v₁, v₂, ..., vₙ} is a basis for a vector space V if:</p>
        <ol>
        <li>B is linearly independent</li>
        <li>B spans V: span(B) = V</li>
        </ol>
        </div>

        <p><strong>Intuition:</strong> A basis is a minimal spanning set—it contains the fewest vectors needed to generate the entire space.</p>

        <p><strong>Key Property - Unique Representation:</strong></p>
        <div class='success-box'>
        <p>If B = {v₁, v₂, ..., vₙ} is a basis for V, then every vector v ∈ V can be written <strong>uniquely</strong> as:</p>
        <pre class='code-block'>v = c₁v₁ + c₂v₂ + ... + cₙvₙ</pre>
        <p>The scalars c₁, c₂, ..., cₙ are called the <strong>coordinates</strong> of v with respect to B.</p>
        </div>

        <p><strong>Why Uniqueness?</strong> Linear independence guarantees this. If two representations existed:</p>
        <pre class='code-block'>v = c₁v₁ + ... + cₙvₙ = d₁v₁ + ... + dₙvₙ</pre>
        <p>Then (c₁ - d₁)v₁ + ... + (cₙ - dₙ)vₙ = 0. By linear independence, all coefficients are 0, so cᵢ = dᵢ.</p>

        <p><strong>Spanning ensures existence; independence ensures uniqueness.</strong></p>
        """
    },
    {
        "title": "Standard Bases and Examples",
        "body": """
        <p><strong>Example 1: Standard Basis of ℝⁿ</strong></p>
        <div class='worked-example'>
        <p>In ℝⁿ, the <strong>standard basis</strong> is:</p>
        <pre class='code-block'>E = {e₁, e₂, ..., eₙ}</pre>
        <p>where eᵢ has a 1 in position i and 0s elsewhere:</p>
        <pre class='code-block'>e₁ = [1, 0, 0, ..., 0]
e₂ = [0, 1, 0, ..., 0]
eₙ = [0, 0, 0, ..., 1]</pre>
        <p><strong>Why is it a basis?</strong></p>
        <ul>
        <li><strong>Spanning:</strong> Any vector [x₁, x₂, ..., xₙ] = x₁e₁ + x₂e₂ + ... + xₙeₙ</li>
        <li><strong>Independence:</strong> If Σcᵢeᵢ = 0, then [c₁, c₂, ..., cₙ] = [0, 0, ..., 0], so all cᵢ = 0</li>
        </ul>
        <p><strong>Coordinates:</strong> [x₁, x₂, ..., xₙ] has coordinates (x₁, x₂, ..., xₙ) with respect to E (same as the vector itself).</p>
        </div>

        <p><strong>Example 2: Basis for Polynomials Pₙ(ℝ)</strong></p>
        <div class='worked-example'>
        <p>The standard basis for polynomials of degree ≤ n is:</p>
        <pre class='code-block'>B = {1, x, x², ..., xⁿ}</pre>
        <p>This set has n + 1 elements.</p>
        <p><strong>Why is it a basis?</strong></p>
        <ul>
        <li><strong>Spanning:</strong> Any polynomial a₀ + a₁x + ... + aₙxⁿ is a linear combination of these</li>
        <li><strong>Independence:</strong> If a₀·1 + a₁·x + ... + aₙ·xⁿ = 0 (zero polynomial), then aᵢ = 0 for all i</li>
        </ul>
        </div>

        <p><strong>Example 3: Basis for Matrices Mₘₓₙ(ℝ)</strong></p>
        <div class='worked-example'>
        <p>A basis consists of all matrices Eᵢⱼ with a 1 at position (i, j) and 0s elsewhere:</p>
        <pre class='code-block'>B = {E₁₁, E₁₂, ..., Eₘₙ}</pre>
        <p>This set has m·n elements.</p>
        <p><strong>Example for M₂ₓ₂:</strong></p>
        <pre class='code-block'>E₁₁ = [1 0]    E₁₂ = [0 1]    E₂₁ = [0 0]    E₂₂ = [0 0]
      [0 0]          [0 0]          [1 0]          [0 1]</pre>
        </div>

        <p><strong>Example 4: Non-Standard Basis</strong></p>
        <div class='worked-example'>
        <p>In ℝ², let B = {[1, 1], [1, -1]}.</p>
        <p><strong>Is B a basis?</strong></p>
        <ul>
        <li><strong>Spanning:</strong> Any [x, y] = c₁[1, 1] + c₂[1, -1] = [c₁ + c₂, c₁ - c₂]
          So x = c₁ + c₂, y = c₁ - c₂. Solving: c₁ = (x+y)/2, c₂ = (x-y)/2. ✓</li>
        <li><strong>Independence:</strong> If c₁[1, 1] + c₂[1, -1] = [0, 0], then c₁ + c₂ = 0 and c₁ - c₂ = 0.
          Solving: c₁ = 0, c₂ = 0. ✓</li>
        </ul>
        <p>Yes, B is a basis!</p>
        <p><strong>Coordinates of [3, 1]:</strong> c₁ = (3+1)/2 = 2, c₂ = (3-1)/2 = 1, so [3, 1] = 2[1, 1] + 1[1, -1]</p>
        </div>
        """
    },
    {
        "title": "Dimension",
        "body": """
        <div class='concept-box'>
        <p><strong>Dimension:</strong> The dimension of a vector space V, denoted dim(V), is the number of vectors in any basis of V.</p>
        </div>

        <p><strong>Key Theorem:</strong> Every basis of a vector space V has the same number of elements. This makes dimension well-defined.</p>

        <p><strong>Examples of Dimensions:</strong></p>
        <div class='worked-example'>
        <ul>
        <li>dim(ℝⁿ) = n (n standard basis vectors)</li>
        <li>dim(Pₙ(ℝ)) = n + 1 (polynomials have n+1 basis vectors {1, x, ..., xⁿ})</li>
        <li>dim(Mₘₓₙ(ℝ)) = m·n (m×n matrices have m·n basis vectors)</li>
        <li>dim({0}) = 0 (zero space has empty basis)</li>
        <li>dim(C(ℝ)) = ∞ (infinite-dimensional space of continuous functions)</li>
        </ul>
        </div>

        <p><strong>Dimension of Subspaces:</strong></p>
        <p>If W is a subspace of V, then dim(W) ≤ dim(V), with equality only if W = V.</p>

        <div class='worked-example'>
        <p><strong>Example: Dimension of Constraint Space</strong></p>
        <p>Let W = {(x, y, z) ∈ ℝ³ : x + 2y - z = 0}.</p>
        <p><strong>Find dim(W):</strong></p>
        <p>From the constraint: z = x + 2y, so vectors in W have the form:</p>
        <pre class='code-block'>(x, y, x + 2y) = x(1, 0, 1) + y(0, 1, 2)</pre>
        <p>A basis for W is {(1, 0, 1), (0, 1, 2)}.</p>
        <p>Therefore, dim(W) = 2.</p>
        </div>

        <p><strong>Interpretation:</strong> dim(V) tells you:</p>
        <ul>
        <li>How many parameters you need to specify a vector</li>
        <li>The "degrees of freedom" in the space</li>
        <li>The size of any basis</li>
        </ul>
        """
    },
    {
        "title": "Rank, Nullity, and the Rank-Nullity Theorem",
        "body": """
        <p><strong>Definitions for an m × n matrix A:</strong></p>

        <div class='concept-box'>
        <ul>
        <li><strong>Rank(A):</strong> The dimension of the column space (number of pivot columns)</li>
        <li><strong>Nullity(A):</strong> The dimension of the null space (number of free variables)</li>
        </ul>
        </div>

        <p><strong>The Rank-Nullity Theorem:</strong></p>
        <div class='success-box'>
        <p>For an m × n matrix A:</p>
        <pre class='code-block'>rank(A) + nullity(A) = n</pre>
        <p>where n is the number of columns.</p>
        </div>

        <p><strong>Interpretation:</strong> Every column is either pivotal (contributing to rank) or free (contributing to nullity).</p>

        <div class='worked-example'>
        <p><strong>Example:</strong></p>
        <p>Let A = \\(\\begin{bmatrix} 1 & 2 & -1 \\\\ 2 & 4 & -2 \\end{bmatrix}\\)</p>
        <p>RREF form:</p>
        <pre class='code-block'>[1  2 -1]
[0  0  0]</pre>
        <p>One pivot (column 1), two free variables (columns 2, 3).</p>
        <p>rank(A) = 1, nullity(A) = 2</p>
        <p>Check: 1 + 2 = 3 ✓</p>
        </div>

        <p><strong>Fundamental Subspaces:</strong> For m × n matrix A:</p>
        <ul>
        <li>dim(Col(A)) = rank(A)</li>
        <li>dim(Null(A)) = nullity(A) = n - rank(A)</li>
        <li>dim(Row(A)) = rank(A) (row rank = column rank)</li>
        <li>dim(Null(Aᵀ)) = m - rank(A)</li>
        </ul>

        <p><strong>Application: Existence and Uniqueness of Solutions</strong></p>
        <p>For Ax = b:</p>
        <ul>
        <li>Solvable for any b ⟺ rank(A) = m (all rows are used)</li>
        <li>Unique solution ⟺ rank(A) = n (no free variables)</li>
        <li>Unique solution for all b ⟺ A is m × n with rank m = n (square, invertible)</li>
        </ul>
        """
    }
]
