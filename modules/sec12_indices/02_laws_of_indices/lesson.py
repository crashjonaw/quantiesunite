TITLE = "Laws of Indices: Multiplication & Division"

SECTIONS = [
    {
        "title": "Law 1: Multiplying Powers (Same Base)",
        "body": """<div class='concept-box'>
<p><strong>When multiplying numbers with the same base, add the indices.</strong></p>
<p>$$a^m \\times a^n = a^{m+n}$$</p>
</div>

<div class='worked-example'>
<h4>Why This Works</h4>
<p>Let's expand and see:</p>
<pre>2³ × 2² = (2 × 2 × 2) × (2 × 2)
        = 2 × 2 × 2 × 2 × 2
        = 2⁵</pre>
<p>We started with 3 factors of 2, then 2 more factors of 2, giving us 5 total.</p>
<p>So: 3 + 2 = 5 ✓</p>
</div>

<div class='success-box'>
<h4>Examples</h4>
<p>\\(x^4 \\times x^3 = x^{4+3} = x^7\\)</p>
<p>\\(10^2 \\times 10^5 = 10^{2+5} = 10^7\\)</p>
<p>\\(a^2 \\times a^2 \\times a^3 = a^{2+2+3} = a^7\\)</p>
</div>

<p><strong>Visual Representation:</strong></p>
<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg" class="formula-box">
  <text x="20" y="30" class="idx-text" style="font-size:16px;">2³ × 2²</text>

  <!-- First group of 2s -->
  <circle cx="30" cy="70" r="6" fill='#79c0ff'/>
  <circle cx="50" cy="70" r="6" fill='#79c0ff'/>
  <circle cx="70" cy="70" r="6" fill='#79c0ff'/>
  <text x="20" y="100" class="idx-label">3 factors</text>

  <!-- Second group of 2s -->
  <circle cx="110" cy="70" r="6" fill='#79c0ff'/>
  <circle cx="130" cy="70" r="6" fill='#79c0ff'/>
  <text x="100" y="100" class="idx-label">2 factors</text>

  <!-- Arrow -->
  <path d="M 200 70 L 260 70" stroke='#30363d' stroke-width="2" fill='none' marker-end="url(#arrowhead)"/>
  <text x="210" y="55" class="idx-text" style="font-size:12px;">add</text>

  <!-- Result -->
  <circle cx="300" cy="70" r="6" fill='#7ee787'/>
  <circle cx="320" cy="70" r="6" fill='#7ee787'/>
  <circle cx="340" cy="70" r="6" fill='#7ee787'/>
  <circle cx="360" cy="70" r="6" fill='#7ee787'/>
  <circle cx="380" cy="70" r="6" fill='#7ee787'/>
  <text x="290" y="100" class="idx-text" style="font-size: 14px">= 2⁵</text>

  <text x="280" y="145" class="idx-text" style="font-size:12px;">Total: 3 + 2 = 5 factors of 2</text>

  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill='#30363d'/>
    </marker>
  </defs>
</svg>
"""
    },
    {
        "title": "Law 2: Dividing Powers (Same Base)",
        "body": """<div class='concept-box'>
<p><strong>When dividing numbers with the same base, subtract the indices.</strong></p>
<p>$$a^m \\div a^n = a^{m-n}$$</p>
</div>

<div class='worked-example'>
<h4>Why This Works</h4>
<p>Let's expand and simplify:</p>
<pre>2⁵ ÷ 2² = (2 × 2 × 2 × 2 × 2) ÷ (2 × 2)
        = (2 × 2 × 2 × 2 × 2)/(2 × 2)
        = 2 × 2 × 2     [the 2 × 2 cancel out]
        = 2³</pre>
<p>We started with 5 factors of 2, removed 2 of them, leaving 3.</p>
<p>So: 5 - 2 = 3 ✓</p>
</div>

<div class='success-box'>
<h4>Examples</h4>
<p>\\(x^7 \\div x^4 = x^{7-4} = x^3\\)</p>
<p>\\(10^8 \\div 10^3 = 10^{8-3} = 10^5\\)</p>
<p>\\(\\frac{a^6}{a^2} = a^{6-2} = a^4\\)</p>
</div>

<p><strong>Key Point:</strong> Division can be written as a fraction, and the rule works the same way.</p>
<p>\\(\\frac{a^m}{a^n} = a^m \\div a^n = a^{m-n}\\)</p>
"""
    },
    {
        "title": "Law 3: Power of a Power",
        "body": """<div class='concept-box'>
<p><strong>When raising a power to a power, multiply the indices.</strong></p>
<p>$$(a^m)^n = a^{mn}$$</p>
</div>

<div class='worked-example'>
<h4>Why This Works</h4>
<p>Method 1 - Using multiplication law:</p>
<pre>(2³)² = 2³ × 2³
      = 2³⁺³
      = 2⁶
      = 64</pre>
<p>Method 2 - Expanding fully:</p>
<pre>(2³)² means "2³ multiplied by itself"
     = (2 × 2 × 2) × (2 × 2 × 2)
     = 2 × 2 × 2 × 2 × 2 × 2
     = 2⁶</pre>
<p>We have 3 factors, repeated 2 times: 3 × 2 = 6 ✓</p>
</div>

<div class='success-box'>
<h4>Examples</h4>
<p>\\((3^2)^4 = 3^{2 \\times 4} = 3^8\\)</p>
<p>\\((a^5)^3 = a^{5 \\times 3} = a^{15}\\)</p>
<p>\\((x^{-2})^3 = x^{-2 \\times 3} = x^{-6}\\)</p>
</div>

<div class='warning-box'>
<h4>Common Mistake</h4>
<p><strong>Don't add!</strong> (a²)³ ≠ a⁵</p>
<p><strong>Do multiply!</strong> (a²)³ = a²ˣ³ = a⁶</p>
</div>
"""
    },
    {
        "title": "Combining Multiple Laws",
        "body": """<div class='worked-example'>
<h4>Complex Example 1</h4>
<p>Simplify: \\((2^4 \\times 2^3) \\div 2^5\\)</p>
<p><strong>Step 1:</strong> Multiply powers with same base (add indices)</p>
<p style="margin-left:20px;">\\(2^4 \\times 2^3 = 2^{4+3} = 2^7\\)</p>
<p><strong>Step 2:</strong> Divide (subtract indices)</p>
<p style="margin-left:20px;">\\(2^7 \\div 2^5 = 2^{7-5} = 2^2 = 4\\)</p>
</div>

<div class='worked-example'>
<h4>Complex Example 2</h4>
<p>Simplify: \\((3^2)^3 \\times 3^1\\)</p>
<p><strong>Step 1:</strong> Power of a power (multiply indices)</p>
<p style="margin-left:20px;">\\((3^2)^3 = 3^{2 \\times 3} = 3^6\\)</p>
<p><strong>Step 2:</strong> Multiply (add indices)</p>
<p style="margin-left:20px;">\\(3^6 \\times 3^1 = 3^{6+1} = 3^7 = 2187\\)</p>
</div>

<div class='worked-example'>
<h4>With Different Bases</h4>
<p>Simplify: \\(a^5 \\times b^3 \\times a^2 \\div b\\)</p>
<p><strong>Step 1:</strong> Group like bases</p>
<p style="margin-left:20px;">\\(= (a^5 \\times a^2) \\times (b^3 \\div b)\\)</p>
<p><strong>Step 2:</strong> Apply laws to each group</p>
<p style="margin-left:20px;">\\(= a^{5+2} \\times b^{3-1}\\)</p>
<p><strong>Step 3:</strong> Simplify</p>
<p style="margin-left:20px;">\\(= a^7 \\times b^2 = a^7b^2\\)</p>
</div>

<div class='success-box'>
<h4>Summary of Laws So Far</h4>
<ul>
<li>\\(a^m \\times a^n = a^{m+n}\\) (Multiply: Add)</li>
<li>\\(a^m \\div a^n = a^{m-n}\\) (Divide: Subtract)</li>
<li>\\((a^m)^n = a^{mn}\\) (Power of Power: Multiply)</li>
</ul>
</div>
"""
    }
]
