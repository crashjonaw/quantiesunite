SECTIONS = [
    {
        "title": "Dot Product, Orthogonality, and Norms",
        "body": """
        <p><strong>Dot Product (Inner Product):</strong> For vectors u, v ∈ ℝⁿ, the dot product is:</p>
        <pre class='code-block'>u · v = u₁v₁ + u₂v₂ + ... + uₙvₙ = uᵀv</pre>

        <p><strong>Properties of the dot product:</strong></p>
        <ul>
        <li><strong>Commutative:</strong> u · v = v · u</li>
        <li><strong>Distributive:</strong> u · (v + w) = u · v + u · w</li>
        <li><strong>Scalar multiplication:</strong> (cu) · v = c(u · v)</li>
        <li><strong>Self dot product:</strong> v · v = ||v||²≥ 0 (equals 0 iff v = 0)</li>
        </ul>

        <p><strong>Norm (Length):</strong> The Euclidean norm of v is:</p>
        <pre class='code-block'>||v|| = √(v · v) = √(v₁² + v₂² + ... + vₙ²)</pre>

        <p><strong>Orthogonality:</strong> Two vectors u and v are orthogonal (perpendicular) if:</p>
        <pre class='code-block'>u · v = 0</pre>

        <p><strong>Unit Vector:</strong> A vector u is a unit vector if ||u|| = 1. Normalize any nonzero vector by dividing by its norm:</p>
        <pre class='code-block'>û = u / ||u||</pre>

        <p><strong>Angle between vectors:</strong> The angle θ between nonzero u and v satisfies:</p>
        <pre class='code-block'>cos(θ) = (u · v) / (||u|| · ||v||)</pre>

        <p><strong>Cauchy-Schwarz Inequality:</strong> For any vectors u, v:</p>
        <pre class='code-block'>|u · v| ≤ ||u|| · ||v||</pre>

        <p>Equality holds iff u and v are parallel (scalar multiples).</p>

        <div class='example-box'>
        <p><strong>Example: Orthogonality and norms</strong></p>
        <pre class='code-block'>u = [1, 2], v = [2, -1]
u · v = 1·2 + 2·(-1) = 0
Since u · v = 0, u and v are orthogonal.

||u|| = √(1² + 2²) = √5
||v|| = √(2² + (-1)²) = √5

û = [1/√5, 2/√5] is the unit vector in direction of u.
v̂ = [2/√5, -1/√5] is the unit vector in direction of v.</pre>
        </div>

        <p><strong>Distance between vectors:</strong> The Euclidean distance is:</p>
        <pre class='code-block'>d(u, v) = ||u - v|| = √((u₁-v₁)² + ... + (uₙ-vₙ)²)</pre>

        <p>This makes ℝⁿ a metric space and connects linear algebra to geometry and analysis.</p>
        """
    },
    {
        "title": "Orthogonal and Orthonormal Sets",
        "body": """
        <p><strong>Orthogonal Set:</strong> A set of vectors {v₁, v₂, ..., vₖ} is orthogonal if vᵢ · vⱼ = 0 for all i ≠ j.</p>

        <p><strong>Orthonormal Set:</strong> A set is orthonormal if:</p>
        <ul>
        <li>It is orthogonal</li>
        <li>Each vector is a unit vector: ||vᵢ|| = 1</li>
        </ul>

        <p>Equivalently: vᵢ · vⱼ = δᵢⱼ (Kronecker delta: 1 if i = j, 0 otherwise).</p>

        <p><strong>Orthonormal basis:</strong> An orthonormal set that spans the space. If {u₁, u₂, ..., uₙ} is an orthonormal basis, any vector v can be written as:</p>
        <pre class='code-block'>v = (v · u₁)u₁ + (v · u₂)u₂ + ... + (v · uₙ)uₙ</pre>

        <p>The coordinates are simply the dot products! This makes computations very efficient.</p>

        <p><strong>Orthogonal Matrix:</strong> A square matrix Q is orthogonal if QᵀQ = I (equivalently, Q⁻¹ = Qᵀ). The columns (and rows) of Q form an orthonormal set.</p>

        <p><strong>Properties of orthogonal matrices:</strong></p>
        <ul>
        <li>||Qv|| = ||v|| for all v (preserves lengths)</li>
        <li>(Qu) · (Qv) = u · v (preserves angles)</li>
        <li>det(Q) = ±1</li>
        <li>Q⁻¹ = Qᵀ (very easy to invert!)</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Orthonormal set in ℝ³</strong></p>
        <pre class='code-block'>u₁ = [1, 0, 0], u₂ = [0, 1, 0], u₃ = [0, 0, 1]

Check orthonormality:
u₁ · u₂ = 0, u₁ · u₃ = 0, u₂ · u₃ = 0 (orthogonal)
||u₁|| = ||u₂|| = ||u₃|| = 1 (unit vectors)

This is the standard basis—always orthonormal!

For v = [2, 3, 5]:
v = (v · u₁)u₁ + (v · u₂)u₂ + (v · u₃)u₃ = 2u₁ + 3u₂ + 5u₃

Coordinates with respect to the orthonormal basis are just the components!</pre>

        <p><strong>Example: Orthogonal matrix (rotation)</strong></p>
        <pre class='code-block'>Q = [cos(θ)  -sin(θ)]
    [sin(θ)   cos(θ)]

Columns: u₁ = [cos(θ), sin(θ)], u₂ = [-sin(θ), cos(θ)]
u₁ · u₂ = -cos(θ)sin(θ) + sin(θ)cos(θ) = 0 ✓
||u₁|| = √(cos²(θ) + sin²(θ)) = 1 ✓
||u₂|| = √(sin²(θ) + cos²(θ)) = 1 ✓

Q is orthogonal. QᵀQ = I and Q⁻¹ = Qᵀ.</pre>
        </div>

        <p><strong>Advantages of orthonormal bases:</strong></p>
        <ul>
        <li>Easy coordinate computation (just dot products)</li>
        <li>Numerically stable in algorithms</li>
        <li>Geometric intuition (unit length, perpendicular)</li>
        <li>Many matrices (rotation, reflection) are orthogonal</li>
        </ul>
        """
    },
    {
        "title": "Gram-Schmidt Process and QR Decomposition",
        "body": """
        <p><strong>Gram-Schmidt Orthogonalization:</strong> Given a linearly independent set {v₁, v₂, ..., vₙ}, produce an orthogonal set {w₁, w₂, ..., wₙ} by:</p>

        <pre class='code-block'>w₁ = v₁
w₂ = v₂ - (v₂·w₁/||w₁||²)w₁  (subtract projection of v₂ onto w₁)
w₃ = v₃ - (v₃·w₁/||w₁||²)w₁ - (v₃·w₂/||w₂||²)w₂  (subtract projections)
...
wₖ = vₖ - Σⱼ₌₁^{k-1} (vₖ·wⱼ/||wⱼ||²)wⱼ</pre>

        <p>Normalize to get orthonormal: uₖ = wₖ / ||wₖ||</p>

        <p><strong>Algorithm (Gram-Schmidt):</strong></p>
        <pre class='code-block'>for k = 1 to n:
    wₖ = vₖ
    for j = 1 to k-1:
        wₖ = wₖ - (vₖ · uⱼ)uⱼ  (subtract projection onto u_j)
    uₖ = wₖ / ||wₖ||  (normalize)</pre>

        <p><strong>QR Decomposition:</strong> Any m × n matrix A with linearly independent columns can be factored as:</p>
        <pre class='code-block'>A = QR</pre>

        <p>where Q is m × n with orthonormal columns, and R is n × n upper triangular.</p>

        <p><strong>Connection to Gram-Schmidt:</strong> Gram-Schmidt on the columns of A produces Q, and R captures the coefficients in the orthogonalization process.</p>

        <p><strong>Computing QR:</strong></p>
        <pre class='code-block'>1. Apply Gram-Schmidt to columns of A
2. The orthonormal vectors form the columns of Q
3. R_ij = (column i of A) · (column j of Q)  for i ≤ j
   R_ij = 0  for i > j (upper triangular)</pre>

        <div class='example-box'>
        <p><strong>Example: Gram-Schmidt in ℝ³</strong></p>
        <pre class='code-block'>v₁ = [1, 0, 0], v₂ = [1, 1, 0]

w₁ = [1, 0, 0]
u₁ = w₁ / ||w₁|| = [1, 0, 0] (already unit)

w₂ = v₂ - (v₂ · u₁)u₁ = [1, 1, 0] - (1)[1, 0, 0] = [0, 1, 0]
u₂ = w₂ / ||w₂|| = [0, 1, 0] (already unit)

Orthonormal set: {u₁ = [1, 0, 0], u₂ = [0, 1, 0]}</pre>

        <p><strong>Example: QR decomposition</strong></p>
        <pre class='code-block'>A = [1  1]
    [0  1]
    [0  0]

Columns: v₁ = [1, 0, 0], v₂ = [1, 1, 0]
From Gram-Schmidt: u₁ = [1, 0, 0], u₂ = [0, 1, 0]

Q = [1  0]
    [0  1]
    [0  0]

R = [1  1]
    [0  1]

Verify: QR = [1  0][1  1] = [1  1] = A ✓
            [0  1][0  1]   [0  1]
            [0  0]         [0  0]</pre>
        </div>

        <p><strong>Why QR is important:</strong></p>
        <ul>
        <li>Solves least squares efficiently and numerically stably</li>
        <li>Eigenvalue algorithms (QR iteration) use QR decomposition</li>
        <li>Used in many numerical linear algebra routines</li>
        </ul>
        """
    },
    {
        "title": "Orthogonal Projection and Least Squares",
        "body": """
        <p><strong>Orthogonal Projection:</strong> The orthogonal projection of a vector v onto a nonzero vector u is:</p>
        <pre class='code-block'>proj_u(v) = (v · u / ||u||²) u</pre>

        <p>This is the "shadow" of v on the direction of u.</p>

        <p><strong>Projection onto a subspace:</strong> If W is a subspace with orthonormal basis {u₁, u₂, ..., uₖ}, the orthogonal projection of v onto W is:</p>
        <pre class='code-block'>proj_W(v) = (v · u₁)u₁ + (v · u₂)u₂ + ... + (v · uₖ)uₖ</pre>

        <p>The perpendicular component is v - proj_W(v), which is orthogonal to W.</p>

        <p><strong>Least Squares Problem:</strong> Given an overdetermined system Ax = b (more equations than unknowns, generally no exact solution), find x that minimizes:</p>
        <pre class='code-block'>||Ax - b||²  (sum of squared errors)</pre>

        <p><strong>Normal Equations:</strong> The least squares solution minimizes ||Ax - b||² and satisfies:</p>
        <pre class='code-block'>Aᵀ Ax = Aᵀb</pre>

        <p>If A has full column rank, the unique solution is:</p>
        <pre class='code-block'>x̂ = (AᵀA)⁻¹Aᵀb</pre>

        <p><strong>Geometric interpretation:</strong> The least squares solution projects b onto the column space of A:</p>
        <pre class='code-block'>Ax̂ = proj_{Col(A)}(b)</pre>

        <p>The residual r = b - Ax̂ is orthogonal to the column space of A, i.e., Aᵀr = 0.</p>

        <p><strong>Using QR for least squares:</strong> If A = QR (QR decomposition), then:</p>
        <pre class='code-block'>x̂ = R⁻¹Qᵀb</pre>

        <p>This is more numerically stable than computing (AᵀA)⁻¹Aᵀb.</p>

        <div class='example-box'>
        <p><strong>Example: Least squares fit</strong></p>
        <pre class='code-block'>Fit a line y = mx + b to points: (0, 1), (1, 2), (2, 4)

System: m(0) + b = 1
        m(1) + b = 2
        m(2) + b = 4

Matrix form: [0  1][m]   [1]
             [1  1][b] = [2]
             [2  1]      [4]

A = [0  1], b = [1]
    [1  1]      [2]
    [2  1]      [4]

Normal equations: AᵀAx = Aᵀb
AᵀA = [5  3], Aᵀb = [10]
      [3  3]        [7]

Solve: [5  3][m]   [10]
       [3  3][b] = [7]

From 5m + 3b = 10 and 3m + 3b = 7:
Subtracting: 2m = 3, so m = 1.5
Then: 3(1.5) + 3b = 7, so 4.5 + 3b = 7, thus b = 0.833...

Best fit line: y ≈ 1.5x + 0.833</pre>
        </div>

        <p><strong>Applications of least squares:</strong></p>
        <ul>
        <li><strong>Linear regression:</strong> Fit a line/plane to data points</li>
        <li><strong>Polynomial fitting:</strong> Find best approximating polynomial</li>
        <li><strong>Data fitting:</strong> Determine parameters in models from noisy observations</li>
        <li><strong>Signal processing:</strong> Filter and denoise signals</li>
        </ul>
        """
    },
    {
        "title": "Applications in Statistics and Data Analysis",
        "body": """
        <p><strong>Covariance matrix:</strong> For data with mean 0, the covariance matrix is:</p>
        <pre class='code-block'>Σ = (1/n) XᵀX</pre>

        <p>where X is the data matrix (rows = observations, columns = variables). The covariance matrix is symmetric and positive semi-definite.</p>

        <p><strong>Principal Component Analysis (PCA):</strong> To reduce dimensionality while preserving variance:</p>
        <ol>
        <li>Compute covariance matrix Σ</li>
        <li>Find eigenvalues and eigenvectors of Σ</li>
        <li>The eigenvectors are principal components (directions of maximum variance)</li>
        <li>Project data onto top k eigenvectors</li>
        </ol>

        <p>The eigenvectors form an orthonormal basis, making the transformation efficient and interpretable.</p>

        <p><strong>Normal equations in statistics:</strong> For linear regression y = Xβ + ε, the least squares estimate is:</p>
        <pre class='code-block'>β̂ = (XᵀX)⁻¹Xᵀy</pre>

        <p>This is the maximum likelihood estimator under Gaussian noise assumptions.</p>

        <p><strong>Ridge Regression:</strong> To handle ill-conditioning in (XᵀX), add regularization:</p>
        <pre class='code-block'>β̂_λ = (XᵀX + λI)⁻¹Xᵀy</pre>

        <p>The parameter λ > 0 balances goodness of fit and magnitude of coefficients.</p>

        <div class='example-box'>
        <p><strong>Example: Simple PCA</strong></p>
        <pre class='code-block'>Data matrix X (2 observations × 2 variables):
X = [1  2]
    [3  4]

Covariance Σ = (1/2)XᵀX = (1/2)[10  14] = [5   7]
                           [14  20]   [7  10]

Eigenvalues: det(Σ - λI) = (5-λ)(10-λ) - 49 = λ² - 15λ + 1
λ ≈ 14.93, 0.07 (one large, one small)

The first eigenvector (high variance) captures the main trend.
Projecting onto this eigenvector reduces to 1D while preserving most variance.</pre>
        </div>

        <p><strong>Orthogonal transformation benefits in statistics:</strong></p>
        <ul>
        <li>Eigenvector basis decorrelates variables (makes them independent)</li>
        <li>Variance along principal components is easy to interpret</li>
        <li>Low-rank approximation via SVD (singular value decomposition)</li>
        <li>Numerical stability through orthogonal transformations</li>
        </ul>

        <p><strong>Summary:</strong> Orthogonality and least squares are fundamental to modern statistics, machine learning, and applied mathematics. They provide elegant solutions to data fitting problems and interpretable transformations.</p>
        """
    }
]
