TITLE = "Variables and Expressions"

SECTIONS = [
    {
        "title": "What is a Variable?",
        "body": """
<h4>A Variable is a Placeholder</h4>
<p>A <strong>variable</strong> is a letter that can stand for different numbers.</p>

<div class='concept-box'>
<p>Think of it like a box:</p>
<p style='text-align: center; font-size: 24px; font-family: monospace; background: #f9f9f9; padding: 15px; border-radius: 5px;'>[   x   ]</p>
<p>Inside the box is a number we don't know yet. The letter \\(x\\) is just the label on the box.</p>
</div>

<h4>Variables Can Represent Many Things:</h4>
<ul>
<li>\\(x\\) could be any number: 1, 5, 10, 100, or even 3.5</li>
<li>\\(h\\) could be someone's height (like 150 cm)</li>
<li>\\(c\\) could be the cost of something (like $25)</li>
<li>\\(n\\) could be the number of items</li>
</ul>

<h4>Variables vs. Numbers</h4>
<table style='border-collapse: collapse; width: 100%;'>
<tr style=';'>
<td style='padding: 10px;'><strong>Number</strong></td>
<td style='padding: 10px;'><strong>Variable</strong></td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>5 is always 5</td>
<td style='padding: 10px;'>\\(x\\) can be 1, 5, 100, etc.</td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>Numbers are fixed</td>
<td style='padding: 10px;'>Variables can change</td>
</tr>
<tr>
<td style='padding: 10px;'>We know what it is</td>
<td style='padding: 10px;'>We're trying to figure it out</td>
</tr>
</table>
"""
    },
    {
        "title": "Algebraic Expressions",
        "body": """
<h4>What is an Expression?</h4>
<p>An <strong>expression</strong> is a combination of numbers, variables, and operations (like \\(+, -, \\times, \\div\\)).</p>

<div class='worked-example'>
<h4>Examples of Expressions:</h4>
<ul>
<li>\\(x + 5\\) (variable + number)</li>
<li>\\(3x\\) (number × variable)</li>
<li>\\(2x + 7\\) (variable and number operations combined)</li>
<li>\\(a + b\\) (two variables)</li>
<li>\\(4n - 3\\) (variable, number, and operations)</li>
</ul>
</div>

<h4>NOT Expressions (These are Equations):</h4>
<ul>
<li>\\(x + 5 = 12\\) ← has an equals sign, so it's an equation, not just an expression</li>
<li>\\(3x = 21\\) ← has an equals sign</li>
</ul>

<h4>Key Difference:</h4>
<ul>
<li><strong>Expression:</strong> A mathematical phrase (no equals sign). Example: \\(2x + 5\\)</li>
<li><strong>Equation:</strong> A complete sentence with an equals sign. Example: \\(2x + 5 = 17\\)</li>
</ul>
"""
    },
    {
        "title": "Translating Words to Expressions",
        "body": """
<h4>How to Convert English to Algebra</h4>
<p>When you see a word problem, convert it step-by-step into an algebraic expression.</p>

<div class='concept-box'>
<h4>Translation Guide:</h4>
<table style='border-collapse: collapse; width: 100%;'>
<tr style=';'>
<td style='padding: 10px;'><strong>English</strong></td>
<td style='padding: 10px;'><strong>Algebra</strong></td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>a number</td>
<td style='padding: 10px;'>\\(x\\)</td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>increased by 7 / 7 more than</td>
<td style='padding: 10px;'>\\(x + 7\\)</td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>decreased by 3 / 3 less than</td>
<td style='padding: 10px;'>\\(x - 3\\)</td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>twice a number / double</td>
<td style='padding: 10px;'>\\(2x\\)</td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>half a number</td>
<td style='padding: 10px;'>\\(\\frac{x}{2}\\) or \\(0.5x\\)</td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>triple / 3 times a number</td>
<td style='padding: 10px;'>\\(3x\\)</td>
</tr>
<tr>
<td style='padding: 10px;'>5 more than twice a number</td>
<td style='padding: 10px;'>\\(2x + 5\\)</td>
</tr>
</table>
</div>

<h4>Examples:</h4>
<ul>
<li>"A number increased by 7" → \\(x + 7\\)</li>
<li>"A number decreased by 3" → \\(x - 3\\)</li>
<li>"Twice a number" → \\(2x\\)</li>
<li>"Half a number" → \\(\\frac{x}{2}\\)</li>
<li>"5 more than twice a number" → \\(2x + 5\\)</li>
<li>"10 less than three times a number" → \\(3x - 10\\)</li>
<li>"A number divided by 4" → \\(\\frac{x}{4}\\)</li>
</ul>
"""
    },
    {
        "title": "Like Terms and Simplifying",
        "body": """
<h4>What are Like Terms?</h4>
<p><strong>Like terms</strong> are terms that have the same variable (or no variable).</p>

<div class='concept-box'>
<h4>Like Terms Examples:</h4>
<ul>
<li>\\(3x\\) and \\(5x\\) ← both have \\(x\\)</li>
<li>\\(2a\\) and \\(a\\) ← both have \\(a\\)</li>
<li>\\(4\\) and \\(7\\) ← both are just numbers</li>
<li>\\(3xy\\) and \\(2xy\\) ← both have \\(xy\\)</li>
</ul>

<h4>NOT Like Terms:</h4>
<ul>
<li>\\(3x\\) and \\(5y\\) ← different variables</li>
<li>\\(2x\\) and \\(2x^2\\) ← different powers of x</li>
<li>\\(5a\\) and \\(5\\) ← one has \\(a\\), one doesn't</li>
</ul>
</div>

<h4>Simplifying by Combining Like Terms</h4>
<p>We add or subtract like terms to make the expression simpler.</p>

<div class='worked-example'>
<h4>Example 1: Simplify \\(3x + 2x\\)</h4>
<ul>
<li>Both terms have \\(x\\)</li>
<li>\\(3x + 2x = (3 + 2)x = 5x\\)</li>
<li>Answer: \\(5x\\)</li>
</ul>

<h4>Example 2: Simplify \\(4x + 3 + 2x + 5\\)</h4>
<ul>
<li>Combine \\(x\\) terms: \\(4x + 2x = 6x\\)</li>
<li>Combine number terms: \\(3 + 5 = 8\\)</li>
<li>Answer: \\(6x + 8\\)</li>
</ul>

<h4>Example 3: Simplify \\(3a + 2b + 5a\\)</h4>
<ul>
<li>\\(a\\) terms: \\(3a + 5a = 8a\\)</li>
<li>\\(b\\) term stays alone: \\(2b\\)</li>
<li>Answer: \\(8a + 2b\\)</li>
</ul>
</div>
"""
    },
    {
        "title": "Building and Evaluating Expressions",
        "body": """
<h4>What Does it Mean to Evaluate an Expression?</h4>
<p><strong>Evaluate</strong> means: find the value of an expression by replacing the variable with a number.</p>

<div class='worked-example'>
<h4>Example: Evaluate \\(2x + 5\\) when \\(x = 3\\)</h4>
<ul>
<li>Start with: \\(2x + 5\\)</li>
<li>Replace \\(x\\) with \\(3\\): \\(2(3) + 5\\)</li>
<li>Multiply: \\(6 + 5\\)</li>
<li>Add: \\(11\\)</li>
<li>Answer: \\(11\\)</li>
</ul>

<h4>Example: Evaluate \\(3a + 2b\\) when \\(a = 4\\) and \\(b = 5\\)</h4>
<ul>
<li>Replace \\(a\\) with \\(4\\) and \\(b\\) with \\(5\\): \\(3(4) + 2(5)\\)</li>
<li>Calculate: \\(12 + 10\\)</li>
<li>Answer: \\(22\\)</li>
</ul>
</div>

<h4>Why Is This Useful?</h4>
<p>Evaluating lets us find actual answers to real-world problems!</p>
<ul>
<li>If cost = \\(5n + 2\\) (where \\(n\\) = number of items), and you buy 7 items, the cost is \\(5(7) + 2 = 37\\)</li>
<li>If height = \\(12x\\) (where \\(x\\) = the side length), and \\(x = 3\\), then height = \\(12(3) = 36\\)</li>
</ul>
"""
    }
]
