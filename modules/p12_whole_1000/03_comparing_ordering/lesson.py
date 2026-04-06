"""Comparing and Ordering Numbers to 1000"""

TITLE = "Comparing and Ordering Numbers to 1000"

SECTIONS = [
    {
        "title": "Comparison Symbols: > < =",
        "body": """<div class="concept-box">
<p>We use three special symbols to compare numbers:</p>
<ul>
<li><strong>&gt;</strong> means <strong>greater than</strong> (the bigger number is on the left)</li>
<li><strong>&lt;</strong> means <strong>less than</strong> (the smaller number is on the left)</li>
<li><strong>=</strong> means <strong>equal to</strong> (both numbers are the same)</li>
</ul>
<p><strong>Memory tip:</strong> The <strong>open mouth of &gt; and &lt; always points to the SMALLER number!</strong></p>
</div>

<svg viewBox="0 0 600 205" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="300" y="22" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Comparison Symbols</text>

  <!-- Greater than example -->
  <rect x="20" y="45" width="175" height="65" fill='#4f8ef730' stroke='#4f8ef7' stroke-width="2" rx="4"/>
  <text x="108" y="72" text-anchor='middle' fill='currentColor' font-size='20' font-weight='bold'>487 > 312</text>
  <text x="108" y="95" text-anchor='middle' fill='currentColor' font-size='11'>487 is greater than 312</text>

  <!-- Less than example -->
  <rect x="210" y="45" width="175" height="65" fill='#22c55e30' stroke='#22c55e' stroke-width="2" rx="4"/>
  <text x="298" y="72" text-anchor='middle' fill='currentColor' font-size='20' font-weight='bold'>156 &lt; 329</text>
  <text x="298" y="95" text-anchor='middle' fill='currentColor' font-size='11'>156 is less than 329</text>

  <!-- Equals example -->
  <rect x="400" y="45" width="175" height="65" fill='#f59e0b30' stroke='#f59e0b' stroke-width="2" rx="4"/>
  <text x="488" y="72" text-anchor='middle' fill='currentColor' font-size='20' font-weight='bold'>500 = 500</text>
  <text x="488" y="95" text-anchor='middle' fill='currentColor' font-size='11'>500 is equal to 500</text>

  <!-- Mouth tip explanation -->
  <rect x="20" y="130" width="560" height="55" fill='#ec489915' stroke='#ec4899' stroke-width="1" stroke-dasharray="3,3" rx="4"/>
  <text x="30" y="152" text-anchor='start' fill='currentColor' font-size='11' font-weight='bold'>Mouth Tip:</text>
  <text x="30" y="168" text-anchor='start' fill='currentColor' font-size='11'>The open side of the symbol ALWAYS points to the smaller number.</text>
  <text x="30" y="180" text-anchor='start' fill='currentColor' font-size='11'>487 > 312  (mouth points at 312, the smaller number)</text>
</svg>"""
    },
    {
        "title": "Comparing Two Numbers",
        "body": """<div class="concept-box">
<p>To compare two numbers, check each place from LEFT to RIGHT (hundreds first):</p>
<ol>
<li>Compare the <strong>hundreds digits</strong></li>
<li>If they're the same, compare the <strong>tens digits</strong></li>
<li>If those are the same too, compare the <strong>ones digits</strong></li>
</ol>
</div>

<svg viewBox="0 0 600 275" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="300" y="22" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Step-by-Step Comparison</text>

  <!-- Example 1 -->
  <rect x="20" y="42" width="560" height="62" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="1" rx="4"/>
  <text x="30" y="62" text-anchor='start' fill='currentColor' font-size='12' font-weight='bold'>Compare 643 and 628:</text>
  <text x="30" y="80" text-anchor='start' fill='currentColor' font-size='11'>Hundreds: 6 = 6 (same) -- Check tens next</text>
  <text x="30" y="96" text-anchor='start' fill='currentColor' font-size='11'>Tens: 4 > 2 -- So <tspan font-weight='bold'>643 > 628</tspan></text>

  <!-- Example 2 -->
  <rect x="20" y="116" width="560" height="62" fill='#22c55e20' stroke='#22c55e' stroke-width="1" rx="4"/>
  <text x="30" y="136" text-anchor='start' fill='currentColor' font-size='12' font-weight='bold'>Compare 517 and 592:</text>
  <text x="30" y="154" text-anchor='start' fill='currentColor' font-size='11'>Hundreds: 5 = 5 (same) -- Check tens next</text>
  <text x="30" y="170" text-anchor='start' fill='currentColor' font-size='11'>Tens: 1 &lt; 9 -- So <tspan font-weight='bold'>517 &lt; 592</tspan></text>

  <!-- Example 3 -->
  <rect x="20" y="190" width="560" height="62" fill='#f59e0b20' stroke='#f59e0b' stroke-width="1" rx="4"/>
  <text x="30" y="210" text-anchor='start' fill='currentColor' font-size='12' font-weight='bold'>Compare 834 and 831:</text>
  <text x="30" y="228" text-anchor='start' fill='currentColor' font-size='11'>Hundreds: 8 = 8, Tens: 3 = 3 (same) -- Check ones</text>
  <text x="30" y="244" text-anchor='start' fill='currentColor' font-size='11'>Ones: 4 > 1 -- So <tspan font-weight='bold'>834 > 831</tspan></text>
</svg>"""
    },
    {
        "title": "Ordering Numbers on a Number Line",
        "body": """<div class="concept-box">
<p>A number line shows numbers in order from smallest (left) to biggest (right). It helps us see which numbers are greater or smaller.</p>
</div>

<svg viewBox="0 0 600 200" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="300" y="22" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Number Line from 500 to 700</text>

  <!-- Main number line -->
  <line x1="40" y1="90" x2="560" y2="90" stroke='#4f8ef7' stroke-width="2"/>

  <!-- Tick marks and labels -->
  <line x1="40" y1="85" x2="40" y2="95" stroke='#4f8ef7' stroke-width="2"/>
  <text x="40" y="112" text-anchor='middle' fill='currentColor' font-size='11'>500</text>

  <line x1="170" y1="85" x2="170" y2="95" stroke='#808080' stroke-width="1"/>
  <text x="170" y="112" text-anchor='middle' fill='currentColor' font-size='10'>550</text>

  <line x1="300" y1="85" x2="300" y2="95" stroke='#4f8ef7' stroke-width="2"/>
  <text x="300" y="112" text-anchor='middle' fill='currentColor' font-size='11'>600</text>

  <line x1="430" y1="85" x2="430" y2="95" stroke='#808080' stroke-width="1"/>
  <text x="430" y="112" text-anchor='middle' fill='currentColor' font-size='10'>650</text>

  <line x1="560" y1="85" x2="560" y2="95" stroke='#4f8ef7' stroke-width="2"/>
  <text x="560" y="112" text-anchor='middle' fill='currentColor' font-size='11'>700</text>

  <!-- Place some numbers with labels above -->
  <circle cx="118" cy="65" r="5" fill='#ec4899'/>
  <text x="118" y="55" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>530</text>
  <line x1="118" y1="70" x2="118" y2="90" stroke='#ec4899' stroke-width="1" stroke-dasharray="3,3"/>

  <circle cx="274" cy="65" r="5" fill='#22c55e'/>
  <text x="274" y="55" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>590</text>
  <line x1="274" y1="70" x2="274" y2="90" stroke='#22c55e' stroke-width="1" stroke-dasharray="3,3"/>

  <circle cx="404" cy="65" r="5" fill='#f59e0b'/>
  <text x="404" y="55" text-anchor='middle' fill='currentColor' font-size='11' font-weight='bold'>640</text>
  <line x1="404" y1="70" x2="404" y2="90" stroke='#f59e0b' stroke-width="1" stroke-dasharray="3,3"/>

  <!-- Order at bottom -->
  <text x="30" y="150" text-anchor='start' fill='currentColor' font-size='12' font-weight='bold'>In order:</text>
  <text x="30" y="170" text-anchor='start' fill='currentColor' font-size='12'>500 &lt; 530 &lt; 590 &lt; 600 &lt; 640 &lt; 700</text>
</svg>"""
    },
    {
        "title": "Ordering a List of Numbers",
        "body": """<div class="concept-box">
<p>To put numbers in order from smallest to largest (or largest to smallest), compare them carefully:</p>
<p><strong>Smallest to Largest:</strong> Start with the smallest and move up.<br>
<strong>Largest to Smallest:</strong> Start with the largest and move down.</p>
</div>

<svg viewBox="0 0 600 260" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="300" y="22" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Ordering Numbers Practice</text>

  <!-- Example 1 -->
  <rect x="20" y="42" width="560" height="90" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="1" rx="4"/>
  <text x="30" y="62" text-anchor='start' fill='currentColor' font-size='12' font-weight='bold'>Order from smallest to largest: 325, 523, 253</text>
  <text x="30" y="80" text-anchor='start' fill='currentColor' font-size='11'>Step 1: Compare hundreds: 2__ is smallest, 5__ is largest</text>
  <text x="30" y="96" text-anchor='start' fill='currentColor' font-size='11'>Step 2: Between 325 and 523, which is smaller? 325 &lt; 523</text>
  <text x="30" y="114" text-anchor='start' fill='currentColor' font-size='12' font-weight='bold'>Answer: 253 &lt; 325 &lt; 523</text>

  <!-- Example 2 -->
  <rect x="20" y="146" width="560" height="90" fill='#22c55e20' stroke='#22c55e' stroke-width="1" rx="4"/>
  <text x="30" y="166" text-anchor='start' fill='currentColor' font-size='12' font-weight='bold'>Order from largest to smallest: 789, 879, 798</text>
  <text x="30" y="184" text-anchor='start' fill='currentColor' font-size='11'>Step 1: Compare hundreds: All start with 7 or 8</text>
  <text x="30" y="200" text-anchor='start' fill='currentColor' font-size='11'>Step 2: 8__ is the largest. Between 879 and 798 from the remaining</text>
  <text x="30" y="218" text-anchor='start' fill='currentColor' font-size='12' font-weight='bold'>Answer: 879 > 798 > 789</text>
</svg>"""
    },
    {
        "title": "Worked Example: Comparing and Ordering",
        "body": """<div class="worked-example">
<p><strong>Question:</strong> Put these numbers in order from smallest to largest: 612, 621, 261</p>

<p><strong>Step 1:</strong> Look at the hundreds digit.</p>
<ul>
<li>261 has 2 hundreds (smallest)</li>
<li>612 and 621 both have 6 hundreds (larger)</li>
</ul>

<p><strong>Step 2:</strong> Compare 612 and 621 (both have 6 hundreds).</p>
<ul>
<li>612 has 1 ten</li>
<li>621 has 2 tens</li>
<li>1 &lt; 2, so 612 &lt; 621</li>
</ul>

<p><strong>Final Answer:</strong></p>
<p>$$261 &lt; 612 &lt; 621$$</p>
</div>"""
    }
]
