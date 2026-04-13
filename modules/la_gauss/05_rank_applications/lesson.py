TITLE = "Rank, Applications, and Advanced Topics"

SECTIONS = [
    {
        "title": "Rank: Definition and Properties",
        "body": """
        <p>Rank is one of the most important concepts in linear algebra. It quantifies the "independence" or "effective dimension" of a matrix.</p>

        <div class='concept-box'>
        <p><strong>Definition of Rank:</strong> The rank of a matrix A (denoted rank(A) or rk(A)) is the number of nonzero rows in any row echelon form (REF) of A. Equivalently, it is the number of pivots in the REF.</p>
        </div>

        <p>Rank is well-defined because all row echelon forms of the same matrix have the same number of nonzero rows (though their entries may differ).</p>

        <div class='worked-example'>
        <p><strong>Example 1: Full rank</strong></p>
        <pre class='code-block'>A = [1  2  3]
    [4  5  6]
    [7  8  10]

REF:
    [1  2   3]
    [0  -3  -6]
    [0  0   1]

Number of nonzero rows: 3, so rank(A) = 3.
For a 3×3 matrix, rank 3 is "full rank."</pre>
        </div>

        <div class='worked-example'>
        <p><strong>Example 2: Rank deficient</strong></p>
        <pre class='code-block'>A = [1  2  3]
    [2  4  6]
    [3  6  9]

REF:
    [1  2  3]
    [0  0  0]
    [0  0  0]

Number of nonzero rows: 1, so rank(A) = 1.
All rows are multiples of the first row (linearly dependent).</pre>
        </div>

        <div class='concept-box'>
        <p><strong>Key properties of rank:</strong></p>
        <ul>
        <li>\(\\text{rank}(A) \\leq \min(m, n)\) for an \(m \\times n\) matrix (bounded by both dimensions).</li>
        <li>\(\\text{rank}(A) = \\text{rank}(A^T)\) (rank of transpose equals rank of original).</li>
        <li>\(\\text{rank}(A) = n\) (full column rank) \(\iff\) columns of \(A\) are linearly independent.</li>
        <li>\(\\text{rank}(A) = m\) (full row rank) \(\iff\) rows of \(A\) are linearly independent.</li>
        <li>For a square \(n \\times n\) matrix: \(\\text{rank}(A) = n \iff A\) is invertible (\(\det(A) \\neq 0\)).</li>
        </ul>
        </div>

        <div class='success-box'>
        <p><strong>Interpretation:</strong> Rank measures the "effective number of independent constraints" (rows) or "effective dimensionality" (columns) of a matrix. A rank-deficient matrix has redundancy—some rows or columns are linear combinations of others.</p>
        </div>
        """
    },
    {
        "title": "The Fundamental Theorem for Systems Ax = b",
        "body": """
        <p>The fundamental theorem completely characterizes the solution set of any linear system by comparing ranks.</p>

        <div class='concept-box'>
        <p><strong>Fundamental Theorem for Systems Ax = b:</strong></p>
        <p>Consider a system of m equations in n unknowns Ax = b. Let A be the coefficient matrix and [A|b] be the augmented matrix.</p>
        <ul>
        <li><strong>Inconsistent (no solution):</strong> \(\\text{rank}(A) < \\text{rank}([A|b])\). The augmented matrix has an additional rank due to the right-hand side, indicating a contradiction.</li>
        <li><strong>Consistent with unique solution:</strong> \(\\text{rank}(A) = \\text{rank}([A|b]) = n\). All variables are pivots.</li>
        <li><strong>Consistent with infinitely many solutions:</strong> \(\\text{rank}(A) = \\text{rank}([A|b]) < n\). Some variables are free (\(n - \\text{rank}(A)\) free variables).</li>
        </ul>
        </div>

        <div class='worked-example'>
        <p><strong>Example 1: Inconsistent system</strong></p>
        <pre class='code-block'>System:
x + 2y = 1
2x + 4y = 3

Augmented matrix:
[1  2 | 1]
[2  4 | 3]

REF:
[1  2 | 1]
[0  0 | 1]  ← Last row says 0 = 1 (contradiction!)

rank(A) = 1 (first row only has a pivot)
rank([A|b]) = 2 (both rows are nonzero)

Since rank(A) < rank([A|b]), the system is <strong>inconsistent (no solution)</strong>.</pre>
        </div>

        <div class='worked-example'>
        <p><strong>Example 2: Unique solution</strong></p>
        <pre class='code-block'>System:
x + y = 3
2x + 3y = 8

Augmented matrix:
[1  1 | 3]
[2  3 | 8]

REF:
[1  1 | 3]
[0  1 | 2]

rank(A) = 2 (two nonzero rows, two pivots)
rank([A|b]) = 2 (two nonzero rows)
n = 2 (number of variables)

Since rank(A) = rank([A|b]) = n = 2, the system has a <strong>unique solution</strong>.
By back substitution: y = 2, x = 1.</pre>
        </div>

        <div class='worked-example'>
        <p><strong>Example 3: Infinitely many solutions</strong></p>
        <pre class='code-block'>System:
x + 2y + z = 4
2x + 4y + 2z = 8

Augmented matrix:
[1  2  1 | 4]
[2  4  2 | 8]

REF:
[1  2  1 | 4]
[0  0  0 | 0]

rank(A) = 1 (one nonzero row, one pivot)
rank([A|b]) = 1 (one nonzero row)
n = 3 (number of variables)

Since rank(A) = rank([A|b]) = 1 < 3, the system is <strong>consistent with infinitely many solutions</strong>.
Number of free variables: 3 − 1 = 2.
Solution: (x, y, z) = (4 − 2s − t, s, t) for s, t ∈ ℝ.</pre>
        </div>

        <div class='success-box'>
        <p><strong>Before solving:</strong> Compute the ranks of A and [A|b] to immediately determine if solutions exist and how many.</p>
        </div>
        """
    },
    {
        "title": "Rank, Nullspace, and Solution Dimension",
        "body": """
        <p>The dimension of the solution set is directly determined by the rank.</p>

        <div class='concept-box'>
        <p><strong>Rank-nullity theorem (for consistent systems):</strong></p>
        <ul>
        <li>If \(Ax = b\) is consistent, the solution set is an <strong>affine subspace</strong> of dimension \(n - \\text{rank}(A)\).</li>
        <li>For homogeneous systems \(Ax = 0\), the solution set (nullspace of \(A\)) is a <strong>linear subspace</strong> of dimension \(n - \\text{rank}(A)\), denoted \(\\text{nullity}(A) = n - \\text{rank}(A)\).</li>
        </ul>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Nullspace of a matrix</strong></p>
        <pre class='code-block'>A = [1  2  3  4]
    [2  4  6  8]

REF:
    [1  2  3  4]
    [0  0  0  0]

rank(A) = 1, nullity(A) = 4 − 1 = 3.

The nullspace is 3-dimensional. Let's find a basis.
Set x₂ = 1, x₃ = 0, x₄ = 0: Row 1 gives x₁ = −2. Vector v₁ = (−2, 1, 0, 0).
Set x₂ = 0, x₃ = 1, x₄ = 0: Row 1 gives x₁ = −3. Vector v₂ = (−3, 0, 1, 0).
Set x₂ = 0, x₃ = 0, x₄ = 1: Row 1 gives x₁ = −4. Vector v₃ = (−4, 0, 0, 1).

Nullspace: span{(−2, 1, 0, 0), (−3, 0, 1, 0), (−4, 0, 0, 1)}</pre>
        </div>

        <div class='success-box'>
        <p><strong>Dimension formula:</strong> \(\\text{rank}(A) + \\text{nullity}(A) = n\). This fundamental identity relates the rank and the dimension of the nullspace.</p>
        </div>
        """
    },
    {
        "title": "Applications and Computational Considerations",
        "body": """
        <div class='concept-box'>
        <p><strong>LU Decomposition:</strong> Gaussian elimination can be reformulated as a matrix factorization A = LU, where L is lower triangular and U is upper triangular (row echelon form). This factorization is useful for solving multiple systems Ax = bᵢ efficiently.</p>
        <pre class='code-block'>To solve Ax = b using LU:
1. Compute A = LU (Gaussian elimination, store multipliers in L)
2. Solve Ly = b by forward substitution (O(n²) operations)
3. Solve Ux = y by back substitution (O(n²) operations)

If solving many systems with the same A: O(n³) once for LU, then O(n²) per right-hand side.</pre>
        </div>

        <div class='worked-example'>
        <p><strong>Numerical Stability—Partial Pivoting:</strong> In floating-point arithmetic, divisions by small pivots amplify rounding errors. Partial pivoting (choosing the largest absolute value as pivot) dramatically reduces error growth.</p>
        <pre class='code-block'>Without pivoting (vulnerable to errors):
0.0001 x + y = 1
x + y = 2

With pivoting (swap rows first):
x + y = 2
0.0001 x + y = 1</pre>
        </div>

        <div class='worked-example'>
        <p><strong>Sparse matrices:</strong> Many real-world matrices are sparse (mostly zeros). Gaussian elimination typically destroys sparsity (fill-in). Specialized algorithms and data structures preserve sparsity patterns for efficiency in very large systems.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Ill-conditioned systems:</strong> Some matrices are inherently sensitive to perturbations (small changes in input cause large changes in output). The condition number \(\kappa(A)\) measures this sensitivity. For ill-conditioned systems, iterative refinement is used:</p>
        <pre class='code-block'>1. Compute approximate solution x₀ via Gaussian elimination
2. Compute residual r = b − Ax₀
3. Solve Ad = r for correction d
4. Refine: x₁ = x₀ + d
5. Repeat until convergence</pre>
        </div>

        <div class='success-box'>
        <p><strong>Complexity summary:</strong> Gaussian elimination is \(O(n^3)\) in time and \(O(n^2)\) in space. For very large systems (\(n > 10{,}000\)) or special structure (sparsity), specialized iterative methods (conjugate gradient, GMRES) or preconditioned solvers are preferred.</p>
        </div>
        """
    },
    {
        "title": "Least Squares and Overdetermined Systems",
        "body": """
        <p>When a system Ax = b has more equations than unknowns (m > n) and is inconsistent, we seek the best approximate solution. Gaussian elimination can be extended to solve this.</p>

        <div class='concept-box'>
        <p><strong>Least squares problem:</strong> Given an overdetermined system \(Ax = b\) (\(m > n\)), find \(x\) that minimizes the residual \(\|b - Ax\|^2\). The solution \(x^*\) is given by the <strong>normal equations</strong>:</p>
        <pre class='code-block'>Aᵀ Ax* = Aᵀb</pre>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Fitting a line to data points</strong></p>
        <p>Three points: (1, 2), (2, 3), (3, 5). Fit y = mx + c.</p>
        <pre class='code-block'>Overdetermined system:
m + c = 2
2m + c = 3
3m + c = 5

Matrix form:
[1  1] [m]   [2]
[2  1] [c] = [3]
[3  1]       [5]

A = [1 1], b = [2]
    [2 1]      [3]
    [3 1]      [5]

Normal equations: Aᵀ Ax = Aᵀ b
[1  2  3] [1  1] [m]   [1  2  3] [2]
[1  1  1] [2  1] [c] = [1  1  1] [3]
          [3  1]                 [5]

[14  6] [m]   [22]
[6   3] [c] = [10]

Solve via Gaussian elimination: m ≈ 1.5, c ≈ 0.5</pre>
        </div>

        <div class='success-box'>
        <p><strong>Advantage of least squares:</strong> Avoids the contradiction of an inconsistent system by finding the best compromise. Widely used in data fitting, regression, and parameter estimation.</p>
        </div>
        """
    }
]
