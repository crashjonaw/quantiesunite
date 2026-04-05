"""Rounding and Estimating Numbers to 1000"""

TITLE = "Rounding and Estimating Numbers to 1000"

SECTIONS = [
    {
        "title": "What is Rounding?",
        "body": """<div class="concept-box">
<p><strong>Rounding</strong> means finding the nearest "friendly" number. Instead of saying 47, we might say "about 50" (rounded to the nearest 10).</p>
<p>Rounded numbers are easier to work with and useful for estimation and quick mental math.</p>
</div>

<svg viewBox="0 0 600 240" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="300" y="20" text-anchor='middle' fill='#e6edf3' font-size='15' font-weight='bold'>Understanding Rounding</text>

  <!-- Number line showing rounding -->
  <line x1="40" y1="80" x2="560" y2="80" stroke='#4f8ef7' stroke-width="2"/>

  <!-- Tick marks -->
  <line x1="40" y1="75" x2="40" y2="85" stroke='#4f8ef7' stroke-width="2"/>
  <text x="40" y="100" text-anchor='middle' fill='#4f8ef7' font-size='11' font-weight='bold'>40</text>

  <line x1="300" y1="75" x2="300" y2="85" stroke='#4f8ef7' stroke-width="2"/>
  <text x="300" y="100" text-anchor='middle' fill='#4f8ef7' font-size='11' font-weight='bold'>50</text>

  <line x1="560" y1="75" x2="560" y2="85" stroke='#4f8ef7' stroke-width="2"/>
  <text x="560" y="100" text-anchor='middle' fill='#4f8ef7' font-size='11' font-weight='bold'>60</text>

  <!-- Number 47 positioned -->
  <circle cx="260" cy="60" r="8" fill='#ec4899'/>
  <text x="260" y="65" text-anchor='middle' fill='#fff' font-size='10' font-weight='bold'>47</text>

  <!-- Arrows showing which way it rounds -->
  <line x1="260" y1="125" x2="300" y2="125" stroke='#22c55e' stroke-width="3" marker-end="url(#arrowgreen)"/>
  <text x="280" y="155" text-anchor='middle' fill='#e6edf3' font-size='12' font-weight='bold'>47 rounds to 50</text>

  <!-- SVG marker definition -->
  <defs>
    <marker id="arrowgreen" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill='#22c55e' />
    </marker>
  </defs>

  <!-- Explanation box -->
  <rect x="30" y="180" width="540" height="50" fill='#22c55e15' stroke='#22c55e' stroke-width="1" stroke-dasharray="3,3" rx="3"/>
  <text x="40" y="200" text-anchor='start' fill='#e6edf3' font-size='11'><strong>Key Idea:</strong> Is 47 closer to 40 or 50? Distance to 50 = 3, distance to 40 = 7.</text>
  <text x="40" y="217" text-anchor='start' fill='#e6edf3' font-size='11'>So 47 is closer to 50. Answer: 47 rounds UP to 50.</text>
</svg>"""
    },
    {
        "title": "Rounding to the Nearest 10",
        "body": """<div class="concept-box">
<p>To round to the nearest 10, look at the <strong>ones digit</strong>:</p>
<ul>
<li>If the ones digit is <strong>0, 1, 2, 3, or 4</strong>, round <strong>DOWN</strong> (keep the tens digit the same)</li>
<li>If the ones digit is <strong>5, 6, 7, 8, or 9</strong>, round <strong>UP</strong> (add 1 to the tens digit)</li>
</ul>
</div>

<svg viewBox="0 0 600 280" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="300" y="20" text-anchor='middle' fill='#e6edf3' font-size='15' font-weight='bold'>Rounding to Nearest 10</text>

  <!-- Rule visualization -->
  <rect x="20" y="40" width="270" height="60" fill='#22c55e20' stroke='#22c55e' stroke-width="2" rx="4"/>
  <text x="155" y="60" text-anchor='middle' fill='#e6edf3' font-size='12' font-weight='bold'>Ones: 0, 1, 2, 3, 4</text>
  <text x="155" y="80" text-anchor='middle' fill='#e6edf3' font-size='12' font-weight='bold'>ROUND DOWN</text>

  <rect x="310" y="40" width="270" height="60" fill='#ec489920' stroke='#ec4899' stroke-width="2" rx="4"/>
  <text x="445" y="60" text-anchor='middle' fill='#e6edf3' font-size='12' font-weight='bold'>Ones: 5, 6, 7, 8, 9</text>
  <text x="445" y="80" text-anchor='middle' fill='#e6edf3' font-size='12' font-weight='bold'>ROUND UP</text>

  <!-- Examples -->
  <rect x="20" y="120" width="540" height="50" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="1" rx="3"/>
  <text x="30" y="140" text-anchor='start' fill='#e6edf3' font-size='11'><strong>Examples (Down):</strong> 21→20, 34→30, 48→50 (wait, 8 is 5+, so round UP!)</text>
  <text x="30" y="155" text-anchor='start' fill='#e6edf3' font-size='11'><strong>Corrected:</strong> 21→20, 34→30, 44→40, 46→50</text>

  <rect x="20" y="185" width="540" height="50" fill='#ec489920' stroke='#ec4899' stroke-width="1" rx="3"/>
  <text x="30" y="205" text-anchor='start' fill='#e6edf3' font-size='11'><strong>Examples (Up):</strong> 25→30, 37→40, 59→60, 78→80</text>

  <!-- Visual number line example -->
  <line x1="50" y1="260" x2="550" y2="260" stroke='#808080' stroke-width="1"/>
  <circle cx="150" cy="260" r="5" fill='#4f8ef7'/>
  <text x="150" y="280" text-anchor='middle' fill='#4f8ef7' font-size='10'>24→20</text>

  <circle cx="330" cy="260" r="5" fill='#ec4899'/>
  <text x="330" y="280" text-anchor='middle' fill='#ec4899' font-size='10'>35→40</text>
</svg>"""
    },
    {
        "title": "Rounding to the Nearest 100",
        "body": """<div class="concept-box">
<p>To round to the nearest 100, look at the <strong>tens digit</strong>:</p>
<ul>
<li>If the tens digit is <strong>0, 1, 2, 3, or 4</strong>, round <strong>DOWN</strong> (keep the hundreds digit the same)</li>
<li>If the tens digit is <strong>5, 6, 7, 8, or 9</strong>, round <strong>UP</strong> (add 1 to the hundreds digit)</li>
</ul>
</div>

<svg viewBox="0 0 600 300" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="300" y="20" text-anchor='middle' fill='#e6edf3' font-size='15' font-weight='bold'>Rounding to Nearest 100</text>

  <!-- Rule visualization -->
  <rect x="20" y="40" width="270" height="60" fill='#22c55e20' stroke='#22c55e' stroke-width="2" rx="4"/>
  <text x="155" y="60" text-anchor='middle' fill='#e6edf3' font-size='12' font-weight='bold'>Tens: 0, 1, 2, 3, 4</text>
  <text x="155" y="80" text-anchor='middle' fill='#e6edf3' font-size='12' font-weight='bold'>ROUND DOWN</text>

  <rect x="310" y="40" width="270" height="60" fill='#ec489920' stroke='#ec4899' stroke-width="2" rx="4"/>
  <text x="445" y="60" text-anchor='middle' fill='#e6edf3' font-size='12' font-weight='bold'>Tens: 5, 6, 7, 8, 9</text>
  <text x="445" y="80" text-anchor='middle' fill='#e6edf3' font-size='12' font-weight='bold'>ROUND UP</text>

  <!-- Examples -->
  <rect x="20" y="120" width="540" height="50" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="1" rx="3"/>
  <text x="30" y="140" text-anchor='start' fill='#e6edf3' font-size='11'><strong>Examples (Down):</strong> 214→200, 340→300, 449→400</text>
  <text x="30" y="155" text-anchor='start' fill='#e6edf3' font-size='11'>The hundreds digit stays the same when tens digit is 0-4.</text>

  <rect x="20" y="185" width="540" height="50" fill='#ec489920' stroke='#ec4899' stroke-width="1" rx="3"/>
  <text x="30" y="205" text-anchor='start' fill='#e6edf3' font-size='11'><strong>Examples (Up):</strong> 257→300, 375→400, 689→700, 956→1000</text>
  <text x="30" y="220" text-anchor='start' fill='#e6edf3' font-size='11'>The hundreds digit increases by 1 when tens digit is 5-9.</text>

  <!-- Worked example -->
  <rect x="20" y="245" width="540" height="50" fill='#f59e0b15' stroke='#f59e0b' stroke-width="1" rx="3"/>
  <text x="30" y="262" text-anchor='start' fill='#e6edf3' font-size='11'><strong>Example:</strong> Round 347 to nearest 100</text>
  <text x="30" y="277" text-anchor='start' fill='#e6edf3' font-size='11'>Tens digit = 4 (which is 0-4) → Round DOWN → Answer: 300</text>
</svg>"""
    },
    {
        "title": "Using Rounding for Estimation",
        "body": """<div class="concept-box">
<p>Rounding helps us estimate answers to math problems. We round first, then do the math with friendly numbers.</p>
</div>

<svg viewBox="0 0 600 260" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="300" y="20" text-anchor='middle' fill='#e6edf3' font-size='15' font-weight='bold'>Estimation Using Rounding</text>

  <!-- Example 1 -->
  <rect x="20" y="40" width="540" height="70" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="1" rx="3"/>
  <text x="30" y="60" text-anchor='start' fill='#e6edf3' font-size='12' font-weight='bold'>Example 1: Estimate 247 + 152</text>
  <text x="30" y="78" text-anchor='start' fill='#e6edf3' font-size='11'>Round 247→250, Round 152→150</text>
  <text x="30" y="93" text-anchor='start' fill='#e6edf3' font-size='11'>Estimated sum: 250 + 150 = 400 (actual: 399, very close!)</text>

  <!-- Example 2 -->
  <rect x="20" y="125" width="540" height="70" fill='#22c55e20' stroke='#22c55e' stroke-width="1" rx="3"/>
  <text x="30" y="145" text-anchor='start' fill='#e6edf3' font-size='12' font-weight='bold'>Example 2: Estimate 567 - 234</text>
  <text x="30" y="163" text-anchor='start' fill='#e6edf3' font-size='11'>Round 567→600, Round 234→200</text>
  <text x="30" y="178" text-anchor='start' fill='#e6edf3' font-size='11'>Estimated difference: 600 - 200 = 400 (actual: 333)</text>

  <!-- Why estimation matters -->
  <rect x="20" y="210" width="540" height="45" fill='#ec489915' stroke='#ec4899' stroke-width="1" stroke-dasharray="3,3" rx="3"/>
  <text x="30" y="230" text-anchor='start' fill='#e6edf3' font-size='11'><strong>Why estimate?</strong> Quick mental math check, real-world decisions (shopping, cooking, distance)</text>
</svg>"""
    },
    {
        "title": "Worked Example: Rounding",
        "body": """<div class="worked-example">
<p><strong>Question 1:</strong> Round 347 to the nearest 10.</p>
<p><strong>Step 1:</strong> Look at the ones digit: 7</p>
<p><strong>Step 2:</strong> 7 is in the 5-9 range, so round UP</p>
<p><strong>Step 3:</strong> The tens digit (4) increases by 1 → 5</p>
<p><strong>Answer:</strong> 347 rounds to <strong>350</strong></p>

<hr style="border:1px dashed #666;margin:10px 0;">

<p><strong>Question 2:</strong> Round 423 to the nearest 100.</p>
<p><strong>Step 1:</strong> Look at the tens digit: 2</p>
<p><strong>Step 2:</strong> 2 is in the 0-4 range, so round DOWN</p>
<p><strong>Step 3:</strong> The hundreds digit stays the same: 4</p>
<p><strong>Answer:</strong> 423 rounds to <strong>400</strong></p>
</div>"""
    }
]
