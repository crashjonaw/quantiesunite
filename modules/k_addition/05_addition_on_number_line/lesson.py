"""Concept 5: Addition on the Number Line — Jumping and Moving."""

TITLE = "Addition on the Number Line: Jumping Forward"

SECTIONS = [
    {
        "title": "What is a Number Line?",
        "body": """<h3>A Line of Numbers</h3>
<p>A <strong>number line</strong> is a straight line with numbers written in order, from left (small) to right (big).</p>

<svg viewBox="0 0 450 80" style="width: 100%; max-width: 500px; height: auto; display: block; margin: 20px auto;">
  <!-- Main line -->
  <line x1="20" y1="40" x2="430" y2="40" stroke='#4169E1' stroke-width="3"/>

  <!-- Tick marks and numbers -->
  <g font-size='14' text-anchor='middle'>
    <line x1="20" y1="35" x2="20" y2="45" stroke='#4169E1' stroke-width="2"/>
    <text x="20" y="60" fill='currentColor'>0</text>

    <line x1="70" y1="35" x2="70" y2="45" stroke='#4169E1' stroke-width="2"/>
    <text x="70" y="60" fill='currentColor'>1</text>

    <line x1="120" y1="35" x2="120" y2="45" stroke='#4169E1' stroke-width="2"/>
    <text x="120" y="60" fill='currentColor'>2</text>

    <line x1="170" y1="35" x2="170" y2="45" stroke='#4169E1' stroke-width="2"/>
    <text x="170" y="60" fill='currentColor'>3</text>

    <line x1="220" y1="35" x2="220" y2="45" stroke='#4169E1' stroke-width="2"/>
    <text x="220" y="60" fill='currentColor'>4</text>

    <line x1="270" y1="35" x2="270" y2="45" stroke='#4169E1' stroke-width="2"/>
    <text x="270" y="60" fill='currentColor'>5</text>

    <line x1="320" y1="35" x2="320" y2="45" stroke='#4169E1' stroke-width="2"/>
    <text x="320" y="60" fill='currentColor'>6</text>

    <line x1="370" y1="35" x2="370" y2="45" stroke='#4169E1' stroke-width="2"/>
    <text x="370" y="60" fill='currentColor'>7</text>

    <line x1="420" y1="35" x2="420" y2="45" stroke='#4169E1' stroke-width="2"/>
    <text x="420" y="60" fill='currentColor'>8</text>
  </g>
</svg>

<h3>Why Use a Number Line for Addition?</h3>
<p>A number line helps because:</p>
<ul>
  <li>You can <strong>see</strong> the addition happening as movement</li>
  <li>It connects counting to addition (each jump = one count)</li>
  <li>It shows that addition moves toward bigger numbers</li>
  <li>It works for <em>any</em> numbers, big or small</li>
</ul>

<div class="concept-box">
  <h4>The Key Idea</h4>
  <p><strong>Addition on a number line means jumping forward (to the right) from your starting number.</strong></p>
</div>"""
    },

    {
        "title": "How to Add on a Number Line",
        "body": """<h3>Step-by-Step: Adding 3 + 2</h3>

<div class="formula-box">
  <p style="font-size: 16px; margin-bottom: 15px;"><strong>Step 1: Find your starting number (3) on the line.</strong></p>

  <svg viewBox="0 0 450 100" style="width: 100%; max-width: 500px; height: auto; display: block; margin: 10px 0;">
    <line x1="20" y1="50" x2="430" y2="50" stroke='#4169E1' stroke-width="3"/>
    <g font-size='14' text-anchor='middle'>
      <line x1="20" y1="45" x2="20" y2="55" stroke='#4169E1' stroke-width="2"/>
      <text x="20" y="70" fill='currentColor'>0</text>
      <line x1="70" y1="45" x2="70" y2="55" stroke='#4169E1' stroke-width="2"/>
      <text x="70" y="70" fill='currentColor'>1</text>
      <line x1="120" y1="45" x2="120" y2="55" stroke='#4169E1' stroke-width="2"/>
      <text x="120" y="70" fill='currentColor'>2</text>
      <line x1="170" y1="45" x2="170" y2="55" stroke='#4169E1' stroke-width="2"/>
      <text x="170" y="70" fill='currentColor'>3</text>
      <line x1="220" y1="45" x2="220" y2="55" stroke='#4169E1' stroke-width="2"/>
      <text x="220" y="70" fill='currentColor'>4</text>
      <line x1="270" y1="45" x2="270" y2="55" stroke='#4169E1' stroke-width="2"/>
      <text x="270" y="70" fill='currentColor'>5</text>
    </g>
    <circle cx="170" cy="50" r="8" fill='#22c55e' stroke='#8b949e' stroke-width="2"/>
    <text x="170" y="25" text-anchor='middle' font-size='12' font-weight='bold'>Start here: 3</text>
  </svg>

  <p style="font-size: 16px; margin-top: 15px; margin-bottom: 15px;"><strong>Step 2: Jump forward 2 steps (because we're adding 2).</strong></p>

  <svg viewBox="0 0 450 120" style="width: 100%; max-width: 500px; height: auto; display: block; margin: 10px 0;">
    <line x1="20" y1="60" x2="430" y2="60" stroke='#4169E1' stroke-width="3"/>
    <g font-size='14' text-anchor='middle'>
      <line x1="20" y1="55" x2="20" y2="65" stroke='#4169E1' stroke-width="2"/>
      <text x="20" y="80" fill='currentColor'>0</text>
      <line x1="70" y1="55" x2="70" y2="65" stroke='#4169E1' stroke-width="2"/>
      <text x="70" y="80" fill='currentColor'>1</text>
      <line x1="120" y1="55" x2="120" y2="65" stroke='#4169E1' stroke-width="2"/>
      <text x="120" y="80" fill='currentColor'>2</text>
      <line x1="170" y1="55" x2="170" y2="65" stroke='#4169E1' stroke-width="2"/>
      <text x="170" y="80" fill='currentColor'>3</text>
      <line x1="220" y1="55" x2="220" y2="65" stroke='#4169E1' stroke-width="2"/>
      <text x="220" y="80" fill='currentColor'>4</text>
      <line x1="270" y1="55" x2="270" y2="65" stroke='#4169E1' stroke-width="2"/>
      <text x="270" y="80" fill='currentColor'>5</text>
    </g>
    <circle cx="170" cy="60" r="8" fill='#22c55e' stroke='#8b949e' stroke-width="2"/>
    <circle cx="270" cy="60" r="8" fill='#f59e0b' stroke='#8b949e' stroke-width="2"/>
    <path d="M 180 30 L 210 30 L 210 20" stroke='#ef4444' stroke-width="2" fill='none'/>
    <path d="M 220 30 L 250 30 L 250 20" stroke='#ef4444' stroke-width="2" fill='none'/>
    <text x="200" y="18" text-anchor='middle' font-size='12' fill='#ef4444'>+1</text>
    <text x="240" y="18" text-anchor='middle' font-size='12' fill='#ef4444'>+1</text>
  </svg>

  <p style="font-size: 16px; margin-top: 15px; margin-bottom: 15px;"><strong>Step 3: See where you land (5). That's your answer!</strong></p>

  <p style="text-align: center; font-size: 18px; margin-top: 10px; font-weight: bold;">3 + 2 = 5 ✓</p>
</div>

<h3>More Examples on the Number Line</h3>

<div class="worked-example">
  <h4>Example 1: 2 + 4</h4>
  <p>Start at 2. Jump forward 4 steps: 3, 4, 5, 6.</p>
  <p style="font-size: 16px; text-align: center; font-weight: bold;">2 + 4 = 6</p>
</div>

<div class="worked-example">
  <h4>Example 2: 5 + 3</h4>
  <p>Start at 5. Jump forward 3 steps: 6, 7, 8.</p>
  <p style="font-size: 16px; text-align: center; font-weight: bold;">5 + 3 = 8</p>
</div>"""
    },

    {
        "title": "The Power of the Number Line",
        "body": """<h3>Why the Number Line is Great for Addition</h3>

<div style="padding: 15px; border-radius: 8px; margin: 15px 0;">
  <h4>👁️ You Can See It</h4>
  <p>Addition isn't just numbers in your head — you can watch it happen on the line!</p>
</div>

<div style="padding: 15px; border-radius: 8px; margin: 15px 0;">
  <h4>🎯 It Works for Big Numbers</h4>
  <p>The number line works the same way whether you're adding 2 + 3 or 27 + 15.
  Same process, just more jumps!</p>
</div>

<div style="background: #f3e5f5; padding: 15px; border-radius: 8px; margin: 15px 0;">
  <h4>🔄 It Connects to Subtraction</h4>
  <p>Later, you'll learn that subtraction is the opposite:
  Instead of jumping forward (right), you jump backward (left).</p>
</div>

<h3>Important Fact About the Number Line</h3>
<div class="success-box">
  <p><strong>Addition always means moving RIGHT on the number line.</strong></p>
  <p>The bigger the number you add, the more steps you jump forward.</p>
</div>"""
    },

    {
        "title": "Practice with the Number Line",
        "body": """<h3>Solve These Using a Number Line</h3>

<div class="mcq-group">
  <p><strong>If you start at 4 and jump forward 3 steps, where do you land?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="Try jumping carefully: 4 → 5, 6, 7. You land at 7.">6</button>
    <button class="mcq-option" data-correct="true" data-explanation="Start at 4, jump 1 (to 5), jump 2 (to 6), jump 3 (to 7). 4 + 3 = 7.">7</button>
    <button class="mcq-option" data-correct="false" data-explanation="That would be jumping 4 steps, not 3.">8</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="mcq-group" style="margin-top: 20px;">
  <p><strong>Using the number line, what is 6 + 2?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="Start at 6 and jump forward 2: 7, 8.">7</button>
    <button class="mcq-option" data-correct="true" data-explanation="6 → 7 (jump 1) → 8 (jump 2). 6 + 2 = 8.">8</button>
    <button class="mcq-option" data-correct="false" data-explanation="That's jumping 3 times, not 2.">9</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="mcq-group" style="margin-top: 20px;">
  <p><strong>What is 1 + 5 on the number line?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="Start at 1 and count on 5 steps: 2, 3, 4, 5, 6.">5</button>
    <button class="mcq-option" data-correct="true" data-explanation="1 + 5 = 6. Start at 1, jump 5 times to land at 6.">6</button>
    <button class="mcq-option" data-correct="false" data-explanation="Count again. You only add 5, so you should land at 6.">7</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<h3>Try Drawing Your Own</h3>
<div style="padding: 15px; border-radius: 8px; margin: 15px 0;">
  <p style="font-size: 16px;"><strong>Challenge: Draw a number line and solve 3 + 4.</strong></p>
  <p style="margin-top: 10px; font-size: 14px">Hint: Draw a line with numbers 0-8. Put a circle at 3. Draw 4 jumps to the right.</p>
  <p style="margin-top: 10px;"><strong>Answer: 3 + 4 = 7</strong></p>
</div>"""
    }
]
