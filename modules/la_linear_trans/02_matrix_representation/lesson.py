TITLE = "Matrix Representation of Linear Transformations"

SECTIONS = [
    {
        "title": "Finding Matrix Representations",
        "body": """
        <div class='concept-box'>
        <p><strong>Key insight:</strong> Every linear transformation T: ℝⁿ → ℝᵐ can be represented by an m × n matrix A such that T(x) = Ax.</p>

        <p><strong>Construction:</strong> If T: ℝⁿ → ℝᵐ is linear, apply T to each standard basis vector eⱼ and stack the results as columns:</p>
        <pre class='code-block'>A = [T(e₁) | T(e₂) | ... | T(eₙ)]</pre>

        <p>This is a column-stacked matrix where the j-th column is T(eⱼ).</p>
        </div>
        """
    },
    {
        "title": "Matrix Representation with General Bases",
        "body": """
        <div class='concept-box'>
        <p><strong>Definition:</strong> If T: V → W and B = {v₁, ..., vₙ} is a basis for V, B' = {w₁, ..., wₘ} is a basis for W, then the matrix representation [T]_B'^B is:</p>
        <pre class='code-block'>[T]_B'^B = [[T(v₁)]_{B'} | [T(v₂)]_{B'} | ... | [T(vₙ)]_{B'}]</pre>

        <p>Each column is the coordinate vector of T(vⱼ) with respect to the basis B'.</p>

        <p><strong>Relationship to coordinates:</strong> For v ∈ V with coordinates [v]_B and T(v) ∈ W with coordinates [T(v)]_{B'}:</p>
        <pre class='code-block'>[T(v)]_{B'} = [T]_B'^B [v]_B</pre>
        </div>
        """
    },
    {
        "title": "Examples",
        "body": """
        <div class='worked-example'>
        <p><strong>Example 1: Standard basis representation</strong></p>
        <p><strong>Find matrix representation of T(x, y) = (2x - y, x + y)</strong></p>
        <pre class='code-block'>T(e₁) = T(1, 0) = (2·1 - 0, 1 + 0) = (2, 1)
T(e₂) = T(0, 1) = (2·0 - 1, 0 + 1) = (-1, 1)

A = [2  -1]
    [1   1]

Verify: A[x, y]ᵀ = [2x - y, x + y]ᵀ = T(x, y) ✓</pre>

        <p><strong>Example 2: Non-standard basis representation</strong></p>
        <pre class='code-block'>V = ℝ² with basis B = {v₁ = [1, 0], v₂ = [1, 1]}
W = ℝ² with basis B' = {w₁ = [1, 1], w₂ = [0, 1]}
T(x, y) = (2x - y, x + y)

T(v₁) = T(1, 0) = (2, 1). Express in B':
(2, 1) = a(1, 1) + b(0, 1) → a = 2, b = -1. [T(v₁)]_{B'} = [2, -1]ᵀ

T(v₂) = T(1, 1) = (1, 2). Express in B':
(1, 2) = a(1, 1) + b(0, 1) → a = 1, b = 1. [T(v₂)]_{B'} = [1, 1]ᵀ

[T]_B'^B = [2  1]
           [-1 1]</pre>
        </div>
        """
    },
    {
        "title": "Similarity and Change of Basis",
        "body": """
        <div class='concept-box'>
        <p><strong>Change of basis for linear operators:</strong> If T: V → V is a linear operator and P is the change of basis matrix from B to B', then:</p>
        <pre class='code-block'>[T]_{B'} = P⁻¹ [T]_B P</pre>

        <p>This shows how the matrix representation changes when the basis changes (similarity transformation). The matrices [T]_B and [T]_{B'} represent the same transformation in different bases.</p>
        </div>
        """
    }
]
