TITLE = "Gram-Schmidt Process"

SECTIONS = [
    {
        "title": "The Gram-Schmidt Algorithm",
        "body": """
        <p><strong>Problem:</strong> Given a linearly independent set $\\{\\mathbf{v}_1, \\mathbf{v}_2, \\ldots, \\mathbf{v}_n\\}$, construct an orthonormal set spanning the same space.</p>

        <p><strong>Solution:</strong> The Gram-Schmidt process orthogonalizes vectors step by step. For each vector, subtract its projections onto all previous vectors:</p>

        <div class='concept-box'>
        $$\\mathbf{w}_1 = \\mathbf{v}_1$$
        $$\\mathbf{w}_2 = \\mathbf{v}_2 - \\frac{\\mathbf{v}_2 \\cdot \\mathbf{w}_1}{||\\mathbf{w}_1||^2}\\mathbf{w}_1$$
        $$\\mathbf{w}_3 = \\mathbf{v}_3 - \\frac{\\mathbf{v}_3 \\cdot \\mathbf{w}_1}{||\\mathbf{w}_1||^2}\\mathbf{w}_1 - \\frac{\\mathbf{v}_3 \\cdot \\mathbf{w}_2}{||\\mathbf{w}_2||^2}\\mathbf{w}_2$$
        $$\\vdots$$
        $$\\mathbf{w}_k = \\mathbf{v}_k - \\sum_{j=1}^{k-1} \\frac{\\mathbf{v}_k \\cdot \\mathbf{w}_j}{||\\mathbf{w}_j||^2}\\mathbf{w}_j$$
        </div>

        <p>Then normalize: $\\mathbf{u}_k = \\frac{\\mathbf{w}_k}{||\\mathbf{w}_k||}$ to get orthonormal vectors.</p>

        <p><strong>Intuition:</strong> At each step, we "remove" the component of $\\mathbf{v}_k$ that lies in the span of previous vectors. What remains is orthogonal to all previous vectors.</p>

        <p><strong>Algorithm (Pseudocode):</strong></p>
        <pre>for k = 1 to n:
    w_k = v_k
    for j = 1 to k-1:
        w_k = w_k - (v_k · u_j) u_j  // subtract projection onto u_j
    u_k = w_k / ||w_k||  // normalize
return {u_1, u_2, ..., u_n}</pre>

        <p><strong>Note:</strong> Gram-Schmidt assumes the input vectors are linearly independent. If a vector is dependent on previous ones, it will have zero norm when orthogonalized, signaling linear dependence.</p>

        <div class='worked-example'>
        <p><strong>Example:</strong> Orthonormalize $\\mathbf{v}_1 = [1, 0]$, $\\mathbf{v}_2 = [1, 1]$ in $\\mathbb{R}^2$.</p>
        <pre>Step 1: w₁ = [1, 0]
        u₁ = [1, 0] / ||[1, 0]|| = [1, 0] / 1 = [1, 0]

Step 2: w₂ = [1, 1] - ([1, 1] · [1, 0])[1, 0]
             = [1, 1] - 1·[1, 0]
             = [1, 1] - [1, 0]
             = [0, 1]
        u₂ = [0, 1] / ||[0, 1]|| = [0, 1] / 1 = [0, 1]

Orthonormal basis: {[1, 0], [0, 1]}</pre>
        </div>
        """
    },
    {
        "title": "QR Decomposition",
        "body": """
        <p><strong>Theorem (QR Decomposition):</strong> Any $m \\times n$ matrix $A$ with linearly independent columns can be factored as:</p>

        <div class='concept-box'>
        $$A = QR$$
        </div>

        <p>where:</p>
        <ul>
        <li>$Q$ is $m \\times n$ with orthonormal columns</li>
        <li>$R$ is $n \\times n$ upper triangular with positive diagonal entries</li>
        </ul>

        <p><strong>Computing QR via Gram-Schmidt:</strong></p>
        <ol>
        <li>Apply Gram-Schmidt to the columns of $A$ to get orthonormal vectors $\\mathbf{u}_1, \\ldots, \\mathbf{u}_n$</li>
        <li>The orthonormal vectors form the columns of $Q$</li>
        <li>The entries of $R$ are projections: $R_{ij} = \\mathbf{a}_i \\cdot \\mathbf{u}_j$ for $i \\leq j$, and $R_{ij} = 0$ for $i > j$</li>
        </ol>

        <p><strong>Why QR is Important:</strong></p>
        <ul>
        <li><strong>Numerical stability:</strong> QR is more stable than computing $A^T A$ explicitly</li>
        <li><strong>Least squares:</strong> Solves $A\\mathbf{x} = \\mathbf{b}$ efficiently via $R\\mathbf{x} = Q^T\\mathbf{b}$</li>
        <li><strong>Eigenvalue algorithms:</strong> QR iteration is the foundation for eigenvalue computations</li>
        <li><strong>Rank detection:</strong> The diagonal of $R$ reveals the rank</li>
        </ul>

        <div class='worked-example'>
        <p><strong>Example:</strong> QR decomposition of $A = \\begin{bmatrix} 1 & 1 \\\\ 0 & 1 \\\\ 0 & 0 \\end{bmatrix}$.</p>
        <pre>Columns: a₁ = [1, 0, 0], a₂ = [1, 1, 0]

Gram-Schmidt:\\nu₁ = [1, 0, 0]  (already unit)\\nu₂ = [1, 1, 0] - (1)[1, 0, 0] = [0, 1, 0]

Q = [1  0]
    [0  1]
    [0  0]

R: R₁₁ = a₁·u₁ = 1
   R₁₂ = a₂·u₁ = 1
   R₂₂ = a₂·u₂ = 1

R = [1  1]
    [0  1]

Verify: QR = [1  0][1  1] = [1  1] = A ✓
            [0  1][0  1]   [0  1]
            [0  0]         [0  0]</pre>
        </div>

        <div class='success-box'>
        <p><strong>Takeaway:</strong> QR decomposition transforms a general linear system into a simpler triangular one while maintaining mathematical structure through orthogonality.</p>
        </div>
        """
    },
    {
        "title": "Stability and Modified Gram-Schmidt",
        "body": """
        <p><strong>Numerical Stability Issue:</strong> Classical Gram-Schmidt can suffer from numerical errors, especially when vectors are nearly linearly dependent. Rounding errors accumulate.</p>

        <p><strong>Modified Gram-Schmidt (MGS):</strong> A more numerically stable variant reorders operations:</p>

        <pre>for j = 1 to n:
    u_j = v_j
    for i = 1 to j-1:
        u_j = u_j - (u_j · u_i) u_i  // subtract projection iteratively
    u_j = u_j / ||u_j||</pre>

        <p>Instead of computing all projections at once, MGS subtracts them one by one. This reduces error accumulation in finite precision arithmetic.</p>

        <p><strong>Practical Guidance:</strong></p>
        <ul>
        <li><strong>Classical GS:</strong> Simple to understand, good for theory and hand calculations</li>
        <li><strong>Modified GS:</strong> Use in practical numerical code (better numerical stability)</li>
        <li><strong>Householder reflections:</strong> Even more stable for QR decomposition in production software</li>
        </ul>

        <div class='warning-box'>
        <p><strong>Warning:</strong> Never implement Gram-Schmidt naively in production code without considering numerical stability. Libraries like LAPACK use more sophisticated methods (Householder reflections, Givens rotations) that are more stable.</p>
        </div>

        <p><strong>Summary:</strong> While classical Gram-Schmidt teaches the concept clearly, be aware of numerical issues in practice. Modified Gram-Schmidt is a simple improvement, but professional libraries use even more advanced techniques.</p>
        """
    }
]
