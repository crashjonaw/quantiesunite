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

        <svg viewBox="0 0 450 210" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; margin: 20px 0;">
            <defs>
                <marker id="arrowBlue" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7' />
                </marker>
                <marker id="arrowGreen" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#2da44e' />
                </marker>
                <marker id="arrowRed" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#f85149' />
                </marker>
            </defs>

            <!-- Left diagram: Triangle rule -->
            <rect x="15" y="15" width="195" height="180" rx="4" fill='#161b22' stroke='#30363d' stroke-width="1"/>
            <text x="112" y="38" fill='currentColor' font-size='13' font-weight='bold' font-family='sans-serif' text-anchor='middle'>Triangle Rule</text>

            <!-- Start point A -->
            <circle cx="35" cy="110" r="4" fill='#4f8ef7'/>
            <text x="28" y="130" fill='currentColor' font-size='11' font-family='sans-serif'>A</text>

            <!-- Vector u: A to B -->
            <line x1="35" y1="110" x2="135" y2="110" stroke='#4f8ef7' stroke-width="2.5" marker-end="url(#arrowBlue)"/>
            <text x="85" y="100" fill='#4f8ef7' font-size='12' font-weight='bold' font-family='sans-serif' text-anchor='middle'>u</text>

            <!-- Point B -->
            <circle cx="140" cy="110" r="4" fill='#4f8ef7'/>
            <text x="145" y="100" fill='currentColor' font-size='11' font-family='sans-serif'>B</text>

            <!-- Vector v: B to C -->
            <line x1="140" y1="110" x2="175" y2="170" stroke='#2da44e' stroke-width="2.5" marker-end="url(#arrowGreen)"/>
            <text x="167" y="138" fill='#2da44e' font-size='12' font-weight='bold' font-family='sans-serif'>v</text>

            <!-- Point C -->
            <circle cx="178" cy="173" r="4" fill='#2da44e'/>
            <text x="183" y="170" fill='currentColor' font-size='11' font-family='sans-serif'>C</text>

            <!-- Resultant: A to C -->
            <line x1="35" y1="110" x2="175" y2="170" stroke='#f85149' stroke-width="2.5" stroke-dasharray="5,3" marker-end="url(#arrowRed)"/>
            <text x="90" y="155" fill='#f85149' font-size='11' font-weight='bold' font-family='sans-serif'>u + v</text>

            <!-- Right diagram: Parallelogram rule -->
            <rect x="240" y="15" width="195" height="180" rx="4" fill='#161b22' stroke='#30363d' stroke-width="1"/>
            <text x="337" y="38" fill='currentColor' font-size='13' font-weight='bold' font-family='sans-serif' text-anchor='middle'>Parallelogram Rule</text>

            <!-- Origin O -->
            <circle cx="265" cy="140" r="4" fill='#4f8ef7'/>
            <text x="252" y="155" fill='currentColor' font-size='11' font-family='sans-serif'>O</text>

            <!-- Vector u to the right -->
            <line x1="265" y1="140" x2="370" y2="140" stroke='#4f8ef7' stroke-width="2.5" marker-end="url(#arrowBlue)"/>
            <text x="315" y="158" fill='#4f8ef7' font-size='12' font-weight='bold' font-family='sans-serif' text-anchor='middle'>u</text>

            <!-- Vector v upward -->
            <line x1="265" y1="140" x2="295" y2="70" stroke='#2da44e' stroke-width="2.5" marker-end="url(#arrowGreen)"/>
            <text x="268" y="100" fill='#2da44e' font-size='12' font-weight='bold' font-family='sans-serif'>v</text>

            <!-- Parallelogram sides (dashed) -->
            <line x1="375" y1="140" x2="405" y2="70" stroke='#8b949e' stroke-width="1" stroke-dasharray="3,3" opacity="0.5"/>
            <line x1="300" y1="70" x2="405" y2="70" stroke='#8b949e' stroke-width="1" stroke-dasharray="3,3" opacity="0.5"/>

            <!-- Diagonal (sum) -->
            <line x1="265" y1="140" x2="402" y2="70" stroke='#f85149' stroke-width="2.5" marker-end="url(#arrowRed)"/>
            <text x="345" y="92" fill='#f85149' font-size='11' font-weight='bold' font-family='sans-serif'>u + v</text>

            <!-- Corner point -->
            <circle cx="405" cy="70" r="4" fill='#f85149'/>
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
                <marker id="arrow3r" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#f85149' />
                </marker>
                <marker id="arrow3g" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#2da44e' />
                </marker>
                <marker id="arrow3b" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7' />
                </marker>
                <marker id="arrow3grey" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#8b949e' />
                </marker>
            </defs>
            <!-- Background -->
            <rect x="15" y="15" width="490" height="170" rx="4" fill='#161b22' stroke='#30363d' stroke-width="1"/>

            <!-- k < 0: reverses direction -->
            <text x="55" y="42" fill='currentColor' font-size='11' font-weight='bold' font-family='sans-serif' text-anchor='middle'>k = -2</text>
            <text x="55" y="56" fill='currentColor' opacity='0.6' font-size='10' font-family='sans-serif' text-anchor='middle'>reverse + scale</text>
            <circle cx="80" cy="85" r="3" fill='#f85149'/>
            <line x1="78" y1="85" x2="25" y2="85" stroke='#f85149' stroke-width="2.5" marker-end="url(#arrow3r)"/>

            <!-- 0 < k < 1: shrinks -->
            <text x="185" y="42" fill='currentColor' font-size='11' font-weight='bold' font-family='sans-serif' text-anchor='middle'>k = 0.5</text>
            <text x="185" y="56" fill='currentColor' opacity='0.6' font-size='10' font-family='sans-serif' text-anchor='middle'>shrink</text>
            <circle cx="170" cy="85" r="3" fill='#2da44e'/>
            <line x1="173" y1="85" x2="200" y2="85" stroke='#2da44e' stroke-width="2.5" marker-end="url(#arrow3g)"/>

            <!-- k > 1: stretches -->
            <text x="335" y="42" fill='currentColor' font-size='11' font-weight='bold' font-family='sans-serif' text-anchor='middle'>k = 2</text>
            <text x="335" y="56" fill='currentColor' opacity='0.6' font-size='10' font-family='sans-serif' text-anchor='middle'>stretch</text>
            <circle cx="295" cy="85" r="3" fill='#4f8ef7'/>
            <line x1="298" y1="85" x2="378" y2="85" stroke='#4f8ef7' stroke-width="2.5" marker-end="url(#arrow3b)"/>

            <!-- k = 0: zero vector -->
            <text x="460" y="42" fill='currentColor' font-size='11' font-weight='bold' font-family='sans-serif' text-anchor='middle'>k = 0</text>
            <text x="460" y="56" fill='currentColor' opacity='0.6' font-size='10' font-family='sans-serif' text-anchor='middle'>disappears</text>
            <circle cx="460" cy="85" r="5" fill='currentColor' opacity='0.4'/>
            <text x="460" y="108" fill='currentColor' opacity='0.5' font-size='10' font-family='sans-serif' text-anchor='middle'>zero vector</text>

            <!-- Reference vector -->
            <text x="100" y="155" fill='currentColor' opacity='0.6' font-size='11' font-family='sans-serif'>Original v</text>
            <circle cx="165" cy="150" r="3" fill='#8b949e'/>
            <line x1="168" y1="150" x2="228" y2="150" stroke='#8b949e' stroke-width="2" marker-end="url(#arrow3grey)"/>
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
