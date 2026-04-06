TITLE = "What is Algebra?"

SECTIONS = [
    {
        "title": "From Arithmetic to Algebra",
        "body": """
<div class='concept-box'>
<h3>The Big Idea</h3>
<p>In <strong>arithmetic</strong>, you always know the numbers: 3 + 5 = 8.</p>
<p>But what if someone says: <em>"I'm thinking of a number, and when I add 5, I get 8"?</em></p>
<p>The unknown number is what <strong>algebra</strong> is about. We use a LETTER (like \\(x\\)) to stand for the number we don't know yet, then figure it out using logic.</p>
</div>

<h4>Compare:</h4>
<table style='border-collapse: collapse; width: 100%;'>
<tr style=';'>
<td style='padding: 10px;'><strong>Arithmetic</strong></td>
<td style='padding: 10px;'><strong>Algebra</strong></td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>3 + 5 = 8</td>
<td style='padding: 10px;'>\\(x\\) + 5 = 8</td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>Known numbers only</td>
<td style='padding: 10px;'>Unknown number (variable) + known numbers</td>
</tr>
<tr>
<td style='padding: 10px;'>We calculate the answer</td>
<td style='padding: 10px;'>We find what the unknown is</td>
</tr>
</table>

<h4>So what is Algebra?</h4>
<p><strong>Algebra</strong> is the part of mathematics where we use <strong>letters (called variables)</strong> to represent unknown numbers or quantities.</p>
"""
    },
    {
        "title": "Why Do We Need Algebra?",
        "body": """
<div class='success-box'>
<h4>Five Great Reasons:</h4>
<ul>
<li><strong>Solve mysteries:</strong> Find unknowns hidden in word problems</li>
<li><strong>Write rules:</strong> Write general patterns that work for any number (like "if side = s, then perimeter = 4s")</li>
<li><strong>Be organized:</strong> Make problem-solving systematic and clear</li>
<li><strong>Handle relationships:</strong> Show how one quantity depends on another</li>
<li><strong>Think like a scientist:</strong> Use variables to model real-world problems</li>
</ul>
</div>

<h4>Real-World Examples:</h4>
<ul>
<li><strong>Video games:</strong> Your score changes based on actions → \(\text{score} = 10 \times \text{kills} - 5 \times \text{deaths}\)</li>
<li><strong>Money:</strong> Pocket money after spending → money_left = starting_amount - amount_spent</li>
<li><strong>Cooking:</strong> A recipe scales up → If 1 batch needs 2 cups flour, then \\(b\\) batches need \\(2b\\) cups</li>
<li><strong>Distance:</strong> How far you travel → distance = speed × time, or \\(d = st\\)</li>
</ul>
"""
    },
    {
        "title": "Letters as Unknowns",
        "body": """
<h4>What is a Variable?</h4>
<p>A <strong>variable</strong> is a letter that stands for a number we don't know (yet). Common variables:</p>
<ul>
<li><strong>x, y, z</strong> — used for any unknown</li>
<li><strong>a, b, c</strong> — often for constants (fixed values)</li>
<li><strong>n</strong> — often for a count or sequence position</li>
<li><strong>s, d, t</strong> — often for specific quantities (side, distance, time)</li>
</ul>

<div class='concept-box'>
<h4>Example:</h4>
<p>"I'm thinking of a number. When I add 5, I get 12."</p>
<p>In algebra: <strong>\\(x\\) + 5 = 12</strong></p>
<p>\\(x\\) is the variable. It stands for the unknown number. Our job is to figure out that \\(x = 7\\).</p>
</div>

<h4>The Variable is NOT a Specific Letter</h4>
<p>We can use any letter we want! These all mean the same thing:</p>
<ul>
<li>\\(x + 5 = 12\\)</li>
<li>\\(n + 5 = 12\\)</li>
<li>\\(a + 5 = 12\\)</li>
</ul>
<p>Usually \\(x\\) is most common, but the letter itself doesn't matter. The letter just holds a place for the unknown.</p>
"""
    },
    {
        "title": "Reading Algebraic Statements",
        "body": """
<h4>How to Say Algebra Out Loud</h4>
<p>Algebraic statements are just a shorthand for English sentences:</p>

<table style='border-collapse: collapse; width: 100%;'>
<tr style=';'>
<td style='padding: 10px;'><strong>Symbol</strong></td>
<td style='padding: 10px;'><strong>What It Means (Read Aloud)</strong></td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>\\(x + 5\\)</td>
<td style='padding: 10px;'>"x plus 5" or "5 more than x"</td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>\\(x - 3\\)</td>
<td style='padding: 10px;'>"x minus 3" or "3 less than x"</td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>\\(2x\\)</td>
<td style='padding: 10px;'>"2 times x" or "twice x" or "double x"</td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>\\(\\frac{x}{4}\\)</td>
<td style='padding: 10px;'>"x divided by 4" or "a quarter of x"</td>
</tr>
<tr style=';'>
<td style='padding: 10px;'>\\(3x + 2\\)</td>
<td style='padding: 10px;'>"3x plus 2" or "2 more than 3x"</td>
</tr>
<tr>
<td style='padding: 10px;'>\\(x = 7\\)</td>
<td style='padding: 10px;'>"x equals 7" (the unknown is 7)</td>
</tr>
</table>

<div class='worked-example'>
<h4>Practice Reading:</h4>
<ul>
<li>\\(x + y\\) → "x plus y" or "the sum of x and y"</li>
<li>\\(2a - 5\\) → "2a minus 5" or "5 less than twice a"</li>
<li>\\(4n + 1\\) → "4n plus 1" or "one more than four times n"</li>
</ul>
</div>
"""
    },
    {
        "title": "Your First Algebraic Mystery",
        "body": """
<div class='success-box'>
<h4>Solve This!</h4>
<p>Someone thinks of a number, multiplies it by 2, and adds 3. The answer is 15.</p>
<p>What number did they think of?</p>
</div>

<h4>In Algebra:</h4>
<p>If the unknown number is \\(x\\), then:</p>
<ul>
<li>Multiply by 2: \\(2x\\)</li>
<li>Add 3: \\(2x + 3\\)</li>
<li>The result is 15: \\(2x + 3 = 15\\)</li>
</ul>

<h4>Can You Figure Out \\(x\\)?</h4>
<p>Think about it:</p>
<ul>
<li>If \\(2x + 3 = 15\\), then \\(2x = 15 - 3 = 12\\)</li>
<li>If \\(2x = 12\\), then \\(x = 12 \div 2 = 6\\)</li>
</ul>

<div class='success-box'>
<h4>Answer: \\(x = 6\\)</h4>
<p>Check: If we start with 6, multiply by 2 (= 12), then add 3 (= 15). ✓</p>
</div>

<p><strong>Congratulations!</strong> You just solved your first algebraic equation. In this module, you'll learn all the tricks to solve problems like this systematically.</p>
"""
    }
]
