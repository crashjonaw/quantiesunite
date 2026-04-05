TITLE = "Applications: PCA, Pseudoinverse, and Beyond"

SECTIONS = [
    {
        "title": "Pseudoinverse and Solving Linear Systems",
        "body": """
        <p><strong>Moore-Penrose Pseudoinverse:</strong> SVD provides a natural way to generalize matrix inversion to rectangular matrices:</p>
        <p>$$A^+ = V\\Sigma^+ U^T$$</p>

        <p>where $\\Sigma^+$ is the pseudoinverse of $\\Sigma$ (reciprocals of nonzero singular values):</p>
        <p>$\\Sigma^+$ has entries $1/\\sigma_i$ for $\\sigma_i > 0$ and $0$ for $\\sigma_i = 0$.</p>

        <p><strong>Why pseudoinverse matters:</strong> $A^+$ solves $A\\mathbf{x} = \\mathbf{b}$ optimally in multiple scenarios:</p>
        <ul>
        <li><strong>Full rank, square:</strong> $A^+ = A^{-1}$ (true inverse)</li>
        <li><strong>Tall, full rank:</strong> $A^+ = (A^T A)^{-1} A^T$ (least squares solution)</li>
        <li><strong>Rank-deficient:</strong> $A^+$ gives the minimum-norm solution among all solutions</li>
        <li><strong>Wide, full rank:</strong> $A^+ = A^T (AA^T)^{-1}$ (minimum-norm solution)</li>
        </ul>

        <p><strong>Least squares solution:</strong> The least squares solution to $A\\mathbf{x} = \\mathbf{b}$ is:</p>
        <p>$$\\hat{\\mathbf{x}} = A^+ \\mathbf{b} = V\\Sigma^+ U^T \\mathbf{b}$$</p>

        <p>This works even when $\\mathbf{b}$ is not in $\\text{Col}(A)$.</p>

        <div class='worked-example'>
        <p><strong>Example: Solve overdetermined system using SVD</strong></p>
        <pre class='code-block'>$A\\mathbf{x} = \\mathbf{b}$ where $A$ is $3 \\times 2$, $\\mathbf{x}$ is $2 \\times 1$, $\\mathbf{b}$ is $3 \\times 1$

$$A = \\begin{bmatrix} 1 & 0 \\\\ 0 & 2 \\\\ 0 & 0 \\end{bmatrix} \\quad \\mathbf{b} = \\begin{bmatrix} 2 \\\\ 4 \\\\ 0 \\end{bmatrix}$$

This is overdetermined (3 equations, 2 unknowns).

SVD: $A = U\\Sigma V^T$ where
$$U = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{bmatrix} \\quad \\Sigma = \\begin{bmatrix} 1 & 0 \\\\ 0 & 2 \\\\ 0 & 0 \\end{bmatrix} \\quad V = \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix}$$

Pseudoinverse: $$A^+ = V\\Sigma^+ U^T = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1/2 & 0 \\end{bmatrix}$$

Least squares solution: $$\\hat{\\mathbf{x}} = A^+ \\mathbf{b} = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1/2 & 0 \\end{bmatrix} \\begin{bmatrix} 2 \\\\ 4 \\\\ 0 \\end{bmatrix} = \\begin{bmatrix} 2 \\\\ 2 \\end{bmatrix}$$

Check: $A\\hat{\\mathbf{x}} = \\begin{bmatrix} 2 \\\\ 4 \\\\ 0 \\end{bmatrix}$ (matches $\\mathbf{b}$ exactly!)</pre>
        </div>

        <p><strong>Numerical stability:</strong> SVD is far superior to normal equations $(A^T A)^{-1} A^T \\mathbf{b}$ for least squares because:</p>
        <ul>
        <li>SVD works directly with $A$</li>
        <li>$A^T A$ has condition number $\\kappa(A^T A) = \\kappa(A)^2$, squaring ill-conditioning</li>
        <li>SVD can detect rank deficiency (singular values near zero)</li>
        <li>SVD directly gives condition number $\\kappa(A) = \\sigma_{\\max} / \\sigma_{\\min}$</li>
        </ul>

        <div class='warning-box'>
        <p><strong>Never use normal equations:</strong> For numerically stable least squares, use SVD (or QR) instead of forming $(A^T A)^{-1} A^T$. The latter loses information through rounding and amplifies conditioning problems.</p>
        </div>
        """
    },
    {
        "title": "Principal Component Analysis (PCA)",
        "body": """
        <p><strong>PCA via SVD:</strong> For a data matrix $X$ ($n$ samples $\\times$ $p$ variables, centered), the SVD $X = U\\Sigma V^T$ directly gives PCA:</p>

        <ul>
        <li><strong>Principal components:</strong> Columns of $V$ (directions of maximum variance)</li>
        <li><strong>Scores:</strong> $U\\Sigma$ (projection of data onto principal components)</li>
        <li><strong>Explained variance:</strong> $\\sigma_i^2 / (\\sum_j \\sigma_j^2)$ = fraction of total variance along component $i$</li>
        <li><strong>Singular value = $\\sqrt{\\text{variance} \\times n}$</strong> for centered data</li>
        </ul>

        <p><strong>Dimensionality reduction in PCA:</strong> Keep first $k$ principal components (largest singular values). Project $n$-sample $\\times$ $p$-variable data onto $k$-dimensional space while retaining maximum variance.</p>

        <div class='concept-box'>
        <p><strong>Why SVD is ideal for PCA:</strong></p>
        <ul>
        <li>Directly gives eigenvectors of covariance matrix</li>
        <li>Numerically stable (no need to compute $XX^T$ or $X^T X$)</li>
        <li>Reveals explained variance through singular value magnitudes</li>
        <li>Automatically orders components by importance</li>
        </ul>
        </div>

        <div class='worked-example'>
        <p><strong>Example: PCA on 2D data</strong></p>
        <pre class='code-block'>Data points (centered): $[1, 2]^T$, $[2, 4]^T$, $[-1, -2]^T$

Data matrix $$X = \\begin{bmatrix} 1 & 2 & -1 \\\\ 2 & 4 & -2 \\end{bmatrix}$$

SVD: $X = U\\Sigma V^T$ where $U$ is $2 \\times 2$, $\\Sigma$ is $2 \\times 2$, $V$ is $3 \\times 2$

Singular values: $\\sigma_1 \\approx 4.899$, $\\sigma_2 \\approx 0.0002$

Explained variance:
$\\sigma_1^2 / (\\sigma_1^2 + \\sigma_2^2) \\approx 4.899^2 / (4.899^2 + 0.0002^2) \\approx 99.998\\%$

First principal component ($V[:, 0]$): $[0.447, 0.894]^T \\approx [1/\\sqrt{5}, 2/\\sqrt{5}]^T$
(direction of maximum variance)

All data lies nearly on a line in this direction (1D structure!)
Scores ($U\\Sigma$): projection of data onto principal components
Principal components reveal true underlying structure.</pre>
        </div>
        """
    },
    {
        "title": "Other Applications",
        "body": """
        <p><strong>Latent Semantic Analysis (LSA) for text:</strong> Apply SVD to document-term matrix:</p>
        <ul>
        <li>Columns of $U$: latent "semantic concepts" in the corpus</li>
        <li>Singular values: strength/importance of each concept</li>
        <li>Columns of $V$: representation of documents in concept space</li>
        <li>Low-rank approximation: remove noise, group similar documents, improve search</li>
        </ul>

        <p><strong>Recommender Systems:</strong> For user-item matrix with missing entries:</p>
        <ul>
        <li>Assume ratings follow low-rank structure (latent factors)</li>
        <li>Compute SVD on observed entries</li>
        <li>Use low-rank approximation to predict missing ratings</li>
        <li>Discovers latent preferences and item properties</li>
        </ul>

        <p><strong>Image and Face Recognition (Eigenfaces):</strong></p>
        <ol>
        <li>Stack face images as columns of matrix $X$</li>
        <li>Compute SVD to find principal modes of facial variation</li>
        <li>Each face = linear combination of eigenfaces (columns of $U$/$V$)</li>
        <li>Recognition: find closest match in eigenface space</li>
        </ol>

        <p><strong>Signal Denoising and Filtering:</strong> Noisy signal = true signal + noise:</p>
        <ul>
        <li>SVD reveals true structure in dominant singular values</li>
        <li>Small singular values = noise (high-frequency variations)</li>
        <li>Truncate small $\\sigma$ to remove noise</li>
        <li>Reconstruct from low-rank approximation = denoised signal</li>
        </ul>

        <div class='success-box'>
        <p><strong>Why SVD is essential in machine learning:</strong></p>
        <ul>
        <li><strong>Dimensionality reduction:</strong> High-dimensional to low-rank representation</li>
        <li><strong>Feature extraction:</strong> Principal components are interpretable learned features</li>
        <li><strong>Noise filtering:</strong> Small singular values often correspond to noise</li>
        <li><strong>Regularization:</strong> Low-rank approximation prevents overfitting</li>
        <li><strong>Interpretability:</strong> Orthogonal bases make results easier to understand</li>
        </ul>
        </div>

        <p><strong>Modern extensions:</strong> SVD and variants are central to cutting-edge applications:</p>
        <ul>
        <li>Randomized SVD: fast approximation for huge matrices</li>
        <li>Tensor decomposition: SVD generalized to 3+ dimensions</li>
        <li>Nuclear norm minimization: low-rank matrix completion</li>
        <li>Deep learning: weight matrix analysis, network initialization</li>
        <li>Sparse recovery: compressed sensing and signal reconstruction</li>
        <li>Natural language: word embeddings, document analysis</li>
        <li>Computer vision: face recognition, object detection</li>
        </ul>
        """
    }
]
