SECTIONS = [
    {
        "title": "What is a Number? Building from One",
        "body": """
<h3>The Concept of Counting</h3>
<p>Before we can talk about big numbers, we need to understand what a <strong>number</strong> is. A number represents a <strong>quantity</strong> — how many objects we have.</p>

<p>Imagine you have apples. If you have one apple, we write <strong>1</strong>. If you add another apple, you have two apples, which we write <strong>2</strong>. Each time you add one more apple, the number increases by one.</p>

<div class="visual-grid" style="margin: 20px 0; text-align: center;">
  <strong>1 apple:</strong>
  <svg width="80" height="80" style="display: inline-block; margin: 0 10px;">
    <circle cx="40" cy="40" r="25" fill="#f59e0b80" stroke="#f59e0b" stroke-width="2"/>
  </svg>
  <strong>2 apples:</strong>
  <svg width="120" height="80" style="display: inline-block; margin: 0 10px;">
    <circle cx="30" cy="40" r="25" fill="#f59e0b80" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="90" cy="40" r="25" fill="#f59e0b80" stroke="#f59e0b" stroke-width="2"/>
  </svg>
  <strong>3 apples:</strong>
  <svg width="160" height="80" style="display: inline-block; margin: 0 10px;">
    <circle cx="25" cy="40" r="25" fill="#f59e0b80" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="80" cy="40" r="25" fill="#f59e0b80" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="135" cy="40" r="25" fill="#f59e0b80" stroke="#f59e0b" stroke-width="2"/>
  </svg>
</div>

<h3>The Number Line</h3>
<p>All whole numbers can be arranged on a <strong>number line</strong> that goes from left to right. Each tick mark represents one more unit.</p>

<div class="diagram-container">
  <svg width="600" height="80" viewBox="0 0 600 80">
    <line x1="20" y1="40" x2="580" y2="40" stroke="#333" stroke-width="2"/>
    <circle cx="20" cy="40" r="4" fill="#4169E1"/>
    <text x="20" y="65" text-anchor="middle" font-size="14">0</text>
    <line x1="70" y1="35" x2="70" y2="45" stroke="#333" stroke-width="2"/>
    <text x="70" y="65" text-anchor="middle" font-size="14">1</text>
    <line x1="120" y1="35" x2="120" y2="45" stroke="#333" stroke-width="2"/>
    <text x="120" y="65" text-anchor="middle" font-size="14">2</text>
    <line x1="170" y1="35" x2="170" y2="45" stroke="#333" stroke-width="2"/>
    <text x="170" y="65" text-anchor="middle" font-size="14">3</text>
    <line x1="220" y1="35" x2="220" y2="45" stroke="#333" stroke-width="2"/>
    <text x="220" y="65" text-anchor="middle" font-size="14">4</text>
    <line x1="270" y1="35" x2="270" y2="45" stroke="#333" stroke-width="2"/>
    <text x="270" y="65" text-anchor="middle" font-size="14">5</text>
    <line x1="320" y1="35" x2="320" y2="45" stroke="#333" stroke-width="2"/>
    <text x="320" y="65" text-anchor="middle" font-size="14">6</text>
    <line x1="370" y1="35" x2="370" y2="45" stroke="#333" stroke-width="2"/>
    <text x="370" y="65" text-anchor="middle" font-size="14">7</text>
    <line x1="420" y1="35" x2="420" y2="45" stroke="#333" stroke-width="2"/>
    <text x="420" y="65" text-anchor="middle" font-size="14">8</text>
    <line x1="470" y1="35" x2="470" y2="45" stroke="#333" stroke-width="2"/>
    <text x="470" y="65" text-anchor="middle" font-size="14">9</text>
    <line x1="520" y1="35" x2="520" y2="45" stroke="#333" stroke-width="2"/>
    <text x="520" y="65" text-anchor="middle" font-size="14">10</text>
  </svg>
  <div class="diagram-caption">The number line starts at 0 and continues forever</div>
</div>

<div class="concept-box">
<h4>Key Concept: Whole Numbers</h4>
<p><strong>Whole numbers</strong> are: 0, 1, 2, 3, 4, 5, 6, ... and so on forever. They never include fractions or decimals. Every whole number is exactly one more than the number before it.</p>
</div>
"""
    },
    {
        "title": "Place Value: How to Build Bigger Numbers",
        "body": """
<h3>Understanding Place Value</h3>
<p>When we write numbers, the <strong>position of each digit</strong> tells us what that digit represents. This is called <strong>place value</strong>.</p>

<p>Let's look at the number <strong>347</strong>:</p>

<div class="diagram-container">
  <svg width="500" height="200" viewBox="0 0 500 200">
    <rect x="20" y="40" width="120" height="80" fill="#4169E180" stroke="#4169E1" stroke-width="2"/>
    <text x="80" y="110" text-anchor="middle" font-size="36" font-weight="bold">3</text>
    <text x="80" y="150" text-anchor="middle" font-size="14" font-weight="bold">Hundreds place</text>

    <rect x="190" y="40" width="120" height="80" fill="#22c55e80" stroke="#22c55e" stroke-width="2"/>
    <text x="250" y="110" text-anchor="middle" font-size="36" font-weight="bold">4</text>
    <text x="250" y="150" text-anchor="middle" font-size="14" font-weight="bold">Tens place</text>

    <rect x="360" y="40" width="120" height="80" fill="#f59e0b80" stroke="#f59e0b" stroke-width="2"/>
    <text x="420" y="110" text-anchor="middle" font-size="36" font-weight="bold">7</text>
    <text x="420" y="150" text-anchor="middle" font-size="14" font-weight="bold">Ones place</text>
  </svg>
  <div class="diagram-caption">In 347, the 3 is in the hundreds place, the 4 is in the tens place, and the 7 is in the ones place</div>
</div>

<p>This number means: <strong>3 hundreds + 4 tens + 7 ones</strong></p>
<p>Or written mathematically: \\(3 \\times 100 + 4 \\times 10 + 7 \\times 1 = 300 + 40 + 7 = 347\\)</p>

<h3>The Place Value System</h3>
<p>Each place to the left is worth 10 times more than the place to its right.</p>

<table style="margin: 20px auto; border-collapse: collapse; width: 100%; max-width: 600px;">
  <tr style="background: #f0f0f0;">
    <th style="border: 1px solid #333; padding: 10px;">Place Name</th>
    <th style="border: 1px solid #333; padding: 10px;">Value</th>
    <th style="border: 1px solid #333; padding: 10px;">Example</th>
  </tr>
  <tr>
    <td style="border: 1px solid #333; padding: 10px;">Ones</td>
    <td style="border: 1px solid #333; padding: 10px;">1</td>
    <td style="border: 1px solid #333; padding: 10px;">5 ones = 5</td>
  </tr>
  <tr style="background: #f9f9f9;">
    <td style="border: 1px solid #333; padding: 10px;">Tens</td>
    <td style="border: 1px solid #333; padding: 10px;">10</td>
    <td style="border: 1px solid #333; padding: 10px;">3 tens = 30</td>
  </tr>
  <tr>
    <td style="border: 1px solid #333; padding: 10px;">Hundreds</td>
    <td style="border: 1px solid #333; padding: 10px;">100</td>
    <td style="border: 1px solid #333; padding: 10px;">2 hundreds = 200</td>
  </tr>
  <tr style="background: #f9f9f9;">
    <td style="border: 1px solid #333; padding: 10px;">Thousands</td>
    <td style="border: 1px solid #333; padding: 10px;">1,000</td>
    <td style="border: 1px solid #333; padding: 10px;">7 thousands = 7,000</td>
  </tr>
  <tr>
    <td style="border: 1px solid #333; padding: 10px;">Ten Thousands</td>
    <td style="border: 1px solid #333; padding: 10px;">10,000</td>
    <td style="border: 1px solid #333; padding: 10px;">4 ten thousands = 40,000</td>
  </tr>
</table>

<div class="concept-box">
<h4>Key Concept: Place Value Position</h4>
<p>In any number, each digit's meaning depends on its position. Moving a digit one place to the left multiplies its value by 10. Moving it one place to the right divides its value by 10.</p>
</div>
"""
    },
    {
        "title": "Reading and Writing Numbers Up to 100,000",
        "body": """
<h3>Building Large Numbers</h3>
<p>Now that we understand place value, we can read and write numbers all the way up to 100,000!</p>

<h3>The Ten Thousand Milestone</h3>
<p>The number <strong>10,000</strong> (ten thousand) is our first five-digit number. We write a comma after the ten thousands place to make it easier to read.</p>

<div class="example-box">
<h4>Example: Reading the Number 27,564</h4>
<p><strong>Breaking it down by place value:</strong></p>
<ul>
  <li>2 is in the ten thousands place = 2 times 10,000 = 20,000</li>
  <li>7 is in the thousands place = 7 times 1,000 = 7,000</li>
  <li>5 is in the hundreds place = 5 times 100 = 500</li>
  <li>6 is in the tens place = 6 times 10 = 60</li>
  <li>4 is in the ones place = 4 times 1 = 4</li>
</ul>
<p><strong>We read this as:</strong> Twenty-seven thousand, five hundred sixty-four</p>
<p><strong>In expanded form:</strong> \\(20,000 + 7,000 + 500 + 60 + 4\\)</p>
</div>

<h3>Understanding Commas in Numbers</h3>
<p>We use commas to separate every three digits, starting from the right. This makes numbers easier to read:</p>

<div class="diagram-container">
  <svg width="550" height="150" viewBox="0 0 550 150">
    <text x="275" y="40" text-anchor="middle" font-size="18" font-weight="bold">Number: 92,356</text>

    <line x1="50" y1="80" x2="50" y2="130" stroke="#4169E1" stroke-width="3"/>
    <text x="50" y="65" text-anchor="middle" font-size="14">9</text>
    <text x="50" y="145" text-anchor="middle" font-size="12">ten thousands</text>

    <line x1="90" y1="80" x2="90" y2="130" stroke="#22c55e" stroke-width="3"/>
    <text x="90" y="65" text-anchor="middle" font-size="14">2</text>
    <text x="90" y="145" text-anchor="middle" font-size="12">thousands</text>

    <text x="120" y="90" font-size="20" font-weight="bold">,</text>

    <line x1="150" y1="80" x2="150" y2="130" stroke="#f59e0b" stroke-width="3"/>
    <text x="150" y="65" text-anchor="middle" font-size="14">3</text>
    <text x="150" y="145" text-anchor="middle" font-size="12">hundreds</text>

    <line x1="190" y1="80" x2="190" y2="130" stroke="#ef4444" stroke-width="3"/>
    <text x="190" y="65" text-anchor="middle" font-size="14">5</text>
    <text x="190" y="145" text-anchor="middle" font-size="12">tens</text>

    <line x1="230" y1="80" x2="230" y2="130" stroke="#8b5cf6" stroke-width="3"/>
    <text x="230" y="65" text-anchor="middle" font-size="14">6</text>
    <text x="230" y="145" text-anchor="middle" font-size="12">ones</text>
  </svg>
  <div class="diagram-caption">The comma separates thousands from hundreds</div>
</div>

<div class="success-box">
<h4>Remember: Reading Large Numbers</h4>
<p>To read a number like 92,356: Say the first group of digits before the comma (92 = "ninety-two"), then the word "thousand", then read the remaining digits as you normally would (356 = "three hundred fifty-six"). Result: "Ninety-two thousand, three hundred fifty-six"</p>
</div>

<h3>Common Numbers to Know</h3>
<ul>
  <li><strong>One hundred:</strong> 100</li>
  <li><strong>One thousand:</strong> 1,000</li>
  <li><strong>Ten thousand:</strong> 10,000</li>
  <li><strong>One hundred thousand:</strong> 100,000</li>
</ul>
"""
    },
    {
        "title": "Comparing and Ordering Numbers",
        "body": """
<h3>Which Number is Bigger?</h3>
<p>Now that we can read large numbers, we need to compare them. We use special symbols:</p>

<div class="formula-box">
  <div class="formula-label">Comparison Symbols</div>
  <p>\\( < \\) means "is less than"</p>
  <p>\\( > \\) means "is greater than"</p>
  <p>\\( = \\) means "is equal to"</p>
</div>

<h3>Comparing Strategy: Look Left to Right</h3>
<p>To compare two numbers, we look at the <strong>leftmost digits first</strong>. The number with the larger digit in the highest place value wins.</p>

<div class="example-box">
<h4>Example: Compare 45,230 and 42,890</h4>
<p><strong>Step 1:</strong> Look at the ten thousands place</p>
<p>Both have 4 in the ten thousands place (4 = 4). So they're still tied.</p>
<p><strong>Step 2:</strong> Look at the thousands place</p>
<p>45,230 has 5 in the thousands place</p>
<p>42,890 has 2 in the thousands place</p>
<p>Since 5 > 2, we know that 45,230 > 42,890</p>
<p><strong>We write: 45,230 > 42,890</strong></p>
</div>

<h3>Ordering Numbers from Least to Greatest</h3>
<p>Sometimes we need to arrange several numbers in order. We compare them in pairs and arrange them from smallest to largest.</p>

<div class="example-box">
<h4>Example: Order These Numbers from Least to Greatest</h4>
<p>23,456 | 2,345 | 32,456 | 23,465 | 32,450</p>
<p><strong>Step 1:</strong> Look at how many digits each has</p>
<ul>
  <li>2,345 has 4 digits (smallest)</li>
  <li>The others have 5 digits</li>
</ul>
<p><strong>Step 2:</strong> Among 5-digit numbers, compare by ten thousands place</p>
<ul>
  <li>23,456 and 23,465 start with 23...</li>
  <li>32,456 and 32,450 start with 32...</li>
</ul>
<p><strong>Step 3:</strong> Order the 23,000s by comparing the next digit</p>
<ul>
  <li>23,456 and 23,465 → compare hundreds: both have 4</li>
  <li>Compare tens: 23,456 has 5, and 23,465 has 6 → 23,456 < 23,465</li>
</ul>
<p><strong>Final Answer from Least to Greatest:</strong></p>
<p>2,345 < 23,456 < 23,465 < 32,450 < 32,456</p>
</div>

<div class="concept-box">
<h4>Key Concept: Place Value Comparison</h4>
<p>The most important rule: Always compare starting from the leftmost (highest) place value. The first digit that's different determines which number is larger.</p>
</div>
"""
    },
    {
        "title": "Rounding Numbers to the Nearest Ten, Hundred, and Thousand",
        "body": """
<h3>Why Do We Round?</h3>
<p>Sometimes we don't need an exact number—we just need to know "about how many?" For example, if a store has 47 apples, we might say "about 50" to make the number easier to work with. This is called <strong>rounding</strong>.</p>

<h3>Rounding Using a Number Line</h3>
<p>The easiest way to understand rounding is to use a number line. We find which "round number" our number is closest to.</p>

<div class="diagram-container">
  <svg width="600" height="120" viewBox="0 0 600 120">
    <line x1="20" y1="50" x2="580" y2="50" stroke="#333" stroke-width="2"/>
    <circle cx="20" cy="50" r="5" fill="#4169E1" stroke="#4169E1" stroke-width="2"/>
    <text x="20" y="75" text-anchor="middle" font-size="14" font-weight="bold">40</text>

    <circle cx="140" cy="50" r="5" fill="#cccccc"/>
    <text x="140" y="75" text-anchor="middle" font-size="12">45</text>

    <circle cx="300" cy="50" r="8" fill="#f59e0b" stroke="#f59e0b" stroke-width="2"/>
    <text x="300" y="75" text-anchor="middle" font-size="14" font-weight="bold">47</text>
    <text x="300" y="35" text-anchor="middle" font-size="12" fill="#f59e0b">This is our number</text>

    <circle cx="460" cy="50" r="5" fill="#cccccc"/>
    <text x="460" y="75" text-anchor="middle" font-size="12">55</text>

    <circle cx="580" cy="50" r="5" fill="#22c55e" stroke="#22c55e" stroke-width="2"/>
    <text x="580" y="75" text-anchor="middle" font-size="14" font-weight="bold">60</text>

    <line x1="20" y1="45" x2="20" y2="55" stroke="#4169E1" stroke-width="2"/>
    <line x1="580" y1="45" x2="580" y2="55" stroke="#22c55e" stroke-width="2"/>
  </svg>
  <div class="diagram-caption">47 is closer to 50 than to 40, so 47 rounds to 50</div>
</div>

<h3>The Rounding Rule</h3>
<p>Here's the simple rule to round any number:</p>

<div class="steps-container">
  <div class="step-item">
    <div class="step-num">1</div>
    <div class="step-content">
      <p><strong>Find the place value you're rounding to.</strong> For example, if you're rounding to the nearest ten, find the tens digit.</p>
    </div>
  </div>
  <div class="step-item">
    <div class="step-num">2</div>
    <div class="step-content">
      <p><strong>Look at the digit to the right of that place.</strong> This is the "helper digit."</p>
    </div>
  </div>
  <div class="step-item">
    <div class="step-num">3</div>
    <div class="step-content">
      <p><strong>If the helper digit is 5 or more, round UP.</strong> If it's 4 or less, round DOWN.</p>
    </div>
  </div>
  <div class="step-item">
    <div class="step-num">4</div>
    <div class="step-content">
      <p><strong>Change all digits to the right to zeros.</strong></p>
    </div>
  </div>
</div>

<h3>Rounding Examples</h3>

<div class="example-box">
<h4>Example 1: Round 47 to the Nearest Ten</h4>
<p><strong>Step 1:</strong> The tens place has 4</p>
<p><strong>Step 2:</strong> The helper digit (ones place) is 7</p>
<p><strong>Step 3:</strong> Since 7 ≥ 5, we round UP</p>
<p><strong>Answer:</strong> 47 rounds to <strong>50</strong></p>
</div>

<div class="example-box">
<h4>Example 2: Round 23,456 to the Nearest Hundred</h4>
<p><strong>Step 1:</strong> The hundreds place has 4</p>
<p><strong>Step 2:</strong> The helper digit (tens place) is 5</p>
<p><strong>Step 3:</strong> Since 5 ≥ 5, we round UP</p>
<p><strong>Answer:</strong> 23,456 rounds to <strong>23,500</strong></p>
</div>

<div class="example-box">
<h4>Example 3: Round 58,723 to the Nearest Thousand</h4>
<p><strong>Step 1:</strong> The thousands place has 8</p>
<p><strong>Step 2:</strong> The helper digit (hundreds place) is 7</p>
<p><strong>Step 3:</strong> Since 7 ≥ 5, we round UP</p>
<p><strong>Answer:</strong> 58,723 rounds to <strong>59,000</strong></p>
</div>

<div class="warning-box">
<h4>Common Mistake: The Magic Number 5</h4>
<p>Remember: When the helper digit is exactly 5, you ALWAYS round UP, not down. This might feel strange, but it's the mathematical rule.</p>
</div>
"""
    },
    {
        "title": "Counting in Ones, Tens, Hundreds, and Thousands",
        "body": """
<h3>Skip Counting Builds Fluency</h3>
<p>Being able to count by different amounts helps us understand how place value works and prepares us for multiplication and division.</p>

<h3>Counting by Tens</h3>
<p>When we count by tens, we add 10 each time. Listen to the pattern of the tens digit:</p>

<p><strong>0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, ...</strong></p>

<p>Notice how the tens digit goes: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2... It's a repeating pattern!</p>

<div class="diagram-container">
  <svg width="650" height="120" viewBox="0 0 650 120">
    <text x="325" y="25" text-anchor="middle" font-size="16" font-weight="bold">Counting by Tens: Look at the Pattern</text>
    <g id="tens">
      <rect x="10" y="50" width="30" height="50" fill="#4169E180" stroke="#4169E1" stroke-width="2"/>
      <text x="25" y="85" text-anchor="middle" font-size="14" font-weight="bold">0</text>

      <rect x="50" y="50" width="30" height="50" fill="#4169E180" stroke="#4169E1" stroke-width="2"/>
      <text x="65" y="85" text-anchor="middle" font-size="14" font-weight="bold">10</text>

      <rect x="90" y="50" width="30" height="50" fill="#4169E180" stroke="#4169E1" stroke-width="2"/>
      <text x="105" y="85" text-anchor="middle" font-size="14" font-weight="bold">20</text>

      <rect x="130" y="50" width="30" height="50" fill="#4169E180" stroke="#4169E1" stroke-width="2"/>
      <text x="145" y="85" text-anchor="middle" font-size="14" font-weight="bold">30</text>

      <rect x="170" y="50" width="30" height="50" fill="#4169E180" stroke="#4169E1" stroke-width="2"/>
      <text x="185" y="85" text-anchor="middle" font-size="14" font-weight="bold">40</text>

      <rect x="210" y="50" width="30" height="50" fill="#4169E180" stroke="#4169E1" stroke-width="2"/>
      <text x="225" y="85" text-anchor="middle" font-size="14" font-weight="bold">50</text>
    </g>
  </svg>
  <div class="diagram-caption">Each number is 10 more than the previous one</div>
</div>

<h3>Counting by Hundreds</h3>
<p>When we count by hundreds, we add 100 each time:</p>

<p><strong>0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, ...</strong></p>

<p>The pattern is even simpler here. The hundreds digit counts: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1...</p>

<h3>Counting by Thousands</h3>
<p>When we count by thousands, we add 1,000 each time:</p>

<p><strong>0, 1,000, 2,000, 3,000, 4,000, 5,000, ..., 50,000, ..., 100,000</strong></p>

<div class="interactive-widget">
  <h4>Practice: Skip Counting</h4>
  <p>Which number comes next?</p>
  <p><strong>5,000, 6,000, 7,000, _____?</strong></p>
  <p>Answer: <span style="color: #4169E1; font-weight: bold;">8,000</span> (we add 1,000 each time)</p>
</div>

<h3>Using Skip Counting for Estimation</h3>
<p>Skip counting helps us quickly estimate totals. For example:</p>
<ul>
  <li>If you count by tens to 90, you're counting 9 groups of 10 items</li>
  <li>If you count by hundreds to 500, you're counting 5 groups of 100 items</li>
</ul>

<div class="success-box">
<h4>Remember: The Power of Patterns</h4>
<p>Skip counting isn't just a fun exercise—it shows us that numbers follow patterns. These patterns make it easier to add, subtract, multiply, and divide.</p>
</div>
"""
    },
    {
        "title": "Real-World Applications of Large Numbers",
        "body": """
<h3>Where Do We Use Large Numbers?</h3>
<p>Numbers up to 100,000 appear in real life all the time. Understanding them helps us make sense of our world.</p>

<h3>Example 1: Population of Cities</h3>
<p>A city might have 45,000 people living in it. To understand what this means:</p>
<ul>
  <li>45,000 = 45 thousand</li>
  <li>That's like if you had 45 groups of 1,000 people each</li>
  <li>It's between 40,000 and 50,000</li>
</ul>

<div class="diagram-container">
  <svg width="600" height="200" viewBox="0 0 600 200">
    <text x="300" y="25" text-anchor="middle" font-size="16" font-weight="bold">City Population Comparison</text>

    <rect x="50" y="50" width="150" height="120" fill="#4169E180" stroke="#4169E1" stroke-width="2"/>
    <text x="125" y="120" text-anchor="middle" font-size="14" font-weight="bold">Small Town</text>
    <text x="125" y="145" text-anchor="middle" font-size="12">12,000 people</text>

    <rect x="250" y="30" width="150" height="140" fill="#22c55e80" stroke="#22c55e" stroke-width="2"/>
    <text x="325" y="110" text-anchor="middle" font-size="14" font-weight="bold">Medium City</text>
    <text x="325" y="135" text-anchor="middle" font-size="12">45,000 people</text>

    <rect x="450" y="10" width="150" height="160" fill="#f59e0b80" stroke="#f59e0b" stroke-width="2"/>
    <text x="525" y="100" text-anchor="middle" font-size="14" font-weight="bold">Large City</text>
    <text x="525" y="125" text-anchor="middle" font-size="12">87,000 people</text>
  </svg>
  <div class="diagram-caption">Taller bars represent larger populations</div>
</div>

<h3>Example 2: Money and Savings</h3>
<p>Imagine you're saving money for something special. Large numbers help you set goals:</p>

<div class="example-box">
<h4>Example: Saving for a Computer</h4>
<p>A computer costs 85,000 dollars. Your family has saved 32,500 dollars so far.</p>
<p>How much more do they need? 85,000 - 32,500 = 52,500 dollars</p>
<p>To understand this: They've saved almost 33 thousand dollars, and the computer costs almost 85 thousand.</p>
</div>

<h3>Example 3: Distance and Travel</h3>
<p>Distances are often expressed using large numbers:</p>
<ul>
  <li>The distance from one city to another might be 67,000 meters</li>
  <li>A road might be 45,000 meters long</li>
  <li>An airplane trip might be 92,000 meters high</li>
</ul>

<h3>Example 4: School and Sports Records</h3>
<p>Large numbers show us records and achievements:</p>
<ul>
  <li>A popular soccer stadium might hold 72,000 fans</li>
  <li>A big video game might have been downloaded by 156,000 people in a week</li>
  <li>A school district might have 45,000 students</li>
</ul>

<div class="concept-box">
<h4>Key Concept: Numbers in Context</h4>
<p>Understanding large numbers helps us understand the world. When we read that a city has 87,000 people or a computer costs 52,000 dollars, we need to be able to picture what those numbers mean and compare them to other numbers.</p>
</div>

<div class="success-box">
<h4>Remember: Practice Reading Large Numbers Everywhere</h4>
<p>Start noticing large numbers in your world—on signs, in news stories, on billboards, in sports. This real-world practice makes learning numbers meaningful and fun!</p>
</div>
"""
    }
]
