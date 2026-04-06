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
                <li>If det(A) = 3, the transformation scales all areas by factor 3</li>
                <li>If det(A) = -1, the transformation flips the region (negative sign) and keeps area unchanged</li>
                <li>If det(A) = 0, the transformation collapses the region to a line or point (area becomes zero)</li>
            </ul>

            <p><strong>The critical insight:</strong> A det(A) = 0 means the matrix is "broken"—information is lost. We can't reverse such a transformation, so no inverse exists.</p>

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

            <p style="text-align: center; margin: 20px 0; font-size: 1.3em; padding: 15px">
            <strong>A = (</strong>a  b<br/>
            c  d<strong>)&nbsp;&nbsp;⟹&nbsp;&nbsp;det(A) = ad − bc</strong>
            </p>

            <p><strong>How to remember:</strong></p>
            <ol style="margin-left: 20px;">
                <li>Multiply the diagonal (top-left to bottom-right): <strong>a × d</strong></li>
                <li>Multiply the anti-diagonal (top-right to bottom-left): <strong>b × c</strong></li>
                <li>Subtract: <strong>ad − bc</strong></li>
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
            <p><strong>Question:</strong> Find det(A) for <strong>A = (</strong>3  2<br/>1  4<strong>)</strong></p>

            <p><strong>Solution:</strong></p>
            <ul style="margin-left: 20px; margin-bottom: 0;">
                <li>a = 3, b = 2, c = 1, d = 4</li>
                <li>det(A) = (3)(4) − (2)(1)</li>
                <li>det(A) = 12 − 2 = <strong style="color: #2dd4bf;">10</strong></li>
            </ul>
        </div>

        <div class="worked-example" style="margin-top: 20px;">
            <h4>Worked Example 2: Negative Determinant</h4>
            <p><strong>Question:</strong> Find det(B) for <strong>B = (</strong>1  3<br/>2  5<strong>)</strong></p>

            <p><strong>Solution:</strong></p>
            <ul style="margin-left: 20px; margin-bottom: 0;">
                <li>det(B) = (1)(5) − (3)(2)</li>
                <li>det(B) = 5 − 6 = <strong style="color: #f85149;">−1</strong></li>
                <li>The negative value means this transformation flips (reflects) the space</li>
            </ul>
        </div>

        <div class="concept-box" style="margin-top: 25px;">
            <h3>Properties of Determinants</h3>
            <ul style="margin-left: 20px;">
                <li><strong>det(A) ≠ 0:</strong> The matrix is <strong>non-singular</strong> (invertible)</li>
                <li><strong>det(A) = 0:</strong> The matrix is <strong>singular</strong> (not invertible)</li>
                <li><strong>det(AB) = det(A) × det(B):</strong> The determinant of a product is the product of determinants</li>
                <li><strong>det(A<sup>T</sup>) = det(A):</strong> Transposing doesn't change the determinant</li>
                <li><strong>det(I) = 1:</strong> The identity matrix has determinant 1</li>
            </ul>
        </div>
        """
    },
    {
        "title": "The Inverse Matrix",
        "body": """
        <div class="concept-box">
            <h3>What is a Matrix Inverse?</h3>
            <p>For ordinary numbers: if 3x = 1, then x = 1/3 (we multiply by the multiplicative inverse).</p>

            <p>For matrices: if AX = B, we want to solve for X by "dividing by A". But we can't divide matrices—instead, we multiply by the <strong>inverse matrix</strong> A<sup>−1</sup>.</p>

            <p style="text-align: center; margin: 20px 0; font-size: 1.1em; padding: 15px">
            <strong>AX = B&nbsp;&nbsp;⟹&nbsp;&nbsp;X = A</strong><sup>−1</sup><strong>B</strong>
            </p>

            <p><strong>Requirement:</strong> The inverse only exists if det(A) ≠ 0. If det(A) = 0, the matrix is singular and has no inverse.</p>

            <h4 class="accent-heading" style="margin-top: 20px;">The 2×2 Inverse Formula</h4>
            <p>For <strong>A = (</strong>a  b<br/>c  d<strong>)</strong> with det(A) ≠ 0:</p>

            <p style="text-align: center; margin: 20px 0; font-family: monospace; font-size: 1.05em; padding: 15px">
            <strong>A</strong><sup>−1</sup><strong> = (1/det(A)) × (</strong>d  −b<br/>
            −c   a<strong>)</strong>
            </p>

            <p><strong>Steps to find the inverse:</strong></p>
            <ol style="margin-left: 20px;">
                <li>Calculate det(A) = ad − bc</li>
                <li>Check if det(A) ≠ 0 (if det = 0, stop—no inverse exists)</li>
                <li>Swap a and d</li>
                <li>Negate b and c</li>
                <li>Multiply the entire matrix by 1/det(A)</li>
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
            <p><strong>Question:</strong> Find A<sup>−1</sup> for <strong>A = (</strong>3  2<br/>1  4<strong>)</strong></p>

            <p><strong>Solution:</strong></p>
            <ul style="margin-left: 20px;">
                <li>Step 1: det(A) = (3)(4) − (2)(1) = 12 − 2 = <strong>10</strong> ✓ (≠ 0, so inverse exists)</li>
                <li>Step 2: Swap a and d: (4, 3)</li>
                <li>Step 3: Negate b and c: matrix becomes <strong>(</strong>4  −2<br/>−1  3<strong>)</strong></li>
                <li>Step 4: Multiply by 1/10:</li>
            </ul>
            <p style="text-align: center; margin: 15px 0; font-family: monospace; font-size: 0.95em; color: #2dd4bf; padding: 10px">
            <strong>A</strong><sup>−1</sup><strong> = (1/10) × (</strong>4  −2<br/>
            −1  3<strong>) = (</strong>0.4  −0.2<br/>
            −0.1  0.3<strong>)</strong>
            </p>
        </div>

        <div class="concept-box" style="margin-top: 25px;">
            <h3>Verifying an Inverse: AA<sup>−1</sup> = I</h3>
            <p>To check that you've computed the inverse correctly, multiply A by A<sup>−1</sup>. You should get the identity matrix I.</p>

            <p style="text-align: center; margin: 15px 0; font-family: monospace; font-size: 1em; padding: 10px">
            <strong>A × A</strong><sup>−1</sup><strong> = I</strong>
            </p>

            <p><strong>Example from above:</strong></p>
            <p style="text-align: center; margin: 10px 0; font-family: monospace; font-size: 0.85em">
            <strong>(</strong>3  2<br/>
            1  4<strong>)</strong> × <strong>(</strong>0.4  −0.2<br/>
            −0.1  0.3<strong>) = (</strong>1  0<br/>
            0  1<strong>)</strong> ✓
            </p>
        </div>
        """
    }
]
