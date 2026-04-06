TITLE = "Introduction to Trigonometric Ratios (SOH-CAH-TOA)"

SECTIONS = [
    {
        "title": "Why Trigonometry? Understanding Right Triangles",
        "body": """
<div class="concept-box">
<h3>The Big Question</h3>
<p>How can we find unknown sides and angles in right triangles without measuring them? Trigonometry gives us the mathematical tools to do exactly that.</p>
</div>

<h3>The Problem We're Solving</h3>
<p>Imagine you have a right triangle where you know one side and one angle. How do you find the other sides? Direct measurement isn't always possible. We need a relationship between angles and side lengths.</p>

<p>That's where trigonometric ratios come in. They're simply fractions (ratios) of the sides of a right triangle that depend on the angle.</p>

<h3>Setting Up Our Triangle</h3>
<p>Consider a right triangle with an angle \\(\\theta\\) (theta). Relative to this angle, the three sides have special names:</p>

<svg viewBox="0 0 380 280" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:380px; margin:20px auto; display:block;">
  <defs>
    <marker id="arr-tri" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill='#4f8ef7'/>
    </marker>
  </defs>

  <!-- Right triangle -->
  <line x1="50" y1="220" x2="270" y2="220" stroke='#4f8ef7' stroke-width="2"/>
  <line x1="270" y1="220" x2="270" y2="60" stroke='#4f8ef7' stroke-width="2"/>
  <line x1="50" y1="220" x2="270" y2="60" stroke='#4f8ef7' stroke-width="2"/>

  <!-- Right angle indicator -->
  <polyline points="258,220 258,208 270,208" fill='none' stroke='#4f8ef7' stroke-width="1.5"/>

  <!-- Angle theta arc -->
  <path d="M 85 220 A 35 35 0 0 0 74 195" fill='none' stroke='#e8b04f' stroke-width="2"/>
  <text x="92" y="205" fill='#e8b04f' font-size='15' font-weight='bold'>θ</text>

  <!-- Side labels -->
  <text x="160" y="250" fill='currentColor' font-size='14' text-anchor='middle'>Adjacent</text>
  <text x="290" y="145" fill='currentColor' font-size='14'>Opposite</text>
  <text x="130" y="125" fill='#4f8ef7' font-size='14' font-weight='bold' text-anchor='middle' transform="rotate(-36, 130, 125)">Hypotenuse</text>
</svg>

<ul>
  <li><strong>Hypotenuse:</strong> The longest side, always opposite the right angle</li>
  <li><strong>Opposite:</strong> The side across from angle \\(\\theta\\)</li>
  <li><strong>Adjacent:</strong> The side next to angle \\(\\theta\\) (but not the hypotenuse)</li>
</ul>
"""
    },
    {
        "title": "The Three Basic Trigonometric Ratios",
        "body": """
<h3>Understanding Ratios from First Principles</h3>
<p>A ratio compares two quantities by division. For example, if a triangle has opposite = 3 and hypotenuse = 5, the ratio of opposite to hypotenuse is 3/5.</p>

<p>The key insight: <strong>For a given angle, the ratio of any two sides is always the same, regardless of the triangle's size.</strong> This is why we can use these ratios to find unknowns.</p>

<h3>The Three Ratios: SOH-CAH-TOA</h3>

<div class="concept-box">
<p><strong>SOH:</strong> \\(\\sin(\\theta) = \\frac{\\text{Opposite}}{\\text{Hypotenuse}}\\)</p>
<p><strong>CAH:</strong> \\(\\cos(\\theta) = \\frac{\\text{Adjacent}}{\\text{Hypotenuse}}\\)</p>
<p><strong>TOA:</strong> \\(\\tan(\\theta) = \\frac{\\text{Opposite}}{\\text{Adjacent}}\\)</p>
</div>

<h3>Why These Ratios?</h3>
<p>These three ratios are chosen because they're the most useful combinations:</p>
<ul>
  <li><strong>Sine and Cosine</strong> both relate a side to the hypotenuse—useful when you know or need the hypotenuse</li>
  <li><strong>Tangent</strong> relates the two legs—useful when you don't know the hypotenuse</li>
</ul>

<h3>Worked Example: Using SOHCAHTOA</h3>

<div class="worked-example">
<p><strong>Problem:</strong> In a right triangle, the angle \\(\\theta = 35°\\). The adjacent side is 8 cm. Find the opposite side.</p>

<p><strong>Step 1:</strong> Identify what we know and need.
<ul>
  <li>Known: angle (35°), adjacent side (8 cm)</li>
  <li>Need: opposite side</li>
</ul>
</p>

<p><strong>Step 2:</strong> Choose the ratio that uses both adjacent and opposite.
<ul>
  <li>That's <strong>TOA</strong>: \\(\\tan(\\theta) = \\frac{\\text{Opposite}}{\\text{Adjacent}}\\)</li>
</ul>
</p>

<p><strong>Step 3:</strong> Set up the equation and solve.
$$\\tan(35°) = \\frac{\\text{Opposite}}{8}$$
$$\\text{Opposite} = 8 \\times \\tan(35°)$$
$$\\text{Opposite} = 8 \\times 0.7002 \\approx 5.60 \\text{ cm}$$
</p>
</div>
"""
    },
    {
        "title": "Finding Unknown Sides: Practice and Strategy",
        "body": """
<h3>The Three Question Types</h3>

<p><strong>Type 1: Find opposite when you know adjacent and angle</strong></p>
<div class="worked-example">
<p>Given: adjacent = 10, \\(\\theta = 40°\\). Find opposite.</p>
<p>Use TOA: \\(\\tan(40°) = \\frac{\\text{opp}}{10}\\), so \\(\\text{opp} = 10\\tan(40°) \\approx 8.39\\)</p>
</div>

<p><strong>Type 2: Find hypotenuse when you know opposite and angle</strong></p>
<div class="worked-example">
<p>Given: opposite = 7, \\(\\theta = 28°\\). Find hypotenuse.</p>
<p>Use SOH: \\(\\sin(28°) = \\frac{7}{\\text{hyp}}\\), so \\(\\text{hyp} = \\frac{7}{\\sin(28°)} \\approx 14.71\\)</p>
</div>

<p><strong>Type 3: Find adjacent when you know hypotenuse and angle</strong></p>
<div class="worked-example">
<p>Given: hypotenuse = 15, \\(\\theta = 50°\\). Find adjacent.</p>
<p>Use CAH: \\(\\cos(50°) = \\frac{\\text{adj}}{15}\\), so \\(\\text{adj} = 15\\cos(50°) \\approx 9.64\\)</p>
</div>

<h3>Strategy Checklist</h3>
<ul>
  <li>1. Label the right triangle clearly</li>
  <li>2. Identify which sides you know and which you need</li>
  <li>3. Choose SOH, CAH, or TOA based on which sides appear</li>
  <li>4. Write the ratio equation</li>
  <li>5. Solve for the unknown</li>
  <li>6. Check your answer makes sense (sides should be positive, acute angles should be less than 90°)</li>
</ul>
"""
    },
    {
        "title": "Finding Unknown Angles: The Inverse (Inverse) Functions",
        "body": """
<h3>The Inverse Problem</h3>
<p>Now we know the sides and need the angle. This requires the inverse trigonometric functions:</p>

<div class="concept-box">
<p>\\(\\sin^{-1}(x)\\) or \\(\\arcsin(x)\\) gives the angle whose sine is \\(x\\)</p>
<p>\\(\\cos^{-1}(x)\\) or \\(\\arccos(x)\\) gives the angle whose cosine is \\(x\\)</p>
<p>\\(\\tan^{-1}(x)\\) or \\(\\arctan(x)\\) gives the angle whose tangent is \\(x\\)</p>
</div>

<p><strong>Important:</strong> The inverse functions "undo" the trigonometric functions. If \\(\\sin(\\theta) = 0.5\\), then \\(\\theta = \\sin^{-1}(0.5) = 30°\\).</p>

<h3>Worked Example: Finding an Angle</h3>

<div class="worked-example">
<p><strong>Problem:</strong> In a right triangle, the opposite side is 6 and the hypotenuse is 10. Find angle \\(\\theta\\).</p>

<p><strong>Step 1:</strong> Identify which ratio to use.
<ul>
  <li>We have opposite and hypotenuse → use SOH (sine)</li>
</ul>
</p>

<p><strong>Step 2:</strong> Set up the ratio equation.
$$\\sin(\\theta) = \\frac{6}{10} = 0.6$$
</p>

<p><strong>Step 3:</strong> Use the inverse sine to find the angle.
$$\\theta = \\sin^{-1}(0.6) \\approx 36.87°$$
</p>

<p><strong>Check:</strong> \\(\\sin(36.87°) \\approx 0.6\\) ✓</p>
</div>

<h3>Real-World Problem</h3>

<div class="worked-example">
<p><strong>A ladder leans against a wall:</strong> The ladder is 5 meters long, and its base is 1.5 meters from the wall. At what angle does the ladder lean?</p>

<p><strong>Solution:</strong></p>
<p>The ladder forms the hypotenuse (5 m), the distance from wall is the adjacent side (1.5 m).</p>
<p>Using CAH: \\(\\cos(\\theta) = \\frac{1.5}{5} = 0.3\\)</p>
<p>\\(\\theta = \\cos^{-1}(0.3) \\approx 72.54°\\)</p>

<p>The ladder leans at about 72.54° from the ground.</p>
</div>
"""
    }
]
