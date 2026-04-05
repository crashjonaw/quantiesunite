TITLE = "What are Indices (Exponents)?"

SECTIONS = [
    {
        "title": "Shorthand for Repeated Multiplication",
        "body": """<div class='concept-box'>
<p><strong>Indices</strong> (or <strong>exponents</strong>) are a shorthand way of writing repeated multiplication.</p>
<p>Instead of writing 2 × 2 × 2, we write <strong>2³</strong> (read as "2 to the power of 3" or "2 cubed").</p>
</div>

<div class='worked-example'>
<h4>The Problem</h4>
<p>Writing 2 × 2 × 2 × 2 × 2 is tedious. How can we make this clearer?</p>
<h4>The Solution</h4>
<p>Count the repetitions (5 times) and write: 2⁵</p>
<p>This notation unlocks powerful rules for simplifying.</p>
</div>

<p><strong>Visual Representation:</strong></p>
<svg width="100%" viewBox="0 0 480 180" style="max-width:500px;">
  <defs>
    <marker id="arrowhead-idx" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill='#4169E1'/>
    </marker>
  </defs>

  <!-- Left: expanded form -->
  <text x="20" y="28" font-size="13" font-weight="bold" fill="currentColor">Expanded Form</text>
  <rect x="15" y="40" width="160" height="50" rx="8" fill="rgba(65,105,225,0.1)" stroke="#4169E1" stroke-width="1.5"/>
  <text x="95" y="70" text-anchor="middle" font-size="18" font-weight="bold" fill="currentColor">2 × 2 × 2 = 8</text>
  <text x="95" y="115" text-anchor="middle" font-size="12" fill="currentColor">3 groups of 2</text>
  <circle cx="55" cy="115" r="6" fill="#4169E180" stroke="#4169E1" stroke-width="1.5"/>
  <circle cx="95" cy="115" r="6" fill="#4169E180" stroke="#4169E1" stroke-width="1.5"/>
  <circle cx="135" cy="115" r="6" fill="#4169E180" stroke="#4169E1" stroke-width="1.5"/>
  <text x="95" y="145" text-anchor="middle" font-size="11" fill="currentColor">3 groups of 2</text>

  <!-- Arrow -->
  <line x1="195" y1="65" x2="245" y2="65" stroke="#4169E1" stroke-width="2" marker-end="url(#arrowhead-idx)"/>
  <text x="220" y="55" text-anchor="middle" font-size="11" fill="currentColor">convert</text>

  <!-- Right: index form -->
  <text x="270" y="28" font-size="13" font-weight="bold" fill="currentColor">Index Form</text>
  <rect x="265" y="40" width="190" height="50" rx="8" fill="rgba(34,197,94,0.1)" stroke="#22c55e" stroke-width="1.5"/>
  <text x="290" y="72" font-size="26" font-weight="bold" fill="currentColor">2³</text>
  <text x="330" y="72" font-size="22" fill="currentColor">=</text>
  <text x="360" y="72" font-size="26" font-weight="bold" fill="#22c55e">8</text>

  <text x="285" y="115" font-size="12" fill="#4169E1" font-weight="600">base = 2</text>
  <text x="285" y="135" font-size="12" fill="#f59e0b" font-weight="600">index = 3 (how many times)</text>

  <!-- Annotation lines -->
  <line x1="295" y1="78" x2="295" y2="105" stroke="#4169E1" stroke-width="1" stroke-dasharray="3"/>
  <line x1="308" y1="48" x2="308" y2="105" stroke="#f59e0b" stroke-width="1" stroke-dasharray="3"/>
</svg>
"""
    },
    {
        "title": "Parts of an Index",
        "body": """<div class='concept-box'>
<p>When we write <strong>2³</strong>, there are two key parts:</p>
</div>

<div class='worked-example'>
<h4>In the expression 2³:</h4>
<ul>
<li><strong>Base (2):</strong> The number being multiplied</li>
<li><strong>Index or Exponent (3):</strong> The small number showing how many times the base is multiplied by itself</li>
</ul>
</div>

<p><strong>More Examples:</strong></p>

<svg width="100%" viewBox="0 0 460 190" style="max-width:500px;">
  <!-- Example 1 -->
  <rect x="10" y="8" width="440" height="75" rx="8" fill="rgba(65,105,225,0.06)" stroke="rgba(65,105,225,0.2)" stroke-width="1"/>
  <text x="20" y="30" font-size="11" font-weight="600" fill="#4169E1">Example 1</text>
  <text x="20" y="60" font-size="22" font-weight="bold" fill="currentColor">3⁴</text>
  <text x="65" y="60" font-size="16" fill="currentColor">=</text>
  <text x="90" y="60" font-size="15" fill="currentColor">3 × 3 × 3 × 3</text>
  <text x="270" y="60" font-size="16" fill="currentColor">=</text>
  <text x="295" y="60" font-size="22" font-weight="bold" fill="#22c55e">81</text>
  <text x="350" y="60" font-size="11" fill="currentColor">base=3, index=4</text>

  <!-- Example 2 -->
  <rect x="10" y="98" width="440" height="75" rx="8" fill="rgba(245,158,11,0.06)" stroke="rgba(245,158,11,0.2)" stroke-width="1"/>
  <text x="20" y="120" font-size="11" font-weight="600" fill="#f59e0b">Example 2</text>
  <text x="20" y="150" font-size="22" font-weight="bold" fill="currentColor">5²</text>
  <text x="65" y="150" font-size="16" fill="currentColor">=</text>
  <text x="90" y="150" font-size="15" fill="currentColor">5 × 5</text>
  <text x="170" y="150" font-size="16" fill="currentColor">=</text>
  <text x="195" y="150" font-size="22" font-weight="bold" fill="#22c55e">25</text>
  <text x="250" y="150" font-size="11" fill="currentColor">(read as "5 squared")</text>
</svg>
"""
    },
    {
        "title": "Special Index Values",
        "body": """<div class='concept-box'>
<p>There are two important special cases for indices:</p>
</div>

<div class='success-box'>
<h4>Index = 1</h4>
<p>Any number to the power 1 equals itself:</p>
<p style="margin-left:20px;">\\(5^1 = 5\\)</p>
<p style="margin-left:20px;">\\(a^1 = a\\)</p>
</div>

<div class='warning-box'>
<h4>Index = 0</h4>
<p>Any <strong>non-zero</strong> number to the power 0 equals 1:</p>
<p style="margin-left:20px;">\\(5^0 = 1\\)</p>
<p style="margin-left:20px;">\\(a^0 = 1\\)</p>
<p style="margin-left:20px;">\\((100)^0 = 1\\)</p>
<p style="font-size:12px; margin-top:10px;">We'll explain why \\(a^0 = 1\\) makes sense in the next concept!</p>
</div>

<p><strong>Quick Check:</strong></p>
<table style="width:100%; border-collapse:collapse; margin-top:15px;">
<tr >
  <td style="padding: 10px;">Expression</td>
  <td style="padding: 10px;">Answer</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">\\(7^1\\)</td>
  <td style="padding: 10px; color: var(--success);">7</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">\\(7^0\\)</td>
  <td style="padding: 10px; color: var(--success);">1</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">\\(x^1\\)</td>
  <td style="padding: 10px; color: var(--success);">x</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">\\(x^0\\)</td>
  <td style="padding: 10px; color: var(--success);">1</td>
</tr>
</table>
"""
    },
    {
        "title": "Why Indices Are Useful",
        "body": """<div class='concept-box'>
<p>Indices aren't just shorthand—they're essential tools in mathematics and science.</p>
</div>

<div class='success-box'>
<h4>Simplifies Large Calculations</h4>
<p>Imagine writing this without indices:</p>
<p style="margin-left: 20px; font-family: monospace">2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2</p>
<p>Instead, we write simply: \\(2^{10}\\)</p>
</div>

<div class='success-box'>
<h4>Reveals Patterns</h4>
<p>Powers of 2 show exponential growth:</p>
<p>\\(2^1 = 2\\), \\(2^2 = 4\\), \\(2^3 = 8\\), \\(2^4 = 16\\), \\(2^5 = 32\\), \\(2^6 = 64\\)</p>
<p>The pattern is clear and powerful!</p>
</div>

<div class='success-box'>
<h4>Essential in Science</h4>
<ul>
<li><strong>Very large numbers:</strong> Distance to stars = \\(4.37 \\times 10^{16}\\) meters</li>
<li><strong>Very small numbers:</strong> Width of atom = \\(1 \\times 10^{-10}\\) meters</li>
<li><strong>Biology:</strong> Bacteria count, viral spread</li>
<li><strong>Physics:</strong> Speed of light, energy calculations</li>
</ul>
</div>

<p><strong>Example Comparison:</strong></p>
<table style="width:100%; border-collapse:collapse; margin-top:15px;">
<tr >
  <td style="padding: 10px;">Without Indices</td>
  <td style="padding: 10px;">With Indices</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">4,500,000,000,000 meters</td>
  <td style="padding: 10px; color: var(--success);">\\(4.5 \\times 10^{12}\\) meters</td>
</tr>
<tr class="worked-example">
  <td style="padding: 10px;">0.00000000032 meters</td>
  <td style="padding: 10px; color: var(--success);">\\(3.2 \\times 10^{-10}\\) meters</td>
</tr>
</table>
"""
    }
]
