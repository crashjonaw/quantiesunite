"""Eigenvalues & Eigenvectors — Concept 2: Finding Eigenvalues

TITLE: The Characteristic Equation — Finding Eigenvalues
"""

TITLE = "The Characteristic Equation — Finding Eigenvalues"

SECTIONS = [
    {
        "title": "Derivation: From Av = λv to det(A - λI) = 0",
        "body": """
<p style=';'>Starting with the eigenvector equation:</p>

<div class='worked-example' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p style='font-family: monospace;'>Av = λv</p>
  <p>Rewrite as:</p>
  <p style='font-family: monospace;'>Av - λv = 0</p>
  <p style='font-family: monospace;'>Av - λIv = 0  (multiply λ by identity matrix)</p>
  <p style='font-family: monospace;'>(A - λI)v = 0</p>
</div>

<p style=';'>For a non-zero solution <strong>v</strong> to exist, the matrix (A - λI) must be <strong>singular</strong> (non-invertible):</p>

<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>The Characteristic Equation:</strong></p>
  <p style='font-family: monospace; font-size: 18px;'><strong>det(A - λI) = 0</strong></p>
  <p>Solving this polynomial equation gives all eigenvalues λ₁, λ₂, …</p>
</div>
"""
    },
    {
        "title": "Computing a 2×2 example",
        "body": """
<p style=';'>Find the eigenvalues of:</p>

<div class='worked-example' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p style='font-family: monospace;'>A = [[2, 1], [1, 2]]</p>

  <p><strong>Step 1: Form (A - λI)</strong></p>
  <p style='font-family: monospace;'>A - λI = [[2-λ, 1], [1, 2-λ]]</p>

  <p><strong>Step 2: Compute the determinant</strong></p>
  <p style='font-family: monospace;'>det(A - λI) = (2-λ)(2-λ) - (1)(1)</p>
  <p style='font-family: monospace;'>           = (2-λ)² - 1</p>
  <p style='font-family: monospace;'>           = 4 - 4λ + λ² - 1</p>
  <p style='font-family: monospace;'>           = λ² - 4λ + 3</p>

  <p><strong>Step 3: Solve λ² - 4λ + 3 = 0</strong></p>
  <p style='font-family: monospace;'>(λ - 1)(λ - 3) = 0</p>
  <p style='font-family: monospace;'>λ₁ = 1,  λ₂ = 3</p>
</div>

<div class='success-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  The eigenvalues are <strong>λ = 1</strong> and <strong>λ = 3</strong>.
</div>
"""
    },
    {
        "title": "Characteristic polynomial properties",
        "body": """
<p style=';'>The characteristic polynomial has important properties:</p>

<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <ul>
    <li><strong>Degree:</strong> An n×n matrix has a characteristic polynomial of degree n</li>
    <li><strong>Number of eigenvalues:</strong> An n×n matrix has exactly n eigenvalues (counting multiplicity, possibly complex)</li>
    <li><strong>Trace and Determinant:</strong>
      <ul style='margin-top: 8px;'>
        <li>Sum of eigenvalues = trace(A) = sum of diagonal entries</li>
        <li>Product of eigenvalues = det(A)</li>
      </ul>
    </li>
  </ul>
</div>

<div class='warning-box' style='border-left: 4px solid #d32f2f; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <strong>Complex eigenvalues:</strong> Real matrices can have complex eigenvalues, which always appear in conjugate pairs.
</div>
"""
    },
    {
        "title": "Quick shortcuts for special matrices",
        "body": """
<p style=';'>Some matrices have eigenvalues you can find instantly:</p>

<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>Diagonal matrices:</strong> The diagonal entries are the eigenvalues</p>
  <p style='font-family: monospace;'>[[a, 0, 0], [0, b, 0], [0, 0, c]] has eigenvalues a, b, c</p>

  <p style='margin-top: 12px;'><strong>Upper/Lower triangular matrices:</strong> Same — diagonal entries are eigenvalues</p>

  <p style='margin-top: 12px;'><strong>Symmetric matrices:</strong> All eigenvalues are real (no complex values)</p>
</div>

<div class='success-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <strong>Recognizing these patterns saves computation time!</strong>
</div>
"""
    }
]
