"""Counting to 20 — Extending Your Number Knowledge."""

TITLE = "Counting to 20"

SECTIONS = [
    {
        "title": "The Extended Sequence: 1 to 20",
        "body": """<h3>Going Beyond 10</h3>
<p>You've mastered counting to 10! Now it's time to extend your counting knowledge to \\(20\\). The good news: the pattern is very similar to what you already learned.</p>

<div style="background: #4169E180; padding: 20px; border-radius: 8px; margin: 20px 0; text-align: center;">
  <p style="font-size: 16px; margin-bottom: 10px;"><strong>1 to 10:</strong></p>
  <p style="font-size: 18px; margin: 0;">1, 2, 3, 4, 5, 6, 7, 8, 9, 10</p>

  <p style="font-size: 16px; margin-top: 20px; margin-bottom: 10px;"><strong>1 to 20:</strong></p>
  <p style="font-size: 18px; margin: 0;">1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20</p>
</div>

<h3>The Pattern in the Teens</h3>
<p>Numbers 11–19 follow a pattern. Look at the pattern:</p>

<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
  <tr style="background: #4169E180;">
    <th style="padding: 8px;">Number</th>
    <th style="padding: 8px;">How It Sounds</th>
    <th style="padding: 8px;">Pattern</th>
  </tr>
  <tr>
    <td style="padding: 8px;">11</td>
    <td style="padding: 8px;">Eleven</td>
    <td style="padding: 8px;">One + ten = 11 (but we say "eleven")</td>
  </tr>
  <tr style="background: rgba(255,255,255,0.03);">
    <td style="padding: 8px;">12</td>
    <td style="padding: 8px;">Twelve</td>
    <td style="padding: 8px;">Two + ten = 12 (but we say "twelve")</td>
  </tr>
  <tr>
    <td style="padding: 8px;">13–19</td>
    <td style="padding: 8px;">Thirteen–Nineteen</td>
    <td style="padding: 8px;">Number + teen (like 3 + teen = thirteen)</td>
  </tr>
  <tr style="background: rgba(255,255,255,0.03);">
    <td style="padding: 8px;">20</td>
    <td style="padding: 8px;">Twenty</td>
    <td style="padding: 8px;">Two tens = 20</td>
  </tr>
</table>

<div class="concept-box">
  <h4>Understanding Place Value</h4>
  <p>Numbers like \\(15\\) mean "1 ten and 5 ones." When you count \\(15\\) objects, you have one group of \\(10\\) and \\(5\\) more.</p>
</div>

<svg viewBox="0 0 400 150" style="width:100%;max-width:500px;height:auto;display:block;margin:20px auto;">
  <!-- Title -->
  <text x="200" y="20" text-anchor='middle' font-size='14' font-weight='bold'>15 Objects = 1 Ten + 5 Ones</text>

  <!-- 10 circles in a box (the "ten") -->
  <rect x="30" y="40" width="140" height="90" fill='none' stroke='#4169E1' stroke-width="2" stroke-dasharray="5,5"/>
  <text x="100" y="35" text-anchor='middle' font-size='12' fill='#4169E1'>1 Ten</text>

  <circle cx="45" cy="55" r="8" fill='#4169E1'/>
  <circle cx="65" cy="55" r="8" fill='#4169E1'/>
  <circle cx="85" cy="55" r="8" fill='#4169E1'/>
  <circle cx="105" cy="55" r="8" fill='#4169E1'/>
  <circle cx="125" cy="55" r="8" fill='#4169E1'/>
  <circle cx="45" cy="80" r="8" fill='#4169E1'/>
  <circle cx="65" cy="80" r="8" fill='#4169E1'/>
  <circle cx="85" cy="80" r="8" fill='#4169E1'/>
  <circle cx="105" cy="80" r="8" fill='#4169E1'/>
  <circle cx="125" cy="80" r="8" fill='#4169E1'/>

  <!-- Plus sign -->
  <text x="200" y="95" text-anchor='middle' font-size='28' font-weight='bold'>+</text>

  <!-- 5 circles (the "ones") -->
  <text x="300" y="35" text-anchor='middle' font-size='12' fill='#ef4444'>5 Ones</text>
  <circle cx="270" cy="55" r="8" fill='#ef4444'/>
  <circle cx="290" cy="55" r="8" fill='#ef4444'/>
  <circle cx="310" cy="55" r="8" fill='#ef4444'/>
  <circle cx="330" cy="55" r="8" fill='#ef4444'/>
  <circle cx="350" cy="55" r="8" fill='#ef4444'/>

  <!-- Answer -->
  <text x="200" y="145" text-anchor='middle' font-size='16' font-weight='bold' fill='#22c55e'>Total = 15</text>
</svg>"""
    },
    {
        "title": "Counting and Organizing Large Groups",
        "body": """<h3>Counting Beyond 10 Gets Tricky</h3>
<p>When you have more than 10 objects, counting one by one becomes slower and harder. It's easy to lose track. Smart counters use grouping strategies to stay organized.</p>

<h3>Strategy: Count by Tens First, Then Ones</h3>
<p>Instead of counting all 15 objects one at a time, make a group of 10 and a group of 5. Then count: "10... 11, 12, 13, 14, 15"</p>

<div class="worked-example">
  <h4>Example: Counting 15 Stars Smartly</h4>
  <p style="text-align: center; font-size: 20px; margin-bottom: 15px;">🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟 | 🌟🌟🌟🌟🌟</p>
  <p><strong>Step 1:</strong> Make groups — 10 stars in one group, 5 in another</p>
  <p><strong>Step 2:</strong> Count the big group: "1, 2, 3... 10"</p>
  <p><strong>Step 3:</strong> Count on from 10: "10... 11, 12, 13, 14, 15"</p>
  <p style="margin-top: 15px; font-weight: bold; color: var(--success);">Answer: 15 stars! ✓</p>
  <p style="margin-top: 10px; font-size: 14px">This is much faster than counting all 15 one by one!</p>
</div>

<h3>Counting On Instead of Starting Over</h3>
<p>Once you reach 10, you don't count "1, 2, 3..." again. Instead, you "count on" from 10:</p>

<div class="formula-box">
  <p><strong>Example:</strong> You have 10 blocks and add 5 more.</p>
  <p style="margin-top: 10px;">❌ Wrong way: Count all 15 from the beginning: "1, 2, 3, 4, 5... 15"</p>
  <p style="margin-top: 10px;">✓ Right way: Count on from 10: "10... 11, 12, 13, 14, 15"</p>
  <p style="margin-top: 10px; font-weight: bold;">The answer is the same (15), but counting on is much faster!</p>
</div>

<canvas id="countChart2" data-chart='{"type":"bar","data":{"labels":["Group A (10)","Group B (8)","Total"],"datasets":[{"label":"Count","data":[10,8,18],"backgroundColor":["#4169E1","#ef4444","#22c55e"]}]},"options":{"plugins":{"title":{"display":true,"text":"Counting in Groups: 10 + 8 = 18"}},"scales":{"y":{"beginAtZero":true,"max":20}}}}' height="220"></canvas>"""
    },
    {
        "title": "Recognizing Numbers 11–20",
        "body": """<h3>Number Recognition: Seeing the Numbers</h3>
<p>Being able to count to 20 is important. But also being able to recognize the written numbers \\(11\\)–\\(20\\) helps you in reading, writing, and math problems.</p>

<div class="formula-box">
  <h4>Numbers 11–20 Chart:</h4>
  <table style="width: 100%; border-collapse: collapse;">
    <tr>
      <td style="padding: 8px; text-align: center; font-size: 16px;">11</td>
      <td style="padding: 8px; text-align: center; font-size: 16px;">12</td>
      <td style="padding: 8px; text-align: center; font-size: 16px;">13</td>
      <td style="padding: 8px; text-align: center; font-size: 16px;">14</td>
      <td style="padding: 8px; text-align: center; font-size: 16px;">15</td>
    </tr>
    <tr>
      <td style="padding: 8px; text-align: center; font-size: 16px;">16</td>
      <td style="padding: 8px; text-align: center; font-size: 16px;">17</td>
      <td style="padding: 8px; text-align: center; font-size: 16px;">18</td>
      <td style="padding: 8px; text-align: center; font-size: 16px;">19</td>
      <td style="padding: 8px; text-align: center; font-size: 16px;">20</td>
    </tr>
  </table>
</div>

<h3>Quick Check: What Number Comes Next?</h3>

<div class="mcq-group">
  <p><strong>What number comes after 16?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="That's 1 less than 16, not more.">15</button>
    <button class="mcq-option" data-correct="true" data-explanation="Correct! After 16 comes 17.">17</button>
    <button class="mcq-option" data-correct="false" data-explanation="That's 3 numbers ahead.">19</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<p style="margin-top: 20px;"></p>

<div class="mcq-group">
  <p><strong>What number comes before 14?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Yes! 13 comes right before 14.">13</button>
    <button class="mcq-option" data-correct="false" data-explanation="That's 2 numbers back.">12</button>
    <button class="mcq-option" data-correct="false" data-explanation="That's the same, not before.">14</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="success-box">
  <h4>You've Learned to Count to 20!</h4>
  <p>This is a huge accomplishment. You can now count objects all the way to 20, recognize the numbers, and understand how they're organized in tens and ones.</p>
</div>"""
    }
]
