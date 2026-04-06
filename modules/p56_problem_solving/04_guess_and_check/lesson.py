TITLE = "Guess and Check - Trial and Refinement"

SECTIONS = [
    {
        "title": "What is Guess and Check?",
        "body": """
<div class="concept-box">
<h3>The Strategy</h3>

<p><strong>Guess and Check</strong> is a problem-solving method where you:</p>

<ol>
<li>Make a reasonable guess for the unknown</li>
<li>Check if it satisfies all conditions in the problem</li>
<li>If wrong, use the result to make a better guess</li>
<li>Repeat until you find the correct answer</li>
</ol>

<h3>This Isn't Random Guessing!</h3>

<p>Guess and Check is <strong>smart guessing</strong>. You use information from each guess to guide the next one. It's like detective work — each attempt gives you a clue.</p>
</div>

<div class="warning-box">
<h3>Important Distinction</h3>

<p><strong>❌ Random Guessing:</strong> "Let me try 5... nope. Try 7... nope. Try 13..."</p>

<p><strong>✓ Smart Checking:</strong> "My guess was too small. Numbers must be bigger. Let me try higher values."</p>
</div>

<div class="worked-example">
<h4>Simple Example</h4>

<p><strong>Problem:</strong> "A number is doubled, then 3 is subtracted, giving 11. What is the number?"</p>

<p><strong>Guess and Check:</strong></p>

<table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
<tr >
<th style="padding: 10px; text-align: center;">Guess</th>
<th style="padding: 10px; text-align: center;">Double It</th>
<th style="padding: 10px; text-align: center;">Subtract 3</th>
<th style="padding: 10px; text-align: center;">Result</th>
<th style="padding: 10px; text-align: center;">Check</th>
</tr>
<tr>
<td style="padding: 10px; text-align: center;">5</td>
<td style="padding: 10px; text-align: center;">10</td>
<td style="padding: 10px; text-align: center;">7</td>
<td style="padding: 10px; text-align: center;">7</td>
<td style="padding: 10px; text-align: center;">Too small</td>
</tr>
<tr >
<td style="padding: 10px; text-align: center;">7</td>
<td style="padding: 10px; text-align: center;">14</td>
<td style="padding: 10px; text-align: center;">11</td>
<td style="padding: 10px; text-align: center;">11</td>
<td style="padding: 10px; text-align: center;">✓ CORRECT!</td>
</tr>
</table>

<p><strong>Answer:</strong> The number is 7.</p>

<p>Notice: After the first guess (5) gave too small a result, we increased to 7 and found the answer!</p>
</div>
"""
    },
    {
        "title": "Building Check Tables",
        "body": """
<div class="concept-box">
<h3>Organize Your Guesses</h3>

<p>Always make a table to organize your guesses. This helps you:</p>

<ul>
<li>Keep track of what you tried</li>
<li>See a pattern in the results</li>
<li>Know where to guess next</li>
<li>Avoid repeating the same guess</li>
</ul>
</div>

<div class="worked-example">
<h4>Problem with Two Unknowns</h4>

<p><strong>Problem:</strong> "Two numbers add up to 12 and their product is 35. Find the numbers."</p>

<p><strong>Setup:</strong> Let's call the numbers a and b.
<ul>
<li>Condition 1: \(a + b = 12\)</li>
<li>Condition 2: \(a \times b = 35\)</li>
</ul>

<p><strong>Check Table:</strong></p>

<table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
<tr >
<th style="padding: 10px; text-align: center;">Guess a</th>
<th style="padding: 10px; text-align: center;">Then b</th>
<th style="padding: 10px; text-align: center;">Sum (a+b)</th>
<th style="padding: 10px; text-align: center;">Product (a×b)</th>
<th style="padding: 10px; text-align: center;">Check</th>
</tr>
<tr>
<td style="padding: 10px; text-align: center;">3</td>
<td style="padding: 10px; text-align: center;">9</td>
<td style="padding: 10px; text-align: center;">12 ✓</td>
<td style="padding: 10px; text-align: center;">27 ✗</td>
<td style="padding: 10px; text-align: center;">Product too small</td>
</tr>
<tr >
<td style="padding: 10px; text-align: center;">4</td>
<td style="padding: 10px; text-align: center;">8</td>
<td style="padding: 10px; text-align: center;">12 ✓</td>
<td style="padding: 10px; text-align: center;">32 ✗</td>
<td style="padding: 10px; text-align: center;">Product too small</td>
</tr>
<tr>
<td style="padding: 10px; text-align: center;">5</td>
<td style="padding: 10px; text-align: center;">7</td>
<td style="padding: 10px; text-align: center;">12 ✓</td>
<td style="padding: 10px; text-align: center;">35 ✓</td>
<td style="padding: 10px; text-align: center;">CORRECT!</td>
</tr>
</table>

<p><strong>Answer:</strong> The numbers are 5 and 7.</p>

<p><strong>Why the table works:</strong> As we tried 3, 4, 5..., we could see the product increasing. When product reached 35 at a=5, b=7, we had the answer!</p>
</div>

<div class="success-box">
<h3>Smart Strategies for Guessing</h3>

<ul>
<li><strong>Use a reasonable starting range.</strong> If adding two numbers to get 12, try numbers between 1 and 11.</li>
<li><strong>Start with easy numbers.</strong> Try 5 (middle), not random numbers.</li>
<li><strong>Learn from each guess.</strong> "Product was too small, so I need bigger numbers."</li>
<li><strong>Narrow down systematically.</strong> Use patterns in your table to guide next guesses.</li>
<li><strong>Don't jump around randomly.</strong> Make educated moves based on previous results.</li>
</ul>
</div>
"""
    },
    {
        "title": "Multi-Condition Problems",
        "body": """
<div class="concept-box">
<h3>Checking Multiple Conditions</h3>

<p>Some problems have MORE THAN ONE condition that must ALL be satisfied. Your guess must pass EVERY check.</p>
</div>

<div class="worked-example">
<h4>Example: Age Problem with Two Conditions</h4>

<p><strong>Problem:</strong> "Maria is twice as old as her brother. Together they are 21 years old. How old is each?"</p>

<p><strong>Conditions:</strong></p>
<ul>
<li>Maria's age = \(2 \times\) brother's age</li>
<li>Maria's age + brother's age \(= 21\)</li>
</ul>

<p><strong>Check Table:</strong></p>

<table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
<tr >
<th style="padding: 10px; text-align: center;">Brother</th>
<th style="padding: 10px; text-align: center;">Maria (2×)</th>
<th style="padding: 10px; text-align: center;">Sum</th>
<th style="padding: 10px; text-align: center;">Check Sum</th>
<th style="padding: 10px; text-align: center;">All OK?</th>
</tr>
<tr>
<td style="padding: 10px; text-align: center;">5</td>
<td style="padding: 10px; text-align: center;">10</td>
<td style="padding: 10px; text-align: center;">15</td>
<td style="padding: 10px; text-align: center;">✗</td>
<td style="padding: 10px; text-align: center;">Too small</td>
</tr>
<tr >
<td style="padding: 10px; text-align: center;">7</td>
<td style="padding: 10px; text-align: center;">14</td>
<td style="padding: 10px; text-align: center;">21</td>
<td style="padding: 10px; text-align: center;">✓</td>
<td style="padding: 10px; text-align: center;">PERFECT!</td>
</tr>
</table>

<p><strong>Answer:</strong> Brother is 7, Maria is 14.</p>
</div>

<div class="worked-example">
<h4>Example: Money Problem with Three Conditions</h4>

<p><strong>Problem:</strong> "Pens cost 2 dollars each. Notebooks cost 5 dollars each. I buy 10 items for 35 dollars total. How many of each?"</p>

<p><strong>Conditions:</strong></p>
<ul>
<li>Pens + Notebooks \(= 10\) items</li>
<li>\(2 \times\) Pens \(+ 5 \times\) Notebooks \(= 35\) dollars</li>
</ul>

<p><strong>Check Table:</strong></p>

<table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
<tr >
<th style="padding: 10px; text-align: center;">Pens</th>
<th style="padding: 10px; text-align: center;">Notebooks</th>
<th style="padding: 10px; text-align: center;">Total Items</th>
<th style="padding: 10px; text-align: center;">Total Cost</th>
<th style="padding: 10px; text-align: center;">Both OK?</th>
</tr>
<tr>
<td style="padding: 10px; text-align: center;">5</td>
<td style="padding: 10px; text-align: center;">5</td>
<td style="padding: 10px; text-align: center;">10 ✓</td>
<td style="padding: 10px; text-align: center;">35 ✓</td>
<td style="padding: 10px; text-align: center;">CORRECT!</td>
</tr>
</table>

<p><strong>Answer:</strong> 5 pens and 5 notebooks.</p>

<p>Lucky guess! But often you need multiple tries. The key is checking ALL conditions.</p>
</div>
"""
    },
    {
        "title": "Guess and Check vs. Other Strategies",
        "body": """
<div class="concept-box">
<h3>When to Use Guess and Check</h3>

<p><strong>Best for:</strong></p>
<ul>
<li>Small numbers (checking is quick)</li>
<li>Problems with limited possibilities</li>
<li>When other strategies don't work easily</li>
<li>To verify answers from other methods</li>
</ul>

<p><strong>Avoid when:</strong></p>
<ul>
<li>Numbers are very large (takes forever)</li>
<li>You don't have a good starting range</li>
<li>Other strategies (bar model, working backward) are clearly better</li>
</ul>
</div>

<div class="success-box">
<h3>Smart Guessing Tips</h3>

<ol>
<li><strong>Know your range.</strong> What are reasonable values? If buying items that cost 2-5 dollars each with 30 dollars, can't need more than 15 items.</li>
<li><strong>Start in the middle.</strong> If range is 1-10, try 5 first. Then 7 or 3 based on results.</li>
<li><strong>Notice patterns.</strong> As you increase your guess, does the result increase or decrease?</li>
<li><strong>Use the pattern to jump faster.</strong> If the result increases by 3 each step, and you need to increase by 6 total, jump by 2 next time.</li>
<li><strong>Document everything.</strong> Table keeps you organized and shows your thinking.</li>
</ol>
</div>

<div class="worked-example">
<h4>Comparing Strategies</h4>

<p><strong>Problem:</strong> "I think of a number, multiply by 3, add 7. I get 28. What's the number?"</p>

<p><strong>Method 1: Working Backwards (Best)</strong></p>
<ul>
<li>\(28 - 7 = 21\)</li>
<li>\(21 \div 3 = 7\)</li>
<li>Answer: 7 (one step!)</li>
</ul>

<p><strong>Method 2: Guess and Check (Slower)</strong></p>
<ul>
<li>Guess 5: \(5 \times 3 + 7 = 22\) (too small)</li>
<li>Guess 8: \(8 \times 3 + 7 = 31\) (too big)</li>
<li>Guess 7: \(7 \times 3 + 7 = 28\) (correct!)</li>
<li>Answer: 7 (three guesses)</li>
</ul>

<p><strong>Lesson:</strong> Different strategies work, but working backwards is faster here!</p>
</div>

<div class="warning-box">
<h3>Be Efficient</h3>

<p>Guess and Check is a tool, not your only tool. Ask yourself:</p>

<ul>
<li>Could I draw a bar model? (Maybe faster)</li>
<li>Could I work backwards? (Often faster)</li>
<li>Is this a comparison? (Bar model is better)</li>
<li>Are the numbers small? (Guess and Check is fine)</li>
</ul>

<p><strong>Be a SMART problem solver, not just a guesser!</strong></p>
</div>
"""
    }
]
