TITLE = "Lines of Symmetry"

SECTIONS = [
    {
        "title": "What is a Line of Symmetry?",
        "body": """
        <h3>Definition</h3>
        <p>A <strong>line of symmetry</strong> is an <strong>imaginary line</strong> that divides a shape into two parts that are <strong>exact mirror images</strong> of each other.</p>

        <div class="concept-box">
            <p><strong>The Fold Test:</strong> Imagine folding the shape along a line. If the two halves match perfectly when folded, that line is a line of symmetry!</p>
        </div>

        <h3>Example: The Letter "H"</h3>
        <p>The letter H has a <strong>vertical line of symmetry</strong> down the middle.</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 200 150" style="width:100%;max-width:300px;height:auto;display:block;margin:16px auto;">
                <!-- Left vertical line of H -->
                <rect x="40" y="30" width="15" height="90" fill='#60a5fa' stroke='#1e40af' stroke-width="2"/>

                <!-- Horizontal bar of H -->
                <rect x="40" y="70" width="80" height="15" fill='#60a5fa' stroke='#1e40af' stroke-width="2"/>

                <!-- Right vertical line of H -->
                <rect x="105" y="30" width="15" height="90" fill='#60a5fa' stroke='#1e40af' stroke-width="2"/>

                <!-- Line of symmetry -->
                <line x1="100" y1="20" x2="100" y2="130" stroke='#ef4444' stroke-width="2" stroke-dasharray="5,5"/>
                <text x="110" y="75" fill='#ef4444' font-size='12' font-weight='bold'>Symmetry</text>

                <text x="100" y="145" text-anchor='middle' fill='#e6edf3' font-size='12' font-weight='bold'>Letter H: Vertical Line of Symmetry</text>
            </svg>
        </div>

        <p>The left side is the mirror image of the right side.</p>
        """
    },
    {
        "title": "Counting Lines of Symmetry in Common Shapes",
        "body": """
        <h3>Different Shapes, Different Numbers</h3>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 520 350" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
                <!-- CIRCLE -->
                <circle cx="80" cy="80" r="50" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>
                <line x1="30" y1="80" x2="130" y2="80" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <line x1="80" y1="30" x2="80" y2="130" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <line x1="42" y1="42" x2="118" y2="118" stroke='#22c55e' stroke-width="1.5" stroke-dasharray="5,5"/>
                <line x1="118" y1="42" x2="42" y2="118" stroke='#22c55e' stroke-width="1.5" stroke-dasharray="5,5"/>
                <text x="80" y="160" text-anchor='middle' fill='#e6edf3' font-weight='bold'>Circle: ∞ lines</text>

                <!-- SQUARE -->
                <rect x="200" y="30" width="100" height="100" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>
                <line x1="250" y1="20" x2="250" y2="140" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <line x1="200" y1="80" x2="300" y2="80" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <line x1="205" y1="25" x2="295" y2="135" stroke='#22c55e' stroke-width="1.5" stroke-dasharray="5,5"/>
                <line x1="295" y1="25" x2="205" y2="135" stroke='#22c55e' stroke-width="1.5" stroke-dasharray="5,5"/>
                <text x="250" y="160" text-anchor='middle' fill='#e6edf3' font-weight='bold'>Square: 4 lines</text>

                <!-- RECTANGLE -->
                <rect x="400" y="40" width="80" height="60" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>
                <line x1="440" y1="30" x2="440" y2="110" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <line x1="400" y1="70" x2="480" y2="70" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <text x="440" y="160" text-anchor='middle' fill='#e6edf3' font-weight='bold'>Rectangle: 2 lines</text>

                <!-- EQUILATERAL TRIANGLE -->
                <polygon points="80,220 30,300 130,300" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>
                <line x1="80" y1="220" x2="80" y2="300" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <line x1="48" y1="250" x2="112" y2="290" stroke='#22c55e' stroke-width="1.5" stroke-dasharray="5,5"/>
                <line x1="112" y1="250" x2="48" y2="290" stroke='#22c55e' stroke-width="1.5" stroke-dasharray="5,5"/>
                <text x="80" y="320" text-anchor='middle' fill='#e6edf3' font-weight='bold'>Equilateral △: 3 lines</text>

                <!-- ISOSCELES TRIANGLE -->
                <polygon points="280,220 240,300 320,300" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>
                <line x1="280" y1="220" x2="280" y2="300" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <text x="280" y="320" text-anchor='middle' fill='#e6edf3' font-weight='bold'>Isosceles △: 1 line</text>

                <!-- SCALENE TRIANGLE (no symmetry) -->
                <polygon points="420,240 380,300 460,300" fill='#4f8ef720' stroke='#e74c3c' stroke-width="2" stroke-dasharray="3,3"/>
                <text x="420" y="320" text-anchor='middle' fill='#e74c3c' font-weight='bold'>Scalene △: 0 lines</text>
            </svg>
        </div>

        <h3>Summary Table</h3>
        <table style="width:100%;margin:20px 0;border-collapse:collapse;">
            <tr style="background:#1e293b;">
                <th style="border: 1px solid #475569; padding: 10px; text-align: left">Shape</th>
                <th style="border: 1px solid #475569; padding: 10px; text-align: center">Lines of Symmetry</th>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Circle</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">∞ (infinite)</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Square</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">4</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Rectangle</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">2</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Equilateral Triangle</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">3</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Isosceles Triangle</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">1</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Scalene Triangle</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">0</td>
            </tr>
        </table>
        """
    },
    {
        "title": "Types of Lines of Symmetry",
        "body": """
        <h3>Vertical Lines of Symmetry</h3>
        <p>A vertical line runs up-down through the middle of the shape.</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 250 150" style="width:100%;max-width:350px;height:auto;display:block;margin:16px auto;">
                <!-- Left side of letter A -->
                <polygon points="125,40 100,100 110,100" fill='#60a5fa' opacity='0.7'/>
                <!-- Right side of letter A -->
                <polygon points="125,40 150,100 140,100" fill='#60a5fa' opacity='0.7'/>
                <!-- Horizontal bar -->
                <rect x="105" y="75" width="40" height="8" fill='#60a5fa'/>
                <!-- Vertical line of symmetry -->
                <line x1="125" y1="30" x2="125" y2="110" stroke='#ef4444' stroke-width="2" stroke-dasharray="5,5"/>
                <text x="125" y="140" text-anchor='middle' fill='#e6edf3' font-size='12' font-weight='bold'>Letter A: Vertical Symmetry</text>
            </svg>
        </div>

        <h3>Horizontal Lines of Symmetry</h3>
        <p>A horizontal line runs left-right through the middle of the shape.</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 250 150" style="width:100%;max-width:350px;height:auto;display:block;margin:16px auto;">
                <!-- Top part -->
                <circle cx="125" cy="50" r="20" fill='#60a5fa' opacity='0.7'/>
                <!-- Bottom part -->
                <circle cx="125" cy="100" r="20" fill='#60a5fa' opacity='0.7'/>
                <!-- Horizontal line of symmetry -->
                <line x1="70" y1="75" x2="180" y2="75" stroke='#ef4444' stroke-width="2" stroke-dasharray="5,5"/>
                <text x="125" y="140" text-anchor='middle' fill='#e6edf3' font-size='12' font-weight='bold'>Letter B: Horizontal Symmetry</text>
            </svg>
        </div>

        <h3>Diagonal Lines of Symmetry</h3>
        <p>A diagonal line goes at an angle (like from corner to corner in a square).</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 300 150" style="width:100%;max-width:350px;height:auto;display:block;margin:16px auto;">
                <!-- Square -->
                <rect x="75" y="30" width="80" height="80" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>
                <!-- Diagonal 1 -->
                <line x1="80" y1="35" x2="155" y2="110" stroke='#ef4444' stroke-width="2" stroke-dasharray="5,5"/>
                <!-- Diagonal 2 -->
                <line x1="155" y1="35" x2="80" y2="110" stroke='#22c55e' stroke-width="2" stroke-dasharray="5,5"/>
                <text x="115" y="140" text-anchor='middle' fill='#e6edf3' font-size='12' font-weight='bold'>Square: 2 Diagonal Lines</text>
            </svg>
        </div>
        """
    },
    {
        "title": "Symmetry in Letters and Numbers",
        "body": """
        <h3>Which Letters Have Symmetry?</h3>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 600 200" style="width:100%;max-width:700px;height:auto;display:block;margin:16px auto;">
                <!-- Row 1: Letters with vertical symmetry -->
                <text x="30" y="50" fill='#22c55e' font-size='36' font-weight='bold'>A</text>
                <line x1="40" y1="10" x2="40" y2="60" stroke='#22c55e' stroke-width="1" stroke-dasharray="3,3"/>

                <text x="90" y="50" fill='#22c55e' font-size='36' font-weight='bold'>H</text>
                <line x1="100" y1="10" x2="100" y2="60" stroke='#22c55e' stroke-width="1" stroke-dasharray="3,3"/>

                <text x="150" y="50" fill='#22c55e' font-size='36' font-weight='bold'>M</text>
                <line x1="160" y1="10" x2="160" y2="60" stroke='#22c55e' stroke-width="1" stroke-dasharray="3,3"/>

                <text x="210" y="50" fill='#22c55e' font-size='36' font-weight='bold'>O</text>
                <line x1="220" y1="10" x2="220" y2="60" stroke='#22c55e' stroke-width="1" stroke-dasharray="3,3"/>

                <text x="270" y="50" fill='#22c55e' font-size='36' font-weight='bold'>T</text>
                <line x1="280" y1="10" x2="280" y2="60" stroke='#22c55e' stroke-width="1" stroke-dasharray="3,3"/>

                <text x="330" y="50" fill='#22c55e' font-size='36' font-weight='bold'>V</text>
                <line x1="340" y1="10" x2="340" y2="60" stroke='#22c55e' stroke-width="1" stroke-dasharray="3,3"/>

                <text x="390" y="50" fill='#22c55e' font-size='36' font-weight='bold'>W</text>
                <line x1="400" y1="10" x2="400" y2="60" stroke='#22c55e' stroke-width="1" stroke-dasharray="3,3"/>

                <text x="450" y="50" fill='#22c55e' font-size='36' font-weight='bold'>X</text>
                <line x1="460" y1="10" x2="460" y2="60" stroke='#22c55e' stroke-width="1" stroke-dasharray="3,3"/>

                <text x="510" y="50" fill='#22c55e' font-size='36' font-weight='bold'>Y</text>
                <line x1="520" y1="10" x2="520" y2="60" stroke='#22c55e' stroke-width="1" stroke-dasharray="3,3"/>

                <!-- Row 2: No symmetry -->
                <text x="30" y="120" fill='#ef4444' font-size='36' font-weight='bold'>F</text>
                <text x="35" y="175" fill='#ef4444' font-size='12'>✗ No symmetry</text>

                <text x="90" y="120" fill='#ef4444' font-size='36' font-weight='bold'>L</text>
                <text x="85" y="175" fill='#ef4444' font-size='12'>✗ No symmetry</text>

                <text x="150" y="120" fill='#ef4444' font-size='36' font-weight='bold'>P</text>
                <text x="145" y="175" fill='#ef4444' font-size='12'>✗ No symmetry</text>

                <text x="210" y="120" fill='#ef4444' font-size='36' font-weight='bold'>Z</text>
                <text x="205" y="175" fill='#ef4444' font-size='12'>✗ No symmetry</text>
            </svg>
        </div>

        <h3>Numbers with Symmetry</h3>
        <ul>
            <li><strong>0:</strong> 2 lines of symmetry (vertical and horizontal)</li>
            <li><strong>1:</strong> 1 line of symmetry (vertical)</li>
            <li><strong>2:</strong> 1 line of symmetry (horizontal, depending on font)</li>
            <li><strong>3:</strong> Depends on font</li>
            <li><strong>8:</strong> 2 lines of symmetry (vertical and horizontal)</li>
        </ul>
        """
    },
    {
        "title": "How to Find Lines of Symmetry",
        "body": """
        <h3>The Fold Test Method</h3>

        <div class="worked-example">
            <p><strong>Step 1:</strong> Choose a potential line of symmetry (vertical, horizontal, or diagonal).</p>
            <p><strong>Step 2:</strong> Imagine folding the shape along that line.</p>
            <p><strong>Step 3:</strong> Check: Do both halves match perfectly?</p>
            <p><strong>Step 4:</strong> If yes, that's a line of symmetry. If no, try another line.</p>
        </div>

        <h3>Practice: Rectangle</h3>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 400 200" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
                <!-- Rectangle -->
                <rect x="100" y="40" width="200" height="100" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>

                <!-- Vertical line -->
                <line x1="200" y1="30" x2="200" y2="150" stroke='#ef4444' stroke-width="2" stroke-dasharray="5,5"/>
                <text x="210" y="90" fill='#ef4444' font-size='13' font-weight='bold'>✓</text>

                <!-- Horizontal line -->
                <line x1="90" y1="90" x2="310" y2="90" stroke='#22c55e' stroke-width="2" stroke-dasharray="5,5"/>
                <text x="320" y="95" fill='#22c55e' font-size='13' font-weight='bold'>✓</text>

                <!-- Diagonal (wrong) -->
                <line x1="110" y1="45" x2="290" y2="135" stroke='#8b5cf6' stroke-width="1.5" stroke-dasharray="5,5" opacity='0.5'/>
                <text x="305" y="90" fill='#8b5cf6' font-size='13' font-weight='bold'>✗</text>

                <text x="200" y="180" text-anchor='middle' fill='#e6edf3' font-size='12'>Rectangle: 2 lines of symmetry</text>
            </svg>
        </div>

        <div class="success-box">
            <p><strong>Tip:</strong> Start with the most obvious lines (vertical and horizontal) before trying diagonals.</p>
        </div>
        """
    }
]
