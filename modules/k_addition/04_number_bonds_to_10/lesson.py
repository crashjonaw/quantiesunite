"""Concept 4: Number Bonds to 10 — All Ways to Make 10."""

TITLE = "Number Bonds to 10: Building to the Big Number"

SECTIONS = [
    {
        "title": "Why 10 is Special",
        "body": """<h3>The Magic Number 10</h3>
<p>10 is a very important number in math. Here's why:</p>
<ul>
  <li>We have 10 fingers (perfect for counting!)</li>
  <li>Our number system is built on 10</li>
  <li>If you know all the ways to make 10, you can solve almost any addition problem</li>
</ul>

<div class="concept-box">
  <h4>Big Learning Goal</h4>
  <p><strong>Learn all the number bonds to 10.</strong>
  These facts are so important that you'll want to memorize them!</p>
</div>

<h3>Why Learn Number Bonds to 10?</h3>
<p>Knowing that:</p>
<ul>
  <li><strong>\(7 + 3 = 10\)</strong> helps you solve <strong>\(7 + 4\)</strong> (make 10, then add 1 more)</li>
  <li><strong>\(6 + 4 = 10\)</strong> helps with addition to any number higher than 10</li>
  <li>Later, these bonds help with <em>subtraction</em> too</li>
</ul>"""
    },

    {
        "title": "All the Number Bonds for 10",
        "body": """<h3>Every Way to Make 10</h3>
<p>There are 11 different number bonds to 10 (that's even more than for 5!):</p>

<div class="formula-box">
  <h4>The Complete List:</h4>
  <ul style="font-size: 16px; line-height: 1.8;">
    <li><strong>\(0 + 10 = 10\)</strong></li>
    <li><strong>\(1 + 9 = 10\)</strong></li>
    <li><strong>\(2 + 8 = 10\)</strong></li>
    <li><strong>\(3 + 7 = 10\)</strong></li>
    <li><strong>\(4 + 6 = 10\)</strong></li>
    <li><strong>\(5 + 5 = 10\)</strong> (the middle one — both parts are equal!)</li>
    <li><strong>\(6 + 4 = 10\)</strong></li>
    <li><strong>\(7 + 3 = 10\)</strong></li>
    <li><strong>\(8 + 2 = 10\)</strong></li>
    <li><strong>\(9 + 1 = 10\)</strong></li>
    <li><strong>\(10 + 0 = 10\)</strong></li>
  </ul>
</div>

<h3>See the Pattern</h3>
<p>Look at these pairs:</p>
<ul>
  <li><strong>\(1 + 9\)</strong> and <strong>\(9 + 1\)</strong> — both equal 10</li>
  <li><strong>\(2 + 8\)</strong> and <strong>\(8 + 2\)</strong> — both equal 10</li>
  <li><strong>\(3 + 7\)</strong> and <strong>\(7 + 3\)</strong> — both equal 10</li>
</ul>

<div class="success-box">
  <h4>✨ The Middle Pair</h4>
  <p><strong>\(5 + 5 = 10\)</strong> is special because both parts are the same.
  This is called a <strong>double fact</strong>.</p>
</div>"""
    },

    {
        "title": "Visual Number Bonds to 10",
        "body": """<h3>Seeing 10 with 10 Fingers</h3>
<p>Use your fingers to show number bonds to 10! Here are a few examples:</p>

<div class="formula-box">
  <h4>Example: \(7 + 3 = 10\)</h4>
  <p style="text-align: center; font-size: 18px; margin: 10px 0;">
    Hold up 7 fingers on one hand + 3 fingers on the other = 10 fingers total
  </p>
  <p style="text-align: center; font-size: 16px">🖐️ (7 fingers) + ✋ (3 fingers) = ✋✋ (10 fingers)</p>
</div>

<h3>Number Bonds to 10 Chart</h3>
<p>Here are all the number bonds to 10 shown visually:</p>

<canvas id="bondChart10" data-chart='{"type":"bar","data":{"labels":["0+10","1+9","2+8","3+7","4+6","5+5","6+4","7+3","8+2","9+1","10+0"],"datasets":[{"label":"Different ways to make 10","data":[10,10,10,10,10,10,10,10,10,10,10],"backgroundColor":["#4f8ef7","#4f8ef7","#4f8ef7","#4f8ef7","#4f8ef7","#f59e0b","#4f8ef7","#4f8ef7","#4f8ef7","#4f8ef7","#4f8ef7"]}]},"options":{"plugins":{"title":{"display":true,"text":"All Ways to Make 10 (notice 5+5 is highlighted)"}},"scales":{"y":{"max":11,"title":{"display":true,"text":"Sum"}}}}}' height="250"></canvas>

<h3>The 10-Frame Tool</h3>
<p>A 10-frame is a \(2 \\times 5\) grid that holds exactly 10 objects. It helps us see number bonds clearly:</p>

<svg viewBox="0 0 300 140" style="width: 100%; max-width: 350px; height: auto; display: block; margin: 20px auto;">
  <!-- Title -->
  <text x="105" y="18" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>6 + 4 = 10</text>

  <!-- 10-frame: 2 rows x 5 columns, 6 blue + 4 green -->
  <!-- Row 1: 5 blue -->
  <rect x="15" y="32" width="30" height="30" fill='#4f8ef7' stroke='#8b949e' stroke-width="2" rx="4"/>
  <text x="30" y="52" text-anchor='middle' fill='white' font-size='18' font-weight='bold'>&#9679;</text>

  <rect x="50" y="32" width="30" height="30" fill='#4f8ef7' stroke='#8b949e' stroke-width="2" rx="4"/>
  <text x="65" y="52" text-anchor='middle' fill='white' font-size='18' font-weight='bold'>&#9679;</text>

  <rect x="85" y="32" width="30" height="30" fill='#4f8ef7' stroke='#8b949e' stroke-width="2" rx="4"/>
  <text x="100" y="52" text-anchor='middle' fill='white' font-size='18' font-weight='bold'>&#9679;</text>

  <rect x="120" y="32" width="30" height="30" fill='#4f8ef7' stroke='#8b949e' stroke-width="2" rx="4"/>
  <text x="135" y="52" text-anchor='middle' fill='white' font-size='18' font-weight='bold'>&#9679;</text>

  <rect x="155" y="32" width="30" height="30" fill='#4f8ef7' stroke='#8b949e' stroke-width="2" rx="4"/>
  <text x="170" y="52" text-anchor='middle' fill='white' font-size='18' font-weight='bold'>&#9679;</text>

  <!-- Row 2: 1 blue + 4 green -->
  <rect x="15" y="67" width="30" height="30" fill='#4f8ef7' stroke='#8b949e' stroke-width="2" rx="4"/>
  <text x="30" y="87" text-anchor='middle' fill='white' font-size='18' font-weight='bold'>&#9679;</text>

  <rect x="50" y="67" width="30" height="30" fill='#22c55e' stroke='#8b949e' stroke-width="2" rx="4"/>
  <text x="65" y="87" text-anchor='middle' fill='white' font-size='18' font-weight='bold'>&#9679;</text>

  <rect x="85" y="67" width="30" height="30" fill='#22c55e' stroke='#8b949e' stroke-width="2" rx="4"/>
  <text x="100" y="87" text-anchor='middle' fill='white' font-size='18' font-weight='bold'>&#9679;</text>

  <rect x="120" y="67" width="30" height="30" fill='#22c55e' stroke='#8b949e' stroke-width="2" rx="4"/>
  <text x="135" y="87" text-anchor='middle' fill='white' font-size='18' font-weight='bold'>&#9679;</text>

  <rect x="155" y="67" width="30" height="30" fill='#22c55e' stroke='#8b949e' stroke-width="2" rx="4"/>
  <text x="170" y="87" text-anchor='middle' fill='white' font-size='18' font-weight='bold'>&#9679;</text>

  <!-- Labels -->
  <text x="220" y="52" font-size='12' fill='currentColor'><tspan font-weight='bold'>6</tspan> blue</text>
  <text x="220" y="87" font-size='12' fill='currentColor'><tspan font-weight='bold'>4</tspan> green</text>

  <!-- Summary -->
  <text x="105" y="120" text-anchor='middle' font-size='13' fill='currentColor'>All 10 cells filled!</text>
</svg>"""
    },

    {
        "title": "Using Number Bonds to 10 for Bigger Addition",
        "body": """<h3>How Number Bonds to 10 Help with Larger Numbers</h3>
<p>Once you know the bonds to 10, you can solve any addition problem! Here's how:</p>

<div class="worked-example">
  <h4>Problem: \(7 + 5 = ?\)</h4>
  <p><strong>Step 1:</strong> Look at 7. Ask: "What do I add to 7 to make 10?"</p>
  <p style="margin-left: 20px;">Answer: 3 (because \(7 + 3 = 10\))</p>

  <p style="margin-top: 10px;"><strong>Step 2:</strong> Break 5 into 3 and 2.</p>
  <p style="margin-left: 20px;">So: \(7 + 5 = 7 + (3 + 2)\)</p>

  <p style="margin-top: 10px;"><strong>Step 3:</strong> First make 10.</p>
  <p style="margin-left: 20px;">\(7 + 3 = 10\)</p>

  <p style="margin-top: 10px;"><strong>Step 4:</strong> Then add what's left.</p>
  <p style="margin-left: 20px;">\(10 + 2 = 12\)</p>

  <p style="margin-top: 15px; font-size: 16px; font-weight: bold;">Answer: \(7 + 5 = 12\) ✓</p>
</div>

<div class="success-box">
  <h4>The Strategy</h4>
  <p>
    <strong>Make a 10 first, then add the rest.</strong><br>
    This strategy works for ANY addition! It's very powerful.
  </p>
</div>"""
    },

    {
        "title": "Practice with Number Bonds to 10",
        "body": """<h3>Test Your Knowledge of Bonds to 10</h3>

<div class="mcq-group">
  <p><strong>What is \(6 + 4\)?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="Count on from 6: 7, 8, 9, 10. That's 4 more, so the answer is 10.">9</button>
    <button class="mcq-option" data-correct="true" data-explanation="\(6 + 4 = 10\). This is a number bond to 10.">10</button>
    <button class="mcq-option" data-correct="false" data-explanation="That's too many. \(6 + 4 = 10\), not 11.">11</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="mcq-group" style="margin-top: 20px;">
  <p><strong>If \(5 + 5 = 10\), what is \(5 + 4\)?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="\(5 + 5 = 10\), so \(5 + 4\) is one less. Try again.">9</button>
    <button class="mcq-option" data-correct="true" data-explanation="\(5 + 5 = 10\), so \(5 + 4 = 9\). You're one less than 10.">9</button>
    <button class="mcq-option" data-correct="false" data-explanation="That would be \(5 + 6\). Count on from 5.">11</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="mcq-group" style="margin-top: 20px;">
  <p><strong>Complete the number bond: \(10 = 3 + ?\)</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="\(3 + 6 = 9\), not 10. Try \(3 + 7\).">6</button>
    <button class="mcq-option" data-correct="true" data-explanation="\(3 + 7 = 10\). Start at 3 and count on: 4, 5, 6, 7, 8, 9, 10.">7</button>
    <button class="mcq-option" data-correct="false" data-explanation="\(3 + 8 = 11\), which is too many.">8</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<h3>Try to Match Them All</h3>
<div style="padding: 15px; border-radius: 8px; margin: 15px 0;">
  <p style="font-size: 16px;"><strong>Match these pairs to make 10:</strong></p>
  <ul style="margin-top: 10px;">
    <li>\(1 + ?\) → 10</li>
    <li>\(2 + ?\) → 10</li>
    <li>\(4 + ?\) → 10</li>
    <li>\(8 + ?\) → 10</li>
  </ul>
  <p style="margin-top: 15px; font-size: 14px">
    Answers: 9, 8, 6, 2
  </p>
</div>"""
    }
]
