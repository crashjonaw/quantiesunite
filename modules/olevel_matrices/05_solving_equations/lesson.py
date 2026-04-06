TITLE = "Solving Simultaneous Equations Using Matrices"

SECTIONS = [
    {
        "title": "From Equations to Matrices",
        "body": """
        <div class="concept-box">
            <h3>Why Use Matrices to Solve Equations?</h3>
            <p>Consider this system of 2 equations with 2 unknowns:</p>

            <p style="text-align: center; margin: 15px 0; font-size: 1.05em">
            2x + 3y = 7<br/>
            x − y = 1
            </p>

            <p>You've solved systems like this by substitution or elimination. But what if you have 10 equations with 10 unknowns? Matrices give us a systematic, computer-friendly way to solve any such system.</p>

            <h4 class="accent-heading" style="margin-top: 20px;">Converting to Matrix Form</h4>
            <p>Any system of linear equations can be written as:</p>

            <p style="text-align: center; margin: 20px 0; font-size: 1.15em; padding: 15px; font-weight: bold">
            AX = B
            </p>

            <p>Where:</p>
            <ul style="margin-left: 20px;">
                <li><strong>A</strong> = coefficient matrix (coefficients of the variables)</li>
                <li><strong>X</strong> = variable matrix (the unknowns we're solving for)</li>
                <li><strong>B</strong> = constant matrix (the right-hand side values)</li>
            </ul>

            <div class="worked-example" style="margin-top: 20px;">
                <h5 style="margin-top: 0;">Converting Our Example</h5>
                <p><strong>System:</strong></p>
                <p style="margin: 10px 0; font-family: monospace">
                2x + 3y = 7<br/>
                1x − 1y = 1
                </p>

                <p><strong>Matrix form AX = B:</strong></p>
                <p style="text-align: center; margin: 15px 0; font-family: monospace; font-size: 1em; padding: 10px">
                <strong>(</strong>2  3<br/>
                1  −1<strong>)(</strong>x<br/>
                y<strong>) = (</strong>7<br/>
                1<strong>)</strong>
                </p>

                <p style="margin-left: 20px;">
                <strong>A</strong> = <strong>(</strong>2  3<br/>1  −1<strong>)&nbsp;&nbsp;&nbsp;X</strong> = <strong>(</strong>x<br/>y<strong>)&nbsp;&nbsp;&nbsp;B</strong> = <strong>(</strong>7<br/>1<strong>)</strong>
                </p>
            </div>

            <svg viewBox="-5 -5 430 125" style="margin: 20px auto; display: block; max-width: 100%; height: auto;">
                <defs>
                    <marker id="arrowhead3" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                        <polygon points="0 0, 10 3, 0 6" fill='currentColor' opacity='0.6'/>
                    </marker>
                </defs>

                <!-- Equation form -->
                <text x="50" y="15" font-size='12' fill='currentColor' font-weight='bold'>Equation Form</text>
                <text x="50" y="38" font-size='12' fill='currentColor'>2x + 3y = 7</text>
                <text x="50" y="58" font-size='12' fill='currentColor'>1x − 1y = 1</text>

                <!-- Arrow -->
                <path d="M 155 42 L 195 42" stroke='currentColor' opacity='0.5' stroke-width="2" marker-end="url(#arrowhead3)"/>
                <text x="175" y="30" font-size='10' fill='currentColor' opacity='0.6' text-anchor='middle'>rewrite as</text>

                <!-- Matrix form label -->
                <text x="215" y="15" font-size='12' fill='currentColor' font-weight='bold'>Matrix Form AX = B</text>

                <!-- A matrix -->
                <rect x="215" y="28" width="60" height="55" fill='none' stroke='#4f8ef7' stroke-width="2" rx='4'/>
                <text x="230" y="50" font-size='12' fill='currentColor'>2</text>
                <text x="258" y="50" font-size='12' fill='currentColor'>3</text>
                <text x="230" y="72" font-size='12' fill='currentColor'>1</text>
                <text x="253" y="72" font-size='12' fill='currentColor'>−1</text>
                <text x="245" y="100" font-size='10' fill='currentColor' opacity='0.6' text-anchor='middle'>A</text>

                <!-- X matrix -->
                <rect x="285" y="28" width="35" height="55" fill='none' stroke='#2dd4bf' stroke-width="2" rx='4'/>
                <text x="303" y="50" font-size='12' fill='currentColor' text-anchor='middle'>x</text>
                <text x="303" y="72" font-size='12' fill='currentColor' text-anchor='middle'>y</text>
                <text x="303" y="100" font-size='10' fill='currentColor' opacity='0.6' text-anchor='middle'>X</text>

                <!-- = -->
                <text x="332" y="60" font-size='14' fill='currentColor'>=</text>

                <!-- B matrix -->
                <rect x="350" y="28" width="35" height="55" fill='none' stroke='#f85149' stroke-width="2" rx='4'/>
                <text x="368" y="50" font-size='12' fill='currentColor' text-anchor='middle'>7</text>
                <text x="368" y="72" font-size='12' fill='currentColor' text-anchor='middle'>1</text>
                <text x="368" y="100" font-size='10' fill='currentColor' opacity='0.6' text-anchor='middle'>B</text>
            </svg>
        </div>
        """
    },
    {
        "title": "Solving Using Matrix Inverse",
        "body": """
        <div class="concept-box">
            <h3>The Matrix Solution Method</h3>
            <p>Once we have AX = B, solving for X is elegant:</p>

            <p style="text-align: center; margin: 20px 0; font-size: 1.3em; padding: 15px; font-weight: bold">
            AX = B<br/>
            A<sup>−1</sup>AX = A<sup>−1</sup>B<br/>
            IX = A<sup>−1</sup>B<br/>
            X = A<sup>−1</sup>B
            </p>

            <p><strong>In words:</strong> Multiply both sides by A<sup>−1</sup> from the left. This "cancels out" A on the left, leaving us with the solution X.</p>

            <h4 class="accent-heading" style="margin-top: 20px;">Steps to Solve</h4>
            <ol style="margin-left: 20px;">
                <li>Write the system in matrix form AX = B</li>
                <li>Calculate det(A). If det(A) = 0, stop—no unique solution exists</li>
                <li>Find A<sup>−1</sup> using the 2×2 inverse formula</li>
                <li>Compute X = A<sup>−1</sup>B (multiply A<sup>−1</sup> by B)</li>
                <li>Read off the values of the variables from X</li>
            </ol>
        </div>

        <div class="worked-example" style="margin-top: 25px;">
            <h4>Worked Example: Solving a 2×2 System</h4>
            <p><strong>System:</strong></p>
            <p style="margin: 10px 0; font-family: monospace">
            2x + 3y = 7<br/>
            x − y = 1
            </p>

            <p><strong>Step 1: Matrix form</strong></p>
            <p style="text-align: center; margin: 10px 0; font-family: monospace; font-size: 0.9em; padding: 8px">
            <strong>(</strong>2  3<br/>1  −1<strong>)(</strong>x<br/>y<strong>) = (</strong>7<br/>1<strong>)</strong>
            </p>

            <p><strong>Step 2: Find det(A)</strong></p>
            <p style="margin: 10px 0; font-family: monospace">
            det(A) = (2)(−1) − (3)(1) = −2 − 3 = −5 ✓
            </p>

            <p><strong>Step 3: Find A<sup>−1</sup></strong></p>
            <p style="margin: 10px 0; font-family: monospace">
            A<sup>−1</sup> = (1/(−5)) × <strong>(</strong>−1  −3<br/>−1  2<strong>)</strong> = <strong>(</strong>1/5  3/5<br/>1/5  −2/5<strong>)</strong>
            </p>

            <p><strong>Step 4: Compute X = A<sup>−1</sup>B</strong></p>
            <p style="margin: 10px 0; font-family: monospace; font-size: 0.9em; padding: 8px">
            <strong>(</strong>x<br/>y<strong>) = (</strong>1/5  3/5<br/>1/5  −2/5<strong>)(</strong>7<br/>1<strong>)</strong>
            </p>

            <p style="margin: 10px 0; font-family: monospace">
            x = (1/5)(7) + (3/5)(1) = 7/5 + 3/5 = 10/5 = <strong style="color: #2dd4bf;">2</strong><br/>
            y = (1/5)(7) + (−2/5)(1) = 7/5 − 2/5 = 5/5 = <strong style="color: #2dd4bf;">1</strong>
            </p>

            <p style="margin-top: 15px; color: #2dd4bf;"><strong>Solution: x = 2, y = 1</strong></p>

            <p style="margin-top: 10px; font-style: italic">Check: 2(2) + 3(1) = 7 ✓ and 2 − 1 = 1 ✓</p>
        </div>
        """
    },
    {
        "title": "When No Unique Solution Exists",
        "body": """
        <div class="concept-box">
            <h3>The Role of the Determinant</h3>
            <p>The determinant tells us whether a unique solution exists:</p>

            <ul style="margin-left: 20px;">
                <li><strong>det(A) ≠ 0:</strong> Unique solution exists. Use the matrix method.</li>
                <li><strong>det(A) = 0:</strong> Either no solution or infinitely many solutions. The matrix method fails because A<sup>−1</sup> doesn't exist.</li>
            </ul>

            <h4 class="accent-heading" style="margin-top: 20px;">Geometric Interpretation</h4>
            <p>In 2D, each equation represents a line. The solution is where the lines intersect:</p>

            <svg viewBox="-5 -5 680 175" style="margin: 20px auto; display: block; max-width: 100%; height: auto;">
                <!-- One solution -->
                <g>
                    <text x="100" y="15" font-size='11' fill='currentColor' font-weight='bold' text-anchor='middle'>One Solution (det ≠ 0)</text>
                    <rect x="20" y="28" width="160" height="110" fill='none' stroke='currentColor' opacity='0.3' stroke-width="1" rx='4'/>
                    <line x1="30" y1="130" x2="170" y2="38" stroke='#4f8ef7' stroke-width="2"/>
                    <line x1="30" y1="45" x2="170" y2="125" stroke='#2dd4bf' stroke-width="2"/>
                    <circle cx="100" cy="85" r="4" fill='#f85149'/>
                    <text x="100" y="155" font-size='10' fill='currentColor' opacity='0.6' text-anchor='middle'>Lines intersect</text>
                </g>

                <!-- No solution -->
                <g>
                    <text x="310" y="15" font-size='11' fill='currentColor' font-weight='bold' text-anchor='middle'>No Solution (det = 0)</text>
                    <rect x="230" y="28" width="160" height="110" fill='none' stroke='currentColor' opacity='0.3' stroke-width="1" rx='4'/>
                    <line x1="240" y1="75" x2="380" y2="75" stroke='#4f8ef7' stroke-width="2"/>
                    <line x1="240" y1="105" x2="380" y2="105" stroke='#2dd4bf' stroke-width="2"/>
                    <text x="310" y="155" font-size='10' fill='currentColor' opacity='0.6' text-anchor='middle'>Parallel lines</text>
                </g>

                <!-- Infinite solutions -->
                <g>
                    <text x="520" y="15" font-size='11' fill='currentColor' font-weight='bold' text-anchor='middle'>Infinite Solutions (det = 0)</text>
                    <rect x="440" y="28" width="160" height="110" fill='none' stroke='currentColor' opacity='0.3' stroke-width="1" rx='4'/>
                    <line x1="450" y1="130" x2="590" y2="38" stroke='#4f8ef7' stroke-width="2"/>
                    <line x1="450" y1="130" x2="590" y2="38" stroke='#2dd4bf' stroke-width="2" stroke-dasharray="5,5"/>
                    <text x="520" y="155" font-size='10' fill='currentColor' opacity='0.6' text-anchor='middle'>Same line</text>
                </g>
            </svg>

            <p style="margin-top: 20px;">When det(A) = 0, the rows of A are proportional—they represent the same or parallel lines, so intersection analysis requires deeper inspection.</p>
        </div>

        <div class="concept-box" style="margin-top: 25px;">
            <h3>Example: When det(A) = 0</h3>
            <p><strong>System:</strong></p>
            <p style="margin: 10px 0; font-family: monospace">
            2x + 4y = 6<br/>
            x + 2y = 3
            </p>

            <p><strong>Matrix form:</strong></p>
            <p style="text-align: center; margin: 10px 0; font-family: monospace; font-size: 0.9em; padding: 8px">
            <strong>A = (</strong>2  4<br/>1  2<strong>)</strong>
            </p>

            <p><strong>Determinant:</strong></p>
            <p style="margin: 10px 0; font-family: monospace">
            det(A) = (2)(2) − (4)(1) = 4 − 4 = 0
            </p>

            <p style="color: #f85149; margin-top: 10px;"><strong>✗ Matrix method fails!</strong> We need to analyze the equations differently:</p>
            <ul style="margin-left: 20px">
                <li>The second equation is exactly half the first: x + 2y = 3 is 1/2 × (2x + 4y = 6)</li>
                <li>They represent the same line</li>
                <li><strong>Infinitely many solutions</strong> on the line 2x + 4y = 6</li>
            </ul>
        </div>

        <div class="warning-box" style="margin-top: 25px;">
            <h4 style="color: #f85149; margin-top: 0;">Remember</h4>
            <ul style="margin-left: 20px; margin-bottom: 0;">
                <li>Always check det(A) before using the matrix method</li>
                <li>If det(A) = 0, use traditional methods (substitution, elimination) to analyze the system</li>
                <li>The matrix method is powerful for det(A) ≠ 0 cases</li>
            </ul>
        </div>
        """
    }
]
