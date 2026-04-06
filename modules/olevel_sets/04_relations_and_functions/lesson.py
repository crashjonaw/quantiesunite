TITLE = "Relations and Functions: Sets in Action"

SECTIONS = [
    {
        "title": "Cartesian Products and Ordered Pairs",
        "body": """
<h3>Ordered Pairs: When Order Matters</h3>
<p>Until now, we've treated sets where {a, b} = {b, a}. But sometimes order IS important.</p>

<div class="concept-box">
<p><strong>Ordered Pair:</strong> (a, b) is distinct from (b, a). The first element is the first coordinate.</p>
<p class="text-muted-note" style="font-size: 0.9em; margin-top: 8px;">Example: (3, 5) ≠ (5, 3). In coordinates, (3, 5) is point three units right, five up. (5, 3) is different.</p>
</div>

<h3>Cartesian Product: A × B</h3>
<p>The Cartesian product combines two sets by pairing every element of A with every element of B.</p>

<div class="concept-box">
<p><strong>Definition:</strong> A × B = {(a, b) | a ∈ A and b ∈ B}</p>
<p class="text-muted-note" style="font-size: 0.9em; margin-top: 8px;">"All ordered pairs where the first comes from A and the second from B"</p>
</div>

<div class="worked-example">
<h4>Example 1: Computing Cartesian Product</h4>
<p><strong>A = {1, 2}, B = {red, blue}</strong></p>
<p><strong>Find: A × B</strong></p>
<p style="margin-top: 8px;"><strong>Solution:</strong> Pair each element of A with each element of B</p>
<p style="font-family: monospace; margin-top: 8px;">A × B = {(1, red), (1, blue), (2, red), (2, blue)}</p>
<p style="margin-top: 8px;" class="text-muted-note"><strong>Cardinality:</strong> |A × B| = |A| × |B| = 2 × 2 = 4</p>
</div>

<h3>Order Matters: A × B ≠ B × A</h3>

<div class="worked-example">
<h4>Example 2: A × B vs B × A</h4>
<p><strong>A = {1, 2}, B = {a, b}</strong></p>
<p style="margin-top: 8px;"><strong>A × B =</strong> {(1, a), (1, b), (2, a), (2, b)}</p>
<p style="margin-top: 4px;"><strong>B × A =</strong> {(a, 1), (a, 2), (b, 1), (b, 2)}</p>
<p style="margin-top: 8px;" class="text-muted-note">These are different sets! (1, a) ≠ (a, 1)</p>
</div>

<h3>Real-World Example: Coordinate System</h3>
<p>The xy-coordinate plane is ℝ × ℝ—the Cartesian product of real numbers with itself.</p>
<p>Each point (x, y) is an ordered pair from ℝ × ℝ.</p>

<svg viewBox="-15 -15 380 350" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 300px; margin: 20px auto; display: block;" font-family="sans-serif">
  <rect x="0" y="0" width="350" height="320" rx="4" fill="#0d1117" stroke="#30363d" stroke-width="1"/>

  <!-- Axes -->
  <line x1="175" y1="25" x2="175" y2="295" stroke="#4f8ef7" stroke-width="2"/>
  <line x1="45" y1="160" x2="325" y2="160" stroke="#4f8ef7" stroke-width="2"/>

  <!-- Arrowheads -->
  <polygon points="175,20 170,30 180,30" fill="#4f8ef7"/>
  <polygon points="330,160 320,155 320,165" fill="#4f8ef7"/>

  <!-- Tick marks on x-axis -->
  <line x1="205" y1="156" x2="205" y2="164" stroke="#4f8ef7" stroke-width="1"/>
  <line x1="235" y1="156" x2="235" y2="164" stroke="#4f8ef7" stroke-width="1"/>
  <line x1="265" y1="156" x2="265" y2="164" stroke="#4f8ef7" stroke-width="1"/>
  <text x="205" y="178" font-size="10" fill="currentColor" opacity="0.6" text-anchor="middle">1</text>
  <text x="235" y="178" font-size="10" fill="currentColor" opacity="0.6" text-anchor="middle">2</text>
  <text x="265" y="178" font-size="10" fill="currentColor" opacity="0.6" text-anchor="middle">3</text>

  <!-- Tick marks on y-axis -->
  <line x1="171" y1="130" x2="179" y2="130" stroke="#4f8ef7" stroke-width="1"/>
  <line x1="171" y1="100" x2="179" y2="100" stroke="#4f8ef7" stroke-width="1"/>
  <text x="163" y="134" font-size="10" fill="currentColor" opacity="0.6" text-anchor="end">1</text>
  <text x="163" y="104" font-size="10" fill="currentColor" opacity="0.6" text-anchor="end">2</text>

  <!-- Dashed projection lines for (3, 2) -->
  <line x1="265" y1="160" x2="265" y2="100" stroke="#4f8ef7" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="175" y1="100" x2="265" y2="100" stroke="#4f8ef7" stroke-width="1" stroke-dasharray="4,3"/>

  <!-- Point (3, 2) -->
  <circle cx="265" cy="100" r="5" fill="#4f8ef7"/>

  <!-- Labels -->
  <text x="175" y="310" font-size="14" fill="currentColor" text-anchor="middle">x</text>
  <text x="30" y="164" font-size="14" fill="currentColor" text-anchor="middle">y</text>
  <text x="275" y="92" font-size="12" fill="currentColor">(3, 2)</text>
  <text x="165" y="172" font-size="11" fill="currentColor" opacity="0.6" text-anchor="end">O</text>
</svg>
"""
    },
    {
        "title": "Relations: The Bridge Between Sets",
        "body": """
<h3>What is a Relation?</h3>
<p>A relation connects elements from one set to another. It's a subset of a Cartesian product.</p>

<div class="concept-box">
<p><strong>Definition:</strong> A relation from A to B is any subset of A × B.</p>
<p class="text-muted-note" style="font-size: 0.9em; margin-top: 8px;">R ⊆ A × B. It specifies which pairs (a, b) are "related" by the relation.</p>
</div>

<div class="worked-example">
<h4>Example 3: Creating a Relation</h4>
<p><strong>A = {1, 2, 3}, B = {a, b, c}</strong></p>
<p><strong>A × B =</strong> {(1,a), (1,b), (1,c), (2,a), (2,b), (2,c), (3,a), (3,b), (3,c)}</p>
<p style="margin-top: 8px;"><strong>Relation R: "first element is ≤ second element position"</strong></p>
<p style="margin-top: 8px;"><strong>R =</strong> {(1,a), (1,b), (1,c), (2,b), (2,c), (3,c)}</p>
<p style="margin-top: 8px;" class="text-muted-note">R is a subset of A × B, so it's a valid relation.</p>
</div>

<h3>Domain and Codomain</h3>

<div class="formula-box">
<p><strong>Domain:</strong> The set of all first coordinates in the relation (what we're pairing from A)</p>
<p style="margin-top: 8px;"><strong>Codomain:</strong> The set B we're pairing to (often specified ahead of time)</p>
<p style="margin-top: 8px;"><strong>Range:</strong> The set of actual second coordinates used (subset of codomain)</p>
</div>

<div class="worked-example">
<h4>Example 4: Domain and Range</h4>
<p><strong>Relation: R = {(1,b), (1,c), (2,c), (3,c)}</strong></p>
<p style="margin-top: 8px;"><strong>Domain:</strong> {1, 2, 3} (what actually got paired)</p>
<p style="margin-top: 8px;"><strong>Codomain:</strong> {a, b, c} (where we're pairing to)</p>
<p style="margin-top: 8px;"><strong>Range:</strong> {b, c} (what actually got used in second position)</p>
<p style="margin-top: 8px;" class="text-muted-note">Note: Range ⊆ Codomain, but they need not be equal.</p>
</div>

<h3>Visualizing Relations: Mapping Diagrams</h3>

<svg viewBox="-15 -15 380 270" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 300px; margin: 20px auto; display: block;" font-family="sans-serif">
  <rect x="0" y="0" width="350" height="240" rx="4" fill="#0d1117" stroke="#30363d" stroke-width="1"/>

  <!-- Title -->
  <text x="175" y="30" font-size="11" fill="currentColor" opacity="0.6" text-anchor="middle">R: 1 maps to {b, c}, 2 maps to {c}</text>

  <!-- Left set oval -->
  <ellipse cx="75" cy="120" rx="40" ry="70" fill="transparent" stroke="#4f8ef7" stroke-width="1.5" stroke-dasharray="4,3"/>
  <circle cx="75" cy="80" r="5" fill="#4f8ef7"/>
  <circle cx="75" cy="120" r="5" fill="#4f8ef7"/>
  <circle cx="75" cy="160" r="5" fill="#4f8ef7"/>
  <text x="50" y="84" font-size="11" fill="currentColor" opacity="0.7" text-anchor="end">1</text>
  <text x="50" y="124" font-size="11" fill="currentColor" opacity="0.7" text-anchor="end">2</text>
  <text x="50" y="164" font-size="11" fill="currentColor" opacity="0.7" text-anchor="end">3</text>
  <text x="75" y="218" font-size="12" fill="currentColor" text-anchor="middle">A = {1, 2, 3}</text>

  <!-- Right set oval -->
  <ellipse cx="275" cy="120" rx="40" ry="70" fill="transparent" stroke="#4f8ef7" stroke-width="1.5" stroke-dasharray="4,3"/>
  <circle cx="275" cy="80" r="5" fill="#4f8ef7"/>
  <circle cx="275" cy="120" r="5" fill="#4f8ef7"/>
  <circle cx="275" cy="160" r="5" fill="#4f8ef7"/>
  <text x="300" y="84" font-size="11" fill="currentColor" opacity="0.7">a</text>
  <text x="300" y="124" font-size="11" fill="currentColor" opacity="0.7">b</text>
  <text x="300" y="164" font-size="11" fill="currentColor" opacity="0.7">c</text>
  <text x="275" y="218" font-size="12" fill="currentColor" text-anchor="middle">B = {a, b, c}</text>

  <!-- Arrows for relation: 1→b, 1→c, 2→c -->
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#4f8ef7"/>
    </marker>
  </defs>
  <line x1="80" y1="80" x2="268" y2="118" stroke="#4f8ef7" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <line x1="80" y1="80" x2="268" y2="158" stroke="#4f8ef7" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <line x1="80" y1="120" x2="268" y2="158" stroke="#4f8ef7" stroke-width="1.5" marker-end="url(#arrowhead)"/>
</svg>

<p style="margin-top: 12px">The arrows show which pairs are in the relation. Notice 3 has no outgoing arrows.</p>
"""
    },
    {
        "title": "Functions: Special Relations",
        "body": """
<h3>What Makes a Function Special?</h3>
<p>A function is a relation with a special property: each input has exactly one output.</p>

<div class="concept-box">
<p><strong>Definition:</strong> A function f: A → B is a relation where:</p>
<ol>
  <li><strong>Total:</strong> Every element of A has at least one pair (covered by domain)</li>
  <li><strong>Single-valued:</strong> Each element of A pairs with exactly one element of B</li>
</ol>
<p class="text-muted-note" style="font-size: 0.9em; margin-top: 8px;">In short: For each a ∈ A, there exists exactly one b ∈ B such that (a, b) ∈ f.</p>
</div>

<h3>Function Notation: f(x)</h3>
<p style="font-family: monospace; font-size: 1.05em;">f: A → B</p>
<p style="margin-top: 8px;" class="text-muted-note">Reads as "f is a function from A to B"</p>

<p style="font-family: monospace; font-size: 1.05em; margin-top: 8px;">f(a) = b</p>
<p style="margin-top: 8px;" class="text-muted-note">Reads as "f of a equals b" — a maps to b under f</p>

<div class="worked-example">
<h4>Example 5: Function vs Not a Function</h4>
<p><strong>A = {1, 2, 3}, B = {a, b, c}</strong></p>
<p style="margin-top: 12px;"><strong>IS this a function?</strong> f = {(1,a), (2,b), (3,c)}</p>
<p style="margin-top: 8px;"><strong>Check:</strong> Domain = {1,2,3} (all of A) ✓, each has exactly one output ✓</p>
<p class="accent-heading"><strong>YES, it's a function.</strong></p>
<p style="margin-top: 12px;"><strong>IS this a function?</strong> g = {(1,a), (1,b), (2,c)}</p>
<p style="margin-top: 8px;"><strong>Check:</strong> 1 maps to both a and b ✗ (violates single-valued property)</p>
<p style="color: #e74c3c;"><strong>NO, it's not a function.</strong> (It's a relation, but not a function.)</p>
<p style="margin-top: 12px;"><strong>IS this a function?</strong> h = {(1,a), (2,b)}</p>
<p style="margin-top: 8px;"><strong>Check:</strong> Domain = {1,2} ≠ A, element 3 is missing ✗ (not total)</p>
<p style="color: #e74c3c;"><strong>NO, it's not a function.</strong> Not defined for all of A.</p>
</div>

<h3>Types of Functions</h3>

<div class="concept-box">
<h4>Injective (One-to-One)</h4>
<p style="font-family: monospace;">If f(a₁) = f(a₂), then a₁ = a₂</p>
<p class="text-muted-note" style="font-size: 0.9em; margin-top: 8px;">No two different inputs map to the same output.</p>
<p style="margin-top: 8px;">Example: f(x) = 2x is injective (different x give different 2x)</p>
</div>

<div class="concept-box">
<h4>Surjective (Onto)</h4>
<p style="font-family: monospace;">For every b ∈ B, there exists a ∈ A such that f(a) = b</p>
<p class="text-muted-note" style="font-size: 0.9em; margin-top: 8px;">Every element in B is "hit" by some element from A. Range = Codomain.</p>
<p style="margin-top: 8px;">Example: f: ℤ → {0,1} defined by f(n) = n mod 2 is surjective (0 and 1 both appear)</p>
</div>

<div class="concept-box">
<h4>Bijective (One-to-One and Onto)</h4>
<p style="font-size: 0.9em">A bijection pairs every element of A with exactly one unique element of B.</p>
<p style="margin-top: 8px;">Bijective functions have <strong>inverses</strong>—you can "undo" the mapping.</p>
</div>

<div class="worked-example">
<h4>Example 6: Classifying Functions</h4>
<p><strong>f: {1,2,3} → {a,b,c,d} with f = {(1,a), (2,b), (3,c)}</strong></p>
<p style="margin-top: 8px;"><strong>Injective?</strong> YES — different inputs give different outputs</p>
<p style="margin-top: 8px;"><strong>Surjective?</strong> NO — d is in codomain but never used (range = {a,b,c})</p>
<p style="margin-top: 8px;"><strong>Bijective?</strong> NO — not surjective</p>
</div>

<h3>Composition of Functions</h3>
<p>If f: A → B and g: B → C, we can compose them:</p>
<p style="font-family: monospace; font-size: 1.05em; margin: 8px 0;">(g ∘ f)(a) = g(f(a))</p>
<p class="text-muted-note">Apply f first, then apply g to the result.</p>

<div class="worked-example">
<h4>Example 7: Function Composition</h4>
<p><strong>f(x) = 2x, g(x) = x + 1</strong></p>
<p style="margin-top: 8px;"><strong>Find: (g ∘ f)(3)</strong></p>
<p style="margin-top: 8px;"><strong>Solution:</strong></p>
<p style="font-family: monospace; margin: 4px 0;">f(3) = 2(3) = 6</p>
<p style="font-family: monospace; margin: 4px 0;">g(f(3)) = g(6) = 6 + 1 = 7</p>
<p style="margin-top: 8px;"><strong>Answer: (g ∘ f)(3) = 7</strong></p>
</div>
"""
    },
    {
        "title": "Equivalence Relations and Partitions",
        "body": """
<h3>Properties of Relations on a Set</h3>
<p>When a relation pairs elements from a set to itself, it can have special properties.</p>

<div class="formula-box">
<p><strong>Reflexive:</strong> aRa for all a ∈ A (every element relates to itself)</p>
<p style="margin-top: 8px;"><strong>Symmetric:</strong> If aRb, then bRa (if a relates to b, b relates to a)</p>
<p style="margin-top: 8px;"><strong>Transitive:</strong> If aRb and bRc, then aRc (relation "chains")</p>
</div>

<div class="worked-example">
<h4>Example 8: Properties of Relations</h4>
<p><strong>Relation: "divides" (x | y means x divides y) on positive integers</strong></p>
<p style="margin-top: 8px;"><strong>Reflexive?</strong> x | x for all x ✓ (2 | 2, 5 | 5)</p>
<p style="margin-top: 8px;"><strong>Symmetric?</strong> If x | y, then y | x? NO ✗ (2 | 4, but 4 ∤ 2)</p>
<p style="margin-top: 8px;"><strong>Transitive?</strong> If x | y and y | z, then x | z? YES ✓ (2|4 and 4|8, so 2|8)</p>
<p style="margin-top: 8px;" class="text-muted-note">Conclusion: Reflexive and transitive, but NOT symmetric. Not an equivalence relation.</p>
</div>

<h3>Equivalence Relations: The Three Properties Together</h3>

<div class="concept-box" >
<p><strong>Definition:</strong> An equivalence relation is reflexive, symmetric, AND transitive.</p>
<p class="text-muted-note" style="font-size: 0.9em; margin-top: 8px;">Equivalence relations partition a set into equivalence classes—subsets where all elements "are alike" under the relation.</p>
</div>

<div class="worked-example">
<h4>Example 9: Classic Equivalence Relation</h4>
<p><strong>Relation: a ~ b if a ≡ b (mod 3) on ℤ</strong></p>
<p style="margin-top: 8px;"><strong>Reflexive?</strong> a ≡ a (mod 3) ✓</p>
<p style="margin-top: 8px;"><strong>Symmetric?</strong> If a ≡ b (mod 3), then b ≡ a (mod 3) ✓</p>
<p style="margin-top: 8px;"><strong>Transitive?</strong> If a ≡ b and b ≡ c (mod 3), then a ≡ c (mod 3) ✓</p>
<p style="margin-top: 12px;"><strong>Equivalence classes:</strong></p>
<p style="font-family: monospace; margin: 4px 0;">[0] = {..., -3, 0, 3, 6, ...} (remainder 0)</p>
<p style="font-family: monospace; margin: 4px 0;">[1] = {..., -2, 1, 4, 7, ...} (remainder 1)</p>
<p style="font-family: monospace; margin: 4px 0;">[2] = {..., -1, 2, 5, 8, ...} (remainder 2)</p>
<p style="margin-top: 8px;" class="text-muted-note">These three classes partition all integers. Every integer is in exactly one class.</p>
</div>

<h3>Partitions: Dividing a Set into Equivalence Classes</h3>

<div class="concept-box">
<p><strong>Partition:</strong> A collection of non-empty, disjoint subsets whose union is the original set.</p>
<p class="text-muted-note" style="font-size: 0.9em; margin-top: 8px;"><strong>Key properties:</strong> Subsets don't overlap, and together they cover everything.</p>
</div>

<div class="worked-example">
<h4>Example 10: Partition from Equivalence Relation</h4>
<p><strong>Set A = {1, 2, 3, 4, 5, 6}</strong></p>
<p><strong>Partition by: x ~ y if x and y have the same remainder mod 2</strong></p>
<p style="margin-top: 8px;"><strong>Classes:</strong></p>
<p style="font-family: monospace; margin: 4px 0;">[Odd] = {1, 3, 5}</p>
<p style="font-family: monospace; margin: 4px 0;">[Even] = {2, 4, 6}</p>
<p style="margin-top: 8px;" class="text-muted-note">These two classes partition A: disjoint and their union is A.</p>
</div>

<div class="success-box">
<p><strong>Key Insight:</strong> Every equivalence relation creates a partition, and every partition defines an equivalence relation. They're two ways of describing the same thing.</p>
</div>
"""
    }
]
