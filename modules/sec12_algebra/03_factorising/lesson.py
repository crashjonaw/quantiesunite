"""Factorising — Lesson sections."""

TITLE = "Factorising"

SECTIONS = [
    {
        "title": "Factorising is the reverse of expanding",
        "body": """<div class="concept-box">
<p><strong>Expanding:</strong> Multiply out brackets</p>
<div class="formula-box">
<p>\\(3(x + 2) = 3x + 6\\)</p>
</div>
<p><strong>Factorising:</strong> Put brackets back in (reverse process)</p>
<div class="formula-box">
<p>\\(3x + 6 = 3(x + 2)\\)</p>
</div>
<p>Factorising reveals the <strong>common factors</strong> shared by all terms. This is a key skill for solving equations and simplifying expressions.</p>
</div>"""
    },
    {
        "title": "Finding the highest common factor (HCF)",
        "body": """<div class="concept-box">
<p>To factorise an expression, find the <strong>greatest common factor</strong> of all terms.</p>
<div class="worked-example concept-box">
<p><strong>Factorise: 4x + 12</strong></p>
<p>Factors of 4x: 1, 2, 4, x</p>
<p>Factors of 12: 1, 2, 3, 4, 6, 12</p>
<p>HCF = 4</p>
<p>\\(4x + 12 = 4(x + 3)\\)</p>
</div>
<div class="worked-example concept-box">
<p><strong>Factorise: 6x^2 - 9x</strong></p>
<p>Factors of 6x²: 1, 2, 3, 6, x, x²</p>
<p>Factors of 9x: 1, 3, 9, x</p>
<p>HCF = 3x</p>
<p>\\(6x^2 - 9x = 3x(2x - 3)\\)</p>
</div>
<p class="success-box formula-box">
<strong>Check by expanding:</strong> \\(3x(2x - 3) = 3x \\cdot 2x - 3x \\cdot 3 = 6x^2 - 9x\\) ✓
</p>
</div>"""
    },
    {
        "title": "Factorising by grouping",
        "body": """<div class="concept-box">
<p>When there are four terms with no obvious common factor, try <strong>grouping in pairs</strong>.</p>
<div class="worked-example concept-box">
<p><strong>Factorise: ax + ay + bx + by</strong></p>
<p>Group: \\((ax + ay) + (bx + by)\\)</p>
<p>Factor each group: \\(a(x + y) + b(x + y)\\)</p>
<p>Factor out the common bracket: \\((a + b)(x + y)\\)</p>
</div>
<div class="worked-example concept-box">
<p><strong>Factorise: 2x + 6 + xy + 3y</strong></p>
<p>Group: \\((2x + 6) + (xy + 3y)\\)</p>
<p>Factor each group: \\(2(x + 3) + y(x + 3)\\)</p>
<p>Factor out \\((x + 3)\\): \\((x + 3)(2 + y)\\) or \\((2 + y)(x + 3)\\)</p>
</div>
</div>"""
    },
    {
        "title": "Factorising quadratic expressions",
        "body": """<div class="concept-box">
<p>For expressions of the form \\(x^2 + bx + c\\), find two numbers that:</p>
<ul >
<li>Multiply to give \\(c\\)</li>
<li>Add to give \\(b\\)</li>
</ul>
<div class="worked-example concept-box">
<p><strong>Factorise: x^2 + 5x + 6</strong></p>
<p>Two numbers that multiply to 6 and add to 5: 2 and 3</p>
<p>\\(x^2 + 5x + 6 = (x + 2)(x + 3)\\)</p>
</div>
<div class="worked-example concept-box">
<p><strong>Factorise: x^2 - 4x + 3</strong></p>
<p>Two numbers that multiply to 3 and add to -4: -1 and -3</p>
<p>\\(x^2 - 4x + 3 = (x - 1)(x - 3)\\)</p>
</div>
<p class="warning-box formula-box">
<strong>Tip:</strong> Always check that all four products work before writing your answer.
</p>
</div>"""
    }
]
