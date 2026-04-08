TITLE = "Determinant and Inverse: 2×2 Matrices"

SECTIONS = [
    {
        "title": "What is a Determinant and Why Does It Matter?",
        "body": """
        <div class="concept-box">
            <h3>The Determinant as a Scaling Factor</h3>
            <p>Imagine a transformation in 2D space. A 2×2 matrix can rotate, scale, or shear a region. The determinant tells us: <strong>How much does this transformation scale areas?</strong></p>

            <p><strong>Geometrical interpretation:</strong></p>
            <ul style="margin-left: 20px;">
                <li>If \\(\\det(\\mathbf{A}) = 3\\), the transformation scales all areas by factor 3</li>
                <li>If \\(\\det(\\mathbf{A}) = -1\\), the transformation flips the region (negative sign) and keeps area unchanged</li>
                <li>If \\(\\det(\\mathbf{A}) = 0\\), the transformation collapses the region to a line or point (area becomes zero)</li>
            </ul>

            <p><strong>The critical insight:</strong> A \\(\\det(\\mathbf{A}) = 0\\) means the matrix is "broken"—information is lost. We can't reverse such a transformation, so no inverse exists.</p>

            <svg viewBox="-5 -5 570 160" style="margin: 20px auto; display: block; max-width: 100%; height: auto;">
                <!-- Original square -->
                <g>
                    <text x="50" y="15" font-size='11' fill='currentColor' font-weight='bold' text-anchor='middle'>Original (det = 1)</text>
                    <rect x="20" y="30" width="60" height="60" fill='none' stroke='#4f8ef7' stroke-width="2" rx='4'/>
                    <text x="50" y="110" font-size='10' fill='currentColor' opacity='0.6' text-anchor='middle'>Unit square</text>
                </g>

                <!-- Scaled by 2 -->
                <g>
                    <text x="185" y="15" font-size='11' fill='currentColor' font-weight='bold' text-anchor='middle'>Scaled 2× (det = 4)</text>
                    <rect x="145" y="25" width="80" height="80" fill='none' stroke='#2dd4bf' stroke-width="2" rx='4'/>
                    <text x="185" y="125" font-size='10' fill='currentColor' opacity='0.6' text-anchor='middle'>4× larger area</text>
                </g>

                <!-- Flipped and scaled -->
                <g>
                    <text x="340" y="15" font-size='11' fill='currentColor' font-weight='bold' text-anchor='middle'>Flipped (det = −2)</text>
                    <polygon points="310,35 300,95 370,95 380,35" fill='none' stroke='#f85149' stroke-width="2"/>
                    <text x="340" y="125" font-size='10' fill='currentColor' opacity='0.6' text-anchor='middle'>Flipped and scaled</text>
                </g>

                <!-- Collapsed -->
                <g>
                    <text x="490" y="15" font-size='11' fill='currentColor' font-weight='bold' text-anchor='middle'>Collapsed (det = 0)</text>
                    <line x1="475" y1="35" x2="505" y2="100" stroke='#f85149' stroke-width="3"/>
                    <text x="490" y="125" font-size='10' fill='currentColor' opacity='0.6' text-anchor='middle'>Info lost</text>
                </g>
            </svg>
        </div>
        """
    },
    {
        "title": "Computing the Determinant for 2×2 Matrices",
        "body": """
        <div class="concept-box">
            <h3>The 2×2 Determinant Formula</h3>
            <p>For a 2×2 matrix, the determinant is remarkably simple:</p>

            <p>$$\\mathbf{A} = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix} \\quad \\Longrightarrow \\quad \\det(\\mathbf{A}) = ad - bc$$</p>

            <p><strong>How to remember:</strong></p>
            <ol style="margin-left: 20px;">
                <li>Multiply the diagonal (top-left to bottom-right): \\(a \\times d\\)</li>
                <li>Multiply the anti-diagonal (top-right to bottom-left): \\(b \\times c\\)</li>
                <li>Subtract: \\(ad - bc\\)</li>
            </ol>

            <svg viewBox="-5 -5 320 155" style="margin: 20px auto; display: block; max-width: 100%; height: auto;">
                <!-- Matrix -->
                <rect x="40" y="30" width="80" height="80" fill='none' stroke='#4f8ef7' stroke-width="2" rx='4'/>
                <text x="60" y="62" font-size='16' fill='currentColor' font-weight='bold'>a</text>
                <text x="100" y="62" font-size='16' fill='currentColor' font-weight='bold'>b</text>
                <text x="60" y="100" font-size='16' fill='currentColor' font-weight='bold'>c</text>
                <text x="100" y="100" font-size='16' fill='currentColor' font-weight='bold'>d</text>

                <!-- Main diagonal -->
                <line x1="55" y1="47" x2="105" y2="95" stroke='#2dd4bf' stroke-width="3" opacity='0.7'/>
                <text x="90" y="35" font-size='11' fill='currentColor'>ad</text>

                <!-- Anti-diagonal -->
                <line x1="105" y1="47" x2="55" y2="95" stroke='#f85149' stroke-width="3" opacity='0.7'/>
                <text x="60" y="130" font-size='11' fill='currentColor'>−bc</text>

                <!-- Formula -->
                <text x="210" y="75" font-size='14' fill='currentColor' font-weight='bold' text-anchor='middle'>det = <tspan fill='#2dd4bf'>ad</tspan> − <tspan fill='#f85149'>bc</tspan></text>
            </svg>
        </div>

        <div class="worked-example" style="margin-top: 25px;">
            <h4>Worked Example 1: Simple Determinant</h4>
            <p><strong>Question:</strong> Find \\(\\det(\\mathbf{A})\\) for \\(\\mathbf{A} = \\begin{pmatrix} 3 & 2 \\\\ 1 & 4 \\end{pmatrix}\\)</p>

            <p><strong>Solution:</strong></p>
            <ul style="margin-left: 20px; margin-bottom: 0;">
                <li>\\(a = 3,\\ b = 2,\\ c = 1,\\ d = 4\\)</li>
                <li>\\(\\det(\\mathbf{A}) = (3)(4) - (2)(1)\\)</li>
                <li>\\(\\det(\\mathbf{A}) = 12 - 2 = \\mathbf{10}\\)</li>
            </ul>
        </div>

        <div class="worked-example" style="margin-top: 20px;">
            <h4>Worked Example 2: Negative Determinant</h4>
            <p><strong>Question:</strong> Find \\(\\det(\\mathbf{B})\\) for \\(\\mathbf{B} = \\begin{pmatrix} 1 & 3 \\\\ 2 & 5 \\end{pmatrix}\\)</p>

            <p><strong>Solution:</strong></p>
            <ul style="margin-left: 20px; margin-bottom: 0;">
                <li>\\(\\det(\\mathbf{B}) = (1)(5) - (3)(2)\\)</li>
                <li>\\(\\det(\\mathbf{B}) = 5 - 6 = \\mathbf{-1}\\)</li>
                <li>The negative value means this transformation flips (reflects) the space</li>
            </ul>
        </div>

        <div class="concept-box" style="margin-top: 25px;">
            <h3>Properties of Determinants</h3>
            <ul style="margin-left: 20px;">
                <li><strong>\\(\\det(\\mathbf{A}) \\neq 0\\):</strong> The matrix is <strong>non-singular</strong> (invertible)</li>
                <li><strong>\\(\\det(\\mathbf{A}) = 0\\):</strong> The matrix is <strong>singular</strong> (not invertible)</li>
                <li><strong>\\(\\det(\\mathbf{AB}) = \\det(\\mathbf{A}) \\times \\det(\\mathbf{B})\\):</strong> The determinant of a product is the product of determinants</li>
                <li><strong>\\(\\det(\\mathbf{A}^T) = \\det(\\mathbf{A})\\):</strong> Transposing doesn't change the determinant</li>
                <li><strong>\\(\\det(\\mathbf{I}) = 1\\):</strong> The identity matrix has determinant 1</li>
            </ul>
        </div>
        """
    },
    {
        "title": "The Inverse Matrix",
        "body": """
        <div class="concept-box">
            <h3>What is a Matrix Inverse?</h3>
            <p>For ordinary numbers: if \\(3x = 1\\), then \\(x = \\frac{1}{3}\\) (we multiply by the multiplicative inverse).</p>

            <p>For matrices: if \\(\\mathbf{AX} = \\mathbf{B}\\), we want to solve for \\(\\mathbf{X}\\) by "dividing by \\(\\mathbf{A}\\)". But we can't divide matrices—instead, we multiply by the <strong>inverse matrix</strong> \\(\\mathbf{A}^{-1}\\).</p>

            <p>$$\\mathbf{AX} = \\mathbf{B} \\quad \\Longrightarrow \\quad \\mathbf{X} = \\mathbf{A}^{-1}\\mathbf{B}$$</p>

            <p><strong>Requirement:</strong> The inverse only exists if \\(\\det(\\mathbf{A}) \\neq 0\\). If \\(\\det(\\mathbf{A}) = 0\\), the matrix is singular and has no inverse.</p>

            <h4 class="accent-heading" style="margin-top: 20px;">The 2×2 Inverse Formula</h4>
            <p>For \\(\\mathbf{A} = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}\\) with \\(\\det(\\mathbf{A}) \\neq 0\\):</p>

            <p>$$\\mathbf{A}^{-1} = \\frac{1}{\\det(\\mathbf{A})} \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}$$</p>

            <p><strong>Steps to find the inverse:</strong></p>
            <ol style="margin-left: 20px;">
                <li>Calculate \\(\\det(\\mathbf{A}) = ad - bc\\)</li>
                <li>Check if \\(\\det(\\mathbf{A}) \\neq 0\\) (if det = 0, stop—no inverse exists)</li>
                <li>Swap \\(a\\) and \\(d\\)</li>
                <li>Negate \\(b\\) and \\(c\\)</li>
                <li>Multiply the entire matrix by \\(\\frac{1}{\\det(\\mathbf{A})}\\)</li>
            </ol>

            <svg viewBox="-5 -5 440 185" style="margin: 20px auto; display: block; max-width: 100%; height: auto;">
                <defs>
                    <marker id="arrowhead2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                        <polygon points="0 0, 10 3, 0 6" fill='currentColor' opacity='0.6'/>
                    </marker>
                </defs>

                <!-- Original matrix -->
                <text x="50" y="20" font-size='12' fill='currentColor' font-weight='bold'>A =</text>
                <rect x="80" y="8" width="65" height="60" fill='none' stroke='#4f8ef7' stroke-width="2" rx='4'/>
                <text x="97" y="33" font-size='14' fill='currentColor'>a</text>
                <text x="127" y="33" font-size='14' fill='currentColor'>b</text>
                <text x="97" y="57" font-size='14' fill='currentColor'>c</text>
                <text x="127" y="57" font-size='14' fill='currentColor'>d</text>

                <!-- Arrow with labels -->
                <path d="M 160 38 L 205 38" stroke='currentColor' opacity='0.5' stroke-width="2" marker-end="url(#arrowhead2)"/>
                <text x="183" y="28" font-size='10' fill='currentColor' opacity='0.6' text-anchor='middle'>swap a,d</text>
                <text x="183" y="55" font-size='10' fill='currentColor' opacity='0.6' text-anchor='middle'>negate b,c</text>

                <!-- Adjugate matrix -->
                <rect x="220" y="8" width="75" height="60" fill='none' stroke='#2dd4bf' stroke-width="2" rx='4'/>
                <text x="240" y="33" font-size='14' fill='currentColor'>d</text>
                <text x="275" y="33" font-size='14' fill='currentColor'>−b</text>
                <text x="237" y="57" font-size='14' fill='currentColor'>−c</text>
                <text x="275" y="57" font-size='14' fill='currentColor'>a</text>

                <!-- Final step -->
                <text x="315" y="43" font-size='14' fill='currentColor' text-anchor='start'>× (1/det)</text>

                <!-- Worked example -->
                <text x="15" y="95" font-size='11' fill='currentColor' opacity='0.6' font-style="italic">Example: Find inverse of A = (2  1; 3  2)</text>
                <text x="15" y="117" font-size='12' fill='currentColor'>Step 1: det(A) = (2)(2) − (1)(3) = 4 − 3 = 1</text>
                <text x="15" y="139" font-size='12' fill='currentColor'>Step 2: Swap and negate: (2  −1; −3  2)</text>
                <text x="15" y="161" font-size='12' fill='currentColor' font-weight='bold'>Step 3: A⁻¹ = (1/1) × (2  −1; −3  2) = (2  −1; −3  2)</text>
            </svg>
        </div>

        <div class="worked-example" style="margin-top: 25px;">
            <h4>Worked Example: Finding an Inverse</h4>
            <p><strong>Question:</strong> Find \\(\\mathbf{A}^{-1}\\) for \\(\\mathbf{A} = \\begin{pmatrix} 3 & 2 \\\\ 1 & 4 \\end{pmatrix}\\)</p>

            <p><strong>Solution:</strong></p>
            <ul style="margin-left: 20px;">
                <li>Step 1: \\(\\det(\\mathbf{A}) = (3)(4) - (2)(1) = 12 - 2 = 10\\) ✓ (≠ 0, so inverse exists)</li>
                <li>Step 2: Swap \\(a\\) and \\(d\\): (4, 3)</li>
                <li>Step 3: Negate \\(b\\) and \\(c\\): matrix becomes \\(\\begin{pmatrix} 4 & -2 \\\\ -1 & 3 \\end{pmatrix}\\)</li>
                <li>Step 4: Multiply by \\(\\frac{1}{10}\\):</li>
            </ul>
            <p>$$\\mathbf{A}^{-1} = \\frac{1}{10} \\begin{pmatrix} 4 & -2 \\\\ -1 & 3 \\end{pmatrix} = \\begin{pmatrix} 0.4 & -0.2 \\\\ -0.1 & 0.3 \\end{pmatrix}$$</p>
        </div>

        <div class="concept-box" style="margin-top: 25px;">
            <h3>Verifying an Inverse: \\(\\mathbf{A}\\mathbf{A}^{-1} = \\mathbf{I}\\)</h3>
            <p>To check that you've computed the inverse correctly, multiply \\(\\mathbf{A}\\) by \\(\\mathbf{A}^{-1}\\). You should get the identity matrix \\(\\mathbf{I}\\).</p>

            <p>$$\\mathbf{A} \\times \\mathbf{A}^{-1} = \\mathbf{I}$$</p>

            <p><strong>Example from above:</strong></p>
            <p>$$\\begin{pmatrix} 3 & 2 \\\\ 1 & 4 \\end{pmatrix} \\times \\begin{pmatrix} 0.4 & -0.2 \\\\ -0.1 & 0.3 \\end{pmatrix} = \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix} \\checkmark$$</p>
        </div>
        """
    }
]
