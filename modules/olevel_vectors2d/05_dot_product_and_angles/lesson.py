TITLE = "Dot Product and Angles"

SECTIONS = [
    {
        "title": "The Dot Product: Multiplying Vectors",
        "body": """
        <h3>Why Multiply Vectors?</h3>

        <p>Unlike scalar multiplication (multiplying by a number), there are two meaningful ways to multiply two vectors: the dot product and the cross product (2D/3D). The dot product is the most useful in physics and geometry.</p>

        <h4>The Algebraic Definition</h4>

        <p>The <strong>dot product</strong> (or <strong>scalar product</strong>) of two vectors produces a single number (scalar):</p>

        <div class="concept-box">
            <p style="text-align: center; font-size: 1.15em;">
                \\(\\vec{u} \\cdot \\vec{v} = \\begin{pmatrix} a \\\\ b \\end{pmatrix} \\cdot \\begin{pmatrix} c \\\\ d \\end{pmatrix} = ac + bd\\)
            </p>
        </div>

        <p><strong>How to compute it:</strong> Multiply corresponding components and add the results.</p>

        <div class="worked-example">
            <p><strong>Example 1:</strong> Find \\(\\vec{u} \\cdot \\vec{v}\\) where \\(\\vec{u} = \\begin{pmatrix} 2 \\\\ 3 \\end{pmatrix}\\) and \\(\\vec{v} = \\begin{pmatrix} 4 \\\\ -1 \\end{pmatrix}\\)</p>

            <p class="concept-box">
                \\(\\vec{u} \\cdot \\vec{v} = (2)(4) + (3)(-1) = 8 - 3 = 5\\)
            </p>
        </div>

        <h4>Why is It Called a "Dot" Product?</h4>

        <p>The geometric interpretation reveals the real power of the dot product:</p>

        <div class="concept-box">
            <p style="text-align: center; font-size: 1.15em;">
                \\(\\vec{u} \\cdot \\vec{v} = |\\vec{u}| \\cdot |\\vec{v}| \\cdot \\cos(\\theta)\\)
            </p>
            <p style="text-align: center">where θ is the angle between the vectors</p>
        </div>

        <p><strong>This formula tells us something profound:</strong> The dot product measures how much the two vectors point in the same direction!</p>

        <svg viewBox="0 0 400 250" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; margin: 20px 0;">
            <defs>
                <marker id="arrow8" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7' />
                </marker>
            </defs>

            <text x="150" y="25" fill='#e6edf3' font-size='13' font-weight='bold' text-anchor='middle'>Angle Between Vectors</text>

            <!-- Vector 1 -->
            <circle cx="100" cy="120" r="4" fill='#4f8ef7'/>
            <line x1="100" y1="120" x2="170" y2="80" stroke='#4f8ef7' stroke-width="2.5" marker-end="url(#arrow8)"/>
            <text x="125" y="90" fill='#4f8ef7' font-size='11' font-weight='bold'>\\(\\vec{u}\\)</text>

            <!-- Vector 2 -->
            <line x1="100" y1="120" x2="180" y2="160" stroke='#2da44e' stroke-width="2.5" marker-end="url(#arrow8)"/>
            <text x="135" y="150" fill='#2da44e' font-size='11' font-weight='bold'>\\(\\vec{v}\\)</text>

            <!-- Angle indicator -->
            <path d="M 130 120 A 30 30 0 0 1 145 135" fill='none' stroke='#f85149' stroke-width="1.5"/>
            <text x="145" y="115" fill='#f85149' font-size='11'>θ</text>

            <!-- Information -->
            <text x="50" y="220" fill='#8b949e' font-size='11'>θ = 0°: vectors point same direction</text>
            <text x="50" y="240" fill='#8b949e' font-size='11'>θ = 90°: vectors perpendicular</text>
        </svg>
        """
    },
    {
        "title": "Finding Angles Between Vectors",
        "body": """
        <h3>Rearranging the Formula</h3>

        <p>We can rearrange the dot product formula to find the angle between any two vectors:</p>

        <div class="concept-box">
            <p style="text-align: center; font-size: 1.15em;">
                \\(\\cos(\\theta) = \\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{u}| \\cdot |\\vec{v}|}\\)
            </p>
        </div>

        <p><strong>Step-by-step process:</strong></p>
        <ol>
            <li>Compute \\(\\vec{u} \\cdot \\vec{v}\\) (algebraically)</li>
            <li>Compute \\(|\\vec{u}|\\) and \\(|\\vec{v}|\\) (using magnitude formula)</li>
            <li>Divide: \\(\\cos(\\theta) = \\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{u}| \\cdot |\\vec{v}|}\\)</li>
            <li>Find θ using inverse cosine: \\(\\theta = \\cos^{-1}\\left(\\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{u}| \\cdot |\\vec{v}|}\\right)\\)</li>
        </ol>

        <div class="worked-example">
            <p><strong>Example 2:</strong> Find the angle between \\(\\vec{u} = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}\\) and \\(\\vec{v} = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}\\)</p>

            <p class="concept-box">
                \\(\\vec{u} \\cdot \\vec{v} = (1)(1) + (0)(1) = 1\\)
            </p>

            <p class="concept-box">
                \\(|\\vec{u}| = \\sqrt{1^2 + 0^2} = 1\\)
            </p>

            <p class="concept-box">
                \\(|\\vec{v}| = \\sqrt{1^2 + 1^2} = \\sqrt{2}\\)
            </p>

            <p class="concept-box">
                \\(\\cos(\\theta) = \\frac{1}{1 \\cdot \\sqrt{2}} = \\frac{1}{\\sqrt{2}} = \\frac{\\sqrt{2}}{2}\\)
            </p>

            <p class="concept-box">
                \\(\\theta = \\cos^{-1}\\left(\\frac{\\sqrt{2}}{2}\\right) = 45°\\)
            </p>
        </div>

        <h4>Special Cases</h4>

        <div class="concept-box">
            <table style="width: 100%; margin-top: 10px">
                <tr >
                    <th style="text-align: left; padding: 8px;">Angle</th>
                    <th style="text-align: left; padding: 8px;">cos(θ)</th>
                    <th style="text-align: left; padding: 8px;">\\(\\vec{u} \\cdot \\vec{v}\\)</th>
                    <th style="text-align: left; padding: 8px;">Meaning</th>
                </tr>
                <tr >
                    <td style="padding: 8px;">0°</td>
                    <td style="padding: 8px;">1</td>
                    <td style="padding: 8px;">positive (max)</td>
                    <td style="padding: 8px;">Same direction</td>
                </tr>
                <tr >
                    <td style="padding: 8px;">90°</td>
                    <td style="padding: 8px;">0</td>
                    <td style="padding: 8px;">0</td>
                    <td style="padding: 8px;">Perpendicular</td>
                </tr>
                <tr>
                    <td style="padding: 8px;">180°</td>
                    <td style="padding: 8px;">-1</td>
                    <td style="padding: 8px;">negative (min)</td>
                    <td style="padding: 8px;">Opposite direction</td>
                </tr>
            </table>
        </div>
        """
    },
    {
        "title": "Perpendicularity and Properties of the Dot Product",
        "body": """
        <h3>When Vectors are Perpendicular</h3>

        <p>Two vectors are perpendicular (at right angles) if and only if their dot product is zero:</p>

        <div class="concept-box">
            <p style="text-align: center; font-size: 1.15em;">
                \\(\\vec{u} \\perp \\vec{v} \\iff \\vec{u} \\cdot \\vec{v} = 0\\)
            </p>
        </div>

        <p><strong>Why?</strong> When θ = 90°, cos(90°) = 0, so \\(|\\vec{u}| \\cdot |\\vec{v}| \\cdot 0 = 0\\)</p>

        <div class="worked-example">
            <p><strong>Example 3:</strong> Check if \\(\\vec{u} = \\begin{pmatrix} 3 \\\\ 2 \\end{pmatrix}\\) and \\(\\vec{v} = \\begin{pmatrix} -2 \\\\ 3 \\end{pmatrix}\\) are perpendicular.</p>

            <p class="concept-box">
                \\(\\vec{u} \\cdot \\vec{v} = (3)(-2) + (2)(3) = -6 + 6 = 0\\)
            </p>

            <p>Since the dot product is zero, <strong>yes, they are perpendicular!</strong></p>
        </div>

        <h3>Properties of the Dot Product</h3>

        <div class="concept-box">
            <ul>
                <li><strong>Commutative:</strong> \\(\\vec{u} \\cdot \\vec{v} = \\vec{v} \\cdot \\vec{u}\\)</li>
                <li><strong>Distributive:</strong> \\(\\vec{u} \\cdot (\\vec{v} + \\vec{w}) = \\vec{u} \\cdot \\vec{v} + \\vec{u} \\cdot \\vec{w}\\)</li>
                <li><strong>Scalar:</strong> \\((k\\vec{u}) \\cdot \\vec{v} = k(\\vec{u} \\cdot \\vec{v}) = \\vec{u} \\cdot (k\\vec{v})\\)</li>
                <li><strong>Self-product:</strong> \\(\\vec{v} \\cdot \\vec{v} = |\\vec{v}|^2\\)</li>
            </ul>
        </div>

        <div class="worked-example">
            <p><strong>Example 4:</strong> Use the property \\(\\vec{v} \\cdot \\vec{v} = |\\vec{v}|^2\\) to find \\(|\\vec{v}|\\) if \\(\\vec{v} = \\begin{pmatrix} 3 \\\\ 4 \\end{pmatrix}\\)</p>

            <p class="concept-box">
                \\(\\vec{v} \\cdot \\vec{v} = (3)(3) + (4)(4) = 9 + 16 = 25\\)
            </p>

            <p class="concept-box">
                \\(|\\vec{v}|^2 = 25 \\implies |\\vec{v}| = 5\\)
            </p>

            <p>This confirms our earlier calculation!</p>
        </div>
        """
    },
    {
        "title": "Applications: Physics and Geometry",
        "body": """
        <h3>Application 1: Work in Physics</h3>

        <p>In physics, <strong>work</strong> is defined as force applied in the direction of motion:</p>

        <div class="concept-box">
            <p style="text-align: center; font-size: 1.1em;">
                Work = \\(\\vec{F} \\cdot \\vec{d} = |\\vec{F}| \\cdot |\\vec{d}| \\cdot \\cos(\\theta)\\)
            </p>
            <p style="text-align: center">where \\(\\vec{F}\\) is force and \\(\\vec{d}\\) is displacement</p>
        </div>

        <div class="worked-example">
            <p><strong>Problem:</strong> A force \\(\\vec{F} = \\begin{pmatrix} 10 \\\\ 0 \\end{pmatrix}\\) N is applied to an object that moves \\(\\vec{d} = \\begin{pmatrix} 5 \\\\ 5 \\end{pmatrix}\\) m. Find the work done.</p>

            <p class="concept-box">
                Work = \\(\\vec{F} \\cdot \\vec{d} = (10)(5) + (0)(5) = 50\\) J
            </p>

            <p class="text-muted-note">Only the component of force in the direction of motion contributes to work. The perpendicular component contributes nothing.</p>
        </div>

        <h3>Application 2: Finding Projection Lengths</h3>

        <p>The <strong>projection</strong> of \\(\\vec{u}\\) onto \\(\\vec{v}\\) is the length of the shadow cast by \\(\\vec{u}\\) along the direction of \\(\\vec{v}\\):</p>

        <div class="concept-box">
            <p style="text-align: center; font-size: 1.1em;">
                \\(\\text{proj}_v(u) = \\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{v}|}\\)
            </p>
        </div>

        <svg viewBox="0 0 400 250" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; margin: 20px 0;">
            <defs>
                <marker id="arrow9" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7' />
                </marker>
            </defs>

            <text x="200" y="25" fill='#e6edf3' font-size='12' font-weight='bold' text-anchor='middle'>Projection of \\(\\vec{u}\\) onto \\(\\vec{v}\\)</text>

            <!-- Vector v (base) -->
            <circle cx="80" cy="150" r="4" fill='#4f8ef7'/>
            <line x1="80" y1="150" x2="280" y2="150" stroke='#4f8ef7' stroke-width="2.5" marker-end="url(#arrow9)"/>
            <text x="180" y="135" fill='#4f8ef7' font-size='12' font-weight='bold'>\\(\\vec{v}\\)</text>

            <!-- Vector u -->
            <line x1="80" y1="150" x2="180" y2="80" stroke='#2da44e' stroke-width="2.5" marker-end="url(#arrow9)"/>
            <text x="150" y="110" fill='#2da44e' font-size='12' font-weight='bold'>\\(\\vec{u}\\)</text>

            <!-- Projection (perpendicular drop) -->
            <line x1="180" y1="80" x2="180" y2="150" stroke='#8b949e' stroke-width="1" stroke-dasharray="2,2"/>
            <circle cx="180" cy="150" r="3" fill='#f85149'/>

            <!-- Projection vector -->
            <line x1="80" y1="150" x2="180" y2="150" stroke='#f85149' stroke-width="2.5" marker-end="url(#arrow9)"/>
            <text x="130" y="170" fill='#f85149' font-size='11' font-weight='bold'>projection</text>
        </svg>

        <div class="worked-example">
            <p><strong>Problem:</strong> Find the projection of \\(\\vec{u} = \\begin{pmatrix} 3 \\\\ 2 \\end{pmatrix}\\) onto \\(\\vec{v} = \\begin{pmatrix} 4 \\\\ 0 \\end{pmatrix}\\)</p>

            <p class="concept-box">
                \\(\\vec{u} \\cdot \\vec{v} = (3)(4) + (2)(0) = 12\\)
            </p>

            <p class="concept-box">
                \\(|\\vec{v}| = \\sqrt{16 + 0} = 4\\)
            </p>

            <p class="concept-box">
                \\(\\text{proj}_v(u) = \\frac{12}{4} = 3\\)
            </p>

            <p>The shadow of \\(\\vec{u}\\) along \\(\\vec{v}\\) has length 3 units.</p>
        </div>

        <div class="success-box">
            <p><strong>Geometric Insight:</strong> The dot product essentially measures how much two vectors "overlap" in direction. This is why it's so useful in physics, computer graphics, and machine learning!</p>
        </div>
        """
    }
]
