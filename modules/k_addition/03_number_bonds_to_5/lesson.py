"""Concept 3: Number Bonds to 5 — All Ways to Make 5."""

TITLE = "Number Bonds to 5: All the Ways to Make 5"

SECTIONS = [
    {
        "title": "What is a Number Bond?",
        "body": """<h3>A Special Way to Show Addition</h3>
<p>A <strong>number bond</strong> shows us that one number can be broken into two smaller parts.
It also shows us that two smaller parts can combine to make one bigger number.</p>

<div class="concept-box">
  <h4>Number Bond Idea</h4>
  <p>A number bond is a diagram with three circles:
  <ul style="margin-top: 10px;">
    <li><strong>Top circle:</strong> The total (the big number)</li>
    <li><strong>Bottom left circle:</strong> First part</li>
    <li><strong>Bottom right circle:</strong> Second part</li>
  </ul>
  </p>
</div>

<h3>Why Learn Number Bonds?</h3>
<p>When you know all the ways to make a number, you:</p>
<ul>
  <li>Add faster because you memorize the facts</li>
  <li>Understand that numbers can break apart and come back together</li>
  <li>Get ready for subtraction (if you know \(3 + 2 = 5\), then \(5 - 3 = 2\))</li>
</ul>"""
    },

    {
        "title": "All the Number Bonds for 5",
        "body": """<h3>Every Way to Make 5</h3>
<p>There are exactly 6 different ways to add two numbers and get 5:</p>

<svg viewBox="0 0 540 360" style="width: 100%; max-width: 560px; height: auto; display: block; margin: 20px auto;">
  <!-- Header -->
  <text x="270" y="22" text-anchor='middle' font-size='18' font-weight='bold' fill='currentColor'>All Number Bonds for 5</text>

  <!-- Row 1: 0+5, 1+4, 2+3 — evenly at x=90, 270, 450 -->
  <!-- 0 + 5 -->
  <circle cx="90" cy="75" r="20" fill='#4169E1' stroke='#8b949e' stroke-width="2"/>
  <text x="90" y="82" text-anchor='middle' fill='white' font-size='16' font-weight='bold'>5</text>
  <line x1="78" y1="93" x2="58" y2="110" stroke='#8b949e' stroke-width="2"/>
  <line x1="102" y1="93" x2="122" y2="110" stroke='#8b949e' stroke-width="2"/>
  <circle cx="50" cy="125" r="16" fill='#22c55e' stroke='#8b949e' stroke-width="2"/>
  <text x="50" y="131" text-anchor='middle' fill='white' font-size='14' font-weight='bold'>0</text>
  <circle cx="130" cy="125" r="16" fill='#f59e0b' stroke='#8b949e' stroke-width="2"/>
  <text x="130" y="131" text-anchor='middle' fill='white' font-size='14' font-weight='bold'>5</text>
  <text x="90" y="158" text-anchor='middle' font-size='12' fill='currentColor'>0 + 5 = 5</text>

  <!-- 1 + 4 -->
  <circle cx="270" cy="75" r="20" fill='#4169E1' stroke='#8b949e' stroke-width="2"/>
  <text x="270" y="82" text-anchor='middle' fill='white' font-size='16' font-weight='bold'>5</text>
  <line x1="258" y1="93" x2="238" y2="110" stroke='#8b949e' stroke-width="2"/>
  <line x1="282" y1="93" x2="302" y2="110" stroke='#8b949e' stroke-width="2"/>
  <circle cx="230" cy="125" r="16" fill='#22c55e' stroke='#8b949e' stroke-width="2"/>
  <text x="230" y="131" text-anchor='middle' fill='white' font-size='14' font-weight='bold'>1</text>
  <circle cx="310" cy="125" r="16" fill='#f59e0b' stroke='#8b949e' stroke-width="2"/>
  <text x="310" y="131" text-anchor='middle' fill='white' font-size='14' font-weight='bold'>4</text>
  <text x="270" y="158" text-anchor='middle' font-size='12' fill='currentColor'>1 + 4 = 5</text>

  <!-- 2 + 3 -->
  <circle cx="450" cy="75" r="20" fill='#4169E1' stroke='#8b949e' stroke-width="2"/>
  <text x="450" y="82" text-anchor='middle' fill='white' font-size='16' font-weight='bold'>5</text>
  <line x1="438" y1="93" x2="418" y2="110" stroke='#8b949e' stroke-width="2"/>
  <line x1="462" y1="93" x2="482" y2="110" stroke='#8b949e' stroke-width="2"/>
  <circle cx="410" cy="125" r="16" fill='#22c55e' stroke='#8b949e' stroke-width="2"/>
  <text x="410" y="131" text-anchor='middle' fill='white' font-size='14' font-weight='bold'>2</text>
  <circle cx="490" cy="125" r="16" fill='#f59e0b' stroke='#8b949e' stroke-width="2"/>
  <text x="490" y="131" text-anchor='middle' fill='white' font-size='14' font-weight='bold'>3</text>
  <text x="450" y="158" text-anchor='middle' font-size='12' fill='currentColor'>2 + 3 = 5</text>

  <!-- Row 2: 3+2, 4+1, 5+0 — evenly at x=90, 270, 450 -->
  <!-- 3 + 2 -->
  <circle cx="90" cy="220" r="20" fill='#4169E1' stroke='#8b949e' stroke-width="2"/>
  <text x="90" y="227" text-anchor='middle' fill='white' font-size='16' font-weight='bold'>5</text>
  <line x1="78" y1="238" x2="58" y2="255" stroke='#8b949e' stroke-width="2"/>
  <line x1="102" y1="238" x2="122" y2="255" stroke='#8b949e' stroke-width="2"/>
  <circle cx="50" cy="270" r="16" fill='#22c55e' stroke='#8b949e' stroke-width="2"/>
  <text x="50" y="276" text-anchor='middle' fill='white' font-size='14' font-weight='bold'>3</text>
  <circle cx="130" cy="270" r="16" fill='#f59e0b' stroke='#8b949e' stroke-width="2"/>
  <text x="130" y="276" text-anchor='middle' fill='white' font-size='14' font-weight='bold'>2</text>
  <text x="90" y="303" text-anchor='middle' font-size='12' fill='currentColor'>3 + 2 = 5</text>

  <!-- 4 + 1 -->
  <circle cx="270" cy="220" r="20" fill='#4169E1' stroke='#8b949e' stroke-width="2"/>
  <text x="270" y="227" text-anchor='middle' fill='white' font-size='16' font-weight='bold'>5</text>
  <line x1="258" y1="238" x2="238" y2="255" stroke='#8b949e' stroke-width="2"/>
  <line x1="282" y1="238" x2="302" y2="255" stroke='#8b949e' stroke-width="2"/>
  <circle cx="230" cy="270" r="16" fill='#22c55e' stroke='#8b949e' stroke-width="2"/>
  <text x="230" y="276" text-anchor='middle' fill='white' font-size='14' font-weight='bold'>4</text>
  <circle cx="310" cy="270" r="16" fill='#f59e0b' stroke='#8b949e' stroke-width="2"/>
  <text x="310" y="276" text-anchor='middle' fill='white' font-size='14' font-weight='bold'>1</text>
  <text x="270" y="303" text-anchor='middle' font-size='12' fill='currentColor'>4 + 1 = 5</text>

  <!-- 5 + 0 -->
  <circle cx="450" cy="220" r="20" fill='#4169E1' stroke='#8b949e' stroke-width="2"/>
  <text x="450" y="227" text-anchor='middle' fill='white' font-size='16' font-weight='bold'>5</text>
  <line x1="438" y1="238" x2="418" y2="255" stroke='#8b949e' stroke-width="2"/>
  <line x1="462" y1="238" x2="482" y2="255" stroke='#8b949e' stroke-width="2"/>
  <circle cx="410" cy="270" r="16" fill='#22c55e' stroke='#8b949e' stroke-width="2"/>
  <text x="410" y="276" text-anchor='middle' fill='white' font-size='14' font-weight='bold'>5</text>
  <circle cx="490" cy="270" r="16" fill='#f59e0b' stroke='#8b949e' stroke-width="2"/>
  <text x="490" y="276" text-anchor='middle' fill='white' font-size='14' font-weight='bold'>0</text>
  <text x="450" y="303" text-anchor='middle' font-size='12' fill='currentColor'>5 + 0 = 5</text>
</svg>

<h3>See the Pattern?</h3>
<p>Look at the pairs carefully:</p>
<ul>
  <li><strong>\(0 + 5\)</strong> and <strong>\(5 + 0\)</strong> — both equal 5</li>
  <li><strong>\(1 + 4\)</strong> and <strong>\(4 + 1\)</strong> — both equal 5</li>
  <li><strong>\(2 + 3\)</strong> and <strong>\(3 + 2\)</strong> — both equal 5</li>
</ul>

<div class="success-box">
  <h4>✨ Interesting Discovery</h4>
  <p>It doesn't matter which order you add! <strong>\(2 + 3\)</strong> equals <strong>\(3 + 2\)</strong>.
  This is called <strong>commutativity</strong> (don't worry about the big word — it just means order doesn't matter).</p>
</div>"""
    },

    {
        "title": "Seeing Number Bonds Visually",
        "body": """<h3>Drawing Number Bonds with Objects</h3>
<p>Let's see the number bond \(5 = 2 + 3\) with actual objects:</p>

<div class="formula-box">
  <p style="font-size: 18px; margin-bottom: 15px;"><strong>The Total: 5 Apples</strong></p>
  <p style="font-size: 24px; margin-bottom: 20px;">🍎🍎🍎🍎🍎</p>

  <p style="font-size: 16px; margin-top: 15px">Split them into two groups:</p>

  <p style="font-size: 18px; margin-top: 15px;"><strong>Part 1: 2 apples</strong></p>
  <p style="font-size: 24px; margin: 10px 0;">🍎🍎</p>

  <p style="font-size: 18px; margin-top: 15px;"><strong>Part 2: 3 apples</strong></p>
  <p style="font-size: 24px; margin: 10px 0;">🍎🍎🍎</p>

  <p style="font-size: 16px; margin-top: 15px">The number bond shows:</p>
  <p style="font-size: 18px; margin-top: 10px; font-weight: bold;">\(5 = 2 + 3\)</p>
</div>

<h3>Number Bond Chart</h3>
<p>Here's a table showing all number bonds to 5:</p>

<canvas id="bondChart5" data-chart='{"type":"bar","data":{"labels":["0+5","1+4","2+3","3+2","4+1","5+0"],"datasets":[{"label":"Different ways to make 5","data":[5,5,5,5,5,5],"backgroundColor":["#4f8ef7","#4f8ef7","#4f8ef7","#4f8ef7","#4f8ef7","#4f8ef7"]}]},"options":{"indexAxis":"x","plugins":{"title":{"display":true,"text":"All Ways to Make 5 (all equal 5)"},"legend":{"display":true}},"scales":{"y":{"max":6,"title":{"display":true,"text":"Sum"}}}}}' height="250"></canvas>"""
    },

    {
        "title": "Practice with Number Bonds to 5",
        "body": """<h3>Match the Number Bonds</h3>
<div class="mcq-group">
  <p><strong>If the total is 5 and one part is 2, what is the other part?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="Try drawing 5 circles and removing 2. How many are left?">4</button>
    <button class="mcq-option" data-correct="true" data-explanation="\(5 = 2 + 3\). The two parts are 2 and 3.">3</button>
    <button class="mcq-option" data-correct="false" data-explanation="That's too many. 2 and 4 would make 6, not 5.">4</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="mcq-group" style="margin-top: 20px;">
  <p><strong>Complete this number bond: \(5 = 1 + ?\)</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="1 and 3 makes 4, not 5. Count on your fingers!">3</button>
    <button class="mcq-option" data-correct="true" data-explanation="\(1 + 4 = 5\). The parts are 1 and 4.">4</button>
    <button class="mcq-option" data-correct="false" data-explanation="1 and 5 makes 6. That's too many.">5</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<h3>Write Your Own Number Bonds</h3>
<p>Try to write the missing part:</p>
<div style="padding: 15px; border-radius: 8px; margin: 15px 0;">
  <p>\(5 = 4 + ?\)</p>
  <p style="margin-top: 10px; font-size: 14px">Hint: Start at 4 and count: 5. How many did you count on?</p>
  <p style="margin-top: 10px;"><strong>Answer: \(5 = 4 + 1\)</strong></p>
</div>"""
    }
]
