TITLE = "The Quadratic Formula"

SECTIONS = [
    {
        "title": "Deriving the Quadratic Formula from First Principles",
        "body": """
<h3>The Ultimate Tool</h3>
<p>The quadratic formula is the most general method to solve any quadratic equation. We derive it using completing the square:</p>

<p style="margin: 15px 0"><strong>Starting with:</strong> ax² + bx + c = 0 (where a ≠ 0)</p>

<h3>Step-by-Step Derivation</h3>

<p style="margin-top: 15px"><strong>Step 1:</strong> Divide everything by a</p>
<p>$$x^2 + \\frac{b}{a}x + \\frac{c}{a} = 0$$</p>

<p style="margin-top: 15px"><strong>Step 2:</strong> Isolate constant</p>
<p>$$x^2 + \\frac{b}{a}x = -\\frac{c}{a}$$</p>

<p style="margin-top: 15px"><strong>Step 3:</strong> Complete the square. Take half the coefficient of x: \\(\\frac{b}{2a}\\), then square it: \\(\\left(\\frac{b}{2a}\\right)^2 = \\frac{b^2}{4a^2}\\)</p>
<p>$$x^2 + \\frac{b}{a}x + \\frac{b^2}{4a^2} = -\\frac{c}{a} + \\frac{b^2}{4a^2}$$</p>

<p style="margin-top: 15px"><strong>Step 4:</strong> Write left side as perfect square</p>
<p>$$\\left(x + \\frac{b}{2a}\\right)^2 = \\frac{b^2 - 4ac}{4a^2}$$</p>

<p style="margin-top: 15px"><strong>Step 5:</strong> Take square roots of both sides</p>
<p>$$x + \\frac{b}{2a} = \\pm \\frac{\\sqrt{b^2 - 4ac}}{2a}$$</p>

<p style="margin-top: 15px"><strong>Step 6:</strong> Solve for x</p>
<div class="formula-box">
<p>$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$</p>
<p style="font-size: 0.9em; margin-top: 10px; font-style: italic">This is the QUADRATIC FORMULA</p>
</div>

<div class="success-box" style="background-color: rgba(76, 175, 80, 0.1); border-left: 4px solid #4caf50; padding: 15px; margin: 15px 0; border-radius: 4px;">
<p ><strong>Remarkable Fact:</strong> This formula works for ANY quadratic equation. No exceptions!</p>
</div>
"""
    },
    {
        "title": "Understanding the Formula Components",
        "body": """
<h3>Breaking Down the Formula</h3>

<p style="font-size: 1.05em; margin: 15px 0">$$x = \\underbrace{\\frac{-b}{2a}}_\\text{shift} \\pm \\underbrace{\\frac{\\sqrt{b^2 - 4ac}}{2a}}_\\text{spread}$$</p>

<h3>What Each Part Means</h3>

<table style="width: 100%; border-collapse: collapse; margin: 15px 0">
  <tr >
    <th style="padding: 12px; text-align: left"><strong>Component</strong></th>
    <th style="padding: 12px; text-align: left"><strong>Meaning</strong></th>
  </tr>
  <tr >
    <td style="padding: 12px;">-b/(2a)</td>
    <td style="padding: 12px;">The center point between the two roots (also the x-coordinate of the vertex)</td>
  </tr>
  <tr >
    <td style="padding: 12px;">√(b² - 4ac)</td>
    <td style="padding: 12px;">The discriminant (Δ) under the square root—tells how far roots spread from center</td>
  </tr>
  <tr >
    <td style="padding: 12px;">±</td>
    <td style="padding: 12px;">We get two solutions: one with +, one with -</td>
  </tr>
  <tr>
    <td style="padding: 12px;">2a in denominator</td>
    <td style="padding: 12px;">The stretch factor—how the leading coefficient affects root positions</td>
  </tr>
</table>

<h3>The Role of the Discriminant Revisited</h3>
<p style="margin: 15px 0">Recall: Δ = b² - 4ac</p>

<ul style="line-height: 1.8;">
  <li><strong>If Δ > 0:</strong> √Δ is real → two distinct real roots</li>
  <li><strong>If Δ = 0:</strong> √Δ = 0 → one repeated root: x = -b/(2a)</li>
  <li><strong>If Δ < 0:</strong> √Δ is imaginary → two complex conjugate roots</li>
</ul>
"""
    },
    {
        "title": "Using the Quadratic Formula: Worked Examples",
        "body": """
<h3>Standard Application</h3>

<div class="worked-example">
<h4 class="accent-heading">Example 1: Basic Quadratic</h4>
<p><strong>Problem:</strong> Solve 3x² - 4x - 5 = 0</p>
<p><strong>Solution:</strong></p>
<p><strong>Identify:</strong> a = 3, b = -4, c = -5</p>

<p style="margin-top: 10px;"><strong>Calculate Δ:</strong><br>
$$\\Delta = (-4)^2 - 4(3)(-5) = 16 + 60 = 76$$</p>

<p style="margin-top: 10px;"><strong>Simplify √76:</strong><br>
$$\\sqrt{76} = \\sqrt{4 \\cdot 19} = 2\\sqrt{19}$$</p>

<p style="margin-top: 10px;"><strong>Apply formula:</strong><br>
$$x = \\frac{-(-4) \\pm 2\\sqrt{19}}{2(3)} = \\frac{4 \\pm 2\\sqrt{19}}{6} = \\frac{2(2 \\pm \\sqrt{19})}{6} = \\frac{2 \\pm \\sqrt{19}}{3}$$</p>

<p style="margin-top: 10px"><strong>Answer:</strong> \\(x = \\frac{2 + \\sqrt{19}}{3}\\) or \\(x = \\frac{2 - \\sqrt{19}}{3}\\) <br>
(Approximately x ≈ 1.79 or x ≈ -0.79)</p>
</div>

<div class="worked-example">
<h4 class="accent-heading">Example 2: Perfect Discriminant</h4>
<p><strong>Problem:</strong> Solve x² - 6x + 8 = 0</p>
<p><strong>Solution:</strong></p>
<p><strong>Identify:</strong> a = 1, b = -6, c = 8</p>

<p style="margin-top: 10px;"><strong>Calculate Δ:</strong><br>
$$\\Delta = (-6)^2 - 4(1)(8) = 36 - 32 = 4$$</p>

<p style="margin-top: 10px;"><strong>Apply formula:</strong><br>
$$x = \\frac{-(-6) \\pm \\sqrt{4}}{2(1)} = \\frac{6 \\pm 2}{2}$$</p>

<p style="margin-top: 10px;"><strong>Simplify:</strong><br>
$$x = \\frac{6 + 2}{2} = 4 \\quad \\text{or} \\quad x = \\frac{6 - 2}{2} = 2$$</p>

<p style="margin-top: 10px"><strong>Answer:</strong> x = 2 or x = 4</p>
</div>

<div class="worked-example">
<h4 class="accent-heading">Example 3: Negative Discriminant</h4>
<p><strong>Problem:</strong> Solve x² + 2x + 5 = 0</p>
<p><strong>Solution:</strong></p>
<p><strong>Identify:</strong> a = 1, b = 2, c = 5</p>

<p style="margin-top: 10px;"><strong>Calculate Δ:</strong><br>
$$\\Delta = 2^2 - 4(1)(5) = 4 - 20 = -16$$</p>

<p style="margin-top: 10px;"><strong>Interpretation:</strong> Since Δ < 0, there are no real roots. The solutions are complex.</p>

<p style="margin-top: 10px;"><strong>Complex solutions:</strong><br>
$$x = \\frac{-2 \\pm \\sqrt{-16}}{2} = \\frac{-2 \\pm 4i}{2} = -1 \\pm 2i$$</p>

<p style="margin-top: 10px"><strong>Answer:</strong> x = -1 + 2i or x = -1 - 2i (complex conjugates)</p>
</div>

<div class="warning-box" style="background-color: rgba(255, 165, 0, 0.1); border-left: 4px solid #ff9800; padding: 15px; margin: 15px 0; border-radius: 4px;">
<p ><strong>Tip:</strong> Always simplify square roots! \\(\\sqrt{12} = 2\\sqrt{3}\\), \\(\\sqrt{50} = 5\\sqrt{2}\\), etc.</p>
</div>
"""
    }
]
