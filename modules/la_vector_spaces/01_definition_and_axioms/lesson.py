TITLE = "Definition and Axioms"

SECTIONS = [
    {
        "title": "Vector Space Definition",
        "body": """
        <div class='concept-box'>
        <p><strong>Vector Space:</strong> A vector space V over a field F (usually ℝ or ℂ) is a set equipped with two operations—addition (u + v) and scalar multiplication (c·v)—satisfying 10 axioms.</p>
        </div>

        <p>The field F provides the scalars. Common choices are:</p>
        <ul>
        <li><strong>ℝ:</strong> Real numbers (most applications)</li>
        <li><strong>ℂ:</strong> Complex numbers (quantum mechanics, signal processing)</li>
        <li><strong>𝔽₂:</strong> Binary field {0, 1} (coding theory, cryptography)</li>
        </ul>

        <p>Two operations must be defined:</p>
        <ul>
        <li><strong>Vector addition:</strong> u + v ∈ V for u, v ∈ V</li>
        <li><strong>Scalar multiplication:</strong> c·v ∈ V for c ∈ F, v ∈ V</li>
        </ul>

        <p><strong>Notation:</strong> We write vectors as u, v, w or \\(\\mathbf{u}, \\mathbf{v}\\), and scalars as c, d, α, β.</p>
        """
    },
    {
        "title": "The 10 Axioms",
        "body": """
        <p>For V to be a vector space, the operations must satisfy these 10 axioms:</p>

        <div class='concept-box'>
        <p><strong>Closure Axioms:</strong></p>
        <ul>
        <li>(A1) Closure under addition: If u, v ∈ V, then u + v ∈ V</li>
        <li>(A2) Closure under scalar multiplication: If v ∈ V and c ∈ F, then c·v ∈ V</li>
        </ul>

        <p><strong>Addition Axioms:</strong></p>
        <ul>
        <li>(A3) Associativity of addition: (u + v) + w = u + (v + w)</li>
        <li>(A4) Commutativity of addition: u + v = v + u</li>
        <li>(A5) Additive identity (zero element): There exists 0 ∈ V such that v + 0 = v for all v ∈ V</li>
        <li>(A6) Additive inverses: For each v ∈ V, there exists -v ∈ V such that v + (-v) = 0</li>
        </ul>

        <p><strong>Scalar Multiplication Axioms:</strong></p>
        <ul>
        <li>(A7) Associativity of scalar multiplication: (cd)v = c(dv)</li>
        <li>(A8) Distributivity over vector addition: c(u + v) = cu + cv</li>
        <li>(A9) Distributivity over scalar addition: (c + d)v = cv + dv</li>
        <li>(A10) Scalar multiplicative identity: 1v = v</li>
        </ul>
        </div>

        <p><strong>Interpretations:</strong></p>
        <ul>
        <li><strong>A1 & A2:</strong> The space is "closed"—operations don't produce anything outside V</li>
        <li><strong>A3-A6:</strong> Vector addition behaves like addition of numbers</li>
        <li><strong>A7-A10:</strong> Scalar multiplication interacts naturally with both addition and field operations</li>
        </ul>
        """
    },
    {
        "title": "Examples of Vector Spaces",
        "body": """
        <p><strong>Classical Examples:</strong></p>

        <div class='worked-example'>
        <p><strong>Example 1: Euclidean Space ℝⁿ</strong></p>
        <p>The set of all n-tuples of real numbers:</p>
        <pre class='code-block'>V = ℝⁿ = {(x₁, x₂, ..., xₙ) : xᵢ ∈ ℝ}</pre>
        <p>Operations are component-wise:</p>
        <pre class='code-block'>(x₁,...,xₙ) + (y₁,...,yₙ) = (x₁+y₁,...,xₙ+yₙ)
c(x₁,...,xₙ) = (cx₁,...,cxₙ)</pre>
        <p>Zero element: (0, 0, ..., 0)</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example 2: Matrices Mₘₓₙ(ℝ)</strong></p>
        <p>The set of all m × n matrices with real entries:</p>
        <pre class='code-block'>V = Mₘₓₙ(ℝ) = {m×n matrices with entries in ℝ}</pre>
        <p>Operations are matrix addition and scalar multiplication:</p>
        <pre class='code-block'>(A + B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ
(cA)ᵢⱼ = cAᵢⱼ</pre>
        <p>Zero element: the zero matrix (all entries 0)</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example 3: Polynomials Pₙ(ℝ)</strong></p>
        <p>The set of polynomials of degree at most n with real coefficients:</p>
        <pre class='code-block'>V = Pₙ(ℝ) = {a₀ + a₁x + a₂x² + ... + aₙxⁿ : aᵢ ∈ ℝ}</pre>
        <p>Operations are polynomial addition and scalar multiplication:</p>
        <pre class='code-block'>(p + q)(x) = p(x) + q(x)
(cp)(x) = c·p(x)</pre>
        <p>Zero element: the zero polynomial (all coefficients 0)</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example 4: Continuous Functions C(ℝ)</strong></p>
        <p>The set of all continuous functions from ℝ to ℝ:</p>
        <pre class='code-block'>V = C(ℝ) = {f: ℝ → ℝ : f is continuous}</pre>
        <p>Operations are pointwise addition and scalar multiplication:</p>
        <pre class='code-block'>(f + g)(x) = f(x) + g(x)
(cf)(x) = c·f(x)</pre>
        <p>Zero element: the zero function (f(x) = 0 for all x)</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example 5: Trivial Space {0}</strong></p>
        <p>The space containing only the zero vector:</p>
        <pre class='code-block'>V = {0}</pre>
        <p>Only element: 0 (which is both the additive identity and the zero scalar multiple)</p>
        <p>This is a valid vector space (though not very interesting!)</p>
        </div>
        """
    },
    {
        "title": "Consequences of the Axioms",
        "body": """
        <p>From the 10 axioms alone, several important facts follow without additional assumption:</p>

        <div class='success-box'>
        <p><strong>Theorem:</strong> In any vector space V over field F:</p>
        <ol>
        <li>The zero element 0 is <strong>unique</strong>: there is exactly one zero vector</li>
        <li>For each v ∈ V, the additive inverse -v is <strong>unique</strong></li>
        <li>0v = 0 for all v ∈ V (zero scalar times any vector gives zero vector)</li>
        <li>c·0 = 0 for all c ∈ F (any scalar times zero vector gives zero vector)</li>
        <li>(-1)v = -v (negative one times v equals the additive inverse of v)</li>
        <li>If cv = 0, then either c = 0 or v = 0</li>
        </ol>
        </div>

        <p><strong>Proof sketch of Uniqueness of Zero:</strong></p>
        <p>Suppose 0' is also a zero element. Then:</p>
        <pre class='code-block'>0' = 0' + 0  [using 0 as additive identity]
   = 0       [using 0' as additive identity]</pre>
        <p>So any two zero elements are equal. ∎</p>

        <p><strong>Proof sketch of 0v = 0:</strong></p>
        <pre class='code-block'>0v = (0 + 0)v  [since 0 + 0 = 0 in ℝ]
   = 0v + 0v    [by A9: distributivity]</pre>
        <p>Adding -0v to both sides gives 0v = 0. ∎</p>

        <p><strong>Key insight:</strong> These properties hold in every vector space—they're "free" consequences of the axioms. This is why the axiomatic definition is powerful: we prove things once in full generality!</p>
        """
    }
]
