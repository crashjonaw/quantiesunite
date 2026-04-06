TITLE = "Scalar and Vector Products"

SECTIONS = [
    {
        "title": "Scalar (Dot) Product: Definition and Computation",
        "body": """
<div class="concept-box">
<h3>Algebraic Definition</h3>
<p>The <strong>scalar product</strong> (or <strong>dot product</strong>) of vectors \(\mathbf{u} = (u_1, u_2, u_3)\) and \(\mathbf{v} = (v_1, v_2, v_3)\) is:</p>
<p style="text-align: center; font-weight: bold;">\(\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + u_3 v_3\)</p>
<p>This produces a <strong>scalar</strong> (a single real number), not a vector.</p>
</div>

<h3>Geometric Interpretation</h3>
<p>The scalar product relates to the angle \(\theta\) between two vectors:</p>
<p style="text-align: center; font-weight: bold;">\(\mathbf{u} \cdot \mathbf{v} = |\mathbf{u}| |\mathbf{v}| \cos(\theta)\)</p>

<p><strong>Derivation:</strong> Consider the law of cosines applied to the triangle formed by vectors <strong>u</strong>, <strong>v</strong>, and <strong>u</strong> - <strong>v</strong>:</p>
<p>\(|\mathbf{u} - \mathbf{v}|^2 = |\mathbf{u}|^2 + |\mathbf{v}|^2 - 2|\mathbf{u}||\mathbf{v}|\cos(\theta)\)</p>
<p>Expanding the left side using the dot product:</p>
<p>\((\mathbf{u} - \mathbf{v}) \cdot (\mathbf{u} - \mathbf{v}) = |\mathbf{u}|^2 - 2\mathbf{u} \cdot \mathbf{v} + |\mathbf{v}|^2\)</p>
<p>Comparing both expressions gives us the geometric formula.</p>

<div class="worked-example">
<h4>Example 1: Computing Dot Product</h4>
<p>Find \(\mathbf{u} \cdot \mathbf{v}\) where \(\mathbf{u} = (2, 3, -1)\) and \(\mathbf{v} = (1, -2, 4)\)</p>
<p><strong>Solution:</strong></p>
<p>\(\mathbf{u} \cdot \mathbf{v} = (2)(1) + (3)(-2) + (-1)(4)\)</p>
<p>\(= 2 - 6 - 4 =\) <strong>-8</strong></p>
</div>
"""
    },
    {
        "title": "Applications: Angles and Orthogonality",
        "body": """
<h3>Finding the Angle Between Vectors</h3>
<p>Rearranging the geometric formula, we can find the angle between two vectors:</p>
<p style="text-align: center; font-weight: bold;">\(\cos(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{|\mathbf{u}| |\mathbf{v}|}\)</p>
<p>This formula is valid for \(0° \leq \theta \leq 180°\).</p>

<div class="worked-example">
<h4>Example 2: Angle Between Vectors</h4>
<p>Find the angle between \(\mathbf{u} = (1, 2, 2)\) and \(\mathbf{v} = (2, 1, -2)\)</p>
<p><strong>Solution:</strong></p>
<p>\(\mathbf{u} \cdot \mathbf{v} = (1)(2) + (2)(1) + (2)(-2) = 2 + 2 - 4 = 0\)</p>
<p>Since the dot product is zero, \(\cos(\theta) = 0\), so \(\theta =\) <strong>90°</strong></p>
</div>

<h3>Orthogonality</h3>
<p>Two vectors are <strong>perpendicular</strong> (orthogonal) if and only if their dot product is zero:</p>
<p style="text-align: center; font-weight: bold;">\(\mathbf{u} \perp \mathbf{v} \iff \mathbf{u} \cdot \mathbf{v} = 0\)</p>

<div class="success-box">
<h4>Key Point</h4>
<p>Orthogonality is often easier to check algebraically (by computing the dot product) than to verify geometrically.</p>
</div>

<h3>Properties of the Scalar Product</h3>
<ul>
<li><strong>Commutative:</strong> \(\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}\)</li>
<li><strong>Distributive:</strong> \(\mathbf{u} \cdot (\mathbf{v} + \mathbf{w}) = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}\)</li>
<li><strong>Scalar multiplication:</strong> \((k\mathbf{u}) \cdot \mathbf{v} = k(\mathbf{u} \cdot \mathbf{v})\)</li>
<li><strong>Self dot product:</strong> \(\mathbf{u} \cdot \mathbf{u} = |\mathbf{u}|^2\)</li>
</ul>
"""
    },
    {
        "title": "Vector Projections",
        "body": """
<h3>Scalar Projection</h3>
<p>The <strong>scalar projection</strong> (or component) of vector \(\mathbf{u}\) in the direction of \(\mathbf{v}\) is the length of the shadow \(\mathbf{u}\) casts onto \(\mathbf{v}\):</p>
<p style="text-align: center; font-weight: bold;">\(\text{comp}_{\mathbf{v}}(\mathbf{u}) = \frac{\mathbf{u} \cdot \mathbf{v}}{|\mathbf{v}|}\)</p>
<p>This can be positive (same direction), negative (opposite direction), or zero (perpendicular).</p>

<h3>Vector Projection</h3>
<p>The <strong>vector projection</strong> of \(\mathbf{u}\) onto \(\mathbf{v}\) is the vector component of \(\mathbf{u}\) along \(\mathbf{v}\):</p>
<p style="text-align: center; font-weight: bold;">\(\text{proj}_{\mathbf{v}}(\mathbf{u}) = \frac{\mathbf{u} \cdot \mathbf{v}}{|\mathbf{v}|^2} \mathbf{v}\)</p>
<p>This vector is parallel to \(\mathbf{v}\) and has magnitude equal to the scalar projection.</p>

<div class="worked-example">
<h4>Example 3: Vector Projection</h4>
<p>Find the projection of \(\mathbf{u} = (3, 4, 0)\) onto \(\mathbf{v} = (1, 0, 0)\)</p>
<p><strong>Solution:</strong></p>
<p>\(\mathbf{u} \cdot \mathbf{v} = 3\), \(|\mathbf{v}|^2 = 1\)</p>
<p>\(\text{proj}_{\mathbf{v}}(\mathbf{u}) = 3(1, 0, 0) =\) <strong>(3, 0, 0)</strong></p>
</div>

<div class="warning-box">
<h4>Common Mistake</h4>
<p>Don't confuse vector projection with unit vector multiplication. The projection formula includes division by \(|\mathbf{v}|^2\), not just normalization of \(\mathbf{v}\).</p>
</div>
"""
    },
    {
        "title": "Cross Product: Definition and Computation",
        "body": """
<div class="concept-box">
<h3>Algebraic Definition</h3>
<p>The <strong>cross product</strong> \(\mathbf{u} \times \mathbf{v}\) of vectors \(\mathbf{u} = (u_1, u_2, u_3)\) and \(\mathbf{v} = (v_1, v_2, v_3)\) is:</p>
<p style="text-align: center; font-weight: bold;">\(\mathbf{u} \times \mathbf{v} = (u_2 v_3 - u_3 v_2,\; u_3 v_1 - u_1 v_3,\; u_1 v_2 - u_2 v_1)\)</p>
<p>This produces a <strong>vector</strong>, not a scalar. The result is perpendicular to both \(\mathbf{u}\) and \(\mathbf{v}\).</p>
</div>

<h3>Determinant Formulation</h3>
<p>The cross product can be computed using the determinant:</p>
<p style="text-align: center; font-weight: bold;">\(\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix}\)</p>

<p>Expanding along the first row:</p>
<p style="text-align: center; font-weight: bold;">\(\mathbf{u} \times \mathbf{v} = \mathbf{i}(u_2 v_3 - u_3 v_2) - \mathbf{j}(u_1 v_3 - u_3 v_1) + \mathbf{k}(u_1 v_2 - u_2 v_1)\)</p>

<div class="worked-example">
<h4>Example 4: Computing Cross Product</h4>
<p>Find \(\mathbf{u} \times \mathbf{v}\) where \(\mathbf{u} = (1, 2, 3)\) and \(\mathbf{v} = (4, 5, 6)\)</p>
<p><strong>Solution:</strong></p>
<p>\(\mathbf{u} \times \mathbf{v} = (2 \cdot 6 - 3 \cdot 5,\; 3 \cdot 4 - 1 \cdot 6,\; 1 \cdot 5 - 2 \cdot 4)\)</p>
<p>\(= (12 - 15,\; 12 - 6,\; 5 - 8)\)</p>
<p>\(=\) <strong>(-3, 6, -3)</strong></p>
</div>

<h3>Geometric Interpretation</h3>
<p>The magnitude of the cross product equals the area of the parallelogram spanned by \(\mathbf{u}\) and \(\mathbf{v}\):</p>
<p style="text-align: center; font-weight: bold;">\(|\mathbf{u} \times \mathbf{v}| = |\mathbf{u}| |\mathbf{v}| \sin(\theta)\)</p>

<p>The <strong>direction</strong> follows the <strong>right-hand rule</strong>: curl the fingers of your right hand from \(\mathbf{u}\) toward \(\mathbf{v}\), and your thumb points in the direction of \(\mathbf{u} \times \mathbf{v}\).</p>
"""
    },
    {
        "title": "Properties and Applications of Cross Product",
        "body": """
<h3>Key Properties</h3>
<ul>
<li><strong>Anticommutative:</strong> \(\mathbf{v} \times \mathbf{u} = -(\mathbf{u} \times \mathbf{v})\)</li>
<li><strong>Non-associative:</strong> \((\mathbf{u} \times \mathbf{v}) \times \mathbf{w} \neq \mathbf{u} \times (\mathbf{v} \times \mathbf{w})\) in general</li>
<li><strong>Self-cross:</strong> \(\mathbf{u} \times \mathbf{u} = \mathbf{0}\)</li>
<li><strong>Orthogonality:</strong> \(\mathbf{u} \times \mathbf{v}\) is perpendicular to both \(\mathbf{u}\) and \(\mathbf{v}\)</li>
<li><strong>Distributive:</strong> \(\mathbf{u} \times (\mathbf{v} + \mathbf{w}) = \mathbf{u} \times \mathbf{v} + \mathbf{u} \times \mathbf{w}\)</li>
</ul>

<div class="warning-box">
<h4>Important Distinction</h4>
<p>Unlike scalar multiplication, the cross product is NOT commutative. Order matters: \(\mathbf{u} \times \mathbf{v}\) and \(\mathbf{v} \times \mathbf{u}\) point in opposite directions.</p>
</div>

<h3>Triple Scalar Product (Scalar Triple Product)</h3>
<p>The volume of the parallelepiped (3D parallelogram) spanned by vectors \(\mathbf{u}\), \(\mathbf{v}\), and \(\mathbf{w}\) is:</p>
<p style="text-align: center; font-weight: bold;">\(V = |\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})| = |\det[\mathbf{u}\; \mathbf{v}\; \mathbf{w}]|\)</p>

<p>If the scalar triple product equals zero, the three vectors are <strong>coplanar</strong> (lie in the same plane).</p>

<div class="worked-example">
<h4>Example 5: Determining Coplanarity</h4>
<p>Show that \(\mathbf{u} = (1, 2, 3)\), \(\mathbf{v} = (2, -1, 0)\), and \(\mathbf{w} = (3, 1, 3)\) are coplanar.</p>
<p><strong>Solution:</strong></p>
<p>\(\mathbf{v} \times \mathbf{w} = ((-1) \cdot 3 - 0 \cdot 1,\; 0 \cdot 3 - 2 \cdot 3,\; 2 \cdot 1 - (-1) \cdot 3)\)</p>
<p>\(= (-3, -6, 5)\)</p>
<p>\(\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = (1)(-3) + (2)(-6) + (3)(5)\)</p>
<p>\(= -3 - 12 + 15 =\) <strong>0</strong></p>
<p>Since the scalar triple product is zero, the vectors are coplanar.</p>
</div>

<h3>Applications</h3>
<ul>
<li><strong>Finding normal vectors:</strong> The cross product gives a vector perpendicular to a plane</li>
<li><strong>Calculating areas:</strong> Cross product magnitude equals the area of a parallelogram</li>
<li><strong>Physics:</strong> Torque, angular momentum, and magnetic force use cross products</li>
</ul>
"""
    }
]
