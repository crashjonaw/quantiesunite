TITLE = "What is Symmetry?"

SECTIONS = [
    {
        "title": "Understanding Symmetry",
        "body": """
        <h3>What is Symmetry?</h3>
        <p><strong>Symmetry</strong> means a shape or object is <strong>balanced and identical on both sides of a line or point</strong>. If you fold the shape along a special line called the <strong>line of symmetry</strong>, the two sides match perfectly.</p>

        <div class="concept-box">
            <p><strong>First Principle:</strong> Fold a piece of paper in half. If the two sides match perfectly, that fold line is a LINE OF SYMMETRY. Symmetry means one half is a mirror image of the other.</p>
        </div>

        <h3>Mirror Image Example</h3>
        <p>Imagine looking at a butterfly. If you draw an imaginary line down its middle, the <strong>left wing is an exact mirror image of the right wing</strong>. This is symmetry!</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 400 200" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
                <!-- Mirror line -->
                <line x1="200" y1="20" x2="200" y2="180" stroke='#ef4444' stroke-width="2" stroke-dasharray="5,5"/>
                <text x="210" y="100" fill='#ef4444' font-size='12' font-weight='bold'>Line of Symmetry</text>

                <!-- Left wing -->
                <ellipse cx="140" cy="80" rx="40" ry="60" fill='#22c55e' opacity='0.7' stroke='#16a34a' stroke-width="2"/>
                <circle cx="130" cy="70" r="4" fill='#16a34a'/>
                <circle cx="130" cy="90" r="4" fill='#16a34a'/>

                <!-- Right wing (mirror) -->
                <ellipse cx="260" cy="80" rx="40" ry="60" fill='#22c55e' opacity='0.7' stroke='#16a34a' stroke-width="2"/>
                <circle cx="270" cy="70" r="4" fill='#16a34a'/>
                <circle cx="270" cy="90" r="4" fill='#16a34a'/>

                <!-- Body -->
                <rect x="195" y="70" width="10" height="80" fill='#4f46e5' stroke='#312e81' stroke-width="1"/>
                <circle cx="200" cy="65" r="8" fill='#4f46e5' stroke='#312e81' stroke-width="1"/>

                <text x="200" y="160" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>Butterfly: Perfect Symmetry</text>
            </svg>
        </div>
        """
    },
    {
        "title": "Why Is Symmetry Important?",
        "body": """
        <h3>Symmetry in Nature</h3>
        <p>Nature loves symmetry! Symmetric things have special properties that make problems easier to solve. Let's see where symmetry appears:</p>

        <div class="worked-example">
            <p><strong>🦋 Butterflies:</strong> Bilateral symmetry (left-right)</p>
            <p><strong>❄️ Snowflakes:</strong> 6-fold rotational symmetry</p>
            <p><strong>🌻 Flowers:</strong> Rotational symmetry (3-fold, 4-fold, 5-fold)</p>
            <p><strong>👤 Human faces:</strong> Nearly bilateral symmetry</p>
        </div>

        <h3>Symmetry in Art and Design</h3>
        <ul>
            <li><strong>Creates balance:</strong> Symmetrical designs look pleasing and organized</li>
            <li><strong>Makes recognition easier:</strong> Our brains recognize symmetrical shapes faster</li>
            <li><strong>Improves beauty:</strong> Logos, buildings, and patterns use symmetry intentionally</li>
        </ul>

        <h3>Symmetry in Mathematics</h3>
        <p>Mathematicians study symmetry because:</p>
        <ul>
            <li>It reveals hidden patterns and properties</li>
            <li>It simplifies complex problems</li>
            <li>It helps us classify and organize shapes</li>
        </ul>
        """
    },
    {
        "title": "Two Main Types of Symmetry",
        "body": """
        <h3>1. Reflective Symmetry (Mirror Symmetry)</h3>
        <p>One half of a shape is a <strong>mirror image</strong> of the other half.</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 400 150" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
                <!-- Mirror line -->
                <line x1="200" y1="10" x2="200" y2="140" stroke='#ef4444' stroke-width="2" stroke-dasharray="5,5"/>

                <!-- Left triangle -->
                <polygon points="200,30 140,110 160,110" fill='#60a5fa' opacity='0.8' stroke='#1e40af' stroke-width="2"/>

                <!-- Right triangle (mirror) -->
                <polygon points="200,30 260,110 240,110" fill='#60a5fa' opacity='0.8' stroke='#1e40af' stroke-width="2"/>

                <text x="200" y="145" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>Reflective Symmetry</text>
            </svg>
        </div>

        <p><strong>Test:</strong> If you fold the shape along the line, both halves match perfectly.</p>

        <h3>2. Rotational Symmetry</h3>
        <p>A shape looks <strong>the same after rotating it</strong> (turning it) around a center point, without flipping it.</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 400 150" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
                <!-- Center point -->
                <circle cx="100" cy="75" r="3" fill='#fbbf24' stroke='#b45309' stroke-width="1"/>

                <!-- Square showing rotation -->
                <rect x="60" y="35" width="80" height="80" fill='none' stroke='#22c55e' stroke-width="2"/>
                <text x="85" y="65" fill='#22c55e' font-size='11'>90°</text>

                <!-- Center point -->
                <circle cx="280" cy="75" r="3" fill='#fbbf24' stroke='#b45309' stroke-width="1"/>

                <!-- Rotated square (same looking) -->
                <rect x="240" y="35" width="80" height="80" fill='none' stroke='#22c55e' stroke-width="2"/>
                <text x="265" y="65" fill='#22c55e' font-size='11'>180°</text>

                <text x="200" y="145" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>Rotational Symmetry (Order 2)</text>
            </svg>
        </div>

        <p><strong>Test:</strong> Rotate the shape 360°. Count how many times it looks identical.</p>
        """
    },
    {
        "title": "Symmetry vs. No Symmetry",
        "body": """
        <h3>Symmetrical Shapes</h3>
        <p>These shapes have at least one line of symmetry:</p>

        <div style="text-align:center;margin:20px 0;">
            <svg viewBox="0 0 500 120" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
                <!-- Circle -->
                <circle cx="60" cy="60" r="40" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>
                <line x1="20" y1="60" x2="100" y2="60" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <text x="60" y="110" text-anchor='middle' fill='currentColor' font-size='11'>Circle (∞)</text>

                <!-- Square -->
                <rect x="140" y="20" width="60" height="60" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>
                <line x1="170" y1="10" x2="170" y2="90" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <line x1="140" y1="50" x2="200" y2="50" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <text x="170" y="110" text-anchor='middle' fill='currentColor' font-size='11'>Square (4)</text>

                <!-- Equilateral Triangle -->
                <polygon points="310,80 270,20 350,20" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>
                <line x1="310" y1="80" x2="310" y2="20" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <text x="310" y="110" text-anchor='middle' fill='currentColor' font-size='11'>Equilateral △ (3)</text>

                <!-- Rectangle -->
                <rect x="380" y="30" width="80" height="50" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="2"/>
                <line x1="420" y1="20" x2="420" y2="90" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <line x1="380" y1="55" x2="460" y2="55" stroke='#ef4444' stroke-width="1.5" stroke-dasharray="5,5"/>
                <text x="420" y="110" text-anchor='middle' fill='currentColor' font-size='11'>Rectangle (2)</text>
            </svg>
        </div>

        <h3>Asymmetrical Shapes</h3>
        <p>These shapes have <strong>no lines of symmetry</strong>:</p>

        <div class="warning-box">
            <p><strong>Scalene triangle:</strong> All sides different lengths → No symmetry</p>
            <p><strong>Letter "F":</strong> Left and right sides don't match → No symmetry</p>
            <p><strong>Irregular quadrilateral:</strong> No matching sides → No symmetry</p>
        </div>
        """
    },
    {
        "title": "Key Vocabulary",
        "body": """
        <h3>Essential Terms</h3>

        <div class="concept-box">
            <p><strong>Line of Symmetry:</strong> An imaginary line where a shape can be folded so both halves match perfectly.</p>
            <p><strong>Reflective Symmetry:</strong> When one half is a mirror image of the other half.</p>
            <p><strong>Rotational Symmetry:</strong> When a shape looks the same after being turned around a center point.</p>
            <p><strong>Order of Rotational Symmetry:</strong> How many times a shape looks identical during a 360° rotation.</p>
            <p><strong>Bilateral Symmetry:</strong> Left-right symmetry (like a butterfly).</p>
            <p><strong>Asymmetrical:</strong> A shape with no lines of symmetry.</p>
        </div>

        <h3>Practice Question</h3>
        <p><strong>Which of these shapes has symmetry?</strong></p>
        <ul>
            <li>A square ✓ (4 lines of symmetry)</li>
            <li>A star ✓ (multiple lines of symmetry)</li>
            <li>A random blob ✗ (usually no symmetry)</li>
        </ul>
        """
    }
]
