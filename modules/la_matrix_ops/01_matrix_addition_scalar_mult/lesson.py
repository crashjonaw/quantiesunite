TITLE = "Matrix Addition and Scalar Multiplication"

SECTIONS = [
    {
        "title": "Foundational Concepts",
        "body": """
        <div class="concept-box">
        <p><strong>Matrix Addition:</strong> Two matrices A and B of the same dimensions (m × n) can be added element-wise to produce a matrix C of the same dimension:</p>
        <div class="code-block">If A = [aᵢⱼ] and B = [bᵢⱼ], then C = A + B = [aᵢⱼ + bᵢⱼ]</div>
        </div>

        <p><strong>Properties of matrix addition:</strong></p>
        <ul>
        <li><strong>Commutative:</strong> A + B = B + A</li>
        <li><strong>Associative:</strong> (A + B) + C = A + (B + C)</li>
        <li><strong>Identity element:</strong> A + 0 = A (where 0 is the zero matrix)</li>
        <li><strong>Inverse element:</strong> A + (-A) = 0</li>
        </ul>

        <div class="concept-box">
        <p><strong>Scalar Multiplication:</strong> Multiplying a matrix A by a scalar c produces a matrix where every element is multiplied by c:</p>
        <div class="code-block">cA = [caᵢⱼ]</div>
        </div>

        <p><strong>Properties of scalar multiplication:</strong></p>
        <ul>
        <li><strong>Distributive over addition (matrices):</strong> c(A + B) = cA + cB</li>
        <li><strong>Distributive over addition (scalars):</strong> (c + d)A = cA + dA</li>
        <li><strong>Associative:</strong> (cd)A = c(dA)</li>
        <li><strong>Identity:</strong> 1A = A</li>
        </ul>
        """
    },
    {
        "title": "Worked Examples",
        "body": """
        <div class="worked-example">
        <p><strong>Example 1: Matrix Addition</strong></p>
        <div class="code-block">A = [1  2]    B = [3  0]
    [4  5]        [2  1]

A + B = [1+3  2+0] = [4  2]
        [4+2  5+1]   [6  6]</div>
        </div>

        <div class="worked-example">
        <p><strong>Example 2: Scalar Multiplication</strong></p>
        <div class="code-block">2A = [2·1  2·2] = [2  4]
     [2·4  2·5]   [8 10]</div>
        </div>

        <div class="worked-example">
        <p><strong>Example 3: Combined Operations</strong></p>
        <div class="code-block">A + 2B = [1  2] + [6  0] = [7  2]
         [4  5]   [4  2]   [8  7]</div>
        </div>

        <div class="success-box">
        <p><strong>Verification:</strong> You can always verify addition by checking each element individually. For 2B above: 2·3=6, 2·0=0, 2·2=4, 2·1=2 ✓</p>
        </div>
        """
    },
    {
        "title": "Vector Spaces and Structure",
        "body": """
        <div class="concept-box">
        <p><strong>Vector Space of Matrices:</strong> The set of all m × n matrices with addition and scalar multiplication forms a vector space. This is fundamental to linear algebra—it allows us to apply all vector space concepts (subspaces, span, linear independence, etc.) to matrices.</p>
        </div>

        <p><strong>Key insight:</strong> Because matrices form a vector space under these operations, we can:</p>
        <ul>
        <li>Talk about subspaces of matrices</li>
        <li>Apply the concept of linear independence</li>
        <li>Discuss dimension and basis</li>
        <li>Use vector space theory to analyze matrix properties</li>
        </ul>

        <div class="success-box">
        <p><strong>First Principles:</strong> Matrix addition and scalar multiplication are the simplest operations on matrices. They preserve the structure needed to form a vector space, making matrices a powerful algebraic object for representing linear transformations.</p>
        </div>
        """
    }
]
