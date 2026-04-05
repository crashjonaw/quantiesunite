TITLE = "Fractions, Decimals, and Percentages"

SECTIONS = [
    {
        "title": "Three Representations of the Same Thing",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Different Languages, Same Message</h3>
    <p>A fraction, decimal, and percentage are three different ways to express <strong>the same part of a whole</strong>. Think of them as three languages for numbers:</p>
    <ul>
      <li><strong>Fraction:</strong> Uses a numerator and denominator (\\(\\frac{1}{4}\\))</li>
      <li><strong>Decimal:</strong> Uses place value (0.25)</li>
      <li><strong>Percentage:</strong> Means "out of 100" (25%)</li>
    </ul>
    <p>All three say the same thing: <strong>one quarter</strong> of something.</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 510 300" xmlns="http://www.w3.org/2000/svg">
      <text x="50" y="30" font-size='16' font-weight='bold'>Equivalent Representations:</text>

      <circle cx="100" cy="100" r="50" fill='none' stroke='#8b949e' stroke-width="2"/>
      <path d="M 100 50 A 50 50 0 0 1 150 100" fill='#4169E1' opacity='0.6'/>
      <line x1="100" y1="50" x2="100" y2="100" stroke='#8b949e' stroke-width="1"/>
      <line x1="100" y1="100" x2="150" y2="100" stroke='#8b949e' stroke-width="1"/>
      <text x="100" y="180" font-size='16' text-anchor='middle' font-weight='bold'>\\(\\frac{1}{4}\\)</text>

      <text x="250" y="110" font-size='20' text-anchor='middle' font-weight='bold'>=</text>

      <rect x="280" y="50" width="100" height="100" fill='#4169E1' opacity='0.2' stroke='#8b949e' stroke-width="2"/>
      <line x1="310" y1="50" x2="310" y2="150" stroke='#30363d' stroke-width="1"/>
      <line x1="340" y1="50" x2="340" y2="150" stroke='#30363d' stroke-width="1"/>
      <line x1="370" y1="50" x2="370" y2="150" stroke='#30363d' stroke-width="1"/>
      <rect x="280" y="50" width="25" height="100" fill='#4169E1' opacity='0.6'/>
      <text x="330" y="180" font-size='16' text-anchor='middle' font-weight='bold'>0.25</text>

      <text x="410" y="110" font-size='20' text-anchor='middle' font-weight='bold'>=</text>

      <rect x="440" y="50" width="50" height="100" fill='#22c55e' opacity='0.4' stroke='#8b949e' stroke-width="2"/>
      <text x="490" y="70" font-size='14' text-anchor='middle'>25%</text>
      <line x1="465" y1="85" x2="465" y2="95" stroke='#8b949e' stroke-width="1"/>
      <text x="465" y="110" font-size='12' text-anchor='middle'>25</text>
      <text x="465" y="130" font-size='12' text-anchor='middle'>out of</text>
      <text x="465" y="150" font-size='12' text-anchor='middle'>100</text>
    </svg>
  </div>

  <div class="success-box">
    <h4>The Big Picture:</h4>
    <p>Fractions show parts using any denominator. Decimals use base 10. Percentages always use 100 as the "whole." They're all measuring the same thing!</p>
  </div>
</div>"""
    },
    {
        "title": "Converting Fractions to Decimals",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Division to the Rescue</h3>
    <p>A fraction is a division problem in disguise! \\(\\frac{3}{4}\\) means \\(3 \\div 4\\). To convert a fraction to a decimal, divide the numerator by the denominator.</p>
  </div>

  <div class="steps-container">
    <h3>Method: Fraction to Decimal</h3>
    <div class="step">
      <h4>Step 1: Set up the division</h4>
      <p>\\(\\frac{3}{4}\\) becomes \\(3 \\div 4\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Divide using long division</h4>
      <p>\\(3 \\div 4 = 0\\) remainder \\(3\\)</p>
      <p>Annex a 0: \\(30 \\div 4 = 7\\) remainder \\(2\\)</p>
      <p>Annex a 0: \\(20 \\div 4 = 5\\) remainder \\(0\\)</p>
    </div>
    <div class="step">
      <h4>Step 3: Write the decimal</h4>
      <p>\\(\\frac{3}{4} = 0.75\\)</p>
    </div>
  </div>

  <div class="worked-example">
    <h4>More Examples:</h4>
    <p><strong>Example 1:</strong> \\(\\frac{1}{4}\\)</p>
    <p>\\(1 \\div 4 = 0.25\\)</p>

    <p><strong>Example 2:</strong> \\(\\frac{5}{8}\\)</p>
    <p>\\(5 \\div 8 = 0.625\\)</p>

    <p><strong>Example 3 (Repeating):</strong> \\(\\frac{1}{3}\\)</p>
    <p>\\(1 \\div 3 = 0.333... = 0.\\overline{3}\\) (the 3 repeats forever)</p>
  </div>

  <div class="formula-box">
    <h4>Common Fraction-to-Decimal Conversions:</h4>
    <p>\\(\\frac{1}{2} = 0.5\\) &nbsp;&nbsp;&nbsp;&nbsp; \\(\\frac{1}{4} = 0.25\\) &nbsp;&nbsp;&nbsp;&nbsp; \\(\\frac{3}{4} = 0.75\\)</p>
    <p>\\(\\frac{1}{5} = 0.2\\) &nbsp;&nbsp;&nbsp;&nbsp; \\(\\frac{1}{10} = 0.1\\) &nbsp;&nbsp;&nbsp;&nbsp; \\(\\frac{1}{100} = 0.01\\)</p>
  </div>
</div>"""
    },
    {
        "title": "Converting Decimals to Fractions",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Place Value Guides the Way</h3>
    <p>Every decimal can be read as a fraction! The denominator depends on how many decimal places there are.</p>
    <ul>
      <li>1 decimal place → denominator 10</li>
      <li>2 decimal places → denominator 100</li>
      <li>3 decimal places → denominator 1000</li>
    </ul>
  </div>

  <div class="steps-container">
    <h3>Method: Decimal to Fraction</h3>
    <div class="step">
      <h4>Step 1: Write the decimal as a fraction (with appropriate denominator)</h4>
      <p>\\(0.75 = \\frac{75}{100}\\) (two decimal places → denominator 100)</p>
    </div>
    <div class="step">
      <h4>Step 2: Simplify to lowest terms</h4>
      <p>GCF of 75 and 100 is 25</p>
      <p>\\(\\frac{75}{100} = \\frac{75 \\div 25}{100 \\div 25} = \\frac{3}{4}\\)</p>
    </div>
  </div>

  <div class="worked-example">
    <h4>More Examples:</h4>
    <p><strong>Example 1:</strong> 0.6</p>
    <p>\\(0.6 = \\frac{6}{10} = \\frac{3}{5}\\) (simplified)</p>

    <p><strong>Example 2:</strong> 0.125</p>
    <p>\\(0.125 = \\frac{125}{1000} = \\frac{1}{8}\\) (simplified)</p>

    <p><strong>Example 3:</strong> 0.45</p>
    <p>\\(0.45 = \\frac{45}{100} = \\frac{9}{20}\\) (simplified)</p>
  </div>

  <div class="success-box">
    <h4>Remember:</h4>
    <p>Always simplify the fraction after converting from decimal!</p>
  </div>
</div>"""
    },
    {
        "title": "Converting Percentages to Fractions and Decimals",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Percent Means "Out of 100"</h3>
    <p>The word "percent" comes from Latin: "per" (for each) + "cent" (100). So 25% literally means 25 out of 100, or \\(\\frac{25}{100}\\).</p>
    <p><strong>The Percentage Formula:</strong></p>
    <p>$$\\text{Percentage} = \\text{Fraction} \\times 100$$</p>
  </div>

  <div class="steps-container">
    <h3>Method: Percentage to Fraction</h3>
    <div class="step">
      <h4>Step 1: Write as a fraction over 100</h4>
      <p>\\(35% = \\frac{35}{100}\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Simplify</h4>
      <p>GCF of 35 and 100 is 5</p>
      <p>\\(\\frac{35}{100} = \\frac{7}{20}\\)</p>
    </div>
  </div>

  <div class="steps-container">
    <h3>Method: Percentage to Decimal</h3>
    <div class="step">
      <h4>Step 1: Divide the percentage by 100</h4>
      <p>\\(45% = 45 \\div 100 = 0.45\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Move the decimal point</h4>
      <p>Or simply move the decimal point <strong>2 places to the left</strong></p>
      <p>\\(45\\% \\rightarrow 0.45\\)</p>
    </div>
  </div>

  <div class="worked-example">
    <h4>Examples:</h4>
    <p><strong>Example 1:</strong> Convert 60% to a fraction and decimal</p>
    <p>Fraction: \\(60% = \\frac{60}{100} = \\frac{3}{5}\\)</p>
    <p>Decimal: \\(60% = 0.60\\)</p>

    <p><strong>Example 2:</strong> Convert 12.5% to fraction and decimal</p>
    <p>Decimal: \\(12.5% = 0.125\\)</p>
    <p>Fraction: \\(0.125 = \\frac{125}{1000} = \\frac{1}{8}\\)</p>
  </div>

  <div class="steps-container">
    <h3>Method: Fraction to Percentage</h3>
    <div class="step">
      <h4>Step 1: Convert fraction to decimal</h4>
      <p>\\(\\frac{3}{5} = 0.6\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Multiply by 100 or move decimal right 2 places</h4>
      <p>\\(0.6 \\times 100 = 60\\%\\)</p>
    </div>
  </div>

  <div class="success-box">
    <h4>Quick Conversion Chart:</h4>
    <p>\\(\\frac{1}{2} = 0.5 = 50\\%\\) &nbsp;&nbsp;&nbsp;&nbsp; \\(\\frac{1}{4} = 0.25 = 25\\%\\) &nbsp;&nbsp;&nbsp;&nbsp; \\(\\frac{3}{4} = 0.75 = 75\\%\\)</p>
    <p>\\(\\frac{1}{5} = 0.2 = 20\\%\\) &nbsp;&nbsp;&nbsp;&nbsp; \\(\\frac{1}{10} = 0.1 = 10\\%\\)</p>
  </div>
</div>"""
    }
]
