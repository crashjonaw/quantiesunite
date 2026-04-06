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
  <p style='font-family: monospace;'>\(A\mathbf{v} = \lambda\mathbf{v}\)</p>
  <p>Rewrite as:</p>
  <p style='font-family: monospace;'>\(A\mathbf{v} - \lambda\mathbf{v} = 0\)</p>
  <p style='font-family: monospace;'>\(A\mathbf{v} - \lambda I\mathbf{v} = 0\)  (multiply \(\lambda\) by identity matrix)</p>
  <p style='font-family: monospace;'>\((A - \lambda I)\mathbf{v} = 0\)</p>
</div>

<p style=';'>For a non-zero solution <strong>v</strong> to exist, the matrix \((A - \lambda I)\) must be <strong>singular</strong> (non-invertible):</p>

<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>The Characteristic Equation:</strong></p>
  <p style='font-family: monospace; font-size: 18px;'><strong>\(\det(A - \lambda I) = 0\)</strong></p>
  <p>Solving this polynomial equation gives all eigenvalues \(\lambda_1, \lambda_2, \ldots\)</p>
</div>
"""
    },
    {
        "title": "Computing a 2×2 example",
        "body": """
<p style=';'>Find the eigenvalues of:</p>

<div class='worked-example' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p style='font-family: monospace;'>A = [[2, 1], [1, 2]]</p>

  <p><strong>Step 1: Form \((A - \lambda I)\)</strong></p>
  <p style='font-family: monospace;'>\(A - \lambda I = [[2-\lambda, 1], [1, 2-\lambda]]\)</p>

  <p><strong>Step 2: Compute the determinant</strong></p>
  <p style='font-family: monospace;'>\(\det(A - \lambda I) = (2-\lambda)(2-\lambda) - (1)(1)\)</p>
  <p style='font-family: monospace;'>\(= (2-\lambda)^2 - 1\)</p>
  <p style='font-family: monospace;'>\(= 4 - 4\lambda + \lambda^2 - 1\)</p>
  <p style='font-family: monospace;'>\(= \lambda^2 - 4\lambda + 3\)</p>

  <p><strong>Step 3: Solve \(\lambda^2 - 4\lambda + 3 = 0\)</strong></p>
  <p style='font-family: monospace;'>\((\lambda - 1)(\lambda - 3) = 0\)</p>
  <p style='font-family: monospace;'>\(\lambda_1 = 1,\quad \lambda_2 = 3\)</p>
</div>

<div class='success-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  The eigenvalues are <strong>\(\lambda = 1\)</strong> and <strong>\(\lambda = 3\)</strong>.
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
        <li>Sum of eigenvalues = \(\text{trace}(A)\) = sum of diagonal entries</li>
        <li>Product of eigenvalues = \(\det(A)\)</li>
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
