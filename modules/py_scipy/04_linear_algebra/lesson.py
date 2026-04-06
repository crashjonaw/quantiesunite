"""Linear Algebra - Matrix Operations, Decompositions, and Solvers"""

TITLE = "Linear Algebra: scipy.linalg Fundamentals"

SECTIONS = [
    {
        "id": "py_scipy_linalg_01",
        "title": "Solving Linear Systems",
        "body": """
<div class="worked-example">
    <div class="concept-box formula-box">
        <h3>Core Problem: Ax = b</h3>
        <p>The fundamental linear algebra problem is solving a system of linear equations Ax = b, where A is an n×m matrix, x is the unknown vector, and b is the known vector.</p>

        <h4>Why scipy.linalg over numpy.linalg?</h4>
        <ul>
            <li><strong>More Functions:</strong> scipy.linalg has more decomposition options</li>
            <li><strong>Better Performance:</strong> Uses optimized LAPACK/BLAS routines</li>
            <li><strong>More Control:</strong> Allows specifying algorithm details</li>
            <li><strong>Handles Edge Cases:</strong> Better handling of singular and ill-conditioned matrices</li>
        </ul>

        <h4>Solution Methods in scipy.linalg</h4>
        <ul>
            <li><strong>solve:</strong> Direct solver using LU decomposition. O(n³) complexity.</li>
            <li><strong>lstsq:</strong> Least squares solver for overdetermined systems (m > n)</li>
            <li><strong>solve_triangular:</strong> Fast solver for already-triangular matrices</li>
            <li><strong>lu_solve:</strong> Uses pre-computed LU decomposition</li>
        </ul>

        <h4>Matrix Condition Number</h4>
        <p>The condition number κ(A) measures sensitivity to perturbations: small changes in A or b can cause large changes in x if κ is large (ill-conditioned).</p>
    </div>

    <div class="worked-example success-box">
        <h4>Worked Example: Solving Ax = b</h4>
        <pre class="code-block">
import numpy as np
from scipy.linalg import solve, lu_solve, lu_factor

# System: 3x + 2y = 7, 2x + 5y = 12
A = np.array([[3, 2], [2, 5]])
b = np.array([7, 12])

# Method 1: Direct solve
x = solve(A, b)
print(f"Solution: x = {x}")
print(f"Verification: Ax = {A @ x}")

# Method 2: LU decomposition for multiple right-hand sides
LU, piv = lu_factor(A)
b2 = np.array([5, 8])
x2 = lu_solve((LU, piv), b2)  # Reuse LU decomposition
print(f"\nSecond solution: x2 = {x2}")

# Check condition number
from scipy.linalg import cond
kappa = cond(A)
print(f"Condition number: κ(A) = {kappa:.6f}")
print(f"Matrix is well-conditioned: {kappa < 100}")
        </pre>
    </div>

    <div class="warning-box" style="border-left: 4px solid #fd7e14; padding: 16px; margin: 16px 0; border-radius: 4px">
        <h4>Singular Matrices and Ill-Conditioning</h4>
        <p>If A is singular (det(A) = 0) or nearly singular, solve will fail or produce unreliable results. Always check the condition number first!</p>
    </div>
</div>
        """
    },
    {
        "id": "py_scipy_linalg_02",
        "title": "Matrix Decompositions",
        "body": """
<div class="worked-example">
    <div class="concept-box formula-box">
        <h3>Understanding Matrix Decompositions</h3>
        <p>Decompositions factor a matrix into simpler components: A = U·Σ·V, A = QR, A = LU, etc. Each reveals different structural properties and enables efficient computations.</p>

        <h4>Key Decompositions</h4>
        <ul>
            <li><strong>LU (A = LU):</strong> Lower/Upper triangular. Used for solving systems and computing determinants.</li>
            <li><strong>QR (A = QR):</strong> Orthogonal/Right triangular. Numerically stable, used for least squares.</li>
            <li><strong>SVD (A = UΣVᵀ):</strong> Singular Value. Reveals rank, condition number, and principal directions.</li>
            <li><strong>Eigendecomposition (A = VΛV⁻¹):</strong> For square matrices. Eigenvalues on diagonal of Λ.</li>
            <li><strong>Cholesky (A = LLᵀ):</strong> For symmetric positive-definite matrices. Fastest method.</li>
        </ul>

        <h4>Computational Complexity</h4>
        <ul>
            <li>LU: O(n³) like direct solve, but reusable</li>
            <li>QR: O(n³) but more numerically stable</li>
            <li>SVD: O(n³) but computationally expensive</li>
            <li>Cholesky: O(n³/3), fastest when applicable</li>
        </ul>
    </div>

    <div class="worked-example success-box">
        <h4>Worked Example: SVD and Rank</h4>
        <pre class="code-block">
import numpy as np
from scipy.linalg import svd

# Matrix with rank 2 (third row is sum of first two)
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [5, 7, 9]])  # Row 3 = Row 1 + Row 2

U, s, Vt = svd(A)

print("Singular values:", s)
print(f"Rank (number of nonzero singular values): {np.sum(s > 1e-10)}")

# Reconstruction: A ≈ U @ diag(s) @ Vt
A_reconstructed = U @ np.diag(s) @ Vt
print(f"Reconstruction error: {np.linalg.norm(A - A_reconstructed):.2e}")

# SVD reveals that the matrix has rank 2
# This would cause solve() to fail if used as a system matrix
        </pre>
    </div>

    <div class="success-box">
        <h4>Key Insight: SVD for Dimensionality Reduction</h4>
        <p>The SVD naturally orders singular values. Keeping only the k largest lets you approximate the matrix in lower dimensions—the foundation for Principal Component Analysis (PCA).</p>
    </div>
</div>
        """
    },
    {
        "id": "py_scipy_linalg_03",
        "title": "Eigenvalues and Eigenvectors",
        "body": """
<div class="worked-example">
    <div class="concept-box formula-box">
        <h3>Eigendecomposition: Finding Invariant Directions</h3>
        <p>For a square matrix \(A\), eigenvalues \(\lambda\) and eigenvectors \(v\) satisfy \(Av = \lambda v\). Eigenvectors are directions that don't change direction under the transformation \(A\); eigenvalues are scaling factors.</p>

        <h4>Geometric Interpretation</h4>
        <ul>
            <li>Eigenvectors point along principal axes of the matrix</li>
            <li>Eigenvalues indicate how much A stretches/shrinks along those axes</li>
            <li>If \(\lambda < 0\), the vector gets flipped</li>
            <li>If \(\lambda = 0\), the direction is in the null space</li>
        </ul>

        <h4>Eigenvalue Problems in SciPy</h4>
        <ul>
            <li><strong>eig:</strong> Standard eigenvalue problem for dense matrices</li>
            <li><strong>eigh:</strong> For symmetric/Hermitian matrices (faster, more stable)</li>
            <li><strong>eigsh:</strong> For sparse symmetric matrices</li>
            <li><strong>eigs:</strong> For sparse matrices, computes k largest/smallest eigenvalues</li>
        </ul>

        <h4>Real Applications</h4>
        <ul>
            <li><strong>Stability Analysis:</strong> Check if eigenvalues have negative real parts (stable systems)</li>
            <li><strong>PageRank:</strong> Google's ranking algorithm uses eigenvectors of the web graph</li>
            <li><strong>Principal Component Analysis:</strong> Eigenvectors of covariance matrix are principal axes</li>
        </ul>
    </div>

    <div class="worked-example success-box">
        <h4>Worked Example: Eigenvalues of a 2×2 Matrix</h4>
        <pre class="code-block">
import numpy as np
from scipy.linalg import eig, eigh

# Symmetric matrix (rotation + scaling)
A = np.array([[3, 1],
              [1, 3]])

# For symmetric matrices, use eigh (more stable)
lambdas, V = eigh(A)

print("Eigenvalues:", lambdas)
print("\nEigenvectors (columns):")
print(V)

# Verify: A @ v = λ @ v
for i in range(len(lambdas)):
    v = V[:, i]
    Av = A @ v
    lambda_v = lambdas[i] * v
    print(f"\nλ{i} = {lambdas[i]:.6f}")
    print(f"||Av - λv|| = {np.linalg.norm(Av - lambda_v):.2e}")

# Geometric interpretation:
# Eigenvectors point along principal axes
# Eigenvalues show scaling factor along each axis
        </pre>
    </div>

    <div class="success-box">
        <h4>Key Insight: Stability from Eigenvalues</h4>
        <p>For a dynamical system dx/dt = Ax, if all eigenvalues have negative real parts, the system is stable (solutions decay to zero). This is how engineers check if systems are safe.</p>
    </div>
</div>
        """
    }
]
