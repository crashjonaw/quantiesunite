"""Subtraction on a Number Line — Jumping backwards to subtract."""

TITLE = "Subtraction on a Number Line"

SECTIONS = [
    {
        "title": "Jumping Backwards on the Number Line",
        "body": """<p>A number line is like a <strong>road with numbers</strong>. To subtract, you <em>jump backwards</em>!</p>
<div class="concept-box">
<p><strong>Example:</strong> \(7 - 3 = ?\)<br/>
Start at 7, jump back 3 spaces, land on 4. Answer: <strong>4</strong></p>
</div>
<svg viewBox="0 0 500 120" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <line x1="40" y1="60" x2="490" y2="60" stroke='#8b949e' stroke-width="2"/>
  <circle cx="40" cy="60" r="4" fill='currentColor'/>
  <circle cx="90" cy="60" r="4" fill='currentColor'/>
  <circle cx="140" cy="60" r="4" fill='currentColor'/>
  <circle cx="190" cy="60" r="4" fill='currentColor'/>
  <circle cx="240" cy="60" r="4" fill='currentColor'/>
  <circle cx="290" cy="60" r="4" fill='currentColor'/>
  <circle cx="340" cy="60" r="4" fill='currentColor'/>
  <circle cx="390" cy="60" r="4" fill='currentColor'/>
  <circle cx="440" cy="60" r="4" fill='currentColor'/>
  <circle cx="490" cy="60" r="4" fill='currentColor'/>

  <text x="35" y="85" font-size='14' font-weight='bold' fill='currentColor'>0</text>
  <text x="85" y="85" font-size='14' fill='currentColor'>1</text>
  <text x="135" y="85" font-size='14' fill='currentColor'>2</text>
  <text x="185" y="85" font-size='14' fill='currentColor'>3</text>
  <text x="235" y="85" font-size='14' fill='currentColor'>4</text>
  <text x="285" y="85" font-size='14' fill='currentColor'>5</text>
  <text x="335" y="85" font-size='14' fill='currentColor'>6</text>
  <text x="385" y="85" font-size='14' fill='currentColor'>7</text>
  <text x="435" y="85" font-size='14' fill='currentColor'>8</text>
  <text x="485" y="85" font-size='14' fill='currentColor'>9</text>

  <circle cx="390" cy="60" r="20" fill='none' stroke='#3b82f6' stroke-width="2"/>
  <text x="395" y="25" font-size='16' font-weight='bold' fill='#3b82f6'>Start: 7</text>

  <path d="M 340 40 Q 310 20 240 40" stroke='#ef4444' stroke-width="3" fill='none' marker-end="url(#arrowred)"/>
  <text x="265" y="15" font-size='14' fill='#ef4444' font-weight='bold'>Jump back 3</text>

  <circle cx="240" cy="60" r="20" fill='none' stroke='#22c55e' stroke-width="2"/>
  <text x="235" y="110" font-size='16' font-weight='bold' fill='#22c55e'>Land: 4</text>

  <defs>
    <marker id="arrowred" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill='#ef4444'/>
    </marker>
  </defs>
</svg>
<p style="text-align:center;margin-top:12px;"><strong>\(7 - 3 = 4\)</strong></p>"""
    },
    {
        "title": "Steps for Number Line Subtraction",
        "body": """<p>Follow these steps to subtract on a number line:</p>
<div class="worked-example">
<p><strong>Step 1:</strong> Find the <em>bigger number</em> on the number line. Put your finger there. (Start at 7)</p>
<p style="margin-top:8px;"><strong>Step 2:</strong> Look at the <em>number you're taking away</em>. (We're taking away 3)</p>
<p style="margin-top:8px;"><strong>Step 3:</strong> Jump backwards that many spaces. Count each jump: 6, 5, 4. (Three jumps)</p>
<p style="margin-top:8px;"><strong>Step 4:</strong> Where did you land? That's your answer! (We landed on 4, so \(7 - 3 = 4\))</p>
</div>
<canvas id="numlineChart" data-chart='{
  "type": "scatter",
  "data": {
    "datasets": [
      {
        "label": "Number line 0−10",
        "data": [
          {"x": 0, "y": 1}, {"x": 1, "y": 1}, {"x": 2, "y": 1}, {"x": 3, "y": 1},
          {"x": 4, "y": 1}, {"x": 5, "y": 1}, {"x": 6, "y": 1}, {"x": 7, "y": 1},
          {"x": 8, "y": 1}, {"x": 9, "y": 1}, {"x": 10, "y": 1}
        ],
        "pointRadius": 5,
        "backgroundColor": "#8b5cf6"
      }
    ]
  },
  "options": {
    "plugins": {
      "title": {
        "display": true,
        "text": "Practice: Jump back to subtract"
      },
      "legend": {"display": false}
    },
    "scales": {
      "x": {"min": -1, "max": 11, "title": {"display": true, "text": "Number"}},
      "y": {"display": false}
    }
  }
}' height="150"></canvas>"""
    },
    {
        "title": "Practice: Jumping Back",
        "body": """<p>Use the number line in your head (or draw one!) to solve these:</p>
<div class="mcq-group">
  <p><strong>\(9 - 2 = ?\)</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="Start at 9, jump back 2: 8, 7. Land on 7.">6</button>
    <button class="mcq-option" data-correct="true" data-explanation="Correct! Start at 9, jump back 2 to land on 7.">7</button>
    <button class="mcq-option" data-correct="false" data-explanation="That would be \(9 - 1\). We need to jump back 2.">8</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
<div class="mcq-group">
  <p><strong>\(10 - 4 = ?\)</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="Count back from 10: 9, 8, 7, 6. That's 4 jumps, landing on 6.">5</button>
    <button class="mcq-option" data-correct="true" data-explanation="Correct! Start at 10, jump back 4 spaces: 9, 8, 7, 6.">6</button>
    <button class="mcq-option" data-correct="false" data-explanation="Try jumping back from 10 using 4 jumps.">4</button>
  </div>
  <div class="mcq-feedback"></div>
</div>"""
    },
    {
        "title": "Number Line is a Visual Tool",
        "body": """<p>The number line helps you <strong>see</strong> subtraction as moving backwards. It's like a visual shortcut for "taking away."</p>
<div class="success-box">
<p><strong>Tip:</strong> If you ever forget how to subtract, <em>draw a number line</em> and count back. The number line never lies! 📏</p>
</div>
<p>As you practice more, you won't need to draw the number line every time. You'll be able to picture it in your head and count back instantly. But for now, drawing is a <strong>super power</strong> that helps you solve any subtraction problem! ✨</p>"""
    }
]
