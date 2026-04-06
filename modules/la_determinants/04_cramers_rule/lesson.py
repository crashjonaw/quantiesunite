TITLE = "Cramer's Rule"

SECTIONS = [
    {
        "title": "Statement and Usage of Cramer's Rule",
        "body": """
        <p><strong>Cramer's Rule:</strong> For a system Ax = b where A is n × n and \(det(A) \neq 0\) (unique solution), the solution is:</p>
        <pre class='code-block'>\(x_j = det(A_j) / det(A)\)</pre>

        <p>where \(A_j\) is the matrix obtained by replacing the j-th column of A with the vector b.</p>

        <p><strong>When to use Cramer's Rule:</strong></p>
        <ul>
        <li><strong>Advantage:</strong> Elegant formula; useful for theoretical work and small systems (\(n \leq 3\)).</li>
        <li><strong>Disadvantage:</strong> Computationally expensive for large \(n\) (requires \(n+1\) determinant computations). Gaussian elimination is \(O(n^3)\) vs. Cramer's \(O(n!)\) with cofactor expansion.</li>
        </ul>

        <div class='concept-box'>
        <p><strong>Cramer's Rule Summary:</strong></p>
        <p>For Ax = b with \(det(A) \neq 0\):</p>
        <p>\(x_j = det(A_j) / det(A)\), where \(A_j\) is A with column j replaced by b.</p>
        </div>
        """
    },
    {
        "title": "Worked Example",
        "body": """
        <div class='worked-example'>
        <p><strong>Example: Solve using Cramer's Rule</strong></p>
        <pre class='code-block'>System: 2x + y = 5
        x - y = 1

A = [2  1]    b = [5]
    [1 -1]        [1]

det(A) = 2(-1) - 1(1) = -3

A₁ (replace column 1 with b):
A₁ = [5  1]
     [1 -1]
det(A₁) = 5(-1) - 1(1) = -6

x = det(A₁)/det(A) = -6/(-3) = 2

A₂ (replace column 2 with b):
A₂ = [2  5]
     [1  1]
det(A₂) = 2(1) - 5(1) = -3

y = det(A₂)/det(A) = -3/(-3) = 1

Solution: (x, y) = (2, 1)</pre>
        </div>
        """
    }
]
