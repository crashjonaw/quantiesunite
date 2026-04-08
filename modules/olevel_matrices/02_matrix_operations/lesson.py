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

            <p>$$\\mathbf{A} + \\mathbf{B} = \\begin{pmatrix} a_{11}+b_{11} & a_{12}+b_{12} \\\\ a_{21}+b_{21} & a_{22}+b_{22} \\end{pmatrix}$$</p>

            <p><strong>Why must dimensions match?</strong> You can't add a 2×3 matrix to a 3×2 matrix because there are elements in one that have no "partner" in the other.</p>

            <svg viewBox="-5 -5 500 130" style="margin: 20px auto; display: block; max-width: 100%; height: auto;">
                <!-- Matrix A label -->
                <text x="15" y="45" font-size='13' fill='currentColor' font-weight='bold'>A =</text>

                <!-- Matrix A -->
                <rect x="50" y="10" width="70" height="65" fill='none' stroke='#4f8ef7' stroke-width="2" rx='4'/>
                <text x="70" y="37" font-size='14' fill='currentColor'>1</text>
                <text x="100" y="37" font-size='14' fill='currentColor'>2</text>
                <text x="70" y="62" font-size='14' fill='currentColor'>3</text>
                <text x="100" y="62" font-size='14' fill='currentColor'>4</text>

                <!-- Plus sign -->
                <text x="145" y="48" font-size='20' fill='currentColor' font-weight='bold' text-anchor='middle'>+</text>

                <!-- Matrix B label -->
                <text x="170" y="45" font-size='13' fill='currentColor' font-weight='bold'>B =</text>

                <!-- Matrix B -->
                <rect x="205" y="10" width="70" height="65" fill='none' stroke='#4f8ef7' stroke-width="2" rx='4'/>
                <text x="225" y="37" font-size='14' fill='currentColor'>5</text>
                <text x="255" y="37" font-size='14' fill='currentColor'>6</text>
                <text x="225" y="62" font-size='14' fill='currentColor'>7</text>
                <text x="255" y="62" font-size='14' fill='currentColor'>8</text>

                <!-- Equals sign -->
                <text x="300" y="48" font-size='20' fill='currentColor' font-weight='bold' text-anchor='middle'>=</text>

                <!-- Result Matrix -->
                <rect x="325" y="10" width="80" height="65" fill='none' stroke='#2dd4bf' stroke-width="2" rx='4'/>
                <text x="345" y="37" font-size='14' fill='currentColor'>6</text>
                <text x="385" y="37" font-size='14' fill='currentColor'>8</text>
                <text x="342" y="62" font-size='14' fill='currentColor'>10</text>
                <text x="382" y="62" font-size='14' fill='currentColor'>12</text>

                <!-- Annotation -->
                <path d="M 70 80 L 70 95" stroke='currentColor' opacity='0.5' stroke-width="1" stroke-dasharray="5,5"/>
                <path d="M 345 80 L 345 95" stroke='currentColor' opacity='0.5' stroke-width="1" stroke-dasharray="5,5"/>
                <text x="210" y="110" font-size='11' fill='currentColor' opacity='0.6' text-anchor='middle'>Each entry: 1+5=6, 2+6=8, ...</text>
            </svg>
        </div>

        <div class="worked-example" style="margin-top: 25px;">
            <h4>Worked Example: Adding 2×3 Matrices</h4>
            <p><strong>Question:</strong> Find \\(\\mathbf{A} + \\mathbf{B}\\) where:</p>
            <p>$$\\mathbf{A} = \\begin{pmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\end{pmatrix}, \\quad \\mathbf{B} = \\begin{pmatrix} 10 & 20 & 30 \\\\ 40 & 50 & 60 \\end{pmatrix}$$</p>
            <p><strong>Solution:</strong></p>
            <p>$$\\mathbf{A} + \\mathbf{B} = \\begin{pmatrix} 1+10 & 2+20 & 3+30 \\\\ 4+40 & 5+50 & 6+60 \\end{pmatrix} = \\begin{pmatrix} 11 & 22 & 33 \\\\ 44 & 55 & 66 \\end{pmatrix}$$</p>
        </div>

        <div class="concept-box" style="margin-top: 25px;">
            <h3>Subtraction</h3>
            <p>Subtraction works exactly the same way as addition—just subtract corresponding elements:</p>
            <p>$$\\mathbf{A} - \\mathbf{B} = \\begin{pmatrix} a_{11}-b_{11} & a_{12}-b_{12} \\\\ a_{21}-b_{21} & a_{22}-b_{22} \\end{pmatrix}$$</p>
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
            <p>$$\\text{Prices: } \\begin{pmatrix} 20 & 30 & 40 \\end{pmatrix} \\quad \\Rightarrow \\quad 0.5 \\times \\begin{pmatrix} 20 & 30 & 40 \\end{pmatrix} = \\begin{pmatrix} 10 & 15 & 20 \\end{pmatrix}$$</p>

            <p>$$k \\cdot \\mathbf{A} = \\begin{pmatrix} ka_{11} & ka_{12} \\\\ ka_{21} & ka_{22} \\end{pmatrix}$$</p>

            <p><strong>Key insight:</strong> A single number multiplied by every element means you're scaling the entire matrix. This is why it's called "scalar" multiplication.</p>

            <svg viewBox="-5 -5 430 100" style="margin: 20px auto; display: block; max-width: 100%; height: auto;">
                <!-- Scalar -->
                <text x="15" y="48" font-size='16' fill='currentColor' font-weight='bold'>3</text>

                <!-- Multiplication sign -->
                <text x="40" y="48" font-size='16' fill='currentColor' text-anchor='middle'>×</text>

                <!-- Matrix -->
                <rect x="60" y="15" width="70" height="65" fill='none' stroke='#4f8ef7' stroke-width="2" rx='4'/>
                <text x="80" y="42" font-size='14' fill='currentColor'>1</text>
                <text x="110" y="42" font-size='14' fill='currentColor'>2</text>
                <text x="80" y="67" font-size='14' fill='currentColor'>3</text>
                <text x="110" y="67" font-size='14' fill='currentColor'>4</text>

                <!-- Equals -->
                <text x="155" y="48" font-size='16' fill='currentColor' text-anchor='middle'>=</text>

                <!-- Result -->
                <rect x="180" y="15" width="80" height="65" fill='none' stroke='#2dd4bf' stroke-width="2" rx='4'/>
                <text x="200" y="42" font-size='14' fill='currentColor'>3</text>
                <text x="240" y="42" font-size='14' fill='currentColor'>6</text>
                <text x="200" y="67" font-size='14' fill='currentColor'>9</text>
                <text x="237" y="67" font-size='14' fill='currentColor'>12</text>

                <!-- Annotation -->
                <text x="330" y="50" font-size='11' fill='currentColor' opacity='0.6'>(each element × 3)</text>
            </svg>
        </div>

        <div class="worked-example" style="margin-top: 25px;">
            <h4>Worked Example: Scalar Multiplication</h4>
            <p><strong>Question:</strong> Find \\(2\\mathbf{A}\\) where \\(\\mathbf{A} = \\begin{pmatrix} 5 & -3 \\\\ 1 & 4 \\end{pmatrix}\\)</p>
            <p><strong>Solution:</strong> Multiply each element by 2:</p>
            <p>$$2\\mathbf{A} = 2 \\times \\begin{pmatrix} 5 & -3 \\\\ 1 & 4 \\end{pmatrix} = \\begin{pmatrix} 10 & -6 \\\\ 2 & 8 \\end{pmatrix}$$</p>
        </div>

        <div class="concept-box" style="margin-top: 25px;">
            <h3>Properties of Matrix Operations</h3>
            <ul style="margin-left: 20px;">
                <li><strong>Commutativity of addition:</strong> \\(\\mathbf{A} + \\mathbf{B} = \\mathbf{B} + \\mathbf{A}\\)</li>
                <li><strong>Associativity:</strong> \\((\\mathbf{A} + \\mathbf{B}) + \\mathbf{C} = \\mathbf{A} + (\\mathbf{B} + \\mathbf{C})\\)</li>
                <li><strong>Distributive law:</strong> \\(k(\\mathbf{A} + \\mathbf{B}) = k\\mathbf{A} + k\\mathbf{B}\\)</li>
                <li><strong>Identity:</strong> \\(\\mathbf{A} + \\mathbf{0} = \\mathbf{A}\\)</li>
                <li><strong>Scalar associativity:</strong> \\(k(m\\mathbf{A}) = (km)\\mathbf{A}\\)</li>
            </ul>
        </div>
        """
    }
]
