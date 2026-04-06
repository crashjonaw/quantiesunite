"""Relationship to Addition — Fact families and inverse operations."""

TITLE = "Relationship to Addition"

SECTIONS = [
    {
        "title": "Subtraction is the Opposite of Addition",
        "body": """<p>Addition and subtraction are <strong>best friends</strong> — they're opposites!</p>
<div class="concept-box">
<p><strong>Addition says:</strong> "I'm combining groups."<br/>
<strong>Subtraction says:</strong> "I'm separating a group."</p>
</div>
<p>Look at this:</p>
<div class="worked-example">
<p><strong>Addition:</strong> \(3 + 2 = 5\)<br/>
(Start with 3, add 2, get 5)</p>
<p style="margin-top:12px;"><strong>Subtraction:</strong> \(5 - 2 = 3\)<br/>
(Start with 5, take away 2, get back to 3)</p>
<p style="margin-top:12px;"><strong>Subtraction:</strong> \(5 - 3 = 2\)<br/>
(Start with 5, take away 3, get back to 2)</p>
</div>
<svg viewBox="0 0 450 140" style="width:100%;max-width:450px;height:auto;display:block;margin:16px auto;">
  <text x="20" y="25" font-size='14' font-weight='bold'>Addition & Subtraction Triangle:</text>

  <polygon points="150,50 100,130 200,130" fill='none' stroke='#8b949e' stroke-width="2"/>
  <circle cx="150" cy="50" r="12" fill='#4f8ef7'/>
  <text x="148" y="56" font-size='16' font-weight='bold' fill='white'>5</text>

  <circle cx="100" cy="130" r="12" fill='#ef4444'/>
  <text x="97" y="136" font-size='16' font-weight='bold' fill='white'>3</text>

  <circle cx="200" cy="130" r="12" fill='#22c55e'/>
  <text x="197" y="136" font-size='16' font-weight='bold' fill='white'>2</text>

  <text x="90" y="85" font-size='12' font-weight='bold'>3 + 2 = 5</text>
  <text x="155" y="105" font-size='12' font-weight='bold'>5 - 2 = 3</text>
  <text x="120" y="125" font-size='12' font-weight='bold'>5 - 3 = 2</text>

  <text x="250" y="80" font-size='13'>All three numbers</text>
  <text x="250" y="100" font-size='13'>work together!</text>
</svg>"""
    },
    {
        "title": "Fact Families",
        "body": """<p>When three numbers work together in addition and subtraction, they form a <strong>fact family</strong>.</p>
<div class="concept-box">
<p><strong>The family of 2, 4, and 6:</strong></p>
<p>\(2 + 4 = 6\)<br/>
\(4 + 2 = 6\)<br/>
\(6 - 2 = 4\)<br/>
\(6 - 4 = 2\)</p>
</div>
<p><strong>Why is this useful?</strong> Once you know ONE fact, you get THREE more for free!</p>
<canvas id="factChart" data-chart='{
  "type": "bar",
  "data": {
    "labels": ["2 + 4 = 6", "4 + 2 = 6", "6 − 2 = 4", "6 − 4 = 2"],
    "datasets": [{
      "label": "The Fact Family (2, 4, 6)",
      "data": [6, 6, 4, 2],
      "backgroundColor": ["#3b82f6", "#3b82f6", "#f59e0b", "#f59e0b"]
    }]
  },
  "options": {
    "plugins": {
      "title": {
        "display": true,
        "text": "One fact family: 2, 4, and 6"
      },
      "legend": {"display": false}
    },
    "scales": {
      "y": {"beginAtZero": true, "max": 8}
    }
  }
}' height="200"></canvas>"""
    },
    {
        "title": "Finding Missing Numbers in Fact Families",
        "body": """<p>If you know two numbers in a fact family, you can find the third!</p>
<div class="worked-example">
<p><strong>Example:</strong> You know \(3 + 4 = 7\). What is \(7 - 3\)?</p>
<p style="margin-top:8px;">Since \(3 + 4 = 7\), then \(7 - 3 = 4\). (Subtraction "undoes" addition.)</p>
</div>
<div class="mcq-group">
  <p><strong>If \(2 + 5 = 7\), then \(7 - 5 = ?\)</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="If \(2 + 5 = 7\), then \(7 - 5\) should give us back the 2.">5</button>
    <button class="mcq-option" data-correct="true" data-explanation="Correct! \(7 - 5 = 2\). Subtraction is the opposite of addition!">2</button>
    <button class="mcq-option" data-correct="false" data-explanation="That would be \(7 - 2\). We're taking away 5, so we get back 2.">7</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
<div class="mcq-group">
  <p><strong>If \(6 - 1 = 5\), which addition is true?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="That gives 7, not 6.">\(5 + 1 = 6\)</button>
    <button class="mcq-option" data-correct="true" data-explanation="Correct! \(1 + 5 = 6\). Addition and subtraction undo each other.">\(1 + 5 = 6\)</button>
    <button class="mcq-option" data-correct="false" data-explanation="That's 6 not 6.">\(6 + 1 = 7\)</button>
  </div>
  <div class="mcq-feedback"></div>
</div>"""
    },
    {
        "title": "Using Addition to Check Subtraction",
        "body": """<p>One of the best tricks in math: use addition to <strong>check</strong> your subtraction!</p>
<div class="success-box">
<p><strong>The trick:</strong><br/>
If \(9 - 3 = 6\), then check with addition: \(6 + 3\) should equal \(9\). ✓<br/>
(If it doesn't, you made a mistake!)</p>
</div>
<p><strong>Example:</strong></p>
<ul>
  <li>Subtraction: \(10 - 4 = 6\)</li>
  <li>Check with addition: \(6 + 4 = 10\) ✓ (Correct!)</li>
</ul>
<p><strong>Another example:</strong></p>
<ul>
  <li>Subtraction: \(8 - 2 = 5\) (wait, is this right?)</li>
  <li>Check: \(5 + 2 = 7\), not 8 ✗ (Oops! The answer should be 6, not 5)</li>
  <li>Correct: \(8 - 2 = 6\), and \(6 + 2 = 8\) ✓</li>
</ul>
<p style="margin-top:16px;"><strong>Remember:</strong> If addition and subtraction don't match, you know to re-solve! 🔍</p>"""
    }
]
