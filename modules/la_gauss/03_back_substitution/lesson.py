TITLE = "Back Substitution and Solving from REF"

SECTIONS = [
    {
        "title": "The Principle of Back Substitution",
        "body": """
        <p>Once the augmented matrix is in row echelon form (REF), the system has a triangular structure that makes solving straightforward. Back substitution is the process of solving from the bottom row upward, systematically finding the values of variables.</p>

        <div class='concept-box'>
        <p><strong>Back Substitution Strategy:</strong></p>
        <ol>
        <li><strong>Start with the last (bottom) nonzero row.</strong> Solve for the pivot variable in this row.</li>
        <li><strong>Substitute upward:</strong> Use the value found to substitute into the row above.</li>
        <li><strong>Repeat:</strong> Solve each row for its pivot variable.</li>
        <li><strong>Continue until the first row:</strong> All unknowns are determined.</li>
        </ol>
        </div>

        <p>This works because each row has only one new unknown (the pivot variable), and all other unknowns in that row have already been solved or are free parameters.</p>

        <div class='worked-example'>
        <p><strong>Simple example: Unique solution</strong></p>
        <p>REF augmented matrix:</p>
        <pre class='code-block'>[1  2  3 | 14]
[0  1  2 | 8]
[0  0  1 | 3]</pre>

        <p><strong>Back substitution:</strong></p>
        <p>Row 3: 1·z = 3 → z = 3</p>
        <p>Row 2: 1·y + 2·z = 8 → y + 2(3) = 8 → y = 2</p>
        <p>Row 1: 1·x + 2·y + 3·z = 14 → x + 2(2) + 3(3) = 14 → x = 14 − 4 − 9 = 1</p>
        <p><strong>Solution:</strong> (x, y, z) = (1, 2, 3)</p>
        </div>

        <div class='success-box'>
        <p><strong>Why this works:</strong> The REF creates a triangular dependency. The last row depends only on the last variable, the second-to-last row depends on the last two variables (but we know the last one), and so on. This hierarchical structure allows us to solve "backward."</p>
        </div>
        """
    },
    {
        "title": "Parametrization with Free Variables",
        "body": """
        <p>When the number of pivots is less than the number of variables, some variables are <strong>free</strong>. We parametrize the solution set by these free variables.</p>

        <div class='concept-box'>
        <p><strong>Free vs. Pivot Variables:</strong></p>
        <ul>
        <li><strong>Pivot variable:</strong> A variable that corresponds to a pivot column in REF. Its value is determined by the system.</li>
        <li><strong>Free variable:</strong> A variable that corresponds to a non-pivot column. It can take any value.</li>
        <li><strong>Number of free variables:</strong> \(n - \\text{rank}(A)\), where \(n\) is the number of variables.</li>
        </ul>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Underdetermined system (infinitely many solutions)</strong></p>
        <p>REF augmented matrix:</p>
        <pre class='code-block'>[1  2  3 | 4]
[0  1  5 | 6]
[0  0  0 | 0]</pre>

        <p>Columns 1 and 2 have pivots (in rows 1 and 2). Column 3 does not, so z is a free variable.</p>

        <p><strong>Back substitution with parametrization:</strong></p>
        <p>Let z = t (free parameter, t ∈ ℝ).</p>
        <p>Row 2: y + 5z = 6 → y + 5t = 6 → y = 6 − 5t</p>
        <p>Row 1: x + 2y + 3z = 4 → x + 2(6 − 5t) + 3t = 4 → x + 12 − 10t + 3t = 4 → x = 4 − 12 + 7t = −8 + 7t</p>

        <p><strong>Parametric solution:</strong></p>
        <pre class='code-block'>(x, y, z) = (−8 + 7t, 6 − 5t, t) for any t ∈ ℝ</pre>

        <p>The solution set is a line in 3D space (1-dimensional affine subspace).</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Two free variables (infinitely many solutions with dimension 2)</strong></p>
        <p>REF augmented matrix (3 equations, 5 unknowns):</p>
        <pre class='code-block'>[1  2  0  3  1 | 5]
[0  0  1  2  4 | 7]
[0  0  0  0  0 | 0]</pre>

        <p>Pivots are in columns 1 and 3. Free variables: x₂, x₄, x₅ (columns 2, 4, 5).</p>

        <p>Let x₂ = s, x₄ = u, x₅ = v (free parameters).</p>
        <p>Row 2: x₃ + 2x₄ + 4x₅ = 7 → x₃ + 2u + 4v = 7 → x₃ = 7 − 2u − 4v</p>
        <p>Row 1: x₁ + 2x₂ + 3x₄ + x₅ = 5 → x₁ + 2s + 3u + v = 5 → x₁ = 5 − 2s − 3u − v</p>

        <p><strong>Parametric solution:</strong></p>
        <pre class='code-block'>(x₁, x₂, x₃, x₄, x₅) = (5 − 2s − 3u − v, s, 7 − 2u − 4v, u, v)</pre>

        <p>The solution set is a 3-dimensional affine subspace.</p>
        </div>

        <div class='success-box'>
        <p><strong>Dimension of solution set:</strong> For a consistent system \(Ax = b\), the solution set has dimension \(n - \\text{rank}(A)\). Each additional free variable adds one dimension.</p>
        </div>
        """
    },
    {
        "title": "Solving Homogeneous Systems (Ax = 0)",
        "body": """
        <p>A homogeneous system Ax = 0 always has at least one solution (the trivial solution x = 0). Back substitution reveals the structure of all solutions.</p>

        <div class='concept-box'>
        <p><strong>Homogeneous systems:</strong> A system Ax = 0 (zero right-hand side) is always consistent because x = 0 is always a solution.</p>
        <ul>
        <li>If \(\\text{rank}(A) = n\) (full column rank), the only solution is \(x = 0\) (trivial).</li>
        <li>If \(\\text{rank}(A) < n\), there are infinitely many nontrivial solutions.</li>
        </ul>
        </div>

        <div class='worked-example'>
        <p><strong>Example: Homogeneous system with nontrivial solutions</strong></p>
        <p>Original system: x + 2y − z = 0, 2x + 4y − 2z = 0</p>
        <p>Augmented matrix (notice the zero column on the right):</p>
        <pre class='code-block'>[1  2  -1 | 0]
[2  4  -2 | 0]</pre>

        <p>Apply R₂ − 2R₁ → R₂:</p>
        <pre class='code-block'>[1  2  -1 | 0]
[0  0   0 | 0]</pre>

        <p>Rank = 1, variables = 3, so we have \(3 - 1 = 2\) free variables (\(y\) and \(z\)).</p>
        <p>Let y = s, z = t.</p>
        <p>Row 1: x + 2s − t = 0 → x = −2s + t</p>

        <p><strong>Solution (nullspace):</strong></p>
        <pre class='code-block'>(x, y, z) = (−2s + t, s, t) = s(−2, 1, 0) + t(1, 0, 1)</pre>

        <p>The solution set is spanned by vectors (−2, 1, 0) and (1, 0, 1). Any linear combination of these vectors is a solution to Ax = 0.</p>
        </div>

        <div class='success-box'>
        <p><strong>The nullspace:</strong> For a matrix \(A\), the nullspace is the solution set to \(Ax = 0\). It is a linear subspace of dimension \(n - \\text{rank}(A)\).</p>
        </div>
        """
    },
    {
        "title": "Algorithm Summary: From Matrix to Solution",
        "body": """
        <div class='concept-box'>
        <p><strong>Complete workflow:</strong></p>
        <ol>
        <li><strong>Form the augmented matrix:</strong> [A | b]</li>
        <li><strong>Gaussian elimination (forward pass):</strong> Reduce to REF using EROs.</li>
        <li><strong>Check consistency:</strong> If there is a row \([0\ 0\ \ldots\ 0\ |\ c]\) with \(c \\neq 0\), the system is inconsistent (stop).</li>
        <li><strong>Identify free variables:</strong> Variables corresponding to non-pivot columns are free.</li>
        <li><strong>Back substitution:</strong> Starting from the last nonzero row, solve for each pivot variable in terms of free variables.</li>
        <li><strong>Express the solution:</strong> Either as a unique solution, a parametric family, or "no solution."</li>
        </ol>
        </div>

        <div class='worked-example'>
        <p><strong>Complete example: 3×3 system</strong></p>
        <p>System: x + y + z = 3, 2x + y + 3z = 8, x − y + 2z = 4</p>

        <p><strong>Step 1: Augmented matrix</strong></p>
        <pre class='code-block'>[1  1  1 | 3]
[2  1  3 | 8]
[1 -1  2 | 4]</pre>

        <p><strong>Step 2: Gaussian elimination (REF)</strong></p>
        <p>R₂ − 2R₁ → R₂, R₃ − R₁ → R₃:</p>
        <pre class='code-block'>[1  1  1 | 3]
[0 -1  1 | 2]
[0 -2  1 | 1]</pre>

        <p>R₃ − 2R₂ → R₃:</p>
        <pre class='code-block'>[1  1  1 | 3]
[0 -1  1 | 2]
[0  0 -1 | -3]</pre>

        <p><strong>Step 3: Check consistency</strong> No row \([0\ 0\ 0\ |\ c]\) with \(c \\neq 0\), so the system is consistent.</p>

        <p><strong>Step 4: Identify free variables</strong> Pivots in columns 1, 2, 3. All variables are pivot variables (no free variables).</p>

        <p><strong>Step 5: Back substitution</strong></p>
        <p>Row 3: −z = −3 → z = 3</p>
        <p>Row 2: −y + z = 2 → −y + 3 = 2 → y = 1</p>
        <p>Row 1: x + y + z = 3 → x + 1 + 3 = 3 → x = −1</p>

        <p><strong>Solution:</strong> (x, y, z) = (−1, 1, 3)</p>
        </div>

        <div class='success-box'>
        <p>This workflow applies to any size system: small or large, determined or underdetermined, consistent or inconsistent.</p>
        </div>
        """
    }
]
