"""Place Value: Hundreds, Tens, Ones"""

TITLE = "Understanding Place Value: Hundreds, Tens, and Ones"

SECTIONS = [
    {
        "title": "What is Place Value?",
        "body": """<div class="concept-box">
<p>Every digit in a number has a <strong>place value</strong> depending on where it sits. In the number <strong>347</strong>, the <strong>3</strong> is worth 300 because it's in the <strong>hundreds place</strong>.</p>
<p><strong>Key idea:</strong> The same digit can have different values based on its position!</p>
</div>

<svg viewBox="0 0 600 200" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="300" y="25" text-anchor='middle' fill='currentColor' font-size='16' font-weight='bold'>Digit Position Changes Value</text>

  <!-- First row: 7 in ones place -->
  <circle cx="80" cy="80" r="35" fill='#f59e0b30' stroke='#f59e0b' stroke-width="2"/>
  <text x="80" y="85" text-anchor='middle' fill='#f59e0b' font-size='28' font-weight='bold'>7</text>
  <text x="80" y="140" text-anchor='middle' fill='currentColor' font-size='12'>7 ones = 7</text>

  <!-- Second row: 7 in tens place -->
  <circle cx="240" cy="80" r="35" fill='#22c55e30' stroke='#22c55e' stroke-width="2"/>
  <text x="240" y="85" text-anchor='middle' fill='#22c55e' font-size='28' font-weight='bold'>7</text>
  <text x="240" y="140" text-anchor='middle' fill='currentColor' font-size='12'>7 tens = 70</text>

  <!-- Third row: 7 in hundreds place -->
  <circle cx="400" cy="80" r="35" fill='#4f8ef730' stroke='#4f8ef7' stroke-width="2"/>
  <text x="400" y="85" text-anchor='middle' fill='#4f8ef7' font-size='28' font-weight='bold'>7</text>
  <text x="400" y="140" text-anchor='middle' fill='currentColor' font-size='12'>7 hundreds = 700</text>

  <text x="300" y="180" text-anchor='middle' fill='currentColor' font-size='14'>Same digit, different positions = different values!</text>
</svg>"""
    },
    {
        "title": "The Hundreds Place",
        "body": """<div class="concept-box">
<p>Remember: <strong>10 tens make 1 hundred</strong>. When you count past 99, you need a new place — the hundreds!</p>
<p>\(99 + 1 = \)<strong>100</strong> (one hundred)</p>
</div>

<svg viewBox="0 0 520 220" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="260" y="22" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Building 100: 10 tens = 1 hundred</text>

  <!-- 10 ten-rods arranged in two rows of 5 -->
  <!-- Row 1: rods 1-5 -->
  <rect x="20" y="42" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="2"/>
  <text x="29" y="76" text-anchor='middle' fill='#22c55e' font-size='9' font-weight='bold'>10</text>

  <rect x="44" y="42" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="2"/>
  <text x="53" y="76" text-anchor='middle' fill='#22c55e' font-size='9' font-weight='bold'>10</text>

  <rect x="68" y="42" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="2"/>
  <text x="77" y="76" text-anchor='middle' fill='#22c55e' font-size='9' font-weight='bold'>10</text>

  <rect x="92" y="42" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="2"/>
  <text x="101" y="76" text-anchor='middle' fill='#22c55e' font-size='9' font-weight='bold'>10</text>

  <rect x="116" y="42" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="2"/>
  <text x="125" y="76" text-anchor='middle' fill='#22c55e' font-size='9' font-weight='bold'>10</text>

  <!-- Row 2: rods 6-10 -->
  <rect x="20" y="110" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="2"/>
  <text x="29" y="144" text-anchor='middle' fill='#22c55e' font-size='9' font-weight='bold'>10</text>

  <rect x="44" y="110" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="2"/>
  <text x="53" y="144" text-anchor='middle' fill='#22c55e' font-size='9' font-weight='bold'>10</text>

  <rect x="68" y="110" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="2"/>
  <text x="77" y="144" text-anchor='middle' fill='#22c55e' font-size='9' font-weight='bold'>10</text>

  <rect x="92" y="110" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="2"/>
  <text x="101" y="144" text-anchor='middle' fill='#22c55e' font-size='9' font-weight='bold'>10</text>

  <rect x="116" y="110" width="18" height="60" fill='#22c55e40' stroke='#22c55e' stroke-width="1.5" rx="2"/>
  <text x="125" y="144" text-anchor='middle' fill='#22c55e' font-size='9' font-weight='bold'>10</text>

  <text x="77" y="192" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>10 tens</text>

  <!-- Arrow -->
  <line x1="170" y1="106" x2="250" y2="106" stroke='#ec4899' stroke-width="2.5"/>
  <polygon points="250,99 265,106 250,113" fill='#ec4899'/>
  <text x="217" y="95" text-anchor='middle' fill='#ec4899' font-size='11' font-weight='bold'>group up!</text>

  <!-- 1 hundred block (10x10 grid to show 100 units) -->
  <rect x="290" y="40" width="130" height="130" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="3" rx="5"/>
  <!-- Grid lines to show 10x10 = 100 -->
  <line x1="303" y1="40" x2="303" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="316" y1="40" x2="316" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="329" y1="40" x2="329" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="342" y1="40" x2="342" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="355" y1="40" x2="355" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="368" y1="40" x2="368" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="381" y1="40" x2="381" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="394" y1="40" x2="394" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="407" y1="40" x2="407" y2="170" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="290" y1="53" x2="420" y2="53" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="290" y1="66" x2="420" y2="66" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="290" y1="79" x2="420" y2="79" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="290" y1="92" x2="420" y2="92" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="290" y1="105" x2="420" y2="105" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="290" y1="118" x2="420" y2="118" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="290" y1="131" x2="420" y2="131" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="290" y1="144" x2="420" y2="144" stroke='#4f8ef730' stroke-width="0.5"/>
  <line x1="290" y1="157" x2="420" y2="157" stroke='#4f8ef730' stroke-width="0.5"/>
  <text x="355" y="112" text-anchor='middle' fill='#4f8ef7' font-size='22' font-weight='bold'>100</text>
  <text x="355" y="192" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>1 hundred block</text>

  <!-- Equals sign at bottom -->
  <text x="260" y="210" text-anchor='middle' fill='currentColor' font-size='13'>10 × 10 = <tspan font-weight='bold' fill='#4f8ef7'>100</tspan></text>
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

<svg viewBox="0 0 550 250" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="275" y="20" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>347 in Base-10 Blocks</text>

  <!-- Hundreds (3 large squares) -->
  <rect x="15" y="45" width="60" height="60" fill='#4f8ef740' stroke='#4f8ef7' stroke-width="2" rx="3"/>
  <text x="45" y="78" text-anchor='middle' fill='currentColor' font-size='11'>100</text>

  <rect x="85" y="45" width="60" height="60" fill='#4f8ef740' stroke='#4f8ef7' stroke-width="2" rx="3"/>
  <text x="115" y="78" text-anchor='middle' fill='currentColor' font-size='11'>100</text>

  <rect x="155" y="45" width="60" height="60" fill='#4f8ef740' stroke='#4f8ef7' stroke-width="2" rx="3"/>
  <text x="185" y="78" text-anchor='middle' fill='currentColor' font-size='11'>100</text>

  <!-- Tens (4 rods) -->
  <rect x="250" y="45" width="12" height="60" fill='#22c55e60' stroke='#22c55e' stroke-width="1.5" rx="2"/>
  <rect x="270" y="45" width="12" height="60" fill='#22c55e60' stroke='#22c55e' stroke-width="1.5" rx="2"/>
  <rect x="290" y="45" width="12" height="60" fill='#22c55e60' stroke='#22c55e' stroke-width="1.5" rx="2"/>
  <rect x="310" y="45" width="12" height="60" fill='#22c55e60' stroke='#22c55e' stroke-width="1.5" rx="2"/>

  <!-- Ones (7 small squares) -->
  <rect x="360" y="80" width="12" height="12" fill='#f59e0b60' stroke='#f59e0b' stroke-width="1" rx="1"/>
  <rect x="375" y="80" width="12" height="12" fill='#f59e0b60' stroke='#f59e0b' stroke-width="1" rx="1"/>
  <rect x="390" y="80" width="12" height="12" fill='#f59e0b60' stroke='#f59e0b' stroke-width="1" rx="1"/>
  <rect x="405" y="80" width="12" height="12" fill='#f59e0b60' stroke='#f59e0b' stroke-width="1" rx="1"/>
  <rect x="420" y="80" width="12" height="12" fill='#f59e0b60' stroke='#f59e0b' stroke-width="1" rx="1"/>
  <rect x="435" y="80" width="12" height="12" fill='#f59e0b60' stroke='#f59e0b' stroke-width="1" rx="1"/>
  <rect x="450" y="80" width="12" height="12" fill='#f59e0b60' stroke='#f59e0b' stroke-width="1" rx="1"/>

  <!-- Labels -->
  <text x="100" y="130" text-anchor='middle' fill='#4f8ef7' font-size='12' font-weight='bold'>3 hundreds</text>
  <text x="100" y="145" text-anchor='middle' fill='#4f8ef7' font-size='11'>= 300</text>

  <text x="280" y="130" text-anchor='middle' fill='#22c55e' font-size='12' font-weight='bold'>4 tens</text>
  <text x="280" y="145" text-anchor='middle' fill='#22c55e' font-size='11'>= 40</text>

  <text x="410" y="130" text-anchor='middle' fill='#f59e0b' font-size='12' font-weight='bold'>7 ones</text>
  <text x="410" y="145" text-anchor='middle' fill='#f59e0b' font-size='11'>= 7</text>

  <!-- Final answer box -->
  <rect x="100" y="180" width="350" height="50" fill='none' stroke='#ec4899' stroke-width="2" stroke-dasharray="5,5" rx="4"/>
  <text x="275" y="205" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>300 + 40 + 7 = 347</text>
</svg>"""
    },
    {
        "title": "Place Value Chart",
        "body": """<div class="concept-box">
<p>A place value chart helps us see the value of each digit clearly. Write the number <strong>582</strong> in the chart:</p>
</div>

<svg viewBox="0 0 500 180" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="250" y="20" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>Number 582 in Place Value Chart</text>

  <!-- Table grid -->
  <rect x="30" y="40" width="140" height="50" fill='none' stroke='#4f8ef7' stroke-width="2" rx='4'/>
  <rect x="170" y="40" width="140" height="50" fill='none' stroke='#22c55e' stroke-width="2" rx='4'/>
  <rect x="310" y="40" width="140" height="50" fill='none' stroke='#f59e0b' stroke-width="2" rx='4'/>

  <!-- Dividers -->
  <line x1="30" y1="65" x2="450" y2="65" stroke='#808080' stroke-width="1"/>

  <!-- Headers -->
  <text x="100" y="60" text-anchor='middle' fill='#4f8ef7' font-size='13' font-weight='bold'>Hundreds</text>
  <text x="240" y="60" text-anchor='middle' fill='#22c55e' font-size='13' font-weight='bold'>Tens</text>
  <text x="380" y="60" text-anchor='middle' fill='#f59e0b' font-size='13' font-weight='bold'>Ones</text>

  <!-- Values -->
  <text x="100" y="88" text-anchor='middle' fill='#4f8ef7' font-size='24' font-weight='bold'>5</text>
  <text x="240" y="88" text-anchor='middle' fill='#22c55e' font-size='24' font-weight='bold'>8</text>
  <text x="380" y="88" text-anchor='middle' fill='#f59e0b' font-size='24' font-weight='bold'>2</text>

  <!-- Expanded form below -->
  <text x="30" y="135" text-anchor='start' fill='currentColor' font-size='12'>Expanded form:</text>
  <text x="30" y="160" text-anchor='start' fill='currentColor' font-size='12' font-family='monospace'>582 = (5 × 100) + (8 × 10) + (2 × 1)</text>
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
