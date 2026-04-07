"""02. The Ten Digits — Understanding our number system's building blocks."""

TITLE = "The Ten Digits: Building Blocks of Numbers"

SECTIONS = [
    {
        "title": "The Ten Digits: Our Basic Symbols",
        "body": """<h3>The Foundation of All Numbers</h3>
<p>Every number you will ever write or see is made from just <strong>ten symbols</strong>. These symbols are called <strong>digits</strong>:</p>

<div style="background: linear-gradient(135deg, #e0e7ff 0%, #f0f4ff 100%); color: #1a1a2e; padding: 30px; border-radius: 8px; text-align: center; margin: 20px 0; border-left: 5px solid #4169E1;">
  <p style="font-size: 14px; margin: 0 0 10px 0">THE TEN DIGITS</p>
  <p style="font-size: 48px; letter-spacing: 12px; color: #4169E1; margin: 0; font-weight: bold;">0  1  2  3  4  5  6  7  8  9</p>
</div>

<p>That's it! No more digits after \\(9\\). But here's the amazing part: using only these \\(10\\) symbols, we can write <em>any number that exists</em> — even a trillion!</p>

<h3>How Do We Write Numbers Bigger Than 9?</h3>
<p>We <strong>combine</strong> the digits. Here are some examples:</p>

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin: 20px 0;">
  <div class="formula-box">
    <p style="font-size: 32px; color: #4169E1; margin: 0;"><strong>10</strong></p>
    <p style="font-size: 12px; margin: 5px 0 0 0">Digit 1 + Digit 0</p>
  </div>
  <div class="formula-box">
    <p style="font-size: 32px; color: #4169E1; margin: 0;"><strong>25</strong></p>
    <p style="font-size: 12px; margin: 5px 0 0 0">Digit 2 + Digit 5</p>
  </div>
  <div class="formula-box">
    <p style="font-size: 32px; color: #4169E1; margin: 0;"><strong>100</strong></p>
    <p style="font-size: 12px; margin: 5px 0 0 0">1, then two 0s</p>
  </div>
</div>

<div class="success-box">
  <h4>✓ Amazing Fact</h4>
  <p>With only \\(10\\) digits, mathematicians can write numbers as big as you want: \\(1,000,000\\) (one million), \\(1,000,000,000\\) (one billion), or even bigger!</p>
</div>"""
    },

    {
        "title": "Why Exactly Ten Digits?",
        "body": """<h3>Why Ten?</h3>
<p>You might ask: "Why \\(10\\) digits and not \\(5\\) or \\(20\\)?" The answer is simple: <strong>humans have ten fingers</strong>!</p>

<p>Long, long ago, people counted using their fingers. They would put down one finger for one object, two fingers for two objects, and so on. When they used all ten fingers, they had counted to \\(10\\). So naturally, humans chose a number system based on \\(10\\).</p>

<div style="text-align: center; margin: 20px 0;">
  <p style="font-size: 32px;">👐 👐</p>
  <p><strong>Two hands = 10 fingers</strong></p>
</div>

<h3>The Base-10 System</h3>
<p>Because we use \\(10\\) digits, we say we use the <strong>base-10 number system</strong>. Another name is the <strong>decimal system</strong> (the word "decimal" comes from the Latin word for \\(10\\)).</p>

<div class="concept-box">
  <h4>Base-10: The Pattern</h4>
  <p>In base-10:</p>
  <ul>
    <li>We count: \\(0, 1, 2, 3, 4, 5, 6, 7, 8, 9\\)</li>
    <li>Then we run out of single digits, so we start combining: \\(10, 11, 12, ...\\)</li>
    <li>This makes it easy to work with groups of \\(10\\)</li>
  </ul>
</div>

<h3>Real-World Grouping by Ten</h3>
<p>We group things in tens all the time:</p>

<ul>
  <li>🖐️ <strong>Fingers:</strong> We have \\(10\\) fingers on two hands.</li>
  <li>💰 <strong>Money:</strong> Ten pennies = \\(1\\) dime (in some countries).</li>
  <li>📦 <strong>Eggs:</strong> A baker buys eggs in boxes of \\(10\\) or \\(12\\).</li>
  <li>📅 <strong>Days:</strong> \\(10\\) days, \\(20\\) days, \\(30\\) days are natural groups.</li>
</ul>

<div class="warning-box">
  <h4>⚠️ Not All Systems Use Base-10</h4>
  <p>Some ancient people used different systems. The Babylonians used base-60 (for telling time). But today, almost all humans use base-10 because of our \\(10\\) fingers!</p>
</div>"""
    },

    {
        "title": "Digits vs. Numbers: A Quick Review",
        "body": """<h3>Let's Make Sure We Understand</h3>
<p>Now that you know about the \\(10\\) digits, let's review the difference between a digit and a number.</p>

<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
  <tr style="background: #4169E180;">
    <th style="padding: 12px; text-align: left">Term</th>
    <th style="padding: 12px; text-align: left">Definition</th>
    <th style="padding: 12px; text-align: left">Examples</th>
  </tr>
  <tr>
    <td style="padding: 12px;"><strong>Digit</strong></td>
    <td style="padding: 12px;">One of the \\(10\\) basic symbols</td>
    <td style="padding: 12px;">\\(0, 1, 2, 3, 4, 5, 6, 7, 8, 9\\)</td>
  </tr>
  <tr style="background: rgba(255,255,255,0.03);">
    <td style="padding: 12px;"><strong>Number</strong></td>
    <td style="padding: 12px;">A quantity made from one or more digits</td>
    <td style="padding: 12px;">\\(5, 17, 100, 2,548\\)</td>
  </tr>
</table>

<h3>Practice Questions</h3>
<div class="mcq-group">
  <p><strong>Question 1:</strong> How many digits does it take to write the number \\(42\\)?</p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="Not quite. The number 42 is one number, but it uses more than one digit.">1 digit</button>
    <button class="mcq-option" data-correct="true" data-explanation="Yes! 42 uses the digit 4 and the digit 2.">2 digits</button>
    <button class="mcq-option" data-correct="false" data-explanation="No, we only use 10 digits total in our system.">42 digits</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="mcq-group">
  <p><strong>Question 2:</strong> How many different digits are in the number \\(1{,}234\\)?</p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="false" data-explanation="This is how many digits total, but the question asks for DIFFERENT digits.">4 different digits</button>
    <button class="mcq-option" data-correct="true" data-explanation="Yes! The different digits are 1, 2, 3, and 4. Each one is different.">4 different digits</button>
    <button class="mcq-option" data-correct="false" data-explanation="Nope. There are 4 digit positions, and 4 different digits.">10 different digits</button>
  </div>
  <div class="mcq-feedback"></div>
</div>

<div class="success-box">
  <h4>✓ Summary</h4>
  <p>We use \\(10\\) digits (\\(0\\) through \\(9\\)) to build all numbers. Why \\(10\\)? Because humans have \\(10\\) fingers! Any number can be written using these \\(10\\) building blocks.</p>
</div>"""
    },
]
