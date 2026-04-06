TITLE = "Converting Between Percent, Fraction, and Decimal"

SECTIONS = [
    {
        "title": "Percent to Decimal",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Percent to Decimal: Divide by 100</h3>
    <p>To convert a percent to a decimal, divide by 100.</p>
    <p>This is the same as moving the decimal point 2 places to the left.</p>
  </div>

  <div class="steps-container">
    <h4>Method: Divide by 100</h4>
    <div class="step">
      <p><strong>Example 1:</strong> Convert 45% to a decimal</p>
      <p>\(45\% = 45 \div 100 = 0.45\)</p>
    </div>
    <div class="step">
      <p><strong>Example 2:</strong> Convert 8% to a decimal</p>
      <p>\(8\% = 8 \div 100 = 0.08\)</p>
    </div>
    <div class="step">
      <p><strong>Example 3:</strong> Convert 120% to a decimal</p>
      <p>\(120\% = 120 \div 100 = 1.20\)</p>
    </div>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 500 180" xmlns="http://www.w3.org/2000/svg">
      <text x="250" y="30" font-size='16' font-weight='bold' text-anchor='middle' fill='currentColor'>Move Decimal 2 Places Left</text>

      <text x="50" y="70" font-size='13' fill='currentColor'>65%</text>
      <text x="150" y="70" font-size='13' fill='currentColor'>(= 65.)</text>
      <text x="250" y="70" font-size='13' fill='currentColor'>→</text>
      <text x="320" y="70" font-size='13' fill='currentColor'>0.65</text>

      <text x="50" y="110" font-size='13' fill='currentColor'>8%</text>
      <text x="150" y="110" font-size='13' fill='currentColor'>(= 8.)</text>
      <text x="250" y="110" font-size='13' fill='currentColor'>→</text>
      <text x="320" y="110" font-size='13' fill='currentColor'>0.08</text>

      <text x="50" y="150" font-size='13' fill='currentColor'>150%</text>
      <text x="150" y="150" font-size='13' fill='currentColor'>(= 150.)</text>
      <text x="250" y="150" font-size='13' fill='currentColor'>→</text>
      <text x="320" y="150" font-size='13' fill='currentColor'>1.50</text>

      <text x="250" y="175" font-size='11' text-anchor='middle' fill='#999'>Notice: % > 100 gives decimal > 1</text>
    </svg>
  </div>

  <div class="success-box">
    <h4>Quick Tip:</h4>
    <p>Just move the decimal point 2 places left and drop the % sign. That's it!</p>
  </div>
</div>"""
    },
    {
        "title": "Decimal to Percent",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Decimal to Percent: Multiply by 100</h3>
    <p>To convert a decimal to a percent, multiply by 100.</p>
    <p>This is the same as moving the decimal point 2 places to the right.</p>
  </div>

  <div class="steps-container">
    <h4>Method: Multiply by 100</h4>
    <div class="step">
      <p><strong>Example 1:</strong> Convert 0.35 to a percent</p>
      <p>\(0.35 \times 100 = 35\%\)</p>
    </div>
    <div class="step">
      <p><strong>Example 2:</strong> Convert 0.6 to a percent</p>
      <p>\(0.6 \times 100 = 60\%\)</p>
    </div>
    <div class="step">
      <p><strong>Example 3:</strong> Convert 1.25 to a percent</p>
      <p>\(1.25 \times 100 = 125\%\)</p>
    </div>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 500 180" xmlns="http://www.w3.org/2000/svg">
      <text x="250" y="30" font-size='16' font-weight='bold' text-anchor='middle' fill='currentColor'>Move Decimal 2 Places Right</text>

      <text x="50" y="70" font-size='13' fill='currentColor'>0.42</text>
      <text x="200" y="70" font-size='13' fill='currentColor'>→</text>
      <text x="290" y="70" font-size='13' fill='currentColor'>42%</text>

      <text x="50" y="110" font-size='13' fill='currentColor'>0.08</text>
      <text x="200" y="110" font-size='13' fill='currentColor'>→</text>
      <text x="290" y="110" font-size='13' fill='currentColor'>8%</text>

      <text x="50" y="150" font-size='13' fill='currentColor'>2.5</text>
      <text x="200" y="150" font-size='13' fill='currentColor'>→</text>
      <text x="290" y="150" font-size='13' fill='currentColor'>250%</text>

      <text x="250" y="175" font-size='11' text-anchor='middle' fill='#999'>Notice: decimal > 1 gives % > 100</text>
    </svg>
  </div>

  <div class="success-box">
    <h4>Quick Tip:</h4>
    <p>Move decimal 2 places right and add the % sign.</p>
  </div>
</div>"""
    },
    {
        "title": "Fraction to Percent",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Fraction to Percent: Two Methods</h3>
    <p><strong>Method 1:</strong> Make the denominator 100</p>
    <p><strong>Method 2:</strong> Convert to decimal, then to percent</p>
  </div>

  <div class="steps-container">
    <h4>Method 1: Make Denominator 100</h4>
    <div class="step">
      <p><strong>Example:</strong> Convert \\(\\frac{3}{5}\\) to a percent</p>
      <p>Find what to multiply 5 by to get 100: \(5 \times 20 = 100\)</p>
      <p>Multiply numerator by the same number: \(3 \times 20 = 60\)</p>
      <p>\(\frac{3}{5} = \frac{60}{100} = 60\%\)</p>
    </div>
  </div>

  <div class="steps-container">
    <h4>Method 2: Divide Then Multiply</h4>
    <div class="step">
      <p><strong>Example:</strong> Convert \\(\\frac{3}{8}\\) to a percent</p>
      <p>Divide: \(3 \div 8 = 0.375\)</p>
      <p>Multiply by 100: \(0.375 \times 100 = 37.5\%\)</p>
    </div>
  </div>

  <div class="formula-box">
    <h4>Formula:</h4>
    <p>Percent = Fraction \(\div 1 \times 100\)</p>
    <p>Or: Fraction → Decimal → Multiply by 100</p>
  </div>

  <div class="example-box">
    <h4>More Examples:</h4>
    <p>\(\frac{1}{4} = 0.25 = 25\%\)</p>
    <p>\(\frac{2}{5} = 0.4 = 40\%\)</p>
    <p>\(\frac{7}{10} = 0.7 = 70\%\)</p>
  </div>
</div>"""
    },
    {
        "title": "Percent to Fraction",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Percent to Fraction: Simplify</h3>
    <p>To convert a percent to a fraction, write it as a fraction with 100 as the denominator, then simplify.</p>
  </div>

  <div class="steps-container">
    <h4>Method: Write as /100 Then Simplify</h4>
    <div class="step">
      <p><strong>Example 1:</strong> Convert 35% to a fraction</p>
      <p>35% = \\(\\frac{35}{100}\\)</p>
      <p>Find GCF of 35 and 100: GCF = 5</p>
      <p>\\(\\frac{35}{100} = \\frac{7}{20}\\)</p>
    </div>
    <div class="step">
      <p><strong>Example 2:</strong> Convert 80% to a fraction</p>
      <p>80% = \\(\\frac{80}{100}\\)</p>
      <p>GCF of 80 and 100 is 20</p>
      <p>\\(\\frac{80}{100} = \\frac{4}{5}\\)</p>
    </div>
  </div>

  <div class="steps-container">
    <h4>Recognition Shortcut:</h4>
    <div class="step">
      <p>25% = \\(\\frac{1}{4}\\) &nbsp;&nbsp;&nbsp;&nbsp; 50% = \\(\\frac{1}{2}\\) &nbsp;&nbsp;&nbsp;&nbsp; 75% = \\(\\frac{3}{4}\\)</p>
      <p>20% = \\(\\frac{1}{5}\\) &nbsp;&nbsp;&nbsp;&nbsp; 40% = \\(\\frac{2}{5}\\) &nbsp;&nbsp;&nbsp;&nbsp; 60% = \\(\\frac{3}{5}\\)</p>
      <p>10% = \\(\\frac{1}{10}\\) &nbsp;&nbsp;&nbsp;&nbsp; 30% = \\(\\frac{3}{10}\\)</p>
    </div>
  </div>

  <div class="success-box">
    <h4>Tip:</h4>
    <p>Always simplify fractions to their lowest terms. Check if the GCF of numerator and denominator divides both evenly.</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg">
      <text x="250" y="30" font-size='16' font-weight='bold' text-anchor='middle' fill='currentColor'>Conversion Steps</text>

      <rect x="50" y="60" width="100" height="50" fill='#4169E1' opacity='0.3' stroke='#30363d' stroke-width="2" rx="5"/>
      <text x="100" y="92" font-size='14' font-weight='bold' text-anchor='middle' fill='currentColor'>48%</text>

      <text x="160" y="92" font-size='16' fill='currentColor'>→</text>

      <rect x="190" y="60" width="120" height="50" fill='#22c55e' opacity='0.3' stroke='#30363d' stroke-width="2" rx="5"/>
      <text x="250" y="92" font-size='13' text-anchor='middle' fill='currentColor'>48/100</text>

      <text x="320" y="92" font-size='16' fill='currentColor'>→</text>

      <rect x="350" y="60" width="100" height="50" fill='#f59e0b' opacity='0.3' stroke='#30363d' stroke-width="2" rx="5"/>
      <text x="400" y="92" font-size='13' text-anchor='middle' fill='currentColor'>12/25</text>

      <text x="250" y="150" font-size='11' text-anchor='middle' fill='currentColor'>Divide both by GCF of 4</text>
    </svg>
  </div>
</div>"""
    }
]
