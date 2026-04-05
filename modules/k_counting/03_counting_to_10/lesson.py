"""Counting to 10 — Building Number Sense."""

TITLE = "Counting to 10"

SECTIONS = [
    {
        "title": "Learning the Sequence from 1 to 10",
        "body": """<h3>The Basic Number Sequence</h3>
<p>The first skill in counting is learning the sequence of numbers. In English, we count in this order:</p>

<div style="background: #4169E180; padding: 20px; border-radius: 8px; margin: 20px 0; text-align: center;">
  <p style="font-size: 20px; margin: 0;"><strong>1, 2, 3, 4, 5, 6, 7, 8, 9, 10</strong></p>
</div>

<p>Once you learn this sequence, it <strong>never changes</strong>. No matter what you're counting — apples, fingers, toys, or friends — the counting order is always the same.</p>

<div class="concept-box">
  <h4>Stable Order Principle</h4>
  <p>Numbers always come in the same order. The sequence \\(1, 2, 3...\\) stays stable and reliable, just like the alphabet stays in order.</p>
</div>

<h3>How to Practice the Sequence</h3>
<ul>
  <li><strong>Say it out loud:</strong> Practice saying "1, 2, 3, 4, 5, 6, 7, 8, 9, 10" every day</li>
  <li><strong>Use your fingers:</strong> Count on your fingers as you say each number</li>
  <li><strong>Sing it:</strong> The counting sequence works like a song — it has a rhythm and pattern</li>
  <li><strong>Point as you say:</strong> Point to objects and say numbers in order</li>
</ul>

<svg viewBox="0 0 400 100" style="width:100%;max-width:500px;height:auto;display:block;margin:20px auto;">
  <!-- Numbers 1-10 -->
  <text x="20" y="40" text-anchor='middle' font-size='24' font-weight='bold'>1</text>
  <text x="60" y="40" text-anchor='middle' font-size='24' font-weight='bold'>2</text>
  <text x="100" y="40" text-anchor='middle' font-size='24' font-weight='bold'>3</text>
  <text x="140" y="40" text-anchor='middle' font-size='24' font-weight='bold'>4</text>
  <text x="180" y="40" text-anchor='middle' font-size='24' font-weight='bold'>5</text>
  <text x="220" y="40" text-anchor='middle' font-size='24' font-weight='bold'>6</text>
  <text x="260" y="40" text-anchor='middle' font-size='24' font-weight='bold'>7</text>
  <text x="300" y="40" text-anchor='middle' font-size='24' font-weight='bold'>8</text>
  <text x="340" y="40" text-anchor='middle' font-size='24' font-weight='bold'>9</text>
  <text x="380" y="40" text-anchor='middle' font-size='24' font-weight='bold'>10</text>

  <!-- Connecting line -->
  <line x1="10" y1="60" x2="390" y2="60" stroke='#4169E1' stroke-width="2" marker-end="url(#arrowhead)"/>

  <!-- Arrow marker -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill='#4169E1'/>
    </marker>
  </defs>

  <!-- Label -->
  <text x="200" y="95" text-anchor='middle' font-size='12' fill='#666;'>The stable counting sequence</text>
</svg>"""
    },
    {
        "title": "Counting Objects: From 1 to 10",
        "body": """<h3>Putting It All Together: Counting Real Objects</h3>
<p>Now that you know the sequence, practice counting actual objects. This is where you combine the stable order with one-to-one correspondence.</p>

<h3>Interactive Practice: Count the Blocks</h3>
<p>Look at these colored blocks and count them. Point to each one as you count.</p>

<canvas id="countChart1" data-chart='{"type":"bar","data":{"labels":["Red","Blue","Green","Yellow","Purple"],"datasets":[{"label":"Count","data":[3,5,2,4,1],"backgroundColor":["#ef4444","#3b82f6","#22c55e","#fbbf24","#a855f7"]}]},"options":{"indexAxis":"y","plugins":{"legend":{"display":false},"title":{"display":true,"text":"Count the Colored Blocks"}},"scales":{"x":{"beginAtZero":true,"max":6}}}}' height="220"></canvas>

<div class="formula-box">
  <h4>How to Count the Blocks:</h4>
  <ol>
    <li>Point to the first block and say "1"</li>
    <li>Point to the second block and say "2"</li>
    <li>Keep pointing and counting: "3, 4, 5..."</li>
    <li>Stop when you reach the last block</li>
    <li>The last number is your answer!</li>
  </ol>
</div>

<h3>Counting on Your Fingers</h3>
<p>Your fingers are always with you! You can count on them to practice. When counting to 10, use both hands:</p>

<svg viewBox="0 0 300 100" style="width:100%;max-width:400px;height:auto;display:block;margin:20px auto;">
  <!-- Left hand (5 fingers) -->
  <g>
    <text x="50" y="20" text-anchor='middle' font-size='12' font-weight='bold'>Left Hand</text>
    <rect x="20" y="35" width="8" height="30" rx="4" fill='#4169E1'/> <!-- thumb -->
    <rect x="32" y="30" width="8" height="35" rx="4" fill='#4169E1'/> <!-- index -->
    <rect x="44" y="30" width="8" height="35" rx="4" fill='#4169E1'/> <!-- middle -->
    <rect x="56" y="30" width="8" height="35" rx="4" fill='#4169E1'/> <!-- ring -->
    <rect x="68" y="30" width="8" height="35" rx="4" fill='#4169E1'/> <!-- pinky -->
    <text x="50" y="85" text-anchor='middle' font-size='11'>1, 2, 3, 4, 5</text>
  </g>

  <!-- Plus sign -->
  <text x="150" y="60" text-anchor='middle' font-size='24'>+</text>

  <!-- Right hand (5 fingers) -->
  <g>
    <text x="240" y="20" text-anchor='middle' font-size='12' font-weight='bold'>Right Hand</text>
    <rect x="210" y="35" width="8" height="30" rx="4" fill='#ef4444'/> <!-- thumb -->
    <rect x="222" y="30" width="8" height="35" rx="4" fill='#ef4444'/> <!-- index -->
    <rect x="234" y="30" width="8" height="35" rx="4" fill='#ef4444'/> <!-- middle -->
    <rect x="246" y="30" width="8" height="35" rx="4" fill='#ef4444'/> <!-- ring -->
    <rect x="258" y="30" width="8" height="35" rx="4" fill='#ef4444'/> <!-- pinky -->
    <text x="240" y="85" text-anchor='middle' font-size='11'>6, 7, 8, 9, 10</text>
  </g>
</svg>"""
    },
    {
        "title": "Knowing What Comes Next",
        "body": """<h3>Predicting Numbers: What Comes After?</h3>
<p>Once you learn the sequence well, you can predict what number comes next without counting from the beginning. This is a shortcut!</p>

<div class="worked-example">
  <h4>Example: Complete the Sequence</h4>
  <p><strong>If you see: 5, 6, 7, ?</strong></p>
  <p style="margin-top: 10px;">You know the sequence, so you can say: "8 comes next!"</p>
  <p style="margin-top: 10px;">You don't have to count "1, 2, 3, 4, 5, 6, 7, 8" — you just remember.</p>
</div>

<h3>Practice: Fill in the Missing Numbers</h3>

<div class="mcq-group">
  <p><strong>What comes after 4?</strong></p>
  <p style="font-size: 18px;">4, ?</p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="That comes before 4, not after.">3</button>
    <button class="mcq-option" data-correct="true" data-explanation="Yes! The sequence is 4, 5.">5</button>
    <button class="mcq-option" data-correct="false" data-explanation="That's two numbers away from 4.">6</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<p style="margin-top: 20px;"></p>

<div class="mcq-group">
  <p><strong>What comes after 8?</strong></p>
  <p style="font-size: 18px;">8, ?</p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="That's before 8.">7</button>
    <button class="mcq-option" data-correct="false" data-explanation="That's two numbers away.">10</button>
    <button class="mcq-option" data-correct="true" data-explanation="Correct! The sequence is 8, 9.">9</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="success-box">
  <h4>Key Idea: Know Your Sequence</h4>
  <p>When the counting sequence is automatic (you say it without thinking), everything else becomes easier. You can count faster, predict next numbers, and solve problems.</p>
</div>"""
    }
]
