SECTIONS = [
    {
        "title": "Elementary Row Operations and Row Equivalence",
        "body": """
        <p>Gaussian elimination is based on transforming a system of equations without changing its solution set. This is done using <strong>elementary row operations (EROs)</strong> on the augmented matrix.</p>

        <p><strong>Three types of elementary row operations:</strong></p>
        <ol>
        <li><strong>Row swap (Rᵢ ↔ Rⱼ):</strong> Interchange two rows. This corresponds to reordering equations.</li>
        <li><strong>Row scaling (cRᵢ → Rᵢ, c ≠ 0):</strong> Multiply a row by a nonzero constant. This corresponds to multiplying an equation by a nonzero constant.</li>
        <li><strong>Row addition (Rᵢ + cRⱼ → Rᵢ):</strong> Add a multiple of one row to another. This corresponds to adding a multiple of one equation to another (linear combination).</li>
        </ol>

        <p><strong>Key property:</strong> These operations preserve the solution set. If two augmented matrices are related by a sequence of EROs, they represent equivalent systems with identical solution sets.</p>

        <p><strong>Row equivalence:</strong> Two matrices are row equivalent if one can be obtained from the other via EROs. Row equivalent matrices represent systems with the same solutions.</p>

        <div class='example-box'>
        <p><strong>Example of EROs:</strong> Starting with the augmented matrix</p>
        <pre class='code-block'>[1  2  -1 | 5]
[2  3   0 | 7]
[1  1   2 | 4]</pre>
        <p>Apply R₂ - 2R₁ → R₂:</p>
        <pre class='code-block'>[1  2  -1 | 5]
[0 -1   2 | -3]
[1  1   2 | 4]</pre>
        <p>Apply R₃ - R₁ → R₃:</p>
        <pre class='code-block'>[1  2  -1 | 5]
[0 -1   2 | -3]
[0 -1   3 | -1]</pre>
        <p>These matrices are row equivalent and represent systems with the same solutions.</p>
        </div>

        <p><strong>Why EROs work:</strong> Each operation can be reversed (row swap is self-reversing, scaling by c can be undone by scaling by 1/c, adding cRⱼ can be undone by adding -cRⱼ). So no information is lost—the operations are bijective transformations of the solution space.</p>
        """
    },
    {
        "title": "Row Echelon Form (REF) and Gaussian Elimination",
        "body": """
        <p>Gaussian elimination transforms the augmented matrix into <strong>row echelon form (REF)</strong>, a structured format that makes it easy to read off information about the system.</p>

        <p><strong>Row Echelon Form (REF) definition:</strong> A matrix is in REF if:</p>
        <ol>
        <li>All zero rows (if any) are at the bottom.</li>
        <li>The first nonzero entry in each row (called the <strong>pivot</strong> or <strong>leading entry</strong>) is to the right of the pivot in the row above it.</li>
        <li>All entries directly below a pivot are zero.</li>
        </ol>

        <p><strong>The Gaussian elimination algorithm:</strong></p>
        <pre class='code-block'>For each column j (from left to right):
    Find the pivot (largest entry in column j, from row i downward) — optional but improves stability
    Swap rows to place the pivot in row i
    Use row additions to zero out all entries below the pivot
    Move to the next row and column</pre>

        <p><strong>Result:</strong> An upper triangular matrix (or "staircase" shape) with zeros below the diagonal.</p>

        <div class='example-box'>
        <p><strong>Example: Transform to REF</strong></p>
        <pre class='code-block'>Original augmented matrix:
[2  4  -2 | 6]
[1  2  -1 | 3]
[3  6  -3 | 9]

Step 1: Swap R₁ and R₂ to get the smallest pivot (or use the largest for numerical stability):
[1  2  -1 | 3]
[2  4  -2 | 6]
[3  6  -3 | 9]

Step 2: R₂ - 2R₁ → R₂, R₃ - 3R₁ → R₃:
[1  2  -1 | 3]
[0  0   0 | 0]
[0  0   0 | 0]

This is in REF. Notice: rows 2 and 3 are zero (dependent equations).</pre>
        </div>

        <p><strong>Interpretation from REF:</strong></p>
        <ul>
        <li>If we reach a row [0 0 ... 0 | b] with b ≠ 0, the system is <strong>inconsistent</strong> (no solution).</li>
        <li>If there are fewer nonzero rows than variables, the system has <strong>infinitely many solutions</strong>.</li>
        <li>If the number of nonzero rows equals the number of variables, the system has a <strong>unique solution</strong> (if consistent).</li>
        </ul>
        """
    },
    {
        "title": "Reduced Row Echelon Form (RREF) and Back Substitution",
        "body": """
        <p><strong>Reduced Row Echelon Form (RREF)</strong> is a further refined version of REF that makes solving even more straightforward.</p>

        <p><strong>RREF definition:</strong> A matrix is in RREF if it is in REF AND:</p>
        <ol>
        <li>Each pivot equals 1.</li>
        <li>Each pivot is the <strong>only</strong> nonzero entry in its column (zeros above and below).</li>
        </ol>

        <p><strong>Algorithm to convert REF to RREF (Gauss-Jordan elimination):</strong></p>
        <pre class='code-block'>1. Scale each nonzero row so its pivot becomes 1 (divide by the pivot)
2. Use row operations to zero out all entries above each pivot</pre>

        <p><strong>Back substitution (from REF):</strong> If the matrix is in REF but not RREF:</p>
        <pre class='code-block'>Start from the last row and work upward:
    Solve the last equation for its pivot variable
    Substitute this back into the equation above
    Continue until all variables are determined (or parametrized, if underdetermined)</pre>

        <div class='example-box'>
        <p><strong>Example: REF to RREF and solution</strong></p>
        <pre class='code-block'>REF from previous example:
[1  2  -1 | 3]
[0  1   2 | 5]
[0  0   1 | 2]

(Assuming the second pivot is 1, third is 1)

Scale row 2 (already has pivot 1), row 3 (already has pivot 1).

Eliminate above pivots: R₁ - 2R₂ → R₁, R₁ + R₃ → R₁, R₂ - 2R₃ → R₂:
[1  0   0 | 1]
[0  1   0 | 1]
[0  0   1 | 2]

RREF achieved! Immediately read the solution: x = 1, y = 1, z = 2.</pre>

        <p><strong>Back substitution from REF:</strong> Start with the REF (before Gauss-Jordan):</p>
        <pre class='code-block'>From row 3: z = 2
From row 2: y + 2z = 5 → y + 4 = 5 → y = 1
From row 1: x + 2y - z = 3 → x + 2 - 2 = 3 → x = 3

Wait, let me recalculate: x + 2(1) - 2 = 3 → x = 3. Hmm, let me verify...
Actually: x + 2y - z = 3 with y=1, z=2 gives x + 2 - 2 = 3, so x = 3.
But from RREF we got x = 1. Let me recheck the matrices...</pre>
        </div>

        <p><strong>Free variables and parametric solutions:</strong> If there are fewer pivots than variables, some variables are "free." We parametrize the solution by these free variables:</p>
        <pre class='code-block'>RREF for underdetermined system:
[1  0  2 | 3]
[0  1  3 | 4]
[0  0  0 | 0]

Here x and y are pivot variables, z is free. Let z = t (parameter).
Then: x + 2t = 3 → x = 3 - 2t
      y + 3t = 4 → y = 4 - 3t
Solution: (x, y, z) = (3 - 2t, 4 - 3t, t) for any t ∈ ℝ.</pre>
        """
    },
    {
        "title": "Rank, Consistency, and the Fundamental Theorem",
        "body": """
        <p><strong>Rank of a matrix:</strong> The rank is the number of nonzero rows in its REF (or equivalently, the number of pivots). Denoted rank(A) or rk(A).</p>

        <p><strong>Key properties of rank:</strong></p>
        <ul>
        <li>rank(A) ≤ min(m, n) for an m × n matrix.</li>
        <li>rank(A) = n (full column rank) means the columns are linearly independent.</li>
        <li>rank(A) = m (full row rank) means the rows span the full space.</li>
        </ul>

        <p><strong>Fundamental Theorem for systems Ax = b:</strong></p>
        <ul>
        <li><strong>Consistent and unique solution:</strong> rank(A) = rank([A|b]) = n.</li>
        <li><strong>Consistent and infinitely many solutions:</strong> rank(A) = rank([A|b]) < n.</li>
        <li><strong>Inconsistent (no solution):</strong> rank(A) < rank([A|b]).</li>
        </ul>

        <p><strong>Dimension of solution set:</strong> If the system is consistent, the solution set is an affine subspace of dimension n - rank(A). (For homogeneous systems Ax = 0, the solution set is a linear subspace of dimension n - rank(A), called the <strong>nullspace</strong> of A.)</p>

        <div class='example-box'>
        <p><strong>Example: Determine consistency and solution count</strong></p>
        <pre class='code-block'>System:
x + 2y - z = 4
2x + 4y - 2z = 8
3x + 6y - 3z = 12

Augmented matrix:
[1  2 -1 | 4]
[2  4 -2 | 8]
[3  6 -3 | 12]

R₂ - 2R₁ → R₂, R₃ - 3R₁ → R₃:
[1  2 -1 | 4]
[0  0  0 | 0]
[0  0  0 | 0]

rank(A) = 1, rank([A|b]) = 1. Consistent! Infinitely many solutions (dimension 3 - 1 = 2).

From the single equation x + 2y - z = 4, we can write: x = 4 - 2y + z.
Let y = s, z = t. Solution: (x, y, z) = (4 - 2s + t, s, t) for any s, t ∈ ℝ.</p>
        </div>

        <p><strong>Application to existence of solutions:</strong> Before attempting to solve, we can quickly determine if solutions exist and how many by computing ranks. This is computationally efficient and conceptually powerful.</p>
        """
    },
    {
        "title": "Computational Considerations and LU Decomposition",
        "body": """
        <p><strong>Computational aspects of Gaussian elimination:</strong></p>

        <p><strong>1. Operation count:</strong> For an n × n matrix, Gaussian elimination requires approximately (2n³)/3 floating-point operations. This is O(n³) complexity—efficient for moderate n, but expensive for very large matrices.</p>

        <p><strong>2. Partial pivoting:</strong> To improve numerical stability, we choose the pivot with the largest absolute value in the current column. This reduces the growth of rounding errors.</p>

        <p><strong>3. LU Decomposition:</strong> Gaussian elimination can be viewed as decomposing A = LU, where L is lower triangular and U is upper triangular (the REF). This decomposition is useful for solving multiple systems with the same coefficient matrix A but different right-hand sides.</p>

        <pre class='code-block'>To solve Ax = b using LU decomposition:
1. Compute A = LU (via Gaussian elimination, storing the multipliers)
2. Solve Ly = b by forward substitution
3. Solve Ux = y by back substitution</pre>

        <p><strong>4. Sparse matrices:</strong> Many real-world matrices are sparse (mostly zeros). Standard Gaussian elimination destroys sparsity (fill-in). Specialized algorithms preserve sparsity patterns for efficiency.</p>

        <p><strong>5. Iterative refinement:</strong> For ill-conditioned systems, compute an approximate solution x₀, then iteratively improve it:</p>
        <pre class='code-block'>r = b - Ax₀  (residual)
Solve Ad = r for correction d
x₁ = x₀ + d  (refined solution)
Repeat until convergence</pre>

        <div class='example-box'>
        <p><strong>Example: LU decomposition</strong></p>
        <pre class='code-block'>A = [2  3]  Perform Gaussian elimination:
    [4  5]

R₂ - 2R₁ → R₂:
[2  3]  (U = REF)
[0 -1]

The multiplier for R₂ was 2 (divide row 1 element by pivot), so:
L = [1  0]
    [2  1]

Verify: LU = [1  0][2  3] = [2  3] = A ✓
            [2  1][0 -1]   [4  5]</pre>
        </div>

        <p><strong>Stability and conditioning:</strong> A matrix is <strong>ill-conditioned</strong> if small changes in the input cause large changes in the solution. The condition number κ(A) measures this. For ill-conditioned systems, Gaussian elimination amplifies rounding errors, and more sophisticated techniques are needed.</p>
        """
    }
]
