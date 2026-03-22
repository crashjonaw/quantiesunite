"""Eigenvalues & Eigenvectors — Lesson sections."""

SECTIONS = [
    {"title": "The big idea: special directions",
     "body": """<p>When a matrix A multiplies most vectors, it <em>rotates</em> them — they point in a completely new direction.
     But for some special vectors, the matrix only <strong>stretches or shrinks</strong> them — they stay pointing the same way.</p>
     <p>These special vectors are called <strong>eigenvectors</strong>. The stretch factor is the <strong>eigenvalue</strong> λ.</p>
     <div class='example-box'>Av = λv<br>
     A is the matrix · v is the eigenvector · λ (lambda) is the eigenvalue</div>"""},
    {"title": "Finding eigenvalues: the characteristic equation",
     "body": """<p>We rearrange Av = λv to (A − λI)v = 0.
     For a non-zero solution to exist, the matrix (A−λI) must be <strong>singular</strong> (non-invertible), so:</p>
     <div class='example-box'>det(A − λI) = 0  ← <em>characteristic equation</em></div>
     <p>Solving this polynomial gives all eigenvalues λ₁, λ₂, …</p>
     <div class='example-box'>A = [[2,1],[1,2]]<br>
     det([[2−λ, 1],[1, 2−λ]]) = (2−λ)² − 1 = 0<br>
     (2−λ−1)(2−λ+1) = 0 → λ = 1 or λ = 3</div>"""},
    {"title": "Why eigenvalues matter in deep learning",
     "body": """<p>Eigenvalues appear everywhere in ML:</p>
     <ul>
       <li><strong>PCA</strong>: eigenvectors of the covariance matrix = principal components</li>
       <li><strong>Stability of training</strong>: the largest eigenvalue of the Hessian controls learning rate</li>
       <li><strong>SVD</strong>: built directly from eigenvalue decomposition</li>
       <li><strong>Graph neural networks</strong>: graph Laplacian eigenvalues define spectral convolutions</li>
     </ul>"""},
]
