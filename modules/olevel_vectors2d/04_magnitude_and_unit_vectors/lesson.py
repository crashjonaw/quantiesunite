TITLE = "Magnitude and Unit Vectors"

SECTIONS = [
    {
        "title": "Magnitude: Finding the Length of a Vector",
        "body": """
        <h3>What is Magnitude?</h3>

        <p>The <strong>magnitude</strong> (or <strong>norm</strong>) of a vector is its length—how far it extends. It's always a non-negative number.</p>

        <h4>The Magnitude Formula</h4>

        <p>For a vector \\(\\vec{v} = \\begin{pmatrix} x \\\\ y \\end{pmatrix}\\), the magnitude is:</p>

        <div class="concept-box">
            <p style="text-align: center; font-size: 1.15em;">\\(|\\vec{v}| = \\sqrt{x^2 + y^2}\\)</p>
        </div>

        <p><strong>Where does this come from?</strong> The Pythagorean theorem! The vector components form a right triangle, and the hypotenuse is the vector itself.</p>

        <svg viewBox="0 0 310 260" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:350px; margin:20px auto; display:block;">
            <defs>
                <marker id="arrow6" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7' />
                </marker>
            </defs>
            <!-- Background -->
            <rect x="15" y="15" width="280" height="230" rx="4" fill='#161b22' stroke='#30363d' stroke-width="1"/>

            <!-- Origin -->
            <circle cx="55" cy="200" r="5" fill='#4f8ef7'/>
            <text x="38" y="218" fill='currentColor' font-size='12' font-family='sans-serif'>O</text>

            <!-- Vector endpoint -->
            <circle cx="210" cy="80" r="5" fill='#2da44e'/>
            <text x="218" y="75" fill='currentColor' font-size='12' font-family='sans-serif'>P(x, y)</text>

            <!-- Vector arrow -->
            <line x1="55" y1="200" x2="207" y2="83" stroke='#4f8ef7' stroke-width="2.5" marker-end="url(#arrow6)"/>
            <text x="100" y="130" fill='#4f8ef7' font-size='13' font-weight='bold' font-family='sans-serif'>v</text>

            <!-- Right triangle -->
            <line x1="55" y1="200" x2="210" y2="200" stroke='#8b949e' stroke-width="1.5" stroke-dasharray="3,3" opacity="0.5"/>
            <line x1="210" y1="200" x2="210" y2="80" stroke='#8b949e' stroke-width="1.5" stroke-dasharray="3,3" opacity="0.5"/>

            <!-- Right angle indicator -->
            <rect x="200" y="190" width="10" height="10" fill='none' stroke='#8b949e' stroke-width="1" opacity="0.5"/>

            <!-- Labels -->
            <text x="132" y="218" fill='currentColor' opacity='0.6' font-size='12' font-family='sans-serif' text-anchor='middle'>x</text>
            <text x="225" y="145" fill='currentColor' opacity='0.6' font-size='12' font-family='sans-serif'>y</text>

            <!-- Magnitude label -->
            <text x="155" y="50" fill='#f85149' font-size='12' font-weight='bold' font-family='sans-serif' text-anchor='middle'>|v| = &#8730;(x&#178; + y&#178;)</text>
        </svg>

        <div class="worked-example">
            <p><strong>Example 1:</strong> Find the magnitude of \\(\\vec{v} = \\begin{pmatrix} 3 \\\\ 4 \\end{pmatrix}\\)</p>
            <p>\\(|\\vec{v}| = \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5\\)</p>
            <p>This is the famous 3-4-5 right triangle!</p>
        </div>

        <div class="worked-example">
            <p><strong>Example 2:</strong> Find the magnitude of \\(\\vec{u} = \\begin{pmatrix} -2 \\\\ 1 \\end{pmatrix}\\)</p>
            <p>\\(|\\vec{u}| = \\sqrt{(-2)^2 + 1^2} = \\sqrt{4 + 1} = \\sqrt{5} \\approx 2.24\\)</p>
        </div>

        <h4>Properties of Magnitude</h4>

        <div class="concept-box">
            <ul>
                <li>\\(|\\vec{v}| \\geq 0\\) always (magnitude is never negative)</li>
                <li>\\(|\\vec{v}| = 0\\) only if \\(\\vec{v} = \\vec{0}\\) (zero vector)</li>
                <li>\\(|k\\vec{v}| = |k| \\cdot |\\vec{v}|\\) (scaling a vector scales its magnitude)</li>
                <li>\\(|\\vec{v}|^2 = \\vec{v} \\cdot \\vec{v}\\) (the square of magnitude equals the dot product of a vector with itself)</li>
            </ul>
        </div>
        """
    },
    {
        "title": "Unit Vectors: Vectors with Magnitude 1",
        "body": """
        <h3>What is a Unit Vector?</h3>

        <p>A <strong>unit vector</strong> is any vector with magnitude exactly 1. Unit vectors are useful because they represent pure direction—no scaling involved.</p>

        <div class="concept-box">
            <p><strong>\\(\\hat{u}\\) is a unit vector ⟺ \\(|\\hat{u}| = 1\\)</strong></p>
        </div>

        <h4>How to Convert Any Vector to a Unit Vector</h4>

        <p>To find a unit vector in the same direction as \\(\\vec{v}\\), divide by its magnitude:</p>

        <div class="concept-box">
            <p style="text-align: center; font-size: 1.1em;">\\(\\hat{v} = \\frac{\\vec{v}}{|\\vec{v}|}\\)</p>
        </div>

        <p>This process is called <strong>normalization</strong>.</p>

        <div class="worked-example">
            <p><strong>Example 3:</strong> Find the unit vector in the direction of \\(\\vec{v} = \\begin{pmatrix} 3 \\\\ 4 \\end{pmatrix}\\)</p>

            <p class="concept-box">
                Step 1: Find the magnitude: \\(|\\vec{v}| = \\sqrt{9 + 16} = 5\\)
            </p>

            <p class="concept-box">
                Step 2: Divide by the magnitude: \\(\\hat{v} = \\frac{1}{5}\\begin{pmatrix} 3 \\\\ 4 \\end{pmatrix} = \\begin{pmatrix} 0.6 \\\\ 0.8 \\end{pmatrix}\\)
            </p>

            <p class="concept-box">
                Step 3: Verify: \\(|\\hat{v}| = \\sqrt{0.6^2 + 0.8^2} = \\sqrt{0.36 + 0.64} = \\sqrt{1} = 1\\) ✓
            </p>
        </div>

        <h3>Standard Unit Vectors: \\(\\vec{i}\\) and \\(\\vec{j}\\)</h3>

        <p>In 2D, there are two special standard unit vectors that point along the coordinate axes:</p>

        <div class="concept-box">
            <p style="text-align: center;">
                \\(\\vec{i} = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix}\\) (points along the positive x-axis)
            </p>
            <p style="text-align: center;">
                \\(\\vec{j} = \\begin{pmatrix} 0 \\\\ 1 \\end{pmatrix}\\) (points along the positive y-axis)
            </p>
        </div>

        <h4>Writing Vectors Using Unit Vectors</h4>

        <p>Any 2D vector can be written as a combination of \\(\\vec{i}\\) and \\(\\vec{j}\\):</p>

        <div class="concept-box">
            <p style="text-align: center; font-size: 1.1em;">\\(\\vec{v} = \\begin{pmatrix} x \\\\ y \\end{pmatrix} = x\\vec{i} + y\\vec{j}\\)</p>
        </div>

        <div class="worked-example">
            <p><strong>Example 4:</strong> Express \\(\\vec{v} = \\begin{pmatrix} -2 \\\\ 5 \\end{pmatrix}\\) using \\(\\vec{i}\\) and \\(\\vec{j}\\)</p>
            <p>\\(\\vec{v} = -2\\vec{i} + 5\\vec{j}\\)</p>
        </div>

        <svg viewBox="0 0 370 230" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:400px; margin:20px auto; display:block;">
            <defs>
                <marker id="arrow7i" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7' />
                </marker>
                <marker id="arrow7j" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#2da44e' />
                </marker>
                <marker id="arrow7r" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#f85149' />
                </marker>
            </defs>
            <!-- Background -->
            <rect x="15" y="15" width="340" height="200" rx="4" fill='#161b22' stroke='#30363d' stroke-width="1"/>

            <!-- Axes -->
            <line x1="35" y1="170" x2="340" y2="170" stroke='#30363d' stroke-width="1"/>
            <line x1="85" y1="30" x2="85" y2="200" stroke='#30363d' stroke-width="1"/>
            <text x="335" y="185" fill='currentColor' opacity='0.5' font-size='11' font-family='sans-serif'>x</text>
            <text x="70" y="38" fill='currentColor' opacity='0.5' font-size='11' font-family='sans-serif'>y</text>

            <!-- Origin -->
            <circle cx="85" cy="170" r="4" fill='currentColor'/>
            <text x="68" y="190" fill='currentColor' font-size='12' font-family='sans-serif'>O</text>

            <!-- i vector (x-direction) -->
            <line x1="85" y1="170" x2="145" y2="170" stroke='#4f8ef7' stroke-width="2.5" marker-end="url(#arrow7i)"/>
            <text x="115" y="162" fill='#4f8ef7' font-size='13' font-weight='bold' font-family='sans-serif'>i</text>

            <!-- j vector (y-direction) -->
            <line x1="85" y1="170" x2="85" y2="110" stroke='#2da44e' stroke-width="2.5" marker-end="url(#arrow7j)"/>
            <text x="65" y="140" fill='#2da44e' font-size='13' font-weight='bold' font-family='sans-serif'>j</text>

            <!-- Example title -->
            <text x="250" y="42" fill='currentColor' font-size='12' font-weight='bold' font-family='sans-serif' text-anchor='middle'>Example: 2i + 3j</text>

            <!-- 2i part (horizontal dashed) -->
            <line x1="190" y1="170" x2="250" y2="170" stroke='#4f8ef7' stroke-width="2" stroke-dasharray="3,3"/>
            <text x="220" y="188" fill='#4f8ef7' font-size='11' font-family='sans-serif' text-anchor='middle'>2i</text>

            <!-- 3j part (vertical dashed) -->
            <line x1="250" y1="170" x2="250" y2="80" stroke='#2da44e' stroke-width="2" stroke-dasharray="3,3"/>
            <text x="264" y="130" fill='#2da44e' font-size='11' font-family='sans-serif'>3j</text>

            <!-- Result vector -->
            <line x1="190" y1="170" x2="247" y2="83" stroke='#f85149' stroke-width="2.5" marker-end="url(#arrow7r)"/>
            <text x="200" y="120" fill='#f85149' font-size='12' font-weight='bold' font-family='sans-serif'>Result</text>

            <!-- Result point -->
            <circle cx="250" cy="80" r="4" fill='#f85149'/>
        </svg>
        """
    },
    {
        "title": "Applications: Using Magnitude and Direction",
        "body": """
        <h3>Real-World Applications</h3>

        <h4>Application 1: Normalizing Force Vectors</h4>

        <p>In engineering, we often need to apply a force in a specific direction with magnitude 1 (unit force) as a reference or scaling standard.</p>

        <div class="worked-example">
            <p><strong>Problem:</strong> A force vector is \\(\\vec{F} = \\begin{pmatrix} 6 \\\\ 8 \\end{pmatrix}\\) N. Find the unit force vector in the same direction.</p>

            <p class="concept-box">
                \\(|\\vec{F}| = \\sqrt{36 + 64} = \\sqrt{100} = 10\\) N
            </p>

            <p class="concept-box">
                \\(\\hat{F} = \\frac{\\vec{F}}{10} = \\begin{pmatrix} 0.6 \\\\ 0.8 \\end{pmatrix}\\) (unit vector in the direction of F)
            </p>
        </div>

        <h4>Application 2: Finding Displacement Magnitude</h4>

        <p>A ship travels from port A to port B. Given position vectors (in km), find the straight-line distance.</p>

        <div class="worked-example">
            <p><strong>Problem:</strong> Port A is at (10, 20) and Port B is at (40, 50) (in km). What's the straight-line distance?</p>

            <p class="concept-box">
                \\(\\vec{AB} = \\begin{pmatrix} 40-10 \\\\ 50-20 \\end{pmatrix} = \\begin{pmatrix} 30 \\\\ 30 \\end{pmatrix}\\) km
            </p>

            <p class="concept-box">
                Distance = \\(|\\vec{AB}| = \\sqrt{900 + 900} = \\sqrt{1800} = 30\\sqrt{2} \\approx 42.4\\) km
            </p>
        </div>

        <h4>Application 3: Velocity Direction with Constant Speed</h4>

        <p>A car needs to travel in direction \\(\\vec{d} = \\begin{pmatrix} 3 \\\\ -4 \\end{pmatrix}\\) at a speed of 10 m/s. Find the velocity vector.</p>

        <div class="worked-example">
            <p><strong>Solution:</strong></p>

            <p class="concept-box">
                Step 1: Find the unit direction: \\(\\hat{d} = \\frac{\\begin{pmatrix} 3 \\\\ -4 \\end{pmatrix}}{5} = \\begin{pmatrix} 0.6 \\\\ -0.8 \\end{pmatrix}\\)
            </p>

            <p class="concept-box">
                Step 2: Multiply by speed: \\(\\vec{v} = 10 \\cdot \\hat{d} = \\begin{pmatrix} 6 \\\\ -8 \\end{pmatrix}\\) m/s
            </p>

            <p class="concept-box">
                Check: \\(|\\vec{v}| = \\sqrt{36 + 64} = 10\\) m/s ✓
            </p>
        </div>

        <div class="success-box">
            <p><strong>General Pattern:</strong> To create a vector of magnitude m in direction \\(\\vec{d}\\):</p>
            <p style="text-align: center;">\\(\\vec{v} = m \\cdot \\hat{d} = m \\cdot \\frac{\\vec{d}}{|\\vec{d}|}\\)</p>
        </div>
        """
    }
]
