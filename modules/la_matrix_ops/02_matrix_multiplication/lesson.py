TITLE = "Matrix Multiplication"

SECTIONS = [
    {
        "title": "The Row-Column Rule",
        "body": """
        <div class="concept-box">
        <p><strong>Matrix Multiplication Definition:</strong> If \\(\\mathbf{A}\\) is \\(m \\times p\\) and \\(\\mathbf{B}\\) is \\(p \\times n\\), the product \\(\\mathbf{C} = \\mathbf{AB}\\) is an \\(m \\times n\\) matrix where:</p>
        <p>$$c_{ij} = \\sum_{k=1}^{p} a_{ik} b_{kj} \\quad \\text{(dot product of row } i \\text{ of } \\mathbf{A} \\text{ with column } j \\text{ of } \\mathbf{B}\\text{)}$$</p>
        </div>

        <p><strong>Key requirement:</strong> The number of columns in \\(\\mathbf{A}\\) must equal the number of rows in \\(\\mathbf{B}\\). If \\(\\mathbf{A}\\) is \\(m \\times p\\) and \\(\\mathbf{B}\\) is \\(p \\times n\\), then \\(\\mathbf{AB}\\) is \\(m \\times n\\).</p>

        <div class="warning-box">
        <p><strong>Dimension compatibility:</strong> You cannot multiply \\(\\mathbf{A}\\) and \\(\\mathbf{B}\\) unless \\(\\text{columns}(\\mathbf{A}) = \\text{rows}(\\mathbf{B})\\). For example, a \\(2 \\times 3\\) matrix can only multiply a \\(3 \\times n\\) matrix on the right.</p>
        </div>

        <div class="success-box">
        <p><strong>Geometric intuition:</strong> Each entry \\(c_{ij}\\) is the dot product of row \\(i\\) of \\(\\mathbf{A}\\) with column \\(j\\) of \\(\\mathbf{B}\\). This measures how "aligned" that row and column are.</p>
        </div>
        """
    },
    {
        "title": "Computation and Examples",
        "body": """
        <div class="worked-example">
        <p><strong>Example: \\(2 \\times 3\\) times \\(3 \\times 2\\) = \\(2 \\times 2\\)</strong></p>
        <p>$$\\mathbf{A} = \\begin{pmatrix} 1 & 2 & 3 \\\\ 6 & 7 & 8 \\end{pmatrix}, \\quad \\mathbf{B} = \\begin{pmatrix} 4 & 5 \\\\ 0 & 1 \\\\ 2 & 3 \\end{pmatrix}$$</p>
        <p>$$\\mathbf{C} = \\mathbf{AB} = \\begin{pmatrix} c_{11} & c_{12} \\\\ c_{21} & c_{22} \\end{pmatrix}$$</p>
        <p>\\(c_{11} = (1)(4) + (2)(0) + (3)(2) = 4 + 0 + 6 = 10\\)</p>
        <p>\\(c_{12} = (1)(5) + (2)(1) + (3)(3) = 5 + 2 + 9 = 16\\)</p>
        <p>\\(c_{21} = (6)(4) + (7)(0) + (8)(2) = 24 + 0 + 16 = 40\\)</p>
        <p>\\(c_{22} = (6)(5) + (7)(1) + (8)(3) = 30 + 7 + 24 = 61\\)</p>
        <p>$$\\mathbf{C} = \\begin{pmatrix} 10 & 16 \\\\ 40 & 61 \\end{pmatrix}$$</p>
        </div>

        <p><strong>Properties of matrix multiplication:</strong></p>
        <ul>
        <li><strong>Associative:</strong> \\((\\mathbf{AB})\\mathbf{C} = \\mathbf{A}(\\mathbf{BC})\\)</li>
        <li><strong>Distributive (left):</strong> \\(\\mathbf{A}(\\mathbf{B} + \\mathbf{C}) = \\mathbf{AB} + \\mathbf{AC}\\)</li>
        <li><strong>Distributive (right):</strong> \\((\\mathbf{A} + \\mathbf{B})\\mathbf{C} = \\mathbf{AC} + \\mathbf{BC}\\)</li>
        <li><strong>NOT commutative:</strong> Generally \\(\\mathbf{AB} \\neq \\mathbf{BA}\\) (even if both products are defined)</li>
        <li><strong>Identity:</strong> \\(\\mathbf{I}_m \\mathbf{A} = \\mathbf{A} = \\mathbf{A} \\mathbf{I}_n\\)</li>
        </ul>
        """
    },
    {
        "title": "Complexity and Computational Considerations",
        "body": """
        <div class="concept-box">
        <p><strong>Computational complexity:</strong> Multiplying an \\(m \\times p\\) matrix by a \\(p \\times n\\) matrix requires \\(mnp\\) scalar multiplications. For square matrices, this is \\(O(n^3)\\).</p>
        </div>

        <p><strong>Advanced algorithms:</strong> Strassen's algorithm achieves \\(O(n^{2.807})\\), but is rarely used in practice due to implementation complexity and memory overhead.</p>

        <div class="success-box">
        <p><strong>Practical insight:</strong> For most applications, standard \\(O(n^3)\\) multiplication is sufficient. Modern computational libraries (LAPACK, NumPy) are heavily optimized for matrix multiplication, achieving near-peak hardware performance.</p>
        </div>
        """
    },
    {
        "title": "First Principles: Why This Definition?",
        "body": """
        <div class="concept-box">
        <p><strong>Why this row-column multiplication?</strong> Matrix multiplication is defined this way because it represents composition of linear transformations. If \\(\\mathbf{A}\\) transforms \\(\\mathbf{v} \\to \\mathbf{w}\\) and \\(\\mathbf{B}\\) transforms \\(\\mathbf{w} \\to \\mathbf{z}\\), then \\(\\mathbf{BA}\\) transforms \\(\\mathbf{v} \\to \\mathbf{z}\\) directly.</p>
        </div>

        <p>The dot product (\\(\\sum a_{ik} b_{kj}\\)) emerges naturally from this composition requirement, making matrix multiplication consistent with the algebraic structure of linear maps.</p>

        <div class="success-box">
        <p><strong>Key takeaway:</strong> Matrix multiplication isn't arbitrary—it's defined to perfectly capture the composition of linear transformations, which is one of the most important operations in mathematics and physics.</p>
        </div>
        """
    }
]
