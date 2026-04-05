"""Algebraic Expressions — Lesson sections."""

TITLE = "Algebraic Expressions"

SECTIONS = [
    {
        "title": "From unknowns to variables",
        "body": """<div class="concept-box">
<p>In primary school, you solved puzzles like: <strong>"A number plus 3 equals 7. Find the number."</strong></p>
<p>In algebra, we use a <strong>letter</strong> (called a variable) to stand for the unknown number. We write:</p>
<div class="formula-box">
<p>\\(x + 3 = 7\\)</p>
</div>
<p><strong>x is a variable.</strong> It represents a number we don't know yet.</p>
<p>Variables are just placeholders — they can be any letter: \\(x\\), \\(y\\), \\(n\\), \\(a\\), etc.</p>
</div>"""
    },
    {
        "title": "Building algebraic expressions",
        "body": """<div class="concept-box">
<p>An <strong>algebraic expression</strong> is a mathematical phrase using variables, numbers, and operations.</p>
<table style="width:100%; border-collapse:collapse; margin:12px 0;">
<tr >
<th style="padding: 8px; text-align: left"><strong>English</strong></th>
<th style="padding: 8px; text-align: left"><strong>Expression</strong></th>
</tr>
<tr >
<td style="padding: 8px;">A number times 5</td>
<td style="padding: 8px;">\\(5x\\)</td>
</tr>
<tr >
<td style="padding: 8px;">A number plus 2</td>
<td style="padding: 8px;">\\(x + 2\\)</td>
</tr>
<tr >
<td style="padding: 8px;">A number minus 4, times 3</td>
<td style="padding: 8px;">\\(3(x - 4)\\)</td>
</tr>
<tr >
<td style="padding: 8px;">Twice a number plus 1</td>
<td style="padding: 8px;">\\(2x + 1\\)</td>
</tr>
</table>
<p><strong>Note:</strong> \\(5x\\) means \\(5 \\times x\\). We write it without the multiplication sign.</p>
</div>"""
    },
    {
        "title": "Like terms and collecting",
        "body": """<div class="concept-box">
<p><strong>Like terms</strong> are terms that have the same variable raised to the same power.</p>
<p class="formula-box">
<strong>Like terms:</strong> \\(3x\\) and \\(5x\\) (both have \\(x\\))<br>
<strong>Like terms:</strong> \\(2x^2\\) and \\(-7x^2\\) (both have \\(x^2\\))<br>
<strong>NOT like terms:</strong> \\(3x\\) and \\(3x^2\\) (different powers)<br>
<strong>NOT like terms:</strong> \\(5x\\) and \\(7y\\) (different variables)
</p>
<p>We can simplify expressions by <strong>collecting like terms</strong>:</p>
<div class="worked-example concept-box">
<p><strong>Simplify:</strong> \\(3x + 5x + 2\\)</p>
<p>\\(= 8x + 2\\) (collect \\(3x + 5x\\))</p>
</div>
<div class="worked-example concept-box">
<p><strong>Simplify:</strong> \\(4x + 3 - 2x + 1\\)</p>
<p>\\(= 4x - 2x + 3 + 1\\) (group like terms)</p>
<p>\\(= 2x + 4\\)</p>
</div>
</div>"""
    },
    {
        "title": "Substitution: testing values",
        "body": """<div class="concept-box">
<p><strong>Substitution</strong> means replacing a variable with a number to find the value of an expression.</p>
<div class="worked-example concept-box">
<p><strong>Find the value of</strong> \\(2x + 3\\) <strong>when</strong> \\(x = 5\\)</p>
<p>Replace \\(x\\) with 5:</p>
<p>\\(2(5) + 3 = 10 + 3 = 13\\)</p>
</div>
<div class="worked-example concept-box">
<p><strong>Find the value of</strong> \\(x^2 - 3x\\) <strong>when</strong> \\(x = 4\\)</p>
<p>\\((4)^2 - 3(4) = 16 - 12 = 4\\)</p>
</div>
<p class="warning-box formula-box">
<strong>Remember:</strong> Follow order of operations (BIDMAS/PEMDAS). Do exponents and multiplication before addition and subtraction.
</p>
</div>"""
    }
]
