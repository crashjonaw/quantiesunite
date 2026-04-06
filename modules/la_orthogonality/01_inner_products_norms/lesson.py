TITLE = "Inner Products and Norms"

SECTIONS = [
    {
        "title": "The Dot Product (Inner Product)",
        "body": """
        <p><strong>Definition:</strong> For vectors $\\mathbf{u}, \\mathbf{v} \\in \\mathbb{R}^n$, the dot product is:</p>

        <div class='concept-box'>
        $$\\mathbf{u} \\cdot \\mathbf{v} = u_1v_1 + u_2v_2 + \\cdots + u_nv_n = \\mathbf{u}^T\\mathbf{v}$$
        </div>

        <p><strong>Key Properties:</strong></p>
        <ul>
        <li><strong>Commutative:</strong> $\\mathbf{u} \\cdot \\mathbf{v} = \\mathbf{v} \\cdot \\mathbf{u}$</li>
        <li><strong>Distributive:</strong> $\\mathbf{u} \\cdot (\\mathbf{v} + \\mathbf{w}) = \\mathbf{u} \\cdot \\mathbf{v} + \\mathbf{u} \\cdot \\mathbf{w}$</li>
        <li><strong>Scalar multiplication:</strong> $(c\\mathbf{u}) \\cdot \\mathbf{v} = c(\\mathbf{u} \\cdot \\mathbf{v})$</li>
        <li><strong>Self dot product:</strong> $\\mathbf{v} \\cdot \\mathbf{v} = ||\\mathbf{v}||^2 \\geq 0$ (equals 0 iff $\\mathbf{v} = \\mathbf{0}$)</li>
        </ul>

        <p><strong>First Principles:</strong> The dot product measures how much two vectors "align." When they point in the same direction, their dot product is positive and large. When perpendicular, it's zero. When opposite, it's negative.</p>

        <div class='worked-example'>
        <p><strong>Example:</strong> Compute the dot product of $\\mathbf{u} = [1, 2]$ and $\\mathbf{v} = [3, 4]$.</p>
        <pre>u · v = 1(3) + 2(4) = 3 + 8 = 11</pre>
        </div>
        """
    },
    {
        "title": "Norm (Length of a Vector)",
        "body": """
        <p><strong>Definition:</strong> The Euclidean norm (or length) of vector $\\mathbf{v}$ is:</p>

        <div class='concept-box'>
        $$||\\mathbf{v}|| = \\sqrt{\\mathbf{v} \\cdot \\mathbf{v}} = \\sqrt{v_1^2 + v_2^2 + \\cdots + v_n^2}$$
        </div>

        <p><strong>Geometric Interpretation:</strong> The norm is the Euclidean distance from the origin to the point $\\mathbf{v}$. In $\\mathbb{R}^2$, this is exactly the distance formula from geometry.</p>

        <p><strong>Unit Vectors:</strong> A vector $\\mathbf{u}$ is a unit vector if $||\\mathbf{u}|| = 1$. Normalize any nonzero vector by dividing by its norm:</p>

        <div class='concept-box'>
        $$\\hat{\\mathbf{u}} = \\frac{\\mathbf{u}}{||\\mathbf{u}||}$$
        </div>

        <p>Normalization preserves direction while scaling to unit length.</p>

        <div class='worked-example'>
        <p><strong>Example:</strong> Find the norm and unit vector for $\\mathbf{v} = [3, 4]$.</p>
        <pre>||v|| = √(3² + 4²) = √(9 + 16) = √25 = 5

Unit vector: v̂ = [3/5, 4/5]

Verify: ||v̂|| = √((3/5)² + (4/5)²) = √(9/25 + 16/25) = √(25/25) = 1 ✓</pre>
        </div>

        <p><strong>Distance Between Vectors:</strong> The norm defines distance as:</p>

        <div class='concept-box'>
        $$d(\\mathbf{u}, \\mathbf{v}) = ||\\mathbf{u} - \\mathbf{v}|| = \\sqrt{(u_1-v_1)^2 + \\cdots + (u_n-v_n)^2}$$
        </div>

        <p>This makes $\\mathbb{R}^n$ a metric space and connects linear algebra to geometry and analysis.</p>
        """
    },
    {
        "title": "Angle Between Vectors and the Cauchy-Schwarz Inequality",
        "body": """
        <p><strong>Angle Formula:</strong> The angle $\\theta$ between nonzero vectors $\\mathbf{u}$ and $\\mathbf{v}$ satisfies:</p>

        <div class='concept-box'>
        $$\\cos(\\theta) = \\frac{\\mathbf{u} \\cdot \\mathbf{v}}{||\\mathbf{u}|| \\cdot ||\\mathbf{v}||}$$
        </div>

        <p><strong>Why this works:</strong> The dot product encodes the angle through the projection. When vectors are aligned ($\\theta = 0°$), $\\cos(\\theta) = 1$ and $\\mathbf{u} \\cdot \\mathbf{v}$ is maximized. When perpendicular ($\\theta = 90°$), $\\cos(\\theta) = 0$ and $\\mathbf{u} \\cdot \\mathbf{v} = 0$.</p>

        <p><strong>Cauchy-Schwarz Inequality:</strong> For any vectors $\\mathbf{u}, \\mathbf{v}$:</p>

        <div class='concept-box'>
        $$|\\mathbf{u} \\cdot \\mathbf{v}| \\leq ||\\mathbf{u}|| \\cdot ||\\mathbf{v}||$$
        </div>

        <p>Equality holds if and only if $\\mathbf{u}$ and $\\mathbf{v}$ are parallel (one is a scalar multiple of the other).</p>

        <div class='worked-example'>
        <p><strong>Example:</strong> Find the angle between $\\mathbf{u} = [1, 0]$ and $\\mathbf{v} = [1, 1]$.</p>
        <pre>\(\mathbf{u} \cdot \mathbf{v} = 1(1) + 0(1) = 1\)
\(\|\mathbf{u}\| = \sqrt{1^2 + 0^2} = 1\)
\(\|\mathbf{v}\| = \sqrt{1^2 + 1^2} = \sqrt{2}\)

\(\cos(\theta) = 1 / (1 \cdot \sqrt{2}) = 1/\sqrt{2} = \sqrt{2}/2\)
\(\theta = \arccos(\sqrt{2}/2) = 45° = \pi/4\) radians</pre>
        </div>

        <div class='warning-box'>
        <p><strong>Note:</strong> The cosine formula only works for nonzero vectors. For the zero vector, the angle is undefined. Also, ensure your vectors are in the same space before computing angles.</p>
        </div>
        """
    }
]
