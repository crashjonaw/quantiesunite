"""Number Patterns: Skip Counting and Sequences"""

TITLE = "Number Patterns: Skip Counting and Sequences to 1000"

SECTIONS = [
    {
        "title": "Counting by 2s (Even Numbers)",
        "body": """<div class="concept-box">
<p>When we count by 2s, we skip every other number. These are called <strong>even numbers</strong>.</p>
<p>Start at 0 (or any even number) and keep adding 2: 0, 2, 4, 6, 8, ...</p>
</div>

<svg viewBox="0 0 600 220" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="300" y="22" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Counting by 2s (Even Numbers)</text>

  <!-- Number line -->
  <line x1="30" y1="70" x2="570" y2="70" stroke='#4f8ef7' stroke-width="2"/>

  <!-- Even numbers marked -->
  <circle cx="50" cy="70" r="6" fill='#4f8ef7'/>
  <text x="50" y="92" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>0</text>

  <circle cx="115" cy="70" r="6" fill='#4f8ef7'/>
  <text x="115" y="92" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>2</text>

  <circle cx="180" cy="70" r="6" fill='#4f8ef7'/>
  <text x="180" y="92" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>4</text>

  <circle cx="245" cy="70" r="6" fill='#4f8ef7'/>
  <text x="245" y="92" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>6</text>

  <circle cx="310" cy="70" r="6" fill='#4f8ef7'/>
  <text x="310" y="92" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>8</text>

  <circle cx="375" cy="70" r="6" fill='#4f8ef7'/>
  <text x="375" y="92" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>10</text>

  <text x="410" y="92" text-anchor='start' fill='currentColor' font-size='11'>...</text>

  <!-- Pattern box -->
  <rect x="20" y="118" width="560" height="82" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="1" rx="4"/>
  <text x="30" y="140" text-anchor='start' fill='currentColor' font-size='12' font-weight='bold'>Sequence by 2s:</text>
  <text x="30" y="160" text-anchor='start' fill='currentColor' font-size='11' font-family='monospace'>0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, ...</text>
  <text x="30" y="180" text-anchor='start' fill='currentColor' font-size='11'>Look at the ones place: always ends in 0, 2, 4, 6, or 8</text>
</svg>"""
    },
    {
        "title": "Counting by 5s",
        "body": """<div class="concept-box">
<p>When we count by 5s, we add 5 each time. These numbers are useful for telling time and counting money!</p>
</div>

<svg viewBox="0 0 600 220" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="300" y="22" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Counting by 5s (Skip Counting)</text>

  <!-- Number line -->
  <line x1="30" y1="70" x2="570" y2="70" stroke='#22c55e' stroke-width="2"/>

  <!-- Multiples of 5 marked -->
  <circle cx="50" cy="70" r="6" fill='#22c55e'/>
  <text x="50" y="92" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>0</text>

  <circle cx="115" cy="70" r="6" fill='#22c55e'/>
  <text x="115" y="92" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>5</text>

  <circle cx="180" cy="70" r="6" fill='#22c55e'/>
  <text x="180" y="92" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>10</text>

  <circle cx="245" cy="70" r="6" fill='#22c55e'/>
  <text x="245" y="92" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>15</text>

  <circle cx="310" cy="70" r="6" fill='#22c55e'/>
  <text x="310" y="92" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>20</text>

  <circle cx="375" cy="70" r="6" fill='#22c55e'/>
  <text x="375" y="92" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>25</text>

  <text x="410" y="92" text-anchor='start' fill='currentColor' font-size='11'>...</text>

  <!-- Pattern box -->
  <rect x="20" y="118" width="560" height="82" fill='#22c55e20' stroke='#22c55e' stroke-width="1" rx="4"/>
  <text x="30" y="140" text-anchor='start' fill='currentColor' font-size='12' font-weight='bold'>Sequence by 5s:</text>
  <text x="30" y="160" text-anchor='start' fill='currentColor' font-size='11' font-family='monospace'>0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, ...</text>
  <text x="30" y="180" text-anchor='start' fill='currentColor' font-size='11'>Look at the ones place: always ends in 0 or 5</text>
</svg>"""
    },
    {
        "title": "Counting by 10s",
        "body": """<div class="concept-box">
<p>Counting by 10s is the easiest! Add 10 each time. The tens digit changes, but the ones digit stays 0.</p>
</div>

<svg viewBox="0 0 560 280" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="280" y="22" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Counting by 10s (Decade Pattern)</text>

  <!-- Visual: columns showing tens -->
  <text x="20" y="50" text-anchor='start' fill='currentColor' font-size='12' font-weight='bold'>0 to 100:</text>
  <rect x="20" y="58" width="520" height="30" fill='#f59e0b20' stroke='#f59e0b' stroke-width="1" rx="4"/>
  <text x="280" y="78" text-anchor='middle' fill='currentColor' font-size='11' font-family='monospace'>0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100</text>

  <text x="20" y="112" text-anchor='start' fill='currentColor' font-size='12' font-weight='bold'>100 to 200:</text>
  <rect x="20" y="120" width="520" height="30" fill='#f59e0b20' stroke='#f59e0b' stroke-width="1" rx="4"/>
  <text x="280" y="140" text-anchor='middle' fill='currentColor' font-size='11' font-family='monospace'>100, 110, 120, ..., 190, 200</text>

  <text x="20" y="178" text-anchor='start' fill='currentColor' font-size='12' font-weight='bold'>Pattern Notice:</text>
  <rect x="20" y="188" width="520" height="80" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="1" rx="4"/>
  <text x="30" y="208" text-anchor='start' fill='currentColor' font-size='11'>When counting by 10s, only the TENS and HUNDREDS digits change!</text>
  <text x="30" y="224" text-anchor='start' fill='currentColor' font-size='11'>The ones place is always 0:</text>
  <text x="30" y="240" text-anchor='start' fill='currentColor' font-size='11' font-family='monospace'>10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, ...</text>
  <text x="30" y="256" text-anchor='start' fill='currentColor' font-size='11'>These are all MULTIPLES OF 10.</text>
</svg>"""
    },
    {
        "title": "Counting by 100s",
        "body": """<div class="concept-box">
<p>When we count by 100s, we add 100 each time. Only the <strong>hundreds digit</strong> changes!</p>
</div>

<svg viewBox="0 0 600 240" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="300" y="22" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Counting by 100s (Hundreds Pattern)</text>

  <!-- Number line for hundreds -->
  <line x1="40" y1="70" x2="560" y2="70" stroke='#4f8ef7' stroke-width="2"/>

  <circle cx="40" cy="70" r="6" fill='#4f8ef7'/>
  <text x="40" y="92" text-anchor='middle' fill='currentColor' font-size='10' font-weight='bold'>0</text>

  <circle cx="110" cy="70" r="6" fill='#4f8ef7'/>
  <text x="110" y="92" text-anchor='middle' fill='currentColor' font-size='10' font-weight='bold'>100</text>

  <circle cx="180" cy="70" r="6" fill='#4f8ef7'/>
  <text x="180" y="92" text-anchor='middle' fill='currentColor' font-size='10' font-weight='bold'>200</text>

  <circle cx="250" cy="70" r="6" fill='#4f8ef7'/>
  <text x="250" y="92" text-anchor='middle' fill='currentColor' font-size='10' font-weight='bold'>300</text>

  <circle cx="320" cy="70" r="6" fill='#4f8ef7'/>
  <text x="320" y="92" text-anchor='middle' fill='currentColor' font-size='10' font-weight='bold'>400</text>

  <circle cx="390" cy="70" r="6" fill='#4f8ef7'/>
  <text x="390" y="92" text-anchor='middle' fill='currentColor' font-size='10' font-weight='bold'>500</text>

  <circle cx="460" cy="70" r="6" fill='#4f8ef7'/>
  <text x="460" y="92" text-anchor='middle' fill='currentColor' font-size='10' font-weight='bold'>600</text>

  <circle cx="530" cy="70" r="6" fill='#4f8ef7'/>
  <text x="530" y="92" text-anchor='middle' fill='currentColor' font-size='10' font-weight='bold'>700</text>

  <text x="555" y="92" text-anchor='start' fill='currentColor' font-size='10'>...</text>

  <!-- Sequence -->
  <rect x="20" y="118" width="560" height="60" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="1" rx="4"/>
  <text x="30" y="140" text-anchor='start' fill='currentColor' font-size='12' font-weight='bold'>Sequence by 100s:</text>
  <text x="30" y="160" text-anchor='start' fill='currentColor' font-size='11' font-family='monospace'>0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000</text>

  <!-- Real-world use -->
  <rect x="20" y="194" width="560" height="30" fill='#22c55e15' stroke='#22c55e' stroke-width="1" stroke-dasharray="3,3" rx="4"/>
  <text x="30" y="214" text-anchor='start' fill='currentColor' font-size='11'>Real-world use: Counting money by $100 bills!</text>
</svg>"""
    },
    {
        "title": "Worked Example: Number Patterns",
        "body": """<div class="worked-example">
<p><strong>Question 1:</strong> Fill in the missing numbers. Count by 5s: 0, 5, 10, ___, ___, 25</p>
<p><strong>Answer:</strong> 15 and 20 (each time we add 5)</p>

<hr style="border:1px dashed #666;margin:10px 0;">

<p><strong>Question 2:</strong> What is the next number in this sequence? 200, 300, 400, ___</p>
<p><strong>Answer:</strong> 500 (counting by 100s, so we add 100)</p>

<hr style="border:1px dashed #666;margin:10px 0;">

<p><strong>Question 3:</strong> Count by 10s starting from 350. Write the next three numbers.</p>
<p><strong>Answer:</strong> 360, 370, 380 (add 10 each time)</p>
</div>"""
    }
]
