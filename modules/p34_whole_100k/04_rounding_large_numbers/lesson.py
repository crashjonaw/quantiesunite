TITLE = "Rounding Large Numbers"
SECTIONS = [
    {
        "title": "Why Round? When We Need Approximate Values",
        "body": """
<h3>The Purpose of Rounding</h3>
<p>Sometimes we don't need an exact number. We just need to know "about how many?" For example:</p>
<ul>
  <li>If a city has 47,328 people, we might say "about 47,000" or "about 47,300"</li>
  <li>If a project costs $23,567, we might say "about $23,600" or "about $24,000"</li>
  <li>If attendance was 82,451, we might report "about 82,000"</li>
</ul>

<p>Rounding makes numbers easier to use and remember, while staying close to the true value.</p>

<h3>Rounding Using a Number Line</h3>
<p>The easiest way to understand rounding is with a number line. We find which "round number" our number is closest to.</p>

<div class="diagram-container">
  <svg width="620" height="120" viewBox="-10 0 620 120">
    <line x1="20" y1="50" x2="580" y2="50" stroke='#8b949e' stroke-width="2"/>
    <circle cx="20" cy="50" r="5" fill='#4169E1' stroke='#4169E1' stroke-width="2"/>
    <text x="20" y="75" text-anchor='middle' font-size='14' font-weight='bold'>40,000</text>

    <circle cx="140" cy="50" r="5" fill='#cccccc'/>
    <text x="140" y="75" text-anchor='middle' font-size='12'>45,000</text>

    <circle cx="300" cy="50" r="8" fill='#f59e0b' stroke='#f59e0b' stroke-width="2"/>
    <text x="300" y="75" text-anchor='middle' font-size='14' font-weight='bold'>47,328</text>
    <text x="300" y="35" text-anchor='middle' font-size='11' fill='#f59e0b'>Our number</text>

    <circle cx="460" cy="50" r="5" fill='#cccccc'/>
    <text x="460" y="75" text-anchor='middle' font-size='12'>50,000</text>

    <circle cx="580" cy="50" r="5" fill='#22c55e' stroke='#22c55e' stroke-width="2"/>
    <text x="580" y="75" text-anchor='middle' font-size='14' font-weight='bold'>60,000</text>

    <line x1="20" y1="45" x2="20" y2="55" stroke='#4169E1' stroke-width="2"/>
    <line x1="580" y1="45" x2="580" y2="55" stroke='#22c55e' stroke-width="2"/>
  </svg>
  <div class="diagram-caption">47,328 is closer to 50,000 than to 40,000</div>
</div>

<div class="success-box">
<p>Notice: 47,328 is much closer to 50,000, so it rounds to 50,000.</p>
</div>
"""
    },
    {
        "title": "The Rounding Rule: A Simple Formula",
        "body": """
<h3>Four Steps to Round Any Number</h3>

<div class="steps-container" style="margin: 20px auto;">
  <div class="step-item" style="background: #f0f9ff; padding: 15px; margin: 10px 0; border-radius: 8px">
    <div style="font-weight: bold; font-size: 14px">Step 1: Find the place value you're rounding to</div>
    <p>Are you rounding to the nearest ten, hundred, thousand, or ten thousand? Find that digit and underline it.</p>
  </div>

  <div class="step-item" style="background: #f0fff0; padding: 15px; margin: 10px 0; border-radius: 8px; border-left: 4px solid #22c55e;">
    <div style="font-weight: bold; font-size: 14px; color: var(--success);">Step 2: Look at the digit to the right</div>
    <p>This is the "helper digit." It tells us whether to round up or down.</p>
  </div>

  <div class="step-item formula-box">
    <div style="font-weight: bold; font-size: 14px; color: #f59e0b;">Step 3: Apply the magic rule</div>
    <p>If the helper digit is 5 or more (5, 6, 7, 8, 9) → round UP<br>If the helper digit is 4 or less (0, 1, 2, 3, 4) → round DOWN</p>
  </div>

  <div class="step-item" style="background: #fef2f2; padding: 15px; margin: 10px 0; border-radius: 8px; border-left: 4px solid #ef4444;">
    <div style="font-weight: bold; font-size: 14px; color: #ef4444;">Step 4: Change everything to the right to zero</div>
    <p>All digits to the right of your place become 0.</p>
  </div>
</div>

<div class="warning-box">
<h4>Remember: The Magic Number 5</h4>
<p>When the helper digit is exactly 5, you ALWAYS round UP. This is the rule mathematicians use, and it keeps numbers balanced.</p>
</div>
"""
    },
    {
        "title": "Rounding Examples with Large Numbers",
        "body": """
<h3>Example 1: Round to the Nearest Hundred</h3>

<div class="example-box">
<h4>Round 23,456 to the Nearest Hundred</h4>

<p><strong>Step 1:</strong> Find the hundreds place → 4 (in the position before 56)</p>
<p><strong>Step 2:</strong> Look at the helper digit (tens place) → 5</p>
<p><strong>Step 3:</strong> Since \\(5 \\geq 5\\), round UP</p>
<p><strong>Step 4:</strong> Change everything to the right to zero</p>

<p style="text-align: center; font-size: 15px; margin-top: 10px;"><strong>23,456 rounds to 23,500</strong></p>
</div>

<h3>Example 2: Round to the Nearest Thousand</h3>

<div class="example-box">
<h4>Round 58,723 to the Nearest Thousand</h4>

<p><strong>Step 1:</strong> Find the thousands place → 8</p>
<p><strong>Step 2:</strong> Look at the helper digit (hundreds place) → 7</p>
<p><strong>Step 3:</strong> Since \\(7 \\geq 5\\), round UP</p>
<p><strong>Step 4:</strong> The 8 becomes 9, everything to the right becomes 0</p>

<p style="text-align: center; font-size: 15px; margin-top: 10px;"><strong>58,723 rounds to 59,000</strong></p>
</div>

<h3>Example 3: Round to the Nearest Ten Thousand</h3>

<div class="example-box">
<h4>Round 34,678 to the Nearest Ten Thousand</h4>

<p><strong>Step 1:</strong> Find the ten thousands place → 3</p>
<p><strong>Step 2:</strong> Look at the helper digit (thousands place) → 4</p>
<p><strong>Step 3:</strong> Since \\(4 < 5\\), round DOWN</p>
<p><strong>Step 4:</strong> The 3 stays 3, everything to the right becomes 0</p>

<p style="text-align: center; font-size: 15px; margin-top: 10px;"><strong>34,678 rounds to 30,000</strong></p>
</div>

<h3>Example 4: Rounding Up Past a Boundary</h3>

<div class="example-box">
<h4>Round 49,821 to the Nearest Ten Thousand</h4>

<p><strong>Step 1:</strong> Find the ten thousands place → 4</p>
<p><strong>Step 2:</strong> Look at the helper digit (thousands place) → 9</p>
<p><strong>Step 3:</strong> Since \\(9 \\geq 5\\), round UP</p>
<p><strong>Step 4:</strong> The 4 becomes 5, everything to the right becomes 0</p>

<p style="text-align: center; font-size: 15px; margin-top: 10px;"><strong>49,821 rounds to 50,000</strong></p>

<p style="color: #f59e0b; font-weight: bold; margin-top: 10px;">Notice: We crossed from the 40,000s to the 50,000s!</p>
</div>
"""
    },
    {
        "title": "Real-World Rounding: Using Approximations",
        "body": """
<h3>Why We Round in Real Life</h3>
<p>Rounding happens all around us. Here's where you'll see it:</p>

<h3>Example 1: Population Reports</h3>
<p>A news report says: "The city population is approximately 87,000 people"</p>
<p>The actual population might be 87,453, but 87,000 is easier to say and remember.</p>

<h3>Example 2: Money and Budgets</h3>
<p>Your school might say: "We spent about $45,000 on textbooks"</p>
<p>The real amount was $45,623, but rounding to the nearest thousand makes it simpler.</p>

<h3>Example 3: Attendance at Events</h3>
<p>A stadium report: "The concert had approximately 35,000 fans"</p>
<p>Real count: 35,427. Rounding helps fans get a quick sense of how full it was.</p>

<h3>Example 4: Distance and Measurement</h3>
<p>A sign might say: "Next city is about 67,000 meters away"</p>
<p>Exact: 67,234 meters. Rounded: 67,000 meters for easier reading.</p>

<div class="success-box">
<h4>Key Takeaway: When to Round</h4>
<p>Round when you want an approximate answer that's easier to work with. Rounding helps us communicate big numbers quickly and clearly, even if we lose a tiny bit of precision.</p>
</div>
"""
    }
]
