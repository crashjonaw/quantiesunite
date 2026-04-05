TITLE = "Gauss-Jordan Elimination and Reduced Row Echelon Form"

SECTIONS = [
    {
        "title": "Introduction to Reduced Row Echelon Form (RREF)",
        "body": """
        <p>Row echelon form (REF) is convenient, but there is an even more refined form called <strong>Reduced Row Echelon Form (RREF)</strong>. RREF eliminates the need for back substitution by creating a fully diagonal pivot structure.</p>

        <div class='concept-box'>
        <p><strong>Reduced Row Echelon Form (RREF) Definition:</strong> A matrix is in RREF if:</p>
        <ol>
        <li><strong>It is in row echelon form (REF).</strong> Zero rows at the bottom, staircase pivot pattern.</li>
        <li><strong>Each pivot is 1.</strong> (not just nonzero)</li>
        <li><strong>Each pivot is the only nonzero entry in its column.</strong> All entries above and below each pivot are zero.</li>
        </ol>
        </div>

        <p>RREF is the "most reduced" form of a matrix achievable via row operations. When a system's augmented matrix is in RREF, the solution can be read directly without back substitution.</p>

        <div class='worked-example'>
        <p><strong>Example: RREF for unique solution</strong></p>
        <pre class='code-block'>RREF (3×3):
[1  0  0 | 5]
[0  1  0 | -2]
[0  0  1 | 3]

Solution: x = 5, y = −2, z = 3 (immediate!)</pre>
        </div>

        <div class='worked-example'>
        <p><strong>Example: RREF with free variables</strong></p>
        <pre class='code-block'>RREF (3×5):
[1  0  2  0 | 4]
[0  1 -1  0 | 7]
[0  0  0  1 | 2]

Variables: x₁, x₂, x₃, x₄, x₅
Pivots in columns 1, 2, 4.
Free variables: x₃, x₅.

Set x₃ = s, x₅ = t.
Immediately: x₁ = 4 − 2s, x₂ = 7 + s, x₄ = 2</pre>
        </div>

        <div class='success-box'>
        <p><strong>Advantage of RREF:</strong> Solutions appear directly. No need for back substitution, making the process purely mechanical.</p>
        </div>
        """
    },
    {
        "title": "Gauss-Jordan Elimination Algorithm",
        "body": """
        <p>Gauss-Jordan elimination is the extension of Gaussian elimination that transforms a matrix all the way to RREF (not just REF).</p>

        <div class='concept-box'>
        <p><strong>Algorithm: Gaussian Elimination → REF, then Gauss-Jordan → RREF</strong></p>
        <ol>
        <li><strong>Forward pass (to REF):</strong> Gaussian elimination as before, creating the staircase pattern with zeros below pivots.</li>
        <li><strong>Backward pass (to RREF):</strong> Starting from the bottom pivot and moving up, scale each row so its pivot becomes 1, then eliminate entries <strong>above</strong> each pivot.</li>
        </ol>
        </div>

        <div class='worked-example'>
        <p><strong>Forward pass (to REF): Already computed via Gaussian elimination</strong></p>
        <pre class='code-block'>REF:
[1  2  4 | 7]
[0  1  3 | 5]
[0  0  2 | 6]</pre>

        <p><strong>Backward pass (to RREF):</strong></p>
        <p>Step 1: Scale row 3 so its pivot (2) becomes 1. Multiply row 3 by 1/2:</p>
        <pre class='code-block'>[1  2  4 | 7]
[0  1  3 | 5]
[0  0  1 | 3]</pre>

        <p>Step 2: Eliminate above the pivot in position (3,3). Apply R₁ − 4R₃ → R₁ and R₂ − 3R₃ → R₂:</p>
        <pre class='code-block'>[1  2  0 | -5]
[0  1  0 | -4]
[0  0  1 | 3]</pre>

        <p>Step 3: Scale row 2 (already has pivot 1). Eliminate above: R₁ − 2R₂ → R₁:</p>
        <pre class='code-block'>[1  0  0 | 3]
[0  1  0 | -4]
[0  0  1 | 3]</pre>

        <p><strong>Final RREF:</strong> All pivots are 1, and each pivot is the only nonzero entry in its column.</p>
        <p><strong>Solution:</strong> x = 3, y = −4, z = 3 (immediately obvious!)</p>
        </div>

        <div class='success-box'>
        <p><strong>Computational cost:</strong> Gauss-Jordan is more expensive than Gaussian elimination + back substitution (approximately 50% more operations). However, it is useful when:</p>
        <ul>
        <li>You need to solve many systems Ax = b with the same A but different b's (RREF eliminates b dependence).</li>
        <li>You need to find the inverse A⁻¹ (by applying Gauss-Jordan to [A | I]).</li>
        <li>You want to avoid back substitution entirely.</li>
        </ul>
        </div>
        """
    },
    {
        "title": "Using RREF to Find Matrix Inverses",
        "body": """
        <p>One of the most practical applications of Gauss-Jordan elimination is finding the inverse of a square matrix A.</p>

        <div class='concept-box'>
        <p><strong>Finding A⁻¹ using Gauss-Jordan:</strong></p>
        <p>If A is an n × n invertible matrix, apply Gauss-Jordan elimination to the augmented matrix [A | I], where I is the n × n identity. When A is reduced to I, the right side becomes A⁻¹.</p>
        <p>Result: [A | I] → [I | A⁻¹]</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Find the inverse of A = [2 1; 1 1]</strong></p>
        <p>Augmented matrix [A | I]:</p>
        <pre class='code-block'>[2  1 | 1  0]
[1  1 | 0  1]</pre>

        <p><strong>Forward pass:</strong> Swap R₁ and R₂:</p>
        <pre class='code-block'>[1  1 | 0  1]
[2  1 | 1  0]</pre>

        <p>R₂ − 2R₁ → R₂:</p>
        <pre class='code-block'>[1  1 | 0  1]
[0 -1 | 1 -2]</pre>

        <p><strong>Backward pass:</strong> Scale R₂ by −1:</p>
        <pre class='code-block'>[1  1 | 0  1]
[0  1 | -1  2]</pre>

        <p>R₁ − R₂ → R₁:</p>
        <pre class='code-block'>[1  0 | 1 -1]
[0  1 | -1  2]</pre>

        <p><strong>Result:</strong> A⁻¹ = [1 −1; −1 2]</p>

        <p>Verify: A · A⁻¹ = [2 1; 1 1] · [1 −1; −1 2] = [1 0; 0 1] = I ✓</p>
        </div>

        <div class='warning-box'>
        <p><strong>When does A⁻¹ not exist?</strong> If during Gauss-Jordan on [A | I], you cannot reduce A to the identity (e.g., you get a zero row in the A portion), then A is singular (determinant = 0) and has no inverse.</p>
        </div>

        <div class='success-box'>
        <p><strong>Practical use:</strong> While Gauss-Jordan is theoretically elegant, for numerical computation, LU decomposition is often preferred (more stable and efficient for multiple right-hand sides).</p>
        </div>
        """
    },
    {
        "title": "RREF and Linear Independence",
        "body": """
        <p>The RREF of a matrix reveals information about linear independence of rows and columns.</p>

        <div class='concept-box'>
        <p><strong>Linear independence from RREF:</strong></p>
        <ul>
        <li>The <strong>nonzero rows</strong> of the RREF of a matrix A are linearly independent. They form a basis for the row space of A.</li>
        <li>The <strong>pivot columns</strong> of the RREF of A correspond to linearly independent columns of the original A.</li>
        <li>The <strong>non-pivot columns</strong> can be expressed as linear combinations of the pivot columns.</li>
        </ul>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Identifying linear dependence</strong></p>
        <p>Original matrix:</p>
        <pre class='code-block'>A = [1  2  3]
    [2  4  6]
    [1  1  1]</pre>

        <p>RREF (computed via Gauss-Jordan):</p>
        <pre class='code-block'>RREF(A) = [1  0 -1]
          [0  1  2]
          [0  0  0]</pre>

        <p><strong>Interpretation:</strong></p>
        <ul>
        <li>Pivots in columns 1 and 2. Columns 1 and 2 of A are linearly independent.</li>
        <li>Column 3 is a non-pivot column: column 3 = −1 · column 1 + 2 · column 2 (from the RREF).</li>
        <li>Rank = 2 (two independent columns).</li>
        </ul>
        </div>

        <div class='success-box'>
        <p><strong>Uniqueness of RREF:</strong> Every matrix has a unique RREF. This makes RREF a canonical form for matrices—two matrices are row equivalent if and only if they have the same RREF.</p>
        </div>
        """
    }
]
