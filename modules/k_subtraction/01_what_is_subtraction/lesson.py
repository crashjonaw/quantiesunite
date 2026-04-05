"""What is Subtraction? — Introduction to taking away."""

TITLE = "What is Subtraction?"

SECTIONS = [
    {
        "title": "Taking Away Means Subtraction",
        "body": """<p><strong>Subtraction</strong> is what we do when we <em>take away</em> from a group. Instead of counting everything again, we can calculate how many are left.</p>
<div class="concept-box">
<p><strong>Real-world example:</strong> You have 5 cookies 🍪. You eat 2. How many are left? <br/>
<strong>5 take away 2 = 3 cookies left</strong></p>
</div>
<svg viewBox="0 0 400 120" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
  <text x="10" y="30" font-size='16' font-weight='bold'>Start with 5 cookies:</text>
  <circle cx="40" cy="70" r="15" fill='#d4a574'/>
  <circle cx="80" cy="70" r="15" fill='#d4a574'/>
  <circle cx="120" cy="70" r="15" fill='#d4a574'/>
  <circle cx="160" cy="70" r="15" fill='#d4a574'/>
  <circle cx="200" cy="70" r="15" fill='#d4a574'/>

  <text x="230" y="75" font-size='20' font-weight='bold'>−</text>

  <text x="270" y="30" font-size='16' font-weight='bold'>Take away 2:</text>
  <circle cx="300" cy="70" r="15" fill='#ef4444' opacity='0.5'/>
  <line x1="285" y1="55" x2="315" y2="85" stroke='#ef4444' stroke-width="2"/>
  <circle cx="340" cy="70" r="15" fill='#ef4444' opacity='0.5'/>
  <line x1="325" y1="55" x2="355" y2="85" stroke='#ef4444' stroke-width="2"/>
</svg>
<p style="text-align:center;margin-top:16px;"><strong>5 − 2 = 3</strong> cookies left! 🎉</p>"""
    },
    {
        "title": "The Subtraction Symbol: −",
        "body": """<p>We write subtraction using the <strong>minus sign</strong> (−):</p>
<div class="worked-example">
<p>\\(5 - 2 = 3\\)</p>
<p style="font-size:14px;margin-top:12px;">
  <strong>minuend</strong> (the number we start with) − <strong>subtrahend</strong> (the number we take away) = <strong>difference</strong> (what's left)
</p>
</div>
<canvas id="subChart1" data-chart='{
  "type": "bar",
  "data": {
    "labels": ["Start with", "Take away", "Left over"],
    "datasets": [{
      "label": "Cookies",
      "data": [5, 2, 3],
      "backgroundColor": ["#4f8ef7", "#ef4444", "#22c55e"]
    }]
  },
  "options": {
    "plugins": {
      "title": {
        "display": true,
        "text": "5 − 2 = 3"
      },
      "legend": {"display": false}
    },
    "scales": {
      "y": {"beginAtZero": true, "max": 6}
    }
  }
}' height="200"></canvas>"""
    },
    {
        "title": "Try It: Basic Subtraction",
        "body": """<p>Let's practice identifying subtraction situations:</p>
<div class="mcq-group">
  <p><strong>You have 7 apples 🍎. You give 3 to a friend. How many do you have left?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="That would be adding apples.">10</button>
    <button class="mcq-option" data-correct="true" data-explanation="Correct! 7 − 3 = 4. You still have 4 apples.">4</button>
    <button class="mcq-option" data-correct="false" data-explanation="Count: 7, 6, 5, 4. You have 4 left.">3</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
<div class="mcq-group">
  <p><strong>You have 6 balloons 🎈. Two pop! How many are still good?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Yes! 6 − 2 = 4. Four balloons are still safe.">4</button>
    <button class="mcq-option" data-correct="false" data-explanation="That's 6 − 1. Remember, 2 balloons popped.">5</button>
    <button class="mcq-option" data-correct="false" data-explanation="Count back: 5, 4. You have 4 left.">2</button>
  </div>
  <div class="mcq-feedback"></div>
</div>"""
    },
    {
        "title": "Why Subtraction Matters",
        "body": """<p>Without subtraction, we'd have to <em>recount everything from scratch</em>. Subtraction is a fast shortcut!</p>
<div class="success-box">
<p><strong>The power of subtraction:</strong> Once you know \\(5 - 2\\), you don't have to count 5 apples again. You instantly know 3 are left. 💡</p>
</div>
<p>In kindergarten and beyond, you'll use subtraction for:</p>
<ul>
  <li>🎁 Sharing toys (I had 10, gave away 4, have 6 left)</li>
  <li>🎮 Games (started with 8 lives, lost 2, have 6 left)</li>
  <li>🍕 Snacks (bought 12 cookies, ate 5, have 7 left)</li>
  <li>⏰ Time (it's 3 o'clock, wait 2 hours, it's 5 o'clock — wait, that's addition! But subtraction: it's 5 o'clock, 2 hours ago it was 3 o'clock)</li>
</ul>"""
    }
]
