TITLE = "Set Operations: Union, Intersection, and Complement"

SECTIONS = [
    {
        "title": "Union and Intersection: Combining Sets",
        "body": """
<h3>Understanding Union: A ∪ B</h3>
<p>Think of union as "combining everything from both sets".</p>

<div class="concept-box">
<p><strong>Definition:</strong> A ∪ B (A union B) contains all elements that are in A, or in B, or in both.</p>
<p><strong>In symbols:</strong> A ∪ B = {x | x ∈ A or x ∈ B}</p>
<p class="text-muted-note" style="font-size: 0.9em; margin-top: 8px;">"Or" in mathematics is inclusive—it means at least one is true.</p>
</div>

<div class="worked-example">
<h4>Example 1: Computing Union</h4>
<p><strong>Given:</strong> A = {1, 2, 3}, B = {3, 4, 5}</p>
<p><strong>Find:</strong> A ∪ B</p>
<p style="margin-top: 8px;"><strong>Solution:</strong> Start with all elements from A, then add any new elements from B</p>
<p style="font-family: monospace; margin-top: 4px;">A ∪ B = {1, 2, 3, 4, 5}</p>
<p style="margin-top: 8px;" class="text-muted-note"><strong>Note:</strong> We list 3 only once, even though it's in both sets. Sets contain distinct elements.</p>
</div>

<h3>Understanding Intersection: A ∩ B</h3>
<p>Think of intersection as "finding what they have in common".</p>

<div class="concept-box">
<p><strong>Definition:</strong> A ∩ B (A intersection B) contains only elements in both A and B.</p>
<p><strong>In symbols:</strong> A ∩ B = {x | x ∈ A and x ∈ B}</p>
<p class="text-muted-note" style="font-size: 0.9em; margin-top: 8px;">"And" means <em>both</em> conditions must be true.</p>
</div>

<div class="worked-example">
<h4>Example 2: Computing Intersection</h4>
<p><strong>Given:</strong> A = {1, 2, 3}, B = {3, 4, 5}</p>
<p><strong>Find:</strong> A ∩ B</p>
<p style="margin-top: 8px;"><strong>Solution:</strong> Which elements are in both sets?</p>
<p style="font-family: monospace; margin-top: 4px;">A ∩ B = {3}</p>
<p style="margin-top: 8px;" class="text-muted-note">Only 3 appears in both A and B.</p>
</div>

<h3>Disjoint Sets</h3>
<p>When two sets have nothing in common, they are <strong>disjoint</strong>.</p>
<p style="font-family: monospace;">C = {1, 2}, D = {5, 6}</p>
<p style="font-family: monospace;">C ∩ D = ∅</p>
<p class="text-muted-note">The intersection is empty—they're disjoint.</p>
"""
    },
    {
        "title": "Complement, Difference, and Cardinality Laws",
        "body": """
<h3>The Complement: A'</h3>
<p>The complement contains everything NOT in the set.</p>

<div class="concept-box">
<p><strong>Definition:</strong> A' (A complement) contains all elements in the universal set U that are NOT in A.</p>
<p><strong>In symbols:</strong> A' = {x | x ∈ U and x ∉ A}</p>
<p class="text-muted-note" style="font-size: 0.9em; margin-top: 8px;"><strong>Universal Set U:</strong> The set of all elements we're considering (context-dependent).</p>
</div>

<div class="worked-example">
<h4>Example 3: Finding Complements</h4>
<p><strong>If U = {1, 2, 3, 4, 5} and A = {1, 3, 5}</strong></p>
<p><strong>Find: A'</strong></p>
<p style="margin-top: 8px;"><strong>Solution:</strong> What's in U but not in A?</p>
<p style="font-family: monospace; margin-top: 4px;">A' = {2, 4}</p>
<p style="margin-top: 8px;" class="text-muted-note"><strong>Note:</strong> A ∪ A' = U (together, A and its complement cover everything)</p>
</div>

<h3>Set Difference: A \\ B</h3>
<p>Elements in A that are NOT in B.</p>

<div class="formula-box">
<p><strong>Definition:</strong> A \\ B = {x | x ∈ A and x ∉ B}</p>
</div>

<div class="worked-example">
<h4>Example 4: Set Difference</h4>
<p><strong>A = {1, 2, 3, 4}, B = {3, 4, 5}</strong></p>
<p><strong>Find: A \\ B</strong></p>
<p style="margin-top: 8px;"><strong>Solution:</strong> Elements in A but not in B</p>
<p style="font-family: monospace; margin-top: 4px;">A \\ B = {1, 2}</p>
</div>

<h3>Cardinality and the Inclusion-Exclusion Principle</h3>
<p>How do we count elements in a union without double-counting?</p>

<div class="concept-box">
<p><strong>Inclusion-Exclusion Principle:</strong></p>
<p style="font-family: monospace; margin: 8px 0; font-size: 1.1em;">|A ∪ B| = |A| + |B| - |A ∩ B|</p>
<p style="font-size: 0.9em"><strong>Why subtract?</strong> Elements in A ∩ B are counted twice (once in |A|, once in |B|), so we subtract them once.</p>
</div>

<div class="worked-example">
<h4>Example 5: Counting with Inclusion-Exclusion</h4>
<p><strong>A survey of 100 people:</strong></p>
<p>• 60 like coffee</p>
<p>• 40 like tea</p>
<p>• 20 like both</p>
<p style="margin-top: 12px;"><strong>How many like at least one?</strong></p>
<p style="margin-top: 8px;"><strong>Solution:</strong></p>
<p style="font-family: monospace; margin: 8px 0;">|Coffee ∪ Tea| = 60 + 40 - 20 = 80</p>
<p class="text-muted-note">80 people like coffee, tea, or both.</p>
<p style="margin-top: 8px;" class="text-muted-note"><strong>Interpretation:</strong> If we just added 60 + 40 = 100, we'd be wrong—we'd count the 20 people who like both twice!</p>
</div>
"""
    },
    {
        "title": "Laws of Set Operations",
        "body": """
<h3>Fundamental Properties of Sets</h3>
<p>Sets follow predictable rules, just like numbers do with addition and multiplication.</p>

<div class="concept-box">
<h4>Commutative Law: Order Doesn't Matter</h4>
<p style="font-family: monospace; margin: 8px 0;">A ∪ B = B ∪ A</p>
<p style="font-family: monospace; margin: 8px 0;">A ∩ B = B ∩ A</p>
<p style="font-size: 0.9em">Just like with addition: 2 + 3 = 3 + 2</p>
</div>

<div class="concept-box">
<h4>Associative Law: Grouping Doesn't Matter</h4>
<p style="font-family: monospace; margin: 8px 0;">(A ∪ B) ∪ C = A ∪ (B ∪ C)</p>
<p style="font-family: monospace; margin: 8px 0;">(A ∩ B) ∩ C = A ∩ (B ∩ C)</p>
<p style="font-size: 0.9em">Just like with addition: (2 + 3) + 4 = 2 + (3 + 4)</p>
</div>

<div class="concept-box">
<h4>Distributive Law: Mixing Operations</h4>
<p style="font-family: monospace; margin: 8px 0;">A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)</p>
<p style="font-family: monospace; margin: 8px 0;">A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)</p>
<p style="font-size: 0.9em">Like multiplying: a(b + c) = ab + ac</p>
</div>

<h3>De Morgan's Laws: The Power Tool</h3>
<p>These laws relate complements, unions, and intersections. <strong>This is crucial for logic and computing.</strong></p>

<div class="concept-box" >
<h4>De Morgan's First Law</h4>
<p style="font-family: monospace; font-size: 1.05em; margin: 8px 0;">(A ∪ B)' = A' ∩ B'</p>
<p style="margin-top: 8px;"><strong>In English:</strong> "Not (A or B)" equals "(not A) and (not B)"</p>
<p style="margin-top: 8px;" class="text-muted-note">If you're not in the club AND you're not a member, then you're definitely not in the club.</p>
</div>

<div class="concept-box" >
<h4>De Morgan's Second Law</h4>
<p style="font-family: monospace; font-size: 1.05em; margin: 8px 0;">(A ∩ B)' = A' ∪ B'</p>
<p style="margin-top: 8px;"><strong>In English:</strong> "Not (A and B)" equals "(not A) or (not B)"</p>
<p style="margin-top: 8px;" class="text-muted-note">To NOT be in both groups, you just need to be missing from at least one of them.</p>
</div>

<div class="worked-example">
<h4>Example 6: Applying De Morgan's Laws</h4>
<p><strong>U = {1, 2, 3, 4, 5}, A = {1, 2}, B = {2, 3}</strong></p>
<p style="margin-top: 8px;"><strong>Verify:</strong> (A ∪ B)' = A' ∩ B'</p>
<p style="margin-top: 8px;"><strong>Left side:</strong></p>
<p style="font-family: monospace; margin: 4px 0;">A ∪ B = {1, 2, 3}</p>
<p style="font-family: monospace; margin: 4px 0;">(A ∪ B)' = {4, 5}</p>
<p style="margin-top: 8px;"><strong>Right side:</strong></p>
<p style="font-family: monospace; margin: 4px 0;">A' = {3, 4, 5}</p>
<p style="font-family: monospace; margin: 4px 0;">B' = {1, 4, 5}</p>
<p style="font-family: monospace; margin: 4px 0;">A' ∩ B' = {4, 5} ✓</p>
<p style="margin-top: 8px;" class="text-muted-note">Both sides equal {4, 5}—De Morgan's law verified!</p>
</div>

<h3>Absorption Laws</h3>
<p>Sometimes operations "collapse" to simpler forms:</p>
<p style="font-family: monospace;">A ∩ (A ∪ B) = A</p>
<p style="font-family: monospace;">A ∪ (A ∩ B) = A</p>
<p style="font-size: 0.9em">The intersection/union with a larger set brings you back to A.</p>
"""
    }
]
