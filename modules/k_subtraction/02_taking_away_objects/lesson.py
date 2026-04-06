"""Taking Away Objects — Hands-on subtraction with concrete items."""

TITLE = "Taking Away Objects"

SECTIONS = [
    {
        "title": "See It: Visual Subtraction",
        "body": """<p>The best way to learn subtraction is to <strong>see it happening</strong>. When you <em>cross out</em> or <em>remove</em> objects, you understand what "taking away" really means.</p>
<div class="concept-box">
<p><strong>Example:</strong> Start with 8 stars ⭐, cross out 3. How many remain?</p>
</div>
<svg viewBox="0 0 420 105" style="width:100%;max-width:420px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="20" font-size='14' font-family='Arial, sans-serif' font-weight='bold' fill='currentColor'>8 stars, remove 3:</text>

  <!-- 8 circles evenly spaced: x = 35, 80, 125, 170, 215, 260, 305, 350 (gap 45) -->
  <circle cx="35" cy="55" r="14" fill='#f59e0b'/>
  <text x="35" y="60" font-size='16' font-family='Arial, sans-serif' text-anchor='middle' fill='currentColor'>1</text>

  <circle cx="80" cy="55" r="14" fill='#f59e0b'/>
  <text x="80" y="60" font-size='16' font-family='Arial, sans-serif' text-anchor='middle' fill='currentColor'>2</text>

  <circle cx="125" cy="55" r="14" fill='#f59e0b'/>
  <text x="125" y="60" font-size='16' font-family='Arial, sans-serif' text-anchor='middle' fill='currentColor'>3</text>

  <circle cx="170" cy="55" r="14" fill='#f59e0b'/>
  <text x="170" y="60" font-size='16' font-family='Arial, sans-serif' text-anchor='middle' fill='currentColor'>4</text>

  <circle cx="215" cy="55" r="14" fill='#f59e0b'/>
  <text x="215" y="60" font-size='16' font-family='Arial, sans-serif' text-anchor='middle' fill='currentColor'>5</text>

  <!-- Crossed-out stars (removed) -->
  <circle cx="260" cy="55" r="14" fill='#ef4444' opacity='0.35'/>
  <line x1="248" y1="43" x2="272" y2="67" stroke='#ef4444' stroke-width='2.5'/>
  <line x1="272" y1="43" x2="248" y2="67" stroke='#ef4444' stroke-width='2.5'/>

  <circle cx="305" cy="55" r="14" fill='#ef4444' opacity='0.35'/>
  <line x1="293" y1="43" x2="317" y2="67" stroke='#ef4444' stroke-width='2.5'/>
  <line x1="317" y1="43" x2="293" y2="67" stroke='#ef4444' stroke-width='2.5'/>

  <circle cx="350" cy="55" r="14" fill='#ef4444' opacity='0.35'/>
  <line x1="338" y1="43" x2="362" y2="67" stroke='#ef4444' stroke-width='2.5'/>
  <line x1="362" y1="43" x2="338" y2="67" stroke='#ef4444' stroke-width='2.5'/>

  <text x="210" y="92" font-size='14' font-family='Arial, sans-serif' font-weight='bold' fill='currentColor' text-anchor='middle'>8 - 3 = 5 stars left!</text>
</svg>
<p style="text-align:center;margin-top:12px;"><strong>\(8 - 3 = 5\) stars left</strong></p>"""
    },
    {
        "title": "Hands-On Subtraction with Manipulatives",
        "body": """<p>Use your fingers, blocks, counters, or drawings to practice subtraction:</p>
<div class="worked-example">
<p><strong>Strategy 1: Physical Removal</strong><br/>
Put 10 counters on a table. Remove 4. Count what's left. <strong>\(10 - 4 = 6\)</strong></p>
<p style="margin-top:12px;"><strong>Strategy 2: Crossing Out</strong><br/>
Draw 7 circles. Cross out 2. Count the circles that are NOT crossed out. <strong>\(7 - 2 = 5\)</strong></p>
<p style="margin-top:12px;"><strong>Strategy 3: Hiding</strong><br/>
Show 9 objects. Cover up 3 with your hand. Count what you can still see. <strong>\(9 - 3 = 6\)</strong></p>
</div>
<canvas id="objChart1" data-chart='{
  "type": "bar",
  "data": {
    "labels": ["Start", "Remove", "Left"],
    "datasets": [{
      "label": "Counters",
      "data": [10, 4, 6],
      "backgroundColor": ["#3b82f6", "#ef4444", "#10b981"]
    }]
  },
  "options": {
    "plugins": {
      "title": {
        "display": true,
        "text": "Removing 4 from 10 leaves 6"
      },
      "legend": {"display": false}
    },
    "scales": {
      "y": {"beginAtZero": true, "max": 12}
    }
  }
}' height="200"></canvas>"""
    },
    {
        "title": "Common Subtraction Situations",
        "body": """<p>Subtraction happens everywhere! Learn to spot it:</p>
<div class="mcq-group">
  <p><strong>🍪 You have 9 cookies. You eat 4. How many are left?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="That would be \(9 + 4 = 13\). But we're taking away, not adding.">13</button>
    <button class="mcq-option" data-correct="true" data-explanation="Correct! \(9 - 4 = 5\). Five cookies left for later!">5</button>
    <button class="mcq-option" data-correct="false" data-explanation="That's only 3 eaten. We ate 4, so \(9 - 4 = 5\).">6</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
<div class="mcq-group">
  <p><strong>🎈 You blow up 12 balloons. 5 pop. How many are safe?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="Count on from 5: 6, 7, 8, 9, 10, 11, 12. That's 7 more.">7</button>
    <button class="mcq-option" data-correct="true" data-explanation="Correct! \(12 - 5 = 7\). Seven balloons are still good.">7</button>
    <button class="mcq-option" data-correct="false" data-explanation="You have 12 total. If 5 popped, \(12 - 5 = 7\), not 8.">8</button>
  </div>
  <div class="mcq-feedback"></div>
</div>"""
    },
    {
        "title": "Why We Use Objects to Learn",
        "body": """<p>Using real objects, pictures, or drawings helps your brain <strong>see</strong> what's happening in subtraction. Eventually, you won't need the objects — you'll just <em>know</em> the answer!</p>
<div class="success-box">
<p><strong>The journey:</strong></p>
<ol>
  <li>Use blocks or counters (you see and touch everything)</li>
  <li>Use drawings or dots (you visualize on paper)</li>
  <li>Use counting strategies (you count back in your head)</li>
  <li>Know it instantly (you've practiced so much, you just know! ⚡)</li>
</ol>
</div>
<p>Right now, <strong>use objects and drawings as much as you want</strong>. That's how you build strong math skills! 💪</p>"""
    }
]
