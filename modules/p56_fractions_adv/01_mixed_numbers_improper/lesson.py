TITLE = "Mixed Numbers and Improper Fractions"

SECTIONS = [
    {
        "title": "Improper Fractions and Mixed Numbers Compared",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Two Ways to Write the Same Amount</h3>
    <p>You already know fractions represent parts of a whole. But what happens when the numerator is bigger than the denominator? Meet the <strong>improper fraction</strong>—a fraction where the top is greater than or equal to the bottom.</p>
    <p><strong>Improper Fraction:</strong> \\(\\frac{7}{3}\\) (numerator > denominator)</p>
    <p><strong>Mixed Number:</strong> \\(2\\frac{1}{3}\\) (a whole number + a fraction)</p>
    <p>Both represent the same amount!</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 500 250" xmlns="http://www.w3.org/2000/svg">
      <text x="50" y="30" font-size='16' font-weight='bold'>\\(\\frac{7}{3}\\) shown as wholes and parts:</text>

      <circle cx="80" cy="100" r="30" fill='#4169E1' opacity='0.6'/>
      <text x="80" y="110" font-size='14' text-anchor='middle' font-weight='bold'>1</text>

      <circle cx="150" cy="100" r="30" fill='#4169E1' opacity='0.6'/>
      <text x="150" y="110" font-size='14' text-anchor='middle' font-weight='bold'>2</text>

      <circle cx="220" cy="100" r="30" fill='none' stroke='#8b949e' stroke-width="2"/>
      <path d="M 220 70 A 30 30 0 0 1 250 100" fill='#22c55e' opacity='0.6'/>
      <line x1="220" y1="70" x2="220" y2="100" stroke='#8b949e' stroke-width="1"/>
      <line x1="220" y1="100" x2="250" y2="100" stroke='#8b949e' stroke-width="1"/>

      <text x="150" y="170" font-size='16' font-weight='bold'>= \\(2\\frac{1}{3}\\)</text>

      <text x="50" y="220" font-size='16' font-weight='bold'>Count the thirds: 1, 2, 3, 4, 5, 6, 7 = \\(\\frac{7}{3}\\) = \\(2\\frac{1}{3}\\)</text>
    </svg>
  </div>

  <div class="success-box">
    <h4>Why This Matters:</h4>
    <p>Mixed numbers are easier to read and understand (\\(2\\frac{1}{3}\\) pizza). But improper fractions are easier for calculations. Many problems ask you to convert between them!</p>
  </div>
</div>"""
    },
    {
        "title": "Converting Improper Fractions to Mixed Numbers",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Division Unlocks the Conversion</h3>
    <p>To turn an improper fraction into a mixed number, divide the numerator by the denominator. The quotient becomes the whole number, and the remainder becomes the new numerator.</p>
  </div>

  <div class="steps-container">
    <h3>Method: Improper → Mixed</h3>
    <div class="step">
      <h4>Step 1: Divide numerator by denominator</h4>
      <p>For \\(\\frac{11}{4}\\): Divide \\(11 \\div 4 = 2\\) remainder \\(3\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Build the mixed number</h4>
      <p>Whole part = 2</p>
      <p>New numerator = remainder = 3</p>
      <p>Denominator stays = 4</p>
    </div>
    <div class="step">
      <h4>Step 3: Write as mixed number</h4>
      <p>Result: \\(2\\frac{3}{4}\\)</p>
    </div>
  </div>

  <div class="worked-example">
    <h4>More Examples:</h4>
    <p><strong>Example 1:</strong> Convert \\(\\frac{17}{5}\\)</p>
    <p>\\(17 \\div 5 = 3\\) remainder \\(2\\) → \\(3\\frac{2}{5}\\)</p>

    <p><strong>Example 2:</strong> Convert \\(\\frac{9}{2}\\)</p>
    <p>\\(9 \\div 2 = 4\\) remainder \\(1\\) → \\(4\\frac{1}{2}\\)</p>
  </div>

  <div class="formula-box">
    <h4>The Formula:</h4>
    <p>$$\\frac{numerator}{denominator} = whole\\frac{remainder}{denominator}$$</p>
    <p>Where: <strong>whole</strong> = \\(numerator \\div denominator\\)</p>
  </div>
</div>"""
    },
    {
        "title": "Converting Mixed Numbers to Improper Fractions",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Reverse the Process</h3>
    <p>To turn a mixed number into an improper fraction, multiply the whole number by the denominator, then add the numerator. Use the same denominator.</p>
  </div>

  <div class="steps-container">
    <h3>Method: Mixed → Improper</h3>
    <div class="step">
      <h4>Step 1: Multiply whole by denominator</h4>
      <p>For \\(3\\frac{2}{5}\\): \\(3 \\times 5 = 15\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Add the numerator</h4>
      <p>\\(15 + 2 = 17\\)</p>
    </div>
    <div class="step">
      <h4>Step 3: Use same denominator</h4>
      <p>Result: \\(\\frac{17}{5}\\)</p>
    </div>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg">
      <text x="50" y="30" font-size='16' font-weight='bold'>Converting \\(2\\frac{3}{4}\\) to improper:</text>

      <text x="50" y="70" font-size='14'>Step 1: \\(2 \\times 4 = 8\\)</text>
      <text x="50" y="100" font-size='14'>Step 2: \\(8 + 3 = 11\\)</text>
      <text x="50" y="130" font-size='14'>Step 3: \\(\\frac{11}{4}\\)</text>

      <text x="250" y="70" font-size='16' font-weight='bold'>Verify:</text>
      <text x="250" y="100" font-size='14'>\\(11 \\div 4 = 2\\) r \\(3\\)</text>
      <text x="250" y="130" font-size='14'>Check: \\(2\\frac{3}{4}\\) ✓</text>
    </svg>
  </div>

  <div class="worked-example">
    <h4>More Examples:</h4>
    <p><strong>Example 1:</strong> Convert \\(1\\frac{3}{7}\\)</p>
    <p>\\(1 \\times 7 = 7\\), then \\(7 + 3 = 10\\) → \\(\\frac{10}{7}\\)</p>

    <p><strong>Example 2:</strong> Convert \\(5\\frac{1}{3}\\)</p>
    <p>\\(5 \\times 3 = 15\\), then \\(15 + 1 = 16\\) → \\(\\frac{16}{3}\\)</p>
  </div>

  <div class="success-box">
    <h4>Why Convert?</h4>
    <p>Improper fractions are essential for multiplication and division. Always convert mixed numbers first, then solve!</p>
  </div>
</div>"""
    },
    {
        "title": "Why These Conversions Matter: Equivalent Fractions Foundation",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Mixed Numbers and Equivalent Fractions</h3>
    <p>Converting between mixed and improper fractions uses the same <strong>Golden Rule</strong>: multiply or divide both numerator and denominator by the same number without changing the value.</p>
    <p>When we write \\(2\\frac{1}{3} = \\frac{7}{3}\\), we're saying these are equivalent—they look different but mean the same thing!</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 500 300" xmlns="http://www.w3.org/2000/svg">
      <text x="50" y="30" font-size='16' font-weight='bold'>The Equivalence Circle:</text>

      <circle cx="150" cy="100" r="40" fill='#4169E1' opacity='0.3' stroke='#4169E1' stroke-width="2"/>
      <text x="150" y="105" font-size='14' text-anchor='middle' font-weight='bold'>\\(2\\frac{1}{3}\\)</text>

      <path d="M 190 100 L 260 100" stroke='#8b949e' stroke-width="2" marker-end="url(#arrowhead)"/>
      <text x="225" y="85" font-size='12' text-anchor='middle'>multiply</text>

      <circle cx="330" cy="100" r="40" fill='#22c55e' opacity='0.3' stroke='#22c55e' stroke-width="2"/>
      <text x="330" y="105" font-size='14' text-anchor='middle' font-weight='bold'>\\(\\frac{7}{3}\\)</text>

      <path d="M 260 130 L 190 130" stroke='#8b949e' stroke-width="2" marker-end="url(#arrowhead)"/>
      <text x="225" y="155" font-size='12' text-anchor='middle'>divide</text>

      <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
          <polygon points="0 0, 10 3, 0 6" fill='#e6edf3'/>
        </marker>
      </defs>

      <text x="50" y="200" font-size='14'><strong>Same value, different forms!</strong></text>
      <text x="50" y="225" font-size='13'>This is why we need both:</text>
      <text x="50" y="250" font-size='13'>• Mixed numbers: easy to read</text>
      <text x="50" y="275" font-size='13'>• Improper fractions: easy to compute</text>
    </svg>
  </div>

  <div class="warning-box">
    <h4>Key Insight:</h4>
    <p>Equivalent fractions mean the same amount, just written differently. When you multiply \\(2 \\times 3\\) and add 1, you're multiplying \\(\\frac{1}{3}\\) by \\(\\frac{3}{3}\\) (which equals 1), so the value stays the same!</p>
  </div>
</div>"""
    }
]
