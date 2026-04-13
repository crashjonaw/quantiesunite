TITLE = "Percentage Increase and Decrease"

SECTIONS = [
    {
        "title": "Understanding Percent Change",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Changes as Percentages</h3>
    <p>In real life, prices change, populations grow, and scores improve or worsen.</p>
    <p>We describe these changes using percentages.</p>
    <p><strong>Increase</strong> means something gets bigger. <strong>Decrease</strong> means something gets smaller.</p>
  </div>

  <div class="example-box">
    <h4>Real-World Examples:</h4>
    <p><strong>Increase:</strong> A salary increases by 5%. House prices increase by 8% per year.</p>
    <p><strong>Decrease:</strong> A price is reduced by 20% (sale). Population decreases by 3%.</p>
  </div>

  <div class="success-box">
    <h4>Key Insight:</h4>
    <p>The percent change is always based on the <strong>original</strong> amount, not the new amount.</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 500 150" xmlns="http://www.w3.org/2000/svg">
      <text x="50" y="30" font-size='13' font-weight='bold' fill='currentColor'>Original Amount</text>
      <rect x="50" y="45" width="150" height="40" fill='#4169E1' opacity='0.5' stroke='#30363d' stroke-width="2" rx="4"/>
      <text x="125" y="72" font-size='12' text-anchor='middle' fill='currentColor'>100%</text>

      <text x="50" y="110" font-size='12' fill='currentColor'>Increase by 20%</text>
      <text x="250" y="110" font-size='12' fill='currentColor'>New = 100% + 20% = 120%</text>

      <text x="50" y="135" font-size='12' fill='currentColor'>Decrease by 20%</text>
      <text x="250" y="135" font-size='12' fill='currentColor'>New = 100% - 20% = 80%</text>
    </svg>
  </div>
</div>"""
    },
    {
        "title": "Percent Increase",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Method: Percent Increase</h3>
    <p><strong>Two ways to calculate:</strong></p>
    <p>Method 1: Find the increase, then add to original.</p>
    <p>Method 2: Calculate the new amount directly.</p>
  </div>

  <div class="steps-container">
    <h4>Method 1: Calculate Increase Then Add</h4>
    <div class="step">
      <h5>Problem: A shirt costs £20 and increases by 15%. What is the new price?</h5>
      <p><strong>Step 1:</strong> Calculate the increase amount</p>
      <p>Increase = \(15\%\) of £20 = \(0.15 \\times £20 = £3\)</p>
      <p><strong>Step 2:</strong> Add to original</p>
      <p>New price = \(£20 + £3 = £23\)</p>
    </div>
  </div>

  <div class="steps-container">
    <h4>Method 2: Calculate New Amount Directly</h4>
    <div class="step">
      <h5>Same Problem: A shirt costs £20 and increases by 15%</h5>
      <p>New price = \(100\% + 15\% = 115\%\) of original</p>
      <p>\(115\%\) of £20 = \(1.15 \\times £20 = £23\)</p>
    </div>
  </div>

  <div class="formula-box">
    <h4>Formula for Percent Increase:</h4>
    <p>$$\\text{New Value} = \\text{Original} \\times \\left(1 + \\frac{\\text{Percent}}{100}\\right)$$</p>
    <p>Or: New Value = Original \(\\times 1.15\) for 15% increase</p>
  </div>

  <div class="example-box">
    <h4>More Examples:</h4>
    <p>A £50 amount increased by 20%: \(£50 \\times 1.20 = £60\)</p>
    <p>A score of 80 increased by 25%: \(80 \\times 1.25 = 100\)</p>
    <p>A population of 1000 increased by 5%: \(1000 \\times 1.05 = 1050\)</p>
  </div>

  <div class="success-box">
    <h4>Shortcut for Method 2:</h4>
    <p>Add the percent to 100%, convert to decimal, and multiply.</p>
    <p>\(15\%\) increase → \((100 + 15)\% = 115\% = 1.15 \\times\) original</p>
  </div>
</div>"""
    },
    {
        "title": "Percent Decrease",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Method: Percent Decrease</h3>
    <p><strong>Two ways to calculate:</strong> Same as increase, but we subtract instead.</p>
  </div>

  <div class="steps-container">
    <h4>Method 1: Calculate Decrease Then Subtract</h4>
    <div class="step">
      <h5>Problem: A TV costs £400 and is reduced by 20%. What is the sale price?</h5>
      <p><strong>Step 1:</strong> Calculate the decrease amount</p>
      <p>Decrease = \(20\%\) of £400 = \(0.20 \\times £400 = £80\)</p>
      <p><strong>Step 2:</strong> Subtract from original</p>
      <p>Sale price = \(£400 - £80 = £320\)</p>
    </div>
  </div>

  <div class="steps-container">
    <h4>Method 2: Calculate New Amount Directly</h4>
    <div class="step">
      <h5>Same Problem: A TV costs £400 and is reduced by 20%</h5>
      <p>Sale price = \(100\% - 20\% = 80\%\) of original</p>
      <p>\(80\%\) of £400 = \(0.80 \\times £400 = £320\)</p>
    </div>
  </div>

  <div class="formula-box">
    <h4>Formula for Percent Decrease:</h4>
    <p>$$\\text{New Value} = \\text{Original} \\times \\left(1 - \\frac{\\text{Percent}}{100}\\right)$$</p>
    <p>Or: New Value = Original \(\\times 0.80\) for 20% decrease</p>
  </div>

  <div class="example-box">
    <h4>More Examples:</h4>
    <p>A £50 amount decreased by 10%: \(£50 \\times 0.90 = £45\)</p>
    <p>A 200-page book, 25% reduced: \(200 \\times 0.75 = 150\) pages</p>
    <p>A price of £80, 15% off: \(£80 \\times 0.85 = £68\)</p>
  </div>

  <div class="warning-box">
    <h4>Common Mistake:</h4>
    <p>Don't just add or subtract the percent! You must multiply the original by (1 ± percent/100).</p>
  </div>
</div>"""
    },
    {
        "title": "Comparing Increase and Decrease",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Increase and Decrease Are NOT Symmetric</h3>
    <p>A 20% increase followed by a 20% decrease does NOT return you to the original amount!</p>
  </div>

  <div class="steps-container">
    <h4>Example: Why They're Different</h4>
    <div class="step">
      <h5>Start with £100</h5>
      <p><strong>Step 1:</strong> Increase by 20%: \(£100 \\times 1.20 = £120\)</p>
      <p><strong>Step 2:</strong> Decrease the new amount by 20%: \(£120 \\times 0.80 = £96\)</p>
      <p><strong>Result:</strong> We're back to £96, not £100!</p>
    </div>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 560 200" xmlns="http://www.w3.org/2000/svg">
      <text x="50" y="30" font-size='13' font-weight='bold' fill='currentColor'>Start: £100</text>
      <rect x="50" y="45" width="100" height="35" fill='#4169E1' opacity='0.5' stroke='#30363d' stroke-width="2" rx="4"/>
      <text x="100" y="68" font-size='11' text-anchor='middle' fill='currentColor'>£100</text>

      <text x="170" y="68" font-size='12' fill='currentColor'>+20%</text>

      <text x="210" y="30" font-size='13' font-weight='bold' fill='currentColor'>Now: £120</text>
      <rect x="210" y="45" width="120" height="35" fill='#22c55e' opacity='0.5' stroke='#30363d' stroke-width="2" rx="4"/>
      <text x="270" y="68" font-size='11' text-anchor='middle' fill='currentColor'>£120</text>

      <text x="340" y="68" font-size='12' fill='currentColor'>-20%</text>

      <text x="380" y="30" font-size='13' font-weight='bold' fill='currentColor'>Final: £96</text>
      <rect x="380" y="45" width="96" height="35" fill='#f59e0b' opacity='0.5' stroke='#30363d' stroke-width="2" rx="4"/>
      <text x="428" y="68" font-size='11' text-anchor='middle' fill='currentColor'>£96</text>

      <text x="250" y="130" font-size='12' fill='currentColor'>Why? The 20% decrease is applied to £120, not £100!</text>
      <text x="250" y="150" font-size='12' fill='currentColor'>20% of £120 = £24, so £120 - £24 = £96</text>
      <text x="250" y="170" font-size='12' fill='currentColor'>But 20% of £100 = £20, and £100 - £20 = £80</text>
    </svg>
  </div>

  <div class="success-box">
    <h4>Key Rule:</h4>
    <p>Each percentage change is applied to the <strong>current amount</strong>, not the original amount!</p>
  </div>
</div>"""
    }
]
