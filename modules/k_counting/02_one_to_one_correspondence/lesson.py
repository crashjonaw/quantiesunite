"""One-to-One Correspondence — The Heart of Counting."""

TITLE = "One-to-One Correspondence"

SECTIONS = [
    {
        "title": "What Does One-to-One Correspondence Mean?",
        "body": """<h3>The Most Important Counting Skill</h3>
<p>Imagine you're a teacher with \\(5\\) students and \\(5\\) chairs. You want each student to sit in exactly one chair, and each chair to have exactly one student. You wouldn't want two students sharing a chair, and you wouldn't want empty chairs. This is <strong>one-to-one correspondence</strong> — everything pairs up perfectly with nothing left over and nothing counted twice.</p>

<div class="concept-box">
  <h4>One-to-One Correspondence Definition</h4>
  <p>Each object gets matched to exactly one number, and each number matches exactly one object.</p>
  <ul>
    <li>No object is skipped</li>
    <li>No object is counted more than once</li>
    <li>Every number matches one object</li>
  </ul>
</div>

<h3>Visual Example: Perfect Matching</h3>
<p>Look at this perfect one-to-one match. Each number from \\(1\\) to \\(3\\) pairs with exactly one object:</p>

<svg viewBox="0 0 400 200" style="width:100%;max-width:500px;height:auto;display:block;margin:20px auto;">
  <!-- Title -->
  <text x="200" y="20" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>Perfect One-to-One Match</text>

  <!-- Numbers -->
  <text x="60" y="70" text-anchor='middle' font-size='20' font-weight='bold' fill='currentColor'>1</text>
  <text x="60" y="110" text-anchor='middle' font-size='20' font-weight='bold' fill='currentColor'>2</text>
  <text x="60" y="150" text-anchor='middle' font-size='20' font-weight='bold' fill='currentColor'>3</text>

  <!-- Arrows -->
  <line x1="75" y1="66" x2="210" y2="66" stroke='#4169E1' stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="75" y1="106" x2="210" y2="106" stroke='#4169E1' stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="75" y1="146" x2="210" y2="146" stroke='#4169E1' stroke-width="2" marker-end="url(#arrowhead)"/>

  <!-- Objects -->
  <circle cx="280" cy="66" r="15" fill='#d32f2f'/>
  <circle cx="280" cy="106" r="15" fill='#d32f2f'/>
  <circle cx="280" cy="146" r="15" fill='#d32f2f'/>

  <!-- Object labels -->
  <text x="310" y="70" font-size='12' fill='currentColor'>apple</text>
  <text x="310" y="110" font-size='12' fill='currentColor'>apple</text>
  <text x="310" y="150" font-size='12' fill='currentColor'>apple</text>

  <!-- Arrow marker definition -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill='#4169E1'/>
    </marker>
  </defs>

  <!-- Label -->
  <text x="200" y="190" text-anchor='middle' font-size='12' fill='currentColor'>Each number → one object ✓</text>
</svg>

<div class="mcq-group">
  <p><strong>Is this one-to-one correspondence?</strong></p>
  <p style="text-align: center; font-size: 18px;">Number: 1, 2, 3 | Objects: 🍎, 🍎, 🍎</p>
  <div class="mcq-options">
    <button class="mcq-option" data-correct="true" data-explanation="Perfect! Each number matches exactly one apple.">Yes, each number has exactly one object</button>
    <button class="mcq-option" data-correct="false" data-explanation="No — this is a perfect match!">No, some objects are left out</button>
    <button class="mcq-option" data-correct="false" data-explanation="No — one number can't match two objects.">No, one number matches two objects</button>
  </div>
  <div class="mcq-feedback"></div>
</div>"""
    },
    {
        "title": "Common One-to-One Mistakes",
        "body": """<h3>Mistake #1: Counting an Object Twice</h3>
<p>The biggest mistake children make is counting the same object twice. This happens when you're pointing too fast and not keeping track carefully.</p>

<div class="warning-box">
  <h4>Wrong Way: Double Counting</h4>
  <div class="formula-box">
    <p style="text-align: center; font-size: 18px;"><strong>Objects:</strong> 🍎🍎🍎</p>
    <p style="margin-top: 10px;"><strong>What happened:</strong></p>
    <p>Point to first apple and say "1" ✓</p>
    <p>Point to first apple again and say "2" ❌</p>
    <p>Point to second apple and say "3" ❌</p>
    <p style="margin-top: 10px; color: #ef4444;"><strong>Wrong answer: 3 apples (but there are only 2!)</strong></p>
  </div>

  <h4>Right Way: One Point, One Number</h4>
  <div class="formula-box">
    <p style="text-align: center; font-size: 18px;"><strong>Objects:</strong> 🍎🍎🍎</p>
    <p style="margin-top: 10px;"><strong>What happened:</strong></p>
    <p>Point to first apple and say "1" ✓</p>
    <p>Point to second apple and say "2" ✓</p>
    <p>Point to third apple and say "3" ✓</p>
    <p style="margin-top: 10px; color: var(--success);"><strong>Correct answer: 3 apples! ✓</strong></p>
  </div>
</div>

<h3>Mistake #2: Forgetting to Count an Object</h3>
<p>Sometimes you miss an object because you're not staying organized. This breaks one-to-one correspondence too.</p>

<div class="warning-box">
  <h4>Wrong Way: Skipping an Object</h4>
  <div class="formula-box">
    <p style="text-align: center; font-size: 18px;"><strong>Objects:</strong> 🍎🍎🍎</p>
    <p style="margin-top: 10px;"><strong>What happened:</strong></p>
    <p>Point to first apple and say "1" ✓</p>
    <p>Skip the second apple by accident ❌</p>
    <p>Point to third apple and say "2" ❌</p>
    <p style="margin-top: 10px; color: #ef4444;"><strong>Wrong answer: 2 apples (but there are 3!)</strong></p>
  </div>

  <h4>Right Way: Count Each Apple</h4>
  <div class="formula-box">
    <p style="text-align: center; font-size: 18px;"><strong>Objects:</strong> 🍎🍎🍎</p>
    <p style="margin-top: 10px;"><strong>What happened:</strong></p>
    <p>Point to first apple and say "1" ✓</p>
    <p>Point to second apple and say "2" ✓</p>
    <p>Point to third apple and say "3" ✓</p>
    <p style="margin-top: 10px; color: var(--success);"><strong>Correct answer: 3 apples! ✓</strong></p>
  </div>
</div>"""
    },
    {
        "title": "Strategies for Perfect One-to-One Correspondence",
        "body": """<h3>Strategy #1: Point to Each Object</h3>
<p>Don't just look at objects — actually point to them! When you point, your finger marks which object you're on. This helps you not skip any and not count any twice.</p>

<div class="worked-example">
  <h4>Example: Counting Stars with Your Finger</h4>
  <p style="font-size: 20px; text-align: center;">🌟 🌟 🌟 🌟 🌟</p>
  <p style="text-align: center; margin-top: 15px;">Put your finger on the first star → say "1"</p>
  <p style="text-align: center;">Move your finger to the next star → say "2"</p>
  <p style="text-align: center;">Keep moving your finger → say "3, 4, 5"</p>
  <p style="text-align: center; font-weight: bold; color: var(--success); margin-top: 15px;">Your finger helps you stay organized! ✓</p>
</div>

<h3>Strategy #2: Make a Line and Push Objects Aside</h3>
<p>Arrange objects in a line. As you count each one, push it to the side. This shows clearly which objects you've counted.</p>

<svg viewBox="0 0 400 180" style="width:100%;max-width:500px;height:auto;display:block;margin:20px auto;">
  <!-- Before -->
  <text x="95" y="30" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>Before:</text>
  <circle cx="50" cy="70" r="12" fill='#d32f2f'/>
  <circle cx="80" cy="70" r="12" fill='#d32f2f'/>
  <circle cx="110" cy="70" r="12" fill='#d32f2f'/>
  <circle cx="140" cy="70" r="12" fill='#d32f2f'/>

  <!-- Arrow -->
  <text x="200" y="80" font-size='20' fill='currentColor'>→</text>

  <!-- After -->
  <text x="295" y="30" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>After Counting:</text>
  <circle cx="250" cy="70" r="12" fill='#d32f2f' opacity='0.3'/>
  <circle cx="280" cy="70" r="12" fill='#d32f2f' opacity='0.3'/>
  <circle cx="310" cy="70" r="12" fill='#d32f2f' opacity='0.3'/>
  <circle cx="340" cy="70" r="12" fill='#22c55e'/>
  <text x="340" y="120" text-anchor='middle' font-size='12' fill='#22c55e'>counted ✓</text>

  <!-- Labels -->
  <text x="200" y="160" text-anchor='middle' font-size='12' fill='currentColor'>Counted (moved aside) → Next to count</text>
</svg>

<h3>Strategy #3: Count Slowly and Deliberately</h3>
<p>Take your time. Say each number clearly, point carefully, and make sure you see the object before moving to the next one. Fast counting causes mistakes!</p>

<div class="success-box">
  <h4>Remember: The Power of One-to-One</h4>
  <p>When you count with perfect one-to-one correspondence:</p>
  <ul>
    <li>✓ You never skip objects</li>
    <li>✓ You never count twice</li>
    <li>✓ Your answer is always correct</li>
  </ul>
</div>"""
    }
]
