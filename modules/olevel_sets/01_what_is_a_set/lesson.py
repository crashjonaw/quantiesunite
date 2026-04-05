TITLE = "What is a Set? Foundations and Notation"

SECTIONS = [
    {
        "title": "Understanding Sets from First Principles",
        "body": """
<div class="concept-box">
<h3>Core Idea: A Set is a Container of Distinct Objects</h3>
<p>Imagine a bag containing distinct marbles. A <strong>set</strong> is a mathematical collection that works similarly—it contains distinct objects called <strong>elements</strong>, and we don't care about the order.</p>
<p><strong>Why does this matter?</strong> Sets are the foundation of modern mathematics. Everything in mathematics—numbers, functions, spaces—is ultimately built from sets.</p>
</div>

<h3>Formal Definition</h3>
<p>A <strong>set</strong> is a well-defined collection of distinct objects (elements). "Well-defined" means we can always determine whether something belongs to the set or not.</p>

<div class="worked-example">
<h4>Example 1: What is a Well-Defined Set?</h4>
<p><strong>Good sets:</strong></p>
<ul>
  <li>{1, 2, 3} — clearly defined elements</li>
  <li>{x | x is an even integer} — clear rule (can determine if any number satisfies it)</li>
  <li>The set of vowels in English: {a, e, i, o, u}</li>
</ul>
<p><strong>Not well-defined:</strong></p>
<ul>
  <li>{large numbers} — what counts as "large"? Subjective.</li>
  <li>{beautiful colors} — subjective, no clear rule</li>
</ul>
<p><strong>Why the distinction?</strong> Mathematics requires precision. For a set to be useful, we must always agree on whether something is in it.</p>
</div>

<h3>Notation: How We Write Sets</h3>
<p>Two main ways to describe a set:</p>

<div class="formula-box">
<p><strong>1. Roster (List) Notation:</strong> List all elements</p>
<p style="font-family: monospace; margin: 8px 0;">A = {1, 2, 3, 4, 5}</p>
<p><strong>2. Set-Builder Notation:</strong> Describe by property</p>
<p style="font-family: monospace; margin: 8px 0;">A = {x | x ∈ ℤ, 1 ≤ x ≤ 5}</p>
<p style="font-size: 0.9em">Read as: "A is the set of x where x is an integer and x is between 1 and 5 inclusive"</p>
</div>

<div class="worked-example">
<h4>Example 2: Notation Conversion</h4>
<p><strong>Roster form:</strong> E = {2, 4, 6, 8, 10}</p>
<p><strong>Set-builder form:</strong> E = {x | x is an even integer, 1 ≤ x ≤ 10}</p>
<p><strong>Why both?</strong> Roster notation is concrete and easy to see. Set-builder notation shows the <em>pattern</em> and works for infinite sets.</p>
</div>
"""
    },
    {
        "title": "Membership and Key Concepts",
        "body": """
<h3>Membership: The ∈ Symbol</h3>
<p>The symbol ∈ means "is an element of" or "belongs to".</p>

<div class="formula-box">
<p style="margin: 0;"><span style="font-family: monospace;">3 ∈ {1, 2, 3, 4}</span> reads as "3 is in the set {1, 2, 3, 4}" — <strong>TRUE</strong></p>
<p style="margin: 8px 0 0 0;"><span style="font-family: monospace;">5 ∈ {1, 2, 3, 4}</span> reads as "5 is in the set {1, 2, 3, 4}" — <strong>FALSE</strong></p>
<p style="margin: 8px 0 0 0;"><span style="font-family: monospace;">5 ∉ {1, 2, 3, 4}</span> the symbol ∉ means "is NOT an element of"</p>
</div>

<h3>Important Special Sets</h3>

<div class="concept-box">
<h4>The Empty Set: ∅ (or {})</h4>
<p>The set with <strong>no elements</strong>. This might seem odd—why have a set with nothing?</p>
<p><strong>Why it matters:</strong> Imagine solving "Find all x where x² = -1 and x is real". The answer is the empty set—there are no real solutions. The empty set lets us represent "no solution" mathematically.</p>
<p class="text-muted-note">∅ = {} — both notations mean the same thing</p>
</div>

<h3>Subsets: The ⊆ Symbol</h3>
<p>A = {1, 2} and B = {1, 2, 3}. Set A is a <strong>subset</strong> of B, written A ⊆ B.</p>
<p><strong>Definition:</strong> A ⊆ B means every element of A is also in B.</p>

<div class="worked-example">
<h4>Example 3: Subsets vs Elements</h4>
<p><strong>Is 2 ⊆ {1, 2, 3}?</strong> NO — 2 is an element (use ∈), not a subset.</p>
<p><strong>Is {2} ⊆ {1, 2, 3}?</strong> YES — the set containing just 2 is a subset.</p>
<p><strong>Is {1, 2} ⊆ {1, 2, 3}?</strong> YES — every element of {1, 2} is in {1, 2, 3}.</p>
<p style="margin-top: 8px;" class="text-muted-note"><strong>Key insight:</strong> ⊆ compares sets to sets. ∈ compares elements to sets.</p>
</div>

<h4>Proper Subsets: ⊂</h4>
<p>A ⊂ B means A ⊆ B AND A ≠ B (strict subset, doesn't include itself).</p>
<p style="font-family: monospace;">​{1, 2} ⊂ {1, 2, 3} ✓ (proper subset)</p>
<p style="font-family: monospace;">​{1, 2, 3} ⊂ {1, 2, 3} ✗ (not proper, same set)</p>
"""
    },
    {
        "title": "Number Sets and Cardinality",
        "body": """
<h3>The Number System Hierarchy</h3>
<p>Different types of numbers form sets, nested within each other like Russian dolls.</p>

<div class="formula-box">
<p><strong>ℕ (Natural Numbers):</strong> {0, 1, 2, 3, ...} or {1, 2, 3, ...}</p>
<p style="margin-top: 8px;"><strong>ℤ (Integers):</strong> {..., -2, -1, 0, 1, 2, ...}</p>
<p style="margin-top: 8px;"><strong>ℚ (Rationals):</strong> All fractions p/q where p, q ∈ ℤ and q ≠ 0</p>
<p style="margin-top: 8px;"><strong>ℝ (Real Numbers):</strong> All points on the number line (rationals + irrationals like π, √2)</p>
<p style="margin-top: 8px;"><strong>ℂ (Complex Numbers):</strong> {a + bi | a, b ∈ ℝ, i² = -1}</p>
</div>

<p style="margin-top: 12px">Relationship: ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ (each is a proper subset of the next)</p>

<div class="worked-example">
<h4>Example 4: Which Set Does It Belong To?</h4>
<p><strong>-3:</strong> ℤ, ℚ, ℝ, ℂ (but not ℕ)</p>
<p><strong>1/2:</strong> ℚ, ℝ, ℂ (but not ℤ or ℕ)</p>
<p><strong>π:</strong> ℝ, ℂ (but not ℚ, ℤ, or ℕ—it's irrational)</p>
<p class="text-muted-note">π is in ℝ because we can place it exactly on the number line, even though we can't write it as a fraction.</p>
</div>

<h3>Cardinality: Size of a Set</h3>
<p>The <strong>cardinality</strong> of a set, written |A|, is the number of elements in the set.</p>

<div class="formula-box">
<p style="margin: 0;"><span style="font-family: monospace;">|{1, 2, 3}| = 3</span></p>
<p style="margin: 8px 0 0 0;"><span style="font-family: monospace;">|∅| = 0</span> (empty set has 0 elements)</p>
<p style="margin: 8px 0 0 0;"><span style="font-family: monospace;">|ℕ| = ∞</span> (infinite)</p>
</div>

<h4>Finite vs Infinite Sets</h4>
<p><strong>Finite:</strong> Can list all elements. {red, blue, green} has cardinality 3.</p>
<p><strong>Infinite:</strong> Never ends. ℕ = {0, 1, 2, 3, ...} is infinite.</p>

<div class="worked-example">
<h4>Example 5: Computing Cardinality</h4>
<p>A = {x | x is a day of the week}</p>
<p>A = {Monday, Tuesday, ..., Sunday}</p>
<p>|A| = 7</p>
</div>
"""
    }
]
