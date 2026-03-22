SECTIONS = [
    {
        "title": "Definition and Properties of Linear Transformations",
        "body": """
        <p><strong>Linear Transformation:</strong> A function T: V → W between vector spaces is a linear transformation (or linear map) if:</p>
        <ol>
        <li><strong>Additivity:</strong> T(u + v) = T(u) + T(v) for all u, v ∈ V</li>
        <li><strong>Homogeneity:</strong> T(cv) = cT(v) for all c ∈ F and v ∈ V</li>
        </ol>

        <p>These conditions are equivalent to: T(cu + dv) = cT(u) + dT(v) for all u, v ∈ V and c, d ∈ F (preserves linear combinations).</p>

        <p><strong>Examples of linear transformations:</strong></p>
        <ul>
        <li><strong>Matrix multiplication:</strong> T(x) = Ax (from ℝⁿ to ℝᵐ)</li>
        <li><strong>Projection:</strong> T(x) = proj_W(x) (orthogonal projection onto a subspace W)</li>
        <li><strong>Differentiation:</strong> T(p) = p' (from Pₙ(ℝ) to Pₙ₋₁(ℝ))</li>
        <li><strong>Integration:</strong> T(f) = ∫f(x)dx (from C(ℝ) to ℝ)</li>
        <li><strong>Rotation:</strong> T(v) = Rθv (rotation in the plane by angle θ)</li>
        <li><strong>Reflection:</strong> T(v) = reflection of v across a line/plane</li>
        </ul>

        <p><strong>Key properties:</strong></p>
        <ul>
        <li>T(0) = 0 (zero vector maps to zero vector)</li>
        <li>T(-v) = -T(v)</li>
        <li>Composition of linear transformations is linear: If T: U → V and S: V → W are linear, then S ∘ T: U → W is linear</li>
        <li>Inverse of a bijective linear transformation is linear</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Verify T(x, y) = (2x - y, x + y) is linear</strong></p>
        <pre class='code-block'>Additivity: T((x₁, y₁) + (x₂, y₂)) = T((x₁+x₂, y₁+y₂))
           = (2(x₁+x₂) - (y₁+y₂), (x₁+x₂) + (y₁+y₂))
           = (2x₁ - y₁ + 2x₂ - y₂, x₁ + y₁ + x₂ + y₂)
           = (2x₁ - y₁, x₁ + y₁) + (2x₂ - y₂, x₂ + y₂)
           = T(x₁, y₁) + T(x₂, y₂) ✓

Homogeneity: T(c(x, y)) = T((cx, cy))
            = (2cx - cy, cx + cy)
            = c(2x - y, x + y)
            = cT(x, y) ✓

T is linear.</pre>
        </div>

        <p><strong>Non-linear examples (counterexamples):</strong></p>
        <ul>
        <li>T(x, y) = (x², y) is not linear (not additive: T(1,0) + T(1,0) = 2 but T(2,0) = 4)</li>
        <li>T(x) = x + 1 is not linear (T(0) = 1 ≠ 0)</li>
        <li>T(x, y) = (x + y, xy) is not linear (not homogeneous)</li>
        </ul>
        """
    },
    {
        "title": "Matrix Representation of Linear Transformations",
        "body": """
        <p><strong>Key insight:</strong> Every linear transformation T: ℝⁿ → ℝᵐ can be represented by an m × n matrix A such that T(x) = Ax.</p>

        <p><strong>Finding the matrix representation:</strong> If T: ℝⁿ → ℝᵐ is linear, apply T to each standard basis vector eⱼ and stack the results as columns:</p>
        <pre class='code-block'>A = [T(e₁) | T(e₂) | ... | T(eₙ)]</pre>

        <p>This is a column-stacked matrix where the j-th column is T(eⱼ).</p>

        <p><strong>Matrix representation with respect to general bases:</strong> If T: V → W and B = {v₁, ..., vₙ} is a basis for V, B' = {w₁, ..., wₘ} is a basis for W, then the matrix representation [T]_B'^B is:</p>
        <pre class='code-block'>[T]_B'^B = [[T(v₁)]_{B'} | [T(v₂)]_{B'} | ... | [T(vₙ)]_{B'}]</pre>

        <p>Each column is the coordinate vector of T(vⱼ) with respect to the basis B'.</p>

        <p><strong>Relationship to coordinates:</strong> For v ∈ V with coordinates [v]_B and T(v) ∈ W with coordinates [T(v)]_{B'}:</p>
        <pre class='code-block'>[T(v)]_{B'} = [T]_B'^B [v]_B</pre>

        <div class='example-box'>
        <p><strong>Example: Find matrix representation of T(x, y) = (2x - y, x + y)</strong></p>
        <pre class='code-block'>T(e₁) = T(1, 0) = (2·1 - 0, 1 + 0) = (2, 1)
T(e₂) = T(0, 1) = (2·0 - 1, 0 + 1) = (-1, 1)

A = [2  -1]
    [1   1]

Verify: A[x, y]ᵀ = [2x - y, x + y]ᵀ = T(x, y) ✓</pre>

        <p><strong>Example: Matrix representation with respect to non-standard bases</strong></p>
        <pre class='code-block'>V = ℝ² with basis B = {v₁ = [1, 0], v₂ = [1, 1]}
W = ℝ² with basis B' = {w₁ = [1, 1], w₂ = [0, 1]}
T(x, y) = (2x - y, x + y)

T(v₁) = T(1, 0) = (2, 1). Express in B':
(2, 1) = a(1, 1) + b(0, 1) → a = 2, b = -1. [T(v₁)]_{B'} = [2, -1]ᵀ

T(v₂) = T(1, 1) = (1, 2). Express in B':
(1, 2) = a(1, 1) + b(0, 1) → a = 1, b = 1. [T(v₂)]_{B'} = [1, 1]ᵀ

[T]_B'^B = [2  1]
           [-1 1]</pre>
        </div>

        <p><strong>Change of basis for linear transformations:</strong> If T: V → V is a linear operator and P is the change of basis matrix from B to B', then:</p>
        <pre class='code-block'>[T]_{B'} = P^{-1} [T]_B P</pre>

        <p>This shows how the matrix representation changes when the basis changes (similarity transformation).</p>
        """
    },
    {
        "title": "Kernel, Image, and Rank-Nullity Theorem",
        "body": """
        <p><strong>Kernel (Null Space):</strong> For a linear transformation T: V → W, the kernel is:</p>
        <pre class='code-block'>ker(T) = {v ∈ V : T(v) = 0}</pre>

        <p>The kernel is a subspace of V.</p>

        <p><strong>Image (Range):</strong> The image of T is:</p>
        <pre class='code-block'>im(T) = {w ∈ W : w = T(v) for some v ∈ V}</pre>

        <p>The image is a subspace of W.</p>

        <p><strong>Connection to matrices:</strong> If T(x) = Ax for A an m × n matrix:</p>
        <ul>
        <li>ker(T) = null space of A = {x : Ax = 0}</li>
        <li>im(T) = column space of A = span of columns of A</li>
        <li>rank(T) = dim(im(T)) = rank(A)</li>
        <li>nullity(T) = dim(ker(T)) = nullity(A)</li>
        </ul>

        <p><strong>Rank-Nullity Theorem:</strong> For a linear transformation T: V → W where V is finite-dimensional:</p>
        <pre class='code-block'>rank(T) + nullity(T) = dim(V)</pre>

        <p>This is a fundamental theorem relating the dimensions of the kernel and image.</p>

        <div class='example-box'>
        <p><strong>Example: Find kernel and image of T(x, y) = (x + y, 2x + 2y)</strong></p>
        <pre class='code-block'>Matrix representation: A = [1  1]
                           [2  2]

Kernel: Solve Ax = 0
[1  1][x] = [0]
[2  2][y]   [0]

From row 1: x + y = 0 → x = -y. Free variable y = t.
General solution: x = t[-1, 1]ᵀ
ker(T) = span{[-1, 1]}, dim(ker(T)) = 1 (nullity = 1)

Image: Rank(A) = 1 (one independent column since row 2 = 2·row 1)
im(T) = span{column 1} = span{[1, 2]ᵀ}
dim(im(T)) = 1 (rank = 1)

Check rank-nullity: rank + nullity = 1 + 1 = 2 = dim(ℝ²) ✓</pre>
        </div>

        <p><strong>Injectivity and surjectivity:</strong></p>
        <ul>
        <li><strong>Injective (one-to-one):</strong> T is injective ⟺ ker(T) = {0} ⟺ rank(T) = dim(V)</li>
        <li><strong>Surjective (onto):</strong> T is surjective ⟺ im(T) = W ⟺ rank(T) = dim(W)</li>
        <li><strong>Bijective (isomorphism):</strong> T is bijective ⟺ T is injective and surjective ⟺ rank(T) = dim(V) = dim(W)</li>
        </ul>

        <p><strong>Interpretation:</strong> The rank-nullity theorem says there's a trade-off between kernel and image size. A larger kernel means a smaller image.</p>
        """
    },
    {
        "title": "Eigenvalues, Eigenvectors, and Diagonalization",
        "body": """
        <p><strong>Eigenvector and Eigenvalue:</strong> For a linear operator T: V → V, a nonzero vector v ∈ V is an eigenvector with eigenvalue λ ∈ F if:</p>
        <pre class='code-block'>T(v) = λv</pre>

        <p>For a matrix A, this means: Av = λv, or equivalently, (A - λI)v = 0.</p>

        <p><strong>Finding eigenvalues:</strong> Eigenvalues satisfy the characteristic equation:</p>
        <pre class='code-block'>det(A - λI) = 0</pre>

        <p>This is a polynomial of degree n (for n × n matrices), called the characteristic polynomial.</p>

        <p><strong>Finding eigenvectors:</strong> For each eigenvalue λ, solve (A - λI)v = 0. The eigenvectors are the nonzero solutions (the eigenspace).</p>

        <p><strong>Diagonalization:</strong> A matrix A is diagonalizable if there exists an invertible matrix P such that:</p>
        <pre class='code-block'>A = PDP^{-1}</pre>

        <p>where D is diagonal. The columns of P are eigenvectors, and the diagonal entries of D are eigenvalues.</p>

        <p><strong>When is A diagonalizable?</strong></p>
        <ul>
        <li>If A has n distinct eigenvalues (n × n matrix), then A is diagonalizable</li>
        <li>More generally, A is diagonalizable iff the geometric multiplicity equals the algebraic multiplicity for each eigenvalue</li>
        <li>Symmetric matrices are always diagonalizable (with orthogonal eigenvectors)</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Diagonalize A = [1, 2; 2, 1]</strong></p>
        <pre class='code-block'>Characteristic polynomial: det([1-λ, 2; 2, 1-λ]) = (1-λ)² - 4 = λ² - 2λ - 3 = (λ-3)(λ+1)
Eigenvalues: λ₁ = 3, λ₂ = -1

For λ₁ = 3: (A - 3I)v = 0
[-2  2][v₁] = [0]  → -2v₁ + 2v₂ = 0 → v₁ = v₂
[2  -2][v₂]   [0]

Eigenvector: v₁ = [1, 1]ᵀ (or any scalar multiple)

For λ₂ = -1: (A + I)v = 0
[2  2][v₁] = [0]  → 2v₁ + 2v₂ = 0 → v₁ = -v₂
[2  2][v₂]   [0]

Eigenvector: v₂ = [1, -1]ᵀ

P = [1   1]    D = [3  0]
    [1  -1]        [0 -1]

Verify: A = PDP^{-1} ✓</pre>
        </div>

        <p><strong>Applications of diagonalization:</strong></p>
        <ul>
        <li><strong>Computing powers:</strong> Aⁿ = PDⁿP⁻¹, and Dⁿ is easy (diagonal entries raised to power n)</li>
        <li><strong>Understanding long-term behavior:</strong> For Markov chains and dynamical systems</li>
        <li><strong>Simplifying analysis:</strong> A system is easier to analyze in the eigenvector basis</li>
        </ul>
        """
    },
    {
        "title": "Geometric Interpretation and Applications",
        "body": """
        <p><strong>Linear transformations geometrically:</strong> A linear transformation T: ℝⁿ → ℝᵐ has geometric meaning:</p>

        <ul>
        <li><strong>Scaling:</strong> T(x) = cx shrinks or stretches by factor c</li>
        <li><strong>Rotation:</strong> T(x) = Rθx rotates by angle θ (preserves length and angles)</li>
        <li><strong>Projection:</strong> T(x) = proj_W(x) drops the perpendicular component</li>
        <li><strong>Reflection:</strong> T(x) flips across a line or plane</li>
        <li><strong>Shear:</strong> T(x) shifts one direction relative to another</li>
        </ul>

        <p><strong>Determinant interpretation:</strong> For T(x) = Ax, the determinant det(A) represents the volume scaling factor:</p>
        <ul>
        <li>If det(A) > 0, orientation is preserved</li>
        <li>If det(A) < 0, orientation is reversed</li>
        <li>If det(A) = 0, the transformation collapses to a lower-dimensional subspace</li>
        </ul>

        <p><strong>Rank and geometry:</strong> The rank of T determines the dimension of the image:</p>
        <ul>
        <li>rank(T) = dim(V): T is injective (no two different inputs map to the same output)</li>
        <li>rank(T) = dim(W): T is surjective (every output has a preimage)</li>
        <li>rank(T) < min(dim(V), dim(W)): Information is lost; the image is lower-dimensional</li>
        </ul>

        <p><strong>Applications:</strong></p>
        <ul>
        <li><strong>Computer graphics:</strong> Rotation, scaling, perspective transformations are linear</li>
        <li><strong>Differential equations:</strong> Solution space of linear systems is structured by eigenvectors</li>
        <li><strong>Principal Component Analysis:</strong> Eigenvectors of the covariance matrix identify directions of maximum variance</li>
        <li><strong>Quantum mechanics:</strong> Observables are linear operators (matrices) on Hilbert spaces</li>
        <li><strong>Signal processing:</strong> Fourier transforms and filtering are linear transformations</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Rotation matrix in 2D</strong></p>
        <pre class='code-block'>R = [cos(θ)  -sin(θ)]
    [sin(θ)   cos(θ)]

This matrix rotates vectors counterclockwise by angle θ.
det(R) = cos²(θ) + sin²(θ) = 1 (orientation preserved, no scaling)
Eigenvalues: λ = cos(θ) ± i·sin(θ) = e^{±iθ} (complex, on unit circle)</pre>

        <p><strong>Example: Projection onto a line</strong></p>
        <pre class='code-block'>P = uuᵀ, where u is a unit vector
This projects any vector v onto the direction of u.
The image is 1-dimensional (the line), and the kernel is the orthogonal complement.
rank(P) = 1, nullity(P) = n - 1 (for n-dimensional space)</pre>
        </div>

        <p><strong>Summary:</strong> Linear transformations are among the most important objects in mathematics, bridging abstract algebra with geometry and enabling powerful computational methods across science and engineering.</p>
        """
    }
]
