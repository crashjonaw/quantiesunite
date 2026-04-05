TITLE = "Symmetry in Shapes"

SECTIONS = [
    {
        "title": "Triangles: The Variety of Symmetry",
        "body": """
        <h3>Equilateral Triangle (All sides equal)</h3>
        <p><strong>3 lines of symmetry</strong> — one through each vertex to the midpoint of the opposite side.</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 300 250" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
                <!-- Equilateral triangle -->
                <polygon points="150,50 80,200 220,200" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>

                <!-- Vertical line (top to bottom middle) -->
                <line x1="150" y1="50" x2="150" y2="200" stroke='#ef4444' stroke-width="2" stroke-dasharray="5,5"/>

                <!-- Line from bottom-left to opposite midpoint -->
                <line x1="80" y1="200" x2="185" y2="125" stroke='#22c55e' stroke-width="1.5" stroke-dasharray="5,5"/>

                <!-- Line from bottom-right to opposite midpoint -->
                <line x1="220" y1="200" x2="115" y2="125" stroke='#22c55e' stroke-width="1.5" stroke-dasharray="5,5"/>

                <text x="150" y="230" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>Equilateral: 3 lines of symmetry</text>
            </svg>
        </div>

        <h3>Isosceles Triangle (Two equal sides)</h3>
        <p><strong>1 line of symmetry</strong> — vertical line from the top vertex to the midpoint of the base.</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 300 250" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
                <!-- Isosceles triangle -->
                <polygon points="150,50 100,200 200,200" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>

                <!-- Vertical line only -->
                <line x1="150" y1="50" x2="150" y2="200" stroke='#ef4444' stroke-width="2" stroke-dasharray="5,5"/>

                <text x="150" y="230" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>Isosceles: 1 line of symmetry</text>
            </svg>
        </div>

        <h3>Scalene Triangle (All sides different)</h3>
        <p><strong>0 lines of symmetry</strong> — no fold line makes the two halves match.</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 300 250" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
                <!-- Scalene triangle -->
                <polygon points="150,60 90,200 240,200" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>

                <!-- Show that no line works with X -->
                <text x="150" y="130" text-anchor='middle' fill='#ef4444' font-size='24' font-weight='bold'>✗</text>

                <text x="150" y="230" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>Scalene: 0 lines of symmetry</text>
            </svg>
        </div>

        <h3>Rule for Triangles</h3>
        <div class="concept-box">
            <ul>
                <li><strong>Equilateral:</strong> All angles equal → 3 lines of symmetry</li>
                <li><strong>Isosceles:</strong> Two angles equal → 1 line of symmetry</li>
                <li><strong>Scalene:</strong> All angles different → 0 lines of symmetry</li>
            </ul>
        </div>
        """
    },
    {
        "title": "Quadrilaterals: Squares, Rectangles, and More",
        "body": """
        <h3>Square: Perfect Symmetry</h3>
        <p><strong>4 lines of symmetry</strong> — 2 diagonal, 1 vertical, 1 horizontal.</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 300 220" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
                <!-- Square -->
                <rect x="100" y="40" width="100" height="100" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>

                <!-- Vertical -->
                <line x1="150" y1="30" x2="150" y2="160" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>

                <!-- Horizontal -->
                <line x1="90" y1="90" x2="210" y2="90" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>

                <!-- Diagonal 1 -->
                <line x1="105" y1="45" x2="195" y2="135" stroke='#22c55e' stroke-width="1.5" stroke-dasharray="5,5"/>

                <!-- Diagonal 2 -->
                <line x1="195" y1="45" x2="105" y2="135" stroke='#22c55e' stroke-width="1.5" stroke-dasharray="5,5"/>

                <text x="150" y="180" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>Square: 4 lines of symmetry</text>
            </svg>
        </div>

        <h3>Rectangle: Limited Symmetry</h3>
        <p><strong>2 lines of symmetry</strong> — 1 vertical, 1 horizontal (no diagonals).</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 350 220" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
                <!-- Rectangle -->
                <rect x="100" y="50" width="150" height="80" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>

                <!-- Vertical -->
                <line x1="175" y1="40" x2="175" y2="140" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>

                <!-- Horizontal -->
                <line x1="90" y1="90" x2="260" y2="90" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>

                <!-- Show diagonals DON'T work -->
                <line x1="105" y1="55" x2="245" y2="125" stroke='#8b5cf6' stroke-width="1" stroke-dasharray="3,3" opacity='0.4'/>
                <text x="255" y="85" fill='#8b5cf6' font-size='11'>✗</text>

                <text x="175" y="180" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>Rectangle: 2 lines of symmetry</text>
            </svg>
        </div>

        <h3>Rhombus: Diagonal Symmetry</h3>
        <p><strong>2 lines of symmetry</strong> — both diagonal lines.</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 300 220" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
                <!-- Rhombus -->
                <polygon points="150,40 210,90 150,140 90,90" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>

                <!-- Diagonal 1 (vertical) -->
                <line x1="150" y1="40" x2="150" y2="140" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>

                <!-- Diagonal 2 (horizontal) -->
                <line x1="90" y1="90" x2="210" y2="90" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>

                <text x="150" y="180" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>Rhombus: 2 lines of symmetry</text>
            </svg>
        </div>
        """
    },
    {
        "title": "Circles: Infinite Symmetry",
        "body": """
        <h3>Circle: The Ultimate Symmetrical Shape</h3>
        <p><strong>∞ (infinite) lines of symmetry</strong> — ANY line through the center is a line of symmetry!</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 300 220" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
                <!-- Circle -->
                <circle cx="150" cy="90" r="70" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>

                <!-- Several lines of symmetry through the center -->
                <line x1="80" y1="90" x2="220" y2="90" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <line x1="150" y1="20" x2="150" y2="160" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <line x1="95" y1="35" x2="205" y2="145" stroke='#22c55e' stroke-width="1.5" stroke-dasharray="5,5"/>
                <line x1="205" y1="35" x2="95" y2="145" stroke='#22c55e' stroke-width="1.5" stroke-dasharray="5,5"/>
                <line x1="115" y1="30" x2="185" y2="150" stroke='#fbbf24' stroke-width="1.5" stroke-dasharray="5,5"/>

                <!-- Center point -->
                <circle cx="150" cy="90" r="3" fill='#ffffff' stroke='#ffffff' stroke-width="1"/>

                <text x="150" y="180" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>Circle: ∞ lines of symmetry</text>
            </svg>
        </div>

        <h3>Why a Circle Has Infinite Symmetry</h3>
        <p>A circle is perfectly round. Every point on the circle is the same distance from the center. This means you can draw a line from the center in <strong>any direction</strong>, and it divides the circle into two perfect mirror images.</p>

        <div class="success-box">
            <p><strong>The Center is Key:</strong> Any line through the center of a circle is a line of symmetry. There are infinite directions you can draw a line, so there are infinite lines of symmetry!</p>
        </div>
        """
    },
    {
        "title": "Completing Symmetric Figures Using a Grid",
        "body": """
        <h3>The Method</h3>

        <div class="worked-example">
            <p><strong>Step 1:</strong> Find the line of symmetry (marked with a dashed line).</p>
            <p><strong>Step 2:</strong> Look at a point on the given half. Count its distance from the line.</p>
            <p><strong>Step 3:</strong> On the other side of the line, mark a point the same distance away.</p>
            <p><strong>Step 4:</strong> Connect the points to draw the mirror image.</p>
        </div>

        <h3>Grid Example: Complete the Heart</h3>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 400 300" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
                <!-- Grid background -->
                <defs>
                    <pattern id="grid" width="25" height="25" patternUnits="userSpaceOnUse">
                        <path d="M 25 0 L 0 0 0 25" fill='none' stroke='#475569' stroke-width="0.5"/>
                    </pattern>
                </defs>
                <rect width="400" height="300" fill='#0f172a' class="background"/>
                <rect width="400" height="300" fill='url(#grid)' class="grid"/>

                <!-- Vertical line of symmetry -->
                <line x1="200" y1="20" x2="200" y2="280" stroke='#ef4444' stroke-width="2" stroke-dasharray="5,5"/>
                <text x="210" y="40" fill='#ef4444' font-size='12' font-weight='bold'>Fold Line</text>

                <!-- Right half of heart (given) -->
                <path d="M 200 80 Q 260 40 280 60 Q 300 85 200 180" fill='#60a5fa' opacity='0.7' stroke='#1e40af' stroke-width="2"/>

                <!-- Left half of heart (to complete - shown lighter) -->
                <path d="M 200 80 Q 140 40 120 60 Q 100 85 200 180" fill='#60a5fa' opacity='0.3' stroke='#1e40af' stroke-width="1" stroke-dasharray="3,3"/>

                <!-- Grid points to help -->
                <circle cx="280" cy="60" r="2" fill='#fbbf24'/>
                <circle cx="120" cy="60" r="2" fill='#fbbf24'/>

                <text x="200" y="260" text-anchor='middle' fill='currentColor' font-size='11'>Mirror the right half across the fold line</text>
            </svg>
        </div>

        <h3>Tips for Completing Figures</h3>
        <div class="concept-box">
            <ul>
                <li><strong>Use grid squares:</strong> Count squares from the line to help measure distances.</li>
                <li><strong>Mark key points first:</strong> Corners and peaks are easiest to mirror.</li>
                <li><strong>Connect smoothly:</strong> Once you have the points, connect them to match the shape.</li>
                <li><strong>Check your work:</strong> Fold your paper along the line. Both halves should match!</li>
            </ul>
        </div>
        """
    },
    {
        "title": "Real-World Symmetry: Shapes Around Us",
        "body": """
        <h3>Common Shapes and Their Symmetry</h3>

        <table style="width:100%;margin:20px 0;border-collapse:collapse;">
            <tr style="background:#1e293b;">
                <th style="border: 1px solid #475569; padding: 10px; text-align: left">Shape</th>
                <th style="border: 1px solid #475569; padding: 10px; text-align: center">Lines of Symmetry</th>
                <th style="border: 1px solid #475569; padding: 10px; text-align: left">Real-World Examples</th>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Circle</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">∞</td>
                <td style="border:1px solid #475569;padding:10px;">Wheels, coins, clocks, plates</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Square</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">4</td>
                <td style="border:1px solid #475569;padding:10px;">Tiles, windows, traffic signs</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Rectangle</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">2</td>
                <td style="border:1px solid #475569;padding:10px;">Doors, books, tables, screens</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Equilateral Triangle</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">3</td>
                <td style="border:1px solid #475569;padding:10px;">Warning signs, pyramids</td>
            </tr>
            <tr style="background:#0f172a;">
                <td style="border:1px solid #475569;padding:10px;">Hexagon</td>
                <td style="border:1px solid #475569;padding:10px;text-align:center;">6</td>
                <td style="border:1px solid #475569;padding:10px;">Honeycomb, nuts, snowflakes</td>
            </tr>
        </table>

        <h3>Finding Symmetry Outdoors</h3>
        <p>Challenge yourself to spot symmetry in these places:</p>
        <ul>
            <li><strong>Road signs:</strong> Triangle warnings, octagon stop signs, round speed limits</li>
            <li><strong>Architecture:</strong> Buildings with symmetric facades, symmetric doorways</li>
            <li><strong>Nature:</strong> Leaves, flowers, butterfly wings, starfish</li>
            <li><strong>Objects:</strong> Clocks, compasses, badges, logos</li>
        </ul>
        """
    }
]
