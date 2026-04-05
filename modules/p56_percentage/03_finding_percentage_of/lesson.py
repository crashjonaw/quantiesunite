TITLE = "Finding a Percentage of a Quantity"

SECTIONS = [
    {
        "title": "Calculate a Percent of an Amount",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>The Formula</h3>
    <p>To find a percent of a number, convert the percent to a decimal and multiply.</p>
    <p>$$\\text{Percent of Amount} = \\frac{\\text{Percent}}{100} \\times \\text{Amount}$$</p>
    <p><strong>Example:</strong> 25% of 80 = 0.25 × 80 = 20</p>
  </div>

  <div class="steps-container">
    <h4>Three-Step Process</h4>
    <div class="step">
      <h5>Step 1: Convert percent to decimal</h5>
      <p>To convert: Divide percent by 100 (or move decimal left 2 places)</p>
      <p>Example: 30% = 30 ÷ 100 = 0.30</p>
    </div>
    <div class="step">
      <h5>Step 2: Multiply by the quantity</h5>
      <p>0.30 × 200 = 60</p>
    </div>
    <div class="step">
      <h5>Step 3: Write your answer</h5>
      <p>30% of 200 is 60</p>
    </div>
  </div>

  <div class="example-box">
    <h4>More Examples:</h4>
    <p>25% of 80 = 0.25 × 80 = 20</p>
    <p>15% of 200 = 0.15 × 200 = 30</p>
    <p>5% of 400 = 0.05 × 400 = 20</p>
    <p>120% of 50 = 1.20 × 50 = 60 (more than the original!)</p>
  </div>

  <div class="success-box">
    <h4>Key Insight:</h4>
    <p>Percentages greater than 100% give results larger than the original amount.</p>
  </div>
</div>"""
    },
    {
        "title": "Using Bar Models to Visualize",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Bar Models Show the Relationship</h3>
    <p>A bar model helps us see what percent of a quantity means.</p>
    <p>The whole bar represents 100%. Shaded parts show the percent we want.</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 500 280" xmlns="http://www.w3.org/2000/svg">
      <text x="50" y="30" font-size='14' font-weight='bold' fill='#e6edf3'>Find 40% of 150</text>

      <text x="50" y="70" font-size='12' fill='#e6edf3'>Whole amount: 150</text>

      <rect x="50" y="90" width="400" height="40" fill='none' stroke='#30363d' stroke-width="2"/>
      <rect x="50" y="90" width="160" height="40" fill='#4169E1' opacity='0.6'/>
      <text x="130" y="120" font-size='11' text-anchor='middle' fill='#e6edf3'>40% = 60</text>
      <text x="280" y="120" font-size='11' text-anchor='middle' fill='#e6edf3'>Remaining 60%</text>

      <text x="50" y="160" font-size='12' fill='#e6edf3'>Breakdown:</text>
      <text x="50" y="185" font-size='12' fill='#e6edf3'>The bar represents 150 total.</text>
      <text x="50" y="205" font-size='12' fill='#e6edf3'>100% of 150 = 150 (whole bar)</text>
      <text x="50" y="225" font-size='12' fill='#e6edf3'>40% of 150 = 0.40 × 150 = 60 (shaded part)</text>
      <text x="50" y="245" font-size='12' fill='#e6edf3'>60% of 150 = 0.60 × 150 = 90 (unshaded part)</text>

      <text x="250" y="270" font-size='11' text-anchor='middle' fill='#999'>40% + 60% = 100% ✓</text>
    </svg>
  </div>

  <div class="steps-container">
    <h4>Another Example: Find 25% of 200</h4>
    <div class="step">
      <p>Draw a bar for 200. Mark 4 equal sections (since 100% ÷ 4 = 25% each section).</p>
      <p>Each section = 200 ÷ 4 = 50</p>
      <p>One section (25%) = 50</p>
    </div>
  </div>
</div>"""
    },
    {
        "title": "Using Fractions Instead of Decimals",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Percent as a Fraction</h3>
    <p>Some people find it easier to work with fractions instead of decimals.</p>
    <p>Convert the percent to a fraction first, then multiply.</p>
  </div>

  <div class="steps-container">
    <h4>Method: Fraction × Quantity</h4>
    <div class="step">
      <h5>Example: Find 40% of 150</h5>
      <p>40% = \\(\\frac{40}{100} = \\frac{2}{5}\\)</p>
      <p>\\(\\frac{2}{5}\\) × 150 = \\(\\frac{2 \\times 150}{5}\\) = \\(\\frac{300}{5}\\) = 60</p>
    </div>
  </div>

  <div class="example-box">
    <h4>More Examples Using Fractions:</h4>
    <p>25% of 80 = \\(\\frac{1}{4}\\) × 80 = 20</p>
    <p>50% of 120 = \\(\\frac{1}{2}\\) × 120 = 60</p>
    <p>75% of 200 = \\(\\frac{3}{4}\\) × 200 = 150</p>
    <p>20% of 250 = \\(\\frac{1}{5}\\) × 250 = 50</p>
  </div>

  <div class="success-box">
    <h4>Tip:</h4>
    <p>Use fractions when the percent is a "nice" one like 25%, 50%, 75%, 20%. Use decimals for others like 37% or 63%.</p>
  </div>
</div>"""
    },
    {
        "title": "Real-World Applications",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Percents in Everyday Situations</h3>
    <p>Finding percentages of quantities happens constantly in real life:</p>
    <p>Discounts in shops, tips in restaurants, tax on purchases, interest on savings.</p>
  </div>

  <div class="example-box">
    <h4>Example 1: Shop Discount</h4>
    <p>A shirt costs £60. It is 30% off. How much do you save?</p>
    <p>Discount = 30% of £60 = 0.30 × £60 = £18</p>
    <p>Sale price = £60 - £18 = £42</p>
  </div>

  <div class="example-box">
    <h4>Example 2: Restaurant Tip</h4>
    <p>A meal costs £45. You want to tip 20%. How much is the tip?</p>
    <p>Tip = 20% of £45 = 0.20 × £45 = £9</p>
    <p>Total to pay = £45 + £9 = £54</p>
  </div>

  <div class="example-box">
    <h4>Example 3: Exam Preparation</h4>
    <p>There are 120 questions in a practice test. You need to answer 75% correctly to pass.</p>
    <p>Questions needed = 75% of 120 = 0.75 × 120 = 90 questions</p>
  </div>

  <div class="warning-box">
    <h4>Watch Out!</h4>
    <p>When there's a discount, find the discount amount first, then subtract from the original price.</p>
    <p>When there's a tax or tip, find the amount to add first, then add to the original price.</p>
  </div>
</div>"""
    }
]
