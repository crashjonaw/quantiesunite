"""Eigenvalues & Eigenvectors — Concept 1: Eigenvalues Intro

TITLE: Eigenvalues & Eigenvectors: The Big Idea
"""

TITLE = "Eigenvalues & Eigenvectors: The Big Idea"

SECTIONS = [
    {
        "title": "What makes a vector special?",
        "body": """
<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p>When a matrix <strong>A</strong> multiplies most vectors, it <em>rotates</em> them — they point in a completely new direction.</p>
  <p>But for some <strong>special vectors</strong>, the matrix only <strong>stretches or shrinks</strong> them — they stay pointing the same way.</p>
</div>

<p style=';'>These special vectors are called <strong>eigenvectors</strong>. The stretch factor is the <strong>eigenvalue</strong> \(\lambda\) (lambda).</p>

<div class='worked-example' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <strong>The fundamental relationship:</strong>
  <p style='font-family: monospace; font-size: 16px; margin: 8px 0;'><strong>\(A\mathbf{v} = \lambda\mathbf{v}\)</strong></p>
  <ul style='margin: 8px 0;'>
    <li><strong>A</strong> is the matrix</li>
    <li><strong>v</strong> is the eigenvector (the special direction)</li>
    <li><strong>\(\lambda\)</strong> (lambda) is the eigenvalue (the stretch factor)</li>
  </ul>
</div>
"""
    },
    {
        "title": "Visualizing eigenvectors",
        "body": """
<p style=';'>Imagine a transformation matrix that scales horizontally by 2 and vertically by 0.5:</p>

<div class='worked-example' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p style='font-family: monospace;'>A = [[2, 0], [0, 0.5]]</p>
  <p>The eigenvectors are:</p>
  <ul>
    <li>Direction [1, 0] (horizontal) → stretched by eigenvalue \(\lambda = 2\)</li>
    <li>Direction [0, 1] (vertical) → shrunk by eigenvalue \(\lambda = 0.5\)</li>
  </ul>
</div>

<div class='success-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <strong>Key insight:</strong> Eigenvectors don't change direction — only magnitude. They align with the "natural axes" of the transformation.
</div>
"""
    },
    {
        "title": "Eigenvalues tell us about behavior",
        "body": """
<p style=';'>The eigenvalue \(\lambda\) reveals what the transformation does to an eigenvector:</p>

<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <ul>
    <li><strong>\(\lambda > 1\)</strong> → eigenvector is stretched (grows in magnitude)</li>
    <li><strong>\(0 < \lambda < 1\)</strong> → eigenvector is shrunk (decreases in magnitude)</li>
    <li><strong>\(\lambda = 0\)</strong> → eigenvector collapses to the zero vector</li>
    <li><strong>\(\lambda < 0\)</strong> → eigenvector is flipped in direction and scaled</li>
  </ul>
</div>

<div class='warning-box' style='border-left: 4px solid #d32f2f; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <strong>Important:</strong> Not all vectors are eigenvectors, and not all matrices have real eigenvalues. But every square matrix has at least one eigenvalue (possibly complex).
</div>
"""
    },
    {
        "title": "Why this matters in practice",
        "body": """
<p style=';'>Eigenvalues and eigenvectors appear everywhere in applied mathematics and machine learning:</p>

<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <ul>
    <li><strong>Physics:</strong> Vibration modes of structures, quantum mechanics energy levels</li>
    <li><strong>Machine Learning:</strong> Principal Component Analysis (PCA), covariance matrices</li>
    <li><strong>Graph Theory:</strong> Connectivity properties, PageRank algorithm</li>
    <li><strong>Stability Analysis:</strong> Whether systems converge or diverge over time</li>
  </ul>
</div>

<p style=';'>Understanding eigenvalues unlocks the ability to understand and simplify complex linear transformations.</p>
"""
    }
]
