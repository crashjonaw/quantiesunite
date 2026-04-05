TITLE = "Vector Operations"

SECTIONS = [
    {
        "title": "Vector Addition: The Triangle and Parallelogram Rules",
        "body": """
        <h3>Why Add Vectors?</h3>
        <p>In real life, we combine forces, velocities, and displacements. Understanding how to add vectors is essential for physics and engineering.</p>

        <h4>Adding Vectors Algebraically</h4>
        <p>To add two vectors, simply add their corresponding components:</p>

        <div class="concept-box">
            <p style="text-align: center;">
                \\(\\vec{u} + \\vec{v} = \\begin{pmatrix} a \\\\ b \\end{pmatrix} + \\begin{pmatrix} c \\\\ d \\end{pmatrix} = \\begin{pmatrix} a+c \\\\ b+d \\end{pmatrix}\\)
            </p>
        </div>

        <div class="worked-example">
            <p><strong>Example 1:</strong> Add \\(\\vec{u} = \\begin{pmatrix} 2 \\\\ 3 \\end{pmatrix}\\) and \\(\\vec{v} = \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix}\\)</p>
            <p>\\(\\vec{u} + \\vec{v} = \\begin{pmatrix} 2+1 \\\\ 3+(-1) \\end{pmatrix} = \\begin{pmatrix} 3 \\\\ 2 \\end{pmatrix}\\)</p>
        </div>

        <h4>Adding Vectors Geometrically: The Triangle Rule</h4>
        <p>To visualize vector addition, place the tail of the second vector at the head of the first. The sum is the vector from start to end:</p>

        <svg viewBox="0 0 420 250" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; margin: 20px 0;">
            <defs>
                <marker id="arrowHead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7' />
                </marker>
            </defs>

            <!-- Left diagram: Triangle rule -->
            <text x="100" y="20" fill='#e6edf3' font-size='14' font-weight='bold'>Triangle Rule: \\(\\vec{u} + \\vec{v}\\)</text>

            <!-- Start point -->
            <circle cx="50" cy="100" r="4" fill='#4f8ef7'/>
            <text x="35" y="105" fill='#8b949e' font-size='12'>A</text>

            <!-- First vector u -->
            <line x1="50" y1="100" x2="150" y2="100" stroke='#4f8ef7' stroke-width="2.5" marker-end="url(#arrowHead)"/>
            <text x="100" y="85" fill='#4f8ef7' font-size='12' font-weight='bold'>\\(\\vec{u}\\)</text>

            <!-- End of u (point B) -->
            <circle cx="150" cy="100" r="4" fill='#4f8ef7'/>
            <text x="150" y="85" fill='#8b949e' font-size='12'>B</text>

            <!-- Second vector v from B -->
            <line x1="150" y1="100" x2="180" y2="160" stroke='#2da44e' stroke-width="2.5" marker-end="url(#arrowHead)"/>
            <text x="155" y="135" fill='#2da44e' font-size='12' font-weight='bold'>\\(\\vec{v}\\)</text>

            <!-- End of v (point C) -->
            <circle cx="180" cy="160" r="4" fill='#2da44e'/>
            <text x="185" y="160" fill='#8b949e' font-size='12'>C</text>

            <!-- Resultant from A to C -->
            <line x1="50" y1="100" x2="180" y2="160" stroke='#f85149' stroke-width="3" stroke-dasharray="4,4" marker-end="url(#arrowHead)"/>
            <text x="105" y="125" fill='#f85149' font-size='12' font-weight='bold'>\\(\\vec{u}+\\vec{v}\\)</text>

            <!-- Right diagram: Parallelogram rule -->
            <text x="280" y="20" fill='#e6edf3' font-size='14' font-weight='bold'>Parallelogram Rule</text>

            <!-- Start point -->
            <circle cx="230" cy="100" r="4" fill='#4f8ef7'/>
            <text x="215" y="105" fill='#8b949e' font-size='12'>O</text>

            <!-- Vector u to the right -->
            <line x1="230" y1="100" x2="330" y2="100" stroke='#4f8ef7' stroke-width="2.5" marker-end="url(#arrowHead)"/>
            <text x="280" y="85" fill='#4f8ef7' font-size='11' font-weight='bold'>\\(\\vec{u}\\)</text>

            <!-- Vector v upward -->
            <line x1="230" y1="100" x2="260" y2="50" stroke='#2da44e' stroke-width="2.5" marker-end="url(#arrowHead)"/>
            <text x="235" y="70" fill='#2da44e' font-size='11' font-weight='bold'>\\(\\vec{v}\\)</text>

            <!-- Parallelogram sides -->
            <line x1="330" y1="100" x2="360" y2="50" stroke='#30363d' stroke-width="1" stroke-dasharray="2,2"/>
            <line x1="260" y1="50" x2="360" y2="50" stroke='#30363d' stroke-width="1" stroke-dasharray="2,2"/>

            <!-- Diagonal (sum) -->
            <line x1="230" y1="100" x2="360" y2="50" stroke='#f85149' stroke-width="3" marker-end="url(#arrowHead)"/>
            <text x="290" y="80" fill='#f85149' font-size='11' font-weight='bold'>\\(\\vec{u}+\\vec{v}\\)</text>

            <!-- Corner point -->
            <circle cx="360" cy="50" r="4" fill='#f85149'/>
        </svg>

        <p style="text-align: center; margin-top: 20px">
            <strong>Key insight:</strong> Both methods give the same result. Triangle rule is more intuitive; parallelogram rule shows symmetry.
        </p>
        """
    },
    {
        "title": "Vector Subtraction and Scalar Multiplication",
        "body": """
        <h3>Subtraction: Adding Negative Vectors</h3>

        <p>Vector subtraction works by adding the negative (opposite) vector:</p>

        <div class="concept-box">
            <p style="text-align: center;">
                \\(\\vec{u} - \\vec{v} = \\vec{u} + (-\\vec{v}) = \\begin{pmatrix} a \\\\ b \\end{pmatrix} - \\begin{pmatrix} c \\\\ d \\end{pmatrix} = \\begin{pmatrix} a-c \\\\ b-d \\end{pmatrix}\\)
            </p>
        </div>

        <div class="worked-example">
            <p><strong>Example 2:</strong> Calculate \\(\\vec{u} - \\vec{v}\\) where \\(\\vec{u} = \\begin{pmatrix} 5 \\\\ 2 \\end{pmatrix}\\) and \\(\\vec{v} = \\begin{pmatrix} 1 \\\\ -3 \\end{pmatrix}\\)</p>
            <p>\\(\\vec{u} - \\vec{v} = \\begin{pmatrix} 5-1 \\\\ 2-(-3) \\end{pmatrix} = \\begin{pmatrix} 4 \\\\ 5 \\end{pmatrix}\\)</p>
        </div>

        <h3>Scalar Multiplication: Stretching and Shrinking</h3>

        <p>When we multiply a vector by a scalar (real number), we scale its magnitude and possibly reverse its direction:</p>

        <div class="concept-box">
            <p style="text-align: center;">
                \\(k\\vec{v} = k\\begin{pmatrix} a \\\\ b \\end{pmatrix} = \\begin{pmatrix} ka \\\\ kb \\end{pmatrix}\\)
            </p>
        </div>

        <h4>What Different Scalars Do</h4>

        <svg viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; margin: 20px 0;">
            <defs>
                <marker id="arrow3" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#e6edf3' />
                </marker>
            </defs>

            <!-- k < 0: reverses direction -->
            <text x="20" y="25" fill='#e6edf3' font-size='12' font-weight='bold'>k = -2 (reverse &amp; scale)</text>
            <circle cx="50" cy="70" r="3" fill='#e6edf3'/>
            <line x1="50" y1="70" x2="10" y2="70" stroke='#f85149' stroke-width="2.5" marker-end="url(#arrow3)"/>

            <!-- 0 < k < 1: shrinks -->
            <text x="140" y="25" fill='#e6edf3' font-size='12' font-weight='bold'>k = 0.5 (shrink)</text>
            <circle cx="170" cy="70" r="3" fill='#e6edf3'/>
            <line x1="170" y1="70" x2="190" y2="70" stroke='#2da44e' stroke-width="2.5" marker-end="url(#arrow3)"/>

            <!-- k > 1: stretches -->
            <text x="250" y="25" fill='#e6edf3' font-size='12' font-weight='bold'>k = 2 (stretch)</text>
            <circle cx="280" cy="70" r="3" fill='#e6edf3'/>
            <line x1="280" y1="70" x2="350" y2="70" stroke='#4f8ef7' stroke-width="2.5" marker-end="url(#arrow3)"/>

            <!-- k = 0: zero vector -->
            <text x="410" y="25" fill='#e6edf3' font-size='12' font-weight='bold'>k = 0 (disappears)</text>
            <circle cx="440" cy="70" r="4" fill='#8b949e'/>
            <text x="435" y="100" fill='#8b949e' font-size='11' text-anchor='middle'>zero vector</text>

            <!-- Reference vector -->
            <text x="50" y="160" fill='#8b949e' font-size='11'>Original \\(\\vec{v}\\) →</text>
            <circle cx="50" cy="140" r="3" fill='#8b949e'/>
            <line x1="50" y1="140" x2="110" y2="140" stroke='#8b949e' stroke-width="2" marker-end="url(#arrow3)"/>
        </svg>

        <div class="worked-example">
            <p><strong>Example 3:</strong> Scalar multiplication examples</p>
            <p>If \\(\\vec{v} = \\begin{pmatrix} 2 \\\\ -3 \\end{pmatrix}\\), find 3\\(\\vec{v}\\) and -2\\(\\vec{v}\\)</p>
            <p>\\(3\\vec{v} = 3\\begin{pmatrix} 2 \\\\ -3 \\end{pmatrix} = \\begin{pmatrix} 6 \\\\ -9 \\end{pmatrix}\\) ← stretches to 3 times the size</p>
            <p>\\(-2\\vec{v} = -2\\begin{pmatrix} 2 \\\\ -3 \\end{pmatrix} = \\begin{pmatrix} -4 \\\\ 6 \\end{pmatrix}\\) ← reverses direction and doubles size</p>
        </div>
        """
    },
    {
        "title": "Properties of Vector Operations and Resultants",
        "body": """
        <h3>The Algebra of Vectors</h3>

        <p>Vector addition and scalar multiplication follow familiar rules:</p>

        <div class="concept-box">
            <p><strong>Commutative:</strong> \\(\\vec{u} + \\vec{v} = \\vec{v} + \\vec{u}\\)</p>
            <p><strong>Associative:</strong> \\((\\vec{u} + \\vec{v}) + \\vec{w} = \\vec{u} + (\\vec{v} + \\vec{w})\\)</p>
            <p><strong>Identity:</strong> \\(\\vec{u} + \\vec{0} = \\vec{u}\\) (zero vector is the additive identity)</p>
            <p><strong>Inverse:</strong> \\(\\vec{u} + (-\\vec{u}) = \\vec{0}\\) (each vector has an opposite)</p>
        </div>

        <h4>Distributive Properties for Scalar Multiplication</h4>

        <div class="concept-box">
            <p><strong>Distributes over vector addition:</strong> \\(k(\\vec{u} + \\vec{v}) = k\\vec{u} + k\\vec{v}\\)</p>
            <p><strong>Distributes over scalar addition:</strong> \\((k+m)\\vec{v} = k\\vec{v} + m\\vec{v}\\)</p>
            <p><strong>Associative with scalars:</strong> \\(k(m\\vec{v}) = (km)\\vec{v}\\)</p>
        </div>

        <h3>Resultant Vectors: Combining Multiple Forces</h3>

        <p>In physics, a <strong>resultant</strong> is the single vector that has the same effect as multiple combined vectors. This is why vector addition matters!</p>

        <div class="worked-example">
            <p><strong>Example 4:</strong> Three forces act on a particle:</p>
            <p>\\(\\vec{F}_1 = \\begin{pmatrix} 3 \\\\ 4 \\end{pmatrix}\\) N</p>
            <p>\\(\\vec{F}_2 = \\begin{pmatrix} -1 \\\\ 2 \\end{pmatrix}\\) N</p>
            <p>\\(\\vec{F}_3 = \\begin{pmatrix} 2 \\\\ -3 \\end{pmatrix}\\) N</p>
            <p>Find the resultant force.</p>

            <p style="margin-top: 15px; padding: 10px">
                <strong>Resultant:</strong> \\(\\vec{F}_1 + \\vec{F}_2 + \\vec{F}_3 = \\begin{pmatrix} 3-1+2 \\\\ 4+2-3 \\end{pmatrix} = \\begin{pmatrix} 4 \\\\ 3 \\end{pmatrix}\\) N
            </p>
        </div>

        <div class="success-box">
            <p><strong>Why this matters:</strong> Instead of tracking three separate forces, we can replace them with a single resultant force of \\(\\begin{pmatrix} 4 \\\\ 3 \\end{pmatrix}\\) N. The effect on the particle is identical.</p>
        </div>
        """
    }
]
