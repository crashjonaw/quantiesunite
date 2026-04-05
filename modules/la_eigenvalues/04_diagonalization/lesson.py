"""Eigenvalues & Eigenvectors — Concept 4: Diagonalization

TITLE: Diagonalization — Simplifying Matrices via Eigendecomposition
"""

TITLE = "Diagonalization — Simplifying Matrices via Eigendecomposition"

SECTIONS = [
    {
        "title": "The diagonalization idea",
        "body": """
<p style=';'>One of the most powerful uses of eigenvectors is <strong>diagonalization</strong>: rewriting a matrix in terms of its eigenvalues and eigenvectors.</p>

<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>Matrix diagonalization:</strong></p>
  <p style='font-family: monospace;'>A = PDP⁻¹</p>
  <ul style='margin-top: 8px;'>
    <li><strong>P</strong> = matrix with eigenvectors as columns</li>
    <li><strong>D</strong> = diagonal matrix with eigenvalues on the diagonal</li>
    <li><strong>P⁻¹</strong> = inverse of P</li>
  </ul>
</div>

<p style=';'>This works when the matrix has enough linearly independent eigenvectors (true for symmetric matrices and many others).</p>
"""
    },
    {
        "title": "Diagonalization example",
        "body": """
<p style=';'>Using our matrix A = [[2, 1], [1, 2]] with eigenvectors [1, -1]ᵀ and [1, 1]ᵀ:</p>

<div class='worked-example' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>Step 1: Construct P and D</strong></p>
  <p style='font-family: monospace;'>P = [[1, 1], [-1, 1]]  (eigenvectors as columns)</p>
  <p style='font-family: monospace;'>D = [[1, 0], [0, 3]]  (eigenvalues on diagonal)</p>

  <p style='margin-top: 12px;'><strong>Step 2: Compute P⁻¹</strong></p>
  <p style='font-family: monospace;'>P⁻¹ = (1/2)[[ 1, -1], [ 1,  1]]</p>

  <p style='margin-top: 12px;'><strong>Step 3: Verify A = PDP⁻¹</strong></p>
  <p style='font-family: monospace;'>PDP⁻¹ = [[1, 1], [-1, 1]] [[1, 0], [0, 3]] (1/2)[[ 1, -1], [ 1,  1]]</p>
  <p style='font-family: monospace;'>      = [[2, 1], [1, 2]] = A ✓</p>
</div>
"""
    },
    {
        "title": "Why diagonalization is powerful",
        "body": """
<p style=';'>Diagonalization transforms complicated matrix operations into simple ones:</p>

<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>Computing powers of A:</strong></p>
  <p style='font-family: monospace;'>A² = (PDP⁻¹)² = PD²P⁻¹</p>
  <p style='font-family: monospace;'>Aⁿ = PDⁿP⁻¹</p>
  <p>And D^n is easy — just raise the diagonal entries to the nth power!</p>

  <p style='margin-top: 12px;'><strong>Example:</strong> If D = [[1, 0], [0, 3]], then</p>
  <p style='font-family: monospace;'>D¹⁰ = [[1, 0], [0, 3¹⁰]] = [[1, 0], [0, 59049]]</p>
</div>

<div class='success-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <strong>Impact:</strong> Computing A¹⁰ directly would require 10 matrix multiplications. Via diagonalization, it's just 1 diagonal multiplication!
</div>
"""
    },
    {
        "title": "When can you diagonalize?",
        "body": """
<p style=';'>Not all matrices are diagonalizable. Here's what you need:</p>

<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>A matrix is diagonalizable if:</strong></p>
  <ul>
    <li>It has n linearly independent eigenvectors (for an n×n matrix)</li>
  </ul>

  <p style='margin-top: 12px;'><strong>Guarantees diagonalizability:</strong></p>
  <ul>
    <li>Symmetric matrices (Aᵀ = A)</li>
    <li>Matrices with n distinct eigenvalues</li>
  </ul>
</div>

<div class='warning-box' style='border-left: 4px solid #d32f2f; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <strong>Defective matrices:</strong> Matrices with repeated eigenvalues may lack enough eigenvectors to be diagonalizable. These require Jordan normal form instead.
</div>
"""
    }
]
