"""Skip Counting — Counting by Groups."""

TITLE = "Skip Counting"

SECTIONS = [
    {
        "title": "What is Skip Counting?",
        "body": """<h3>A Faster Way to Count</h3>
<p>When you count \(1, 2, 3, 4, 5, 6, 7, 8, 9, 10\), you say every number. But sometimes, you don't need every number. You can count by <strong>groups</strong> instead. This is called <strong>skip counting</strong> — you skip over numbers to count faster.</p>

<div class="concept-box">
  <h4>Skip Counting Definition</h4>
  <p>Skip counting means counting by a certain number over and over. Instead of saying "1, 2, 3, 4, 5," you might say "2, 4, 6, 8, 10" or "5, 10, 15, 20."</p>
</div>

<h3>Why Do We Skip Count?</h3>
<p>Skip counting is useful because:</p>
<ul>
  <li><strong>It's faster:</strong> To count to 20, you can say "2, 4, 6, 8, 10, 12, 14, 16, 18, 20" (10 numbers) instead of all 20 numbers</li>
  <li><strong>It helps with multiplication:</strong> Counting by \(2\)s is like \(2 + 2 + 2\ldots\)</li>
  <li><strong>It's practical:</strong> Coins often come in groups, so we skip count by their value</li>
  <li><strong>It shows patterns:</strong> Numbers that repeat a pattern help us understand math</li>
</ul>

<div class="success-box">
  <h4>Remember</h4>
  <p>Skip counting is still using the same rules as regular counting — we just count by bigger groups instead of by ones.</p>
</div>"""
    },
    {
        "title": "Counting by 2s and 5s",
        "body": """<h3>Counting by 2s: Every Other Number</h3>
<p>When you count by \(2\)s, you say every other number. Start at 2 and keep adding 2:</p>

<div style="background: #4169E180; padding: 20px; border-radius: 8px; margin: 20px 0; text-align: center;">
  <p style="font-size: 18px;"><strong>2, 4, 6, 8, 10, 12, 14, 16, 18, 20</strong></p>
</div>

<p>Notice: each number is 2 more than the one before. This pattern never breaks.</p>

<svg viewBox="0 0 400 120" style="width:100%;max-width:500px;height:auto;display:block;margin:20px auto;">
  <!-- Title -->
  <text x="200" y="20" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>Counting by 2s: Pairs of Objects</text>

  <!-- Pair 1 -->
  <circle cx="30" cy="60" r="10" fill='#4169E1'/>
  <circle cx="50" cy="60" r="10" fill='#4169E1'/>
  <text x="40" y="100" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>2</text>

  <!-- Pair 2 -->
  <circle cx="100" cy="60" r="10" fill='#4169E1'/>
  <circle cx="120" cy="60" r="10" fill='#4169E1'/>
  <text x="110" y="100" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>4</text>

  <!-- Pair 3 -->
  <circle cx="170" cy="60" r="10" fill='#4169E1'/>
  <circle cx="190" cy="60" r="10" fill='#4169E1'/>
  <text x="180" y="100" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>6</text>

  <!-- Pair 4 -->
  <circle cx="240" cy="60" r="10" fill='#4169E1'/>
  <circle cx="260" cy="60" r="10" fill='#4169E1'/>
  <text x="250" y="100" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>8</text>

  <!-- Pair 5 -->
  <circle cx="310" cy="60" r="10" fill='#4169E1'/>
  <circle cx="330" cy="60" r="10" fill='#4169E1'/>
  <text x="320" y="100" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>10</text>
</svg>

<h3>Counting by 5s: Making Groups of Five</h3>
<p>When you count by \(5\)s, you say numbers that are 5 apart. This is great for counting fingers or coins!</p>

<div style="background: #ef444480; padding: 20px; border-radius: 8px; margin: 20px 0; text-align: center;">
  <p style="font-size: 18px;"><strong>5, 10, 15, 20</strong></p>
</div>

<div class="worked-example">
  <h4>Example: Counting Fingers by 5s</h4>
  <p style="text-align: center; margin-bottom: 15px;">Left hand: 🖐️ (5 fingers)</p>
  <p style="text-align: center; margin-bottom: 15px;">Count: "5"</p>
  <p style="text-align: center; margin-bottom: 15px;">Right hand: 🖐️ (5 fingers)</p>
  <p style="text-align: center; margin-bottom: 15px;">Count on: "5... 10"</p>
  <p style="margin-top: 15px; font-weight: bold; color: var(--success);">Total: 10 fingers! ✓</p>
</div>

<h3>Quick Practice: Fill in the Blanks</h3>

<div class="mcq-group">
  <p><strong>Counting by 2s: 2, 4, 6, ?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="When counting by 2s, add 2 each time, not 1.">7</button>
    <button class="mcq-option" data-correct="true" data-explanation="Correct! \(6 + 2 = 8\).">8</button>
    <button class="mcq-option" data-correct="false" data-explanation="That's 2 numbers away.">10</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<p style="margin-top: 20px;"></p>

<div class="mcq-group">
  <p><strong>Counting by 5s: 5, 10, 15, ?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="When counting by 5s, add 5 each time.">18</button>
    <button class="mcq-option" data-correct="true" data-explanation="Correct! \(15 + 5 = 20\).">20</button>
    <button class="mcq-option" data-correct="false" data-explanation="That's too far. Add 5 to 15.">25</button>
  </div>
  <div class="mcq-feedback"></div>
</div>"""
    },
    {
        "title": "Real-World Uses of Skip Counting",
        "body": """<h3>Counting by 2s: Pairs and Pairs</h3>
<p>You use counting by 2s when you have pairs of things:</p>
<ul>
  <li><strong>Socks:</strong> If you have 5 pairs of socks, that's 2, 4, 6, 8, 10 individual socks</li>
  <li><strong>Shoes:</strong> 3 pairs = 2, 4, 6 shoes</li>
  <li><strong>Eyes:</strong> Each person has 2 eyes. For 5 people: 2, 4, 6, 8, 10 eyes</li>
  <li><strong>Wheels:</strong> Each car has 4 wheels. For bicycles (2 wheels each), count: 2, 4, 6, 8...</li>
</ul>

<h3>Counting by 5s: Money and Hands</h3>
<p>You use counting by 5s when dealing with groups of five:</p>
<ul>
  <li><strong>Fingers:</strong> Count your fingers by 5s: one hand = 5, two hands = 10</li>
  <li><strong>Nickels:</strong> Each nickel is worth 5 cents. If you have 4 nickels: 5, 10, 15, 20 cents</li>
  <li><strong>Groups of kids:</strong> If you have 3 groups of 5 kids, count: 5, 10, 15 kids total</li>
</ul>

<canvas id="countChart3" data-chart='{"type":"bar","data":{"labels":["Nickels","Total Cents"],"datasets":[{"label":"Count","data":[4,20],"backgroundColor":["#a78bfa","#22c55e"]}]},"options":{"plugins":{"title":{"display":true,"text":"Skip Counting by 5s: 4 Nickels = 20 Cents"}},"scales":{"y":{"beginAtZero":true,"max":25}}}}' height="220"></canvas>

<button class="reveal-btn" data-reveal="rev1">▼ Show Example Calculation</button>
<div class="reveal-panel" id="rev1">
  <p><strong>You have 4 nickels (5 cents each)</strong></p>
  <p style="margin-top: 10px;">Count by 5s: 5, 10, 15, 20</p>
  <p style="margin-top: 10px;"><strong>Total: 20 cents ✓</strong></p>
</div>

<div class="success-box">
  <h4>Skip Counting is Practical!</h4>
  <p>You don't need to count one by one for everything. When things come in groups, skip counting gets you the answer faster and it's a valuable skill for real-life math.</p>
</div>"""
    }
]
