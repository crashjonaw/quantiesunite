TITLE = "Position Vectors"

SECTIONS = [
    {
        "title": "Position Vectors: Locating Points with Vectors",
        "body": """
        <h3>Anchoring Vectors to the Origin</h3>

        <p>So far, we've treated vectors as "free"—they can start anywhere. But when we anchor a vector at the origin O(0, 0), we get a <strong>position vector</strong>.</p>

        <div class="concept-box">
            <p>The <strong>position vector</strong> of a point P(x, y) is the vector from the origin O to P:</p>
            <p style="text-align: center; font-size: 1.1em;">\\(\\vec{OP} = \\begin{pmatrix} x \\\\ y \\end{pmatrix}\\)</p>
        </div>

        <p>In other words: <strong>The coordinates of a point ARE its position vector.</strong></p>

        <div class="worked-example">
            <p><strong>Example 1:</strong> Find the position vectors of these points:</p>
            <ul>
                <li>Point A(3, 2): Position vector \\(\\vec{OA} = \\begin{pmatrix} 3 \\\\ 2 \\end{pmatrix}\\)</li>
                <li>Point B(-1, 4): Position vector \\(\\vec{OB} = \\begin{pmatrix} -1 \\\\ 4 \\end{pmatrix}\\)</li>
                <li>Point C(0, -5): Position vector \\(\\vec{OC} = \\begin{pmatrix} 0 \\\\ -5 \\end{pmatrix}\\)</li>
            </ul>
        </div>

        <h4>Visual Representation</h4>

        <svg viewBox="0 0 320 280" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:400px; margin:20px auto; display:block;">
            <defs>
                <marker id="arrow4" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7' />
                </marker>
            </defs>

            <!-- Axes -->
            <line x1="30" y1="200" x2="280" y2="200" stroke='#30363d' stroke-width="1.5"/>
            <line x1="30" y1="30" x2="30" y2="200" stroke='#30363d' stroke-width="1.5"/>

            <!-- Grid -->
            <line x1="30" y1="120" x2="280" y2="120" stroke='#30363d' stroke-width="0.5" opacity='0.3'/>
            <line x1="30" y1="40" x2="280" y2="40" stroke='#30363d' stroke-width="0.5" opacity='0.3'/>
            <line x1="30" y1="160" x2="280" y2="160" stroke='#30363d' stroke-width="0.5" opacity='0.3'/>
            <line x1="110" y1="30" x2="110" y2="200" stroke='#30363d' stroke-width="0.5" opacity='0.3'/>
            <line x1="190" y1="30" x2="190" y2="200" stroke='#30363d' stroke-width="0.5" opacity='0.3'/>
            <line x1="270" y1="30" x2="270" y2="200" stroke='#30363d' stroke-width="0.5" opacity='0.3'/>

            <!-- Origin -->
            <circle cx="30" cy="200" r="5" fill='#4f8ef7'/>
            <text x="15" y="220" fill='currentColor' font-size='12' font-weight='bold'>O</text>

            <!-- Point P(3, 2) -->
            <circle cx="270" cy="40" r="5" fill='#2da44e'/>
            <text x="275" y="35" fill='currentColor' font-size='12'>P(3, 2)</text>

            <!-- Position vector OP -->
            <line x1="30" y1="200" x2="270" y2="40" stroke='#2da44e' stroke-width="2.5" marker-end="url(#arrow4)"/>
            <text x="70" y="175" fill='#2da44e' font-size='11' font-weight='bold'>\\(\\vec{OP}\\)</text>

            <!-- Dashed construction -->
            <line x1="270" y1="200" x2="270" y2="40" stroke='#8b949e' stroke-width="1" stroke-dasharray="2,2" opacity='0.6'/>
            <line x1="30" y1="200" x2="270" y2="200" stroke='#8b949e' stroke-width="1" stroke-dasharray="2,2" opacity='0.6'/>

            <!-- Component labels -->
            <text x="150" y="210" fill='currentColor' opacity='0.6' font-size='10' text-anchor='middle'>3</text>
            <text x="280" y="120" fill='currentColor' opacity='0.6' font-size='10'>2</text>

            <!-- Axis labels -->
            <text x="270" y="215" fill='currentColor' opacity='0.6' font-size='11'>x</text>
            <text x="15" y="25" fill='currentColor' opacity='0.6' font-size='11'>y</text>
        </svg>

        <p style="text-align: center; margin-top: 15px">
            The position vector points directly from the origin to the point.
        </p>
        """
    },
    {
        "title": "Vectors Between Two Points and Finding Distances",
        "body": """
        <h3>How to Find a Vector from A to B</h3>

        <p>We often need to find the vector between two arbitrary points. The key insight is to use position vectors:</p>

        <div class="concept-box">
            <p>If points A and B have position vectors \\(\\vec{a}\\) and \\(\\vec{b}\\):</p>
            <p style="text-align: center; font-size: 1.1em;">\\(\\vec{AB} = \\vec{b} - \\vec{a}\\)</p>
        </div>

        <p><strong>Why this works:</strong> We travel from O to A (vector \\(\\vec{a}\\)), then from A to B (vector \\(\\vec{AB}\\)). These add up to \\(\\vec{b}\\), so \\(\\vec{AB} = \\vec{b} - \\vec{a}\\).</p>

        <div class="worked-example">
            <p><strong>Example 2:</strong> Find \\(\\vec{AB}\\) where A(1, 2) and B(5, 6)</p>
            <p>\\(\\vec{a} = \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix}\\), \\(\\vec{b} = \\begin{pmatrix} 5 \\\\ 6 \\end{pmatrix}\\)</p>
            <p>\\(\\vec{AB} = \\vec{b} - \\vec{a} = \\begin{pmatrix} 5 \\\\ 6 \\end{pmatrix} - \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix} = \\begin{pmatrix} 4 \\\\ 4 \\end{pmatrix}\\)</p>
            <p>So the displacement from A to B is 4 units right and 4 units up.</p>
        </div>

        <h4>Finding the Distance Between Points</h4>

        <p>The magnitude of the vector \\(\\vec{AB}\\) is the straight-line distance from A to B:</p>

        <div class="concept-box">
            <p style="text-align: center;">\\(|AB| = |\\vec{AB}| = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}\\)</p>
        </div>

        <div class="worked-example">
            <p><strong>Example 3:</strong> Find the distance from A(1, 2) to B(5, 6)</p>
            <p>\\(|AB| = \\sqrt{(5-1)^2 + (6-2)^2} = \\sqrt{16 + 16} = \\sqrt{32} = 4\\sqrt{2} \\approx 5.66\\)</p>
        </div>

        <svg viewBox="0 0 300 280" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:400px; margin:20px auto; display:block;">
            <defs>
                <marker id="arrow5" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <polygon points="0 0, 10 3, 0 6" fill='#f85149' />
                </marker>
            </defs>

            <!-- Axes -->
            <line x1="30" y1="200" x2="280" y2="200" stroke='#30363d' stroke-width="1.5"/>
            <line x1="30" y1="30" x2="30" y2="200" stroke='#30363d' stroke-width="1.5"/>

            <!-- Point A -->
            <circle cx="60" cy="140" r="5" fill='#4f8ef7'/>
            <text x="45" y="135" fill='currentColor' font-size='12'>A(1,2)</text>

            <!-- Point B -->
            <circle cx="180" cy="20" r="5" fill='#2da44e'/>
            <text x="185" y="15" fill='currentColor' font-size='12'>B(5,6)</text>

            <!-- Vector AB -->
            <line x1="60" y1="140" x2="180" y2="20" stroke='#f85149' stroke-width="2.5" marker-end="url(#arrow5)"/>
            <text x="115" y="70" fill='#f85149' font-size='11' font-weight='bold'>\\(\\vec{AB}\\)</text>

            <!-- Right triangle for distance -->
            <line x1="60" y1="140" x2="180" y2="140" stroke='#8b949e' stroke-width="1" stroke-dasharray="2,2"/>
            <line x1="180" y1="140" x2="180" y2="20" stroke='#8b949e' stroke-width="1" stroke-dasharray="2,2"/>

            <!-- Labels -->
            <text x="120" y="155" fill='currentColor' opacity='0.6' font-size='10'>4 units</text>
            <text x="195" y="80" fill='currentColor' opacity='0.6' font-size='10'>4 units</text>
        </svg>
        """
    },
    {
        "title": "Parametric Equations of Lines and Collinearity",
        "body": """
        <h3>The Parametric Form of a Line</h3>

        <p>Using vectors, we can describe every point on a line with a single equation:</p>

        <div class="concept-box">
            <p><strong>A line through point A with direction \\(\\vec{d}\\):</strong></p>
            <p style="text-align: center; font-size: 1.1em;">\\(\\vec{r}(t) = \\vec{a} + t\\vec{d}\\)</p>
            <p>where t is any real number (parameter) and \\(\\vec{a}\\) is the position vector of A.</p>
        </div>

        <p><strong>Interpretation:</strong> For each value of t, we get a different point on the line.</p>

        <div class="worked-example">
            <p><strong>Example 4:</strong> Write the parametric equation of the line through P(2, 3) in direction \\(\\vec{d} = \\begin{pmatrix} 1 \\\\ -2 \\end{pmatrix}\\)</p>
            <p>\\(\\vec{r}(t) = \\begin{pmatrix} 2 \\\\ 3 \\end{pmatrix} + t\\begin{pmatrix} 1 \\\\ -2 \\end{pmatrix} = \\begin{pmatrix} 2+t \\\\ 3-2t \\end{pmatrix}\\)</p>

            <p style="margin-top: 15px;"><strong>Points on the line:</strong></p>
            <ul>
                <li>t = 0: (2, 3) ← the starting point</li>
                <li>t = 1: (3, 1)</li>
                <li>t = 2: (4, -1)</li>
                <li>t = -1: (1, 5) ← points in the opposite direction</li>
            </ul>
        </div>

        <h3>Collinearity: Are Three Points on the Same Line?</h3>

        <p>Three points A, B, C are collinear (on the same line) if and only if the vectors \\(\\vec{AB}\\) and \\(\\vec{AC}\\) are parallel—one is a scalar multiple of the other.</p>

        <div class="concept-box">
            <p><strong>A, B, C are collinear ⟺ \\(\\vec{AB} = k\\vec{AC}\\) for some scalar k</strong></p>
        </div>

        <div class="worked-example">
            <p><strong>Example 5:</strong> Are A(1, 2), B(3, 5), C(7, 11) collinear?</p>

            <p class="concept-box">
                \\(\\vec{AB} = \\begin{pmatrix} 3-1 \\\\ 5-2 \\end{pmatrix} = \\begin{pmatrix} 2 \\\\ 3 \\end{pmatrix}\\)
            </p>

            <p class="concept-box">
                \\(\\vec{AC} = \\begin{pmatrix} 7-1 \\\\ 11-2 \\end{pmatrix} = \\begin{pmatrix} 6 \\\\ 9 \\end{pmatrix} = 3\\begin{pmatrix} 2 \\\\ 3 \\end{pmatrix} = 3\\vec{AB}\\)
            </p>

            <p>Since \\(\\vec{AC} = 3\\vec{AB}\\), the vectors are parallel. <strong>Yes, A, B, C are collinear!</strong></p>
        </div>

        <div class="success-box">
            <p><strong>Key insight:</strong> C is located twice as far from A as B is, along the same line. This is why the vector from A to C is 3 times the vector from A to B (B is at distance t=1, C is at distance t=3 on the parametric line).</p>
        </div>
        """
    }
]
