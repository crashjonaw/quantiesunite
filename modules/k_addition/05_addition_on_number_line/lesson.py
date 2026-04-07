"""Concept 5: Addition on the Number Line — Jumping and Moving."""

TITLE = "Addition on the Number Line: Jumping Forward"

SECTIONS = [
    {
        "title": "What is a Number Line?",
        "body": """<h3>A Line of Numbers</h3>
<p>A <strong>number line</strong> is a straight line with numbers written in order, from left (small) to right (big).</p>

<svg viewBox="0 0 450 80" style="width: 100%; max-width: 500px; height: auto; display: block; margin: 20px auto;">
  <!-- Main line -->
  <line x1="15" y1="35" x2="435" y2="35" stroke='#4169E1' stroke-width="3"/>

  <!-- Tick marks and numbers, evenly spaced at 52.5px intervals -->
  <g font-size='14' text-anchor='middle'>
    <line x1="15" y1="30" x2="15" y2="40" stroke='#4169E1' stroke-width="2"/>
    <text x="15" y="58" fill='currentColor'>0</text>

    <line x1="67" y1="30" x2="67" y2="40" stroke='#4169E1' stroke-width="2"/>
    <text x="67" y="58" fill='currentColor'>1</text>

    <line x1="120" y1="30" x2="120" y2="40" stroke='#4169E1' stroke-width="2"/>
    <text x="120" y="58" fill='currentColor'>2</text>

    <line x1="172" y1="30" x2="172" y2="40" stroke='#4169E1' stroke-width="2"/>
    <text x="172" y="58" fill='currentColor'>3</text>

    <line x1="225" y1="30" x2="225" y2="40" stroke='#4169E1' stroke-width="2"/>
    <text x="225" y="58" fill='currentColor'>4</text>

    <line x1="277" y1="30" x2="277" y2="40" stroke='#4169E1' stroke-width="2"/>
    <text x="277" y="58" fill='currentColor'>5</text>

    <line x1="330" y1="30" x2="330" y2="40" stroke='#4169E1' stroke-width="2"/>
    <text x="330" y="58" fill='currentColor'>6</text>

    <line x1="382" y1="30" x2="382" y2="40" stroke='#4169E1' stroke-width="2"/>
    <text x="382" y="58" fill='currentColor'>7</text>

    <line x1="435" y1="30" x2="435" y2="40" stroke='#4169E1' stroke-width="2"/>
    <text x="435" y="58" fill='currentColor'>8</text>
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
        "body": """<h3>Step-by-Step: Adding \(3 + 2\)</h3>

<div class="formula-box">
  <p style="font-size: 16px; margin-bottom: 15px;"><strong>Step 1: Find your starting number (3) on the line.</strong></p>

  <svg viewBox="0 0 340 90" style="width: 100%; max-width: 400px; height: auto; display: block; margin: 10px auto;">
    <line x1="15" y1="52" x2="325" y2="52" stroke='#4169E1' stroke-width="3"/>
    <g font-size='14' text-anchor='middle'>
      <line x1="15" y1="47" x2="15" y2="57" stroke='#4169E1' stroke-width="2"/>
      <text x="15" y="75" fill='currentColor'>0</text>
      <line x1="77" y1="47" x2="77" y2="57" stroke='#4169E1' stroke-width="2"/>
      <text x="77" y="75" fill='currentColor'>1</text>
      <line x1="139" y1="47" x2="139" y2="57" stroke='#4169E1' stroke-width="2"/>
      <text x="139" y="75" fill='currentColor'>2</text>
      <line x1="201" y1="47" x2="201" y2="57" stroke='#4169E1' stroke-width="2"/>
      <text x="201" y="75" fill='currentColor'>3</text>
      <line x1="263" y1="47" x2="263" y2="57" stroke='#4169E1' stroke-width="2"/>
      <text x="263" y="75" fill='currentColor'>4</text>
      <line x1="325" y1="47" x2="325" y2="57" stroke='#4169E1' stroke-width="2"/>
      <text x="325" y="75" fill='currentColor'>5</text>
    </g>
    <circle cx="201" cy="52" r="8" fill='#22c55e' stroke='#8b949e' stroke-width="2"/>
    <text x="201" y="28" text-anchor='middle' font-size='12' font-weight='bold' fill='currentColor'>Start here: 3</text>
  </svg>

  <p style="font-size: 16px; margin-top: 15px; margin-bottom: 15px;"><strong>Step 2: Jump forward 2 steps (because we're adding 2).</strong></p>

  <svg viewBox="0 0 340 110" style="width: 100%; max-width: 400px; height: auto; display: block; margin: 10px auto;">
    <defs><marker id="arrowJ" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#ef4444"/></marker></defs>
    <line x1="15" y1="65" x2="325" y2="65" stroke='#4169E1' stroke-width="3"/>
    <g font-size='14' text-anchor='middle'>
      <line x1="15" y1="60" x2="15" y2="70" stroke='#4169E1' stroke-width="2"/>
      <text x="15" y="88" fill='currentColor'>0</text>
      <line x1="77" y1="60" x2="77" y2="70" stroke='#4169E1' stroke-width="2"/>
      <text x="77" y="88" fill='currentColor'>1</text>
      <line x1="139" y1="60" x2="139" y2="70" stroke='#4169E1' stroke-width="2"/>
      <text x="139" y="88" fill='currentColor'>2</text>
      <line x1="201" y1="60" x2="201" y2="70" stroke='#4169E1' stroke-width="2"/>
      <text x="201" y="88" fill='currentColor'>3</text>
      <line x1="263" y1="60" x2="263" y2="70" stroke='#4169E1' stroke-width="2"/>
      <text x="263" y="88" fill='currentColor'>4</text>
      <line x1="325" y1="60" x2="325" y2="70" stroke='#4169E1' stroke-width="2"/>
      <text x="325" y="88" fill='currentColor'>5</text>
    </g>
    <!-- Start at 3 -->
    <circle cx="201" cy="65" r="8" fill='#22c55e' stroke='#8b949e' stroke-width="2"/>
    <!-- End at 5 -->
    <circle cx="325" cy="65" r="8" fill='#f59e0b' stroke='#8b949e' stroke-width="2"/>
    <!-- Jump arcs -->
    <path d="M 207 53 Q 232 25 257 53" stroke='#ef4444' stroke-width="2" fill='none' marker-end="url(#arrowJ)"/>
    <path d="M 269 53 Q 294 25 319 53" stroke='#ef4444' stroke-width="2" fill='none' marker-end="url(#arrowJ)"/>
    <!-- Jump labels -->
    <text x="232" y="22" text-anchor='middle' font-size='11' fill='#ef4444'>+1</text>
    <text x="294" y="22" text-anchor='middle' font-size='11' fill='#ef4444'>+1</text>
  </svg>

  <p style="font-size: 16px; margin-top: 15px; margin-bottom: 15px;"><strong>Step 3: See where you land (5). That's your answer!</strong></p>

  <p style="text-align: center; font-size: 18px; margin-top: 10px; font-weight: bold;">\(3 + 2 = 5\) ✓</p>
</div>

<h3>More Examples on the Number Line</h3>

<div class="worked-example">
  <h4>Example 1: \(2 + 4\)</h4>
  <p>Start at 2. Jump forward 4 steps: 3, 4, 5, 6.</p>
  <p style="font-size: 16px; text-align: center; font-weight: bold;">\(2 + 4 = 6\)</p>
</div>

<div class="worked-example">
  <h4>Example 2: \(5 + 3\)</h4>
  <p>Start at 5. Jump forward 3 steps: 6, 7, 8.</p>
  <p style="font-size: 16px; text-align: center; font-weight: bold;">\(5 + 3 = 8\)</p>
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
  <p>The number line works the same way whether you're adding \(2 + 3\) or \(27 + 15\).
  Same process, just more jumps!</p>
</div>

<div style="background: #f3e5f5; padding: 15px; border-radius: 8px; margin: 15px 0; color: #1a1a2e;">
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
    <button class="mcq-option" data-correct="true" data-explanation="Start at 4, jump 1 (to 5), jump 2 (to 6), jump 3 (to 7). \(4 + 3 = 7\).">7</button>
    <button class="mcq-option" data-correct="false" data-explanation="That would be jumping 4 steps, not 3.">8</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="mcq-group" style="margin-top: 20px;">
  <p><strong>Using the number line, what is \(6 + 2\)?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="Start at 6 and jump forward 2: 7, 8.">7</button>
    <button class="mcq-option" data-correct="true" data-explanation="6 → 7 (jump 1) → 8 (jump 2). \(6 + 2 = 8\).">8</button>
    <button class="mcq-option" data-correct="false" data-explanation="That's jumping 3 times, not 2.">9</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="mcq-group" style="margin-top: 20px;">
  <p><strong>What is \(1 + 5\) on the number line?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="Start at 1 and count on 5 steps: 2, 3, 4, 5, 6.">5</button>
    <button class="mcq-option" data-correct="true" data-explanation="\(1 + 5 = 6\). Start at 1, jump 5 times to land at 6.">6</button>
    <button class="mcq-option" data-correct="false" data-explanation="Count again. You only add 5, so you should land at 6.">7</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<h3>Try Drawing Your Own</h3>
<div style="padding: 15px; border-radius: 8px; margin: 15px 0;">
  <p style="font-size: 16px;"><strong>Challenge: Draw a number line and solve \(3 + 4\).</strong></p>
  <p style="margin-top: 10px; font-size: 14px">Hint: Draw a line with numbers 0–8. Put a circle at 3. Draw 4 jumps to the right.</p>
  <p style="margin-top: 10px;"><strong>Answer: \(3 + 4 = 7\)</strong></p>
</div>"""
    }
]
