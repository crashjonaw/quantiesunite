"""Place Value: Hundreds, Tens, Ones"""

TITLE = "Understanding Place Value: Hundreds, Tens, and Ones"

SECTIONS = [
    {
        "title": "What is Place Value?",
        "body": """<div class="concept-box">
<p>Every digit in a number has a <strong>place value</strong> depending on where it sits. In the number <strong>347</strong>, the <strong>3</strong> is worth 300 because it's in the <strong>hundreds place</strong>.</p>
<p><strong>Key idea:</strong> The same digit can have different values based on its position!</p>
</div>

<svg viewBox="0 0 520 200" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="260" y="25" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Digit Position Changes Value</text>

  <!-- 7 in ones place -->
  <circle cx="90" cy="80" r="35" fill='#f59e0b30' stroke='#f59e0b' stroke-width="2"/>
  <text x="90" y="86" text-anchor='middle' fill='currentColor' font-size='28' font-weight='bold'>7</text>
  <text x="90" y="135" text-anchor='middle' fill='currentColor' font-size='12'>7 ones = 7</text>

  <!-- 7 in tens place -->
  <circle cx="260" cy="80" r="35" fill='#22c55e30' stroke='#22c55e' stroke-width="2"/>
  <text x="260" y="86" text-anchor='middle' fill='currentColor' font-size='28' font-weight='bold'>7</text>
  <text x="260" y="135" text-anchor='middle' fill='currentColor' font-size='12'>7 tens = 70</text>

  <!-- 7 in hundreds place -->
  <circle cx="430" cy="80" r="35" fill='#4f8ef730' stroke='#4f8ef7' stroke-width="2"/>
  <text x="430" y="86" text-anchor='middle' fill='currentColor' font-size='28' font-weight='bold'>7</text>
  <text x="430" y="135" text-anchor='middle' fill='currentColor' font-size='12'>7 hundreds = 700</text>

  <text x="260" y="180" text-anchor='middle' fill='currentColor' font-size='13'>Same digit, different positions = different values!</text>
</svg>"""
    },
    {
        "title": "The Hundreds Place",
        "body": """<div class="concept-box">
<p>Remember: <strong>10 tens make 1 hundred</strong>. When you count past 99, you need a new place — the hundreds!</p>
<p>\(99 + 1 = \)<strong>100</strong> (one hundred)</p>
</div>

<svg viewBox="0 0 450 225" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="225" y="20" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Building 100: 10 tens = 1 hundred</text>

  <!-- 10 ten-rods arranged in two rows of 5 -->
  <!-- Row 1: rods 1-5 -->
  <rect x="20" y="42" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="4"/>
  <text x="29" y="76" text-anchor='middle' fill='currentColor' font-size='9' font-weight='bold'>10</text>

  <rect x="44" y="42" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="4"/>
  <text x="53" y="76" text-anchor='middle' fill='currentColor' font-size='9' font-weight='bold'>10</text>

  <rect x="68" y="42" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="4"/>
  <text x="77" y="76" text-anchor='middle' fill='currentColor' font-size='9' font-weight='bold'>10</text>

  <rect x="92" y="42" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="4"/>
  <text x="101" y="76" text-anchor='middle' fill='currentColor' font-size='9' font-weight='bold'>10</text>

  <rect x="116" y="42" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="4"/>
  <text x="125" y="76" text-anchor='middle' fill='currentColor' font-size='9' font-weight='bold'>10</text>

  <!-- Row 2: rods 6-10 -->
  <rect x="20" y="112" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="4"/>
  <text x="29" y="146" text-anchor='middle' fill='currentColor' font-size='9' font-weight='bold'>10</text>

  <rect x="44" y="112" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="4"/>
  <text x="53" y="146" text-anchor='middle' fill='currentColor' font-size='9' font-weight='bold'>10</text>

  <rect x="68" y="112" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="4"/>
  <text x="77" y="146" text-anchor='middle' fill='currentColor' font-size='9' font-weight='bold'>10</text>

  <rect x="92" y="112" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="4"/>
  <text x="101" y="146" text-anchor='middle' fill='currentColor' font-size='9' font-weight='bold'>10</text>

  <rect x="116" y="112" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="4"/>
  <text x="125" y="146" text-anchor='middle' fill='currentColor' font-size='9' font-weight='bold'>10</text>

  <text x="77" y="192" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>10 tens</text>

  <!-- Arrow -->
  <line x1="155" y1="106" x2="220" y2="106" stroke='#ec4899' stroke-width="2.5"/>
  <polygon points="220,99 235,106 220,113" fill='#ec4899'/>
  <text x="195" y="95" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>group up!</text>

  <!-- 1 hundred block (10x10 grid) -->
  <rect x="260" y="40" width="130" height="130" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="3" rx="4"/>
  <!-- Grid lines -->
  <line x1="273" y1="40" x2="273" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="286" y1="40" x2="286" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="299" y1="40" x2="299" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="312" y1="40" x2="312" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="325" y1="40" x2="325" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="338" y1="40" x2="338" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="351" y1="40" x2="351" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="364" y1="40" x2="364" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="377" y1="40" x2="377" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="260" y1="53" x2="390" y2="53" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="260" y1="66" x2="390" y2="66" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="260" y1="79" x2="390" y2="79" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="260" y1="92" x2="390" y2="92" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="260" y1="105" x2="390" y2="105" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="260" y1="118" x2="390" y2="118" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="260" y1="131" x2="390" y2="131" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="260" y1="144" x2="390" y2="144" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="260" y1="157" x2="390" y2="157" stroke='#4f8ef730' stroke-width="0.5"/>
  <text x="325" y="112" text-anchor='middle' fill='currentColor' font-size='22' font-weight='bold'>100</text>
  <text x="325" y="192" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>1 hundred block</text>

  <!-- Equals sign at bottom -->
  <text x="225" y="212" text-anchor='middle' fill='currentColor' font-size='13'>10 x 10 = <tspan font-weight='bold' fill='#4f8ef7'>100</tspan></text>
</svg>"""
    },
    {
        "title": "347 in Base-10 Blocks",
        "body": """<div class="concept-box">
<p>Let's break down <strong>347</strong> using base-10 blocks. Each block type represents a different place value:</p>
<ul>
<li><strong class="accent-heading">Large square</strong> = 1 hundred (100)</li>
<li><strong style="color:#22c55e;">Rod</strong> = 1 ten (10)</li>
<li><strong style="color:#f59e0b;">Tiny square</strong> = 1 one (1)</li>
</ul>
</div>

<svg viewBox="0 0 490 250" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="245" y="20" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>347 in Base-10 Blocks</text>

  <!-- Hundreds (3 large squares) -->
  <rect x="15" y="45" width="60" height="60" fill='#4f8ef740' stroke='#4f8ef7' stroke-width="2" rx="4"/>
  <text x="45" y="80" text-anchor='middle' fill='currentColor' font-size='11'>100</text>

  <rect x="85" y="45" width="60" height="60" fill='#4f8ef740' stroke='#4f8ef7' stroke-width="2" rx="4"/>
  <text x="115" y="80" text-anchor='middle' fill='currentColor' font-size='11'>100</text>

  <rect x="155" y="45" width="60" height="60" fill='#4f8ef740' stroke='#4f8ef7' stroke-width="2" rx="4"/>
  <text x="185" y="80" text-anchor='middle' fill='currentColor' font-size='11'>100</text>

  <!-- Tens (4 rods) -->
  <rect x="250" y="45" width="14" height="60" fill='#22c55e60' stroke='#22c55e' stroke-width="1.5" rx="4"/>
  <rect x="272" y="45" width="14" height="60" fill='#22c55e60' stroke='#22c55e' stroke-width="1.5" rx="4"/>
  <rect x="294" y="45" width="14" height="60" fill='#22c55e60' stroke='#22c55e' stroke-width="1.5" rx="4"/>
  <rect x="316" y="45" width="14" height="60" fill='#22c55e60' stroke='#22c55e' stroke-width="1.5" rx="4"/>

  <!-- Ones (7 small squares) -->
  <rect x="365" y="80" width="14" height="14" fill='#f59e0b60' stroke='#f59e0b' stroke-width="1" rx="4"/>
  <rect x="383" y="80" width="14" height="14" fill='#f59e0b60' stroke='#f59e0b' stroke-width="1" rx="4"/>
  <rect x="401" y="80" width="14" height="14" fill='#f59e0b60' stroke='#f59e0b' stroke-width="1" rx="4"/>
  <rect x="419" y="80" width="14" height="14" fill='#f59e0b60' stroke='#f59e0b' stroke-width="1" rx="4"/>
  <rect x="365" y="60" width="14" height="14" fill='#f59e0b60' stroke='#f59e0b' stroke-width="1" rx="4"/>
  <rect x="383" y="60" width="14" height="14" fill='#f59e0b60' stroke='#f59e0b' stroke-width="1" rx="4"/>
  <rect x="401" y="60" width="14" height="14" fill='#f59e0b60' stroke='#f59e0b' stroke-width="1" rx="4"/>

  <!-- Labels -->
  <text x="115" y="130" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>3 hundreds</text>
  <text x="115" y="145" text-anchor='middle' fill='currentColor' font-size='11'>= 300</text>

  <text x="290" y="130" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>4 tens</text>
  <text x="290" y="145" text-anchor='middle' fill='currentColor' font-size='11'>= 40</text>

  <text x="400" y="130" text-anchor='middle' fill='currentColor' font-size='12' font-weight='bold'>7 ones</text>
  <text x="400" y="145" text-anchor='middle' fill='currentColor' font-size='11'>= 7</text>

  <!-- Final answer box -->
  <rect x="70" y="175" width="350" height="50" fill='none' stroke='#ec4899' stroke-width="2" stroke-dasharray="5,5" rx="4"/>
  <text x="245" y="205" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>300 + 40 + 7 = 347</text>
</svg>"""
    },
    {
        "title": "Place Value Chart",
        "body": """<div class="concept-box">
<p>A place value chart helps us see the value of each digit clearly. Write the number <strong>582</strong> in the chart:</p>
</div>

<svg viewBox="0 0 500 185" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="250" y="20" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>Number 582 in Place Value Chart</text>

  <!-- Table grid -->
  <rect x="30" y="40" width="140" height="55" fill='none' stroke='#4f8ef7' stroke-width="2" rx='4'/>
  <rect x="180" y="40" width="140" height="55" fill='none' stroke='#22c55e' stroke-width="2" rx='4'/>
  <rect x="330" y="40" width="140" height="55" fill='none' stroke='#f59e0b' stroke-width="2" rx='4'/>

  <!-- Dividers -->
  <line x1="30" y1="65" x2="470" y2="65" stroke='#808080' stroke-width="1"/>

  <!-- Headers -->
  <text x="100" y="60" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>Hundreds</text>
  <text x="250" y="60" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>Tens</text>
  <text x="400" y="60" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>Ones</text>

  <!-- Values -->
  <text x="100" y="90" text-anchor='middle' fill='#4f8ef7' font-size='24' font-weight='bold'>5</text>
  <text x="250" y="90" text-anchor='middle' fill='#22c55e' font-size='24' font-weight='bold'>8</text>
  <text x="400" y="90" text-anchor='middle' fill='#f59e0b' font-size='24' font-weight='bold'>2</text>

  <!-- Expanded form below -->
  <text x="30" y="130" text-anchor='start' fill='currentColor' font-size='12'>Expanded form:</text>
  <text x="30" y="155" text-anchor='start' fill='currentColor' font-size='12' font-family='monospace'>582 = (5 x 100) + (8 x 10) + (2 x 1)</text>
</svg>"""
    },
    {
        "title": "Worked Example: 634",
        "body": """<div class="worked-example">
<p><strong>Question:</strong> Break down 634 using place value.</p>
<p><strong>Step 1:</strong> Identify each digit and its place.</p>
<ul>
<li>6 is in the <strong>hundreds</strong> place</li>
<li>3 is in the <strong>tens</strong> place</li>
<li>4 is in the <strong>ones</strong> place</li>
</ul>
<p><strong>Step 2:</strong> Find the value of each digit.</p>
<ul>
<li>6 hundreds = \(6 \times 100 = \)<strong>600</strong></li>
<li>3 tens = \(3 \times 10 = \)<strong>30</strong></li>
<li>4 ones = \(4 \times 1 = \)<strong>4</strong></li>
</ul>
<p><strong>Step 3:</strong> Write in expanded form.</p>
<p>$$634 = 600 + 30 + 4$$</p>
<p>Or: \\(634 = (6 \\times 100) + (3 \\times 10) + (4 \\times 1)\\)</p>
</div>"""
    }
]
