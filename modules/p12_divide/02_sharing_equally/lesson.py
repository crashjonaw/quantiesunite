"""Sharing Equally — Concept lesson."""

TITLE = "Sharing Equally (Partitive Division)"

SECTIONS = [
    {
        "title": "What is Sharing Equally?",
        "body": """<p><strong>Sharing equally</strong> means taking a total amount and dividing it into a known number of groups, where each group gets the same amount.</p>
<p>This is the most common way we think about division in everyday life. When you share, you already know how many people (or groups) there are, and you want to find out how much each person gets.</p>
<div class="concept-box">
  <strong>The Sharing Question:</strong><br>
  "I have 12 cookies and 3 friends. How many cookies does each friend get if I share fairly?"<br>
  Answer: 12 ÷ 3 = 4 cookies each
</div>
<p>Notice: We know there are 3 friends (the divisor) and 12 cookies (the dividend). We're looking for the amount each friend gets (the quotient).</p>
<svg viewBox="0 0 500 240" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <text x="250" y="25" text-anchor='middle' fill='#e6edf3' font-size='16' font-weight='bold'>Sharing 12 Cookies Among 3 Friends</text>

  <!-- Friend 1 with plate -->
  <circle cx="70" cy="110" r="40" fill='none' stroke='#4f8ef7' stroke-width="2"/>
  <circle cx="60" cy="90" r="8" fill='#f59e0b'/>
  <circle cx="80" cy="90" r="8" fill='#f59e0b'/>
  <circle cx="50" cy="110" r="8" fill='#f59e0b'/>
  <circle cx="90" cy="110" r="8" fill='#f59e0b'/>
  <text x="70" y="175" text-anchor='middle' fill='#e6edf3' font-size='12'>Friend 1</text>
  <text x="70" y="190" text-anchor='middle' fill='#22c55e' font-size='14' font-weight='bold'>4 cookies</text>

  <!-- Friend 2 with plate -->
  <circle cx="250" cy="110" r="40" fill='none' stroke='#4f8ef7' stroke-width="2"/>
  <circle cx="240" cy="90" r="8" fill='#f59e0b'/>
  <circle cx="260" cy="90" r="8" fill='#f59e0b'/>
  <circle cx="230" cy="110" r="8" fill='#f59e0b'/>
  <circle cx="270" cy="110" r="8" fill='#f59e0b'/>
  <text x="250" y="175" text-anchor='middle' fill='#e6edf3' font-size='12'>Friend 2</text>
  <text x="250" y="190" text-anchor='middle' fill='#22c55e' font-size='14' font-weight='bold'>4 cookies</text>

  <!-- Friend 3 with plate -->
  <circle cx="430" cy="110" r="40" fill='none' stroke='#4f8ef7' stroke-width="2"/>
  <circle cx="420" cy="90" r="8" fill='#f59e0b'/>
  <circle cx="440" cy="90" r="8" fill='#f59e0b'/>
  <circle cx="410" cy="110" r="8" fill='#f59e0b'/>
  <circle cx="450" cy="110" r="8" fill='#f59e0b'/>
  <text x="430" y="175" text-anchor='middle' fill='#e6edf3' font-size='12'>Friend 3</text>
  <text x="430" y="190" text-anchor='middle' fill='#22c55e' font-size='14' font-weight='bold'>4 cookies</text>

  <text x="250" y="230" text-anchor='middle' fill='#e6edf3' font-size='13'>12 ÷ 3 = 4</text>
</svg>"""
    },
    {
        "title": "How to Share Fairly",
        "body": """<p>To share something equally among a group, you give each person (or group) one item at a time, going around until everything is distributed.</p>
<p><strong>Strategy:</strong> Count by the number of people until you reach your total.</p>
<div class="worked-example">
  <strong>Example: Share 15 candies equally among 5 children</strong><br><br>
  Round 1: Give 1 candy to each child (5 candies used, 10 left)<br>
  Round 2: Give 1 more to each child (10 candies used, 5 left)<br>
  Round 3: Give 1 more to each child (15 candies used, 0 left)<br><br>
  <strong>Result:</strong> Each child gets 3 candies (15 ÷ 5 = 3)
</div>
<svg viewBox="0 0 450 200" style="width:100%;max-width:450px;height:auto;display:block;margin:16px auto;">
  <text x="225" y="25" text-anchor='middle' fill='#e6edf3' font-size='15' font-weight='bold'>Sharing in Rounds</text>

  <!-- Round 1 -->
  <text x="40" y="50" fill='#e6edf3' font-size='13' font-weight='bold'>Round 1:</text>
  <circle cx="40" cy="75" r="6" fill='#f59e0b'/>
  <circle cx="70" cy="75" r="6" fill='#f59e0b'/>
  <circle cx="100" cy="75" r="6" fill='#f59e0b'/>
  <circle cx="130" cy="75" r="6" fill='#f59e0b'/>
  <circle cx="160" cy="75" r="6" fill='#f59e0b'/>
  <text x="40" y="100" fill='#e6edf3' font-size='12'>5 given out</text>

  <!-- Round 2 -->
  <text x="220" y="50" fill='#e6edf3' font-size='13' font-weight='bold'>Round 2:</text>
  <circle cx="220" cy="75" r="6" fill='#f59e0b'/>
  <circle cx="250" cy="75" r="6" fill='#f59e0b'/>
  <circle cx="280" cy="75" r="6" fill='#f59e0b'/>
  <circle cx="310" cy="75" r="6" fill='#f59e0b'/>
  <circle cx="340" cy="75" r="6" fill='#f59e0b'/>
  <text x="220" y="100" fill='#e6edf3' font-size='12'>10 given out</text>

  <!-- Round 3 -->
  <text x="50" y="145" fill='#e6edf3' font-size='13' font-weight='bold'>Round 3:</text>
  <circle cx="50" cy="170" r="6" fill='#f59e0b'/>
  <circle cx="80" cy="170" r="6" fill='#f59e0b'/>
  <circle cx="110" cy="170" r="6" fill='#f59e0b'/>
  <circle cx="140" cy="170" r="6" fill='#f59e0b'/>
  <circle cx="170" cy="170" r="6" fill='#f59e0b'/>
  <text x="50" y="195" fill='#e6edf3' font-size='12'>15 given out</text>

  <text x="300" y="170" fill='#22c55e' font-size='13' font-weight='bold'>Each gets 3!</text>
</svg>"""
    },
    {
        "title": "Real-World Sharing Examples",
        "body": """<p>Here are situations where we use sharing division every day:</p>
<ul style="font-size:14px;">
  <li><strong>Pizza party:</strong> 8 slices of pizza shared among 4 friends = 2 slices each</li>
  <li><strong>Team games:</strong> 20 players divided into 4 teams = 5 players on each team</li>
  <li><strong>Snack time:</strong> 18 grapes shared among 6 children = 3 grapes each</li>
  <li><strong>Toy sharing:</strong> 12 building blocks shared among 3 children = 4 blocks each</li>
  <li><strong>Seating:</strong> 24 chairs divided into 6 rows = 4 chairs in each row</li>
</ul>
<div class="success-box">
  <strong>Remember:</strong> In sharing division, the number of groups is always given. We find how much each group gets.
</div>
<canvas id="div_sharing1" data-chart='{
  "type":"bar",
  "data":{
    "labels":["8 ÷ 2","12 ÷ 3","15 ÷ 5","20 ÷ 4"],
    "datasets":[{
      "label":"Amount per group",
      "data":[4,4,3,5],
      "backgroundColor":["#4f8ef7","#22c55e","#f59e0b","#a855f7"]
    }]
  },
  "options":{
    "plugins":{
      "title":{"display":true,"text":"Sharing: Different Totals, Different Numbers of Groups"}
    },
    "scales":{"y":{"beginAtZero":true,"max":6}}
  }
}' height="250"></canvas>"""
    },
    {
        "title": "Drawing a Sharing Picture",
        "body": """<p><strong>When solving a sharing problem, drawing a picture helps!</strong></p>
<p><strong>Steps:</strong></p>
<ol>
  <li>Draw circles or boxes to show the number of groups</li>
  <li>Draw small items (dots, stars, etc.) to show what's being shared</li>
  <li>Distribute items one at a time or in groups to each container</li>
  <li>Count how many each group has</li>
</ol>
<svg viewBox="0 0 450 240" style="width:100%;max-width:450px;height:auto;display:block;margin:16px auto;">
  <text x="225" y="25" text-anchor='middle' fill='#e6edf3' font-size='15' font-weight='bold'>Drawing a Sharing Problem: 12 ÷ 3</text>

  <!-- Three baskets -->
  <g fill='none' stroke='#4f8ef7' stroke-width="2">
    <rect x="30" y="60" width="100" height="100" rx="5"/>
    <rect x="175" y="60" width="100" height="100" rx="5"/>
    <rect x="320" y="60" width="100" height="100" rx="5"/>
  </g>

  <!-- Items in basket 1 -->
  <circle cx="50" cy="85" r="7" fill='#f59e0b'/>
  <circle cx="85" cy="85" r="7" fill='#f59e0b'/>
  <circle cx="50" cy="120" r="7" fill='#f59e0b'/>
  <circle cx="85" cy="120" r="7" fill='#f59e0b'/>

  <!-- Items in basket 2 -->
  <circle cx="195" cy="85" r="7" fill='#f59e0b'/>
  <circle cx="230" cy="85" r="7" fill='#f59e0b'/>
  <circle cx="195" cy="120" r="7" fill='#f59e0b'/>
  <circle cx="230" cy="120" r="7" fill='#f59e0b'/>

  <!-- Items in basket 3 -->
  <circle cx="340" cy="85" r="7" fill='#f59e0b'/>
  <circle cx="375" cy="85" r="7" fill='#f59e0b'/>
  <circle cx="340" cy="120" r="7" fill='#f59e0b'/>
  <circle cx="375" cy="120" r="7" fill='#f59e0b'/>

  <!-- Labels -->
  <text x="80" y="200" text-anchor='middle' fill='#e6edf3' font-size='12'>Group 1</text>
  <text x="225" y="200" text-anchor='middle' fill='#e6edf3' font-size='12'>Group 2</text>
  <text x="370" y="200" text-anchor='middle' fill='#e6edf3' font-size='12'>Group 3</text>

  <text x="80" y="225" text-anchor='middle' fill='#22c55e' font-size='13' font-weight='bold'>4 items</text>
  <text x="225" y="225" text-anchor='middle' fill='#22c55e' font-size='13' font-weight='bold'>4 items</text>
  <text x="370" y="225" text-anchor='middle' fill='#22c55e' font-size='13' font-weight='bold'>4 items</text>
</svg>"""
    }
]
