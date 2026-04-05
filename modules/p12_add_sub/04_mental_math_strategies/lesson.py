TITLE = "Mental Math Strategies for Addition and Subtraction"

SECTIONS = [
    {
        "title": "Why Learn Mental Math?",
        "body": """<p>The column method works great, but sometimes you don't have paper and pencil. Mental math means doing math in your head quickly!</p>
<p>Good news: You don't need to memorize anything. We'll use <strong>strategies</strong> that you already know, just in clever ways.</p>
<div class="concept-box">
<p><strong>Three main strategies:</strong></p>
<ol>
<li><strong>Jump Strategy:</strong> Count up (or down) in jumps</li>
<li><strong>Split Strategy:</strong> Break numbers into tens and ones</li>
<li><strong>Compensation:</strong> Add or subtract a bit extra, then fix it</li>
</ol>
</div>"""
    },
    {
        "title": "Strategy 1: The Jump Strategy (Number Line Hopping)",
        "body": """<p>Imagine a number line. Start at one number and make jumps to reach the other.</p>
<p><strong>Example: 34 + 23</strong></p>
<svg viewBox="0 0 650 140" style="width:100%;max-width:750px;height:auto;display:block;margin:16px auto;">
  <!-- Number line -->
  <line x1="40" y1="80" x2="620" y2="80" stroke='#8b949e' stroke-width="2"/>
  <!-- Start -->
  <circle cx="80" cy="80" r="6" fill='#4f8ef7' stroke='currentColor' stroke-width="2"/>
  <text x="80" y="110" text-anchor='middle' fill='currentColor' font-size='12'>34</text>
  <!-- Jump +20 -->
  <path d="M 80 70 Q 140 40 200 70" fill='none' stroke='#4f8ef7' stroke-width="2"/>
  <text x="140" y="35" text-anchor='middle' fill='#4f8ef7' font-size='12' font-weight='bold'>+20</text>
  <!-- After first jump -->
  <circle cx="200" cy="80" r="6" fill='currentColor' stroke='currentColor' stroke-width="1"/>
  <text x="200" y="110" text-anchor='middle' fill='currentColor' font-size='12'>54</text>
  <!-- Jump +3 -->
  <path d="M 200 70 Q 230 50 260 70" fill='none' stroke='#22c55e' stroke-width="2"/>
  <text x="230" y="45" text-anchor='middle' fill='#22c55e' font-size='12' font-weight='bold'>+3</text>
  <!-- End -->
  <circle cx="260" cy="80" r="6" fill='#22c55e' stroke='currentColor' stroke-width="2"/>
  <text x="260" y="110" text-anchor='middle' fill='currentColor' font-size='12'>57</text>
</svg>
<p><strong>Method:</strong></p>
<ol>
<li>Start at 34</li>
<li>Jump +20 to reach 54</li>
<li>Jump +3 to reach 57</li>
</ol>
<p>Why? We split 23 into 20 + 3, then jump in two steps. Much easier than counting 1, 2, 3...</p>"""
    },
    {
        "title": "Strategy 2: The Split Strategy (Breaking into Tens and Ones)",
        "body": """<p>This is like the column method, but we do it all in our heads.</p>
<p><strong>Example: 47 + 36</strong></p>
<div class="worked-example">
<p><strong>Step-by-step thinking:</strong></p>
<svg viewBox="0 0 600 180" style="width:100%;max-width:700px;height:auto;display:block;margin:16px auto;">
  <text x="50" y="25" fill='currentColor' font-size='13'>47 + 36 = ?</text>

  <text x="50" y="50" fill='currentColor' font-size='13'>Break into tens and ones:</text>
  <text x="50" y="70" fill='#4f8ef7' font-size='13'>47 = 40 + 7</text>
  <text x="50" y="90" fill='#4f8ef7' font-size='13'>36 = 30 + 6</text>

  <text x="50" y="115" fill='currentColor' font-size='13'>Add tens: 40 + 30 = 70</text>
  <text x="50" y="135" fill='currentColor' font-size='13'>Add ones: 7 + 6 = 13</text>

  <text x="50" y="160" fill='#f59e0b' font-size='14' font-weight='bold'>Answer: 70 + 13 = 83</text>
</svg>
<p><strong>Why it works:</strong> This is the same as the column method, just done faster without writing!</p>
</div>"""
    },
    {
        "title": "Strategy 3: Compensation (Make it Easy, Then Fix It)",
        "body": """<p>Sometimes it's easier to add or subtract a different number, then adjust.</p>
<p><strong>Example 1: 47 + 9 (Hard because of +9)</strong></p>
<p>Instead: Add 10, then subtract 1.</p>
<svg viewBox="0 0 600 120" style="width:100%;max-width:700px;height:auto;display:block;margin:16px auto;">
  <text x="50" y="30" fill='currentColor' font-size='13'>47 + 9 = ?</text>
  <text x="50" y="55" fill='currentColor' font-size='13'>Think: 9 is almost 10</text>
  <text x="50" y="75" fill='#4f8ef7' font-size='13'>Add 10: 47 + 10 = 57</text>
  <text x="50" y="95" fill='#22c55e' font-size='13'>Subtract 1: 57 - 1 = 56</text>
</svg>
<p><strong>Example 2: 52 - 9 (Hard because of -9)</strong></p>
<p>Instead: Subtract 10, then add 1.</p>
<svg viewBox="0 0 600 120" style="width:100%;max-width:700px;height:auto;display:block;margin:16px auto;">
  <text x="50" y="30" fill='currentColor' font-size='13'>52 - 9 = ?</text>
  <text x="50" y="55" fill='currentColor' font-size='13'>Think: 9 is almost 10</text>
  <text x="50" y="75" fill='#4f8ef7' font-size='13'>Subtract 10: 52 - 10 = 42</text>
  <text x="50" y="95" fill='#22c55e' font-size='13'>Add 1: 42 + 1 = 43</text>
</svg>"""
    },
    {
        "title": "Practice: Mental Math Strategies",
        "body": """<p>Try these using your favorite strategy! Some problems are easier with jumps, others with splitting.</p>
<div class="mcq-group">
  <p><strong>What is 25 + 30 using the jump strategy?</strong></p>
  <p><em>Hint: Start at 25, jump +30 to reach 55</em></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Jump +30 from 25 lands at 55. Answer: 55">55</button>
    <button class="mcq-option" data-correct="false">45</button>
    <button class="mcq-option" data-correct="false">65</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
<div class="mcq-group">
  <p><strong>What is 38 + 27 using the split strategy?</strong></p>
  <p><em>Hint: Tens: 30+20=50, Ones: 8+7=15</em></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false">55</button>
    <button class="mcq-option" data-correct="true" data-explanation="Tens: 30 + 20 = 50. Ones: 8 + 7 = 15. Answer: 50 + 15 = 65">65</button>
    <button class="mcq-option" data-correct="false">75</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
<div class="mcq-group">
  <p><strong>What is 43 + 9 using compensation?</strong></p>
  <p><em>Hint: Add 10 (get 53), then subtract 1</em></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false">51</button>
    <button class="mcq-option" data-correct="true" data-explanation="Add 10: 43 + 10 = 53. Subtract 1: 53 - 1 = 52. Answer: 52">52</button>
    <button class="mcq-option" data-correct="false">53</button>
  </div>
  <div class="mcq-feedback"></div>
</div>"""
    }
]
