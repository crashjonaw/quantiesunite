"""05. Number Line — Visualizing numbers and their order."""

TITLE = "The Number Line: Ordering Numbers"

SECTIONS = [
    {
        "title": "What is a Number Line?",
        "body": """<h3>A Visual Way to Show Numbers</h3>
<p>A <strong>number line</strong> is a straight line with numbers marked on it in order. It shows:</p>
<ul>
  <li>Which numbers are smaller (on the left)</li>
  <li>Which numbers are bigger (on the right)</li>
  <li>How far apart two numbers are</li>
  <li>Which number comes next</li>
</ul>

<h3>The Number Line from 0 to 20</h3>
<p>Here's a number line showing all the numbers from 0 to 20:</p>

<svg viewBox="-35 0 470 100" style="width: 100%; height: auto; margin: 20px 0; background: rgba(255,255,255,0.03); border-radius: 8px; padding: 10px 0;">
  <!-- Main line -->
  <line x1="10" y1="50" x2="410" y2="50" stroke='#4169E1' stroke-width="3"/>

  <!-- Arrows -->
  <polygon points="5,50 0,45 0,55" fill='#4169E1'/>
  <polygon points="415,50 420,45 420,55" fill='#4169E1'/>

  <!-- Tick marks and numbers -->
  <g font-size='12' text-anchor='middle' fill='#e6edf3'>
    <line x1="10" y1="45" x2="10" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="10" y="75" fill='#e6edf3' font-weight='bold'>0</text>

    <line x1="30" y1="45" x2="30" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="30" y="75" fill='#e6edf3'>1</text>

    <line x1="50" y1="45" x2="50" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="50" y="75" fill='#e6edf3'>2</text>

    <line x1="70" y1="45" x2="70" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="70" y="75" fill='#e6edf3'>3</text>

    <line x1="90" y1="45" x2="90" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="90" y="75" fill='#e6edf3'>4</text>

    <line x1="110" y1="45" x2="110" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="110" y="75" fill='#e6edf3'>5</text>

    <line x1="130" y1="45" x2="130" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="130" y="75" fill='#e6edf3'>6</text>

    <line x1="150" y1="45" x2="150" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="150" y="75" fill='#e6edf3'>7</text>

    <line x1="170" y1="45" x2="170" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="170" y="75" fill='#e6edf3'>8</text>

    <line x1="190" y1="45" x2="190" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="190" y="75" fill='#e6edf3'>9</text>

    <line x1="210" y1="45" x2="210" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="210" y="75" fill='#e6edf3'>10</text>

    <line x1="230" y1="45" x2="230" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="230" y="75" fill='#e6edf3'>11</text>

    <line x1="250" y1="45" x2="250" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="250" y="75" fill='#e6edf3'>12</text>

    <line x1="270" y1="45" x2="270" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="270" y="75" fill='#e6edf3'>13</text>

    <line x1="290" y1="45" x2="290" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="290" y="75" fill='#e6edf3'>14</text>

    <line x1="310" y1="45" x2="310" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="310" y="75" fill='#e6edf3'>15</text>

    <line x1="330" y1="45" x2="330" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="330" y="75" fill='#e6edf3'>16</text>

    <line x1="350" y1="45" x2="350" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="350" y="75" fill='#e6edf3'>17</text>

    <line x1="370" y1="45" x2="370" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="370" y="75" fill='#e6edf3'>18</text>

    <line x1="390" y1="45" x2="390" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="390" y="75" fill='#e6edf3'>19</text>

    <line x1="410" y1="45" x2="410" y2="55" stroke='#4169E1' stroke-width="2"/>
    <text x="410" y="75" fill='#e6edf3'>20</text>
  </g>

  <!-- Direction labels -->
  <text x="5" y="20" font-size='11' fill='#8b949e' text-anchor='end'>Smaller</text>
  <text x="415" y="20" font-size='11' fill='#8b949e'>Bigger →</text>
</svg>

<h3>What Does the Number Line Show?</h3>
<ul>
  <li><strong>Left side (0):</strong> The smallest number in our range</li>
  <li><strong>Right side (20):</strong> The biggest number in our range</li>
  <li><strong>Middle:</strong> All the numbers in between, in order</li>
  <li><strong>Equal spacing:</strong> The distance between each tick mark is the same</li>
</ul>

<div class="concept-box">
  <h4>The Golden Rule</h4>
  <p><strong>Numbers on the right are always bigger than numbers on the left.</strong></p>
</div>"""
    },

    {
        "title": "Using the Number Line to Compare",
        "body": """<h3>Comparing with the Number Line</h3>
<p>The number line makes comparing numbers super easy! Just look at where the numbers are:</p>

<h4>Example: Is 7 bigger than 3?</h4>

<svg viewBox="0 0 420 120" style="width: 100%; height: auto; margin: 20px 0; background: rgba(255,255,255,0.03); border-radius: 8px; padding: 10px 0;">
  <!-- Main line -->
  <line x1="10" y1="50" x2="410" y2="50" stroke='#30363d' stroke-width="2"/>

  <!-- Tick marks and numbers -->
  <g font-size='12' text-anchor='middle' fill='#e6edf3'>
    <line x1="10" y1="45" x2="10" y2="55" stroke='#30363d' stroke-width="1"/>
    <text x="10" y="75" fill='#e6edf3'>0</text>

    <line x1="50" y1="45" x2="50" y2="55" stroke='#30363d' stroke-width="1"/>
    <text x="50" y="75" fill='#e6edf3'>2</text>

    <line x1="70" y1="45" x2="70" y2="55" stroke='#30363d' stroke-width="1"/>
    <text x="70" y="75" fill='#e6edf3' font-weight='bold' font-size='16'>3</text>

    <line x1="150" y1="45" x2="150" y2="55" stroke='#30363d' stroke-width="1"/>
    <text x="150" y="75" fill='#e6edf3'>7</text>

    <line x1="210" y1="45" x2="210" y2="55" stroke='#30363d' stroke-width="1"/>
    <text x="210" y="75" fill='#e6edf3'>10</text>

    <line x1="410" y1="45" x2="410" y2="55" stroke='#30363d' stroke-width="1"/>
    <text x="410" y="75" fill='#e6edf3'>20</text>
  </g>

  <!-- Highlight 3 -->
  <circle cx="70" cy="50" r="8" fill='none' stroke='#ff9800' stroke-width="3"/>
  <text x="70" y="25" text-anchor='middle' font-size='12' fill='#ff9800' font-weight='bold'>3</text>

  <!-- Highlight 7 -->
  <circle cx="150" cy="50" r="8" fill='none' stroke='#4caf50' stroke-width="3"/>
  <text x="150" y="25" text-anchor='middle' font-size='12' fill='#4caf50' font-weight='bold'>7</text>

  <!-- Arrow showing 7 is to the right -->
  <path d="M 70 90 L 150 90 M 145 85 L 150 90 L 145 95" stroke='#4caf50' stroke-width="2" fill='none'/>
  <text x="110" y="110" text-anchor='middle' font-size='12' fill='#4caf50' font-weight='bold'>7 is to the right!</text>
</svg>

<p><strong>Answer:</strong> Yes! \\(7\\) is to the right of \\(3\\), so \\(7 > 3\\).</p>

<h4>Rule: Which Number is Bigger?</h4>
<p>On a number line:</p>
<ul>
  <li>If a number is to the <strong>right</strong>, it's <strong>bigger</strong> ✓</li>
  <li>If a number is to the <strong>left</strong>, it's <strong>smaller</strong> ✓</li>
  <li>If numbers are at the same spot, they're <strong>equal</strong> ✓</li>
</ul>

<div class="mcq-group">
  <p><strong>Question:</strong> Look at the number line. Which is bigger: 15 or 8?</p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="No, 8 is to the left, so it's smaller.">8</button>
    <button class="mcq-option" data-correct="true" data-explanation="Yes! 15 is to the right of 8, so 15 is bigger.">15</button>
    <button class="mcq-option" data-correct="false" data-explanation="They're not in the same position, so they're not equal.">They're equal</button>
  </div>
  <div class="mcq-feedback"></div>
</div>"""
    },

    {
        "title": "Counting and Jumping on the Number Line",
        "body": """<h3>Using the Number Line to Count</h3>
<p>The number line is perfect for counting! You can:</p>
<ul>
  <li>Count up from any starting number</li>
  <li>Count down to find the number before</li>
  <li>Jump ahead multiple steps</li>
  <li>Find the distance between two numbers</li>
</ul>

<h4>Example: Count from 5 to 10</h4>

<svg viewBox="0 0 420 140" style="width: 100%; height: auto; margin: 20px 0; background: rgba(255,255,255,0.03); border-radius: 8px; padding: 10px 0;">
  <!-- Main line -->
  <line x1="10" y1="60" x2="410" y2="60" stroke='#4169E1' stroke-width="2"/>

  <!-- All numbers -->
  <g font-size='12' text-anchor='middle' fill='#ccc'>
    <line x1="10" y1="55" x2="10" y2="65" stroke='#30363d' stroke-width="1"/>
    <text x="10" y="85">0</text>

    <line x1="50" y1="55" x2="50" y2="65" stroke='#30363d' stroke-width="1"/>
    <text x="50" y="85">2</text>

    <line x1="110" y1="55" x2="110" y2="65" stroke='#30363d' stroke-width="1"/>
    <text x="110" y="85">5</text>

    <line x1="150" y1="55" x2="150" y2="65" stroke='#30363d' stroke-width="1"/>
    <text x="150" y="85">7</text>

    <line x1="210" y1="55" x2="210" y2="65" stroke='#30363d' stroke-width="1"/>
    <text x="210" y="85">10</text>

    <line x1="410" y1="55" x2="410" y2="65" stroke='#30363d' stroke-width="1"/>
    <text x="410" y="85">20</text>
  </g>

  <!-- Highlighting 5 to 10 -->
  <g>
    <circle cx="110" cy="60" r="7" fill='none' stroke='#ff9800' stroke-width="2"/>
    <text x="110" y="40" text-anchor='middle' font-size='11' fill='#ff9800' font-weight='bold'>Start: 5</text>

    <circle cx="210" cy="60" r="7" fill='none' stroke='#4caf50' stroke-width="2"/>
    <text x="210" y="40" text-anchor='middle' font-size='11' fill='#4caf50' font-weight='bold'>End: 10</text>
  </g>

  <!-- Jumps -->
  <g stroke='#4caf50' stroke-width="2" fill='none'>
    <path d="M 110 100 L 130 100 M 125 95 L 130 100 L 125 105"/>
    <path d="M 130 100 L 150 100 M 145 95 L 150 100 L 145 105"/>
    <path d="M 150 100 L 170 100 M 165 95 L 170 100 L 165 105"/>
    <path d="M 170 100 L 190 100 M 185 95 L 190 100 L 185 105"/>
    <path d="M 190 100 L 210 100 M 205 95 L 210 100 L 205 105"/>
  </g>

  <text x="160" y="125" text-anchor='middle' font-size='11' fill='#8b949e'>5 steps up!</text>
</svg>

<p><strong>Count:</strong> 5, 6, 7, 8, 9, 10 — that's 5 steps!</p>

<h3>Finding the Next and Previous Numbers</h3>
<p>The number line makes it easy:</p>

<ul>
  <li>What comes right after 7? Look one mark to the right: <strong>8</strong></li>
  <li>What comes right before 15? Look one mark to the left: <strong>14</strong></li>
  <li>What number is between 10 and 12? Look at what's in the middle: <strong>11</strong></li>
</ul>

<div class="worked-example">
  <h4>Worked Example: What is 3 more than 8?</h4>
  <p><strong>Step 1:</strong> Start at 8 on the number line.</p>
  <p><strong>Step 2:</strong> Jump right 3 times (one jump per unit): 9, 10, 11.</p>
  <p><strong>Step 3:</strong> You land on 11.</p>
  <p><strong>Answer:</strong> 3 more than 8 is 11.</p>
</div>

<div class="success-box">
  <h4>✓ Number Line Powers</h4>
  <p>Use the number line to:</p>
  <ul>
    <li>Compare numbers (left = smaller, right = bigger)</li>
    <li>Count up or down</li>
    <li>Find what comes next or before</li>
    <li>Add or subtract by jumping</li>
  </ul>
</div>"""
    },
]
