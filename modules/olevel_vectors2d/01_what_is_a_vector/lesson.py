TITLE = "What is a Vector?"

SECTIONS = [
    {
        "title": "Scalars vs Vectors: Understanding the Difference",
        "body": """
        <h3>Why Do We Need Vectors?</h3>
        <p>In physics and mathematics, we encounter two types of quantities:</p>

        <div class="concept-box">
            <p><strong>Scalars</strong> have only magnitude (size): temperature (25°C), distance (10 m), mass (5 kg)</p>
            <p><strong>Vectors</strong> have both magnitude AND direction: displacement (10 m north), velocity (5 m/s east), force (20 N upward)</p>
        </div>

        <h4>Why This Matters</h4>
        <p>Consider two scenarios:</p>
        <ul>
            <li><strong>Scalar:</strong> "The distance from A to B is 5 km" ← fully describes the journey length</li>
            <li><strong>Vector:</strong> "The displacement from A to B is 5 km southeast" ← specifies both how far AND in which direction</li>
        </ul>

        <p>In real applications (navigation, physics, engineering), direction is crucial. A force of 10 N pushing left is completely different from 10 N pushing right—even though both have the same magnitude!</p>

        <h4>Visual Representation</h4>
        <svg viewBox="0 0 460 160" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; margin: 20px 0;">
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7' />
                </marker>
            </defs>
            <!-- Left side: scalar -->
            <rect x="15" y="15" width="190" height="130" rx="4" fill='#161b22' stroke='#30363d' stroke-width="1"/>
            <text x="110" y="45" fill='currentColor' font-size='14' font-weight='bold' font-family='sans-serif' text-anchor='middle'>Scalar: 10 units</text>
            <circle cx="110" cy="80" r="6" fill='#4f8ef7'/>
            <text x="110" y="125" fill='currentColor' opacity='0.6' text-anchor='middle' font-size='12' font-family='sans-serif'>Just a number</text>

            <!-- Right side: vector -->
            <rect x="235" y="15" width="210" height="130" rx="4" fill='#161b22' stroke='#30363d' stroke-width="1"/>
            <text x="340" y="45" fill='currentColor' font-size='14' font-weight='bold' font-family='sans-serif' text-anchor='middle'>Vector: 10 units</text>
            <circle cx="280" cy="85" r="5" fill='#4f8ef7'/>
            <line x1="285" y1="85" x2="400" y2="85" stroke='#4f8ef7' stroke-width="2.5" marker-end="url(#arrowhead)"/>
            <text x="340" y="125" fill='currentColor' opacity='0.6' text-anchor='middle' font-size='12' font-family='sans-serif'>Magnitude + Direction</text>
        </svg>
        """
    },
    {
        "title": "Vector Notation and Representation",
        "body": """
        <h3>How Do We Write Vectors?</h3>
        <p>Mathematicians use several notations for vectors. They all mean the same thing—it's just preference:</p>

        <div class="concept-box">
            <ul>
                <li><strong>Arrow notation:</strong> \\(\\vec{v}\\) or \\(\\vec{AB}\\) — shows it's a vector</li>
                <li><strong>Bold notation:</strong> <strong>v</strong> or <strong>AB</strong> — common in textbooks</li>
                <li><strong>Component form:</strong> (x, y) or ⟨x, y⟩ — lists horizontal and vertical parts</li>
                <li><strong>Unit vector form:</strong> x<strong>i</strong> + y<strong>j</strong> — uses basis vectors</li>
            </ul>
        </div>

        <h4>Understanding Column Vector Notation</h4>
        <p>The most useful way to write a vector is the <strong>column vector</strong> form:</p>
        <p style="text-align: center; font-size: 1.1em;">
            \\(\\vec{v} = \\begin{pmatrix} x \\\\ y \\end{pmatrix}\\)
        </p>

        <p>This means: "move x units horizontally and y units vertically"</p>

        <div class="worked-example">
            <p><strong>Example 1:</strong> A displacement vector \\(\\vec{AB} = \\begin{pmatrix} 3 \\\\ 4 \\end{pmatrix}\\)</p>
            <p>This represents moving 3 units right and 4 units up.</p>

            <svg viewBox="0 0 230 240" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:300px; margin:15px auto; display:block;">
                <defs>
                    <marker id="arrow1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                        <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7' />
                    </marker>
                </defs>
                <!-- Background -->
                <rect x="15" y="15" width="200" height="210" rx="4" fill='#161b22' stroke='#30363d' stroke-width="1"/>

                <!-- Grid -->
                <line x1="40" y1="195" x2="195" y2="195" stroke='#30363d' stroke-width="1"/>
                <line x1="40" y1="35" x2="40" y2="195" stroke='#30363d' stroke-width="1"/>

                <!-- Grid lines -->
                <line x1="75" y1="35" x2="75" y2="195" stroke='#30363d' stroke-width="0.5" opacity='0.3'/>
                <line x1="110" y1="35" x2="110" y2="195" stroke='#30363d' stroke-width="0.5" opacity='0.3'/>
                <line x1="145" y1="35" x2="145" y2="195" stroke='#30363d' stroke-width="0.5" opacity='0.3'/>
                <line x1="180" y1="35" x2="180" y2="195" stroke='#30363d' stroke-width="0.5" opacity='0.3'/>
                <line x1="40" y1="155" x2="195" y2="155" stroke='#30363d' stroke-width="0.5" opacity='0.3'/>
                <line x1="40" y1="115" x2="195" y2="115" stroke='#30363d' stroke-width="0.5" opacity='0.3'/>
                <line x1="40" y1="75" x2="195" y2="75" stroke='#30363d' stroke-width="0.5" opacity='0.3'/>

                <!-- Point A -->
                <circle cx="75" cy="155" r="5" fill='#4f8ef7'/>
                <text x="55" y="172" fill='currentColor' font-size='12' font-family='sans-serif'>A</text>

                <!-- Vector arrow -->
                <line x1="75" y1="155" x2="180" y2="35" stroke='#4f8ef7' stroke-width="2.5" marker-end="url(#arrow1)"/>
                <text x="105" y="85" fill='#4f8ef7' font-size='12' font-weight='bold' font-family='sans-serif'>AB</text>

                <!-- Dashed construction lines -->
                <line x1="75" y1="155" x2="180" y2="155" stroke='#8b949e' stroke-width="1" stroke-dasharray="3,3"/>
                <line x1="180" y1="155" x2="180" y2="35" stroke='#8b949e' stroke-width="1" stroke-dasharray="3,3"/>

                <!-- Labels for components -->
                <text x="115" y="175" fill='currentColor' opacity='0.6' font-size='11' font-family='sans-serif' text-anchor='middle'>3 units</text>
                <text x="195" y="100" fill='currentColor' opacity='0.6' font-size='11' font-family='sans-serif'>4 units</text>

                <!-- Point B -->
                <circle cx="180" cy="35" r="5" fill='#4f8ef7'/>
                <text x="185" y="52" fill='currentColor' font-size='12' font-family='sans-serif'>B</text>

                <!-- Axes labels -->
                <text x="190" y="210" fill='currentColor' opacity='0.6' font-size='11' font-family='sans-serif'>x</text>
                <text x="28" y="42" fill='currentColor' opacity='0.6' font-size='11' font-family='sans-serif'>y</text>
            </svg>
        </div>

        <h4>Position Vectors</h4>
        <p>When a vector starts from the origin O(0, 0), we call it a <strong>position vector</strong>. The vector to point P(x, y) is simply \\(\\vec{OP} = \\begin{pmatrix} x \\\\ y \\end{pmatrix}\\)</p>
        """
    },
    {
        "title": "Equal Vectors, Parallel Vectors, and Free Vectors",
        "body": """
        <h3>Do Vectors Need to Start from the Same Place?</h3>

        <p>This is a key insight in vector mathematics: <strong>A vector only represents a direction and magnitude. It doesn't have a fixed location.</strong></p>

        <h4>Equal Vectors</h4>
        <p>Two vectors are equal if they have the same components (same magnitude AND direction), regardless of where they start:</p>

        <div class="concept-box">
            <p>\\(\\vec{u} = \\vec{v}\\) ⟺ they have identical components</p>
        </div>

        <svg viewBox="0 0 430 200" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; margin: 20px 0;">
            <defs>
                <marker id="arrow2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7' />
                </marker>
            </defs>
            <!-- Background -->
            <rect x="15" y="15" width="400" height="170" rx="4" fill='#161b22' stroke='#30363d' stroke-width="1"/>

            <!-- Vector u -->
            <circle cx="60" cy="65" r="5" fill='#4f8ef7'/>
            <line x1="60" y1="65" x2="150" y2="115" stroke='#4f8ef7' stroke-width="2.5" marker-end="url(#arrow2)"/>
            <text x="75" y="55" fill='currentColor' font-size='13' font-weight='bold' font-family='sans-serif'>u</text>

            <!-- Vector v (same components, different location) -->
            <circle cx="230" cy="40" r="5" fill='#4f8ef7'/>
            <line x1="230" y1="40" x2="320" y2="90" stroke='#4f8ef7' stroke-width="2.5" marker-end="url(#arrow2)"/>
            <text x="245" y="35" fill='currentColor' font-size='13' font-weight='bold' font-family='sans-serif'>v</text>

            <!-- Equals sign between -->
            <text x="190" y="85" fill='#2da44e' font-size='20' font-weight='bold' font-family='sans-serif' text-anchor='middle'>=</text>

            <text x="215" y="160" fill='currentColor' opacity='0.6' text-anchor='middle' font-size='12' font-family='sans-serif'>Both vectors: same direction and magnitude, so u = v</text>
        </svg>

        <div class="worked-example">
            <p><strong>Example 2:</strong> Are these vectors equal?</p>
            <p>\\(\\vec{u} = \\begin{pmatrix} 2 \\\\ -3 \\end{pmatrix}\\) starting from A(1, 1)</p>
            <p>\\(\\vec{v} = \\begin{pmatrix} 2 \\\\ -3 \\end{pmatrix}\\) starting from C(0, 5)</p>
            <p>Yes! They have identical components, so \\(\\vec{u} = \\vec{v}\\). The starting point doesn't matter.</p>
        </div>

        <h4>Parallel Vectors</h4>
        <p>Vectors are parallel if one is a scalar multiple of the other:</p>

        <div class="concept-box">
            <p>\\(\\vec{u}\\) and \\(\\vec{v}\\) are parallel ⟺ \\(\\vec{u} = k\\vec{v}\\) for some non-zero scalar k</p>
        </div>

        <p>Geometrically: parallel vectors point in the same or opposite directions. They may have different magnitudes.</p>

        <div class="worked-example">
            <p><strong>Example 3:</strong> Check if \\(\\vec{u} = \\begin{pmatrix} 2 \\\\ 4 \\end{pmatrix}\\) and \\(\\vec{v} = \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix}\\) are parallel.</p>
            <p>We need to find k such that \\(\\vec{u} = k\\vec{v}\\)</p>
            <p>\\(\\begin{pmatrix} 2 \\\\ 4 \\end{pmatrix} = k\\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix} = \\begin{pmatrix} k \\\\ 2k \\end{pmatrix}\\)</p>
            <p>From the first component: k = 2. Check with the second: 2k = 4 ✓</p>
            <p><strong>Yes, they are parallel, with \\(\\vec{u} = 2\\vec{v}\\)</strong></p>
        </div>

        <h4>Why This Matters: Free Vectors</h4>
        <p>In mathematics, we treat vectors as <strong>"free vectors"</strong> — they can be translated anywhere without changing their identity. This is different from "position vectors" which are anchored at the origin.</p>
        """
    }
]
