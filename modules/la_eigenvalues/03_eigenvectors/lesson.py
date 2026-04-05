"""Eigenvalues & Eigenvectors — Concept 3: Finding Eigenvectors

TITLE: Finding Eigenvectors — Solving (A - λI)v = 0
"""

TITLE = "Finding Eigenvectors — Solving (A - λI)v = 0"

SECTIONS = [
    {
        "title": "The eigenvector equation",
        "body": """
<p style=';'>Once you have an eigenvalue λ, finding its eigenvectors means solving:</p>

<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p style='font-family: monospace; font-size: 18px;'><strong>(A - λI)v = 0</strong></p>
  <p>This is a homogeneous system of linear equations.</p>
  <p>The eigenvectors are all non-zero solutions to this system.</p>
</div>

<p style=';'><strong>Important:</strong> For each eigenvalue, there is a whole <em>subspace</em> of eigenvectors (the eigenspace). Any non-zero vector in that subspace is an eigenvector.</p>
"""
    },
    {
        "title": "Example: Finding eigenvectors for λ = 1",
        "body": """
<p style=';'>Continuing from our 2×2 example with A = [[2, 1], [1, 2]] and eigenvalues λ = 1 and λ = 3:</p>

<div class='worked-example' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>For λ = 1:</strong></p>
  <p style='font-family: monospace;'>A - I = [[2-1, 1], [1, 2-1]] = [[1, 1], [1, 1]]</p>

  <p style='margin-top: 12px;'>Solve (A - I)v = 0:</p>
  <p style='font-family: monospace;'>[[1, 1], [1, 1]][v₁, v₂] = [0, 0]</p>

  <p style='margin-top: 12px;'>This gives: v₁ + v₂ = 0 → v₂ = -v₁</p>

  <p style='margin-top: 12px;'>Eigenvectors: <strong>v = [1, -1]</strong> (and any scalar multiple)</p>
</div>

<div class='success-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  Check: A[1, -1]ᵀ = [[2, 1], [1, 2]][1, -1]ᵀ = [1, -1]ᵀ = 1·[1, -1]ᵀ ✓
</div>
"""
    },
    {
        "title": "Example: Finding eigenvectors for λ = 3",
        "body": """
<div class='worked-example' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>For λ = 3:</strong></p>
  <p style='font-family: monospace;'>A - 3I = [[2-3, 1], [1, 2-3]] = [[-1, 1], [1, -1]]</p>

  <p style='margin-top: 12px;'>Solve (A - 3I)v = 0:</p>
  <p style='font-family: monospace;'>[[-1, 1], [1, -1]][v₁, v₂] = [0, 0]</p>

  <p style='margin-top: 12px;'>This gives: -v₁ + v₂ = 0 → v₂ = v₁</p>

  <p style='margin-top: 12px;'>Eigenvectors: <strong>v = [1, 1]</strong> (and any scalar multiple)</p>
</div>

<div class='success-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  Check: A[1, 1]ᵀ = [[2, 1], [1, 2]][1, 1]ᵀ = [3, 3]ᵀ = 3·[1, 1]ᵀ ✓
</div>
"""
    },
    {
        "title": "Geometric interpretation",
        "body": """
<p style=';'>The eigenvectors have a beautiful geometric meaning:</p>

<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <ul>
    <li><strong>Eigenvectors:</strong> The directions along which the transformation acts purely as scaling</li>
    <li><strong>Eigenvalues:</strong> The scaling factors along those directions</li>
    <li><strong>Eigenspace:</strong> All vectors along the same "natural axis" are eigenvectors for the same eigenvalue</li>
  </ul>
</div>

<div class='warning-box' style='border-left: 4px solid #d32f2f; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <strong>Convention:</strong> We typically normalize eigenvectors to unit length (||v|| = 1) or use the simplest integer representation.
</div>
"""
    }
]
