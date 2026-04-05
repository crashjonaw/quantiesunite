TITLE = "Congruence and Similarity of Shapes"

SECTIONS = [
    {
        "title": "Congruent Shapes: Identical in Every Way",
        "body": """
<h4>What Does Congruent Mean?</h4>
<div class="concept-box">
<p><strong>Congruent shapes</strong> are exactly the same shape and size. If you cut one out, it would fit perfectly on top of the other (possibly after rotating or flipping).</p>
<p><strong>Symbol:</strong> We write \\(\\triangle ABC \\cong \\triangle DEF\\) to mean the triangles are congruent.</p>
</div>

<h4>Four Tests for Congruent Triangles</h4>
<p>Two triangles are congruent if ONE of these conditions is true:</p>

<div class="success-box">
<h5>1. SSS (Side-Side-Side)</h5>
<p>All three sides of one triangle equal all three sides of the other.</p>
<svg width="100%" height="120" viewBox="0 0 400 120" class="formula-box">
  <text x="20" y="25" fill='currentColor' font-size='12' font-weight='bold'>Triangle 1:</text>
  <polygon points="50,100 30,40 90,40" fill='none' stroke='#58a6ff' stroke-width="2.5"/>
  <text x="40" y="75" fill='#79c0ff' font-size='11'>5cm</text>
  <text x="75" y="55" fill='#79c0ff' font-size='11'>4cm</text>
  <text x="60" y="110" fill='#79c0ff' font-size='11'>3cm</text>

  <text x="200" y="25" fill='currentColor' font-size='12' font-weight='bold'>Triangle 2:</text>
  <polygon points="250,100 230,40 290,40" fill='none' stroke='#56d364' stroke-width="2.5"/>
  <text x="240" y="75" fill='#79c0ff' font-size='11'>5cm</text>
  <text x="275" y="55" fill='#79c0ff' font-size='11'>4cm</text>
  <text x="260" y="110" fill='#79c0ff' font-size='11'>3cm</text>

  <text x="100" y="50" fill='currentColor' font-size='13' font-weight='bold'>✓ SSS</text>
</svg>
</div>

<div class="success-box">
<h5>2. SAS (Side-Angle-Side)</h5>
<p>Two sides and the included angle (the angle between them) are equal.</p>
<p><strong>Important:</strong> The angle MUST be between the two sides!</p>
<svg width="100%" height="120" viewBox="0 0 400 120" class="formula-box">
  <text x="20" y="25" fill='currentColor' font-size='12' font-weight='bold'>Triangle 1: 5cm, 60°, 4cm</text>
  <polygon points="50,100 30,40 90,40" fill='none' stroke='#58a6ff' stroke-width="2.5"/>
  <text x="40" y="75" fill='#79c0ff' font-size='10'>4cm</text>
  <text x="75" y="55" fill='#79c0ff' font-size='10'>5cm</text>
  <circle cx="30" cy="40" r="12" fill='none' stroke='#79c0ff' stroke-width="1.5"/>
  <text x="18" y="50" fill='#79c0ff' font-size='10'>60°</text>

  <text x="200" y="25" fill='currentColor' font-size='12' font-weight='bold'>Triangle 2: 5cm, 60°, 4cm</text>
  <polygon points="250,100 230,40 290,40" fill='none' stroke='#56d364' stroke-width="2.5"/>
  <text x="240" y="75" fill='#79c0ff' font-size='10'>4cm</text>
  <text x="275" y="55" fill='#79c0ff' font-size='10'>5cm</text>
  <circle cx="230" cy="40" r="12" fill='none' stroke='#79c0ff' stroke-width="1.5"/>
  <text x="218" y="50" fill='#79c0ff' font-size='10'>60°</text>

  <text x="100" y="50" fill='currentColor' font-size='13' font-weight='bold'>✓ SAS</text>
</svg>
</div>

<div class="success-box">
<h5>3. ASA (Angle-Side-Angle)</h5>
<p>Two angles and the included side (the side between them) are equal.</p>
<p><strong>Important:</strong> The side MUST be between the two angles!</p>
</div>

<div class="success-box">
<h5>4. RHS (Right angle-Hypotenuse-Side)</h5>
<p>For right-angled triangles: the hypotenuse and one other side are equal.</p>
<p><strong>Note:</strong> The right angle doesn't need to be stated (it's guaranteed), and only the hypotenuse and one side matter.</p>
<svg width="100%" height="120" viewBox="0 0 400 120" class="formula-box">
  <text x="20" y="25" fill='currentColor' font-size='12' font-weight='bold'>Triangle 1: hyp=10, side=6</text>
  <polygon points="50,100 30,40 90,100" fill='none' stroke='#58a6ff' stroke-width="2.5"/>
  <rect x="85" y="95" width="7" height="7" fill='none' stroke='#58a6ff' stroke-width="1.5"/>
  <text x="60" y="70" fill='#79c0ff' font-size='10'>10cm</text>
  <text x="75" y="110" fill='#79c0ff' font-size='10'>6cm</text>

  <text x="200" y="25" fill='currentColor' font-size='12' font-weight='bold'>Triangle 2: hyp=10, side=6</text>
  <polygon points="250,100 230,40 290,100" fill='none' stroke='#56d364' stroke-width="2.5"/>
  <rect x="285" y="95" width="7" height="7" fill='none' stroke='#56d364' stroke-width="1.5"/>
  <text x="260" y="70" fill='#79c0ff' font-size='10'>10cm</text>
  <text x="275" y="110" fill='#79c0ff' font-size='10'>6cm</text>

  <text x="100" y="50" fill='currentColor' font-size='13' font-weight='bold'>✓ RHS</text>
</svg>
</div>

<h4>Why These Tests Work</h4>
<div class="warning-box">
<p>Once you specify certain parts of a triangle (the required sides and angles), the rest of the triangle is completely determined. You cannot draw a different triangle with the same parts—the shape is fixed!</p>
</div>
"""
    },
    {
        "title": "Similar Shapes: Same Shape, Different Sizes",
        "body": """
<h4>What Does Similar Mean?</h4>
<div class="concept-box">
<p><strong>Similar shapes</strong> have the same shape but different sizes. One is an enlargement (or reduction) of the other.</p>
<p><strong>Key idea:</strong> All corresponding angles are equal, and all corresponding sides are proportional (in the same ratio).</p>
<p><strong>Symbol:</strong> We write \\(\\triangle ABC \\sim \\triangle DEF\\) to mean the triangles are similar.</p>
</div>

<h4>Example: Similar Triangles</h4>
<div class="success-box">
<p><strong>Triangle A: sides 3 cm, 4 cm, 5 cm</strong></p>
<p><strong>Triangle B: sides 6 cm, 8 cm, 10 cm</strong></p>
<p><strong>Scale factor:</strong> 6÷3 = 8÷4 = 10÷5 = 2</p>
<p>Triangle B is an enlargement of Triangle A with scale factor 2.</p>
<p><strong>They are similar (same angles, proportional sides).</strong></p>

<svg width="100%" height="160" viewBox="0 0 500 160" class="formula-box">
  <text x="40" y="25" fill='currentColor' font-size='12' font-weight='bold'>Triangle A (3-4-5)</text>
  <polygon points="80,140 50,70 110,70" fill='none' stroke='#58a6ff' stroke-width="2.5"/>
  <text x="60" y="105" fill='#79c0ff' font-size='10'>4cm</text>
  <text x="95" y="85" fill='#79c0ff' font-size='10'>3cm</text>
  <text x="80" y="155" fill='#79c0ff' font-size='10'>5cm</text>

  <text x="260" y="25" fill='currentColor' font-size='12' font-weight='bold'>Triangle B (6-8-10)</text>
  <polygon points="320,140 260,30 380,30" fill='none' stroke='#56d364' stroke-width="2.5"/>
  <text x="275" y="85" fill='#79c0ff' font-size='10'>8cm</text>
  <text x="325" y="55" fill='#79c0ff' font-size='10'>6cm</text>
  <text x="340" y="155" fill='#79c0ff' font-size='10'>10cm</text>

  <text x="150" y="80" fill='#a371f7' font-size='11' font-weight='bold'>Scale × 2</text>
</svg>
</div>

<h4>Tests for Similar Triangles</h4>

<div class="success-box">
<h5>1. AAA (Angle-Angle-Angle)</h5>
<p>If all three angles of one triangle match all three angles of another, the triangles are similar.</p>
<p><strong>Note:</strong> You only need to check two angles (AA), because if two angles match, the third must also match!</p>
</div>

<div class="success-box">
<h5>2. SSS (Side-Side-Side)</h5>
<p>If all three sides of one triangle are proportional to all three sides of another, they're similar.</p>
<p><strong>Example:</strong> Triangle with sides 2, 3, 4 is similar to triangle with sides 4, 6, 8 (scale factor 2).</p>
</div>

<div class="success-box">
<h5>3. SAS (Side-Angle-Side)</h5>
<p>If two sides are proportional and the included angle is equal, the triangles are similar.</p>
</div>

<h4>Finding Unknown Sides in Similar Triangles</h4>
<div class="warning-box">
<p><strong>Triangle A has sides 2cm, 3cm, 4cm. Triangle B is similar with sides 4cm, 6cm, and x. Find x.</strong></p>
<div class="worked-example">
<p>Check the scale factor:</p>
<p>4÷2 = 2 and 6÷3 = 2, so scale factor = 2</p>
<p>x = 4 × 2 = 8 cm</p>
<p><strong>Answer: x = 8 cm</strong></p>
</div>
</div>
"""
    },
    {
        "title": "Linear Scale Factor vs Area Scale Factor",
        "body": """
<h4>The Two-Dimensional Nature of Area</h4>
<div class="concept-box">
<p>When shapes are similar with a <strong>linear scale factor k</strong> (sides scaled by k):</p>
<ul >
<li><strong>Linear scale factor:</strong> k</li>
<li><strong>Area scale factor:</strong> k²</li>
</ul>
<p><strong>Why?</strong> Area is two-dimensional, so it scales with the square of the linear scale factor.</p>
</div>

<h4>Example: Areas of Similar Shapes</h4>
<div class="success-box">
<p><strong>Triangle A has area 10 cm². Triangle B is similar with linear scale factor 3.</strong></p>
<p>What is the area of Triangle B?</p>

<p>Area of B = 10 × 3² = 10 × 9 = 90 cm²</p>

<svg width="100%" height="180" viewBox="0 0 500 180" class="formula-box">
  <!-- Triangle A -->
  <text x="40" y="25" fill='currentColor' font-size='12' font-weight='bold'>Triangle A (scale × 1)</text>
  <polygon points="80,140 50,60 110,60" fill='#1f6feb' opacity='0.3' stroke='#58a6ff' stroke-width="2.5"/>
  <text x="70" y="100" fill='#79c0ff' font-size='11' font-weight='bold'>Area = 10 cm²</text>

  <!-- Triangle B -->
  <text x="260" y="25" fill='currentColor' font-size='12' font-weight='bold'>Triangle B (scale × 3)</text>
  <polygon points="360,150 260,10 460,10" fill='#1f6feb' opacity='0.3' stroke='#56d364' stroke-width="2.5"/>
  <text x="330" y="85" fill='#79c0ff' font-size='11' font-weight='bold'>Area = 90 cm²</text>

  <text x="80" y="170" fill='#a371f7' font-size='12'>Linear: × 3</text>
  <text x="330" y="170" fill='#a371f7' font-size='12'>Area: × 9 = 3²</text>
</svg>
</div>

<h4>General Formula</h4>
<div class="warning-box">
<p><strong>If linear scale factor = k, then area scale factor = k²</strong></p>
<p>\\(\\text{New Area} = \\text{Original Area} \\times k^2\\)</p>

<p><strong>Examples:</strong></p>
<ul>
<li>Scale factor 2 → area scale factor = 4</li>
<li>Scale factor 3 → area scale factor = 9</li>
<li>Scale factor ½ → area scale factor = ¼</li>
<li>Scale factor 10 → area scale factor = 100</li>
</ul>
</div>
"""
    },
    {
        "title": "Congruent vs Similar: Key Differences",
        "body": """
<h4>Comparison Table</h4>
<div class="success-box">
<table style="width: 100%">
<tr style=";">
<th>Property</th><th>Congruent</th><th>Similar</th>
</tr>
<tr class="formula-box">
<td><strong>Same shape?</strong></td><td>✓ Yes</td><td>✓ Yes</td>
</tr>
<tr class="formula-box">
<td><strong>Same size?</strong></td><td>✓ Yes</td><td>✗ No</td>
</tr>
<tr class="formula-box">
<td><strong>Angles equal?</strong></td><td>✓ Yes</td><td>✓ Yes</td>
</tr>
<tr class="formula-box">
<td><strong>Sides equal?</strong></td><td>✓ Yes</td><td>✗ Proportional</td>
</tr>
<tr class="formula-box">
<td><strong>Scale factor</strong></td><td>k = 1</td><td>k ≠ 1</td>
</tr>
</table>
</div>

<h4>Important Rule</h4>
<div class="concept-box">
<p><strong>All congruent shapes are similar, but not all similar shapes are congruent.</strong></p>
<p>Why? Congruence is a special case of similarity where the scale factor equals 1.</p>
</div>

<h4>Identifying the Right Relationship</h4>
<div class="warning-box">
<p><strong>Shape A: sides 3cm, 4cm, 5cm with angles 30°, 60°, 90°</strong></p>
<p><strong>Shape B: sides 3cm, 4cm, 5cm with angles 30°, 60°, 90°</strong></p>
<p>→ <strong>Congruent</strong> (same size and shape)</p>

<p><strong>Shape C: sides 6cm, 8cm, 10cm with angles 30°, 60°, 90°</strong></p>
<p>→ <strong>Similar to A and B</strong> (same shape, different size, scale factor 2)</p>
</div>
"""
    }
]
