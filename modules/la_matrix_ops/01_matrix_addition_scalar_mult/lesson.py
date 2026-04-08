TITLE = "Matrix Addition and Scalar Multiplication"

SECTIONS = [
    {
        "title": "Foundational Concepts",
        "body": """
        <div class="concept-box">
        <p><strong>Matrix Addition:</strong> Two matrices \\(\\mathbf{A}\\) and \\(\\mathbf{B}\\) of the same dimensions (m × n) can be added element-wise to produce a matrix \\(\\mathbf{C}\\) of the same dimension:</p>
        <p>$$\\text{If } \\mathbf{A} = [a_{ij}] \\text{ and } \\mathbf{B} = [b_{ij}], \\text{ then } \\mathbf{C} = \\mathbf{A} + \\mathbf{B} = [a_{ij} + b_{ij}]$$</p>
        </div>

        <p><strong>Properties of matrix addition:</strong></p>
        <ul>
        <li><strong>Commutative:</strong> \\(\\mathbf{A} + \\mathbf{B} = \\mathbf{B} + \\mathbf{A}\\)</li>
        <li><strong>Associative:</strong> \\((\\mathbf{A} + \\mathbf{B}) + \\mathbf{C} = \\mathbf{A} + (\\mathbf{B} + \\mathbf{C})\\)</li>
        <li><strong>Identity element:</strong> \\(\\mathbf{A} + \\mathbf{0} = \\mathbf{A}\\)</li>
        <li><strong>Inverse element:</strong> \\(\\mathbf{A} + (-\\mathbf{A}) = \\mathbf{0}\\)</li>
        </ul>

        <div class="concept-box">
        <p><strong>Scalar Multiplication:</strong> Multiplying a matrix \\(\\mathbf{A}\\) by a scalar \\(c\\) produces a matrix where every element is multiplied by \\(c\\):</p>
        <p>$$c\\mathbf{A} = [c \\cdot a_{ij}]$$</p>
        </div>

        <p><strong>Properties of scalar multiplication:</strong></p>
        <ul>
        <li><strong>Distributive over addition (matrices):</strong> \\(c(\\mathbf{A} + \\mathbf{B}) = c\\mathbf{A} + c\\mathbf{B}\\)</li>
        <li><strong>Distributive over addition (scalars):</strong> \\((c + d)\\mathbf{A} = c\\mathbf{A} + d\\mathbf{A}\\)</li>
        <li><strong>Associative:</strong> \\((cd)\\mathbf{A} = c(d\\mathbf{A})\\)</li>
        <li><strong>Identity:</strong> \\(1\\mathbf{A} = \\mathbf{A}\\)</li>
        </ul>
        """
    },
    {
        "title": "Worked Examples",
        "body": """
        <div class="worked-example">
        <p><strong>Example 1: Matrix Addition</strong></p>
        <p>$$\\mathbf{A} = \\begin{pmatrix} 1 & 2 \\\\ 4 & 5 \\end{pmatrix}, \\quad \\mathbf{B} = \\begin{pmatrix} 3 & 0 \\\\ 2 & 1 \\end{pmatrix}$$</p>
        <p>$$\\mathbf{A} + \\mathbf{B} = \\begin{pmatrix} 1+3 & 2+0 \\\\ 4+2 & 5+1 \\end{pmatrix} = \\begin{pmatrix} 4 & 2 \\\\ 6 & 6 \\end{pmatrix}$$</p>
        </div>

        <div class="worked-example">
        <p><strong>Example 2: Scalar Multiplication</strong></p>
        <p>$$2\\mathbf{A} = \\begin{pmatrix} 2 \\cdot 1 & 2 \\cdot 2 \\\\ 2 \\cdot 4 & 2 \\cdot 5 \\end{pmatrix} = \\begin{pmatrix} 2 & 4 \\\\ 8 & 10 \\end{pmatrix}$$</p>
        </div>

        <div class="worked-example">
        <p><strong>Example 3: Combined Operations</strong></p>
        <p>$$\\mathbf{A} + 2\\mathbf{B} = \\begin{pmatrix} 1 & 2 \\\\ 4 & 5 \\end{pmatrix} + \\begin{pmatrix} 6 & 0 \\\\ 4 & 2 \\end{pmatrix} = \\begin{pmatrix} 7 & 2 \\\\ 8 & 7 \\end{pmatrix}$$</p>
        </div>

        <div class="success-box">
        <p><strong>Verification:</strong> You can always verify addition by checking each element individually. For \\(2\\mathbf{B}\\) above: \\(2 \\cdot 3 = 6\\), \\(2 \\cdot 0 = 0\\), \\(2 \\cdot 2 = 4\\), \\(2 \\cdot 1 = 2\\) ✓</p>
        </div>
        """
    },
    {
        "title": "Vector Spaces and Structure",
        "body": """
        <div class="concept-box">
        <p><strong>Vector Space of Matrices:</strong> The set of all \\(m \\times n\\) matrices with addition and scalar multiplication forms a vector space. This is fundamental to linear algebra—it allows us to apply all vector space concepts (subspaces, span, linear independence, etc.) to matrices.</p>
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
