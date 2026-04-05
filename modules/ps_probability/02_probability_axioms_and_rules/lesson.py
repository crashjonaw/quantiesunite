TITLE = "Probability Axioms and Rules: The Logical Foundation"

SECTIONS = [
    {
        "id": "axioms_intro",
        "title": "The Three Sacred Axioms of Kolmogorov",
        "body": """
<div class="concept-box">
<h3>Historical Context</h3>
<p>In 1933, Andrey Kolmogorov published <em>Grundbegriffe der Wahrscheinlichkeitsrechnung</em> (Foundations of the Theory of Probability). He proposed a minimal set of three axioms that would unite all probability theory—from coin flips to infinite-dimensional spaces. Everything that follows from probability theory is derivable from these three rules.</p>
</div>

<h3>The Three Axioms</h3>

<div class="concept-box">
<h4>Axiom 1: Non-Negativity</h4>
<p>For any event \\(A \\in \\mathcal{F}\\):</p>
$$P(A) \\geq 0$$
<p><strong>Interpretation:</strong> Probability is never negative. We cannot be "less than zero" certain.</p>
</div>

<div class="concept-box">
<h4>Axiom 2: Unitarity (Normalization)</h4>
<p>The entire sample space has probability 1:</p>
$$P(\\Omega) = 1$$
<p><strong>Interpretation:</strong> Something must happen. We assign total certainty to the sample space, and probabilities measure portions of this total.</p>
</div>

<div class="concept-box">
<h4>Axiom 3: Countable Additivity</h4>
<p>For any countable collection of <em>pairwise disjoint</em> events \\(A_1, A_2, A_3, \\ldots \\in \\mathcal{F}\\):</p>
$$P\\left(\\bigcup_{i=1}^{\\infty} A_i\\right) = \\sum_{i=1}^{\\infty} P(A_i)$$
<p><strong>Interpretation:</strong> If events do not overlap, their probabilities add. This applies to countably infinite collections, not just finite ones.</p>
</div>

<h3>Why These Three?</h3>

<p><strong>Axiom 1</strong> is intuitive: probability cannot be negative.</p>

<p><strong>Axiom 2</strong> is a normalization rule. Probability could theoretically be defined on any scale (0 to 100, or 0 to 1000), but using 0 to 1 is standard and natural—probabilities are <em>shares of total certainty</em>.</p>

<p><strong>Axiom 3</strong> is the most subtle and powerful. It does <em>not</em> say that probabilities add for arbitrary events—only for disjoint ones. For overlapping events, we need inclusion-exclusion. The axiom assumes <strong>countable additivity</strong>, not merely finite additivity. Why does this matter? Because on infinite spaces, finite additivity is too weak. It cannot handle the limit of a sequence of events, which is essential for probability on the real numbers.</p>

<div class="warning-box">
<h4>Finite vs. Countable Additivity</h4>
<p>Imagine flipping a fair coin infinitely many times. If only finite additivity held, the probability of "infinitely many heads" would be ill-defined—we could not sum infinitely many non-zero probabilities consistently. Countable additivity resolves this by ensuring the infinite sum has meaning.</p>
</div>
"""
    },
    {
        "id": "axioms_consequences",
        "title": "Immediate Consequences of the Axioms",
        "body": """
<h3>Power of the Three Axioms</h3>

<p>From just these three rules, we can derive every result in probability theory. Here are the most fundamental consequences.</p>

<div class="success-box">
<h4>Consequence 1: Empty Set Has Zero Probability</h4>
<p>\\(P(\\emptyset) = 0\\)</p>
<p><strong>Proof:</strong> Consider the countable collection \\(A_1 = \\Omega, A_2 = \\emptyset, A_3 = \\emptyset, \\ldots\\) These are pairwise disjoint and \\(\\bigcup A_i = \\Omega\\). By Axiom 3:</p>
$$P(\\Omega) = P(\\Omega) + P(\\emptyset) + P(\\emptyset) + \\cdots$$
<p>Since \\(P(\\Omega) = 1\\) (Axiom 2), the only way this equation holds is if \\(P(\\emptyset) = 0\\).</p>
</div>

<div class="success-box">
<h4>Consequence 2: Complement Rule</h4>
<p>For any event \\(A\\):</p>
$$P(A^c) = 1 - P(A)$$
<p><strong>Proof:</strong> The events \\(A\\) and \\(A^c\\) are disjoint and \\(A \\cup A^c = \\Omega\\). By Axiom 3 applied to two disjoint events:</p>
$$P(A \\cup A^c) = P(A) + P(A^c) = P(\\Omega) = 1$$
</div>

<div class="success-box">
<h4>Consequence 3: Monotonicity</h4>
<p>If \\(A \\subseteq B\\), then \\(P(A) \\leq P(B)\\)</p>
<p><strong>Proof:</strong> We can write \\(B = A \\cup (B \\setminus A)\\) where \\(B \\setminus A\\) is disjoint from \\(A\\). By Axiom 3:</p>
$$P(B) = P(A) + P(B \\setminus A) \\geq P(A)$$
<p>since \\(P(B \\setminus A) \\geq 0\\) (Axiom 1).</p>
</div>

<div class="success-box">
<h4>Consequence 4: Union Bound (Boole's Inequality)</h4>
<p>For any events \\(A_1, A_2, \\ldots, A_n\\):</p>
$$P\\left(\\bigcup_{i=1}^{n} A_i\\right) \\leq \\sum_{i=1}^{n} P(A_i)$$
<p><strong>Interpretation:</strong> The probability of at least one event occurring is at most the sum of individual probabilities. Equality holds if and only if the events are pairwise disjoint.</p>
</div>

<h3>Finite vs. Infinite Additivity Revisited</h3>

<p>Axiom 3 says: for disjoint events, \\(P(A_1 \\cup A_2 \\cup \\cdots) = P(A_1) + P(A_2) + \\cdots\\) This enables probability on infinite sample spaces. Without it, we cannot define probability on \\(\\mathbb{R}\\) or other uncountable spaces.</p>
"""
    },
    {
        "id": "axioms_basic_rules",
        "title": "Basic Probability Rules Derived from the Axioms",
        "body": """
<h3>Finite Additivity</h3>

<p>A direct consequence of Axiom 3: for any finite number of disjoint events \\(A_1, \\ldots, A_n\\):</p>
$$P(A_1 \\cup \\cdots \\cup A_n) = P(A_1) + \\cdots + P(A_n)$$

<p>This is used constantly in discrete probability.</p>

<div class="worked-example">
<h4>Fair Die Example</h4>
<p>Each outcome \\(i \\in \\{1, 2, 3, 4, 5, 6\\}\\) has probability \\(1/6\\). The event "rolling even or 1" is \\(\\{1, 2, 4, 6\\}\\), which is the union of four disjoint singleton events. By finite additivity:</p>
$$P(\\{1, 2, 4, 6\\}) = P(\\{1\\}) + P(\\{2\\}) + P(\\{4\\}) + P(\\{6\\}) = \\frac{1}{6} + \\frac{1}{6} + \\frac{1}{6} + \\frac{1}{6} = \\frac{4}{6} = \\frac{2}{3}$$
</div>

<h3>Inclusion-Exclusion Principle</h3>

<p>For two events \\(A\\) and \\(B\\) (not necessarily disjoint):</p>

<div class="concept-box">
<h4>Two-Event Inclusion-Exclusion</h4>
$$P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$$
<p><strong>Intuition:</strong> If we add \\(P(A)\\) and \\(P(B)\\), we count the overlap \\(A \\cap B\\) twice, so we subtract it once.</p>
</div>

<div class="worked-example">
<h4>Example: Drawing Cards</h4>
<p>Draw one card from a standard deck. Let:</p>
<ul>
<li>\\(A\\) = "card is a heart" with \\(P(A) = 13/52\\)</li>
<li>\\(B\\) = "card is a face card" with \\(P(B) = 12/52\\)</li>
</ul>
<p>How many cards are both hearts AND face cards? Three (jack, queen, king of hearts), so \\(P(A \\cap B) = 3/52\\).</p>
$$P(A \\cup B) = \\frac{13}{52} + \\frac{12}{52} - \\frac{3}{52} = \\frac{22}{52} = \\frac{11}{26}$$
</div>

<h3>Continuity of Probability (Advanced)</h3>

<p>A subtle but important property: if \\(A_1 \\subseteq A_2 \\subseteq A_3 \\subseteq \\cdots\\) is an increasing sequence of events with union \\(A = \\bigcup A_i\\), then:</p>

$$\\lim_{n \\to \\infty} P(A_n) = P(A)$$

<p>Similarly, if \\(A_1 \\supseteq A_2 \\supseteq A_3 \\supseteq \\cdots\\) is a decreasing sequence with intersection \\(A = \\bigcap A_i\\), then:</p>

$$\\lim_{n \\to \\infty} P(A_n) = P(A)$$

<p>This flows from countable additivity and justifies taking limits in probability calculations.</p>
"""
    },
    {
        "id": "axioms_discrete_spaces",
        "title": "Probability on Finite and Discrete Spaces",
        "body": """
<h3>Constructing Probabilities on Finite Spaces</h3>

<p>On a finite sample space \\(\\Omega = \\{\\omega_1, \\ldots, \\omega_n\\}\\), a probability measure \\(P\\) is completely determined by assigning probabilities \\(p_i = P(\\{\\omega_i\\})\\) to each outcome, subject to:</p>

$$\\sum_{i=1}^{n} p_i = 1 \\quad \\text{and} \\quad p_i \\geq 0 \\text{ for all } i$$

<p>Then for any event \\(A \\subseteq \\Omega\\):</p>

$$P(A) = \\sum_{\\omega_i \\in A} p_i$$

<div class="worked-example">
<h4>Biased Die</h4>
<p>Suppose a die has outcome probabilities \\(p_1 = 0.1, p_2 = 0.1, p_3 = 0.1, p_4 = 0.2, p_5 = 0.2, p_6 = 0.3\\). Then:</p>
<ul>
<li>\\(P(\\text{even}) = p_2 + p_4 + p_6 = 0.1 + 0.2 + 0.3 = 0.6\\)</li>
<li>\\(P(\\text{≥5}) = p_5 + p_6 = 0.2 + 0.3 = 0.5\\)</li>
</ul>
</div>

<h3>The Uniform Distribution</h3>

<p>When all outcomes are equally likely, \\(p_i = 1/n\\) for all \\(i\\). Then:</p>

$$P(A) = \\frac{|A|}{|\\Omega|} = \\frac{\\text{number of favorable outcomes}}{\\text{total number of outcomes}}$$

<p>This is the classical definition of probability and applies when we have no reason to favor one outcome over another.</p>

<div class="worked-example">
<h4>Fair Die</h4>
<p>\\(P(\\text{≥4}) = P(\\{4, 5, 6\\}) = \\frac{3}{6} = \\frac{1}{2}\\)</p>
</div>

<h3>Probability on Countably Infinite Spaces</h3>

<p>If \\(\\Omega = \\{\\omega_1, \\omega_2, \\ldots\\}\\) is countably infinite, we assign probabilities \\(p_i = P(\\{\\omega_i\\})\\) with:</p>

$$\\sum_{i=1}^{\\infty} p_i = 1$$

<p>This series must converge. Then for any event \\(A\\):</p>

$$P(A) = \\sum_{\\omega_i \\in A} p_i$$

<div class="worked-example">
<h4>Geometric Distribution</h4>
<p>Flip a biased coin (heads probability \\(p\\)) until it lands heads. Let \\(X\\) be the number of flips. Then:</p>
$$P(X = k) = (1-p)^{k-1} p \\quad \\text{for } k = 1, 2, 3, \\ldots$$
<p>We can verify: \\(\\sum_{k=1}^{\\infty} (1-p)^{k-1} p = p \\cdot \\frac{1}{1-(1-p)} = p \\cdot \\frac{1}{p} = 1\\) ✓</p>
</div>
"""
    }
]
