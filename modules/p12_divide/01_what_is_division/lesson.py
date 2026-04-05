"""What is Division? — Concept lesson."""

TITLE = "What is Division?"

SECTIONS = [
    {
        "title": "Division Means Sharing Fairly",
        "body": """<p>Division is the way we <strong>share something equally</strong> among people or groups. When we divide, everyone gets the same amount!</p>
<p>Imagine you have 12 cookies and 3 friends. You want each friend to get the same number of cookies. How many should each friend get?</p>
<div class="concept-box">
  <strong>Division Symbol:</strong> The ÷ symbol means "divide" or "share equally"
</div>
<p>When we write <strong>12 ÷ 3 = 4</strong>, we're saying: "12 things divided equally among 3 people gives each person 4 things."</p>
<svg viewBox="0 0 500 200" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <text x="250" y="25" text-anchor='middle' fill='#e6edf3' font-size='16' font-weight='bold'>12 cookies shared equally among 3 friends</text>

  <!-- Friend 1 plate -->
  <circle cx="80" cy="110" r="45" fill='none' stroke='#4f8ef7' stroke-width="3"/>
  <circle cx="65" cy="85" r="10" fill='#f59e0b'/>
  <circle cx="95" cy="85" r="10" fill='#f59e0b'/>
  <circle cx="65" cy="110" r="10" fill='#f59e0b'/>
  <circle cx="95" cy="110" r="10" fill='#f59e0b'/>
  <text x="80" y="175" text-anchor='middle' fill='#e6edf3' font-size='13' font-weight='bold'>Friend 1: 4</text>

  <!-- Friend 2 plate -->
  <circle cx="250" cy="110" r="45" fill='none' stroke='#4f8ef7' stroke-width="3"/>
  <circle cx="235" cy="85" r="10" fill='#f59e0b'/>
  <circle cx="265" cy="85" r="10" fill='#f59e0b'/>
  <circle cx="235" cy="110" r="10" fill='#f59e0b'/>
  <circle cx="265" cy="110" r="10" fill='#f59e0b'/>
  <text x="250" y="175" text-anchor='middle' fill='#e6edf3' font-size='13' font-weight='bold'>Friend 2: 4</text>

  <!-- Friend 3 plate -->
  <circle cx="420" cy="110" r="45" fill='none' stroke='#4f8ef7' stroke-width="3"/>
  <circle cx="405" cy="85" r="10" fill='#f59e0b'/>
  <circle cx="435" cy="85" r="10" fill='#f59e0b'/>
  <circle cx="405" cy="110" r="10" fill='#f59e0b'/>
  <circle cx="435" cy="110" r="10" fill='#f59e0b'/>
  <text x="420" y="175" text-anchor='middle' fill='#e6edf3' font-size='13' font-weight='bold'>Friend 3: 4</text>
</svg>"""
    },
    {
        "title": "Understanding the Division Equation",
        "body": """<p>Let's understand what each number in a division problem means:</p>
<div class="worked-example">
  <strong>\\(12 \\div 3 = 4\\)</strong><br><br>
  <strong>12</strong> = the total amount we're dividing (the dividend)<br>
  <strong>÷</strong> = the division symbol<br>
  <strong>3</strong> = the number of groups or people (the divisor)<br>
  <strong>4</strong> = the amount each group gets (the quotient)
</div>
<p><strong>Real-world examples:</strong></p>
<ul>
  <li>12 pencils shared among 3 students → each gets 4 pencils</li>
  <li>15 apples divided equally into 5 baskets → each basket gets 3 apples</li>
  <li>20 cookies shared among 4 friends → each friend gets 5 cookies</li>
</ul>
<svg viewBox="0 0 450 180" style="width:100%;max-width:450px;height:auto;display:block;margin:16px auto;">
  <text x="225" y="25" text-anchor='middle' fill='#e6edf3' font-size='15' font-weight='bold'>Parts of a Division Problem</text>

  <g fill='none' stroke='#22c55e' stroke-width="2">
    <rect x="50" y="60" width="80" height="60" rx="5"/>
  </g>
  <text x="90" y="95" text-anchor='middle' fill='#e6edf3' font-size='18' font-weight='bold'>12</text>
  <text x="90" y="130" text-anchor='middle' fill='#e6edf3' font-size='11'>Total amount</text>

  <text x="150" y="100" text-anchor='middle' fill='#e6edf3' font-size='20' font-weight='bold'>÷</text>

  <g fill='none' stroke='#22c55e' stroke-width="2">
    <rect x="180" y="60" width="80" height="60" rx="5"/>
  </g>
  <text x="220" y="95" text-anchor='middle' fill='#e6edf3' font-size='18' font-weight='bold'>3</text>
  <text x="220" y="130" text-anchor='middle' fill='#e6edf3' font-size='11'>Number of groups</text>

  <text x="280" y="100" text-anchor='middle' fill='#e6edf3' font-size='20' font-weight='bold'>=</text>

  <g fill='none' stroke='#22c55e' stroke-width="2">
    <rect x="310" y="60" width="80" height="60" rx="5"/>
  </g>
  <text x="350" y="95" text-anchor='middle' fill='#e6edf3' font-size='18' font-weight='bold'>4</text>
  <text x="350" y="130" text-anchor='middle' fill='#e6edf3' font-size='11'>Amount per group</text>
</svg>"""
    },
    {
        "title": "Why Division Matters",
        "body": """<p>Division is one of the four basic math operations (along with addition, subtraction, and multiplication). We use it all the time in real life!</p>
<div class="success-box">
  <strong>Uses of Division:</strong><br>
  ✓ Sharing food or toys fairly among friends<br>
  ✓ Splitting costs between people<br>
  ✓ Organizing items into equal groups<br>
  ✓ Figuring out fair turns and schedules<br>
  ✓ Solving word problems
</div>
<p>When we learn division, we're learning to be fair and to think logically about breaking things into equal parts.</p>
<canvas id="div_concept1" data-chart='{
  "type":"bar",
  "data":{
    "labels":["12 divided by 2","12 divided by 3","12 divided by 4","12 divided by 6"],
    "datasets":[{
      "label":"Result",
      "data":[6,4,3,2],
      "backgroundColor":["#4f8ef7","#22c55e","#f59e0b","#a855f7"]
    }]
  },
  "options":{
    "plugins":{
      "title":{"display":true,"text":"Dividing 12 Different Ways"}
    },
    "scales":{"y":{"beginAtZero":true,"max":8}}
  }
}' height="250"></canvas>
<p style="margin-top:20px;"><strong>Key insight:</strong> The more groups we divide into, the fewer things each group gets!</p>"""
    },
    {
        "title": "From Sharing to Division",
        "body": """<p>Think about a real moment: you're at a birthday party with cookies to share. That's division!</p>
<p>Division starts with a <strong>simple idea:</strong> "How do we split this fairly?"</p>
<ol>
  <li><strong>Start:</strong> You have a total amount (12 cookies)</li>
  <li><strong>Decide:</strong> How many groups? (3 friends)</li>
  <li><strong>Share:</strong> Give each group the same amount</li>
  <li><strong>Check:</strong> Does everyone have the same? ✓</li>
</ol>
<svg viewBox="0 0 400 200" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
  <text x="200" y="25" text-anchor='middle' fill='#e6edf3' font-size='14' font-weight='bold'>The Division Process</text>

  <circle cx="80" cy="100" r="35" fill='none' stroke='#4f8ef7' stroke-width="2"/>
  <text x="80" y="105" text-anchor='middle' fill='#e6edf3' font-size='13'>Start:<br/>12 cookies</text>

  <text x="140" y="105" text-anchor='middle' fill='#e6edf3' font-size='16' font-weight='bold'>→</text>

  <circle cx="200" cy="100" r="35" fill='none' stroke='#22c55e' stroke-width="2"/>
  <text x="200" y="105" text-anchor='middle' fill='#e6edf3' font-size='13'>Divide into:<br/>3 groups</text>

  <text x="260" y="105" text-anchor='middle' fill='#e6edf3' font-size='16' font-weight='bold'>→</text>

  <circle cx="320" cy="100" r="35" fill='none' stroke='#f59e0b' stroke-width="2"/>
  <text x="320" y="105" text-anchor='middle' fill='#e6edf3' font-size='13'>Each gets:<br/>4 cookies</text>

  <text x="200" y="170" text-anchor='middle' fill='#e6edf3' font-size='13'>12 ÷ 3 = 4</text>
</svg>"""
    },
    {
        "title": "Check Your Understanding",
        "body": """<p><strong>Question:</strong> If you have 15 apples and want to share them equally among 5 friends, how many apples does each friend get?</p>
<p>Think about it step by step:</p>
<ol>
  <li>Total amount: 15 apples</li>
  <li>Number of friends: 5</li>
  <li>We write: 15 ÷ 5 = ?</li>
  <li>Each friend gets: 3 apples</li>
</ol>
<div class="success-box">
  <strong>Answer:</strong> 15 ÷ 5 = 3<br>
  Each friend gets 3 apples.
</div>
<p><strong>Try this yourself:</strong> If you have 20 pencils and share them equally among 4 students, how many pencils does each student get? (Hint: Write it as a division problem: 20 ÷ 4 = ?)</p>"""
    }
]
