TITLE = "Least Squares"

SECTIONS = [
    {
        "title": "The Least Squares Problem",
        "body": """
        <p><strong>The Problem:</strong> Given an overdetermined system $A\\mathbf{x} = \\mathbf{b}$ with more equations than unknowns (more rows than columns), there is generally no exact solution. We want to find $\\mathbf{x}$ that minimizes the error:</p>

        <div class='concept-box'>
        $$\\min_\\mathbf{x} ||A\\mathbf{x} - \\mathbf{b}||^2$$
        </div>

        <p>This minimizes the sum of squared residuals—hence "least squares."</p>

        <p><strong>Geometric Interpretation:</strong> The column space $\\text{Col}(A)$ is generally a proper subspace of $\\mathbb{R}^m$. The vector $A\\mathbf{x}$ lies in $\\text{Col}(A)$. We want the point in $\\text{Col}(A)$ closest to $\\mathbf{b}$. This is the orthogonal projection of $\\mathbf{b}$ onto $\\text{Col}(A)$:</p>

        <div class='concept-box'>
        $$A\\hat{\\mathbf{x}} = \\text{proj}_{\\text{Col}(A)}(\\mathbf{b})$$
        </div>

        <p><strong>Key Insight:</strong> The residual vector $\\mathbf{r} = \\mathbf{b} - A\\hat{\\mathbf{x}}$ must be orthogonal to the column space of $A$, which means:</p>

        <div class='concept-box'>
        $$A^T \\mathbf{r} = \\mathbf{0} \\quad \\Rightarrow \\quad A^T(\\mathbf{b} - A\\hat{\\mathbf{x}}) = \\mathbf{0}$$
        </div>

        <p>This is the foundation of the normal equations.</p>

        <p><strong>Why Least Squares Matters:</strong> Nearly all real-world data is noisy. Least squares finds the best fit despite the noise, making it fundamental to statistics, machine learning, and science.</p>

        <div class='worked-example'>
        <p><strong>Example:</strong> Fit a line $y = mx + b$ to the points: $(0, 1), (1, 2), (2, 4)$.</p>
        <pre>System (overdetermined):
m(0) + b = 1
m(1) + b = 2
m(2) + b = 4

Matrix form: A = [0  1],  x = [m],  b = [1]
                 [1  1]      [b]      [2]
                 [2  1]                [4]

Note: 3 equations, 2 unknowns → overdetermined
(No exact solution exists because points aren't collinear)</pre>
        </div>
        """
    },
    {
        "title": "Normal Equations and the Least Squares Solution",
        "body": """
        <p><strong>Theorem:</strong> The least squares solution to $A\\mathbf{x} = \\mathbf{b}$ satisfies the normal equations:</p>

        <div class='concept-box'>
        $$A^T A \\hat{\\mathbf{x}} = A^T \\mathbf{b}$$
        </div>

        <p>If $A$ has full column rank (linearly independent columns), then $A^T A$ is invertible, and:</p>

        <div class='concept-box'>
        $$\\hat{\\mathbf{x}} = (A^T A)^{-1} A^T \\mathbf{b}$$
        </div>

        <p>The matrix $(A^T A)^{-1} A^T$ is the pseudoinverse of $A$, often denoted $A^+$.</p>

        <p><strong>Derivation (from First Principles):</strong> To minimize $f(\\mathbf{x}) = ||A\\mathbf{x} - \\mathbf{b}||^2 = (A\\mathbf{x} - \\mathbf{b})^T(A\\mathbf{x} - \\mathbf{b})$, take the gradient and set to zero:</p>

        <pre>\(\nabla f = 2A^T(A\mathbf{x} - \mathbf{b}) = 0\)
\(A^T A \mathbf{x} = A^T \mathbf{b}\)</pre>

        <p><strong>Geometric Check:</strong> The residual $\\mathbf{r} = \\mathbf{b} - A\\hat{\\mathbf{x}}$ satisfies:</p>

        <pre>A^T 𝐫 = A^T(𝐛 - A𝐱̂) = A^T𝐛 - A^T A𝐱̂ = 0</pre>

        <p>This confirms that $\\mathbf{r} \\perp \\text{Col}(A)$.</p>

        <p><strong>Normal Equations Method:</strong></p>
        <ol>
        <li>Form $A^T A$ and $A^T \\mathbf{b}$</li>
        <li>Solve the $n \\times n$ system $A^T A \\hat{\\mathbf{x}} = A^T \\mathbf{b}$</li>
        <li>(Optional) Compute residual $\\mathbf{r} = \\mathbf{b} - A\\hat{\\mathbf{x}}$</li>
        </ol>

        <div class='worked-example'>
        <p><strong>Example (continued):</strong> Solve the line-fitting problem using normal equations.</p>
        <pre>A = [0  1],  b = [1]
    [1  1]      [2]
    [2  1]      [4]

A^T A = [0  1  2][0  1] = [5  3]
        [1  1  1][1  1]   [3  3]
                 [2  1]

A^T b = [0  1  2][1] = [10]
        [1  1  1][2]   [7]
                 [4]

Solve: [5  3][m] = [10]
       [3  3][b]   [7]

From 5m + 3b = 10 and 3m + 3b = 7:
Subtract: 2m = 3, so m = 1.5
Then: 3(1.5) + 3b = 7 ⟹ b = 5/6

Best fit line: y ≈ 1.5x + 5/6</pre>
        </div>

        <div class='warning-box'>
        <p><strong>Numerical Caveat:</strong> Computing $(A^T A)^{-1}$ directly can be numerically unstable if $A^T A$ is ill-conditioned. Use QR decomposition instead for better numerical stability (see next section).</p>
        </div>
        """
    },
    {
        "title": "QR-Based Least Squares and Applications",
        "body": """
        <p><strong>QR Method (More Stable):</strong> If $A = QR$ with $Q$ orthonormal, then:</p>

        <div class='concept-box'>
        $$A\\hat{\\mathbf{x}} = \\mathbf{b} \\quad \\Rightarrow \\quad QR\\hat{\\mathbf{x}} = \\mathbf{b} \\quad \\Rightarrow \\quad R\\hat{\\mathbf{x}} = Q^T \\mathbf{b}$$
        </div>

        <p>Since $R$ is upper triangular, this is solved efficiently by back-substitution. Moreover, orthogonal transformations don't amplify rounding errors, making this much more numerically stable.</p>

        <p><strong>QR Least Squares Algorithm:</strong></p>
        <ol>
        <li>Compute QR decomposition of $A$: $A = QR$</li>
        <li>Compute $\\mathbf{c} = Q^T \\mathbf{b}$</li>
        <li>Solve $R\\hat{\\mathbf{x}} = \\mathbf{c}$ by back-substitution</li>
        </ol>

        <p><strong>When to Use Each Method:</strong></p>
        <ul>
        <li><strong>Normal equations:</strong> Small problems, pen-and-paper calculations, understanding the theory</li>
        <li><strong>QR decomposition:</strong> Production code, large problems, numerical stability is critical</li>
        <li><strong>SVD:</strong> When you need rank detection, pseudoinverses, or very ill-conditioned systems</li>
        </ul>

        <p><strong>Applications of Least Squares:</strong></p>
        <ul>
        <li><strong>Linear regression:</strong> Fit a line/hyperplane to data</li>
        <li><strong>Polynomial fitting:</strong> Find the best polynomial approximating a function</li>
        <li><strong>Machine learning:</strong> Linear models, neural network training (gradient descent minimizes least squares)</li>
        <li><strong>Signal processing:</strong> Filter design, denoising, spectrum estimation</li>
        <li><strong>Image processing:</strong> Image reconstruction, blur removal</li>
        <li><strong>Scientific computing:</strong> Parameter estimation from experimental data</li>
        </ul>

        <p><strong>Statistical Interpretation:</strong> Under Gaussian noise assumptions, the least squares estimator is the maximum likelihood estimate. This connects optimization to statistics.</p>

        <div class='success-box'>
        <p><strong>Takeaway:</strong> Least squares is one of the most powerful tools in applied mathematics. It elegantly combines linear algebra (projections, QR), optimization, and statistics into a unified framework.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example (PCA Data Projection):</strong> Project high-dimensional data onto a lower-dimensional subspace.</p>
        <pre>Given: Data matrix X (1000 × 100) [1000 observations, 100 features]
Goal: Reduce to 10 features while preserving variance

Solution:
1. Compute covariance Σ = (1/n) X^T X
2. Find top 10 eigenvectors {u₁, ..., u₁₀} (principal components)
3. Project: X_reduced = X [u₁ ... u₁₀]  (1000 × 10)

Geometrically, this is projecting onto the 10-dimensional subspace spanned by
the principal components—a least squares problem in disguise!</pre>
        </div>
        """
    }
]
