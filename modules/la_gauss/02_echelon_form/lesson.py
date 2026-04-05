TITLE = "Row Echelon Form and Gaussian Elimination Algorithm"

SECTIONS = [
    {
        "title": "What is Row Echelon Form (REF)?",
        "body": """
        <p>Row Echelon Form is a structured matrix format that makes the solution of a system obvious. Once a matrix is in REF, we can read off information about consistency, rank, and the general form of solutions.</p>

        <div class='concept-box'>
        <p><strong>Row Echelon Form (REF) Definition:</strong> A matrix is in REF if:</p>
        <ol>
        <li><strong>All zero rows are at the bottom.</strong> If there are rows that are entirely zero, they must come after all nonzero rows.</li>
        <li><strong>The leading entry (pivot) of each nonzero row is to the right of the pivot in the row above.</strong> This creates a "staircase" pattern.</li>
        <li><strong>All entries directly below a pivot are zero.</strong> This ensures the triangular structure.</li>
        </ol>
        </div>

        <div class='worked-example'>
        <p><strong>Examples of matrices in REF:</strong></p>
        <pre class='code-block'>Example 1 (3×3):     Example 2 (3×4):     Example 3 (4×3):
[1  2  3]            [2  1  0  5]         [1  3  2]
[0  1  4]            [0  3  1  7]         [0  2  5]
[0  0  5]            [0  0  0  2]         [0  0  1]
                                          [0  0  0]</pre>

        <p>Each matrix has a pivot in each nonzero row, positioned rightward in a staircase. All entries below pivots are zero.</p>
        </div>

        <div class='warning-box'>
        <p><strong>What is NOT REF:</strong></p>
        <pre class='code-block'>Not REF (zero row not at bottom):
[1  2  3]
[0  0  0]
[0  1  2]  ← nonzero row below zero row

Not REF (pivots not staggered):
[1  2  3]
[0  2  4]
[0  0  5]  (this is OK)

[2  1  3]
[1  3  4]  ← second row pivot at same position as first row</pre>
        </div>
        """
    },
    {
        "title": "The Gaussian Elimination Algorithm",
        "body": """
        <p>Gaussian elimination is the systematic process of transforming an augmented matrix into REF using elementary row operations. The algorithm processes columns from left to right, creating the staircase pattern.</p>

        <div class='concept-box'>
        <p><strong>Gaussian Elimination (Forward Pass):</strong></p>
        <pre class='code-block'>FOR each column j (from left to right):
  FOR each row i (starting from current position):
    Find the pivot: a nonzero entry in column j (from row i downward)
      [Optional: choose the largest for numerical stability—partial pivoting]
    Swap rows to place the pivot in the current row
    Use row additions to zero out all entries BELOW this pivot in column j
    Move to the next row and next column</pre>
        </div>

        <p>The result is an upper triangular matrix (staircase shape) with zeros below the diagonal—this is row echelon form.</p>

        <div class='worked-example'>
        <p><strong>Step-by-step example: Transform to REF</strong></p>
        <p>Original augmented matrix:</p>
        <pre class='code-block'>[2  4  -2 | 6]
[1  2  -1 | 3]
[3  6  -3 | 9]</pre>

        <p><strong>Step 1:</strong> Focus on column 1. Find a pivot in column 1 (rows 1–3). Use row 2 (which has 1, smallest). Swap R₁ and R₂:</p>
        <pre class='code-block'>[1  2  -1 | 3]
[2  4  -2 | 6]
[3  6  -3 | 9]</pre>

        <p><strong>Step 2:</strong> Zero out entries below the pivot (1) in column 1.</p>
        <p>Apply R₂ − 2R₁ → R₂ and R₃ − 3R₁ → R₃:</p>
        <pre class='code-block'>[1  2  -1 | 3]
[0  0   0 | 0]
[0  0   0 | 0]</pre>

        <p><strong>Step 3:</strong> Move to row 2, column 2. No nonzero entries below, and row 2 is zero—skip to row 3.</p>
        <p>Row 3 is also zero. We are done. The matrix is in REF.</p>

        <p><strong>Observation:</strong> We have only one pivot (in position (1,1)), so rank = 1. The system has infinitely many solutions (since 1 < 3 variables).</p>
        </div>

        <div class='success-box'>
        <p><strong>Partial Pivoting (Numerical Stability):</strong> In practice, instead of just finding any nonzero pivot, we choose the pivot with the <strong>largest absolute value</strong> in the current column. This is called partial pivoting and reduces rounding errors in floating-point arithmetic.</p>
        </div>
        """
    },
    {
        "title": "Reading Solutions from REF",
        "body": """
        <p>Once the augmented matrix is in REF, we can immediately assess consistency and solution structure.</p>

        <div class='concept-box'>
        <p><strong>Interpretation from REF:</strong></p>
        <ul>
        <li><strong>Inconsistent system:</strong> If we reach a row [0 0 ... 0 | b] with b ≠ 0, the system is inconsistent (no solution). This row says "0 = b," which is a contradiction.</li>
        <li><strong>Unique solution:</strong> If the number of nonzero rows (pivots) equals the number of variables, the system has a unique solution (assuming consistent).</li>
        <li><strong>Infinitely many solutions:</strong> If the number of pivots is less than the number of variables, the system has infinitely many solutions parametrized by the free variables.</li>
        </ul>
        </div>

        <div class='worked-example'>
        <p><strong>Example 1: Inconsistent system</strong></p>
        <pre class='code-block'>REF:
[1  2  -1 | 4]
[0  1   2 | 5]
[0  0   0 | 3]  ← This row says 0x + 0y + 0z = 3, a contradiction!</pre>
        <p>The system is <strong>inconsistent (no solution)</strong>.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example 2: Infinitely many solutions (underdetermined)</strong></p>
        <pre class='code-block'>REF:
[1  2  -1 | 5]
[0  1   2 | 3]
[0  0   0 | 0]

Number of pivots: 2, Number of variables: 3.
Free variables: 1 (namely, z is free).
Solutions: Infinitely many (1-parameter family).</pre>
        </div>

        <div class='worked-example'>
        <p><strong>Example 3: Unique solution</strong></p>
        <pre class='code-block'>REF:
[1  3  2 | 5]
[0  1  1 | 2]
[0  0  1 | 3]

Number of pivots: 3, Number of variables: 3.
The system has a <strong>unique solution</strong> (can find by back substitution).</pre>
        </div>

        <div class='success-box'>
        <p><strong>Rank and dimensions:</strong> The rank of the coefficient matrix is the number of nonzero rows (pivots) in REF. If the system is consistent, the dimension of the solution set is n − rank(A), where n is the number of variables.</p>
        </div>
        """
    },
    {
        "title": "Complexity and Computational Cost",
        "body": """
        <p>Understanding the computational cost of Gaussian elimination is important for large systems.</p>

        <div class='concept-box'>
        <p><strong>Operation count for Gaussian elimination on an n × n matrix:</strong></p>
        <ul>
        <li>Forward pass (to REF): approximately (2n³)/3 floating-point operations.</li>
        <li>Time complexity: O(n³).</li>
        <li>This is efficient for moderate n (e.g., n < 10,000) but expensive for very large matrices.</li>
        </ul>
        </div>

        <p>For very large or sparse matrices, specialized algorithms (iterative methods, sparse direct solvers) are often used instead.</p>

        <div class='worked-example'>
        <p><strong>Complexity examples:</strong></p>
        <ul>
        <li>n = 10: ~667 operations (fast)</li>
        <li>n = 100: ~667,000 operations (still fast)</li>
        <li>n = 1,000: ~667,000,000 operations (slower)</li>
        <li>n = 10,000: ~667,000,000,000 operations (very slow)</li>
        </ul>
        <p>For n = 10,000, a modern computer (10⁹ operations/second) would take ~667 seconds ≈ 11 minutes.</p>
        </div>

        <div class='success-box'>
        <p><strong>Partial pivoting cost:</strong> Searching for the pivot with the largest absolute value adds a small additional cost but dramatically improves numerical stability. It is standard in practice.</p>
        </div>
        """
    }
]
