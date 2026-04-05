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
        <svg viewBox="-15 0 460 200" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; margin: 20px 0;">
            <defs>
                <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7' />
                </marker>
            </defs>
            <!-- Left side: scalar -->
            <text x="50" y="30" fill='#e6edf3' font-size='16' font-weight='bold'>Scalar: 10 units</text>
            <circle cx="50" cy="80" r="5" fill='#4f8ef7'/>
            <text x="30" y="130" fill='#8b949e' text-anchor='middle' font-size='12'>Just a number</text>

            <!-- Right side: vector -->
            <text x="300" y="30" fill='#e6edf3' font-size='16' font-weight='bold'>Vector: 10 units →</text>
            <circle cx="200" cy="80" r="5" fill='#4f8ef7'/>
            <line x1="200" y1="80" x2="320" y2="80" stroke='#4f8ef7' stroke-width="2" marker-end="url(#arrowhead)"/>
            <text x="260" y="130" fill='#8b949e' text-anchor='middle' font-size='12'>Magnitude + Direction</text>
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

            <svg viewBox="0 0 200 250" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:300px; margin:15px auto; display:block;">
                <defs>
                    <marker id="arrow1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                        <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7' />
                    </marker>
                </defs>
                <!-- Grid -->
                <line x1="10" y1="200" x2="180" y2="200" stroke='#30363d' stroke-width="1"/>
                <line x1="10" y1="10" x2="10" y2="200" stroke='#30363d' stroke-width="1"/>

                <!-- Grid lines -->
                <line x1="40" y1="10" x2="40" y2="200" stroke='#30363d' stroke-width="0.5" opacity='0.5'/>
                <line x1="70" y1="10" x2="70" y2="200" stroke='#30363d' stroke-width="0.5" opacity='0.5'/>
                <line x1="100" y1="10" x2="100" y2="200" stroke='#30363d' stroke-width="0.5" opacity='0.5'/>
                <line x1="130" y1="10" x2="130" y2="200" stroke='#30363d' stroke-width="0.5" opacity='0.5'/>
                <line x1="160" y1="10" x2="160" y2="200" stroke='#30363d' stroke-width="0.5" opacity='0.5'/>
                <line x1="10" y1="40" x2="180" y2="40" stroke='#30363d' stroke-width="0.5" opacity='0.5'/>
                <line x1="10" y1="70" x2="180" y2="70" stroke='#30363d' stroke-width="0.5" opacity='0.5'/>
                <line x1="10" y1="100" x2="180" y2="100" stroke='#30363d' stroke-width="0.5" opacity='0.5'/>
                <line x1="10" y1="130" x2="180" y2="130" stroke='#30363d' stroke-width="0.5" opacity='0.5'/>
                <line x1="10" y1="160" x2="180" y2="160" stroke='#30363d' stroke-width="0.5" opacity='0.5'/>

                <!-- Point A -->
                <circle cx="40" cy="160" r="4" fill='#4f8ef7'/>
                <text x="25" y="180" fill='#e6edf3' font-size='12'>A</text>

                <!-- Vector arrow -->
                <line x1="40" y1="160" x2="130" y2="40" stroke='#4f8ef7' stroke-width="3" marker-end="url(#arrow1)"/>
                <text x="90" y="90" fill='#8b949e' font-size='11' font-weight='bold'>\\(\\vec{AB}\\)</text>

                <!-- Dashed construction lines -->
                <line x1="40" y1="160" x2="130" y2="160" stroke='#8b949e' stroke-width="1" stroke-dasharray="2,2"/>
                <line x1="130" y1="160" x2="130" y2="40" stroke='#8b949e' stroke-width="1" stroke-dasharray="2,2"/>

                <!-- Labels for components -->
                <text x="85" y="175" fill='#8b949e' font-size='10'>3 units →</text>
                <text x="140" y="100" fill='#8b949e' font-size='10'>4 units ↑</text>

                <!-- Point B -->
                <circle cx="130" cy="40" r="4" fill='#4f8ef7'/>
                <text x="135" y="75" fill='#e6edf3' font-size='12'>B</text>

                <!-- Axes labels -->
                <text x="175" y="215" fill='#8b949e' font-size='11'>x</text>
                <text x="5" y="25" fill='#8b949e' font-size='11'>y</text>
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

        <svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; margin: 20px 0;">
            <defs>
                <marker id="arrow2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7' />
                </marker>
            </defs>

            <!-- Vector 1 -->
            <circle cx="50" cy="80" r="4" fill='#4f8ef7'/>
            <line x1="50" y1="80" x2="130" y2="130" stroke='#4f8ef7' stroke-width="2" marker-end="url(#arrow2)"/>
            <text x="80" y="95" fill='#e6edf3' font-size='12' font-weight='bold'>\\(\\vec{u}\\)</text>

            <!-- Vector 2 (same components, different location) -->
            <circle cx="200" cy="30" r="4" fill='#4f8ef7'/>
            <line x1="200" y1="30" x2="280" y2="80" stroke='#4f8ef7' stroke-width="2" marker-end="url(#arrow2)"/>
            <text x="230" y="45" fill='#e6edf3' font-size='12' font-weight='bold'>\\(\\vec{v}\\)</text>

            <text x="200" y="170" fill='#8b949e' text-anchor='middle' font-size='12'>Both vectors: same 3 right, 5 down → \\(\\vec{u} = \\vec{v}\\)</text>
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
