"""Eigenvalues & Eigenvectors — Concept 5: Applications

TITLE: Applications in Machine Learning, Physics, and Data Science
"""

TITLE = "Applications in Machine Learning, Physics, and Data Science"

SECTIONS = [
    {
        "title": "Principal Component Analysis (PCA)",
        "body": """
<p style=';'>PCA is one of the most fundamental dimensionality reduction techniques in machine learning.</p>

<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>How it uses eigenvalues:</strong></p>
  <ul>
    <li>Compute the covariance matrix <strong>C</strong> of your data</li>
    <li>Find the eigenvectors of <strong>C</strong> (the principal components)</li>
    <li>The eigenvalues tell you the variance along each principal component</li>
    <li>Larger eigenvalues = directions of greatest variation</li>
  </ul>
</div>

<div class='worked-example' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>Example:</strong> 100-dimensional image dataset</p>
  <ul>
    <li>Compute covariance matrix (100×100)</li>
    <li>Find top 10 eigenvectors (components with largest eigenvalues)</li>
    <li>Project data onto these 10 directions</li>
    <li>Result: 100D data compressed to 10D, retaining ~95% of variance</li>
  </ul>
</div>
"""
    },
    {
        "title": "Neural network training stability",
        "body": """
<p style=';'>Eigenvalues of the Hessian matrix (second derivatives) control neural network training dynamics:</p>

<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>The condition number:</strong></p>
  <p style='font-family: monospace;'>κ = λ_max / λ_min</p>
  <p>Where λ_max and λ_min are the largest and smallest eigenvalues of the Hessian.</p>

  <ul style='margin-top: 12px;'>
    <li><strong>High κ:</strong> Optimization landscape is very "elongated" → slow convergence</li>
    <li><strong>Low κ:</strong> Optimization landscape is well-rounded → fast convergence</li>
  </ul>
</div>

<div class='success-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <strong>In practice:</strong> Batch normalization and learning rate scheduling implicitly reduce the condition number.
</div>
"""
    },
    {
        "title": "Graph neural networks and spectral methods",
        "body": """
<p style=';'>The eigenvalues of the graph Laplacian matrix unlock powerful spectral graph theory:</p>

<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>Graph Laplacian:</strong> L = D - A, where D is the degree matrix and A is the adjacency matrix</p>

  <ul style='margin-top: 12px;'>
    <li><strong>Smallest eigenvalue λ₀ = 0</strong> → corresponds to the graph being connected</li>
    <li><strong>Second smallest λ₁</strong> → the algebraic connectivity (how well-connected is the graph?)</li>
    <li><strong>Eigenvectors:</strong> Can partition the graph into communities (spectral clustering)</li>
  </ul>
</div>

<div class='worked-example' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>Spectral convolution:</strong> Graph neural networks perform convolutions using eigenvectors as a basis:</p>
  <p style='font-family: monospace;'>Output = U · filter(Λ) · Uᵀ · Input</p>
  <p>Where U contains eigenvectors and Λ is the eigenvalue diagonal matrix.</p>
</div>
"""
    },
    {
        "title": "Stability in dynamical systems",
        "body": """
<p style=';'>Eigenvalues determine whether systems grow, decay, or oscillate:</p>

<div class='concept-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>Linear dynamical system:</strong> x(t+1) = Ax(t)</p>

  <ul style='margin-top: 12px;'>
    <li><strong>All |λᵢ| < 1</strong> → system converges to equilibrium (stable)</li>
    <li><strong>Any |λᵢ| > 1</strong> → system diverges (unstable)</li>
    <li><strong>Complex eigenvalues:</strong> Cause oscillatory behavior</li>
  </ul>
</div>

<div class='success-box' style='border-left: 4px solid #4f8ef7; padding: 16px; margin: 12px 0; border-radius: 6px;'>
  <p><strong>In neural networks:</strong> RNNs are prone to vanishing/exploding gradients. Why?</p>
  <ul>
    <li>Gradient flow through time involves powers of the weight matrix</li>
    <li>If eigenvalues are small (< 1), gradients vanish exponentially</li>
    <li>If eigenvalues are large (> 1), gradients explode exponentially</li>
  </ul>
</div>
"""
    }
]
