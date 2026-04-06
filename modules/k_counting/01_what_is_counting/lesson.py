"""What is Counting? — Understanding the Foundation of Number."""

TITLE = "What is Counting?"

SECTIONS = [
    {
        "title": "Why Do We Need to Count?",
        "body": """<h3>Real-World Problem: Are Your Toys Safe?</h3>
<p>Imagine you have a collection of toy cars. You love them all and don't want to lose any. But how do you know if one is missing? You can't just look at them and guess. You need to <strong>count</strong> them — to match each toy to a number and find out exactly how many you have. If tomorrow you count again and get a different number, you know one went missing!</p>

<p>Counting is the tool we use to answer the question: <strong>"How many?"</strong></p>

<div class="success-box">
  <h4>Counting Solves Problems</h4>
  <p>We count to answer questions like:</p>
  <ul>
    <li>Do I have enough toys?</li>
    <li>Do I have more apples or more oranges?</li>
    <li>Will this fit in my backpack?</li>
    <li>Did I leave something behind?</li>
  </ul>
</div>

<h3>Saying Numbers is NOT the Same as Counting</h3>
<p>Many young children can recite: "1, 2, 3, 4, 5, 6, 7, 8, 9, 10..." like singing a song. But this is just <strong>reciting</strong>. Real counting is different.</p>

<div style="background: #fee2e2; padding: 15px; border-radius: 8px; margin: 20px 0;">
  <p><strong>Just Reciting:</strong> "One-two-three-four-five-six-seven-eight-nine-ten" (singing it fast)</p>
  <p style="margin-top: 10px;"><strong>Real Counting:</strong> Point to each toy, say one number for each toy, and use the last number to answer "how many?"</p>
</div>

<div class="concept-box">
  <h4>What Real Counting Is</h4>
  <p>Counting is <strong>pointing to objects one at a time and saying one number for each object in order</strong>. The last number you say tells you how many there are total.</p>
</div>"""
    },
    {
        "title": "The Three Key Ideas About Counting",
        "body": """<h3>Counting Uses Three Important Rules</h3>
<p>Mathematicians have discovered that all good counting follows three key principles. These principles help us count correctly every time, from \(1\) toy to \(100\) stars!</p>

<div class="formula-box">
  <div style="margin-bottom: 20px;">
    <h4 style="color: #4169E1;">1. Stable Order</h4>
    <p>Numbers always come in the same order. When counting: 1, 2, 3, 4, 5... the order never changes, no matter what you're counting.</p>
    <p style="margin-top: 10px; font-size: 14px">Example: Counting apples, toys, or fingers — the sequence is always 1, 2, 3, 4, 5...</p>
  </div>

  <div style="margin-bottom: 20px;">
    <h4 style="color: #4169E1;">2. One-to-One Correspondence</h4>
    <p>Each object gets exactly one number, and each number matches exactly one object. No object is skipped, no number matches two objects.</p>
    <p style="margin-top: 10px; font-size: 14px">Example: If you have 3 cookies, you say three numbers: 1, 2, 3 — one for each cookie.</p>
  </div>

  <div>
    <h4 style="color: #4169E1;">3. Cardinality</h4>
    <p>The last number you say is <strong>not just another number</strong> — it tells you the total amount. That number represents how many objects there are.</p>
    <p style="margin-top: 10px; font-size: 14px">Example: When you count 5 stars, the last number (5) is the answer to "how many stars?"</p>
  </div>
</div>

<svg viewBox="0 0 360 175" style="width:100%;max-width:460px;height:auto;display:block;margin:20px auto;">
  <!-- Title -->
  <text x="180" y="20" text-anchor='middle' font-size='15' font-weight='bold' fill='currentColor'>Counting 3 Apples</text>

  <!-- Apple 1 -->
  <circle cx="60" cy="70" r="20" fill='#d32f2f'/>
  <text x="60" y="120" text-anchor='middle' font-size='16' font-weight='bold' fill='currentColor'>1st</text>

  <!-- Apple 2 -->
  <circle cx="180" cy="70" r="20" fill='#d32f2f'/>
  <text x="180" y="120" text-anchor='middle' font-size='16' font-weight='bold' fill='currentColor'>2nd</text>

  <!-- Apple 3 (with highlight) -->
  <circle cx="300" cy="70" r="20" fill='#d32f2f'/>
  <circle cx="300" cy="70" r="24" fill='none' stroke='#22c55e' stroke-width="3"/>
  <text x="300" y="120" text-anchor='middle' font-size='16' font-weight='bold' fill='#22c55e'>3rd = Total!</text>

  <!-- Count labels -->
  <text x="60" y="155" text-anchor='middle' font-size='13' fill='currentColor'>Say "1"</text>
  <text x="180" y="155" text-anchor='middle' font-size='13' fill='currentColor'>Say "2"</text>
  <text x="300" y="155" text-anchor='middle' font-size='13' fill='currentColor'>Say "3"</text>
</svg>"""
    },
    {
        "title": "How to Count Step by Step",
        "body": """<h3>The Five Steps of Real Counting</h3>

<p>To count \(n\) objects correctly, follow these steps every time:</p>

<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
  <tr style="background: #4169E180;">
    <th style="padding: 12px; width: 15%">Step</th>
    <th style="padding: 12px;">What to Do</th>
    <th style="padding: 12px;">Example</th>
  </tr>
  <tr>
    <td style="padding: 12px; font-weight: bold">1</td>
    <td style="padding: 12px;">Look at all the objects you need to count</td>
    <td style="padding: 12px;">🍎🍎🍎🍎 (4 apples)</td>
  </tr>
  <tr style="background: rgba(255,255,255,0.03);">
    <td style="padding: 12px; font-weight: bold">2</td>
    <td style="padding: 12px;">Point to the first object</td>
    <td style="padding: 12px;">Point to the first apple</td>
  </tr>
  <tr>
    <td style="padding: 12px; font-weight: bold">3</td>
    <td style="padding: 12px;">Say "ONE" for the first object</td>
    <td style="padding: 12px;">Say "ONE" ✓</td>
  </tr>
  <tr style="background: rgba(255,255,255,0.03);">
    <td style="padding: 12px; font-weight: bold">4</td>
    <td style="padding: 12px;">Move to the next object and say the next number</td>
    <td style="padding: 12px;">Say "TWO" for the second apple</td>
  </tr>
  <tr>
    <td style="padding: 12px; font-weight: bold">5</td>
    <td style="padding: 12px;">Keep going until you reach the last object</td>
    <td style="padding: 12px;">Say "THREE," "FOUR" for the rest</td>
  </tr>
  <tr style="">
    <td style="padding: 12px; font-weight: bold">✓</td>
    <td style="padding: 12px; font-weight: bold">The last number = your answer!</td>
    <td style="padding: 12px; font-weight: bold">There are 4 apples!</td>
  </tr>
</table>

<h3>Quick Tip: Stay Organized</h3>
<p>To count well, keep your objects organized so you don't miss any or count twice:</p>
<ul>
  <li><strong>Make a line:</strong> Put objects in a straight row from left to right</li>
  <li><strong>Push aside:</strong> As you count, move each object to the side to show you've counted it</li>
  <li><strong>Count slowly:</strong> Give yourself time to think about each number-object pair</li>
  <li><strong>Use your finger:</strong> Point to each object — don't just look!</li>
</ul>

<div class="warning-box">
  <h4>Mistakes to Avoid</h4>
  <ul>
    <li>❌ Counting too fast and skipping objects</li>
    <li>❌ Pointing to the same object twice</li>
    <li>❌ Forgetting where you started</li>
    <li>❌ Saying numbers out of order (like "1, 3, 2")</li>
  </ul>
</div>

<div class="worked-example">
  <h4>Worked Example: Counting 3 Toys</h4>
  <p><strong>Goal:</strong> Count these toys: 🧸🚗🎮</p>
  <p style="margin-top: 10px;"><strong>Step 1:</strong> Look at all three toys ✓</p>
  <p><strong>Step 2:</strong> Point to the teddy bear</p>
  <p><strong>Step 3:</strong> Say "ONE" 🧸</p>
  <p><strong>Step 4:</strong> Point to the car, say "TWO" 🚗</p>
  <p><strong>Step 5:</strong> Point to the video game, say "THREE" 🎮</p>
  <p style="margin-top: 15px; font-weight: bold; color: var(--success);">Answer: There are \(3\) toys! ✓</p>
</div>

<h3>Quick Check: Is This Real Counting?</h3>

<div class="mcq-group">
  <p><strong>A child says "1, 2, 3, 4, 5" really fast without looking at the toys. Is that real counting?</strong></p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Right! Saying numbers without pointing to objects is just reciting, not counting.">No, that's reciting, not counting</button>
    <button class="mcq-option" data-correct="false" data-explanation="No — real counting requires matching numbers to objects.">Yes, that's real counting</button>
    <button class="mcq-option" data-correct="false" data-explanation="Reciting fast doesn't make it real counting.">Maybe, if they say it really fast</button>
  </div>
  <div class="mcq-feedback"></div>
</div>"""
    }
]
