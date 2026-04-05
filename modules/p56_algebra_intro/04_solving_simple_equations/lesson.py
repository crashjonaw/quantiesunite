TITLE = "Solving Simple Equations"

SECTIONS = [
    {
        "title": "Inverse Operations",
        "body": """
<h4>The Golden Rule of Algebra</h4>
<p>To undo an operation, use its opposite (inverse).</p>

<table style='border-collapse: collapse; width: 100%;'>
<tr style=';'>
<td style='padding: 10px;'><strong>Operation</strong></td>
<td style='padding: 10px;'><strong>Inverse Operation</strong></td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>Addition (\\(+\\))</td>
<td style='padding: 10px;'>Subtraction (\\(-\\))</td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>Subtraction (\\(-\\))</td>
<td style='padding: 10px;'>Addition (\\(+\\))</td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>Multiplication (\\(\\times\\))</td>
<td style='padding: 10px;'>Division (\\(\\div\\))</td>
</tr>
<tr>
<td style='padding: 10px;'>Division (\\(\\div\\))</td>
<td style='padding: 10px;'>Multiplication (\\(\\times\\))</td>
</tr>
</table>

<div class='concept-box'>
<h4>Example: If I add 5, then subtract 5</h4>
<p>Start with 10 → add 5 (= 15) → subtract 5 (= 10) ← back to start!</p>
<p>Subtraction undoes addition.</p>
</div>

<h4>Why This Matters for Algebra:</h4>
<p>We use inverse operations to isolate the variable (get \\(x\\) by itself on one side).</p>
"""
    },
    {
        "title": "One-Step Equations: Addition and Subtraction",
        "body": """
<h4>Type 1: \\(x + a = b\\)</h4>

<div class='worked-example'>
<h4>Solve: \\(x + 5 = 12\\)</h4>
<ul>
<li><strong>What's done to x?</strong> We add 5</li>
<li><strong>Undo it:</strong> Subtract 5 from both sides</li>
<li>\\(x + 5 - 5 = 12 - 5\\)</li>
<li>\\(x = 7\\)</li>
<li><strong>Check:</strong> \\(7 + 5 = 12\\) ✓</li>
</ul>
</div>

<h4>Type 2: \\(x - a = b\\)</h4>

<div class='worked-example'>
<h4>Solve: \\(x - 3 = 8\\)</h4>
<ul>
<li><strong>What's done to x?</strong> We subtract 3</li>
<li><strong>Undo it:</strong> Add 3 to both sides</li>
<li>\\(x - 3 + 3 = 8 + 3\\)</li>
<li>\\(x = 11\\)</li>
<li><strong>Check:</strong> \\(11 - 3 = 8\\) ✓</li>
</ul>
</div>

<h4>The Balance Scale Idea</h4>
<p>Whatever you do to one side, you must do to the other side to keep it balanced:</p>
<p style='text-align: center; font-family: monospace; background: #f9f9f9; padding: 10px;'>Left = Right<br>If Left - 5, then Right - 5<br>Still equal!</p>
"""
    },
    {
        "title": "One-Step Equations: Multiplication and Division",
        "body": """
<h4>Type 3: \\(ax = b\\)</h4>

<div class='worked-example'>
<h4>Solve: \\(2x = 10\\)</h4>
<ul>
<li><strong>What's done to x?</strong> Multiply by 2</li>
<li><strong>Undo it:</strong> Divide both sides by 2</li>
<li>\\(\\frac{2x}{2} = \\frac{10}{2}\\)</li>
<li>\\(x = 5\\)</li>
<li><strong>Check:</strong> \\(2 \\times 5 = 10\\) ✓</li>
</ul>
</div>

<h4>More Examples:</h4>
<ul>
<li>\\(3x = 15\\) → divide by 3 → \\(x = 5\\)</li>
<li>\\(4x = 20\\) → divide by 4 → \\(x = 5\\)</li>
<li>\\(5x = 30\\) → divide by 5 → \\(x = 6\\)</li>
</ul>

<h4>Type 4: \\(\\frac{x}{a} = b\\)</h4>

<div class='worked-example'>
<h4>Solve: \\(\\frac{x}{3} = 4\\)</h4>
<ul>
<li><strong>What's done to x?</strong> Divide by 3</li>
<li><strong>Undo it:</strong> Multiply both sides by 3</li>
<li>\\(\\frac{x}{3} \\times 3 = 4 \\times 3\\)</li>
<li>\\(x = 12\\)</li>
<li><strong>Check:</strong> \\(\\frac{12}{3} = 4\\) ✓</li>
</ul>
</div>

<h4>More Examples:</h4>
<ul>
<li>\\(\\frac{x}{2} = 6\\) → multiply by 2 → \\(x = 12\\)</li>
<li>\\(\\frac{x}{5} = 3\\) → multiply by 5 → \\(x = 15\\)</li>
</ul>
"""
    },
    {
        "title": "Two-Step Equations",
        "body": """
<h4>The Strategy: Undo in Reverse Order</h4>
<p>When there are two operations, undo them in reverse order of BODMAS.</p>
<p>Remember BODMAS? In reverse: first undo addition/subtraction, then undo multiplication/division.</p>

<div class='worked-example'>
<h4>Solve: \\(2x + 3 = 11\\)</h4>
<ul>
<li><strong>Step 1:</strong> Undo the addition first → subtract 3 from both sides</li>
<li>\\(2x + 3 - 3 = 11 - 3\\)</li>
<li>\\(2x = 8\\)</li>
<li><strong>Step 2:</strong> Undo the multiplication → divide both sides by 2</li>
<li>\\(\\frac{2x}{2} = \\frac{8}{2}\\)</li>
<li>\\(x = 4\\)</li>
<li><strong>Check:</strong> \\((2 \\times 4) + 3 = 8 + 3 = 11\\) ✓</li>
</ul>
</div>

<div class='worked-example'>
<h4>Solve: \\(3x - 5 = 16\\)</h4>
<ul>
<li><strong>Step 1:</strong> Undo subtraction → add 5 to both sides</li>
<li>\\(3x - 5 + 5 = 16 + 5\\)</li>
<li>\\(3x = 21\\)</li>
<li><strong>Step 2:</strong> Undo multiplication → divide by 3</li>
<li>\\(x = \\frac{21}{3} = 7\\)</li>
<li><strong>Check:</strong> \\((3 \\times 7) - 5 = 21 - 5 = 16\\) ✓</li>
</ul>
</div>

<h4>More Examples:</h4>
<ul>
<li>\\(4x + 2 = 18\\) → subtract 2 (= 16) → divide by 4 (= 4)</li>
<li>\\(5x - 7 = 13\\) → add 7 (= 20) → divide by 5 (= 4)</li>
<li>\\(\\frac{x}{2} + 3 = 8\\) → subtract 3 (= 5) → multiply by 2 (= 10)</li>
</ul>
"""
    },
    {
        "title": "Always Check Your Answer!",
        "body": """
<h4>Checking: The Most Important Habit</h4>
<p>After you solve, plug your answer back into the original equation. If it works, you're correct!</p>

<div class='success-box'>
<h4>Why Check?</h4>
<ul>
<li>It catches simple mistakes</li>
<li>It confirms your answer is right</li>
<li>It builds confidence</li>
<li>Real mathematicians ALWAYS check!</li>
</ul>
</div>

<div class='worked-example'>
<h4>Example: Check \\(2x + 5 = 17\\) with \\(x = 6\\)</h4>
<ul>
<li>Original equation: \\(2x + 5 = 17\\)</li>
<li>Substitute \\(x = 6\\): \\(2(6) + 5 = ?\\)</li>
<li>Calculate: \\(12 + 5 = 17\\)</li>
<li>Does left = right? \\(17 = 17\\) ✓</li>
<li><strong>Correct!</strong></li>
</ul>
</div>

<div class='warning-box'>
<h4>If Check Fails:</h4>
<p>If the left and right sides don't match, you made an error. Go back and redo your steps:</p>
<ul>
<li>Did you perform the inverse operation correctly?</li>
<li>Did you apply it to both sides?</li>
<li>Did you do the arithmetic right?</li>
</ul>
</div>

<h4>Checking Multiple Answers (Word Problems)</h4>
<p>In word problems, also check that your answer makes sense:</p>
<ul>
<li>If finding a count of objects, is it a whole number?</li>
<li>If finding a distance, is it positive?</li>
<li>Does the answer match the original story?</li>
</ul>
"""
    }
]
