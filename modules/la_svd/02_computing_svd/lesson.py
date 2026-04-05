TITLE = "Computing the SVD"

SECTIONS = [
    {
        "title": "Derivation from Eigendecomposition",
        "body": """
        <p><strong>Connection to $A^T A$:</strong> The key insight is that SVD relates to the eigendecomposition of $A^T A$. Consider:</p>
        <p>$$A^T A = (U\\Sigma V^T)^T (U\\Sigma V^T) = V\\Sigma^T U^T U\\Sigma V^T = V\\Sigma^T \\Sigma V^T$$</p>

        <p>Since $\\Sigma$ is $m \\times n$ and $\\Sigma^T$ is $n \\times m$, the product $\\Sigma^T \\Sigma$ is $n \\times n$ diagonal with entries $\\sigma_1^2, \\sigma_2^2, \\ldots, \\sigma_n^2$.</p>

        <p><strong>Therefore:</strong> $A^T A = V(\\Sigma^T \\Sigma)V^T$ is the eigendecomposition of $A^T A$!</p>

        <div class='concept-box'>
        <p><strong>The key relationship:</strong></p>
        <ul>
        <li>Columns of $V$ are eigenvectors of $A^T A$</li>
        <li>Singular values $\\sigma_i$ satisfy $\\sigma_i^2 = $ eigenvalues of $A^T A$</li>
        <li>So $\\sigma_i = \\sqrt{\\lambda_i}$ where $\\lambda_i$ are the eigenvalues of $A^T A$</li>
        </ul>
        </div>

        <p>This connection allows us to compute SVD using well-understood eigendecomposition algorithms.</p>
        """
    },
    {
        "title": "Step-by-Step Computation Algorithm",
        "body": """
        <p><strong>Algorithm for computing SVD of $A$ ($m \\times n$):</strong></p>

        <ol>
        <li><strong>Form $A^T A$:</strong> Compute the $n \\times n$ matrix $A^T A$</li>
        <li><strong>Find eigendecomposition:</strong> Compute eigenvalues $\\lambda_1 \\geq \\lambda_2 \\geq \\cdots \\geq \\lambda_n$ and eigenvectors $\\mathbf{v}_1, \\mathbf{v}_2, \\ldots, \\mathbf{v}_n$ of $A^T A$. Call this $A^T A = V\\Lambda V^T$</li>
        <li><strong>Singular values:</strong> $\\sigma_i = \\sqrt{\\lambda_i}$. If $\\lambda_i < 0$ (shouldn't happen for $A^T A$ which is positive semidefinite), set $\\sigma_i = 0$</li>
        <li><strong>Right singular vectors:</strong> $V = [\\mathbf{v}_1 \\mid \\mathbf{v}_2 \\mid \\cdots \\mid \\mathbf{v}_n]$ (columns are eigenvectors, already orthonormal)</li>
        <li><strong>Compute left singular vectors:</strong> For each $i$ where $\\sigma_i \\neq 0$: $\\mathbf{u}_i = \\frac{1}{\\sigma_i} A\\mathbf{v}_i$</li>
        <li><strong>Extend $U$ if needed:</strong> If $\\text{rank}(A) < m$, add orthonormal vectors to complete $U$ to $m \\times m$</li>
        <li><strong>Form $\\Sigma$:</strong> Create $m \\times n$ diagonal matrix with $\\sigma_1, \\sigma_2, \\ldots, \\sigma_r$ on diagonal ($r = \\text{rank}$)</li>
        </ol>

        <div class='worked-example'>
        <p><strong>Example: Compute SVD step-by-step</strong></p>
        <pre class='code-block'>$$A = \\begin{bmatrix} 4 & 3 \\\\ 3 & 4 \\end{bmatrix}$$

Step 1: $A^T A = \\begin{bmatrix} 4 & 3 \\\\ 3 & 4 \\end{bmatrix} \\begin{bmatrix} 4 & 3 \\\\ 3 & 4 \\end{bmatrix} = \\begin{bmatrix} 25 & 24 \\\\ 24 & 25 \\end{bmatrix}$

Step 2: Find eigenvalues and eigenvectors:
$\\det(A^T A - \\lambda I) = (25 - \\lambda)^2 - 24^2 = \\lambda^2 - 50\\lambda + 49$
$\\lambda_1 = 49$, $\\lambda_2 = 1$
$\\mathbf{v}_1 = [1/\\sqrt{2},\\; 1/\\sqrt{2}]^T$ (eigenvector for $\\lambda_1 = 49$)
$\\mathbf{v}_2 = [1/\\sqrt{2},\\; -1/\\sqrt{2}]^T$ (eigenvector for $\\lambda_2 = 1$)

Step 3: $\\sigma_1 = \\sqrt{49} = 7$, $\\sigma_2 = \\sqrt{1} = 1$

Step 4: $$V = \\begin{bmatrix} 1/\\sqrt{2} & 1/\\sqrt{2} \\\\ 1/\\sqrt{2} & -1/\\sqrt{2} \\end{bmatrix}$$

Step 5: $\\mathbf{u}_1 = \\frac{1}{7} A\\mathbf{v}_1 = [1/\\sqrt{2},\\; 1/\\sqrt{2}]^T$
        $\\mathbf{u}_2 = \\frac{1}{1} A\\mathbf{v}_2 = [1/\\sqrt{2},\\; -1/\\sqrt{2}]^T$

Step 6: $$U = \\begin{bmatrix} 1/\\sqrt{2} & 1/\\sqrt{2} \\\\ 1/\\sqrt{2} & -1/\\sqrt{2} \\end{bmatrix}$$

Step 7: $$\\Sigma = \\begin{bmatrix} 7 & 0 \\\\ 0 & 1 \\end{bmatrix}$$

Check: $U\\Sigma V^T = A$ ✓</pre>
        </div>

        <p><strong>Numerical considerations:</strong> In practice, modern algorithms (QR algorithm, Jacobi rotation, divide-and-conquer) compute SVD directly without explicitly forming $A^T A$ to avoid numerical instability.</p>

        <div class='warning-box'>
        <p><strong>Important:</strong> Never compute $A^T A$ explicitly in production code! The condition number $\\kappa(A^T A) = \\kappa(A)^2$, which amplifies numerical errors. Use specialized SVD algorithms instead.</p>
        </div>
        """
    }
]
