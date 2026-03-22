SECTIONS = [
    {
        "title": "Singular Value Decomposition: Definition and Derivation",
        "body": """
        <p><strong>Singular Value Decomposition (SVD):</strong> Any m × n matrix A can be factored as:</p>
        <pre class='code-block'>A = UΣVᵀ</pre>

        <p>where:</p>
        <ul>
        <li>U is an m × m orthogonal matrix (left singular vectors)</li>
        <li>Σ is an m × n diagonal matrix with σ₁ ≥ σ₂ ≥ ... ≥ σᵣ > 0 (singular values)</li>
        <li>V is an n × n orthogonal matrix (right singular vectors)</li>
        <li>r = rank(A)</li>
        </ul>

        <p><strong>Key properties:</strong></p>
        <ul>
        <li>The SVD exists for any matrix (unlike eigendecomposition)</li>
        <li>Singular values σᵢ are always non-negative and real</li>
        <li>rank(A) = number of nonzero singular values</li>
        <li>The columns of U form an orthonormal basis for Col(A) (first r columns) and Null(Aᵀ) (last m-r columns)</li>
        <li>The columns of V form an orthonormal basis for Row(A) (first r columns) and Null(A) (last n-r columns)</li>
        </ul>

        <p><strong>Derivation from eigendecomposition:</strong> Consider AᵀA:</p>
        <pre class='code-block'>AᵀA = (UΣVᵀ)ᵀ(UΣVᵀ) = VΣᵀUᵀUΣVᵀ = VΣᵀΣVᵀ</pre>

        <p>Since Σ is m × n and Σᵀ is n × m, ΣᵀΣ is n × n diagonal with entries σ₁², σ₂², ..., σₙ².</p>

        <p>So AᵀA = V(ΣᵀΣ)Vᵀ is the eigendecomposition of AᵀA!</p>

        <p><strong>Computing SVD:</strong></p>
        <ol>
        <li>Compute eigenvalues and eigenvectors of AᵀA: AᵀA = VΛVᵀ</li>
        <li>Singular values: σᵢ = √λᵢ</li>
        <li>Right singular vectors: V (eigenvectors of AᵀA)</li>
        <li>Left singular vectors: uᵢ = (1/σᵢ)Avᵢ</li>
        <li>Form U, Σ, V into the decomposition</li>
        </ol>

        <div class='example-box'>
        <p><strong>Example: SVD of a 2×2 matrix</strong></p>
        <pre class='code-block'>A = [1  0]
    [0  2]

AᵀA = [1  0][1  0] = [1  0]
      [0  2][0  2]   [0  4]

Eigenvalues: λ₁ = 4, λ₂ = 1
Eigenvectors: v₁ = [0, 1], v₂ = [1, 0] (eigenvectors of diagonal matrix)

Singular values: σ₁ = 2, σ₂ = 1

Left singular vectors:
u₁ = (1/σ₁)Av₁ = (1/2)[1  0][0] = (1/2)[0] = [0]
                       [0  2][1]        [2]   [1]

u₂ = (1/σ₂)Av₂ = (1/1)[1  0][1] = [1]
                       [0  2][0]   [0]

U = [0  1]    Σ = [2  0]    V = [0  1]
    [1  0]        [0  1]        [1  0]

Check: UΣVᵀ = [0  1][2  0][0  1] = [0  1][0  2] = [1  0] = A ✓
              [1  0][0  1][1  0]   [1  0][1  0]   [0  2]</pre>
        </div>

        <p><strong>Interpretation:</strong> The SVD reveals the "hidden structure" of a matrix:</p>
        <ul>
        <li>U and V are rotation/reflection matrices (orthogonal)</li>
        <li>Σ contains the "stretching factors" along different directions</li>
        <li>A = (rotation) × (stretching) × (rotation)</li>
        </ul>
        """
    },
    {
        "title": "Geometric Interpretation and Low-Rank Approximation",
        "body": """
        <p><strong>Geometric meaning of SVD:</strong> Any linear transformation A: ℝⁿ → ℝᵐ can be decomposed into three simple operations:</p>

        <ol>
        <li><strong>Vᵀ:</strong> Rotation (or reflection) in ℝⁿ that aligns axes with principal directions</li>
        <li><strong>Σ:</strong> Scaling: stretch/shrink along each axis by σ₁, σ₂, ..., σₙ</li>
        <li><strong>U:</strong> Rotation (or reflection) in ℝᵐ to align with the output space</li>
        </ol>

        <p><strong>Principal axes:</strong> The columns vⱼ of V are the principal axes in the input space. These are the directions where the transformation has maximal effect (σⱼ gives the scaling in that direction).</p>

        <p><strong>Low-rank approximation:</strong> Since σ₁ ≥ σ₂ ≥ ... ≥ σᵣ, the first singular values dominate. Truncating to the largest k values gives:</p>
        <pre class='code-block'>A_k = Σⱼ₌₁ᵏ σⱼ uⱼ vⱼᵀ</pre>

        <p>This is the best rank-k approximation to A (in Frobenius norm):</p>
        <pre class='code-block'>||A - A_k||_F = √(σₖ₊₁² + σₖ₊₂² + ... + σᵣ²)</pre>

        <p><strong>Applications of low-rank approximation:</strong></p>
        <ul>
        <li><strong>Image compression:</strong> Store only first k singular values and vectors (much smaller than full matrix)</li>
        <li><strong>Noise reduction:</strong> Truncate small singular values which often correspond to noise</li>
        <li><strong>Dimensionality reduction:</strong> Project data onto first k principal directions</li>
        <li><strong>Matrix completion:</strong> Infer missing entries from low-rank structure</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Low-rank approximation</strong></p>
        <pre class='code-block'>A = [4  3]    SVD: U = [3/5  4/5]    Σ = [5  0]    V = [4/5  -3/5]
    [3  4]            [4/5 -3/5]        [0  2]        [3/5   4/5]

Storage:
Full matrix A: 4 numbers
Rank-1 approx A₁ = σ₁u₁v₁ᵀ: 1 singular value + 2 components of u₁ + 2 components of v₁ = 5 numbers (not better)
Rank-2 approx A₂ = A: Full reconstruction

For larger matrices, low-rank approximation saves dramatically:
m × n full matrix: mn numbers
Rank-k approximation: k(m + n + 1) numbers</pre>

        <p><strong>Example: Image compression</strong></p>
        <pre class='code-block'>A is a 1000×1000 grayscale image (1 million numbers)
SVD reveals that data is well-approximated by first 50 singular values
Compressed: 50(1000 + 1000 + 1) ≈ 100,050 numbers (10% of original)
Minimal loss if first 50 singular values capture most variance</pre>
        </div>

        <p><strong>Eckart-Young theorem:</strong> Among all rank-k matrices, A_k (truncated SVD) minimizes the distance to A:</p>
        <pre class='code-block'>min_{rank(B)≤k} ||A - B|| = ||A - A_k|| = σₖ₊₁</pre>

        <p>This proves SVD gives the optimal low-rank approximation.</p>
        """
    },
    {
        "title": "Solving Linear Systems and Least Squares with SVD",
        "body": """
        <p><strong>SVD for solving Ax = b:</strong> Using SVD, the least squares solution is:</p>
        <pre class='code-block'>x̂ = VΣ⁺Uᵀb</pre>

        <p>where Σ⁺ is the pseudoinverse of Σ (reciprocals of nonzero singular values):</p>
        <pre class='code-block'>Σ⁺ = [1/σ₁   0   ...]
      [  0   1/σ₂  ...]
      [.........]</pre>

        <p><strong>Moore-Penrose Pseudoinverse:</strong> The pseudoinverse of A is:</p>
        <pre class='code-block'>A⁺ = VΣ⁺Uᵀ</pre>

        <p>This generalizes matrix inversion to non-square and rank-deficient matrices:</p>
        <ul>
        <li>If A is square and invertible: A⁺ = A⁻¹</li>
        <li>If A is tall and full rank: A⁺ = (AᵀA)⁻¹Aᵀ (least squares)</li>
        <li>If A is rank-deficient: A⁺ gives the minimum-norm solution</li>
        </ul>

        <p><strong>Numerical stability:</strong> SVD is numerically stable even for ill-conditioned matrices:</p>
        <ul>
        <li>No need to compute AᵀA (condition number squared)</li>
        <li>Direct work with singular values</li>
        <li>Can detect rank deficiency: singular values near zero indicate linear dependence</li>
        <li>Condition number: κ(A) = σ_max / σ_min (ratio of largest to smallest singular value)</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: Solve Ax = b using SVD</strong></p>
        <pre class='code-block'>A = [1  0]    b = [2]
    [0  2]        [4]
    [0  0]        [0]

SVD: U = [1  0  0]    Σ = [2  0]    V = [1  0]
         [0  1  0]        [0  2]        [0  1]
         [0  0  1]        [0  0]

Pseudoinverse: Σ⁺ = [1/2  0]    (only nonzero singular values)
                    [0  1/2]

A⁺ = VΣ⁺Uᵀ = [1  0][1/2  0][1  0  0]ᵀ = [1  0][1/2  0  0] = [1/2  0   0]
              [0  1][0  1/2][0  1  0]   [0  1][0  1/2 0]   [0   1/2  0]

Least squares solution: x̂ = A⁺b = [1/2  0   0][2] = [1]
                                    [0   1/2  0][4]   [2]
                                               [0]

Verify: Ax̂ = [1  0][1] = [1]  vs  b = [2]
             [0  2][2]   [4]         [4]
             [0  0]      [0]         [0]
(They match exactly since Ax = b is consistent!)</pre>
        </div>

        <p><strong>Rank detection using SVD:</strong> The number of "significant" singular values determines rank. With threshold ε:</p>
        <pre class='code-block'>estimated rank = number of σᵢ > ε · σ_max</pre>

        <p>This is more reliable than checking exact zeros (which become small due to numerical errors).</p>

        <p><strong>Advantages of SVD over other methods:</strong></p>
        <ul>
        <li>Works for rectangular matrices</li>
        <li>Handles rank-deficient cases naturally</li>
        <li>Numerically more stable than normal equations</li>
        <li>Provides rank information directly</li>
        <li>Enables low-rank approximation and compression</li>
        </ul>
        """
    },
    {
        "title": "Applications in Machine Learning and Data Science",
        "body": """
        <p><strong>Principal Component Analysis (PCA) via SVD:</strong> For centered data matrix X (n samples × p variables), the SVD X = UΣVᵀ gives:</p>

        <ul>
        <li><strong>Principal components:</strong> Columns of V (directions of maximum variance)</li>
        <li><strong>Scores:</strong> UΣ (projection of data onto principal components)</li>
        <li><strong>Explained variance:</strong> σᵢ² / Σⱼσⱼ² (proportion of total variance along component i)</li>
        </ul>

        <p>The first k principal components capture the most important structure in the data.</p>

        <p><strong>Latent Semantic Analysis (LSA) for text:</strong> Apply SVD to document-term matrix:</p>
        <ul>
        <li>Columns of U: latent "concepts" in the corpus</li>
        <li>Singular values: strength of each concept</li>
        <li>Columns of V: representation of documents in concept space</li>
        <li>Low-rank approximation: remove noise, group similar documents</li>
        </ul>

        <p><strong>Recommender Systems:</strong> For user-item matrix with missing entries:</p>
        <ul>
        <li>Compute SVD on observed entries (matrix completion)</li>
        <li>Use low-rank approximation to predict missing ratings</li>
        <li>Assumption: ratings are determined by low-rank factors (latent features)</li>
        </ul>

        <p><strong>Image and Face Recognition:</strong> Using eigenfaces (from SVD):</p>
        <ol>
        <li>Stack face images as columns of matrix X</li>
        <li>Compute SVD to find principal modes of variation</li>
        <li>Each face is represented as linear combination of eigenfaces</li>
        <li>Recognition: find closest match in eigenface space</li>
        </ol>

        <p><strong>Denoising and Filtering:</strong> Noisy signal/image = true signal + noise:</p>
        <ul>
        <li>SVD reveals true structure in dominant singular values</li>
        <li>Truncate small singular values (noise)</li>
        <li>Reconstruct from low-rank approximation</li>
        </ul>

        <div class='example-box'>
        <p><strong>Example: PCA on 2D data</strong></p>
        <pre class='code-block'>Data points (centered): [1  2]ᵀ, [2  4]ᵀ, [-1  -2]ᵀ
Data matrix X = [1   2  -1]
                [2   4  -2]

SVD: X = UΣVᵀ
U is 2×2, Σ is 2×2, V is 3×2

Singular values: σ₁ ≈ 4.899 (large), σ₂ ≈ 0.001 (tiny)
Explained variance: σ₁²/(σ₁² + σ₂²) ≈ 99.99%

Principal component 1 (first column of V): direction of maximum variance
All data lies nearly on a line in this direction (1D structure!)</pre>

        <p><strong>Example: Image compression conceptually</strong></p>
        <pre class='code-block'>High-resolution image: 4000×3000 pixels = 12M numbers
SVD reveals: first 100 singular values explain 95% of variance
Compressed representation: 100 singular values + 4000 + 3000 components ≈ 7,100 numbers
Compression ratio: 12M / 7,100 ≈ 1,700× (with 95% of visual information)</pre>
        </div>

        <p><strong>Why SVD is essential in ML:</strong></p>
        <ul>
        <li>Dimensionality reduction: from high-dimensional to low-rank representation</li>
        <li>Feature extraction: principal components are learned features</li>
        <li>Noise filtering: small singular values often correspond to noise</li>
        <li>Regularization: low-rank approximation prevents overfitting</li>
        <li>Interpretability: orthogonal bases make results easier to understand</li>
        </ul>

        <p><strong>Modern applications:</strong> SVD and its variants (randomized SVD, tensor decomposition, nuclear norm minimization) are central to:</p>
        <ul>
        <li>Deep learning: weight matrix analysis and initialization</li>
        <li>Sparse recovery and compressed sensing</li>
        <li>Matrix completion from incomplete observations</li>
        <li>Natural language processing (word embeddings, LSA)</li>
        <li>Computer vision (face recognition, object detection)</li>
        </ul>
        """
    }
]
