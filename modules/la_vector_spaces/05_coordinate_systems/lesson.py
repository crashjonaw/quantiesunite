TITLE = "Coordinate Systems and Change of Basis"

SECTIONS = [
    {
        "title": "Coordinates with Respect to a Basis",
        "body": """
        <p><strong>Motivation:</strong> Once we fix a basis, every vector can be uniquely represented as a list of coordinates.</p>

        <div class='concept-box'>
        <p>If $\\mathcal{B} = \\{\\mathbf{v}_1, \\mathbf{v}_2, \\ldots, \\mathbf{v}_n\\}$ is a basis for $V$ and $\\mathbf{v} \\in V$, then the unique representation</p>
        <p>$$\\mathbf{v} = c_1 \\mathbf{v}_1 + c_2 \\mathbf{v}_2 + \\cdots + c_n \\mathbf{v}_n$$</p>
        <p>defines the <strong>coordinate vector</strong> of $\\mathbf{v}$ with respect to $\\mathcal{B}$:</p>
        <p>$$[\\mathbf{v}]_{\\mathcal{B}} = [c_1, c_2, \\ldots, c_n]^T$$</p>
        </div>

        <p><strong>Key Properties:</strong></p>
        <ul>
        <li>Each vector in $V$ corresponds to exactly one coordinate vector in $F^n$</li>
        <li>The correspondence preserves addition: $[\\mathbf{u} + \\mathbf{v}]_{\\mathcal{B}} = [\\mathbf{u}]_{\\mathcal{B}} + [\\mathbf{v}]_{\\mathcal{B}}$</li>
        <li>The correspondence preserves scalar multiplication: $[c\\mathbf{u}]_{\\mathcal{B}} = c[\\mathbf{u}]_{\\mathcal{B}}$</li>
        </ul>

        <p><strong>This is an isomorphism:</strong> The vector space $V$ with basis $\\mathcal{B}$ is "the same as" $F^n$ when viewed through coordinates.</p>

        <div class='worked-example'>
        <p><strong>Example 1: Standard Basis</strong></p>
        <p>In $\\mathbb{R}^3$ with standard basis $\\mathcal{B} = \\{\\mathbf{e}_1, \\mathbf{e}_2, \\mathbf{e}_3\\}$:</p>
        <p>The vector $\\mathbf{v} = [5, -2, 7]$ equals $5\\mathbf{e}_1 + (-2)\\mathbf{e}_2 + 7\\mathbf{e}_3$.</p>
        <p>Coordinates: $[\\mathbf{v}]_{\\mathcal{B}} = [5, -2, 7]^T$ (same as $\\mathbf{v}$ itself)</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example 2: Non-Standard Basis</strong></p>
        <p>In $\\mathbb{R}^2$ with basis $\\mathcal{B} = \\{\\mathbf{v}_1 = [1, 1], \\mathbf{v}_2 = [1, -1]\\}$:</p>
        <p>Find coordinates of $\\mathbf{u} = [3, 1]$.</p>
        <p>We need $c_1, c_2$ such that:</p>
        <pre class='code-block'>$c_1[1, 1] + c_2[1, -1] = [3, 1]$
$[c_1 + c_2,\\; c_1 - c_2] = [3, 1]$</pre>
        <p>From the equations:</p>
        <pre class='code-block'>$c_1 + c_2 = 3$
$c_1 - c_2 = 1$</pre>
        <p>Solving: $2c_1 = 4$, so $c_1 = 2$; then $c_2 = 1$.</p>
        <p>Coordinates: $[\\mathbf{u}]_{\\mathcal{B}} = [2, 1]^T$</p>
        <p><strong>Verification:</strong> $2[1, 1] + 1[1, -1] = [2, 2] + [1, -1] = [3, 1]$ ✓</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example 3: Polynomial Space</strong></p>
        <p>In $P_2(\\mathbb{R})$ with basis $\\mathcal{B} = \\{1, x, x^2\\}$:</p>
        <p>The polynomial $p(x) = 2 + 3x - x^2$ has coordinates $[p]_{\\mathcal{B}} = [2, 3, -1]^T$</p>
        </div>
        """
    },
    {
        "title": "Change of Basis Formula",
        "body": """
        <p><strong>Problem:</strong> We know $\\mathbf{v}$'s coordinates in basis $\\mathcal{B}$. What are its coordinates in basis $\\mathcal{B}'$?</p>

        <div class='concept-box'>
        <p><strong>Change of Basis Matrix:</strong> If $\\mathcal{B}$ and $\\mathcal{B}'$ are two bases for $V$, the <strong>change of basis matrix</strong> $P$ from $\\mathcal{B}$ to $\\mathcal{B}'$ is constructed as:</p>
        <p>$$P = \\big[[\\mathbf{v}_1']_{\\mathcal{B}} \\;|\\; [\\mathbf{v}_2']_{\\mathcal{B}} \\;|\\; \\cdots \\;|\\; [\\mathbf{v}_n']_{\\mathcal{B}}\\big]$$</p>
        <p>where $[\\mathbf{v}_i']_{\\mathcal{B}}$ is the coordinate vector of the $i$-th basis vector of $\\mathcal{B}'$ expressed in basis $\\mathcal{B}$.</p>
        </div>

        <p><strong>The Change of Basis Formula:</strong></p>
        <div class='success-box'>
        <p>If $P$ is the change of basis matrix from $\\mathcal{B}$ to $\\mathcal{B}'$, then:</p>
        <p>$$[\\mathbf{v}]_{\\mathcal{B}'} = P^{-1}[\\mathbf{v}]_{\\mathcal{B}}$$</p>
        <p>Equivalently:</p>
        <p>$$[\\mathbf{v}]_{\\mathcal{B}} = P[\\mathbf{v}]_{\\mathcal{B}'}$$</p>
        </div>

        <p><strong>Interpretation:</strong> $P^{-1}$ transforms coordinates in $\\mathcal{B}$ to coordinates in $\\mathcal{B}'$.</p>

        <div class='worked-example'>
        <p><strong>Example: Change of Basis in $\\mathbb{R}^2$</strong></p>
        <p>Standard basis: $\\mathcal{B} = \\{\\mathbf{e}_1 = [1, 0], \\mathbf{e}_2 = [0, 1]\\}$</p>
        <p>New basis: $\\mathcal{B}' = \\{\\mathbf{v}_1 = [1, 1], \\mathbf{v}_2 = [1, -1]\\}$</p>

        <p><strong>Step 1: Express $\\mathcal{B}'$ vectors in $\\mathcal{B}$ coordinates</strong></p>
        <pre class='code-block'>$[\\mathbf{v}_1]_{\\mathcal{B}} = [1, 1]^T$
$[\\mathbf{v}_2]_{\\mathcal{B}} = [1, -1]^T$</pre>

        <p><strong>Step 2: Construct change of basis matrix $P$</strong></p>
        <p>$$P = \\begin{bmatrix} 1 & 1 \\\\ 1 & -1 \\end{bmatrix}$$</p>

        <p><strong>Step 3: Compute $P^{-1}$</strong></p>
        <pre class='code-block'>$\\det(P) = -1 - 1 = -2$
$$P^{-1} = \\frac{1}{-2} \\begin{bmatrix} -1 & -1 \\\\ -1 & 1 \\end{bmatrix} = \\begin{bmatrix} 1/2 & 1/2 \\\\ 1/2 & -1/2 \\end{bmatrix}$$</pre>

        <p><strong>Step 4: Transform coordinates</strong></p>
        <p>For $\\mathbf{u} = [3, 1]$ with $[\\mathbf{u}]_{\\mathcal{B}} = [3, 1]^T$:</p>
        <p>$$[\\mathbf{u}]_{\\mathcal{B}'} = P^{-1}[\\mathbf{u}]_{\\mathcal{B}} = \\begin{bmatrix} 1/2 & 1/2 \\\\ 1/2 & -1/2 \\end{bmatrix} \\begin{bmatrix} 3 \\\\ 1 \\end{bmatrix} = \\begin{bmatrix} 2 \\\\ 1 \\end{bmatrix}$$</p>

        <p><strong>Verification:</strong> In basis $\\mathcal{B}'$, $\\mathbf{u} = 2\\mathbf{v}_1 + 1\\mathbf{v}_2 = 2[1,1] + 1[1,-1] = [3, 1]$ ✓</p>
        </div>
        """
    },
    {
        "title": "Properties and Applications of Change of Basis",
        "body": """
        <p><strong>Important Property: Composition of Changes</strong></p>
        <p>If $P_1$ is the matrix from $\\mathcal{B}$ to $\\mathcal{B}'$ and $P_2$ is the matrix from $\\mathcal{B}'$ to $\\mathcal{B}''$, then the matrix from $\\mathcal{B}$ to $\\mathcal{B}''$ is:</p>
        <p>$$P_1 P_2 = (\\text{change from } \\mathcal{B} \\text{ to } \\mathcal{B}'') = (\\text{change from } \\mathcal{B} \\text{ to } \\mathcal{B}') \\circ (\\text{change from } \\mathcal{B}' \\text{ to } \\mathcal{B}'')$$</p>

        <p><strong>Matrix Similarity:</strong> If $A$ is a matrix representing a linear transformation in basis $\\mathcal{B}$, and we change to basis $\\mathcal{B}'$, the matrix becomes:</p>
        <p>$$A' = P^{-1}AP$$</p>
        <p>where $P$ is the change of basis matrix. We say $A$ and $A'$ are <strong>similar matrices</strong>.</p>

        <p><strong>Key Applications:</strong></p>

        <div class='success-box'>
        <p><strong>1. Diagonalization</strong></p>
        <p>If we choose $\\mathcal{B}'$ to be the basis of eigenvectors, then in this basis the matrix becomes diagonal:</p>
        <p>$$A' = \\begin{bmatrix} \\lambda_1 & 0 & \\cdots & 0 \\\\ 0 & \\lambda_2 & \\cdots & 0 \\\\ \\vdots & & \\ddots & \\vdots \\\\ 0 & 0 & \\cdots & \\lambda_n \\end{bmatrix}$$</p>
        <p>This makes matrix powers and exponentials easy to compute.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example of Diagonalization Benefit:</strong></p>
        <p>Computing $A^{100}$ is hard in standard basis but easy if $A'$ is diagonal:</p>
        <pre class='code-block'>$A^{100} = P(A')^{100} P^{-1}$
$$(A')^{100} = \\begin{bmatrix} \\lambda_1^{100} & 0 \\\\ 0 & \\lambda_2^{100} \\end{bmatrix}$$</pre>
        </div>

        <div class='success-box'>
        <p><strong>2. Simplification of Computations</strong></p>
        <p>Some bases make specific problems easier:</p>
        <ul>
        <li><strong>Orthonormal bases:</strong> Projections become simple (just dot products)</li>
        <li><strong>Eigenvector bases:</strong> Matrix diagonalizes</li>
        <li><strong>Problem-specific bases:</strong> Exploit structure in your problem</li>
        </ul>
        </div>

        <div class='success-box'>
        <p><strong>3. Principal Component Analysis (PCA)</strong></p>
        <p>In data science, we change to the basis of eigenvectors of the covariance matrix, revealing the directions of maximum variance in data.</p>
        </div>

        <p><strong>Geometric Interpretation:</strong></p>
        <p>Changing basis is like rotating your coordinate system. The same geometric object looks different in different coordinate systems, but the underlying space structure remains the same.</p>
        """
    },
    {
        "title": "Computing Change of Basis Matrices",
        "body": """
        <p><strong>Efficient Method: Augmented Matrix</strong></p>

        <p>To find the change of basis matrix from $\\mathcal{B}$ to $\\mathcal{B}'$:</p>
        <ol>
        <li>Create an augmented matrix with $\\mathcal{B}$ vectors on the left and $\\mathcal{B}'$ vectors on the right</li>
        <li>Row reduce until the left side becomes identity</li>
        <li>The right side is $P^{-1}$</li>
        </ol>

        <p><strong>Alternatively:</strong> Form matrix with $\\mathcal{B}$ vectors as columns, matrix with $\\mathcal{B}'$ vectors as columns, then:</p>
        <p>$$P = [\\text{matrix of } \\mathcal{B} \\text{ vectors}]^{-1} [\\text{matrix of } \\mathcal{B}' \\text{ vectors}]$$</p>

        <div class='worked-example'>
        <p><strong>Example: Compute Change Matrix</strong></p>
        <p>In $\\mathbb{R}^3$, find change of basis matrix from $\\mathcal{B} = \\{[1, 0, 0], [0, 1, 0], [0, 0, 1]\\}$ to $\\mathcal{B}' = \\{[1, 1, 0], [0, 1, 1], [1, 0, 1]\\}$.</p>

        <p>Express $\\mathcal{B}'$ vectors in $\\mathcal{B}$:</p>
        <pre class='code-block'>$[1, 1, 0]^T = 1[1,0,0] + 1[0,1,0] + 0[0,0,1]$
$[0, 1, 1]^T = 0[1,0,0] + 1[0,1,0] + 1[0,0,1]$
$[1, 0, 1]^T = 1[1,0,0] + 0[0,1,0] + 1[0,0,1]$</pre>

        <p>Change of basis matrix:</p>
        <p>$$P = \\begin{bmatrix} 1 & 0 & 1 \\\\ 1 & 1 & 0 \\\\ 0 & 1 & 1 \\end{bmatrix}$$</p>

        <p>To find $P^{-1}$, use Gaussian elimination or Cramer's rule (omitted here for brevity).</p>
        </div>

        <p><strong>Quick Check:</strong> Verify $PP^{-1} = I$ to ensure correctness.</p>
        """
    }
]
