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

<svg viewBox="0 0 300 250" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:300px; margin:20px 0;">
  <defs>
    </defs>

  <!-- Triangle -->
  <line x1="30" y1="220" x2="230" y2="220" class="triangle-line"/>
  <line x1="230" y1="220" x2="150" y2="30" class="triangle-line"/>
  <line x1="150" y1="30" x2="30" y2="220" class="triangle-line"/>

  <!-- Vertices -->
  <circle cx="30" cy="220" r="3" fill='#4f8ef7'/>
  <circle cx="230" cy="220" r="3" fill='#4f8ef7'/>
  <circle cx="150" cy="30" r="3" fill='#4f8ef7'/>

  <!-- Vertex labels -->
  <text x="20" y="240" class="label">A</text>
  <text x="240" y="240" class="label">B</text>
  <text x="150" y="15" class="label">C</text>

  <!-- Side labels -->
  <text x="130" y="210" class="label" fill='#8b949e'>a</text>
  <text x="255" y="125" class="label" fill='#8b949e'>b</text>
  <text x="70" y="120" class="label" fill='#8b949e'>c</text>

  <!-- Angle labels -->
  <text x="45" y="205" class="angle-label">∠A</text>
  <text x="210" y="205" class="angle-label">∠B</text>
  <text x="150" y="50" class="angle-label">∠C</text>
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

<svg viewBox="0 0 400 350" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:400px; margin:20px 0;">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="5" refY="5" orient="auto">
      <polygon points="0 0, 10 5, 0 10" fill='#8b949e'/>
    </marker>
  </defs>

  <!-- Main question -->
  <rect x="125" y="10" width="150" height="50" class="decision-box"/>
  <text x="200" y="35" class="decision-text" text-anchor='middle'>What do you know?</text>

  <!-- First level branches -->
  <line x1="160" y1="60" x2="100" y2="110" class="arrow"/>
  <line x1="240" y1="60" x2="300" y2="110" class="arrow"/>
  <text x="120" y="85" class="label">Two angles</text>
  <text x="260" y="85" class="label">Two sides</text>

  <!-- Left branch: Two angles -->
  <rect x="50" y="110" width="100" height="50" class="decision-box"/>
  <text x="100" y="135" class="decision-text" text-anchor='middle'>Plus one side?</text>

  <!-- Right branch: Two sides -->
  <rect x="250" y="110" width="100" height="50" class="decision-box"/>
  <text x="300" y="135" class="decision-text" text-anchor='middle'>Plus angle</text>
  <text x="300" y="150" class="decision-text" text-anchor='middle'>between them?</text>

  <!-- Sub-branches -->
  <line x1="100" y1="160" x2="80" y2="210" class="arrow"/>
  <text x="85" y="190" class="label">Yes: AAS/ASA</text>

  <line x1="300" y1="160" x2="260" y2="210" class="arrow"/>
  <text x="245" y="190" class="label">Yes: SAS</text>

  <line x1="300" y1="160" x2="340" y2="210" class="arrow"/>
  <text x="330" y="190" class="label">No: SSA</text>

  <!-- Answers -->
  <rect x="30" y="210" width="100" height="40" class="answer-box"/>
  <text x="80" y="235" class="decision-text" text-anchor='middle' font-weight='bold'>Law of Sines</text>

  <rect x="210" y="210" width="100" height="40" class="answer-box"/>
  <text x="260" y="235" class="decision-text" text-anchor='middle' font-weight='bold'>Law of Cosines</text>

  <rect x="310" y="210" width="80" height="40" class="answer-box"/>
  <text x="350" y="235" class="decision-text" text-anchor='middle' font-weight='bold'>Law of Sines</text>
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
