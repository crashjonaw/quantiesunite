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

  <p style="text-align:center; font-weight:bold; margin:10px 0;">\\(\\frac{7}{3}\\) shown as wholes and parts:</p>
  <div class="diagram-container">
    <svg viewBox="0 0 460 160" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:460px; display:block; margin:0 auto;">
      <!-- First whole: 3/3 -->
      <circle cx="70" cy="65" r="45" fill='none' stroke='#8b949e' stroke-width="2"/>
      <path d="M 70 20 A 45 45 0 1 1 69.99 20 Z" fill='#4169E1' opacity='0.5'/>
      <text x="70" y="72" font-size='18' text-anchor='middle' fill='currentColor' font-weight='bold'>3/3</text>

      <!-- Plus sign -->
      <text x="140" y="72" font-size='22' text-anchor='middle' fill='currentColor' font-weight='bold'>+</text>

      <!-- Second whole: 3/3 -->
      <circle cx="210" cy="65" r="45" fill='none' stroke='#8b949e' stroke-width="2"/>
      <path d="M 210 20 A 45 45 0 1 1 209.99 20 Z" fill='#4169E1' opacity='0.5'/>
      <text x="210" y="72" font-size='18' text-anchor='middle' fill='currentColor' font-weight='bold'>3/3</text>

      <!-- Plus sign -->
      <text x="280" y="72" font-size='22' text-anchor='middle' fill='currentColor' font-weight='bold'>+</text>

      <!-- Third partial: 1/3 (120 degree arc) -->
      <circle cx="350" cy="65" r="45" fill='none' stroke='#8b949e' stroke-width="2"/>
      <!-- 1/3 arc: from top (0,-45) sweeping 120 degrees -->
      <path d="M 350 20 A 45 45 0 0 1 389 87.5 L 350 65 Z" fill='#22c55e' opacity='0.5'/>
      <text x="350" y="72" font-size='18' text-anchor='middle' fill='currentColor' font-weight='bold'>1/3</text>

      <!-- Bottom labels -->
      <text x="230" y="140" font-size='16' text-anchor='middle' fill='currentColor' font-weight='bold'>= 7 thirds = 7/3 = 2 and 1/3</text>
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
    <p>$$\\frac{\\text{numerator}}{\\text{denominator}} = \\text{whole}\\frac{\\text{remainder}}{\\text{denominator}}$$</p>
    <p>Where: <strong>whole</strong> = \\(\\text{numerator} \\div \\text{denominator}\\)</p>
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

  <div class="worked-example">
    <h4>Worked Example: Converting \\(2\\frac{3}{4}\\) to improper</h4>
    <p>Step 1: \\(2 \\times 4 = 8\\)</p>
    <p>Step 2: \\(8 + 3 = 11\\)</p>
    <p>Step 3: \\(\\frac{11}{4}\\)</p>
    <p>Verify: \\(11 \\div 4 = 2\\) remainder \\(3\\) → \\(2\\frac{3}{4}\\) ✓</p>
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
    <svg viewBox="0 0 460 150" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:460px; display:block; margin:0 auto;">
      <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
          <polygon points="0 0, 10 3, 0 6" fill='currentColor'/>
        </marker>
      </defs>

      <!-- Mixed number bubble -->
      <circle cx="120" cy="60" r="50" fill='#4169E1' opacity='0.2' stroke='#4169E1' stroke-width="2"/>
      <text x="120" y="55" font-size='14' text-anchor='middle' fill='currentColor'>Mixed</text>
      <text x="120" y="75" font-size='16' text-anchor='middle' fill='currentColor' font-weight='bold'>2 1/3</text>

      <!-- Arrows -->
      <path d="M 175 45 L 255 45" stroke='currentColor' opacity='0.5' stroke-width="2" marker-end="url(#arrowhead)"/>
      <text x="215" y="38" font-size='11' text-anchor='middle' fill='currentColor'>multiply</text>

      <path d="M 255 80 L 175 80" stroke='currentColor' opacity='0.5' stroke-width="2" marker-end="url(#arrowhead)"/>
      <text x="215" y="98" font-size='11' text-anchor='middle' fill='currentColor'>divide</text>

      <!-- Improper fraction bubble -->
      <circle cx="340" cy="60" r="50" fill='#22c55e' opacity='0.2' stroke='#22c55e' stroke-width="2"/>
      <text x="340" y="55" font-size='14' text-anchor='middle' fill='currentColor'>Improper</text>
      <text x="340" y="75" font-size='16' text-anchor='middle' fill='currentColor' font-weight='bold'>7/3</text>

      <!-- Bottom text -->
      <text x="230" y="135" font-size='13' text-anchor='middle' fill='currentColor' font-weight='bold'>Same value, different forms!</text>
    </svg>
  </div>

  <p><strong>This is why we need both:</strong></p>
  <ul>
    <li><strong>Mixed numbers:</strong> easy to read and understand</li>
    <li><strong>Improper fractions:</strong> easy to compute with</li>
  </ul>

  <div class="warning-box">
    <h4>Key Insight:</h4>
    <p>Equivalent fractions mean the same amount, just written differently. When you multiply \\(2 \\times 3\\) and add 1, you're multiplying \\(\\frac{1}{3}\\) by \\(\\frac{3}{3}\\) (which equals 1), so the value stays the same!</p>
  </div>
</div>"""
    }
]
