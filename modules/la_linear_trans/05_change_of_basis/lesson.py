TITLE = "Change of Basis and Geometric Interpretation"

SECTIONS = [
    {
        "title": "Change of Basis",
        "body": """
        <div class='concept-box'>
        <p><strong>Problem:</strong> How does a linear transformation look in different coordinate systems?</p>

        <p><strong>Change of basis matrix:</strong> If B and B' are bases for the same space, the change of basis matrix P from B to B' has columns that are the B'-coordinates of the B-basis vectors.</p>

        <p><strong>Coordinate transformation:</strong> If v has coordinates [v]_B in basis B and [v]_{B'} in basis B', then:</p>
        <pre class='code-block'>[v]_{B'} = P⁻¹[v]_B</pre>

        <p>where P is the change of basis matrix.</p>

        <p><strong>Transformation under change of basis:</strong> If T: V → V has matrix [T]_B in basis B and matrix [T]_{B'} in basis B', then:</p>
        <pre class='code-block'>[T]_{B'} = P⁻¹ [T]_B P</pre>

        <p>This is called a similarity transformation. The matrices [T]_B and [T]_{B'} are similar matrices.</p>
        </div>
        """
    },
    {
        "title": "Geometric Interpretation",
        "body": """
        <div class='concept-box'>
        <p><strong>Linear transformations geometrically:</strong> A linear transformation T: ℝⁿ → ℝᵐ has geometric meaning:</p>

        <ul>
        <li><strong>Scaling:</strong> T(x) = cx shrinks or stretches by factor c</li>
        <li><strong>Rotation:</strong> \(T(x) = R_\theta x\) rotates by angle \(\theta\) (preserves length and angles)</li>
        <li><strong>Projection:</strong> T(x) = proj_W(x) drops the perpendicular component</li>
        <li><strong>Reflection:</strong> T(x) flips across a line or plane</li>
        <li><strong>Shear:</strong> T(x) shifts one direction relative to another</li>
        </ul>

        <p><strong>Determinant interpretation:</strong> For T(x) = Ax, the determinant det(A) represents the volume scaling factor:</p>
        <ul>
        <li>If det(A) > 0, orientation is preserved</li>
        <li>If det(A) < 0, orientation is reversed</li>
        <li>If det(A) = 0, the transformation collapses to a lower-dimensional subspace</li>
        </ul>
        </div>
        """
    },
    {
        "title": "Rank and Geometric Meaning",
        "body": """
        <div class='concept-box'>
        <p><strong>Rank and geometry:</strong> The rank of T determines the dimension of the image:</p>
        <ul>
        <li>rank(T) = dim(V): T is injective (no two different inputs map to the same output)</li>
        <li>rank(T) = dim(W): T is surjective (every output has a preimage)</li>
        <li>rank(T) < min(dim(V), dim(W)): Information is lost; the image is lower-dimensional</li>
        </ul>

        <p><strong>Intuition:</strong> The rank tells you how much of the output space is "filled" by the transformation.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example 1: Rotation matrix in 2D</strong></p>
        <pre class='code-block'>\(R = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}\)

This matrix rotates vectors counterclockwise by angle \(\theta\).
\(\det(R) = \cos^2(\theta) + \sin^2(\theta) = 1\) (orientation preserved, no scaling)
Eigenvalues: \(\lambda = \cos(\theta) \pm i \cdot \sin(\theta) = e^{\pm i\theta}\) (complex, on unit circle)</pre>

        <p><strong>Example 2: Projection onto a line</strong></p>
        <pre class='code-block'>P = uuᵀ, where u is a unit vector
This projects any vector v onto the direction of u.
The image is 1-dimensional (the line), and the kernel is the orthogonal complement.
rank(P) = 1, nullity(P) = n - 1 (for n-dimensional space)</pre>
        </div>
        """
    },
    {
        "title": "Applications",
        "body": """
        <div class='concept-box'>
        <p><strong>Real-world applications of linear transformations:</strong></p>
        <ul>
        <li><strong>Computer graphics:</strong> Rotation, scaling, perspective transformations are linear</li>
        <li><strong>Differential equations:</strong> Solution space of linear systems is structured by eigenvectors</li>
        <li><strong>Principal Component Analysis:</strong> Eigenvectors of the covariance matrix identify directions of maximum variance</li>
        <li><strong>Quantum mechanics:</strong> Observables are linear operators (matrices) on Hilbert spaces</li>
        <li><strong>Signal processing:</strong> Fourier transforms and filtering are linear transformations</li>
        <li><strong>Machine learning:</strong> Neural network layers are compositions of linear transformations and nonlinear activations</li>
        </ul>

        <p><strong>Summary:</strong> Linear transformations are among the most important objects in mathematics, bridging abstract algebra with geometry and enabling powerful computational methods across science and engineering.</p>
        </div>
        """
    }
]
