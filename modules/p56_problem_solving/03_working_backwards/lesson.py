TITLE = "Working Backwards - Reverse Operations Strategy"

SECTIONS = [
    {
        "title": "What is Working Backwards?",
        "body": """
<div class="concept-box">
<h3>The Core Idea</h3>

<p><strong>Working backwards</strong> means starting from the END (the final answer) and using OPPOSITE operations to work back to the BEGINNING.</p>

<p>It's like rewinding a video. If you see the final scene, can you figure out how it started?</p>

<h3>Why Does It Work?</h3>

<p>Every math operation has an opposite:</p>

<table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
<tr >
<th style="padding: 10px; text-align: left">Operation</th>
<th style="padding: 10px; text-align: left">Opposite (Inverse)</th>
</tr>
<tr>
<td style="padding: 10px;">Add</td>
<td style="padding: 10px;">Subtract</td>
</tr>
<tr >
<td style="padding: 10px;">Subtract</td>
<td style="padding: 10px;">Add</td>
</tr>
<tr>
<td style="padding: 10px;">Multiply</td>
<td style="padding: 10px;">Divide</td>
</tr>
<tr >
<td style="padding: 10px;">Divide</td>
<td style="padding: 10px;">Multiply</td>
</tr>
</table>

<p>If going forward you ADD 5, going backward you SUBTRACT 5.</p>
</div>

<div class="worked-example">
<h4>Simple Example: One Step</h4>

<p><strong>Problem:</strong> "I think of a number, add 8, and get 15. What was my number?"</p>

<p><strong>Forward journey (what the problem did):</strong></p>
<p class="formula-box">
? &nbsp;&nbsp;<strong>+ 8</strong>&nbsp;&nbsp; = &nbsp;&nbsp;15
</p>

<p><strong>Backward journey (working backwards):</strong></p>
<p class="formula-box">
15 &nbsp;&nbsp;<strong>- 8</strong>&nbsp;&nbsp; = &nbsp;&nbsp;7
</p>

<p><strong>Answer:</strong> The number was 7.</p>

<p><strong>Check:</strong> 7 + 8 = 15 ✓</p>
</div>
"""
    },
    {
        "title": "Multi-Step Working Backwards",
        "body": """
<div class="concept-box">
<h3>When Multiple Operations Happen</h3>

<p>If several operations happen one after another, work backwards through EACH ONE in REVERSE ORDER.</p>

<p><strong>Golden Rule:</strong> The last operation you undo is the FIRST operation that happened. Work backwards in reverse order!</p>
</div>

<div class="worked-example">
<h4>Example: Three Operations</h4>

<p><strong>Problem:</strong> "Sarah started with some money. She spent 10 dollars on lunch, then earned 25 dollars from babysitting, and finally had 85 dollars. How much did she start with?"</p>

<p><strong>Forward (what happened):</strong></p>

<svg width="100%" height="90" viewBox="0 0 530 90" xmlns="http://www.w3.org/2000/svg" style="border-radius: 4px">
  <defs>
    <marker id="fwd-arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill='currentColor'/>
    </marker>
  </defs>

  <rect x="15" y="20" width="90" height="44" fill='none' stroke='#58a6ff' stroke-width="2" rx='4'/>
  <text x="60" y="47" font-size='12' fill='currentColor' text-anchor='middle' font-family='sans-serif'>Start: ?</text>

  <text x="130" y="35" font-size='11' fill='#79c0ff' text-anchor='middle' font-family='sans-serif'>-10</text>
  <line x1="105" y1="42" x2="135" y2="42" stroke='currentColor' stroke-width="2" marker-end="url(#fwd-arrow)"/>

  <rect x="140" y="20" width="90" height="44" fill='none' stroke='#a371f7' stroke-width="2" rx='4'/>
  <text x="185" y="47" font-size='12' fill='currentColor' text-anchor='middle' font-family='sans-serif'>After lunch</text>

  <text x="255" y="35" font-size='11' fill='#79c0ff' text-anchor='middle' font-family='sans-serif'>+25</text>
  <line x1="230" y1="42" x2="260" y2="42" stroke='currentColor' stroke-width="2" marker-end="url(#fwd-arrow)"/>

  <rect x="265" y="20" width="100" height="44" fill='none' stroke='#a371f7' stroke-width="2" rx='4'/>
  <text x="315" y="47" font-size='12' fill='currentColor' text-anchor='middle' font-family='sans-serif'>After babysit</text>

  <line x1="365" y1="42" x2="395" y2="42" stroke='currentColor' stroke-width="2" marker-end="url(#fwd-arrow)"/>

  <rect x="400" y="20" width="90" height="44" fill='none' stroke='#3fb950' stroke-width="2" rx='4'/>
  <text x="445" y="47" font-size='12' fill='currentColor' text-anchor='middle' font-family='sans-serif'>Final: 85</text>
</svg>

<p><strong>Backward (working backwards from 85):</strong></p>

<svg width="100%" height="90" viewBox="0 0 530 90" xmlns="http://www.w3.org/2000/svg" style="border-radius: 4px">
  <defs>
    <marker id="bk-arrow" markerWidth="10" markerHeight="10" refX="2" refY="3" orient="auto">
      <polygon points="10 0, 0 3, 10 6" fill='currentColor'/>
    </marker>
  </defs>

  <rect x="400" y="20" width="90" height="44" fill='none' stroke='#3fb950' stroke-width="2" rx='4'/>
  <text x="445" y="47" font-size='12' fill='currentColor' text-anchor='middle' font-family='sans-serif'>Final: 85</text>

  <text x="380" y="35" font-size='11' fill='#79c0ff' text-anchor='middle' font-family='sans-serif'>-25</text>
  <line x1="395" y1="42" x2="365" y2="42" stroke='currentColor' stroke-width="2" marker-end="url(#bk-arrow)"/>

  <rect x="265" y="20" width="95" height="44" fill='none' stroke='#a371f7' stroke-width="2" rx='4'/>
  <text x="312" y="47" font-size='12' fill='currentColor' text-anchor='middle' font-family='sans-serif'>Before: 60</text>

  <text x="250" y="35" font-size='11' fill='#79c0ff' text-anchor='middle' font-family='sans-serif'>+10</text>
  <line x1="260" y1="42" x2="230" y2="42" stroke='currentColor' stroke-width="2" marker-end="url(#bk-arrow)"/>

  <rect x="140" y="20" width="85" height="44" fill='none' stroke='#a371f7' stroke-width="2" rx='4'/>
  <text x="182" y="47" font-size='12' fill='currentColor' text-anchor='middle' font-family='sans-serif'>Before: 70</text>

  <line x1="135" y1="42" x2="105" y2="42" stroke='currentColor' stroke-width="2" marker-end="url(#bk-arrow)"/>

  <rect x="15" y="20" width="85" height="44" fill='none' stroke='#58a6ff' stroke-width="2" rx='4'/>
  <text x="57" y="47" font-size='12' fill='currentColor' text-anchor='middle' font-family='sans-serif'>Start: 70</text>
</svg>

<p><strong>Step-by-step backward calculation:</strong></p>

<ol>
<li>Final amount: 85 dollars</li>
<li>Undo "earned 25" (subtract 25): \(85 - 25 = 60\)</li>
<li>Undo "spent 10" (add 10): \(60 + 10 = 70\)</li>
<li>Starting amount: 70 dollars</li>
</ol>

<p><strong>Check forward:</strong> \(70 - 10 = 60\), then \(60 + 25 = 85\) ✓</p>
</div>

<div class="worked-example">
<h4>Example with Multiplication and Division</h4>

<p><strong>Problem:</strong> "I think of a number, multiply it by 3, add 7, and get 28. What was the number?"</p>

<p><strong>Operations list:</strong></p>
<ul>
<li>First: multiply by 3</li>
<li>Second: add 7</li>
<li>Final result: 28</li>
</ul>

<p><strong>Working backward (reverse order, opposite operations):</strong></p>
<ul>
<li>Start with final: 28</li>
<li>Undo "add 7" (subtract 7): \(28 - 7 = 21\)</li>
<li>Undo "multiply by 3" (divide by 3): \(21 \div 3 = 7\)</li>
<li>Original number: 7</li>
</ul>

<p><strong>Check:</strong> \(7 \times 3 = 21\), then \(21 + 7 = 28\) ✓</p>
</div>
"""
    },
    {
        "title": "When to Use Working Backwards",
        "body": """
<div class="concept-box">
<h3>Perfect Problems for This Strategy</h3>

<p>Working backwards is BEST when:</p>

<ul>
<li>The final answer is clearly given</li>
<li>You know the sequence of operations</li>
<li>You need to find the starting value</li>
<li>Operations are straightforward (add, subtract, multiply, divide)</li>
</ul>

<p>Working backwards is WORST when:</p>

<ul>
<li>The final answer is NOT given</li>
<li>Operations are complicated or unclear</li>
<li>The sequence of events is mixed up</li>
<li>Multiple unknowns exist at the same time</li>
</ul>
</div>

<div class="success-box">
<h3>Real-World Examples</h3>

<p><strong>Example 1: Cooking</strong></p>
<ul>
<li>A recipe says "Final cake weighs 1200g. It weighed 800g before baking."</li>
<li>Working backward: How much did ingredients weigh? 1200 - 800 = 400g</li>
</ul>

<p><strong>Example 2: Money Problems</strong></p>
<ul>
<li>You end the day with 50 dollars. You spent 20, then earned 35, then spent 5.</li>
<li>Working backward to find starting amount!</li>
</ul>

<p><strong>Example 3: Age Problems</strong></p>
<ul>
<li>Ben's age now is 15. He will be 20 in 5 years. How old was he 3 years ago?</li>
<li>Working backward from 15: subtract 3 = 12 years old</li>
</ul>
</div>
"""
    },
    {
        "title": "Practice and Common Mistakes",
        "body": """
<div class="warning-box">
<h3>Common Mistakes</h3>

<p><strong>Mistake 1: Wrong Order</strong></p>
<ul>
<li>❌ Going backward but using wrong operation order</li>
<li>✓ Always start from the LAST operation that happened</li>
</ul>

<p><strong>Mistake 2: Wrong Opposite</strong></p>
<ul>
<li>❌ Forgetting that subtract is opposite of add</li>
<li>✓ Always use: add ↔ subtract, multiply ↔ divide</li>
</ul>

<p><strong>Mistake 3: Forgetting to Check</strong></p>
<ul>
<li>❌ Finding an answer and stopping</li>
<li>✓ ALWAYS verify by working forward from your answer</li>
</ul>

<p><strong>Mistake 4: Rushing Through Steps</strong></p>
<ul>
<li>❌ Combining operations and getting confused</li>
<li>✓ Do one step at a time, clearly labeled</li>
</ul>
</div>

<div class="success-box">
<h3>How to Avoid Mistakes</h3>

<ol>
<li>List all operations in order (like a checklist)</li>
<li>Start from the FINAL amount</li>
<li>Work down the list from BOTTOM to TOP</li>
<li>Apply the opposite operation to each one</li>
<li>Show your work: "85 - 25 = 60, then 60 + 10 = 70"</li>
<li>Check by working forward from your answer</li>
</ol>
</div>

<div class="worked-example">
<h4>Complete Worked Example with Full Checking</h4>

<p><strong>Problem:</strong> "A number is doubled, then 10 is added. The result is 50. What was the original number?"</p>

<p><strong>Understand:</strong>
<ul>
<li>Unknown starting number</li>
<li>Operation 1: Double it (multiply by 2)</li>
<li>Operation 2: Add 10</li>
<li>Final result: 50</li>
</ul>

<p><strong>Plan:</strong> Work backwards from 50</p>

<p><strong>Execute:</strong>
<ul>
<li>Start with result: 50</li>
<li>Undo add 10 (subtract): \(50 - 10 = 40\)</li>
<li>Undo double (divide by 2): \(40 \div 2 = 20\)</li>
<li>Original number: 20</li>
</ul>

<p><strong>Check:</strong>
<ul>
<li>Start with 20</li>
<li>Double: \(20 \times 2 = 40\)</li>
<li>Add 10: \(40 + 10 = 50\) ✓ CORRECT!</li>
</ul>
</div>
"""
    }
]
