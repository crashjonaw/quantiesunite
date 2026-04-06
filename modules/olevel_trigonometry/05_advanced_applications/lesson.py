TITLE = "Advanced Applications: Rules for Any Triangle"

SECTIONS = [
    {
        "title": "Beyond Right Triangles: The Need for New Rules",
        "body": """
<h3>The Limitation of Right Triangle Trigonometry</h3>
<p>Until now, all our methods require a right angle. But what if we have a triangle with no right angle? The SOHCAHTOA ratios don't apply directly.</p>

<p>We need new tools that work for <strong>any</strong> triangle, whether it has a right angle or not.</p>

<h3>Two Essential Rules</h3>

<div class="concept-box">
<p><strong>Law of Sines:</strong> Relates sides to their opposite angles in any triangle</p>
<p><strong>Law of Cosines:</strong> Relates all three sides and one angle in any triangle</p>
</div>

<p>These rules are fundamental in surveying, navigation, engineering, and astronomy.</p>

<h3>Notation Convention</h3>
<p>In any triangle:</p>
<ul>
  <li>Sides are labeled with lowercase letters: \\(a\\), \\(b\\), \\(c\\)</li>
  <li>Angles opposite these sides use the same letter (uppercase): \\(A\\), \\(B\\), \\(C\\)</li>
  <li>So side \\(a\\) is opposite angle \\(A\\), side \\(b\\) is opposite angle \\(B\\), etc.</li>
</ul>

<svg viewBox="0 0 340 280" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:360px; margin:20px auto; display:block;">

  <!-- Triangle sides -->
  <line x1="40" y1="240" x2="250" y2="240" stroke='#4f8ef7' stroke-width="2"/>
  <line x1="250" y1="240" x2="170" y2="45" stroke='#4f8ef7' stroke-width="2"/>
  <line x1="170" y1="45" x2="40" y2="240" stroke='#4f8ef7' stroke-width="2"/>

  <!-- Angle arcs -->
  <path d="M 70 240 A 30 30 0 0 0 60 218" fill='none' stroke='#e8b04f' stroke-width="1.5"/>
  <path d="M 225 240 A 25 25 0 0 1 237 224" fill='none' stroke='#e8b04f' stroke-width="1.5"/>
  <path d="M 157 67 A 25 25 0 0 0 183 67" fill='none' stroke='#e8b04f' stroke-width="1.5"/>

  <!-- Vertices -->
  <circle cx="40" cy="240" r="4" fill='#4f8ef7'/>
  <circle cx="250" cy="240" r="4" fill='#4f8ef7'/>
  <circle cx="170" cy="45" r="4" fill='#4f8ef7'/>

  <!-- Vertex labels -->
  <text x="22" y="260" fill='currentColor' font-size='15' font-weight='bold'>A</text>
  <text x="258" y="260" fill='currentColor' font-size='15' font-weight='bold'>B</text>
  <text x="165" y="30" fill='currentColor' font-size='15' font-weight='bold'>C</text>

  <!-- Side labels (opposite each vertex) -->
  <text x="145" y="258" fill='currentColor' font-size='14' text-anchor='middle' font-style='italic'>c</text>
  <text x="85" y="135" fill='currentColor' font-size='14' text-anchor='middle' font-style='italic'>b</text>
  <text x="225" y="135" fill='currentColor' font-size='14' text-anchor='middle' font-style='italic'>a</text>
</svg>
"""
    },
    {
        "title": "The Law of Sines: Relating Sides and Opposite Angles",
        "body": """
<h3>The Law of Sines Statement</h3>

<div class="concept-box">
<p>In any triangle:</p>
<p>$$\\frac{a}{\\sin(A)} = \\frac{b}{\\sin(B)} = \\frac{c}{\\sin(C)}$$</p>
</div>

<p>This says: "Each side divided by the sine of its opposite angle is the same ratio in any triangle."</p>

<h3>Where Does It Come From? (Geometric Derivation)</h3>

<p>Drop a perpendicular from vertex \\(C\\) to side \\(c\\). Call the height \\(h\\).</p>

<p>Then:</p>
<p>\\(\\sin(A) = \\frac{h}{b}\\), so \\(h = b\\sin(A)\\)</p>
<p>\\(\\sin(B) = \\frac{h}{a}\\), so \\(h = a\\sin(B)\\)</p>

<p>Since both equal \\(h\\):</p>
<p>\\(b\\sin(A) = a\\sin(B)\\)</p>

<p>Rearranging:</p>
<p>\\(\\frac{a}{\\sin(A)} = \\frac{b}{\\sin(B)}\\)</p>

<p>The same argument with different heights gives the full Law of Sines.</p>

<h3>When to Use the Law of Sines</h3>
<p>Use when you know:</p>
<ul>
  <li><strong>AAS:</strong> Two angles and one side (the angle-angle-side case)</li>
  <li><strong>ASA:</strong> One angle, a side, and another angle</li>
  <li><strong>SSA:</strong> Two sides and an angle opposite one of them (careful: can have 0, 1, or 2 solutions)</li>
</ul>

<h3>Worked Example: Finding a Side</h3>

<div class="worked-example">
<p><strong>In triangle \\(ABC\\): \\(A = 40°\\), \\(B = 60°\\), and side \\(a = 8\\) cm. Find side \\(b\\).</strong></p>

<p><strong>Step 1: Identify what you have</strong></p>
<p>We have two angles and the side opposite one of them (AAS case).</p>

<p><strong>Step 2: Apply the Law of Sines</strong></p>
<p>\\(\\frac{a}{\\sin(A)} = \\frac{b}{\\sin(B)}\\)</p>

<p><strong>Step 3: Substitute known values</strong></p>
<p>\\(\\frac{8}{\\sin(40°)} = \\frac{b}{\\sin(60°)}\\)</p>

<p><strong>Step 4: Solve for \\(b\\)</strong></p>
<p>\\(b = \\frac{8 \\times \\sin(60°)}{\\sin(40°)}\\)</p>
<p>\\(b = \\frac{8 \\times 0.866}{0.643} \\approx 10.77\\) cm</p>
</div>

<h3>Worked Example: Finding an Angle</h3>

<div class="worked-example">
<p><strong>In triangle \\(ABC\\): \\(a = 7\\), \\(b = 10\\), and \\(A = 30°\\). Find angle \\(B\\).</strong></p>

<p><strong>Step 1: Apply the Law of Sines</strong></p>
<p>\\(\\frac{a}{\\sin(A)} = \\frac{b}{\\sin(B)}\\)</p>

<p><strong>Step 2: Substitute</strong></p>
<p>\\(\\frac{7}{\\sin(30°)} = \\frac{10}{\\sin(B)}\\)</p>

<p><strong>Step 3: Solve for \\(\\sin(B)\\)</strong></p>
<p>\\(\\sin(B) = \\frac{10 \\times \\sin(30°)}{7} = \\frac{10 \\times 0.5}{7} = \\frac{5}{7} \\approx 0.714\\)</p>

<p><strong>Step 4: Find \\(B\\)</strong></p>
<p>\\(B = \\sin^{-1}(0.714) \\approx 45.6°\\)</p>

<p><strong>Important:</strong> Since sine is positive in both Quadrants I and II, there might be another solution: \\(180° - 45.6° = 134.4°\\)</p>
<p>However, we need to check if this makes a valid triangle. (Sum of angles must be less than 180°.)</p>
</div>
"""
    },
    {
        "title": "The Law of Cosines: The Generalization of Pythagoras",
        "body": """
<h3>The Law of Cosines Statement</h3>

<div class="concept-box">
<p>In any triangle:</p>
<p>\\(a^2 = b^2 + c^2 - 2bc\\cos(A)\\)</p>
<p>\\(b^2 = a^2 + c^2 - 2ac\\cos(B)\\)</p>
<p>\\(c^2 = a^2 + b^2 - 2ab\\cos(C)\\)</p>
</div>

<p><strong>Special case:</strong> When angle \\(A = 90°\\), \\(\\cos(A) = 0\\), so the law reduces to \\(a^2 = b^2 + c^2\\)—the Pythagorean theorem!</p>

<h3>Why It Works: Derivation</h3>

<p>In a general triangle, drop a perpendicular from \\(C\\) to side \\(c\\), creating a height \\(h\\) that lands at distance \\(x\\) from vertex \\(A\\).</p>

<p>From the right triangle on the left:</p>
<p>\\(x = b\\cos(A)\\) and \\(h = b\\sin(A)\\)</p>

<p>From the right triangle on the right (using the Pythagorean theorem):</p>
<p>\\(a^2 = h^2 + (c - x)^2\\)</p>
<p>\\(a^2 = b^2\\sin^2(A) + (c - b\\cos(A))^2\\)</p>

<p>Expanding and using \\(\\sin^2(A) + \\cos^2(A) = 1\\):</p>
<p>\\(a^2 = b^2 + c^2 - 2bc\\cos(A)\\)</p>

<h3>When to Use the Law of Cosines</h3>
<p>Use when you know:</p>
<ul>
  <li><strong>SAS:</strong> Two sides and the angle between them (side-angle-side)</li>
  <li><strong>SSS:</strong> All three sides (side-side-side)</li>
</ul>

<h3>Worked Example: SAS Case (Finding a Side)</h3>

<div class="worked-example">
<p><strong>In triangle \\(ABC\\): \\(a = 7\\) cm, \\(b = 10\\) cm, and \\(C = 50°\\). Find side \\(c\\).</strong></p>

<p><strong>Step 1: Identify the situation</strong></p>
<p>We have two sides (\\(a\\) and \\(b\\)) and the angle between them (\\(C\\))—this is SAS.</p>

<p><strong>Step 2: Choose the Law of Cosines form that includes the known angle</strong></p>
<p>\\(c^2 = a^2 + b^2 - 2ab\\cos(C)\\)</p>

<p><strong>Step 3: Substitute</strong></p>
<p>\\(c^2 = 7^2 + 10^2 - 2(7)(10)\\cos(50°)\\)</p>
<p>\\(c^2 = 49 + 100 - 140(0.643)\\)</p>
<p>\\(c^2 = 149 - 90.02 = 58.98\\)</p>

<p><strong>Step 4: Solve for \\(c\\)</strong></p>
<p>\\(c = \\sqrt{58.98} \\approx 7.68\\) cm</p>
</div>

<h3>Worked Example: SSS Case (Finding an Angle)</h3>

<div class="worked-example">
<p><strong>In triangle \\(ABC\\): \\(a = 5\\) cm, \\(b = 6\\) cm, \\(c = 7\\) cm. Find angle \\(C\\).</strong></p>

<p><strong>Step 1: Choose the Law of Cosines form that solves for the angle</strong></p>
<p>\\(c^2 = a^2 + b^2 - 2ab\\cos(C)\\)</p>

<p>Rearranging for \\(\\cos(C)\\):</p>
<p>\\(\\cos(C) = \\frac{a^2 + b^2 - c^2}{2ab}\\)</p>

<p><strong>Step 2: Substitute</strong></p>
<p>\\(\\cos(C) = \\frac{5^2 + 6^2 - 7^2}{2(5)(6)} = \\frac{25 + 36 - 49}{60} = \\frac{12}{60} = 0.2\\)</p>

<p><strong>Step 3: Find the angle</strong></p>
<p>\\(C = \\cos^{-1}(0.2) \\approx 78.46°\\)</p>
</div>
"""
    },
    {
        "title": "Choosing the Right Tool and Real-World Applications",
        "body": """
<h3>Decision Tree: Which Rule to Use</h3>

<svg viewBox="0 0 420 300" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:420px; margin:20px auto; display:block;">

  <!-- Main question box -->
  <rect x="135" y="15" width="150" height="40" rx='4' fill='#4f8ef7' fill-opacity='0.15' stroke='#4f8ef7' stroke-width="1.5"/>
  <text x="210" y="40" fill='currentColor' font-size='13' font-weight='bold' text-anchor='middle'>What do you know?</text>

  <!-- Branches down from main -->
  <line x1="170" y1="55" x2="105" y2="90" stroke='#30363d' stroke-width="1.5"/>
  <line x1="250" y1="55" x2="315" y2="90" stroke='#30363d' stroke-width="1.5"/>

  <!-- Branch labels -->
  <text x="120" y="75" fill='currentColor' font-size='11'>Two angles</text>
  <text x="260" y="75" fill='currentColor' font-size='11'>Two sides</text>

  <!-- Left decision box -->
  <rect x="40" y="95" width="130" height="40" rx='4' fill='#e8b04f' fill-opacity='0.12' stroke='#e8b04f' stroke-width="1.5"/>
  <text x="105" y="120" fill='currentColor' font-size='12' text-anchor='middle'>Plus one side?</text>

  <!-- Right decision box -->
  <rect x="250" y="95" width="130" height="40" rx='4' fill='#e8b04f' fill-opacity='0.12' stroke='#e8b04f' stroke-width="1.5"/>
  <text x="315" y="113" fill='currentColor' font-size='12' text-anchor='middle'>Angle between?</text>

  <!-- Left sub-branch -->
  <line x1="105" y1="135" x2="85" y2="175" stroke='#30363d' stroke-width="1.5"/>
  <text x="60" y="165" fill='currentColor' font-size='11'>AAS / ASA</text>

  <!-- Right sub-branches -->
  <line x1="290" y1="135" x2="260" y2="175" stroke='#30363d' stroke-width="1.5"/>
  <text x="230" y="165" fill='currentColor' font-size='11'>Yes: SAS</text>

  <line x1="340" y1="135" x2="360" y2="175" stroke='#30363d' stroke-width="1.5"/>
  <text x="355" y="165" fill='currentColor' font-size='11'>No: SSA</text>

  <!-- Answer boxes -->
  <rect x="30" y="180" width="120" height="36" rx='4' fill='#4f8ef7' fill-opacity='0.2' stroke='#4f8ef7' stroke-width="1.5"/>
  <text x="90" y="203" fill='currentColor' font-size='12' font-weight='bold' text-anchor='middle'>Law of Sines</text>

  <rect x="200" y="180" width="120" height="36" rx='4' fill='#e8b04f' fill-opacity='0.2' stroke='#e8b04f' stroke-width="1.5"/>
  <text x="260" y="203" fill='currentColor' font-size='12' font-weight='bold' text-anchor='middle'>Law of Cosines</text>

  <rect x="325" y="180" width="80" height="36" rx='4' fill='#4f8ef7' fill-opacity='0.2' stroke='#4f8ef7' stroke-width="1.5"/>
  <text x="365" y="203" fill='currentColor' font-size='12' font-weight='bold' text-anchor='middle'>Law of Sines</text>

  <!-- SSS note -->
  <rect x="200" y="235" width="120" height="36" rx='4' fill='#e8b04f' fill-opacity='0.2' stroke='#e8b04f' stroke-width="1.5"/>
  <text x="260" y="258" fill='currentColor' font-size='12' font-weight='bold' text-anchor='middle'>Law of Cosines</text>
  <line x1="260" y1="216" x2="260" y2="235" stroke='#30363d' stroke-width="1.5"/>
  <text x="280" y="230" fill='currentColor' font-size='10'>SSS</text>
</svg>

<h3>Quick Reference</h3>

<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr >
  <th style="padding: 10px; text-align: left">Case</th>
  <th style="padding: 10px;">Rule</th>
  <th style="padding: 10px;">Use When</th>
</tr>
<tr >
  <td style="padding: 10px;">AAS/ASA</td>
  <td style="padding: 10px;">Law of Sines</td>
  <td style="padding: 10px;">Two angles + side</td>
</tr>
<tr >
  <td style="padding: 10px;">SSA</td>
  <td style="padding: 10px;">Law of Sines</td>
  <td style="padding: 10px;">Two sides + angle (not between)</td>
</tr>
<tr >
  <td style="padding: 10px;">SAS</td>
  <td style="padding: 10px;">Law of Cosines</td>
  <td style="padding: 10px;">Two sides + angle between</td>
</tr>
<tr >
  <td style="padding: 10px;">SSS</td>
  <td style="padding: 10px;">Law of Cosines</td>
  <td style="padding: 10px;">All three sides</td>
</tr>
</table>

<h3>Real-World Example: Surveying a Triangle Property</h3>

<div class="worked-example">
<p><strong>Problem:</strong> A surveyor wants to find the distance across a river. She measures from two points \\(A\\) and \\(B\\) that are 50 meters apart on one side. From \\(A\\), the angle to a point \\(C\\) on the far bank is 40°. From \\(B\\), the angle to \\(C\\) is 65°. Find the distance from \\(A\\) to \\(C\\).</p>

<p><strong>Step 1: Identify the situation</strong></p>
<p>We know:</p>
<ul>
  <li>Side \\(AB = c = 50\\) meters</li>
  <li>Angle at \\(A\\) is 40°</li>
  <li>Angle at \\(B\\) is 65°</li>
</ul>
<p>This is an AAS case (two angles + one side).</p>

<p><strong>Step 2: Find the third angle</strong></p>
<p>\\(C = 180° - 40° - 65° = 75°\\)</p>

<p><strong>Step 3: Use the Law of Sines</strong></p>
<p>\\(\\frac{c}{\\sin(C)} = \\frac{AC}{\\sin(B)}\\)</p>

<p><strong>Step 4: Solve for \\(AC\\)</strong></p>
<p>\\(AC = \\frac{c \\times \\sin(B)}{\\sin(C)} = \\frac{50 \\times \\sin(65°)}{\\sin(75°)}\\)</p>
<p>\\(AC = \\frac{50 \\times 0.906}{0.966} \\approx 46.9\\) meters</p>

<p>The river is approximately 46.9 meters wide at this location.</p>
</div>

<h3>The Area of a Triangle Using Trigonometry</h3>

<div class="concept-box">
<p>If you know two sides \\(a\\) and \\(b\\) and the angle \\(C\\) between them:</p>
<p>\\(\\text{Area} = \\frac{1}{2}ab\\sin(C)\\)</p>
</div>

<p><strong>Why:</strong> The height from \\(C\\) to side \\(c\\) is \\(h = a\\sin(B) = b\\sin(A)\\). Using the standard area formula \\(\\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{height}\\), we get the formula above.</p>

<h3>Worked Example: Finding the Area</h3>

<div class="worked-example">
<p><strong>A triangular plot of land has two sides of 80 meters and 100 meters with an angle of 60° between them. What is its area?</strong></p>

<p>\\(\\text{Area} = \\frac{1}{2} \\times 80 \\times 100 \\times \\sin(60°)\\)</p>
<p>\\(= \\frac{1}{2} \\times 8000 \\times 0.866\\)</p>
<p>\\(= 3464\\) square meters</p>
</div>
"""
    }
]
