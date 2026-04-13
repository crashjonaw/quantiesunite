TITLE = "Elementary Row Operations and Row Equivalence"

SECTIONS = [
    {
        "title": "Motivation: Solving Systems Through Transformation",
        "body": """
        <p>Gaussian elimination is based on a fundamental principle: we can transform a system of linear equations without changing its solution set. The key insight is that certain operations on equations (rows of the augmented matrix) preserve the solution.</p>

        <p>Instead of directly solving each equation, we systematically <strong>reduce the system to a simpler form</strong> using transformations that maintain equivalence.</p>

        <div class='concept-box'>
        <p><strong>Why does this work?</strong></p>
        <ul>
        <li>If two systems have the same solution set, they are <strong>equivalent</strong>.</li>
        <li>Certain operations on equations preserve equivalence.</li>
        <li>We can combine these operations to reach a form where solutions are obvious.</li>
        </ul>
        </div>
        """
    },
    {
        "title": "Three Elementary Row Operations",
        "body": """
        <p>There are exactly three types of elementary row operations (EROs). Each corresponds to a valid algebraic manipulation of a system of equations.</p>

        <div class='worked-example'>
        <p><strong>ERO 1: Row Swap (Rᵢ ↔ Rⱼ)</strong></p>
        <p>Interchange two rows. This corresponds to reordering equations—clearly the solution set doesn't change.</p>
        <p>Example: Swapping rows 1 and 2</p>
        <pre class='code-block'>[2  3 | 5]      [1  2 | 3]
[1  2 | 3]  →   [2  3 | 5]</pre>
        </div>

        <div class='worked-example'>
        <p><strong>ERO 2: Row Scaling (\(cR_i \to R_i\), \(c \\neq 0\))</strong></p>
        <p>Multiply a row by a nonzero constant. This corresponds to multiplying an equation by a nonzero constant, which doesn't change the solution (e.g., "2x + 4y = 6" is equivalent to "x + 2y = 3").</p>
        <p>Example: Multiply row 1 by 1/2</p>
        <pre class='code-block'>[2  4 | 6]      [1  2 | 3]
[1  2 | 3]  →   [1  2 | 3]</pre>
        </div>

        <div class='worked-example'>
        <p><strong>ERO 3: Row Addition (Rᵢ + cRⱼ → Rᵢ)</strong></p>
        <p>Add a multiple of one row to another. Algebraically, this replaces one equation with a linear combination of itself and another equation—a fundamental trick in solving systems.</p>
        <p>Example: Replace row 2 with (row 2 − 2 × row 1)</p>
        <pre class='code-block'>[1  2  -1 | 3]      [1  2  -1 | 3]
[2  4  -2 | 6]  →   [0  0   0 | 0]</pre>
        </div>

        <div class='success-box'>
        <p><strong>Key principle:</strong> Each ERO can be reversed:</p>
        <ul>
        <li>Row swap is self-reversing (swap i and j twice → back to original)</li>
        <li>Scaling by c can be undone by scaling by 1/c</li>
        <li>Adding cRⱼ can be undone by subtracting cRⱼ (i.e., adding −cRⱼ)</li>
        </ul>
        <p>Since each operation is reversible, no information is lost.</p>
        </div>
        """
    },
    {
        "title": "Row Equivalence and Solution Preservation",
        "body": """
        <p><strong>Definition:</strong> Two matrices are <strong>row equivalent</strong> if one can be obtained from the other via a sequence of elementary row operations.</p>

        <div class='concept-box'>
        <p><strong>Fundamental theorem:</strong> If two augmented matrices are row equivalent, they represent systems with <strong>identical solution sets</strong>.</p>
        </div>

        <p>This is the foundation of Gaussian elimination: we transform an augmented matrix into a row-equivalent simpler form (row echelon form), then read off the solutions.</p>

        <div class='worked-example'>
        <p><strong>Example: Row operations preserve solutions</strong></p>
        <p>Original system (and augmented matrix):</p>
        <pre class='code-block'>x + 2y - z = 5
2x + 3y + 0z = 7
x + y + 2z = 4

Augmented matrix:
[1  2  -1 | 5]
[2  3   0 | 7]
[1  1   2 | 4]</pre>

        <p>Apply R₂ - 2R₁ → R₂ (eliminate x from row 2):</p>
        <pre class='code-block'>[1  2  -1 | 5]
[0 -1   2 | -3]
[1  1   2 | 4]</pre>

        <p>Apply R₃ - R₁ → R₃ (eliminate x from row 3):</p>
        <pre class='code-block'>[1  2  -1 | 5]
[0 -1   2 | -3]
[0 -1   3 | -1]</pre>

        <p>The new augmented matrix is row equivalent to the original. Any solution to the original system is also a solution to the transformed system, and vice versa.</p>
        </div>

        <div class='warning-box'>
        <p><strong>What about other operations?</strong> Operations like "multiply row i by 0" or "replace row i with row i plus row j (without a multiplier) changed by something arbitrary" are NOT elementary row operations because they are not reversible or change the solution set.</p>
        </div>
        """
    },
    {
        "title": "Why Elementary Row Operations Are Reversible",
        "body": """
        <p>The reversibility of EROs is essential: it guarantees that applying an ERO doesn't lose or create spurious solutions.</p>

        <div class='worked-example'>
        <p><strong>Row Swap Reversal:</strong> (Rᵢ ↔ Rⱼ) is its own inverse.</p>
        <p>Applying "swap rows 1 and 2" twice gives the original matrix.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Scaling Reversal:</strong> If we apply \((cR_i \to R_i)\) with \(c \\neq 0\), we can undo it with \((1/c \\cdot R_i \to R_i)\).</p>
        <p>Example: Double row 1, then halve row 1 → back to original.</p>
        <pre class='code-block'>Original:     [1  2 | 3]
2R₁:          [2  4 | 6]
(1/2)R₁:      [1  2 | 3]</pre>
        </div>

        <div class='worked-example'>
        <p><strong>Row Addition Reversal:</strong> If we apply (Rᵢ + cRⱼ → Rᵢ), we can undo it with (Rᵢ − cRⱼ → Rᵢ).</p>
        <p>Example:</p>
        <pre class='code-block'>Original:            [1  2 | 3]    [1  2 | 3]
                     [0  3 | 6]    [0  3 | 6]

After R₁ + 2R₂:     [1  8 | 15]   [0  3 | 6]
                     [0  3 | 6]

After R₁ − 2R₂:     [1  2 | 3]    [0  3 | 6]  ← Back to original</pre>
        </div>

        <div class='success-box'>
        <p><strong>Consequence:</strong> The transformation from the original matrix to its row-equivalent form is a <strong>bijection</strong> (one-to-one, onto map) between solution sets. Thus solutions are preserved perfectly.</p>
        </div>
        """
    }
]
