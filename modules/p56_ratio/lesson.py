SECTIONS = [
    {
        "id": "1_ratio_meaning",
        "title": "What is a Ratio? Understanding Comparisons",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>Ratio: Comparing Two Quantities</h3>
    <p>A <strong>ratio</strong> compares two amounts. It shows the relationship between them.</p>
    <p>If we have 3 red balls and 2 blue balls, the ratio of red to blue is <strong>3 : 2</strong> (read as "3 to 2").</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg">
      <text x="50" y="30" font-size="18" font-weight="bold" fill="currentColor">3 red balls : 2 blue balls</text>

      <circle cx="100" cy="80" r="25" fill="#ef4444"/>
      <circle cx="150" cy="80" r="25" fill="#ef4444"/>
      <circle cx="200" cy="80" r="25" fill="#ef4444"/>
      <circle cx="280" cy="80" r="25" fill="#4169E1"/>
      <circle cx="330" cy="80" r="25" fill="#4169E1"/>

      <text x="150" y="150" font-size="20" font-weight="bold" text-anchor="middle" fill="currentColor">Ratio = 3 : 2</text>
      <text x="150" y="180" font-size="14" text-anchor="middle" fill="currentColor">For every 3 red, there are 2 blue</text>
    </svg>
  </div>

  <div class="formula-box">
    <h4>Three Ways to Write a Ratio:</h4>
    <p>The same information can be written three ways:</p>
    <ul>
      <li><strong>3 : 2</strong> (colon notation)</li>
      <li><strong>3 to 2</strong> (words)</li>
      <li><strong>\\\\( \\\\frac{3}{2} \\\\)</strong> (fraction)</li>
    </ul>
    <p>All mean: for every 3 units of the first quantity, there are 2 units of the second.</p>
  </div>

  <div class="example-box">
    <h4>Real-World Examples:</h4>
    <ul>
      <li>Recipe: flour to sugar is 2:1 (2 cups flour for 1 cup sugar)</li>
      <li>Map: 1:100,000 means 1 unit on map = 100,000 units in real life</li>
      <li>Paint mixture: red paint to white paint is 3:5</li>
    </ul>
  </div>

  <div class="warning-box">
    <h4>Important: Order Matters!</h4>
    <p>The ratio 3:2 is different from 2:3.</p>
    <p>3:2 means "3 of the first for every 2 of the second"</p>
    <p>2:3 means "2 of the first for every 3 of the second"</p>
    <p>Always read the problem carefully to get the order right!</p>
  </div>
</div>'''
    },
    {
        "id": "2_equivalent_ratios",
        "title": "Equivalent Ratios and Scaling",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>Equivalent Ratios Are Equal Relationships</h3>
    <p>Just like equivalent fractions, two ratios are equivalent if they represent the same relationship.</p>
    <p>2:3 and 4:6 are equivalent—they both mean "2 units of the first for every 3 units of the second."</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 570 290" xmlns="http://www.w3.org/2000/svg">
      <text x="50" y="30" font-size="16" font-weight="bold" fill="currentColor">Recipe: 2:3 ratio (2 cups flour : 3 cups sugar)</text>

      <rect x="50" y="50" width="100" height="40" fill="#f59e0b" opacity="0.6" stroke="#30363d" stroke-width="2" rx="4"/>
      <rect x="160" y="50" width="150" height="40" fill="#22c55e" opacity="0.6" stroke="#30363d" stroke-width="2" rx="4"/>
      <text x="100" y="85" font-size="14" text-anchor="middle" font-weight="bold" fill="currentColor">2 flour</text>
      <text x="235" y="85" font-size="14" text-anchor="middle" font-weight="bold" fill="currentColor">3 sugar</text>

      <text x="50" y="130" font-size="16" font-weight="bold" fill="currentColor">Scale up by × 2 (double the recipe)</text>

      <rect x="50" y="150" width="200" height="40" fill="#f59e0b" opacity="0.6" stroke="#30363d" stroke-width="2" rx="4"/>
      <rect x="260" y="150" width="300" height="40" fill="#22c55e" opacity="0.6" stroke="#30363d" stroke-width="2" rx="4"/>
      <text x="150" y="185" font-size="14" text-anchor="middle" font-weight="bold" fill="currentColor">4 flour</text>
      <text x="410" y="185" font-size="14" text-anchor="middle" font-weight="bold" fill="currentColor">6 sugar</text>

      <text x="50" y="240" font-size="16" font-weight="bold" fill="currentColor">2:3 = 4:6 = 6:9 = 8:12 ...</text>
      <text x="50" y="270" font-size="14" fill="currentColor">All are equivalent ratios! We multiply or divide both parts by the same number.</text>
    </svg>
  </div>

  <div class="formula-box">
    <h4>Method to Find Equivalent Ratios:</h4>
    <p>\\\\( a : b = (a \\\\times k) : (b \\\\times k) \\\\) for any number \\\\( k \\\\)</p>
    <p>Example: 3:4 × 3 = 9:12</p>
  </div>

  <div class="steps-container">
    <h3>Finding Equivalent Ratios</h3>
    <div class="step">
      <h4>Method 1: Multiply Both Sides</h4>
      <p>Given 2:5, find an equivalent ratio by multiplying by 3:</p>
      <p>2:5 = (2×3):(5×3) = 6:15</p>
    </div>
    <div class="step">
      <h4>Method 2: Divide Both Sides</h4>
      <p>Given 12:8, simplify by dividing by 4:</p>
      <p>12:8 = (12÷4):(8÷4) = 3:2</p>
    </div>
  </div>

  <div class="success-box">
    <h4>Key Insight:</h4>
    <p>Scaling a ratio up or down doesn't change the relationship. A 3:2 ratio of boys to girls in one class is the same as a 30:20 ratio in a whole year group.</p>
  </div>
</div>'''
    },
    {
        "id": "3_simplifying_ratios",
        "title": "Simplifying Ratios to Lowest Terms",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>Ratio in Simplest Form</h3>
    <p>A ratio is in <strong>simplest form</strong> when the two numbers have no common factors except 1.</p>
    <p>Example: 12:8 can be simplified to 3:2 (divide both by 4)</p>
  </div>

  <div class="steps-container">
    <h3>Method: Simplify a Ratio</h3>
    <div class="step">
      <h4>Step 1: Find the GCF (Greatest Common Factor)</h4>
      <p>For 18:24:</p>
      <p>Factors of 18: 1, 2, 3, 6, 9, 18</p>
      <p>Factors of 24: 1, 2, 3, 4, 6, 8, 12, 24</p>
      <p>Common factors: 1, 2, 3, 6</p>
      <p>GCF = 6</p>
    </div>
    <div class="step">
      <h4>Step 2: Divide Both by the GCF</h4>
      <p>18:24 = (18÷6):(24÷6) = 3:4</p>
    </div>
    <div class="step">
      <h4>Step 3: Check</h4>
      <p>Are 3 and 4 coprime (no common factors)? Yes! So 3:4 is in simplest form.</p>
    </div>
  </div>

  <div class="example-box">
    <h4>More Examples:</h4>
    <p>Simplify 15:25</p>
    <p>GCF of 15 and 25 is 5</p>
    <p>15:25 = (15÷5):(25÷5) = 3:5</p>
    <br>
    <p>Simplify 20:30</p>
    <p>GCF of 20 and 30 is 10</p>
    <p>20:30 = (20÷10):(30÷10) = 2:3</p>
  </div>

  <div class="formula-box">
    <h4>Ratio Properties:</h4>
    <ul>
      <li>If \\\\( a : b \\\\) is in simplest form, then GCF(a, b) = 1</li>
      <li>Any ratio can be simplified using the GCF</li>
      <li>Sometimes it helps to find prime factors</li>
    </ul>
  </div>
</div>'''
    },
    {
        "id": "4_using_ratios_to_divide",
        "title": "Using Ratios to Divide Quantities",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>Dividing in a Given Ratio</h3>
    <p>Ratios tell us how to <strong>share or divide</strong> a total amount.</p>
    <p>If we have 35 sweets and we want to divide them in the ratio 2:5, we need to find how many equal parts there are.</p>
  </div>

  <div class="steps-container">
    <h3>Method: Divide a Quantity in a Given Ratio</h3>
    <div class="step">
      <h4>Problem: Share 35 sweets in ratio 2:5</h4>
    </div>
    <div class="step">
      <h4>Step 1: Find the total number of parts</h4>
      <p>Ratio is 2:5, so total parts = 2 + 5 = 7</p>
    </div>
    <div class="step">
      <h4>Step 2: Find the value of one part</h4>
      <p>One part = Total ÷ Total parts = 35 ÷ 7 = 5 sweets</p>
    </div>
    <div class="step">
      <h4>Step 3: Multiply each ratio part by the value of one part</h4>
      <p>First share: 2 × 5 = 10 sweets</p>
      <p>Second share: 5 × 5 = 25 sweets</p>
    </div>
    <div class="step">
      <h4>Step 4: Check your answer</h4>
      <p>10 + 25 = 35 ✓</p>
      <p>10:25 = 2:5 ✓</p>
    </div>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 510 250" xmlns="http://www.w3.org/2000/svg">
      <text x="50" y="30" font-size="16" font-weight="bold" fill="currentColor">35 sweets shared in ratio 2:5</text>

      <rect x="50" y="50" width="400" height="60" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>

      <rect x="50" y="50" width="114.3" height="60" fill="#f59e0b" opacity="0.6"/>
      <rect x="164.3" y="50" width="114.3" height="60" fill="#f59e0b" opacity="0.6"/>
      <rect x="278.6" y="50" width="171.4" height="60" fill="#4169E1" opacity="0.6"/>

      <text x="114.3" y="90" font-size="14" text-anchor="middle" font-weight="bold" fill="currentColor">5</text>
      <text x="228.6" y="90" font-size="14" text-anchor="middle" font-weight="bold" fill="currentColor">5</text>
      <text x="314.3" y="90" font-size="14" text-anchor="middle" font-weight="bold" fill="currentColor">5</text>
      <text x="363.5" y="90" font-size="14" text-anchor="middle" font-weight="bold" fill="currentColor">5</text>
      <text x="412.7" y="90" font-size="14" text-anchor="middle" font-weight="bold" fill="currentColor">5</text>

      <text x="107.15" y="140" font-size="14" text-anchor="middle" font-weight="bold" fill="currentColor">2 parts = 10</text>
      <text x="364.3" y="140" font-size="14" text-anchor="middle" font-weight="bold" fill="currentColor">5 parts = 25</text>

      <text x="50" y="200" font-size="16" font-weight="bold" fill="currentColor">Ratio = 2:5, Total parts = 7</text>
      <text x="50" y="225" font-size="14" fill="currentColor">Each part = 35 ÷ 7 = 5 sweets</text>
    </svg>
  </div>

  <div class="success-box">
    <h4>The Pattern:</h4>
    <p>To divide \\\\( T \\\\) in ratio \\\\( a : b \\\\):</p>
    <p>First amount = \\\\( \\\\frac{a}{a+b} \\\\times T \\\\)</p>
    <p>Second amount = \\\\( \\\\frac{b}{a+b} \\\\times T \\\\)</p>
  </div>
</div>'''
    },
    {
        "id": "5_proportion_and_direct_variation",
        "title": "Proportion: When Things Scale Together",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>What is a Proportion?</h3>
    <p>A <strong>proportion</strong> is an equation that states two ratios are equal.</p>
    <p>Example: \\\\( \\\\frac{2}{3} = \\\\frac{4}{6} \\\\) is a proportion.</p>
    <p>In ratio form: 2:3 = 4:6 is a proportion.</p>
  </div>

  <div class="concept-box">
    <h3>Direct Proportion</h3>
    <p>Two quantities are in <strong>direct proportion</strong> if when one increases, the other increases at the same rate.</p>
    <p>If 3 apples cost 50 cents, then 6 apples cost 100 cents (exactly double).</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 510 310" xmlns="http://www.w3.org/2000/svg">
      <text x="50" y="30" font-size="16" font-weight="bold" fill="currentColor">Direct Proportion: Cost of Apples</text>

      <text x="50" y="260" font-size="14" fill="currentColor"><tspan x="50">If 3 apples cost 50 cents, how much do 6 apples cost?</tspan><tspan x="50" dy="20">Using proportion: \\\\( \\\\frac{3}{50} = \\\\frac{6}{x} \\\\)</tspan><tspan x="50" dy="20">Cross multiply: 3x = 50 × 6 = 300</tspan><tspan x="50" dy="20">Therefore: x = 100 cents</tspan></text>
    </svg>
  </div>

  <div class="formula-box">
    <h4>Cross Multiplication for Proportions:</h4>
    <p>If \\\\( \\\\frac{a}{b} = \\\\frac{c}{d} \\\\), then \\\\( a \\\\times d = b \\\\times c \\\\)</p>
    <p>This helps us solve for unknown values.</p>
  </div>

  <div class="steps-container">
    <h3>Solving Proportions</h3>
    <div class="step">
      <h4>Example: If 5 pencils cost £2, what do 15 pencils cost?</h4>
    </div>
    <div class="step">
      <h4>Step 1: Write the proportion</h4>
      <p>\\\\( \\\\frac{5}{2} = \\\\frac{15}{x} \\\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Cross multiply</h4>
      <p>5 × x = 2 × 15</p>
      <p>5x = 30</p>
    </div>
    <div class="step">
      <h4>Step 3: Solve for x</h4>
      <p>x = 30 ÷ 5 = 6</p>
      <p>15 pencils cost £6</p>
    </div>
  </div>
</div>'''
    },
    {
        "id": "6_maps_and_scale_diagrams",
        "title": "Using Ratios: Maps and Scale Diagrams",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>Scale Diagrams and Maps</h3>
    <p>Maps and diagrams use <strong>scale ratios</strong> to show real sizes on paper.</p>
    <p>A map scale of 1:100,000 means 1 unit on the map represents 100,000 units in real life.</p>
  </div>

  <div class="steps-container">
    <h3>Method: Using Scale to Find Real Distances</h3>
    <div class="step">
      <h4>Problem: A map has scale 1:50,000. A road on the map is 8 cm long. How long is the real road?</h4>
    </div>
    <div class="step">
      <h4>Step 1: Write the scale as a ratio</h4>
      <p>Map : Real = 1 : 50,000</p>
    </div>
    <div class="step">
      <h4>Step 2: Set up a proportion</h4>
      <p>\\\\( \\\\frac{1}{50000} = \\\\frac{8}{x} \\\\)</p>
    </div>
    <div class="step">
      <h4>Step 3: Cross multiply</h4>
      <p>1 × x = 50,000 × 8</p>
      <p>x = 400,000 cm</p>
    </div>
    <div class="step">
      <h4>Step 4: Convert units</h4>
      <p>400,000 cm = 4,000 m = 4 km</p>
      <p>The real road is 4 km long.</p>
    </div>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 510 200" xmlns="http://www.w3.org/2000/svg">
      <text x="50" y="30" font-size="16" font-weight="bold" fill="currentColor">Map Example: Scale 1:100,000</text>

      <rect x="50" y="50" width="100" height="60" fill="none" stroke="#4169E1" stroke-width="2" rx="4"/>
      <text x="100" y="90" font-size="14" text-anchor="middle" fill="currentColor">2 cm on map</text>

      <path d="M 160 80 L 200 80" stroke="currentColor" stroke-width="2" marker-end="url(#arrowhead3)"/>
      <text x="180" y="70" font-size="12" text-anchor="middle" fill="currentColor">× 100,000</text>

      <rect x="210" y="50" width="200" height="60" fill="none" stroke="#22c55e" stroke-width="2" rx="4"/>
      <text x="310" y="90" font-size="14" text-anchor="middle" fill="currentColor">2 km in reality</text>

      <defs>
        <marker id="arrowhead3" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
          <polygon points="0 0, 10 3, 0 6" fill="currentColor"/>
        </marker>
      </defs>

      <text x="50" y="160" font-size="12" fill="currentColor">Scale shows the ratio between map distance and real distance.</text>
      <text x="50" y="180" font-size="12" fill="currentColor">Always check your units! 100,000 cm = 1 km</text>
    </svg>
  </div>

  <div class="success-box">
    <h4>Common Scales:</h4>
    <ul>
      <li>Model railways: 1:87 or 1:100 (very detailed models)</li>
      <li>Maps: 1:50,000 or 1:100,000 (popular for walking)</li>
      <li>Building plans: 1:100 (1 cm = 1 m)</li>
    </ul>
  </div>
</div>'''
    },
    {
        "id": "7_ratio_word_problems",
        "title": "Solving Ratio Problems with Bar Models",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>Ratio Problems in Real Life</h3>
    <p>Ratios appear in recipes, mixing paints, sharing money, comparing populations, and more.</p>
    <p>The bar model strategy helps us visualize and solve these problems.</p>
  </div>

  <div class="example-box">
    <h4>Problem 1: Sharing Money</h4>
    <p><strong>Question:</strong> Ali and Ben share £60 in the ratio 2:3. How much does each get?</p>

    <div class="diagram-container">
      <svg viewBox="0 0 510 200" xmlns="http://www.w3.org/2000/svg">
        <text x="50" y="30" font-size="14" font-weight="bold" fill="currentColor">Total: £60 shared in ratio 2:3</text>

        <text x="50" y="60" font-size="12" fill="currentColor">Ali:</text>
        <rect x="50" y="70" width="130" height="30" fill="#4169E1" opacity="0.6" stroke="#30363d" stroke-width="2" rx="4"/>
        <text x="115" y="92" font-size="12" text-anchor="middle" font-weight="bold" fill="currentColor">2 parts</text>

        <text x="50" y="130" font-size="12" fill="currentColor">Ben:</text>
        <rect x="50" y="140" width="195" height="30" fill="#22c55e" opacity="0.6" stroke="#30363d" stroke-width="2" rx="4"/>
        <text x="147.5" y="162" font-size="12" text-anchor="middle" font-weight="bold" fill="currentColor">3 parts</text>

        <text x="300" y="70" font-size="12" fill="currentColor"><tspan x="300">Total parts = 2 + 3 = 5</tspan><tspan x="300" dy="20">Each part = £60 ÷ 5 = £12</tspan><tspan x="300" dy="20">Ali = 2 × £12 = £24</tspan><tspan x="300" dy="20">Ben = 3 × £12 = £36</tspan></text>
      </svg>
    </div>
  </div>

  <div class="example-box">
    <h4>Problem 2: Recipe Scaling</h4>
    <p><strong>Question:</strong> A recipe uses flour and sugar in ratio 3:2. If you have 300g of flour, how much sugar do you need?</p>

    <div class="steps-container">
      <div class="step">
        <h4>Step 1: Write the ratio</h4>
        <p>Flour : Sugar = 3 : 2</p>
      </div>
      <div class="step">
        <h4>Step 2: Set up a proportion</h4>
        <p>\\\\( \\\\frac{3}{2} = \\\\frac{300}{x} \\\\)</p>
      </div>
      <div class="step">
        <h4>Step 3: Cross multiply</h4>
        <p>3x = 2 × 300 = 600</p>
      </div>
      <div class="step">
        <h4>Step 4: Solve</h4>
        <p>x = 200g sugar</p>
      </div>
    </div>
  </div>

  <div class="example-box">
    <h4>Problem 3: Comparing Ratios</h4>
    <p><strong>Question:</strong> Class A has boys:girls = 3:4. Class B has boys:girls = 5:6. Which class has a higher proportion of girls?</p>

    <div class="steps-container">
      <div class="step">
        <h4>Step 1: Convert to fractions</h4>
        <p>Class A: Girls = \\\\( \\\\frac{4}{7} \\\\) of the class</p>
        <p>Class B: Girls = \\\\( \\\\frac{6}{11} \\\\) of the class</p>
      </div>
      <div class="step">
        <h4>Step 2: Compare fractions</h4>
        <p>\\\\( \\\\frac{4}{7} \\\\approx 0.571 = 57.1% \\\\)</p>
        <p>\\\\( \\\\frac{6}{11} \\\\approx 0.545 = 54.5% \\\\)</p>
      </div>
      <div class="step">
        <h4>Step 3: Conclusion</h4>
        <p>Class A has a higher proportion of girls.</p>
      </div>
    </div>
  </div>

  <div class="warning-box">
    <h4>Key Phrases to Watch:</h4>
    <ul>
      <li>"in the ratio 2:3" means parts add up: 2 + 3 = 5 total parts</li>
      <li>"the ratio of A to B" tells you order: A comes first</li>
      <li>"for every 3... there are 2..." sets up the ratio</li>
    </ul>
  </div>
</div>'''
    },
    {
        "id": "8_unequal_sharing_with_remainders",
        "title": "Unequal Sharing and Remainders",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>When Sharing Doesn't Divide Evenly</h3>
    <p>Sometimes the total doesn't divide evenly by the ratio parts. We must handle the remainder carefully.</p>
  </div>

  <div class="example-box">
    <h4>Problem: Sharing with Remainders</h4>
    <p><strong>Question:</strong> Share 100 marbles in ratio 3:4. If we cannot break up marbles, what is the closest division?</p>

    <div class="diagram-container">
      <svg viewBox="0 0 510 250" xmlns="http://www.w3.org/2000/svg">
        <text x="50" y="30" font-size="14" font-weight="bold" fill="currentColor">100 marbles in ratio 3:4</text>

        <text x="50" y="70" font-size="12" fill="currentColor">Expected:</text>
        <text x="50" y="95" font-size="12" fill="currentColor">Total parts = 3 + 4 = 7</text>
        <text x="50" y="115" font-size="12" fill="currentColor">100 ÷ 7 = 14 remainder 2</text>
        <text x="50" y="135" font-size="12" fill="currentColor">Each part = 14 (not exact)</text>

        <text x="50" y="170" font-size="12" fill="currentColor">Distribution 1 (using whole parts):</text>
        <text x="50" y="190" font-size="12" fill="currentColor">First: 3 × 14 = 42 marbles</text>
        <text x="50" y="210" font-size="12" fill="currentColor">Second: 4 × 14 = 56 marbles</text>
        <text x="50" y="230" font-size="12" fill="currentColor">Total: 42 + 56 = 98 (short by 2)</text>

        <text x="300" y="70" font-size="12" fill="currentColor">When we cannot divide evenly:</text>
        <text x="300" y="100" font-size="12" fill="currentColor">Option A: Give extra to one person</text>
        <text x="300" y="120" font-size="12" fill="currentColor">First: 42 + 2 = 44</text>
        <text x="300" y="140" font-size="12" fill="currentColor">Second: 56</text>
        <text x="300" y="160" font-size="12" font-weight="bold" fill="currentColor">Ratio becomes 44:56 ≈ 3:4</text>

        <text x="300" y="190" font-size="12" fill="currentColor">Option B: Round down both</text>
        <text x="300" y="210" font-size="12" fill="currentColor">First: 42, Second: 56</text>
        <text x="300" y="230" font-size="12" fill="currentColor">(2 marbles left over)</text>
      </svg>
    </div>
  </div>

  <div class="success-box">
    <h4>Real-World Context:</h4>
    <ul>
      <li><strong>Money:</strong> If the remainder is pence, usually give it all to one person (or split it)</li>
      <li><strong>Objects:</strong> If you cannot split an object, you must round</li>
      <li><strong>Measurements:</strong> For liquids, you can usually keep the exact ratio</li>
    </ul>
  </div>

  <div class="warning-box">
    <h4>Check Your Answer:</h4>
    <ol>
      <li>Do the amounts add up to the total?</li>
      <li>Is the ratio as close as possible to the given ratio?</li>
      <li>Have you handled remainders sensibly given the context?</li>
    </ol>
  </div>
</div>'''
    }
]
