TITLE = "Matrix Operations: Addition, Subtraction, and Scaling"

SECTIONS = [
    {
        "title": "Why Do Matrices Have Their Own Arithmetic?",
        "body": """
        <div class="concept-box">
            <h3>The Foundation: Element-Wise Operations</h3>
            <p>When we add two ordinary numbers like 3 + 5 = 8, the operation is straightforward. But what happens when we want to add two tables of data?</p>

            <p><strong>Intuitive Idea:</strong> If you have test scores from two semesters and want a combined total, you naturally add corresponding entries:</p>

            <table style="border-collapse: collapse; margin: 20px auto; width: 90%; max-width: 600px">
                <tr >
                    <th style="padding: 8px; text-align: left;">Semester</th>
                    <th style="padding: 8px; text-align: center;">Test 1</th>
                    <th style="padding: 8px; text-align: center;">Test 2</th>
                    <th style="padding: 8px; text-align: center;">Test 3</th>
                </tr>
                <tr >
                    <td style="padding: 8px; font-weight: bold;">Fall</td>
                    <td style="padding: 8px; text-align: center;">85</td>
                    <td style="padding: 8px; text-align: center;">92</td>
                    <td style="padding: 8px; text-align: center;">88</td>
                </tr>
                <tr >
                    <td style="padding: 8px; font-weight: bold;">Spring</td>
                    <td style="padding: 8px; text-align: center;">90</td>
                    <td style="padding: 8px; text-align: center;">88</td>
                    <td style="padding: 8px; text-align: center;">91</td>
                </tr>
                <tr >
                    <td style="padding: 8px; font-weight: bold;">Total</td>
                    <td style="padding: 8px; text-align: center"><strong>175</strong></td>
                    <td style="padding: 8px; text-align: center"><strong>180</strong></td>
                    <td style="padding: 8px; text-align: center"><strong>179</strong></td>
                </tr>
            </table>

            <p>This is exactly what matrix addition does: add corresponding positions.</p>
        </div>
        """
    },
    {
        "title": "Matrix Addition and Subtraction",
        "body": """
        <div class="concept-box">
            <h3>Adding Matrices: The Rule</h3>
            <p>To add two matrices:</p>
            <ol style="margin-left: 20px;">
                <li><strong>Check compatibility:</strong> Both matrices must have the same dimensions</li>
                <li><strong>Add element-by-element:</strong> Add the elements in the same positions</li>
            </ol>

            <p style="text-align: center; margin: 20px 0; font-family: monospace; font-size: 1.05em; padding: 15px">
            <strong>A + B = (</strong>a₁₁+b₁₁  a₁₂+b₁₂<br/>
            a₂₁+b₂₁  a₂₂+b₂₂<strong>)</strong>
            </p>

            <p><strong>Why must dimensions match?</strong> You can't add a 2×3 matrix to a 3×2 matrix because there are elements in one that have no "partner" in the other.</p>

            <svg viewBox="0 0 500 150" style="margin: 20px auto; display: block; max-width: 100%; height: auto;">
                <!-- Matrix A -->
                <text x="30" y="20" font-size='12' fill='currentColor' font-weight='bold'>A =</text>
                <rect x="80" y="10" width="60" height="60" fill='none' stroke='#4f8ef7' stroke-width="2"/>
                <text x="95" y="35" font-size='14' fill='#4f8ef7'>1</text>
                <text x="125" y="35" font-size='14' fill='#4f8ef7'>2</text>
                <text x="95" y="55" font-size='14' fill='#4f8ef7'>3</text>
                <text x="125" y="55" font-size='14' fill='#4f8ef7'>4</text>

                <!-- Plus sign -->
                <text x="160" y="45" font-size='20' fill='currentColor' font-weight='bold' text-anchor='middle'>+</text>

                <!-- Matrix B -->
                <text x="190" y="20" font-size='12' fill='currentColor' font-weight='bold'>B =</text>
                <rect x="240" y="10" width="60" height="60" fill='none' stroke='#4f8ef7' stroke-width="2"/>
                <text x="255" y="35" font-size='14' fill='#4f8ef7'>5</text>
                <text x="285" y="35" font-size='14' fill='#4f8ef7'>6</text>
                <text x="255" y="55" font-size='14' fill='#4f8ef7'>7</text>
                <text x="285" y="55" font-size='14' fill='#4f8ef7'>8</text>

                <!-- Equals sign -->
                <text x="320" y="45" font-size='20' fill='currentColor' font-weight='bold' text-anchor='middle'>=</text>

                <!-- Matrix Result -->
                <rect x="350" y="10" width="60" height="60" fill='none' stroke='#2dd4bf' stroke-width="2"/>
                <text x="365" y="35" font-size='14' fill='#2dd4bf'>6</text>
                <text x="395" y="35" font-size='14' fill='#2dd4bf'>8</text>
                <text x="365" y="55" font-size='14' fill='#2dd4bf'>10</text>
                <text x="395" y="55" font-size='14' fill='#2dd4bf'>12</text>

                <!-- Annotations -->
                <path d="M 95 65 L 95 85" stroke='#8b949e' stroke-width="1" stroke-dasharray="5,5"/>
                <path d="M 365 65 L 365 85" stroke='#8b949e' stroke-width="1" stroke-dasharray="5,5"/>
                <text x="95" y="105" font-size='11' fill='currentColor' opacity='0.6' text-anchor='middle'>1+5=6</text>
            </svg>
        </div>

        <div class="worked-example" style="margin-top: 25px;">
            <h4>Worked Example: Adding 2×3 Matrices</h4>
            <p><strong>Question:</strong> Find A + B where:</p>
            <p style="text-align: center; margin: 15px 0; font-family: monospace; font-size: 1em; padding: 10px">
            <strong>A = (</strong>1  2  3<br/>
            4  5  6<strong>)&nbsp;&nbsp;&nbsp;B = (</strong>10  20  30<br/>
            40  50  60<strong>)</strong>
            </p>
            <p><strong>Solution:</strong></p>
            <p style="text-align: center; margin: 15px 0; font-family: monospace; font-size: 1em; padding: 10px">
            <strong>A + B = (</strong>1+10  2+20  3+30<br/>
            4+40  5+50  6+60<strong>) = (</strong>11  22  33<br/>
            44  55  66<strong>)</strong>
            </p>
        </div>

        <div class="concept-box" style="margin-top: 25px;">
            <h3>Subtraction</h3>
            <p>Subtraction works exactly the same way as addition—just subtract corresponding elements:</p>
            <p style="text-align: center; margin: 15px 0; font-family: monospace; font-size: 1em; padding: 10px">
            <strong>A − B = (</strong>a₁₁−b₁₁  a₁₂−b₁₂<br/>
            a₂₁−b₂₁  a₂₂−b₂₂<strong>)</strong>
            </p>
        </div>
        """
    },
    {
        "title": "Scalar Multiplication",
        "body": """
        <div class="concept-box">
            <h3>Multiplying a Matrix by a Number</h3>
            <p>A <strong>scalar</strong> is just an ordinary number (as opposed to a matrix). Scalar multiplication means multiplying every element in the matrix by that number.</p>

            <p><strong>Real-world example:</strong> If a store sells 3 items at certain prices, and they want to apply a 50% discount, they multiply each price by 0.5:</p>
            <p style="text-align: center; margin: 15px 0; font-family: monospace; font-size: 1em; padding: 10px">
            Prices: <strong>(</strong>20  30  40<strong>)</strong><br/>
            After 50% discount: 0.5 × <strong>(</strong>20  30  40<strong>) = (</strong>10  15  20<strong>)</strong>
            </p>

            <p style="text-align: center; margin: 20px 0; font-family: monospace; font-size: 1.05em; padding: 15px">
            <strong>k·A = (</strong>ka₁₁  ka₁₂<br/>
            ka₂₁  ka₂₂<strong>)</strong>
            </p>

            <p><strong>Key insight:</strong> A single number multiplied by every element means you're scaling the entire matrix. This is why it's called "scalar" multiplication.</p>

            <svg viewBox="0 0 430 120" style="margin: 20px auto; display: block; max-width: 100%; height: auto;">
                <!-- Scalar -->
                <text x="30" y="35" font-size='16' fill='#4f8ef7' font-weight='bold'>3</text>

                <!-- Multiplication sign -->
                <text x="55" y="35" font-size='16' fill='currentColor' text-anchor='middle'>×</text>

                <!-- Matrix -->
                <rect x="75" y="15" width="60" height="60" fill='none' stroke='#4f8ef7' stroke-width="2"/>
                <text x="90" y="40" font-size='14' fill='#4f8ef7'>1</text>
                <text x="120" y="40" font-size='14' fill='#4f8ef7'>2</text>
                <text x="90" y="60" font-size='14' fill='#4f8ef7'>3</text>
                <text x="120" y="60" font-size='14' fill='#4f8ef7'>4</text>

                <!-- Equals -->
                <text x="155" y="35" font-size='16' fill='currentColor' text-anchor='middle'>=</text>

                <!-- Result -->
                <rect x="175" y="15" width="60" height="60" fill='none' stroke='#2dd4bf' stroke-width="2"/>
                <text x="190" y="40" font-size='14' fill='#2dd4bf'>3</text>
                <text x="220" y="40" font-size='14' fill='#2dd4bf'>6</text>
                <text x="190" y="60" font-size='14' fill='#2dd4bf'>9</text>
                <text x="220" y="60" font-size='14' fill='#2dd4bf'>12</text>

                <!-- Annotation -->
                <text x="320" y="45" font-size='11' fill='currentColor' opacity='0.6'>(each element × 3)</text>
            </svg>
        </div>

        <div class="worked-example" style="margin-top: 25px;">
            <h4>Worked Example: Scalar Multiplication</h4>
            <p><strong>Question:</strong> Find 2A where <strong>A = (</strong>5  -3<br/>1   4<strong>)</strong></p>
            <p><strong>Solution:</strong> Multiply each element by 2:</p>
            <p style="text-align: center; margin: 15px 0; font-family: monospace; font-size: 1em; padding: 10px">
            2A = 2 × <strong>(</strong>5  -3<br/>
            1   4<strong>) = (</strong>10  -6<br/>
            2    8<strong>)</strong>
            </p>
        </div>

        <div class="concept-box" style="margin-top: 25px;">
            <h3>Properties of Matrix Operations</h3>
            <ul style="margin-left: 20px;">
                <li><strong>Commutativity of addition:</strong> A + B = B + A (order doesn't matter)</li>
                <li><strong>Associativity:</strong> (A + B) + C = A + (B + C)</li>
                <li><strong>Distributive law:</strong> k(A + B) = kA + kB (scalar distributes over addition)</li>
                <li><strong>Identity:</strong> A + 0 = A (adding the zero matrix doesn't change anything)</li>
                <li><strong>Scalar associativity:</strong> k(mA) = (km)A (order of scalar multiplication doesn't matter)</li>
            </ul>
        </div>
        """
    }
]
