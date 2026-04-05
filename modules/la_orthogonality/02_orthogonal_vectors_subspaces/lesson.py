TITLE = "Orthogonal Vectors and Subspaces"

SECTIONS = [
    {
        "title": "Orthogonal and Orthonormal Sets",
        "body": """
        <p><strong>Definition (Orthogonal Set):</strong> A set of vectors $\\{\\mathbf{v}_1, \\mathbf{v}_2, \\ldots, \\mathbf{v}_k\\}$ is orthogonal if:</p>

        <div class='concept-box'>
        $$\\mathbf{v}_i \\cdot \\mathbf{v}_j = 0 \\quad \\text{for all } i \\neq j$$
        </div>

        <p><strong>Definition (Orthonormal Set):</strong> A set is orthonormal if it is orthogonal AND each vector is a unit vector:</p>

        <div class='concept-box'>
        $$\\mathbf{v}_i \\cdot \\mathbf{v}_j = \\delta_{ij} = \\begin{cases} 1 & \\text{if } i = j \\\\ 0 & \\text{if } i \\neq j \\end{cases}$$
        </div>

        <p>This is the Kronecker delta—the elegant way to express orthonormality in one formula.</p>

        <p><strong>Key Insight:</strong> Orthogonal/orthonormal sets are the "simplest" bases because:</p>
        <ul>
        <li>Computations are trivial (just dot products)</li>
        <li>Numerically stable in algorithms</li>
        <li>Geometric intuition is immediate (perpendicular directions)</li>
        </ul>

        <div class='worked-example'>
        <p><strong>Example:</strong> Is the set $\\{[1, 0, 0], [0, 1, 0], [0, 0, 1]\\}$ orthonormal?</p>
        <pre>Standard basis vectors e₁, e₂, e₃.

Check orthogonality:
e₁ · e₂ = 0, e₁ · e₃ = 0, e₂ · e₃ = 0 ✓

Check unit vectors:
||e₁|| = 1, ||e₂|| = 1, ||e₃|| = 1 ✓

Yes, this is orthonormal!</pre>
        </div>
        """
    },
    {
        "title": "Orthonormal Bases and Coordinate Representation",
        "body": """
        <p><strong>Orthonormal Basis:</strong> An orthonormal set that spans the space. If $\\{\\mathbf{u}_1, \\mathbf{u}_2, \\ldots, \\mathbf{u}_n\\}$ is an orthonormal basis of $\\mathbb{R}^n$, any vector $\\mathbf{v}$ can be written as:</p>

        <div class='concept-box'>
        $$\\mathbf{v} = (\\mathbf{v} \\cdot \\mathbf{u}_1)\\mathbf{u}_1 + (\\mathbf{v} \\cdot \\mathbf{u}_2)\\mathbf{u}_2 + \\cdots + (\\mathbf{v} \\cdot \\mathbf{u}_n)\\mathbf{u}_n$$
        </div>

        <p><strong>The coordinates are simply dot products!</strong> No need to solve a system of equations—just compute dot products. This is a huge computational advantage.</p>

        <p><strong>Orthogonal Matrices:</strong> A square matrix $Q$ is orthogonal if:</p>

        <div class='concept-box'>
        $$Q^T Q = I \\quad \\text{equivalently,} \\quad Q^{-1} = Q^T$$
        </div>

        <p>The columns (and rows) of an orthogonal matrix form an orthonormal set.</p>

        <p><strong>Key Properties of Orthogonal Matrices:</strong></p>
        <ul>
        <li>$||Q\\mathbf{v}|| = ||\\mathbf{v}||$ for all $\\mathbf{v}$ (preserve lengths)</li>
        <li>$(Q\\mathbf{u}) \\cdot (Q\\mathbf{v}) = \\mathbf{u} \\cdot \\mathbf{v}$ (preserve angles and dot products)</li>
        <li>$\\det(Q) = \\pm 1$ (volume-preserving transformations)</li>
        <li>$Q^{-1} = Q^T$ (very cheap to invert!)</li>
        </ul>

        <div class='success-box'>
        <p><strong>Why Orthogonal Matrices Matter:</strong> Rotations and reflections are orthogonal matrices. They preserve geometric structure, which is essential in applications ranging from computer graphics to signal processing.</p>
        </div>

        <div class='worked-example'>
        <p><strong>Example:</strong> 2D rotation matrix by angle $\\theta$:</p>
        <pre>Q = [cos(θ)  -sin(θ)]
    [sin(θ)   cos(θ)]

Columns: u₁ = [cos(θ), sin(θ)], u₂ = [-sin(θ), cos(θ)]

Check orthonormality:
u₁ · u₂ = -cos(θ)sin(θ) + sin(θ)cos(θ) = 0 ✓
||u₁|| = √(cos²(θ) + sin²(θ)) = 1 ✓
||u₂|| = √(sin²(θ) + cos²(θ)) = 1 ✓

Inverse: Q⁻¹ = Q^T = [cos(θ)   sin(θ)]
                    [-sin(θ)  cos(θ)]

(rotation by -θ)</pre>
        </div>
        """
    },
    {
        "title": "Orthogonal Subspaces and Decomposition",
        "body": """
        <p><strong>Orthogonal Subspaces:</strong> Two subspaces $U$ and $V$ are orthogonal if every vector in $U$ is orthogonal to every vector in $V$:</p>

        <div class='concept-box'>
        $$U \\perp V \\quad \\Leftrightarrow \\quad \\mathbf{u} \\cdot \\mathbf{v} = 0 \\text{ for all } \\mathbf{u} \\in U, \\mathbf{v} \\in V$$
        </div>

        <p><strong>Orthogonal Complement:</strong> The orthogonal complement of a subspace $W$, denoted $W^\\perp$, is the set of all vectors orthogonal to every vector in $W$:</p>

        <div class='concept-box'>
        $$W^\\perp = \\{\\mathbf{v} : \\mathbf{w} \\cdot \\mathbf{v} = 0 \\text{ for all } \\mathbf{w} \\in W\\}$$
        </div>

        <p><strong>Key Theorem:</strong> Every vector in $\\mathbb{R}^n$ can be uniquely decomposed as:</p>

        <div class='concept-box'>
        $$\\mathbf{v} = \\mathbf{v}_W + \\mathbf{v}_{W^\\perp}$$
        </div>

        <p>where $\\mathbf{v}_W \\in W$ and $\\mathbf{v}_{W^\\perp} \\in W^\\perp$.</p>

        <p><strong>Fundamental Subspaces (for a matrix $A$):</strong></p>
        <ul>
        <li><strong>Column space (Range):</strong> $\\text{Col}(A) = \\{A\\mathbf{x} : \\mathbf{x} \\in \\mathbb{R}^n\\}$</li>
        <li><strong>Null space (Kernel):</strong> $\\text{Null}(A) = \\{\\mathbf{x} : A\\mathbf{x} = \\mathbf{0}\\}$</li>
        <li><strong>Row space:</strong> $\\text{Row}(A) = \\text{Col}(A^T)$</li>
        <li><strong>Left null space:</strong> $\\text{Null}(A^T)$</li>
        </ul>

        <p><strong>Orthogonality Relations:</strong></p>
        <ul>
        <li>$\\text{Null}(A) \\perp \\text{Row}(A)$ — row space and null space are orthogonal complements</li>
        <li>$\\text{Null}(A^T) \\perp \\text{Col}(A)$ — column space and left null space are orthogonal complements</li>
        </ul>

        <div class='concept-box'>
        <p><strong>The Four Fundamental Subspaces:</strong> These four subspaces (with their orthogonality relations) are central to understanding linear systems and least squares problems.</p>
        </div>
        """
    }
]
