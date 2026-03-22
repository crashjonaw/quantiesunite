SECTIONS = [
    {
        "title": "What is Multiplication? The Foundation",
        "body": """
<h3>Understanding Multiplication as Repeated Addition</h3>
<p>Multiplication is a <strong>shortcut for adding the same number over and over</strong>. Instead of writing \\(3 + 3 + 3 + 3\\), we can write \\(3 \\times 4\\), which means "3 repeated 4 times" or "4 groups of 3".</p>

<p>Let's say you have 4 baskets with 3 apples in each basket. Instead of counting 3 + 3 + 3 + 3 = 12, we say \\(3 \\times 4 = 12\\) or "3 times 4 equals 12".</p>

<div class="diagram-container">
  <svg width="600" height="150" viewBox="0 0 600 150">
    <text x="300" y="25" text-anchor="middle" font-size="16" font-weight="bold">4 Baskets with 3 Apples Each</text>
    
    <g id="basket1">
      <rect x="20" y="50" width="80" height="80" fill="none" stroke="#4169E1" stroke-width="2"/>
      <circle cx="40" cy="75" r="12" fill="#f59e0b80" stroke="#f59e0b" stroke-width="1"/>
      <circle cx="60" cy="75" r="12" fill="#f59e0b80" stroke="#f59e0b" stroke-width="1"/>
      <circle cx="50" cy="95" r="12" fill="#f59e0b80" stroke="#f59e0b" stroke-width="1"/>
    </g>

    <g id="basket2">
      <rect x="120" y="50" width="80" height="80" fill="none" stroke="#22c55e" stroke-width="2"/>
      <circle cx="140" cy="75" r="12" fill="#f59e0b80" stroke="#f59e0b" stroke-width="1"/>
      <circle cx="160" cy="75" r="12" fill="#f59e0b80" stroke="#f59e0b" stroke-width="1"/>
      <circle cx="150" cy="95" r="12" fill="#f59e0b80" stroke="#f59e0b" stroke-width="1"/>
    </g>

    <g id="basket3">
      <rect x="220" y="50" width="80" height="80" fill="none" stroke="#f59e0b" stroke-width="2"/>
      <circle cx="240" cy="75" r="12" fill="#f59e0b80" stroke="#f59e0b" stroke-width="1"/>
      <circle cx="260" cy="75" r="12" fill="#f59e0b80" stroke="#f59e0b" stroke-width="1"/>
      <circle cx="250" cy="95" r="12" fill="#f59e0b80" stroke="#f59e0b" stroke-width="1"/>
    </g>

    <g id="basket4">
      <rect x="320" y="50" width="80" height="80" fill="none" stroke="#ef4444" stroke-width="2"/>
      <circle cx="340" cy="75" r="12" fill="#f59e0b80" stroke="#f59e0b" stroke-width="1"/>
      <circle cx="360" cy="75" r="12" fill="#f59e0b80" stroke="#f59e0b" stroke-width="1"/>
      <circle cx="350" cy="95" r="12" fill="#f59e0b80" stroke="#f59e0b" stroke-width="1"/>
    </g>

    <text x="480" y="90" font-size="24" font-weight="bold">3 × 4 = 12</text>
  </svg>
  <div class="diagram-caption">Four baskets with three apples each makes 12 apples total</div>
</div>

<div class="concept-box">
<h4>Key Concept: Multiplication</h4>
<p><strong>Multiplication</strong> is repeated addition. \\(a \\times b\\) means "the number \\(a\\) repeated \\(b\\) times" or "\\(b\\) groups of \\(a\\)". The result is called the <strong>product</strong>.</p>
</div>

<h3>The Language of Multiplication</h3>
<p>When we write \\(3 \\times 4 = 12\\), we can say:</p>
<ul>
  <li>"Three times four equals twelve"</li>
  <li>"Three multiplied by four equals twelve"</li>
  <li>"Four groups of three equals twelve"</li>
</ul>

<p>The numbers have special names:</p>
<p><strong>\\(3 \\times 4 = 12\\)</strong></p>
<ul>
  <li>3 is a <strong>factor</strong></li>
  <li>4 is a <strong>factor</strong></li>
  <li>12 is the <strong>product</strong></li>
</ul>
"""
    },
    {
        "title": "Arrays: Visualizing Multiplication",
        "body": """
<h3>What is an Array?</h3>
<p>An <strong>array</strong> is a way to arrange objects in rows and columns. Arrays help us see multiplication as a picture, which makes it much easier to understand and remember.</p>

<p>Let's look at \\(5 \\times 3\\) using an array:</p>

<div class="diagram-container">
  <svg width="400" height="200" viewBox="0 0 400 200">
    <text x="200" y="25" text-anchor="middle" font-size="16" font-weight="bold">An Array of 5 Rows and 3 Columns</text>

    <g id="array">
      <rect x="80" y="50" width="30" height="30" fill="#4169E180" stroke="#4169E1" stroke-width="2"/>
      <rect x="120" y="50" width="30" height="30" fill="#4169E180" stroke="#4169E1" stroke-width="2"/>
      <rect x="160" y="50" width="30" height="30" fill="#4169E180" stroke="#4169E1" stroke-width="2"/>

      <rect x="80" y="90" width="30" height="30" fill="#22c55e80" stroke="#22c55e" stroke-width="2"/>
      <rect x="120" y="90" width="30" height="30" fill="#22c55e80" stroke="#22c55e" stroke-width="2"/>
      <rect x="160" y="90" width="30" height="30" fill="#22c55e80" stroke="#22c55e" stroke-width="2"/>

      <rect x="80" y="130" width="30" height="30" fill="#f59e0b80" stroke="#f59e0b" stroke-width="2"/>
      <rect x="120" y="130" width="30" height="30" fill="#f59e0b80" stroke="#f59e0b" stroke-width="2"/>
      <rect x="160" y="130" width="30" height="30" fill="#f59e0b80" stroke="#f59e0b" stroke-width="2"/>

      <rect x="80" y="170" width="30" height="30" fill="#ef444480" stroke="#ef4444" stroke-width="2"/>
      <rect x="120" y="170" width="30" height="30" fill="#ef444480" stroke="#ef4444" stroke-width="2"/>
      <rect x="160" y="170" width="30" height="30" fill="#ef444480" stroke="#ef4444" stroke-width="2"/>

      <rect x="80" y="210" width="30" height="30" fill="#8b5cf680" stroke="#8b5cf6" stroke-width="2"/>
      <rect x="120" y="210" width="30" height="30" fill="#8b5cf680" stroke="#8b5cf6" stroke-width="2"/>
      <rect x="160" y="210" width="30" height="30" fill="#8b5cf680" stroke="#8b5cf6" stroke-width="2"/>
    </g>

    <text x="200" y="140" font-size="16" font-weight="bold">5 rows × 3 columns = 15 squares</text>
  </svg>
  <div class="diagram-caption">This array shows 5 × 3 = 15</div>
</div>

<h3>Why Arrays Help Us Learn</h3>
<p>Arrays are powerful because they show us:</p>
<ul>
  <li><strong>The commutative property:</strong> \\(5 \\times 3 = 3 \\times 5\\). If you rotate the array 90 degrees, you get the same number of squares!</li>
  <li><strong>Visual counting:</strong> We can count all the squares to find the product.</li>
  <li><strong>Patterns:</strong> Arrays help us see why certain multiplication facts go together.</li>
</ul>

<div class="concept-box">
<h4>Key Concept: Commutative Property</h4>
<p>Multiplication is <strong>commutative</strong>, which means the order doesn't matter: \\(a \\times b = b \\times a\\). So \\(3 \\times 4 = 4 \\times 3 = 12\\)</p>
</div>

<div class="example-box">
<h4>Example: 2 × 6 and 6 × 2</h4>
<p>If we make an array with 2 rows and 6 columns, we get 12 squares.</p>
<p>If we rotate it and make an array with 6 rows and 2 columns, we still get 12 squares!</p>
<p>This is why \\(2 \\times 6 = 6 \\times 2\\)</p>
</div>
"""
    },
    {
        "title": "The Times Tables: 1s Through 5s",
        "body": """
<h3>Learning the First Five Times Tables</h3>
<p>The <strong>1 times table</strong>, <strong>2 times table</strong>, and so on, show us all the products when we multiply a number by 1, 2, 3, and so on.</p>

<h3>The 1 Times Table</h3>
<p>The 1 times table is the simplest: any number times 1 equals itself.</p>
<p>\\(1 \\times 1 = 1, \\ 1 \\times 2 = 2, \\ 1 \\times 3 = 3, \\ 1 \\times 4 = 4, \\ ...\\)</p>

<h3>The 2 Times Table (Doubling)</h3>
<p>The 2 times table is about doubling. Each answer is 2 more than the last.</p>

<table style="margin: 20px auto; border-collapse: collapse; width: 100%; max-width: 500px;">
  <tr style="background: #f0f0f0;">
    <th style="border: 1px solid #333; padding: 10px;">Multiplication</th>
    <th style="border: 1px solid #333; padding: 10px;">Product</th>
  </tr>
  <tr>
    <td style="border: 1px solid #333; padding: 10px;">2 × 1</td>
    <td style="border: 1px solid #333; padding: 10px;">2</td>
  </tr>
  <tr style="background: #f9f9f9;">
    <td style="border: 1px solid #333; padding: 10px;">2 × 2</td>
    <td style="border: 1px solid #333; padding: 10px;">4</td>
  </tr>
  <tr>
    <td style="border: 1px solid #333; padding: 10px;">2 × 3</td>
    <td style="border: 1px solid #333; padding: 10px;">6</td>
  </tr>
  <tr style="background: #f9f9f9;">
    <td style="border: 1px solid #333; padding: 10px;">2 × 4</td>
    <td style="border: 1px solid #333; padding: 10px;">8</td>
  </tr>
  <tr>
    <td style="border: 1px solid #333; padding: 10px;">2 × 5</td>
    <td style="border: 1px solid #333; padding: 10px;">10</td>
  </tr>
  <tr style="background: #f9f9f9;">
    <td style="border: 1px solid #333; padding: 10px;">2 × 6</td>
    <td style="border: 1px solid #333; padding: 10px;">12</td>
  </tr>
</table>

<p><strong>Pattern:</strong> 2, 4, 6, 8, 10, 12, 14, 16, 18, 20... (all even numbers!)</p>

<h3>The 5 Times Table</h3>
<p>The 5 times table has a beautiful pattern: every answer ends in either 0 or 5.</p>

<p>\\(5, 10, 15, 20, 25, 30, 35, 40, 45, 50\\)</p>

<div class="diagram-container">
  <svg width="600" height="100" viewBox="0 0 600 100">
    <text x="300" y="25" text-anchor="middle" font-size="14" font-weight="bold">5 Times Table Pattern: Notice the 0s and 5s</text>
    <text x="50" y="60" text-anchor="middle" font-size="12">5 × 1</text>
    <text x="50" y="80" text-anchor="middle" font-size="16" font-weight="bold" fill="#f59e0b">5</text>

    <text x="120" y="60" text-anchor="middle" font-size="12">5 × 2</text>
    <text x="120" y="80" text-anchor="middle" font-size="16" font-weight="bold" fill="#f59e0b">10</text>

    <text x="190" y="60" text-anchor="middle" font-size="12">5 × 3</text>
    <text x="190" y="80" text-anchor="middle" font-size="16" font-weight="bold" fill="#f59e0b">15</text>

    <text x="260" y="60" text-anchor="middle" font-size="12">5 × 4</text>
    <text x="260" y="80" text-anchor="middle" font-size="16" font-weight="bold" fill="#f59e0b">20</text>

    <text x="330" y="60" text-anchor="middle" font-size="12">5 × 5</text>
    <text x="330" y="80" text-anchor="middle" font-size="16" font-weight="bold" fill="#f59e0b">25</text>

    <text x="400" y="60" text-anchor="middle" font-size="12">5 × 6</text>
    <text x="400" y="80" text-anchor="middle" font-size="16" font-weight="bold" fill="#f59e0b">30</text>

    <text x="470" y="60" text-anchor="middle" font-size="12">5 × 7</text>
    <text x="470" y="80" text-anchor="middle" font-size="16" font-weight="bold" fill="#f59e0b">35</text>

    <text x="540" y="60" text-anchor="middle" font-size="12">5 × 8</text>
    <text x="540" y="80" text-anchor="middle" font-size="16" font-weight="bold" fill="#f59e0b">40</text>
  </svg>
  <div class="diagram-caption">All 5 times table answers end in 0 or 5</div>
</div>

<h3>The 3 and 4 Times Tables</h3>
<p>The 3 and 4 times tables require a bit more memorization, but they're still manageable.</p>

<div class="example-box">
<h4>3 Times Table</h4>
<p>\\(3, 6, 9, 12, 15, 18, 21, 24, 27, 30\\)</p>
<p><strong>Hint:</strong> Notice the pattern in the digits: 3, 6, 9, 2+1=3, 5, 8, 1+2=3, 4+2=6, 7+2=9, 0</p>
</div>

<div class="example-box">
<h4>4 Times Table</h4>
<p>\\(4, 8, 12, 16, 20, 24, 28, 32, 36, 40\\)</p>
<p><strong>Hint:</strong> Notice that the 4 times table is just the 2 times table doubled. So \\(4 \\times n = 2 \\times (2 \\times n)\\)</p>
</div>
"""
    },
    {
        "title": "The Times Tables: 6s Through 10s",
        "body": """
<h3>Moving to the Bigger Times Tables</h3>
<p>The 6, 7, 8, 9, and 10 times tables build on what you already know, with some helpful patterns to notice.</p>

<h3>The 10 Times Table (The Easiest!)</h3>
<p>The 10 times table is wonderful because it's just adding a zero to any number:</p>

<p>\\(10, 20, 30, 40, 50, 60, 70, 80, 90, 100\\)</p>

<p>\\(10 \\times 3 = 30\\), \\(10 \\times 7 = 70\\), \\(10 \\times 12 = 120\\)</p>

<div class="success-box">
<h4>Remember: The 10 Times Table Rule</h4>
<p>To multiply any number by 10, just add a 0 at the end of the number. This is the place value system at work!</p>
</div>

<h3>The 9 Times Table (The Magical One)</h3>
<p>The 9 times table has a hidden pattern. Look at the digits of each product:</p>

<table style="margin: 20px auto; border-collapse: collapse; width: 100%; max-width: 500px;">
  <tr style="background: #f0f0f0;">
    <th style="border: 1px solid #333; padding: 10px;">Multiplication</th>
    <th style="border: 1px solid #333; padding: 10px;">Product</th>
    <th style="border: 1px solid #333; padding: 10px;">Digits Add to 9</th>
  </tr>
  <tr>
    <td style="border: 1px solid #333; padding: 10px;">9 × 1</td>
    <td style="border: 1px solid #333; padding: 10px;">9</td>
    <td style="border: 1px solid #333; padding: 10px;">9 = 9</td>
  </tr>
  <tr style="background: #f9f9f9;">
    <td style="border: 1px solid #333; padding: 10px;">9 × 2</td>
    <td style="border: 1px solid #333; padding: 10px;">18</td>
    <td style="border: 1px solid #333; padding: 10px;">1 + 8 = 9</td>
  </tr>
  <tr>
    <td style="border: 1px solid #333; padding: 10px;">9 × 3</td>
    <td style="border: 1px solid #333; padding: 10px;">27</td>
    <td style="border: 1px solid #333; padding: 10px;">2 + 7 = 9</td>
  </tr>
  <tr style="background: #f9f9f9;">
    <td style="border: 1px solid #333; padding: 10px;">9 × 4</td>
    <td style="border: 1px solid #333; padding: 10px;">36</td>
    <td style="border: 1px solid #333; padding: 10px;">3 + 6 = 9</td>
  </tr>
  <tr>
    <td style="border: 1px solid #333; padding: 10px;">9 × 5</td>
    <td style="border: 1px solid #333; padding: 10px;">45</td>
    <td style="border: 1px solid #333; padding: 10px;">4 + 5 = 9</td>
  </tr>
</table>

<p><strong>The digits in every answer add up to 9!</strong> This is a fantastic way to check your work.</p>

<h3>The 6, 7, and 8 Times Tables</h3>
<p>These don't have as obvious patterns, so repetition is key to learning them.</p>

<div class="example-box">
<h4>6 Times Table</h4>
<p>\\(6, 12, 18, 24, 30, 36, 42, 48, 54, 60\\)</p>
</div>

<div class="example-box">
<h4>7 Times Table</h4>
<p>\\(7, 14, 21, 28, 35, 42, 49, 56, 63, 70\\)</p>
</div>

<div class="example-box">
<h4>8 Times Table</h4>
<p>\\(8, 16, 24, 32, 40, 48, 56, 64, 72, 80\\)</p>
<p><strong>Hint:</strong> The 8 times table is the 2 times table tripled. \\(8 \\times n = 4 \\times (2 \\times n)\\)</p>
</div>

<div class="concept-box">
<h4>Key Concept: Relationships Between Tables</h4>
<p>Many times tables are related to each other through doubling or other patterns. Learning to recognize these relationships helps you remember all the facts faster.</p>
</div>
"""
    },
    {
        "title": "Strategies for Learning and Remembering Times Tables",
        "body": """
<h3>Why Learn Times Tables?</h3>
<p>Times tables aren't just facts to memorize. They form the <strong>foundation</strong> for all multiplication, division, fractions, and many other areas of mathematics. When you know them automatically, math becomes faster and easier.</p>

<h3>Strategy 1: Skip Counting</h3>
<p>Skip counting is the foundation of multiplication. To learn the 3 times table, count by threes:</p>

<p><strong>3, 6, 9, 12, 15, 18, 21, 24, 27, 30</strong></p>

<p>This shows you that \\(3 \\times 1 = 3\\), \\(3 \\times 2 = 6\\), and so on.</p>

<div class="steps-container">
  <div class="step-item">
    <div class="step-num">1</div>
    <div class="step-content">
      <p><strong>Start at zero:</strong> 0</p>
    </div>
  </div>
  <div class="step-item">
    <div class="step-num">2</div>
    <div class="step-content">
      <p><strong>Add the same number each time:</strong> 0 + 3 = 3, + 3 = 6, + 3 = 9...</p>
    </div>
  </div>
  <div class="step-item">
    <div class="step-num">3</div>
    <div class="step-content">
      <p><strong>Notice the pattern:</strong> Each skip adds another group of that number.</p>
    </div>
  </div>
</div>

<h3>Strategy 2: Look for Patterns</h3>
<p>We've already discovered some patterns:</p>
<ul>
  <li>The 10 times table: just add a zero</li>
  <li>The 5 times table: ends in 0 or 5</li>
  <li>The 2 times table: all even numbers</li>
  <li>The 9 times table: digits add to 9</li>
</ul>

<p>Using these patterns helps you remember faster than just memorizing randomly.</p>

<h3>Strategy 3: Relationship to Other Facts</h3>
<p>Use facts you know to figure out ones you don't:</p>

<div class="example-box">
<h4>Example: Finding 7 × 8 When You Know 7 × 7</h4>
<p>If you know \\(7 \\times 7 = 49\\), you can find \\(7 \\times 8\\) by adding one more group of 7:</p>
<p>\\(7 \\times 8 = 7 \\times 7 + 7 = 49 + 7 = 56\\)</p>
</div>

<h3>Strategy 4: Use Arrays and Visuals</h3>
<p>Drawing arrays or using objects helps make multiplication concrete, not just abstract.</p>

<h3>Strategy 5: Consistent Daily Practice</h3>
<p>Short daily practice (5-10 minutes) is much better than long occasional sessions. Practice facts you don't know as well as facts you do know to keep them fresh.</p>

<div class="warning-box">
<h4>Common Mistake: Confusing Multiplication with Addition</h4>
<p>Remember: \\(3 \\times 4\\) means 3 groups of 4 (or 4 groups of 3), not \\(3 + 4\\). Make sure you understand the difference between "groups of" and "plus".</p>
</div>

<div class="success-box">
<h4>Remember: Multiplication Gets Easier</h4>
<p>Learning times tables takes time and practice, but once you know them, they become automatic. Then math becomes much faster and more enjoyable. Stick with it!</p>
</div>
"""
    },
    {
        "title": "Practicing with Real-World Applications",
        "body": """
<h3>Why Use Multiplication in Real Life?</h3>
<p>Multiplication appears everywhere in the real world. Learning to see multiplication in everyday situations makes learning times tables meaningful and memorable.</p>

<h3>Example 1: Groups of Objects</h3>
<p>Imagine you're organizing things into equal groups:</p>

<div class="example-box">
<h4>Organizing Sports Equipment</h4>
<p>You have 6 soccer balls, and you want to put them into 3 bags equally. How many go in each bag?</p>
<p>This is \\(6 \\div 3 = 2\\) (division), but we can think about it backward: 3 bags with 2 balls each is \\(3 \\times 2 = 6\\).</p>
</div>

<h3>Example 2: Area and Dimensions</h3>
<p>Multiplication helps us measure spaces:</p>

<div class="example-box">
<h4>Tiling a Floor</h4>
<p>You have a rectangular floor that is 4 meters long and 7 meters wide. How many square meters of tile do you need?</p>
<p>Answer: \\(4 \\times 7 = 28\\) square meters</p>
</div>

<h3>Example 3: Money and Shopping</h3>
<p>Multiplication is essential for figuring out costs:</p>

<div class="example-box">
<h4>Buying Items in Bulk</h4>
<p>If a pencil costs 5 dollars and you buy 8 pencils, how much do you spend?</p>
<p>\\(5 \\times 8 = 40\\) dollars</p>
</div>

<h3>Example 4: Time and Schedules</h3>
<p>Multiplication helps us work with time:</p>

<div class="example-box">
<h4>Music Lessons</h4>
<p>You have music lessons every week, and each lesson is 30 minutes. How many minutes of lessons do you have in 9 weeks?</p>
<p>\\(30 \\times 9 = 270\\) minutes (which is 4 hours and 30 minutes)</p>
</div>

<h3>Example 5: Recipes and Cooking</h3>
<p>Recipes often need to be multiplied for more servings:</p>

<div class="example-box">
<h4>Making Cookies</h4>
<p>A cookie recipe makes 12 cookies and calls for 2 cups of flour. If you want to make 4 times as many cookies, how much flour do you need?</p>
<p>\\(2 \\times 4 = 8\\) cups of flour</p>
</div>

<div class="concept-box">
<h4>Key Concept: Multiplication Is Everywhere</h4>
<p>Once you recognize multiplication in the world around you, you'll see it constantly—in shopping, cooking, sports, building, and planning. This real-world connection makes learning times tables purposeful and fun.</p>
</div>

<div class="interactive-widget">
  <h4>Challenge: Find Multiplication in Your Day</h4>
  <p>Think about what you did today. Can you identify 3 situations where multiplication might be useful?</p>
  <p>Some ideas: buying multiple items, arranging objects, measuring spaces, counting time, sharing things fairly...</p>
</div>
"""
    },
    {
        "title": "The Complete Multiplication Table Reference",
        "body": """
<h3>The Full 12 × 12 Multiplication Table</h3>
<p>Here is the complete multiplication table for reference. You don't need to memorize all of it at once—just focus on one or two tables at a time.</p>

<div class="diagram-container">
  <svg width="650" height="680" viewBox="0 0 650 680">
    <text x="325" y="25" text-anchor="middle" font-size="16" font-weight="bold">Complete Multiplication Table (1-12)</text>
    
    <rect x="10" y="40" width="630" height="630" fill="none" stroke="#333" stroke-width="2"/>
    
    <text x="30" y="80" font-size="11" font-weight="bold">×</text>
    <text x="60" y="80" text-anchor="middle" font-size="11" font-weight="bold">1</text>
    <text x="90" y="80" text-anchor="middle" font-size="11" font-weight="bold">2</text>
    <text x="120" y="80" text-anchor="middle" font-size="11" font-weight="bold">3</text>
    <text x="150" y="80" text-anchor="middle" font-size="11" font-weight="bold">4</text>
    <text x="180" y="80" text-anchor="middle" font-size="11" font-weight="bold">5</text>
    <text x="210" y="80" text-anchor="middle" font-size="11" font-weight="bold">6</text>
    <text x="240" y="80" text-anchor="middle" font-size="11" font-weight="bold">7</text>
    <text x="270" y="80" text-anchor="middle" font-size="11" font-weight="bold">8</text>
    <text x="300" y="80" text-anchor="middle" font-size="11" font-weight="bold">9</text>
    <text x="330" y="80" text-anchor="middle" font-size="11" font-weight="bold">10</text>
    <text x="360" y="80" text-anchor="middle" font-size="11" font-weight="bold">11</text>
    <text x="390" y="80" text-anchor="middle" font-size="11" font-weight="bold">12</text>

    <text x="30" y="110" text-anchor="end" font-size="11" font-weight="bold">1</text>
    <text x="60" y="110" text-anchor="middle" font-size="10">1</text>
    <text x="90" y="110" text-anchor="middle" font-size="10">2</text>
    <text x="120" y="110" text-anchor="middle" font-size="10">3</text>
    <text x="150" y="110" text-anchor="middle" font-size="10">4</text>
    <text x="180" y="110" text-anchor="middle" font-size="10">5</text>
    <text x="210" y="110" text-anchor="middle" font-size="10">6</text>
    <text x="240" y="110" text-anchor="middle" font-size="10">7</text>
    <text x="270" y="110" text-anchor="middle" font-size="10">8</text>
    <text x="300" y="110" text-anchor="middle" font-size="10">9</text>
    <text x="330" y="110" text-anchor="middle" font-size="10">10</text>
    <text x="360" y="110" text-anchor="middle" font-size="10">11</text>
    <text x="390" y="110" text-anchor="middle" font-size="10">12</text>

    <text x="30" y="140" text-anchor="end" font-size="11" font-weight="bold">2</text>
    <text x="60" y="140" text-anchor="middle" font-size="10">2</text>
    <text x="90" y="140" text-anchor="middle" font-size="10">4</text>
    <text x="120" y="140" text-anchor="middle" font-size="10">6</text>
    <text x="150" y="140" text-anchor="middle" font-size="10">8</text>
    <text x="180" y="140" text-anchor="middle" font-size="10">10</text>
    <text x="210" y="140" text-anchor="middle" font-size="10">12</text>
    <text x="240" y="140" text-anchor="middle" font-size="10">14</text>
    <text x="270" y="140" text-anchor="middle" font-size="10">16</text>
    <text x="300" y="140" text-anchor="middle" font-size="10">18</text>
    <text x="330" y="140" text-anchor="middle" font-size="10">20</text>
    <text x="360" y="140" text-anchor="middle" font-size="10">22</text>
    <text x="390" y="140" text-anchor="middle" font-size="10">24</text>

    <text x="30" y="170" text-anchor="end" font-size="11" font-weight="bold">3</text>
    <text x="60" y="170" text-anchor="middle" font-size="10">3</text>
    <text x="90" y="170" text-anchor="middle" font-size="10">6</text>
    <text x="120" y="170" text-anchor="middle" font-size="10">9</text>
    <text x="150" y="170" text-anchor="middle" font-size="10">12</text>
    <text x="180" y="170" text-anchor="middle" font-size="10">15</text>
    <text x="210" y="170" text-anchor="middle" font-size="10">18</text>
    <text x="240" y="170" text-anchor="middle" font-size="10">21</text>
    <text x="270" y="170" text-anchor="middle" font-size="10">24</text>
    <text x="300" y="170" text-anchor="middle" font-size="10">27</text>
    <text x="330" y="170" text-anchor="middle" font-size="10">30</text>
    <text x="360" y="170" text-anchor="middle" font-size="10">33</text>
    <text x="390" y="170" text-anchor="middle" font-size="10">36</text>

    <text x="30" y="200" text-anchor="end" font-size="11" font-weight="bold">4</text>
    <text x="60" y="200" text-anchor="middle" font-size="10">4</text>
    <text x="90" y="200" text-anchor="middle" font-size="10">8</text>
    <text x="120" y="200" text-anchor="middle" font-size="10">12</text>
    <text x="150" y="200" text-anchor="middle" font-size="10">16</text>
    <text x="180" y="200" text-anchor="middle" font-size="10">20</text>
    <text x="210" y="200" text-anchor="middle" font-size="10">24</text>
    <text x="240" y="200" text-anchor="middle" font-size="10">28</text>
    <text x="270" y="200" text-anchor="middle" font-size="10">32</text>
    <text x="300" y="200" text-anchor="middle" font-size="10">36</text>
    <text x="330" y="200" text-anchor="middle" font-size="10">40</text>
    <text x="360" y="200" text-anchor="middle" font-size="10">44</text>
    <text x="390" y="200" text-anchor="middle" font-size="10">48</text>

    <text x="30" y="230" text-anchor="end" font-size="11" font-weight="bold">5</text>
    <text x="60" y="230" text-anchor="middle" font-size="10">5</text>
    <text x="90" y="230" text-anchor="middle" font-size="10">10</text>
    <text x="120" y="230" text-anchor="middle" font-size="10">15</text>
    <text x="150" y="230" text-anchor="middle" font-size="10">20</text>
    <text x="180" y="230" text-anchor="middle" font-size="10">25</text>
    <text x="210" y="230" text-anchor="middle" font-size="10">30</text>
    <text x="240" y="230" text-anchor="middle" font-size="10">35</text>
    <text x="270" y="230" text-anchor="middle" font-size="10">40</text>
    <text x="300" y="230" text-anchor="middle" font-size="10">45</text>
    <text x="330" y="230" text-anchor="middle" font-size="10">50</text>
    <text x="360" y="230" text-anchor="middle" font-size="10">55</text>
    <text x="390" y="230" text-anchor="middle" font-size="10">60</text>

    <text x="30" y="260" text-anchor="end" font-size="11" font-weight="bold">6</text>
    <text x="60" y="260" text-anchor="middle" font-size="10">6</text>
    <text x="90" y="260" text-anchor="middle" font-size="10">12</text>
    <text x="120" y="260" text-anchor="middle" font-size="10">18</text>
    <text x="150" y="260" text-anchor="middle" font-size="10">24</text>
    <text x="180" y="260" text-anchor="middle" font-size="10">30</text>
    <text x="210" y="260" text-anchor="middle" font-size="10">36</text>
    <text x="240" y="260" text-anchor="middle" font-size="10">42</text>
    <text x="270" y="260" text-anchor="middle" font-size="10">48</text>
    <text x="300" y="260" text-anchor="middle" font-size="10">54</text>
    <text x="330" y="260" text-anchor="middle" font-size="10">60</text>
    <text x="360" y="260" text-anchor="middle" font-size="10">66</text>
    <text x="390" y="260" text-anchor="middle" font-size="10">72</text>

    <text x="30" y="290" text-anchor="end" font-size="11" font-weight="bold">7</text>
    <text x="60" y="290" text-anchor="middle" font-size="10">7</text>
    <text x="90" y="290" text-anchor="middle" font-size="10">14</text>
    <text x="120" y="290" text-anchor="middle" font-size="10">21</text>
    <text x="150" y="290" text-anchor="middle" font-size="10">28</text>
    <text x="180" y="290" text-anchor="middle" font-size="10">35</text>
    <text x="210" y="290" text-anchor="middle" font-size="10">42</text>
    <text x="240" y="290" text-anchor="middle" font-size="10">49</text>
    <text x="270" y="290" text-anchor="middle" font-size="10">56</text>
    <text x="300" y="290" text-anchor="middle" font-size="10">63</text>
    <text x="330" y="290" text-anchor="middle" font-size="10">70</text>
    <text x="360" y="290" text-anchor="middle" font-size="10">77</text>
    <text x="390" y="290" text-anchor="middle" font-size="10">84</text>

    <text x="30" y="320" text-anchor="end" font-size="11" font-weight="bold">8</text>
    <text x="60" y="320" text-anchor="middle" font-size="10">8</text>
    <text x="90" y="320" text-anchor="middle" font-size="10">16</text>
    <text x="120" y="320" text-anchor="middle" font-size="10">24</text>
    <text x="150" y="320" text-anchor="middle" font-size="10">32</text>
    <text x="180" y="320" text-anchor="middle" font-size="10">40</text>
    <text x="210" y="320" text-anchor="middle" font-size="10">48</text>
    <text x="240" y="320" text-anchor="middle" font-size="10">56</text>
    <text x="270" y="320" text-anchor="middle" font-size="10">64</text>
    <text x="300" y="320" text-anchor="middle" font-size="10">72</text>
    <text x="330" y="320" text-anchor="middle" font-size="10">80</text>
    <text x="360" y="320" text-anchor="middle" font-size="10">88</text>
    <text x="390" y="320" text-anchor="middle" font-size="10">96</text>

    <text x="30" y="350" text-anchor="end" font-size="11" font-weight="bold">9</text>
    <text x="60" y="350" text-anchor="middle" font-size="10">9</text>
    <text x="90" y="350" text-anchor="middle" font-size="10">18</text>
    <text x="120" y="350" text-anchor="middle" font-size="10">27</text>
    <text x="150" y="350" text-anchor="middle" font-size="10">36</text>
    <text x="180" y="350" text-anchor="middle" font-size="10">45</text>
    <text x="210" y="350" text-anchor="middle" font-size="10">54</text>
    <text x="240" y="350" text-anchor="middle" font-size="10">63</text>
    <text x="270" y="350" text-anchor="middle" font-size="10">72</text>
    <text x="300" y="350" text-anchor="middle" font-size="10">81</text>
    <text x="330" y="350" text-anchor="middle" font-size="10">90</text>
    <text x="360" y="350" text-anchor="middle" font-size="10">99</text>
    <text x="390" y="350" text-anchor="middle" font-size="10">108</text>

    <text x="30" y="380" text-anchor="end" font-size="11" font-weight="bold">10</text>
    <text x="60" y="380" text-anchor="middle" font-size="10">10</text>
    <text x="90" y="380" text-anchor="middle" font-size="10">20</text>
    <text x="120" y="380" text-anchor="middle" font-size="10">30</text>
    <text x="150" y="380" text-anchor="middle" font-size="10">40</text>
    <text x="180" y="380" text-anchor="middle" font-size="10">50</text>
    <text x="210" y="380" text-anchor="middle" font-size="10">60</text>
    <text x="240" y="380" text-anchor="middle" font-size="10">70</text>
    <text x="270" y="380" text-anchor="middle" font-size="10">80</text>
    <text x="300" y="380" text-anchor="middle" font-size="10">90</text>
    <text x="330" y="380" text-anchor="middle" font-size="10">100</text>
    <text x="360" y="380" text-anchor="middle" font-size="10">110</text>
    <text x="390" y="380" text-anchor="middle" font-size="10">120</text>

    <text x="30" y="410" text-anchor="end" font-size="11" font-weight="bold">11</text>
    <text x="60" y="410" text-anchor="middle" font-size="10">11</text>
    <text x="90" y="410" text-anchor="middle" font-size="10">22</text>
    <text x="120" y="410" text-anchor="middle" font-size="10">33</text>
    <text x="150" y="410" text-anchor="middle" font-size="10">44</text>
    <text x="180" y="410" text-anchor="middle" font-size="10">55</text>
    <text x="210" y="410" text-anchor="middle" font-size="10">66</text>
    <text x="240" y="410" text-anchor="middle" font-size="10">77</text>
    <text x="270" y="410" text-anchor="middle" font-size="10">88</text>
    <text x="300" y="410" text-anchor="middle" font-size="10">99</text>
    <text x="330" y="410" text-anchor="middle" font-size="10">110</text>
    <text x="360" y="410" text-anchor="middle" font-size="10">121</text>
    <text x="390" y="410" text-anchor="middle" font-size="10">132</text>

    <text x="30" y="440" text-anchor="end" font-size="11" font-weight="bold">12</text>
    <text x="60" y="440" text-anchor="middle" font-size="10">12</text>
    <text x="90" y="440" text-anchor="middle" font-size="10">24</text>
    <text x="120" y="440" text-anchor="middle" font-size="10">36</text>
    <text x="150" y="440" text-anchor="middle" font-size="10">48</text>
    <text x="180" y="440" text-anchor="middle" font-size="10">60</text>
    <text x="210" y="440" text-anchor="middle" font-size="10">72</text>
    <text x="240" y="440" text-anchor="middle" font-size="10">84</text>
    <text x="270" y="440" text-anchor="middle" font-size="10">96</text>
    <text x="300" y="440" text-anchor="middle" font-size="10">108</text>
    <text x="330" y="440" text-anchor="middle" font-size="10">120</text>
    <text x="360" y="440" text-anchor="middle" font-size="10">132</text>
    <text x="390" y="440" text-anchor="middle" font-size="10">144</text>
  </svg>
  <div class="diagram-caption">Use this table as a reference, but focus on learning one table at a time</div>
</div>

<div class="success-box">
<h4>Remember: You've Got This!</h4>
<p>Learning multiplication tables is a journey, not a race. Celebrate each table you master, and remember that with regular practice, these facts will become automatic. Soon you'll be amazed at how fast you can multiply!</p>
</div>
"""
    }
]
