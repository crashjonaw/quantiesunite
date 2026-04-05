"""04. Comparing Numbers — Understanding greater than, less than, and equal to."""

TITLE = "Comparing Numbers: Bigger and Smaller"

SECTIONS = [
    {
        "title": "Why Compare Numbers?",
        "body": """<h3>A Real-World Question</h3>
<p>Imagine you have \\(5\\) apples and your friend has \\(8\\) apples. Who has more? Who has fewer?</p>

<p>In the real world, we constantly compare quantities:</p>
<ul>
  <li>Which toy set has more pieces?</li>
  <li>Who has more birthday candles?</li>
  <li>Which group has more players?</li>
  <li>Does this book have more pages than that book?</li>
</ul>

<p>Numbers let us answer these questions quickly and clearly!</p>

<h3>Three Ways to Compare</h3>

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin: 20px 0;">
  <div style="padding: 15px; border-radius: 8px; border-left: 4px solid #4caf50;">
    <p style="font-size: 18px; color: #2e7d32; margin: 0 0 5px 0; font-weight: bold;">Greater Than</p>
    <p style="font-size: 12px; margin: 0">(bigger, more)</p>
  </div>
  <div class="formula-box">
    <p style="font-size: 18px; color: #e65100; margin: 0 0 5px 0; font-weight: bold;">Less Than</p>
    <p style="font-size: 12px; margin: 0">(smaller, fewer)</p>
  </div>
  <div style="padding: 15px; border-radius: 8px; border-left: 4px solid #2196f3;">
    <p style="font-size: 18px; color: #1565c0; margin: 0 0 5px 0; font-weight: bold;">Equal To</p>
    <p style="font-size: 12px; margin: 0">(the same)</p>
  </div>
</div>

<h3>Visual Comparison: 3 vs. 7</h3>
<p>Let's compare 3 apples and 7 apples:</p>

<div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0; padding: 20px; border-radius: 8px">
  <div style="text-align: center;">
    <p style="font-size: 32px; margin: 0;">🍎🍎🍎</p>
    <p style="font-size: 20px; color: #4169E1; font-weight: bold; margin: 5px 0 0 0;">3</p>
  </div>
  <div style="text-align: center; font-size: 40px; color: #ff9800; font-weight: bold;">
    &lt;
  </div>
  <div style="text-align: center;">
    <p style="font-size: 32px; margin: 0;">🍎🍎🍎🍎🍎🍎🍎</p>
    <p style="font-size: 20px; color: #4169E1; font-weight: bold; margin: 5px 0 0 0;">7</p>
  </div>
</div>

<p style="text-align: center; font-size: 16px">We can see that 3 is <strong>less than</strong> 7 (or 7 is <strong>greater than</strong> 3)</p>

<div class="success-box">
  <h4>✓ What You Just Learned</h4>
  <p>When you line up objects and count them, you can easily see which group has more. \\(7\\) apples is more than \\(3\\) apples!</p>
</div>"""
    },

    {
        "title": "The Symbols: <, >, and =",
        "body": """<h3>Three Special Symbols</h3>
<p>Instead of writing out "less than," "greater than," and "equal to," we use symbols:</p>

<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
  <tr style="background: #4169E180;">
    <th style="padding: 12px; text-align: center">Symbol</th>
    <th style="padding: 12px;">Meaning</th>
    <th style="padding: 12px;">Example</th>
    <th style="padding: 12px;">Say It</th>
  </tr>
  <tr>
    <td style="padding: 12px; text-align: center; font-size: 24px; color: #ff9800"><strong>&lt;</strong></td>
    <td style="padding: 12px;">Less than (smaller)</td>
    <td style="padding: 12px;">\\(3 < 7\\)</td>
    <td style="padding: 12px;">"3 is less than 7"</td>
  </tr>
  <tr style="background: rgba(255,255,255,0.03);">
    <td style="padding: 12px; text-align: center; font-size: 24px; color: #4caf50"><strong>&gt;</strong></td>
    <td style="padding: 12px;">Greater than (bigger)</td>
    <td style="padding: 12px;">\\(7 > 3\\)</td>
    <td style="padding: 12px;">"7 is greater than 3"</td>
  </tr>
  <tr>
    <td style="padding: 12px; text-align: center; font-size: 24px; color: #2196f3"><strong>=</strong></td>
    <td style="padding: 12px;">Equal to (the same)</td>
    <td style="padding: 12px;">\\(5 = 5\\)</td>
    <td style="padding: 12px;">"5 equals 5"</td>
  </tr>
</table>

<h3>A Trick to Remember &lt; and &gt;</h3>
<p>The symbols \\(<\\) and \\(>\\) look like a hungry alligator's mouth! 🐊</p>

<div class="formula-box">
  <p><strong>The Hungry Alligator:</strong> The alligator's mouth always opens toward the <em>bigger</em> number because it wants to eat the bigger meal!</p>
</div>

<div style="text-align: center; margin: 20px 0;">
  <p style="font-size: 16px; margin-bottom: 10px;"><strong>Example 1:</strong></p>
  <p style="font-size: 20px">\\(3 < 7\\) — the mouth opens toward 7 (the bigger number)</p>

  <p style="font-size: 16px; margin: 20px 0 10px 0;"><strong>Example 2:</strong></p>
  <p style="font-size: 20px">\\(7 > 3\\) — the mouth opens toward 7 (the bigger number)</p>
</div>

<h3>Practice with Symbols</h3>
<div class="mcq-group">
  <p><strong>Question 1:</strong> Which symbol makes this true? \\(5 \\_ 8\\)</p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Yes! 5 is less than 8. The symbol opens toward the bigger number.">\\(<\\)</button>
    <button class="mcq-option" data-correct="false" data-explanation="No, > means greater than. 5 is not greater than 8.">\\(>\\)</button>
    <button class="mcq-option" data-correct="false" data-explanation="No, = means equal. 5 and 8 are not the same.">\\(=\\)</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="mcq-group">
  <p><strong>Question 2:</strong> Which is true?</p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="No, 4 is less than 9.">\\(4 > 9\\)</button>
    <button class="mcq-option" data-correct="true" data-explanation="Yes! 4 is less than 9.">\\(4 < 9\\)</button>
    <button class="mcq-option" data-correct="false" data-explanation="No, 4 and 9 are different.">\\(4 = 9\\)</button>
  </div>
  <div class="mcq-feedback"></div>
</div>"""
    },

    {
        "title": "Comparing Numbers from 0 to 20",
        "body": """<h3>Practice: Let's Compare!</h3>
<p>Now let's compare real numbers in our range of 0 to 20:</p>

<div style="max-width:500px;margin:20px auto;">
  <canvas id="comparisonChart" data-chart='{"type":"bar","data":{"labels":["2","5","8","10","15","18"],"datasets":[{"label":"Number Value","data":[2,5,8,10,15,18],"backgroundColor":"#4169E1"}]},"options":{"indexAxis":"y","plugins":{"title":{"display":true,"text":"Numbers 0-20 Size Comparison"}},"scales":{"x":{"max":20}}}}' height="200"></canvas>
</div>

<h3>Examples</h3>
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
  <tr style="background: #4169E180;">
    <th style="padding: 10px;">Comparison</th>
    <th style="padding: 10px;">Symbol</th>
    <th style="padding: 10px;">Read It As</th>
  </tr>
  <tr>
    <td style="padding: 10px;">\\(0\\) and \\(5\\)</td>
    <td style="padding: 10px; text-align: center">\\(0 < 5\\)</td>
    <td style="padding: 10px;">0 is less than 5</td>
  </tr>
  <tr style="background: rgba(255,255,255,0.03);">
    <td style="padding: 10px;">\\(12\\) and \\(9\\)</td>
    <td style="padding: 10px; text-align: center">\\(12 > 9\\)</td>
    <td style="padding: 10px;">12 is greater than 9</td>
  </tr>
  <tr>
    <td style="padding: 10px;">\\(15\\) and \\(15\\)</td>
    <td style="padding: 10px; text-align: center">\\(15 = 15\\)</td>
    <td style="padding: 10px;">15 equals 15</td>
  </tr>
  <tr style="background: rgba(255,255,255,0.03);">
    <td style="padding: 10px;">\\(3\\) and \\(20\\)</td>
    <td style="padding: 10px; text-align: center">\\(3 < 20\\)</td>
    <td style="padding: 10px;">3 is less than 20</td>
  </tr>
</table>

<div class="warning-box">
  <h4>⚠️ Common Mistake</h4>
  <p>Don't mix up the symbols! Remember:</p>
  <ul>
    <li>\\(<\\) points to the <strong>smaller</strong> number (like a hungry mouth opening toward smaller food? No! It opens to the BIGGER number!)</li>
    <li>\\(>\\) points away from the <strong>smaller</strong> number (opening toward the bigger)</li>
  </ul>
  <p><strong>Trick:</strong> The opening always faces the bigger number.</p>
</div>

<button class="reveal-btn" data-reveal="comp-sol">▼ More Examples</button>
<div class="reveal-panel" id="comp-sol" style="margin: 15px 0; padding: 15px; border-radius: 5px;">
  <p><strong>Is \\(10 > 6\\) true or false?</strong> TRUE — 10 is greater than 6 ✓</p>
  <p><strong>Is \\(17 < 20\\) true or false?</strong> TRUE — 17 is less than 20 ✓</p>
  <p><strong>Is \\(8 = 8\\) true or false?</strong> TRUE — 8 equals 8 ✓</p>
  <p><strong>Is \\(14 > 18\\) true or false?</strong> FALSE — 14 is NOT greater than 18 ✗</p>
</div>

<div class="success-box">
  <h4>✓ Key Points</h4>
  <ul>
    <li>Use \\(<\\) when the left number is smaller</li>
    <li>Use \\(>\\) when the left number is bigger</li>
    <li>Use \\(=\\) when the numbers are the same</li>
  </ul>
</div>"""
    },
]
