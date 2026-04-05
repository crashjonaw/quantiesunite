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

<svg viewBox="0 0 600 200" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="300" y="20" text-anchor='middle' fill='#e6edf3' font-size='15' font-weight='bold'>Comparison Symbols</text>

  <!-- Greater than example -->
  <rect x="30" y="45" width="170" height="65" fill='#4f8ef730' stroke='#4f8ef7' stroke-width="2" rx="4"/>
  <text x="115" y="70" text-anchor='middle' fill='#e6edf3' font-size='20' font-weight='bold'>487 &gt; 312</text>
  <text x="115" y="95" text-anchor='middle' fill='#e6edf3' font-size='11'>487 is greater than 312</text>

  <!-- Less than example -->
  <rect x="215" y="45" width="170" height="65" fill='#22c55e30' stroke='#22c55e' stroke-width="2" rx="4"/>
  <text x="300" y="70" text-anchor='middle' fill='#e6edf3' font-size='20' font-weight='bold'>156 &lt; 329</text>
  <text x="300" y="95" text-anchor='middle' fill='#e6edf3' font-size='11'>156 is less than 329</text>

  <!-- Equals example -->
  <rect x="400" y="45" width="170" height="65" fill='#f59e0b30' stroke='#f59e0b' stroke-width="2" rx="4"/>
  <text x="485" y="70" text-anchor='middle' fill='#e6edf3' font-size='20' font-weight='bold'>500 = 500</text>
  <text x="485" y="95" text-anchor='middle' fill='#e6edf3' font-size='11'>500 is equal to 500</text>

  <!-- Mouth tip explanation -->
  <rect x="50" y="130" width="500" height="55" fill='#ec489915' stroke='#ec4899' stroke-width="1" stroke-dasharray="3,3" rx="3"/>
  <text x="60" y="150" text-anchor='start' fill='#ec4899' font-size='11' font-weight='bold'>Mouth Tip:</text>
  <text x="60" y="165" text-anchor='start' fill='#e6edf3' font-size='11'>The open side of the symbol ALWAYS points to the smaller number.</text>
  <text x="60" y="177" text-anchor='start' fill='#e6edf3' font-size='11'>487 &gt; 312  (mouth points at 312, the smaller number)</text>
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

<svg viewBox="0 0 600 280" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="300" y="20" text-anchor='middle' fill='#e6edf3' font-size='15' font-weight='bold'>Step-by-Step Comparison</text>

  <!-- Example 1 -->
  <rect x="30" y="40" width="540" height="60" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="1" rx="3"/>
  <text x="40" y="60" text-anchor='start' fill='#e6edf3' font-size='12' font-weight='bold'>Compare 643 and 628:</text>
  <text x="40" y="80" text-anchor='start' fill='#e6edf3' font-size='11'>Hundreds: 6 = 6 (same) → Check tens next</text>
  <text x="40" y="95" text-anchor='start' fill='#e6edf3' font-size='11'>Tens: 4 &gt; 2 → So <strong class="accent-heading">643 &gt; 628</strong></text>

  <!-- Example 2 -->
  <rect x="30" y="115" width="540" height="60" fill='#22c55e20' stroke='#22c55e' stroke-width="1" rx="3"/>
  <text x="40" y="135" text-anchor='start' fill='#e6edf3' font-size='12' font-weight='bold'>Compare 517 and 592:</text>
  <text x="40" y="155" text-anchor='start' fill='#e6edf3' font-size='11'>Hundreds: 5 = 5 (same) → Check tens next</text>
  <text x="40" y="170" text-anchor='start' fill='#e6edf3' font-size='11'>Tens: 1 &lt; 9 → So <strong style="color:#22c55e;">517 &lt; 592</strong></text>

  <!-- Example 3 -->
  <rect x="30" y="190" width="540" height="60" fill='#f59e0b20' stroke='#f59e0b' stroke-width="1" rx="3"/>
  <text x="40" y="210" text-anchor='start' fill='#e6edf3' font-size='12' font-weight='bold'>Compare 834 and 831:</text>
  <text x="40" y="230" text-anchor='start' fill='#e6edf3' font-size='11'>Hundreds: 8 = 8, Tens: 3 = 3 (same) → Check ones</text>
  <text x="40" y="245" text-anchor='start' fill='#e6edf3' font-size='11'>Ones: 4 &gt; 1 → So <strong style="color:#f59e0b;">834 &gt; 831</strong></text>
</svg>"""
    },
    {
        "title": "Ordering Numbers on a Number Line",
        "body": """<div class="concept-box">
<p>A number line shows numbers in order from smallest (left) to biggest (right). It helps us see which numbers are greater or smaller.</p>
</div>

<svg viewBox="0 0 600 200" style="width:100%;max-width:600px;height:auto;display:block;margin:16px auto;">
  <text x="300" y="20" text-anchor='middle' fill='#e6edf3' font-size='15' font-weight='bold'>Number Line from 500 to 600</text>

  <!-- Main number line -->
  <line x1="40" y1="80" x2="560" y2="80" stroke='#4f8ef7' stroke-width="2"/>

  <!-- Tick marks and labels -->
  <line x1="40" y1="75" x2="40" y2="85" stroke='#4f8ef7' stroke-width="2"/>
  <text x="40" y="105" text-anchor='middle' fill='#e6edf3' font-size='11'>500</text>

  <line x1="150" y1="75" x2="150" y2="85" stroke='#808080' stroke-width="1"/>
  <text x="150" y="105" text-anchor='middle' fill='#999' font-size='10'>550</text>

  <line x1="300" y1="75" x2="300" y2="85" stroke='#4f8ef7' stroke-width="2"/>
  <text x="300" y="105" text-anchor='middle' fill='#e6edf3' font-size='11'>600</text>

  <line x1="450" y1="75" x2="450" y2="85" stroke='#808080' stroke-width="1"/>
  <text x="450" y="105" text-anchor='middle' fill='#999' font-size='10'>650</text>

  <line x1="560" y1="75" x2="560" y2="85" stroke='#4f8ef7' stroke-width="2"/>
  <text x="560" y="105" text-anchor='middle' fill='#e6edf3' font-size='11'>700</text>

  <!-- Place some numbers -->
  <circle cx="100" cy="60" r="8" fill='#ec4899' stroke='#ec4899' stroke-width="2"/>
  <text x="100" y="64" text-anchor='middle' fill='#fff' font-size='10' font-weight='bold'>530</text>

  <circle cx="250" cy="60" r="8" fill='#22c55e' stroke='#22c55e' stroke-width="2"/>
  <text x="250" y="64" text-anchor='middle' fill='#fff' font-size='10' font-weight='bold'>590</text>

  <circle cx="380" cy="60" r="8" fill='#f59e0b' stroke='#f59e0b' stroke-width="2"/>
  <text x="380" y="64" text-anchor='middle' fill='#fff' font-size='10' font-weight='bold'>640</text>

  <!-- Order at bottom -->
  <text x="30" y="155" text-anchor='start' fill='#e6edf3' font-size='12' font-weight='bold'>In order:</text>
  <text x="30" y="175" text-anchor='start' fill='#e6edf3' font-size='12'>500 &lt; 530 &lt; 590 &lt; 600 &lt; 640 &lt; 700</text>
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
  <text x="300" y="20" text-anchor='middle' fill='#e6edf3' font-size='15' font-weight='bold'>Ordering Numbers Practice</text>

  <!-- Example 1 -->
  <rect x="30" y="40" width="540" height="90" fill='#4f8ef720' stroke='#4f8ef7' stroke-width="1" rx="3"/>
  <text x="40" y="60" text-anchor='start' fill='#e6edf3' font-size='12' font-weight='bold'>Order from smallest to largest: 325, 523, 253</text>
  <text x="40" y="80" text-anchor='start' fill='#e6edf3' font-size='11'>Step 1: Compare hundreds: 2__ is smallest, 5__ is largest</text>
  <text x="40" y="95" text-anchor='start' fill='#e6edf3' font-size='11'>Step 2: Between 325 and 523, which is smaller? 325 &lt; 523</text>
  <text x="40" y="110" text-anchor='start' fill='#e6edf3' font-size='12' font-weight='bold'>Answer: 253 &lt; 325 &lt; 523</text>

  <!-- Example 2 -->
  <rect x="30" y="145" width="540" height="90" fill='#22c55e20' stroke='#22c55e' stroke-width="1" rx="3"/>
  <text x="40" y="165" text-anchor='start' fill='#e6edf3' font-size='12' font-weight='bold'>Order from largest to smallest: 789, 879, 798</text>
  <text x="40" y="185" text-anchor='start' fill='#e6edf3' font-size='11'>Step 1: Compare hundreds: All start with 7 or 8</text>
  <text x="40" y="200" text-anchor='start' fill='#e6edf3' font-size='11'>Step 2: 8__ is the largest. Between 879 and 798 from the remaining</text>
  <text x="40" y="215" text-anchor='start' fill='#e6edf3' font-size='12' font-weight='bold'>Answer: 879 &gt; 798 &gt; 789</text>
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
