TITLE = "Composition and Inverse of Linear Transformations"

SECTIONS = [
    {
        "title": "Composition of Linear Transformations",
        "body": """
        <div class='concept-box'>
        <p><strong>Definition:</strong> If T: U → V and S: V → W are linear transformations, the composition S ∘ T: U → W is defined by:</p>
        <pre class='code-block'>(S ∘ T)(u) = S(T(u))</pre>

        <p><strong>Linearity of composition:</strong> The composition of linear transformations is linear.</p>

        <p><strong>Matrix representation:</strong> If A represents T and B represents S, then BA represents S ∘ T:</p>
        <pre class='code-block'>[S ∘ T] = [S][T]  (matrix multiplication)</pre>

        <p>This is why matrix multiplication is defined the way it is!</p>
        </div>
        """
    },
    {
        "title": "Invertible Linear Transformations",
        "body": """
        <div class='concept-box'>
        <p><strong>Definition:</strong> A linear transformation T: V → W is invertible if there exists a linear transformation T⁻¹: W → V such that:</p>
        <pre class='code-block'>T⁻¹ ∘ T = I_V  and  T ∘ T⁻¹ = I_W</pre>

        <p><strong>Invertibility conditions:</strong> For a linear transformation T: V → W:</p>
        <ul>
        <li>T is invertible ⟺ T is bijective (injective and surjective)</li>
        <li>If V and W have equal finite dimension, then T is invertible ⟺ T is injective ⟺ T is surjective</li>
        <li>For matrices: \(A\) is invertible \(\iff \det(A) \\neq 0 \iff A\) has full rank</li>
        </ul>

        <p><strong>Key result:</strong> If T is invertible, then T⁻¹ is also linear.</p>
        </div>
        """
    },
    {
        "title": "Eigenvalues and Eigenvectors",
        "body": """
        <div class='concept-box'>
        <p><strong>Definition:</strong> For a linear operator T: V → V, a nonzero vector \(v \in V\) is an eigenvector with eigenvalue \(\\lambda \in F\) if:</p>
        <pre class='code-block'>\(T(v) = \\lambda v\)</pre>

        <p>For a matrix \(A\), this means: \(Av = \\lambda v\), or equivalently, \((A - \\lambda I)v = 0\).</p>

        <p><strong>Finding eigenvalues:</strong> Eigenvalues satisfy the characteristic equation:</p>
        <pre class='code-block'>\(\det(A - \\lambda I) = 0\)</pre>

        <p>This is a polynomial of degree \(n\) (for \(n \\times n\) matrices), called the characteristic polynomial.</p>

        <p><strong>Finding eigenvectors:</strong> For each eigenvalue \(\\lambda\), solve \((A - \\lambda I)v = 0\). The nonzero solutions are eigenvectors (forming the eigenspace).</p>
        </div>
        """
    },
    {
        "title": "Diagonalization",
        "body": """
        <div class='concept-box'>
        <p><strong>Definition:</strong> A matrix A is diagonalizable if there exists an invertible matrix P such that:</p>
        <pre class='code-block'>A = PDP⁻¹</pre>

        <p>where D is diagonal. The columns of P are eigenvectors, and the diagonal entries of D are the corresponding eigenvalues.</p>

        <p><strong>When is A diagonalizable?</strong></p>
        <ul>
        <li>If \(A\) has \(n\) distinct eigenvalues (\(n \\times n\) matrix), then \(A\) is diagonalizable</li>
        <li>More generally, \(A\) is diagonalizable iff geometric multiplicity equals algebraic multiplicity for each eigenvalue</li>
        <li>Symmetric matrices are always diagonalizable (with orthogonal eigenvectors)</li>
        </ul>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Diagonalize A = [1, 2; 2, 1]</strong></p>
        <pre class='code-block'>Characteristic polynomial: \(\det([1-\\lambda, 2; 2, 1-\\lambda]) = (1-\\lambda)^2 - 4 = \\lambda^2 - 2\\lambda - 3 = (\\lambda-3)(\\lambda+1)\)
Eigenvalues: \(\\lambda_1 = 3\), \(\\lambda_2 = -1\)

For \(\\lambda_1 = 3\): \((A - 3I)v = 0\)
[-2  2][v₁] = [0]  → -2v₁ + 2v₂ = 0 → v₁ = v₂
[2  -2][v₂]   [0]

Eigenvector: v₁ = [1, 1]ᵀ

For \(\\lambda_2 = -1\): \((A + I)v = 0\)
[2  2][v₁] = [0]  → 2v₁ + 2v₂ = 0 → v₁ = -v₂
[2  2][v₂]   [0]

Eigenvector: v₂ = [1, -1]ᵀ

P = [1   1]    D = [3  0]
    [1  -1]        [0 -1]

Verify: A = PDP⁻¹ ✓</pre>

        <p><strong>Applications of diagonalization:</strong></p>
        <ul>
        <li><strong>Computing powers:</strong> \(A^n = PD^nP^{-1}\), and \(D^n\) is easy (diagonal entries raised to power \(n\))</li>
        <li><strong>Understanding long-term behavior:</strong> For Markov chains and dynamical systems</li>
        <li><strong>Simplifying analysis:</strong> A system is easier to analyze in the eigenvector basis</li>
        </ul>
        </div>
        """
    }
]
