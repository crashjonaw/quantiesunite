SECTIONS = [
    {
        "title": "Sets: Foundation and Notation",
        "body": """
<h3>Axiomatic Definition</h3>
<p>A <strong>set</strong> is a well-defined collection of distinct objects (elements).</p>
<p><strong>Notation:</strong> A = {a, b, c} lists elements; A = {x | P(x)} defines by property P</p>

<h3>Key Definitions</h3>
<ul>
  <li>∈: element belongs to set</li>
  <li>⊆: subset (A ⊆ B if every element of A is in B)</li>
  <li>∪: union (A ∪ B contains elements in A or B)</li>
  <li>∩: intersection (A ∩ B contains elements in both)</li>
  <li>A': complement (elements not in A)</li>
  <li>∅: empty set (no elements)</li>
</ul>

<h3>Number Sets</h3>
<ul>
  <li>ℕ: Natural numbers {0,1,2,3,...} or {1,2,3,...}</li>
  <li>ℤ: Integers {...,-2,-1,0,1,2,...}</li>
  <li>ℚ: Rationals {p/q : p,q ∈ ℤ, q ≠ 0}</li>
  <li>ℝ: Real numbers (all points on number line)</li>
  <li>ℂ: Complex numbers {a + bi}</li>
</ul>

<div class="example-box">
<h4>Example 1: Set Operations</h4>
<p>A = {1, 2, 3, 4}, B = {3, 4, 5, 6}</p>
<p>A ∪ B = {1, 2, 3, 4, 5, 6}</p>
<p>A ∩ B = {3, 4}</p>
<p>A ⊆ ℕ (true), A ⊆ B (false)</p>
</div>
"""
    },
    {
        "title": "Set Operations and Laws",
        "body": """
<h3>Fundamental Laws</h3>
<p><strong>Commutative:</strong> A ∪ B = B ∪ A, A ∩ B = B ∩ A</p>
<p><strong>Associative:</strong> (A ∪ B) ∪ C = A ∪ (B ∪ C)</p>
<p><strong>Distributive:</strong> A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)</p>
<p><strong>De Morgan's Laws:</strong></p>
<ul>
  <li>(A ∪ B)' = A' ∩ B'</li>
  <li>(A ∩ B)' = A' ∪ B'</li>
</ul>

<h3>Cardinality</h3>
<p>|A| = number of elements in set A</p>
<p><strong>For finite sets:</strong> |A ∪ B| = |A| + |B| - |A ∩ B|</p>

<div class="example-box">
<h4>Example 2: Set Difference</h4>
<p>A \\ B (A minus B) = elements in A but not in B</p>
<p>A = {1,2,3,4}, B = {3,4,5}</p>
<p>A \\ B = {1,2}</p>
</div>
"""
    },
    {
        "title": "Venn Diagrams and Logical Representation",
        "body": """
<h3>Venn Diagram Basics</h3>
<p>Venn diagrams visualize set relationships with overlapping circles.</p>

<h3>Application: Two and Three Sets</h3>
<p>With two sets: regions are A∩B, A\\B, B\\A, neither</p>
<p>With three sets: eight regions total</p>

<div class="example-box">
<h4>Example 3: Three-Set Problem</h4>
<p>In a class: 15 study Math, 12 study Physics, 10 study Chemistry</p>
<p>8 study Math and Physics, 7 study Physics and Chemistry, 6 study Math and Chemistry</p>
<p>5 study all three. Find how many study exactly one subject.</p>
<p>By inclusion-exclusion and Venn diagram analysis</p>
</div>
"""
    },
    {
        "title": "Relations and Functions as Sets",
        "body": """
<h3>Cartesian Product</h3>
<p>A × B = {(a,b) : a ∈ A, b ∈ B}</p>
<p>|A × B| = |A| · |B| for finite sets</p>

<h3>Relations</h3>
<p>A relation from A to B is a subset of A × B</p>

<h3>Functions as Relations</h3>
<p>A function f: A → B is a relation where each element of A pairs with exactly one element of B</p>

<div class="example-box">
<h4>Example 4: Relation vs Function</h4>
<p>A = {1, 2}, B = {a, b, c}</p>
<p>Relation: {(1,a), (1,b), (2,c)} ✓</p>
<p>Function: {(1,a), (2,b)} ✓ each element of A has exactly one partner</p>
<p>Not a function: {(1,a), (1,b), (2,c)} ✗ 1 maps to both a and b</p>
</div>
"""
    },
    {
        "title": "Equivalence Relations and Partitions",
        "body": """
<h3>Properties of Relations</h3>
<p><strong>Reflexive:</strong> aRa for all a ∈ A</p>
<p><strong>Symmetric:</strong> If aRb then bRa</p>
<p><strong>Transitive:</strong> If aRb and bRc then aRc</p>

<h3>Equivalence Relations</h3>
<p>Relations that are reflexive, symmetric, and transitive partition the set into equivalence classes</p>

<div class="example-box">
<h4>Example 5: Equivalence Relation</h4>
<p>On integers: a ~ b if a ≡ b (mod 3)</p>
<p>Equivalence classes: {... -3, 0, 3, 6, ...}, {... -2, 1, 4, ...}, {... -1, 2, 5, ...}</p>
</div>
"""
    }
]
