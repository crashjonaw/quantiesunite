TITLE = "Arrays and Pictures"
SECTIONS = [
    {
        "title": "What is an Array?",
        "body": """<p>An <strong>array</strong> is a way of arranging objects in neat rows and columns — like a grid.</p>
<p>Arrays are a super useful way to think about multiplication because you can count the objects in two directions!</p>
<ul>
  <li>Count the <strong>rows</strong> (going down)</li>
  <li>Count the <strong>columns</strong> (going across)</li>
</ul>
<p>When you multiply the number of rows by the number of columns, you get the total number of objects.</p>"""
    },
    {
        "title": "Understanding Arrays: Rows × Columns",
        "body": """<p>Look at this array of dots:</p>
<svg viewBox="0 0 470 270" style="width:100%; max-width:550px; height:auto; display:block; margin:16px auto;">
  <rect x="0" y="0" width="470" height="270" rx="4" fill="rgba(0,0,0,0.2)"/>
  <text x="235" y="30" text-anchor='middle' fill='currentColor' font-size='16' font-weight='bold'>3 Rows × 4 Columns = 12 Dots</text>
  <!-- Row 1 -->
  <circle cx="110" cy="75" r="10" fill='#4f8ef7'/>
  <circle cx="170" cy="75" r="10" fill='#4f8ef7'/>
  <circle cx="230" cy="75" r="10" fill='#4f8ef7'/>
  <circle cx="290" cy="75" r="10" fill='#4f8ef7'/>
  <!-- Row 2 -->
  <circle cx="110" cy="135" r="10" fill='#4f8ef7'/>
  <circle cx="170" cy="135" r="10" fill='#4f8ef7'/>
  <circle cx="230" cy="135" r="10" fill='#4f8ef7'/>
  <circle cx="290" cy="135" r="10" fill='#4f8ef7'/>
  <!-- Row 3 -->
  <circle cx="110" cy="195" r="10" fill='#4f8ef7'/>
  <circle cx="170" cy="195" r="10" fill='#4f8ef7'/>
  <circle cx="230" cy="195" r="10" fill='#4f8ef7'/>
  <circle cx="290" cy="195" r="10" fill='#4f8ef7'/>
  <!-- Row labels -->
  <text x="55" y="80" fill='#ef4444' font-size='13' font-weight='bold' text-anchor='middle'>Row 1</text>
  <text x="55" y="140" fill='#ef4444' font-size='13' font-weight='bold' text-anchor='middle'>Row 2</text>
  <text x="55" y="200" fill='#ef4444' font-size='13' font-weight='bold' text-anchor='middle'>Row 3</text>
  <!-- Column labels -->
  <text x="110" y="240" text-anchor='middle' fill='#22c55e' font-size='12' font-weight='bold'>Col 1</text>
  <text x="170" y="240" text-anchor='middle' fill='#22c55e' font-size='12' font-weight='bold'>Col 2</text>
  <text x="230" y="240" text-anchor='middle' fill='#22c55e' font-size='12' font-weight='bold'>Col 3</text>
  <text x="290" y="240" text-anchor='middle' fill='#22c55e' font-size='12' font-weight='bold'>Col 4</text>
  <!-- Result -->
  <text x="390" y="125" fill='#f59e0b' font-size='20' font-weight='bold'>3 × 4</text>
  <text x="390" y="155" fill='currentColor' font-size='14'>= 12 dots</text>
</svg>
<p style="text-align: center; margin-top: 20px;"><strong>3 rows of 4 = \(4 + 4 + 4 = 12\)</strong></p>
<p style="text-align: center;"><strong>OR 4 columns of 3 = \(3 + 3 + 3 + 3 = 12\)</strong></p>"""
    },
    {
        "title": "The Commutative Property: Rotation Magic",
        "body": """<p>Here's something amazing: <strong>\(3 \\times 4 = 4 \\times 3\)</strong></p>
<p>When you rotate an array, the multiplication sentence changes, but the total stays the same!</p>
<svg viewBox="0 0 520 285" style="width:100%; max-width:550px; height:auto; display:block; margin:16px auto;">
  <rect x="0" y="0" width="520" height="285" rx="4" fill="rgba(0,0,0,0.2)"/>
  <text x="260" y="28" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Same Array, Different Views</text>
  <!-- Left array: 3x4 -->
  <text x="110" y="58" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>3 rows × 4 cols</text>
  <circle cx="45" cy="90" r="8" fill='#4f8ef7'/>
  <circle cx="80" cy="90" r="8" fill='#4f8ef7'/>
  <circle cx="115" cy="90" r="8" fill='#4f8ef7'/>
  <circle cx="150" cy="90" r="8" fill='#4f8ef7'/>
  <circle cx="45" cy="125" r="8" fill='#4f8ef7'/>
  <circle cx="80" cy="125" r="8" fill='#4f8ef7'/>
  <circle cx="115" cy="125" r="8" fill='#4f8ef7'/>
  <circle cx="150" cy="125" r="8" fill='#4f8ef7'/>
  <circle cx="45" cy="160" r="8" fill='#4f8ef7'/>
  <circle cx="80" cy="160" r="8" fill='#4f8ef7'/>
  <circle cx="115" cy="160" r="8" fill='#4f8ef7'/>
  <circle cx="150" cy="160" r="8" fill='#4f8ef7'/>
  <text x="110" y="200" text-anchor='middle' fill='#f59e0b' font-size='16' font-weight='bold'>3 × 4 = 12</text>
  <!-- Rotation arrow -->
  <text x="260" y="125" fill='currentColor' font-size='24' text-anchor='middle'>&#x27F2;</text>
  <text x="260" y="150" fill='currentColor' font-size='12' text-anchor='middle'>rotate</text>
  <!-- Right array: 4x3 -->
  <text x="410" y="58" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>4 rows × 3 cols</text>
  <circle cx="375" cy="90" r="8" fill='#22c55e'/>
  <circle cx="410" cy="90" r="8" fill='#22c55e'/>
  <circle cx="445" cy="90" r="8" fill='#22c55e'/>
  <circle cx="375" cy="125" r="8" fill='#22c55e'/>
  <circle cx="410" cy="125" r="8" fill='#22c55e'/>
  <circle cx="445" cy="125" r="8" fill='#22c55e'/>
  <circle cx="375" cy="160" r="8" fill='#22c55e'/>
  <circle cx="410" cy="160" r="8" fill='#22c55e'/>
  <circle cx="445" cy="160" r="8" fill='#22c55e'/>
  <circle cx="375" cy="195" r="8" fill='#22c55e'/>
  <circle cx="410" cy="195" r="8" fill='#22c55e'/>
  <circle cx="445" cy="195" r="8" fill='#22c55e'/>
  <text x="410" y="235" text-anchor='middle' fill='#f59e0b' font-size='16' font-weight='bold'>4 × 3 = 12</text>
</svg>
<p style="text-align: center; margin-top: 20px; font-size: 15px;">The dots are arranged differently, but there are still <strong>12 dots total!</strong></p>
<div class="success-box" style="background: rgba(34, 197, 94, 0.1); border-left: 4px solid #22c55e; padding: 16px; border-radius: 6px; margin: 20px 0;">
  <p style="margin: 0; font-weight: bold;">Commutative Property:</p>
  <p style="margin: 8px 0 0 0;">\\(3 \\times 4 = 4 \\times 3\\)</p>
  <p style="margin: 8px 0 0 0;">You can flip the order of multiplication and still get the same answer!</p>
</div>"""
    },
    {
        "title": "Real-World Arrays",
        "body": """<p>You see arrays in real life all the time!</p>
<div class="concept-box" style="padding: 16px; border-radius: 6px; margin: 16px 0">
  <p style="margin: 8px 0;"><strong>📦 Chocolate bars:</strong> A box of chocolate is arranged \(3 \\times 4 = 12\) pieces</p>
  <p style="margin: 8px 0;"><strong>🪟 Window panes:</strong> A window with \(2 \\times 3 = 6\) panes</p>
  <p style="margin: 8px 0;"><strong>🎒 Desk arrangement:</strong> A classroom with 5 rows of 4 desks each = \(5 \\times 4 = 20\) desks</p>
  <p style="margin: 8px 0;"><strong>🍕 Pizza slices:</strong> Some pizzas are cut \(4 \\times 4 = 16\) slices</p>
</div>"""
    },
    {
        "title": "Check Your Understanding",
        "body": """<div class="mcq-group" style="background: rgba(0,0,0,0.2); padding: 20px; border-radius: 8px; margin: 16px 0;">
  <p style="font-size: 16px; font-weight: bold;">If an array has 5 rows and 6 columns, how many items are there?</p>
  <div class="mcq-options" style="display: flex; flex-direction: column; gap: 12px; margin-top: 12px;">
    <button class="mcq-option" data-correct="true" data-explanation="Yes! 5 rows × 6 columns = 30 items. You can also think of it as 6 rows × 5 columns = 30 items." class="concept-box" style="cursor: pointer;">30</button>
    <button class="mcq-option" data-correct="false" class="concept-box" style="cursor: pointer;">11</button>
    <button class="mcq-option" data-correct="false" class="concept-box" style="cursor: pointer;">25</button>
  </div>
  <div class="mcq-feedback"></div>
</div>"""
    }
]
