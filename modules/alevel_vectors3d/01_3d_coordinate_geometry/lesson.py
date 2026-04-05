TITLE = "3D Coordinate Geometry and Vectors"

SECTIONS = [
    {
        "title": "Vector Notation and Components",
        "body": """
<div class="concept-box">
<h3>Vector Representation in 3D Space</h3>
<p>A vector in 3D space is defined by three components:</p>
<p style="text-align: center; font-weight: bold;">\\mathbf{v} = (x, y, z) \\text{ or } \\mathbf{v} = x\\mathbf{i} + y\\mathbf{j} + z\\mathbf{k}</p>
<p>where <strong>i</strong>, <strong>j</strong>, <strong>k</strong> are the standard basis vectors (unit vectors along x, y, and z axes respectively).</p>
</div>

<h3>Magnitude (Length) of a Vector</h3>
<p>The magnitude represents the length of the vector:</p>
<p style="text-align: center; font-weight: bold;">|\\mathbf{v}| = \\sqrt{x^2 + y^2 + z^2}</p>

<div class="worked-example">
<h4>Example 1: Finding Vector Magnitude</h4>
<p>Find the magnitude of <strong>v</strong> = (3, -4, 12)</p>
<p><strong>Solution:</strong></p>
<p>|<strong>v</strong>| = √(3² + (-4)² + 12²)</p>
<p>= √(9 + 16 + 144)</p>
<p>= √169 = <strong>13</strong></p>
</div>

<h3>Vector Addition and Subtraction</h3>
<p>Vectors are added and subtracted component-wise:</p>
<p style="text-align: center; font-weight: bold;">\\mathbf{u} + \\mathbf{v} = (u_1 + v_1, u_2 + v_2, u_3 + v_3)</p>
<p style="text-align: center; font-weight: bold;">\\mathbf{u} - \\mathbf{v} = (u_1 - v_1, u_2 - v_2, u_3 - v_3)</p>

<h3>Scalar Multiplication</h3>
<p>Multiplying a vector by a scalar (real number) scales each component:</p>
<p style="text-align: center; font-weight: bold;">k\\mathbf{v} = (kx, ky, kz)</p>
<p><strong>Key properties:</strong></p>
<ul>
<li>Addition is commutative: <strong>u</strong> + <strong>v</strong> = <strong>v</strong> + <strong>u</strong></li>
<li>Addition is associative: (<strong>u</strong> + <strong>v</strong>) + <strong>w</strong> = <strong>u</strong> + (<strong>v</strong> + <strong>w</strong>)</li>
<li>Scalar multiplication distributes: k(<strong>u</strong> + <strong>v</strong>) = k<strong>u</strong> + k<strong>v</strong></li>
</ul>
"""
    },
    {
        "title": "Unit Vectors and Normalization",
        "body": """
<h3>Definition of Unit Vectors</h3>
<p>A <strong>unit vector</strong> is a vector with magnitude equal to 1. The standard unit vectors in 3D are:</p>
<p style="text-align: center; font-weight: bold;">\\mathbf{i} = (1, 0, 0), \\quad \\mathbf{j} = (0, 1, 0), \\quad \\mathbf{k} = (0, 0, 1)</p>

<h3>Normalization Process</h3>
<p>To convert any non-zero vector to a unit vector (normalize it):</p>
<p style="text-align: center; font-weight: bold;">\\hat{\\mathbf{v}} = \\frac{\\mathbf{v}}{|\\mathbf{v}|}</p>
<p>The unit vector points in the same direction as the original vector.</p>

<div class="worked-example">
<h4>Example 2: Normalizing a Vector</h4>
<p>Normalize the vector <strong>v</strong> = (1, 2, 2)</p>
<p><strong>Solution:</strong></p>
<p>First, find the magnitude:</p>
<p>|<strong>v</strong>| = √(1² + 2² + 2²) = √(1 + 4 + 4) = √9 = 3</p>
<p>Then divide each component by the magnitude:</p>
<p>$\\hat{\\mathbf{v}} = \\frac{1}{3}(1, 2, 2) = \\left(\\frac{1}{3}, \\frac{2}{3}, \\frac{2}{3}\\right)$</p>
<p><strong>Verification:</strong> $|\\hat{\\mathbf{v}}| = \\sqrt{\\frac{1}{9} + \\frac{4}{9} + \\frac{4}{9}} = \\sqrt{\\frac{9}{9}} = 1$ ✓</p>
</div>

<div class="success-box">
<h4>Key Insight</h4>
<p>Normalization is useful for finding directions independent of magnitude, such as in physics when calculating velocity from speed and direction.</p>
</div>
"""
    },
    {
        "title": "Distance Between Points",
        "body": """
<h3>Distance Formula in 3D</h3>
<p>The distance between two points P(x₁, y₁, z₁) and Q(x₂, y₂, z₂) in 3D space is:</p>
<p style="text-align: center; font-weight: bold;">d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}</p>
<p>This is equivalent to finding the magnitude of the displacement vector <strong>PQ</strong> = Q - P.</p>

<div class="worked-example">
<h4>Example 3: Distance Between Two Points</h4>
<p>Find the distance between P(1, 2, 3) and Q(4, 6, 15)</p>
<p><strong>Solution:</strong></p>
<p>Displacement vector: <strong>PQ</strong> = (4-1, 6-2, 15-3) = (3, 4, 12)</p>
<p>Distance: d = √(3² + 4² + 12²) = √(9 + 16 + 144) = √169 = <strong>13</strong></p>
</div>

<h3>Midpoint of a Line Segment</h3>
<p>The midpoint M of the line segment joining P(x₁, y₁, z₁) and Q(x₂, y₂, z₂) is:</p>
<p style="text-align: center; font-weight: bold;">M = \\left(\\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2}, \\frac{z_1 + z_2}{2}\\right)</p>

<div class="worked-example">
<h4>Example 4: Finding the Midpoint</h4>
<p>Find the midpoint of the segment from A(2, -1, 4) to B(6, 3, 8)</p>
<p><strong>Solution:</strong></p>
<p>$M = \\left(\\frac{2 + 6}{2}, \\frac{-1 + 3}{2}, \\frac{4 + 8}{2}\\right) = (4, 1, 6)$</p>
</div>
"""
    }
]
