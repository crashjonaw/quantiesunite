TITLE = "Scalar and Vector Products"

SECTIONS = [
    {
        "title": "Scalar (Dot) Product: Definition and Computation",
        "body": """
<div class="concept-box">
<h3>Algebraic Definition</h3>
<p>The <strong>scalar product</strong> (or <strong>dot product</strong>) of vectors <strong>u</strong> = (u₁, u₂, u₃) and <strong>v</strong> = (v₁, v₂, v₃) is:</p>
<p style="text-align: center; font-weight: bold;">\\mathbf{u} \\cdot \\mathbf{v} = u_1v_1 + u_2v_2 + u_3v_3</p>
<p>This produces a <strong>scalar</strong> (a single real number), not a vector.</p>
</div>

<h3>Geometric Interpretation</h3>
<p>The scalar product relates to the angle θ between two vectors:</p>
<p style="text-align: center; font-weight: bold;">\\mathbf{u} \\cdot \\mathbf{v} = |\\mathbf{u}| |\\mathbf{v}| \\cos(\\theta)</p>

<p><strong>Derivation:</strong> Consider the law of cosines applied to the triangle formed by vectors <strong>u</strong>, <strong>v</strong>, and <strong>u</strong> - <strong>v</strong>:</p>
<p>|<strong>u</strong> - <strong>v</strong>|² = |<strong>u</strong>|² + |<strong>v</strong>|² - 2|<strong>u</strong>||<strong>v</strong>|cos(θ)</p>
<p>Expanding the left side using the dot product:</p>
<p>(<strong>u</strong> - <strong>v</strong>) · (<strong>u</strong> - <strong>v</strong>) = |<strong>u</strong>|² - 2<strong>u</strong> · <strong>v</strong> + |<strong>v</strong>|²</p>
<p>Comparing both expressions gives us the geometric formula.</p>

<div class="worked-example">
<h4>Example 1: Computing Dot Product</h4>
<p>Find <strong>u</strong> · <strong>v</strong> where <strong>u</strong> = (2, 3, -1) and <strong>v</strong> = (1, -2, 4)</p>
<p><strong>Solution:</strong></p>
<p><strong>u</strong> · <strong>v</strong> = (2)(1) + (3)(-2) + (-1)(4)</p>
<p>= 2 - 6 - 4 = <strong>-8</strong></p>
</div>
"""
    },
    {
        "title": "Applications: Angles and Orthogonality",
        "body": """
<h3>Finding the Angle Between Vectors</h3>
<p>Rearranging the geometric formula, we can find the angle between two vectors:</p>
<p style="text-align: center; font-weight: bold;">\\cos(\\theta) = \\frac{\\mathbf{u} \\cdot \\mathbf{v}}{|\\mathbf{u}| |\\mathbf{v}|}</p>
<p>This formula is valid for 0° ≤ θ ≤ 180°.</p>

<div class="worked-example">
<h4>Example 2: Angle Between Vectors</h4>
<p>Find the angle between <strong>u</strong> = (1, 2, 2) and <strong>v</strong> = (2, 1, -2)</p>
<p><strong>Solution:</strong></p>
<p><strong>u</strong> · <strong>v</strong> = (1)(2) + (2)(1) + (2)(-2) = 2 + 2 - 4 = 0</p>
<p>Since the dot product is zero, cos(θ) = 0, so θ = <strong>90°</strong></p>
</div>

<h3>Orthogonality</h3>
<p>Two vectors are <strong>perpendicular</strong> (orthogonal) if and only if their dot product is zero:</p>
<p style="text-align: center; font-weight: bold;">\\mathbf{u} \\perp \\mathbf{v} \\iff \\mathbf{u} \\cdot \\mathbf{v} = 0</p>

<div class="success-box">
<h4>Key Point</h4>
<p>Orthogonality is often easier to check algebraically (by computing the dot product) than to verify geometrically.</p>
</div>

<h3>Properties of the Scalar Product</h3>
<ul>
<li><strong>Commutative:</strong> <strong>u</strong> · <strong>v</strong> = <strong>v</strong> · <strong>u</strong></li>
<li><strong>Distributive:</strong> <strong>u</strong> · (<strong>v</strong> + <strong>w</strong>) = <strong>u</strong> · <strong>v</strong> + <strong>u</strong> · <strong>w</strong></li>
<li><strong>Scalar multiplication:</strong> (k<strong>u</strong>) · <strong>v</strong> = k(<strong>u</strong> · <strong>v</strong>)</li>
<li><strong>Self dot product:</strong> <strong>u</strong> · <strong>u</strong> = |<strong>u</strong>|²</li>
</ul>
"""
    },
    {
        "title": "Vector Projections",
        "body": """
<h3>Scalar Projection</h3>
<p>The <strong>scalar projection</strong> (or component) of vector <strong>u</strong> in the direction of <strong>v</strong> is the length of the shadow <strong>u</strong> casts onto <strong>v</strong>:</p>
<p style="text-align: center; font-weight: bold;">\\text{comp}_{\\mathbf{v}}(\\mathbf{u}) = \\frac{\\mathbf{u} \\cdot \\mathbf{v}}{|\\mathbf{v}|}</p>
<p>This can be positive (same direction), negative (opposite direction), or zero (perpendicular).</p>

<h3>Vector Projection</h3>
<p>The <strong>vector projection</strong> of <strong>u</strong> onto <strong>v</strong> is the vector component of <strong>u</strong> along <strong>v</strong>:</p>
<p style="text-align: center; font-weight: bold;">\\text{proj}_{\\mathbf{v}}(\\mathbf{u}) = \\frac{\\mathbf{u} \\cdot \\mathbf{v}}{|\\mathbf{v}|^2} \\mathbf{v}</p>
<p>This vector is parallel to <strong>v</strong> and has magnitude equal to the scalar projection.</p>

<div class="worked-example">
<h4>Example 3: Vector Projection</h4>
<p>Find the projection of <strong>u</strong> = (3, 4, 0) onto <strong>v</strong> = (1, 0, 0)</p>
<p><strong>Solution:</strong></p>
<p><strong>u</strong> · <strong>v</strong> = 3, |<strong>v</strong>|² = 1</p>
<p>proj<sub><strong>v</strong></sub>(<strong>u</strong>) = 3(1, 0, 0) = <strong>(3, 0, 0)</strong></p>
</div>

<div class="warning-box">
<h4>Common Mistake</h4>
<p>Don't confuse vector projection with unit vector multiplication. The projection formula includes division by |<strong>v</strong>|², not just normalization of <strong>v</strong>.</p>
</div>
"""
    },
    {
        "title": "Cross Product: Definition and Computation",
        "body": """
<div class="concept-box">
<h3>Algebraic Definition</h3>
<p>The <strong>cross product</strong> <strong>u</strong> × <strong>v</strong> of vectors <strong>u</strong> = (u₁, u₂, u₃) and <strong>v</strong> = (v₁, v₂, v₃) is:</p>
<p style="text-align: center; font-weight: bold;">\\mathbf{u} \\times \\mathbf{v} = (u_2v_3 - u_3v_2, u_3v_1 - u_1v_3, u_1v_2 - u_2v_1)</p>
<p>This produces a <strong>vector</strong>, not a scalar. The result is perpendicular to both <strong>u</strong> and <strong>v</strong>.</p>
</div>

<h3>Determinant Formulation</h3>
<p>The cross product can be computed using the determinant:</p>
<p style="text-align: center; font-weight: bold;">\\mathbf{u} \\times \\mathbf{v} = \\begin{vmatrix} \\mathbf{i} & \\mathbf{j} & \\mathbf{k} \\\\ u_1 & u_2 & u_3 \\\\ v_1 & v_2 & v_3 \\end{vmatrix}</p>

<p>Expanding along the first row:</p>
<p style="text-align: center; font-weight: bold;">\\mathbf{u} \\times \\mathbf{v} = \\mathbf{i}(u_2v_3 - u_3v_2) - \\mathbf{j}(u_1v_3 - u_3v_1) + \\mathbf{k}(u_1v_2 - u_2v_1)</p>

<div class="worked-example">
<h4>Example 4: Computing Cross Product</h4>
<p>Find <strong>u</strong> × <strong>v</strong> where <strong>u</strong> = (1, 2, 3) and <strong>v</strong> = (4, 5, 6)</p>
<p><strong>Solution:</strong></p>
<p><strong>u</strong> × <strong>v</strong> = (2·6 - 3·5, 3·4 - 1·6, 1·5 - 2·4)</p>
<p>= (12 - 15, 12 - 6, 5 - 8)</p>
<p>= <strong>(-3, 6, -3)</strong></p>
</div>

<h3>Geometric Interpretation</h3>
<p>The magnitude of the cross product equals the area of the parallelogram spanned by <strong>u</strong> and <strong>v</strong>:</p>
<p style="text-align: center; font-weight: bold;">|\\mathbf{u} \\times \\mathbf{v}| = |\\mathbf{u}| |\\mathbf{v}| \\sin(\\theta)</p>

<p>The <strong>direction</strong> follows the <strong>right-hand rule</strong>: curl the fingers of your right hand from <strong>u</strong> toward <strong>v</strong>, and your thumb points in the direction of <strong>u</strong> × <strong>v</strong>.</p>
"""
    },
    {
        "title": "Properties and Applications of Cross Product",
        "body": """
<h3>Key Properties</h3>
<ul>
<li><strong>Anticommutative:</strong> <strong>v</strong> × <strong>u</strong> = -(<strong>u</strong> × <strong>v</strong>)</li>
<li><strong>Non-associative:</strong> (<strong>u</strong> × <strong>v</strong>) × <strong>w</strong> ≠ <strong>u</strong> × (<strong>v</strong> × <strong>w</strong>) in general</li>
<li><strong>Self-cross:</strong> <strong>u</strong> × <strong>u</strong> = <strong>0</strong></li>
<li><strong>Orthogonality:</strong> <strong>u</strong> × <strong>v</strong> is perpendicular to both <strong>u</strong> and <strong>v</strong></li>
<li><strong>Distributive:</strong> <strong>u</strong> × (<strong>v</strong> + <strong>w</strong>) = <strong>u</strong> × <strong>v</strong> + <strong>u</strong> × <strong>w</strong></li>
</ul>

<div class="warning-box">
<h4>Important Distinction</h4>
<p>Unlike scalar multiplication, the cross product is NOT commutative. Order matters: <strong>u</strong> × <strong>v</strong> and <strong>v</strong> × <strong>u</strong> point in opposite directions.</p>
</div>

<h3>Triple Scalar Product (Scalar Triple Product)</h3>
<p>The volume of the parallelepiped (3D parallelogram) spanned by vectors <strong>u</strong>, <strong>v</strong>, and <strong>w</strong> is:</p>
<p style="text-align: center; font-weight: bold;">V = |\\mathbf{u} \\cdot (\\mathbf{v} \\times \\mathbf{w})| = |\\det[\\mathbf{u} \\, \\mathbf{v} \\, \\mathbf{w}]|</p>

<p>If the scalar triple product equals zero, the three vectors are <strong>coplanar</strong> (lie in the same plane).</p>

<div class="worked-example">
<h4>Example 5: Determining Coplanarity</h4>
<p>Show that <strong>u</strong> = (1, 2, 3), <strong>v</strong> = (2, -1, 0), and <strong>w</strong> = (3, 1, 3) are coplanar.</p>
<p><strong>Solution:</strong></p>
<p><strong>v</strong> × <strong>w</strong> = ((-1)·3 - 0·1, 0·3 - 2·3, 2·1 - (-1)·3)</p>
<p>= (-3, -6, 5)</p>
<p><strong>u</strong> · (<strong>v</strong> × <strong>w</strong>) = (1)(-3) + (2)(-6) + (3)(5)</p>
<p>= -3 - 12 + 15 = <strong>0</strong></p>
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
