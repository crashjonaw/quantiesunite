TITLE = "Matrix Multiplication: The Inner Product Rule"

SECTIONS = [
    {
        "title": "Why Matrix Multiplication Isn't What You'd Expect",
        "body": """
        <div class="concept-box">
            <h3>A Real Problem Matrix Multiplication Solves</h3>
            <p>Imagine a coffee shop with 3 types of coffee beans. They sell to 2 customers:</p>
            <table style="border-collapse: collapse; margin: 20px auto; width: 90%; max-width: 500px">
                <tr >
                    <th style="padding: 8px; text-align: left;">Bean Type</th>
                    <th style="padding: 8px; text-align: center;">Customer A (kg)</th>
                    <th style="padding: 8px; text-align: center;">Customer B (kg)</th>
                </tr>
                <tr >
                    <td style="padding: 8px;">Arabica</td>
                    <td style="padding: 8px; text-align: center;">2</td>
                    <td style="padding: 8px; text-align: center;">3</td>
                </tr>
                <tr >
                    <td style="padding: 8px;">Robusta</td>
                    <td style="padding: 8px; text-align: center;">1</td>
                    <td style="padding: 8px; text-align: center;">2</td>
                </tr>
                <tr class="formula-box">
                    <td style="padding: 8px;">Colombian</td>
                    <td style="padding: 8px; text-align: center;">3</td>
                    <td style="padding: 8px; text-align: center;">1</td>
                </tr>
            </table>

            <p>The prices per kg are: Arabica $8, Robusta $6, Colombian $10.</p>

            <p><strong>Question:</strong> How much does each customer pay?</p>
            <ul style="margin-left: 20px;">
                <li>Customer A: (2×8) + (1×6) + (3×10) = 16 + 6 + 30 = <strong>$52</strong></li>
                <li>Customer B: (3×8) + (2×6) + (1×10) = 24 + 12 + 10 = <strong>$46</strong></li>
            </ul>

            <p><strong>This is matrix multiplication!</strong> We're taking each column from the sales matrix and combining it with the prices using a special rule: multiply corresponding elements and sum them up.</p>
        </div>
        """
    },
    {
        "title": "The Matrix Multiplication Rule",
        "body": """
        <div class="concept-box">
            <h3>Compatibility: When Can You Multiply?</h3>
            <p>Matrix multiplication is more restrictive than addition. To multiply A (dimensions m × <strong>n</strong>) by B (dimensions <strong>n</strong> × p):</p>
            <ul style="margin-left: 20px;">
                <li><strong>The inner dimensions must match:</strong> Columns of A = Rows of B</li>
                <li><strong>Result dimensions:</strong> m × p</li>
            </ul>

            <p style="text-align: center; margin: 15px 0; font-size: 1.1em; padding: 10px">
            (m × <strong>n</strong>) × (<strong>n</strong> × p) = (m × p)
            </p>

            <p><strong>Example:</strong> A 2×3 matrix times a 3×4 matrix gives a 2×4 result.</p>
            <p><strong>NOT allowed:</strong> A 2×3 matrix times a 2×4 matrix (3 ≠ 2, so they're incompatible).</p>

            <div class="warning-box formula-box">
                <p style="margin: 0;"><strong>⚠ Common mistake:</strong> Students try to multiply incompatible matrices. Always check: "Do the inner dimensions match?"</p>
            </div>
        </div>

        <div class="concept-box" style="margin-top: 25px;">
            <h3>The Multiplication Process: Dot Product</h3>
            <p>To find element (i, j) in the result AB:</p>
            <ol style="margin-left: 20px;">
                <li>Take row <em>i</em> from matrix A</li>
                <li>Take column <em>j</em> from matrix B</li>
                <li><strong>Multiply corresponding elements and sum them</strong> (this is called the <em>dot product</em> or <em>inner product</em>)</li>
            </ol>

            <svg viewBox="0 0 500 250" style="margin: 20px auto; display: block; max-width: 100%; height: auto;">
                <!-- Matrix A -->
                <text x="20" y="20" font-size='12' fill='currentColor' font-weight='bold'>A =</text>
                <rect x="50" y="10" width="80" height="80" fill='none' stroke='#4f8ef7' stroke-width="2"/>
                <text x="65" y="35" font-size='13' fill='#4f8ef7'>1</text>
                <text x="95" y="35" font-size='13' fill='#4f8ef7'>2</text>
                <text x="125" y="35" font-size='13' fill='#4f8ef7'>3</text>
                <text x="65" y="55" font-size='13' fill='currentColor'>4</text>
                <text x="95" y="55" font-size='13' fill='currentColor'>5</text>
                <text x="125" y="55" font-size='13' fill='currentColor'>6</text>
                <text x="65" y="75" font-size='13' fill='currentColor'>7</text>
                <text x="95" y="75" font-size='13' fill='currentColor'>8</text>
                <text x="125" y="75" font-size='13' fill='currentColor'>9</text>
                <text x="90" y="110" font-size='11' fill='currentColor' opacity='0.6' text-anchor='middle'>(3 × 3)</text>

                <!-- Matrix B -->
                <text x="160" y="20" font-size='12' fill='currentColor' font-weight='bold'>B =</text>
                <rect x="195" y="10" width="60" height="80" fill='none' stroke='#4f8ef7' stroke-width="2"/>
                <text x="210" y="35" font-size='13' fill='#4f8ef7'>2</text>
                <text x="240" y="35" font-size='13' fill='#4f8ef7'>1</text>
                <text x="210" y="55" font-size='13' fill='currentColor'>0</text>
                <text x="240" y="55" font-size='13' fill='currentColor'>3</text>
                <text x="210" y="75" font-size='13' fill='currentColor'>4</text>
                <text x="240" y="75" font-size='13' fill='currentColor'>2</text>
                <text x="225" y="110" font-size='11' fill='currentColor' opacity='0.6' text-anchor='middle'>(3 × 2)</text>

                <!-- Arrow -->
                <path d="M 280 50 L 320 50" stroke='#8b949e' stroke-width="2" marker-end="url(#arrowhead)"/>

                <!-- Result -->
                <text x="335" y="20" font-size='12' fill='currentColor' font-weight='bold'>AB =</text>
                <rect x="375" y="10" width="60" height="80" fill='none' stroke='#2dd4bf' stroke-width="2"/>
                <text x="390" y="35" font-size='13' fill='#2dd4bf'>?</text>
                <text x="420" y="35" font-size='13' fill='#2dd4bf'>?</text>
                <text x="390" y="55" font-size='13' fill='currentColor'>?</text>
                <text x="420" y="55" font-size='13' fill='currentColor'>?</text>
                <text x="390" y="75" font-size='13' fill='currentColor'>?</text>
                <text x="420" y="75" font-size='13' fill='currentColor'>?</text>
                <text x="405" y="110" font-size='11' fill='currentColor' opacity='0.6' text-anchor='middle'>(3 × 2)</text>

                <!-- Example calculation -->
                <text x="20" y="150" font-size='11' fill='currentColor' opacity='0.6' font-style="italic">Example: Element (1,1) = Row 1 of A · Column 1 of B</text>
                <text x="20" y="170" font-size='12' fill='currentColor' font-family='monospace'>(1 × 2) + (2 × 0) + (3 × 4) = 2 + 0 + 12 = <strong style="color: #2dd4bf;">14</strong></text>

                <text x="20" y="200" font-size='11' fill='currentColor' opacity='0.6' font-style="italic">Example: Element (1,2) = Row 1 of A · Column 2 of B</text>
                <text x="20" y="220" font-size='12' fill='currentColor' font-family='monospace'>(1 × 1) + (2 × 3) + (3 × 2) = 1 + 6 + 6 = <strong style="color: #2dd4bf;">13</strong></text>

                <defs>
                    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                        <polygon points="0 0, 10 3, 0 6" fill='currentColor' opacity='0.6'/>
                    </marker>
                </defs>
            </svg>
        </div>
        """
    },
    {
        "title": "Key Properties and Common Mistakes",
        "body": """
        <div class="concept-box">
            <h3>Important Properties</h3>

            <h4 style="margin-top: 15px">NOT Commutative: AB ≠ BA</h4>
            <p>This is the biggest difference from regular multiplication! Order matters.</p>
            <p style="text-align: center; margin: 15px 0; font-family: monospace; font-size: 1em; color: #f85149; padding: 10px">
            <strong>A × B ≠ B × A</strong> (in general)
            </p>

            <div class="worked-example" style="margin-top: 15px;">
                <h5 style="margin-top: 0;">Example: AB ≠ BA</h5>
                <p><strong>A = (</strong>1  2<br/>3  4<strong>)&nbsp;&nbsp;&nbsp;B = (</strong>2  0<br/>1  2<strong>)</strong></p>

                <p style="margin-top: 10px;"><strong>AB:</strong></p>
                <p style="font-family: monospace; margin: 5px 0">
                (1,1): (1×2) + (2×1) = 4<br/>
                (1,2): (1×0) + (2×2) = 4<br/>
                (2,1): (3×2) + (4×1) = 10<br/>
                (2,2): (3×0) + (4×2) = 8
                </p>
                <p style="font-family: monospace; padding: 8px; border-radius: 4px">
                <strong>AB = (</strong>4  4<br/>10  8<strong>)</strong>
                </p>

                <p style="margin-top: 10px;"><strong>BA:</strong></p>
                <p style="font-family: monospace; margin: 5px 0">
                (1,1): (2×1) + (0×3) = 2<br/>
                (1,2): (2×2) + (0×4) = 4<br/>
                (2,1): (1×1) + (2×3) = 7<br/>
                (2,2): (1×2) + (2×4) = 10
                </p>
                <p style="font-family: monospace; padding: 8px; border-radius: 4px">
                <strong>BA = (</strong>2  4<br/>7  10<strong>)</strong>
                </p>

                <p style="color: #2dd4bf; margin-top: 10px;"><strong>✓ Clearly AB ≠ BA</strong></p>
            </div>

            <h4 class="accent-heading" style="margin-top: 20px;">Associative: (AB)C = A(BC)</h4>
            <p>The grouping doesn't matter (though you still can't change the order).</p>

            <h4 style="margin-top: 15px">Distributive: A(B + C) = AB + AC</h4>
            <p>You can distribute multiplication over addition.</p>

            <h4 style="margin-top: 15px">Identity: AI = IA = A</h4>
            <p>Multiplying by the identity matrix doesn't change the matrix (like multiplying by 1).</p>
        </div>

        <div class="warning-box" style="margin-top: 25px;">
            <h4 style="color: #f85149; margin-top: 0;">Common Mistakes to Avoid</h4>
            <ul style="margin-left: 20px; margin-bottom: 0;">
                <li><strong>Forgetting to check compatibility:</strong> Always verify columns of A = rows of B</li>
                <li><strong>Computing element-wise multiplication instead:</strong> (A)(B) ≠ just multiplying corresponding elements</li>
                <li><strong>Assuming AB = BA:</strong> This is almost never true for matrices</li>
                <li><strong>Wrong order in the dot product:</strong> Use row from first matrix, column from second matrix</li>
            </ul>
        </div>
        """
    }
]
