TITLE = "Venn Diagrams: Visualizing Set Relationships"

SECTIONS = [
    {
        "title": "Two-Set Venn Diagrams: The Basics",
        "body": """
<h3>Why Venn Diagrams?</h3>
<p>Venn diagrams translate abstract set operations into visual regions. This helps us understand and count elements systematically.</p>

<div class="concept-box">
<p><strong>Core Principle:</strong> Each region represents a different combination of membership.</p>
</div>

<h3>Two Sets: A and B</h3>
<p>With two sets, there are 4 distinct regions:</p>

<svg viewBox="-15 -15 530 330" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 400px; margin: 20px auto; display: block;" font-family="sans-serif">
  <!-- Background -->
  <rect x="0" y="0" width="500" height="300" rx="4" fill="#0d1117" stroke="#30363d" stroke-width="1"/>

  <!-- Circle A -->
  <circle cx="185" cy="150" r="100" fill="rgba(79, 142, 247, 0.2)" stroke="#4f8ef7" stroke-width="2"/>

  <!-- Circle B -->
  <circle cx="315" cy="150" r="100" fill="rgba(79, 142, 247, 0.2)" stroke="#4f8ef7" stroke-width="2"/>

  <!-- Set labels -->
  <text x="120" y="80" font-size="18" fill="currentColor" font-weight="bold">A</text>
  <text x="370" y="80" font-size="18" fill="currentColor" font-weight="bold">B</text>

  <!-- Region labels -->
  <text x="130" y="155" font-size="12" fill="currentColor" opacity="0.6" text-anchor="middle">Only A</text>
  <text x="250" y="155" font-size="12" fill="currentColor" opacity="0.6" text-anchor="middle">A ∩ B</text>
  <text x="370" y="155" font-size="12" fill="currentColor" opacity="0.6" text-anchor="middle">Only B</text>
  <text x="250" y="280" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">Outside (neither)</text>
</svg>

<div class="formula-box">
<p><strong>Region 1:</strong> Left circle only = A \\ B (in A, not in B)</p>
<p style="margin-top: 8px;"><strong>Region 2:</strong> Overlap = A ∩ B (in both)</p>
<p style="margin-top: 8px;"><strong>Region 3:</strong> Right circle only = B \\ A (in B, not in A)</p>
<p style="margin-top: 8px;"><strong>Region 4:</strong> Outside both = (A ∪ B)' (neither in A nor B)</p>
</div>

<div class="worked-example">
<h4>Example 1: Reading a Two-Set Diagram</h4>
<p><strong>Scenario:</strong> A class of 30 students where:</p>
<p>• 15 study Math</p>
<p>• 10 study Physics</p>
<p>• 5 study both</p>
<p style="margin-top: 12px;"><strong>Regions:</strong></p>
<p style="font-family: monospace;">​Math only: 15 - 5 = 10</p>
<p style="font-family: monospace;">​Both: 5</p>
<p style="font-family: monospace;">​Physics only: 10 - 5 = 5</p>
<p style="font-family: monospace;">​Neither: 30 - (10 + 5 + 5) = 10</p>
<p style="margin-top: 8px;" class="text-muted-note"><strong>How many study at least one?</strong> 10 + 5 + 5 = 20</p>
</div>

<h3>Key Property: The Regions Must Add Up</h3>
<p style="padding: 10px; border-radius: 4px; margin: 12px 0">All four regions together = the universal set U</p>
<p style="font-family: monospace; margin-top: 8px;">​(A \\ B) + (A ∩ B) + (B \\ A) + (A ∪ B)' = |U|</p>
"""
    },
    {
        "title": "Three-Set Venn Diagrams: Complex Problems",
        "body": """
<h3>Three Sets: A, B, and C</h3>
<p>Three overlapping circles create 8 distinct regions. This is where Venn diagrams show their power.</p>

<svg viewBox="-15 -15 530 430" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 450px; margin: 20px auto; display: block;" font-family="sans-serif">
  <!-- Background -->
  <rect x="0" y="0" width="500" height="400" rx="4" fill="#0d1117" stroke="#30363d" stroke-width="1"/>

  <!-- Circle A (top-left) -->
  <circle cx="190" cy="170" r="110" fill="rgba(79, 142, 247, 0.15)" stroke="#4f8ef7" stroke-width="2"/>

  <!-- Circle B (top-right) -->
  <circle cx="310" cy="170" r="110" fill="rgba(79, 142, 247, 0.15)" stroke="#4f8ef7" stroke-width="2"/>

  <!-- Circle C (bottom-centre) -->
  <circle cx="250" cy="270" r="110" fill="rgba(79, 142, 247, 0.15)" stroke="#4f8ef7" stroke-width="2"/>

  <!-- Set labels -->
  <text x="110" y="90" font-size="18" fill="currentColor" font-weight="bold">A</text>
  <text x="380" y="90" font-size="18" fill="currentColor" font-weight="bold">B</text>
  <text x="250" y="390" font-size="18" fill="currentColor" font-weight="bold" text-anchor="middle">C</text>

  <!-- Region labels -->
  <text x="130" y="155" font-size="10" fill="currentColor" opacity="0.6" text-anchor="middle">Only A</text>
  <text x="370" y="155" font-size="10" fill="currentColor" opacity="0.6" text-anchor="middle">Only B</text>
  <text x="250" y="340" font-size="10" fill="currentColor" opacity="0.6" text-anchor="middle">Only C</text>
  <text x="190" y="265" font-size="9" fill="currentColor" opacity="0.6" text-anchor="middle">A ∩ C</text>
  <text x="310" y="265" font-size="9" fill="currentColor" opacity="0.6" text-anchor="middle">B ∩ C</text>
  <text x="250" y="140" font-size="9" fill="currentColor" opacity="0.6" text-anchor="middle">A ∩ B</text>
  <text x="250" y="220" font-size="10" fill="currentColor" opacity="0.6" text-anchor="middle" font-weight="bold">A ∩ B ∩ C</text>
</svg>

<div class="concept-box">
<p><strong>The 8 Regions:</strong></p>
<ol style="font-size: 0.95em;">
  <li>Only A: A ∩ B' ∩ C'</li>
  <li>Only B: A' ∩ B ∩ C'</li>
  <li>Only C: A' ∩ B' ∩ C</li>
  <li>A and B only: A ∩ B ∩ C'</li>
  <li>A and C only: A ∩ B' ∩ C</li>
  <li>B and C only: A' ∩ B ∩ C</li>
  <li>All three: A ∩ B ∩ C</li>
  <li>None: (A ∪ B ∪ C)'</li>
</ol>
</div>

<div class="worked-example">
<h4>Example 2: The Classic Three-Subject Problem</h4>
<p><strong>In a class of 40 students:</strong></p>
<p>• 20 study Math (M)</p>
<p>• 15 study Physics (P)</p>
<p>• 12 study Chemistry (C)</p>
<p>• 7 study M and P</p>
<p>• 6 study M and C</p>
<p>• 5 study P and C</p>
<p>• 3 study all three</p>
<p style="margin-top: 12px;"><strong>Find: Students who study exactly one subject</strong></p>
<p style="margin-top: 12px;"><strong>Solution Strategy:</strong> Work inward from the universal set.</p>
<p style="margin-top: 8px;"><strong>Step 1:</strong> Start with "all three" = 3</p>
<p style="margin-top: 8px;"><strong>Step 2:</strong> Find "exactly two":</p>
<p style="font-family: monospace; margin: 4px 0 4px 20px;">M∩P only: 7 - 3 = 4</p>
<p style="font-family: monospace; margin: 4px 0 4px 20px;">M∩C only: 6 - 3 = 3</p>
<p style="font-family: monospace; margin: 4px 0 4px 20px;">P∩C only: 5 - 3 = 2</p>
<p style="margin-top: 8px;"><strong>Step 3:</strong> Find "exactly one":</p>
<p style="font-family: monospace; margin: 4px 0 4px 20px;">Math only: 20 - (4 + 3 + 3) = 10</p>
<p style="font-family: monospace; margin: 4px 0 4px 20px;">Physics only: 15 - (4 + 2 + 3) = 6</p>
<p style="font-family: monospace; margin: 4px 0 4px 20px;">Chemistry only: 12 - (3 + 2 + 3) = 4</p>
<p style="margin-top: 12px;"><strong>Answer:</strong> 10 + 6 + 4 = 20 students study exactly one subject</p>
<p style="margin-top: 8px;" class="text-muted-note"><strong>Verification:</strong> (10 + 6 + 4) + (4 + 3 + 2) + 3 + (40 - 32) = 20 + 9 + 3 + 8 = 40 ✓</p>
</div>

<h3>The General Strategy for Venn Diagram Problems</h3>
<p class="formula-box">
<strong>1.</strong> Identify all regions (draw the diagram)<br/>
<strong>2.</strong> Fill in the "innermost" (most-intersected) region first<br/>
<strong>3.</strong> Work outward to "exactly two" overlaps<br/>
<strong>4.</strong> Calculate "only one set" regions<br/>
<strong>5.</strong> Find elements outside all sets (if total is given)<br/>
<strong>6.</strong> Verify: all regions sum to the universal set
</p>
"""
    },
    {
        "title": "De Morgan's Laws and Visual Proof",
        "body": """
<h3>Seeing De Morgan's Laws in Venn Diagrams</h3>
<p>Visual proof makes abstract laws concrete.</p>

<h4>De Morgan's First Law: (A ∪ B)' = A' ∩ B'</h4>

<p style="font-size: 0.9em; margin: 12px 0"><strong>Left side: (A ∪ B)'</strong> — Everything NOT in the union</p>

<svg viewBox="-15 -15 310 210" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 300px; margin: 10px auto; display: block;" font-family="sans-serif">
  <rect x="0" y="0" width="280" height="180" rx="4" fill="#0d1117" stroke="#30363d" stroke-width="1"/>
  <!-- Universal set shaded -->
  <rect x="10" y="10" width="260" height="160" rx="4" fill="rgba(79, 142, 247, 0.2)" stroke="#30363d" stroke-width="1"/>
  <!-- Circles cut out (unshaded) -->
  <circle cx="100" cy="90" r="50" fill="#0d1117" stroke="#4f8ef7" stroke-width="2"/>
  <circle cx="180" cy="90" r="50" fill="#0d1117" stroke="#4f8ef7" stroke-width="2"/>
  <text x="140" y="30" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">(A ∪ B)' shaded</text>
  <text x="75" y="95" font-size="12" fill="currentColor" text-anchor="middle">A</text>
  <text x="205" y="95" font-size="12" fill="currentColor" text-anchor="middle">B</text>
</svg>

<p style="font-size: 0.9em; margin: 12px 0"><strong>Right side: A' ∩ B'</strong> — Elements in both complements</p>

<svg viewBox="-15 -15 310 210" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 300px; margin: 10px auto; display: block;" font-family="sans-serif">
  <rect x="0" y="0" width="280" height="180" rx="4" fill="#0d1117" stroke="#30363d" stroke-width="1"/>
  <!-- Universal set shaded -->
  <rect x="10" y="10" width="260" height="160" rx="4" fill="rgba(79, 142, 247, 0.2)" stroke="#30363d" stroke-width="1"/>
  <!-- Circles cut out (unshaded) -->
  <circle cx="100" cy="90" r="50" fill="#0d1117" stroke="#4f8ef7" stroke-width="2"/>
  <circle cx="180" cy="90" r="50" fill="#0d1117" stroke="#4f8ef7" stroke-width="2"/>
  <text x="140" y="30" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">A' ∩ B' shaded</text>
  <text x="75" y="95" font-size="12" fill="currentColor" text-anchor="middle">A</text>
  <text x="205" y="95" font-size="12" fill="currentColor" text-anchor="middle">B</text>
</svg>

<p style="padding: 10px; border-radius: 4px; margin-top: 12px"><strong>Key insight:</strong> Both diagrams shade the same region—outside both circles. This proves (A ∪ B)' = A' ∩ B'</p>

<h4>De Morgan's Second Law: (A ∩ B)' = A' ∪ B'</h4>

<p style="font-size: 0.9em; margin: 12px 0"><strong>Left side: (A ∩ B)'</strong> — Everything NOT in the overlap</p>

<svg viewBox="-15 -15 310 210" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 300px; margin: 10px auto; display: block;" font-family="sans-serif">
  <defs>
    <!-- Clip to show only the overlap region -->
    <clipPath id="dm2-overlap">
      <circle cx="100" cy="90" r="50"/>
    </clipPath>
  </defs>
  <rect x="0" y="0" width="280" height="180" rx="4" fill="#0d1117" stroke="#30363d" stroke-width="1"/>
  <!-- Universal set shaded = (A ∩ B)' -->
  <rect x="10" y="10" width="260" height="160" rx="4" fill="rgba(79, 142, 247, 0.2)" stroke="#30363d" stroke-width="1"/>
  <!-- Circles shaded (part of complement) -->
  <circle cx="100" cy="90" r="50" fill="rgba(79, 142, 247, 0.2)" stroke="#4f8ef7" stroke-width="2"/>
  <circle cx="180" cy="90" r="50" fill="rgba(79, 142, 247, 0.2)" stroke="#4f8ef7" stroke-width="2"/>
  <!-- Unshade the overlap (the only region NOT in the complement) -->
  <circle cx="180" cy="90" r="50" clip-path="url(#dm2-overlap)" fill="#0d1117" stroke="none"/>
  <!-- Redraw circle strokes on top -->
  <circle cx="100" cy="90" r="50" fill="none" stroke="#4f8ef7" stroke-width="2"/>
  <circle cx="180" cy="90" r="50" fill="none" stroke="#4f8ef7" stroke-width="2"/>
  <text x="140" y="30" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">(A ∩ B)' shaded</text>
  <text x="75" y="95" font-size="12" fill="currentColor" text-anchor="middle">A</text>
  <text x="205" y="95" font-size="12" fill="currentColor" text-anchor="middle">B</text>
</svg>

<p style="font-size: 0.9em; margin: 12px 0"><strong>Right side: A' ∪ B'</strong> — Everything outside A OR outside B</p>

<svg viewBox="-15 -15 310 210" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 300px; margin: 10px auto; display: block;" font-family="sans-serif">
  <defs>
    <clipPath id="dm2b-overlap">
      <circle cx="100" cy="90" r="50"/>
    </clipPath>
  </defs>
  <rect x="0" y="0" width="280" height="180" rx="4" fill="#0d1117" stroke="#30363d" stroke-width="1"/>
  <!-- Universal set shaded -->
  <rect x="10" y="10" width="260" height="160" rx="4" fill="rgba(79, 142, 247, 0.2)" stroke="#30363d" stroke-width="1"/>
  <!-- Circles shaded -->
  <circle cx="100" cy="90" r="50" fill="rgba(79, 142, 247, 0.2)" stroke="#4f8ef7" stroke-width="2"/>
  <circle cx="180" cy="90" r="50" fill="rgba(79, 142, 247, 0.2)" stroke="#4f8ef7" stroke-width="2"/>
  <!-- Unshade the overlap -->
  <circle cx="180" cy="90" r="50" clip-path="url(#dm2b-overlap)" fill="#0d1117" stroke="none"/>
  <!-- Redraw strokes -->
  <circle cx="100" cy="90" r="50" fill="none" stroke="#4f8ef7" stroke-width="2"/>
  <circle cx="180" cy="90" r="50" fill="none" stroke="#4f8ef7" stroke-width="2"/>
  <text x="140" y="30" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">A' ∪ B' shaded</text>
  <text x="75" y="95" font-size="12" fill="currentColor" text-anchor="middle">A</text>
  <text x="205" y="95" font-size="12" fill="currentColor" text-anchor="middle">B</text>
</svg>

<p style="padding: 10px; border-radius: 4px; margin-top: 12px"><strong>Again:</strong> Both diagrams shade the same regions—the complement of the overlap. This proves (A ∩ B)' = A' ∪ B'</p>

<div class="success-box">
<p><strong>Why This Matters:</strong> De Morgan's laws are fundamental in computer science, circuit design, and logic. Understanding them visually makes them intuitive, not just memorized rules.</p>
</div>
"""
    }
]
