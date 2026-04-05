TITLE = "Applications and Vieta's Formulas"

SECTIONS = [
    {
        "title": "Vieta's Formulas: Relating Roots to Coefficients",
        "body": """
<h3>The Beautiful Connection</h3>
<p>There's a remarkable relationship between the roots of a quadratic and its coefficients. If $\\alpha$ and $\\beta$ are the roots of $ax^2 + bx + c = 0$, then:</p>

<div class="formula-box">
<p>$$\\alpha + \\beta = -\\frac{b}{a}$$</p>
<p>$$\\alpha \\beta = \\frac{c}{a}$$</p>
<p style="font-size: 0.9em; margin-top: 10px"><strong>Vieta's Formulas</strong> — named after François Viète (1540-1603)</p>
</div>

<h3>Why Do These Work?</h3>
<p>If α and β are roots, then by the factored form:</p>
<p>$$ax^2 + bx + c = a(x - \\alpha)(x - \\beta)$$</p>

<p style="margin-top: 10px;">Expanding the right side:</p>
<p>$$a(x - \\alpha)(x - \\beta) = a(x^2 - (\\alpha + \\beta)x + \\alpha\\beta)$$
<br>$$= ax^2 - a(\\alpha + \\beta)x + a\\alpha\\beta$$</p>

<p style="margin-top: 10px;">Comparing with ax² + bx + c:</p>
<ul style="line-height: 1.8;">
  <li>Coefficient of x: -a(α + β) = b  →  α + β = -b/a</li>
  <li>Constant term: aαβ = c  →  αβ = c/a</li>
</ul>

<div class="success-box" style="background-color: rgba(76, 175, 80, 0.1); border-left: 4px solid #4caf50; padding: 15px; margin: 15px 0; border-radius: 4px;">
<p ><strong>Power of Vieta's Formulas:</strong> You can find information about roots WITHOUT solving the equation!</p>
</div>
"""
    },
    {
        "title": "Using Vieta's Formulas: Worked Examples",
        "body": """
<h3>Application 1: Finding Properties of Roots</h3>

<div class="worked-example">
<h4 class="accent-heading">Example 1: Sum and Product of Roots</h4>
<p><strong>Problem:</strong> The roots of 2x² - 6x + 4 = 0 are α and β. Find α + β and αβ.</p>
<p><strong>Solution:</strong></p>

<p style="margin: 10px 0;"><strong>Method 1 (Vieta's Formulas):</strong></p>
<p>$$\\alpha + \\beta = -\\frac{b}{a} = -\\frac{-6}{2} = 3$$</p>
<p>$$\\alpha\\beta = \\frac{c}{a} = \\frac{4}{2} = 2$$</p>

<p style="margin: 10px 0;"><strong>Verification:</strong> Actually solving: 2x² - 6x + 4 = 0 → x² - 3x + 2 = 0 → (x-1)(x-2) = 0</p>
<p class="text-muted-note">So α = 1 and β = 2. Indeed: 1 + 2 = 3 ✓ and 1(2) = 2 ✓</p>
</div>

<h3>Application 2: Finding α² + β² Without Solving</h3>

<div class="worked-example">
<h4 class="accent-heading">Example 2: Sum of Squares</h4>
<p><strong>Problem:</strong> If α and β are roots of x² - 6x + 8 = 0, find α² + β² without finding α and β.</p>
<p><strong>Solution:</strong></p>

<p style="margin: 10px 0;"><strong>From Vieta's Formulas:</strong></p>
<p>$$\\alpha + \\beta = 6$$</p>
<p>$$\\alpha\\beta = 8$$</p>

<p style="margin: 10px 0;"><strong>Algebraic Trick:</strong></p>
<p>We know that (α + β)² = α² + 2αβ + β²</p>
<p>Therefore: α² + β² = (α + β)² - 2αβ</p>

<p style="margin: 10px 0;">$$\\alpha^2 + \\beta^2 = 6^2 - 2(8) = 36 - 16 = 20$$</p>

<p class="text-muted-note"><strong>Verification:</strong> Roots are x = 2 and x = 4, so 2² + 4² = 4 + 16 = 20 ✓</p>
</div>

<h3>Application 3: Constructing Quadratics from Roots</h3>

<div class="worked-example">
<h4 class="accent-heading">Example 3: Building a Quadratic</h4>
<p><strong>Problem:</strong> Write a quadratic equation whose roots are 2 + √3 and 2 - √3</p>
<p><strong>Solution:</strong></p>

<p style="margin: 10px 0;"><strong>Calculate sum and product:</strong></p>
<p>$$\\alpha + \\beta = (2 + \\sqrt{3}) + (2 - \\sqrt{3}) = 4$$</p>
<p>$$\\alpha\\beta = (2 + \\sqrt{3})(2 - \\sqrt{3}) = 4 - 3 = 1$$</p>

<p style="margin: 10px 0;"><strong>Use the formula for a monic quadratic:</strong></p>
<p>$$x^2 - (\\alpha + \\beta)x + \\alpha\\beta = 0$$
<br>$$x^2 - 4x + 1 = 0$$</p>

<p class="text-muted-note"><strong>Verification:</strong> Using the quadratic formula on x² - 4x + 1 = 0:</p>
<p class="text-muted-note">$$x = \\frac{4 \\pm \\sqrt{16 - 4}}{2} = \\frac{4 \\pm \\sqrt{12}}{2} = \\frac{4 \\pm 2\\sqrt{3}}{2} = 2 \\pm \\sqrt{3}$$ ✓</p>
</div>
"""
    },
    {
        "title": "Real-World Applications: Optimization and Motion",
        "body": """
<h3>Optimization: Maximizing Area with Constraints</h3>

<div class="worked-example">
<h4 class="accent-heading">Example 4: Farmer's Fencing Problem</h4>
<p><strong>Problem:</strong> A farmer has 100 meters of fencing to enclose a rectangular field against a river (one side is the river, so no fencing needed). What dimensions maximize the area?</p>
<p><strong>Solution:</strong></p>

<p style="margin: 10px 0;"><strong>Step 1: Set up variables</strong></p>
<p class="text-muted-note">Let x = width (perpendicular to river) in meters<br>
Then y = length (parallel to river) in meters</p>

<p style="margin: 10px 0;"><strong>Step 2: Write constraints</strong></p>
<p>Fencing needed: 2x + y = 100<br>
Therefore: y = 100 - 2x</p>

<p style="margin: 10px 0;"><strong>Step 3: Express area as function of x</strong></p>
<p>$$A(x) = xy = x(100 - 2x) = 100x - 2x^2$$</p>

<p style="margin: 10px 0;"><strong>Step 4: Find the maximum</strong></p>
<p>This is a quadratic with a = -2 < 0 (opens downward), so maximum at vertex.</p>
<p>$$x = -\\frac{100}{2(-2)} = -\\frac{100}{-4} = 25 \\text{ meters}$$</p>

<p style="margin: 10px 0;"><strong>Step 5: Find y and maximum area</strong></p>
<p>$$y = 100 - 2(25) = 50 \\text{ meters}$$
<br>$$A_{\\max} = 25 \\times 50 = 1250 \\text{ m}^2$$</p>

<p class="text-muted-note"><strong>Answer:</strong> Width 25 m, Length 50 m yields maximum area of 1250 m²</p>
</div>

<h3>Projectile Motion: When Does a Ball Return to Ground?</h3>

<div class="worked-example">
<h4 class="accent-heading">Example 5: Ball Thrown Upward</h4>
<p><strong>Problem:</strong> A ball is thrown upward from ground level (h₀ = 0) with initial velocity v₀ = 20 m/s. When does it return to ground level? (Use g = 10 m/s²)</p>
<p><strong>Solution:</strong></p>

<p style="margin: 10px 0;"><strong>Height equation:</strong></p>
<p>$$h(t) = -\\frac{1}{2}gt^2 + v_0 t + h_0 = -5t^2 + 20t$$</p>

<p style="margin: 10px 0;"><strong>When does h(t) = 0?</strong></p>
<p>$$-5t^2 + 20t = 0$$
<br>$$-5t(t - 4) = 0$$</p>

<p style="margin: 10px 0;"><strong>Solutions:</strong> t = 0 (at release) or t = 4 seconds (returns to ground)</p>

<p class="text-muted-note"><strong>Bonus:</strong> Maximum height at t = -b/(2a) = -20/(2(-5)) = 2 seconds</p>
<p class="text-muted-note">h(2) = -5(4) + 20(2) = -20 + 40 = 20 meters</p>

<p class="text-muted-note"><strong>Answer:</strong> Ball returns to ground after 4 seconds. Max height is 20 meters at t = 2 seconds.</p>
</div>

<h3>Revenue Maximization in Business</h3>

<div class="worked-example">
<h4 class="accent-heading">Example 6: Optimal Pricing</h4>
<p><strong>Problem:</strong> A store's weekly demand is q = 500 - 2p units at price p dollars. Find the price that maximizes revenue.</p>
<p><strong>Solution:</strong></p>

<p style="margin: 10px 0;"><strong>Revenue function:</strong></p>
<p>$$R(p) = p \\cdot q = p(500 - 2p) = 500p - 2p^2$$</p>

<p style="margin: 10px 0;"><strong>Find maximum:</strong></p>
<p>This is a downward-opening parabola. Maximum at:</p>
<p>$$p = -\\frac{500}{2(-2)} = -\\frac{500}{-4} = 125 \\text{ dollars}$$</p>

<p style="margin: 10px 0;"><strong>Corresponding demand and revenue:</strong></p>
<p>$$q = 500 - 2(125) = 250 \\text{ units}$$
<br>$$R_{\\max} = 125 \\times 250 = 31,250 \\text{ dollars}$$</p>

<p class="text-muted-note"><strong>Answer:</strong> Optimal price is $125, selling 250 units for maximum revenue of $31,250</p>
</div>
"""
    }
]
