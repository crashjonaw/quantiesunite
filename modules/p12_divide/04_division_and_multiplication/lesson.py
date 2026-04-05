"""Division and Multiplication — Concept lesson."""

TITLE = "Division and Multiplication are Opposites"

SECTIONS = [
    {
        "title": "They Undo Each Other!",
        "body": """<p>Multiplication and division are <strong>inverse operations</strong>. This means they undo each other!</p>
<p>If you multiply two numbers together, you can divide the result by one of them to get back to the other number.</p>
<div class="concept-box">
  <strong>Multiplication and Division are Opposites:</strong><br>
  If 3 × 4 = 12, then<br>
  12 ÷ 3 = 4 (dividing by 3 gives us back the 4)<br>
  12 ÷ 4 = 3 (dividing by 4 gives us back the 3)
</div>
<svg viewBox="0 0 500 180" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <text x="250" y="25" text-anchor='middle' fill='currentColor' font-size='16' font-weight='bold'>Multiplication and Division: A Two-Way Street</text>

  <!-- Multiplication box -->
  <g fill='none' stroke='#4f8ef7' stroke-width="2">
    <rect x="20" y="60" width="150" height="80" rx="5"/>
  </g>
  <text x="95" y="80" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>Multiplication</text>
  <text x="95" y="105" text-anchor='middle' fill='currentColor' font-size='14'>3 × 4</text>
  <text x="95" y="125" text-anchor='middle' fill='currentColor' font-size='14'>=</text>
  <text x="95" y="145" text-anchor='middle' fill='#22c55e' font-size='16' font-weight='bold'>12</text>

  <!-- Arrow right -->
  <text x="190" y="110" text-anchor='middle' fill='currentColor' font-size='18' font-weight='bold'>→</text>

  <!-- Division box -->
  <g fill='none' stroke='#22c55e' stroke-width="2">
    <rect x="220" y="60" width="150" height="80" rx="5"/>
  </g>
  <text x="295" y="80" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>Division</text>
  <text x="295" y="105" text-anchor='middle' fill='currentColor' font-size='14'>12 ÷ 3</text>
  <text x="295" y="125" text-anchor='middle' fill='currentColor' font-size='14'>=</text>
  <text x="295" y="145" text-anchor='middle' fill='#22c55e' font-size='16' font-weight='bold'>4</text>

  <!-- Arrow left -->
  <text x="395" y="110" text-anchor='middle' fill='currentColor' font-size='18' font-weight='bold'>←</text>
</svg>
<p><strong>Think of it like this:</strong> Multiplication <strong>puts things together</strong>, division <strong>takes them apart</strong>.</p>"""
    },
    {
        "title": "Using Multiplication to Check Division",
        "body": """<p><strong>This is super helpful!</strong> You can always check your division answer using multiplication.</p>
<p>If you're not sure about a division answer, multiply the answer by the divisor. You should get back the original number!</p>
<div class="worked-example">
  <strong>Check: Is 20 ÷ 4 = 5?</strong><br>
  Multiply: 5 × 4 = 20 ✓<br>
  Yes! The answer is correct!<br><br>
  <strong>Check: Is 15 ÷ 3 = 6?</strong><br>
  Multiply: 6 × 3 = 18 ✗<br>
  No! The answer is wrong. (Actually 15 ÷ 3 = 5)
</div>
<svg viewBox="0 0 480 220" style="width:100%;max-width:480px;height:auto;display:block;margin:16px auto;">
  <text x="240" y="25" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Checking Division with Multiplication</text>

  <!-- Problem -->
  <text x="40" y="70" fill='currentColor' font-size='13' font-weight='bold'>Problem: 24 ÷ 6 = ?</text>

  <!-- Step 1: Solve -->
  <text x="40" y="110" fill='currentColor' font-size='13'>Step 1: Solve the division</text>
  <text x="60" y="135" fill='currentColor' font-size='12'>24 ÷ 6 = 4</text>

  <!-- Step 2: Check -->
  <text x="40" y="170" fill='currentColor' font-size='13'>Step 2: Check with multiplication</text>
  <text x="60" y="195" fill='currentColor' font-size='12'>4 × 6 = 24 ✓</text>
  <text x="240" y="195" fill='#22c55e' font-size='13' font-weight='bold'>Correct!</text>
</svg>"""
    },
    {
        "title": "Finding Division Facts from Multiplication Facts",
        "body": """<p><strong>If you know your multiplication tables, you already know division!</strong></p>
<p>Every multiplication fact gives you two division facts:</p>
<div class="worked-example">
  <strong>From 3 × 5 = 15, we get two division facts:</strong><br>
  • 15 ÷ 3 = 5<br>
  • 15 ÷ 5 = 3<br><br>
  <strong>From 4 × 6 = 24, we get:</strong><br>
  • 24 ÷ 4 = 6<br>
  • 24 ÷ 6 = 4
</div>
<canvas id="div_multiply1" data-chart='{
  "type":"bar",
  "data":{
    "labels":["2 × 6","3 × 5","4 × 4","5 × 3","6 × 2"],
    "datasets":[{
      "label":"Result",
      "data":[12,15,16,15,12],
      "backgroundColor":["#4f8ef7","#22c55e","#f59e0b","#a855f7","#ef4444"]
    }]
  },
  "options":{
    "plugins":{
      "title":{"display":true,"text":"Multiplication Facts and Their Division Counterparts"}
    },
    "scales":{"y":{"beginAtZero":true,"max":20}}
  }
}' height="250"></canvas>
<p style="margin-top:20px;"><strong>Family facts:</strong> Multiplication and division facts that come from each other are called a "fact family".</p>
<div class="success-box">
  <strong>Fact Family Example: 3, 4, and 12</strong><br>
  3 × 4 = 12<br>
  4 × 3 = 12<br>
  12 ÷ 3 = 4<br>
  12 ÷ 4 = 3
</div>"""
    },
    {
        "title": "Why This Connection Matters",
        "body": """<p>Understanding that multiplication and division are opposites helps you:</p>
<ul style="font-size:14px;">
  <li><strong>Learn faster:</strong> You don't have to memorize division facts separately—they come from multiplication!</li>
  <li><strong>Check your work:</strong> Always verify division with multiplication</li>
  <li><strong>Solve harder problems:</strong> You can use what you know about multiplication to figure out division</li>
  <li><strong>Understand patterns:</strong> You see how numbers relate to each other</li>
</ul>
<svg viewBox="0 0 500 200" style="width:100%;max-width:500px;height:auto;display:block;margin:16px auto;">
  <text x="250" y="25" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Connected Operations</text>

  <!-- Circle 1: Fact group -->
  <g fill='none' stroke='#4f8ef7' stroke-width="2">
    <circle cx="150" cy="120" r="60"/>
  </g>
  <text x="150" y="105" text-anchor='middle' fill='currentColor' font-size='13' font-weight='bold'>2 × 5</text>
  <text x="150" y="125" text-anchor='middle' fill='currentColor' font-size='13'>5 × 2</text>
  <text x="150" y="145" text-anchor='middle' fill='currentColor' font-size='13'>10 ÷ 2</text>
  <text x="150" y="165" text-anchor='middle' fill='#22c55e' font-size='13' font-weight='bold'>10 ÷ 5</text>

  <text x="320" y="80" fill='currentColor' font-size='13' font-weight='bold'>All related!</text>
  <text x="320" y="105" fill='currentColor' font-size='12'>They all involve</text>
  <text x="320" y="125" fill='currentColor' font-size='12'>the same three</text>
  <text x="320" y="145" fill='currentColor' font-size='12'>numbers:</text>
  <text x="320" y="170" fill='#22c55e' font-size='14' font-weight='bold'>2, 5, and 10</text>
</svg>"""
    },
    {
        "title": "Practice: Making Fact Families",
        "body": """<p><strong>Can you make a fact family?</strong> If you know one fact, you can write all four!</p>
<div class="worked-example">
  <strong>Start with: 3 × 6 = 18</strong><br><br>
  The fact family is:<br>
  3 × 6 = 18<br>
  6 × 3 = 18<br>
  18 ÷ 3 = 6<br>
  18 ÷ 6 = 3<br><br>
  <strong>All four facts use the same three numbers: 3, 6, and 18</strong>
</div>
<div class="success-box">
  <strong>Remember:</strong> If you know one number fact, you can always find the others by thinking of multiplication and division as opposites. They're all connected!
</div>
<svg viewBox="0 0 400 200" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;">
  <text x="200" y="25" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Fact Family for 4, 5, and 20</text>

  <g fill='none' stroke='#4f8ef7' stroke-width="2">
    <rect x="30" y="60" width="160" height="35" rx="3"/>
    <rect x="210" y="60" width="160" height="35" rx="3"/>
    <rect x="30" y="110" width="160" height="35" rx="3"/>
    <rect x="210" y="110" width="160" height="35" rx="3"/>
  </g>

  <text x="110" y="85" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>4 × 5 = 20</text>
  <text x="290" y="85" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>5 × 4 = 20</text>
  <text x="110" y="135" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>20 ÷ 4 = 5</text>
  <text x="290" y="135" text-anchor='middle' fill='currentColor' font-size='14' font-weight='bold'>20 ÷ 5 = 4</text>

  <text x="200" y="175" text-anchor='middle' fill='#22c55e' font-size='12' font-weight='bold'>All use: 4, 5, and 20</text>
</svg>"""
    }
]
