TITLE = "Sample Spaces and Events: The Foundation of Probability"

SECTIONS = [
    {
        "id": "ss_motivation",
        "title": "Why Sample Spaces Matter",
        "body": """
<div class="concept-box">
<h3>The Conceptual Foundation</h3>
<p>Before we can assign probabilities, we must define the universe of possible outcomes. A <strong>sample space</strong> is precisely this: the exhaustive set of all possible outcomes of a random experiment. Without clarity here, probability becomes ambiguous.</p>
</div>

<div class="worked-example">
<h4>Real-World Example</h4>
<p>You roll a die. The sample space is \\(\\Omega = \\{1, 2, 3, 4, 5, 6\\}\\). But what if the die lands on an edge? What if it rolls off the table? In practice, we define a <strong>well-posed</strong> experiment: the die lands on a face, and we record the face value. Ambiguity resolved by design.</p>
</div>

<h3>Key Principle</h3>
<p>A sample space must be:</p>
<ul>
<li><strong>Exhaustive:</strong> every possible outcome is included</li>
<li><strong>Mutually exclusive:</strong> each outcome occurs alone; no overlap</li>
<li><strong>Well-defined:</strong> clear rules for what constitutes an outcome</li>
</ul>
"""
    },
    {
        "id": "ss_definition",
        "title": "Defining the Sample Space",
        "body": """
<h3>Discrete vs. Continuous Sample Spaces</h3>

<p>A sample space \\(\\Omega\\) can be finite, countably infinite, or uncountably infinite. This distinction matters for probability theory.</p>

<div class="concept-box">
<h4>Finite Sample Spaces</h4>
<p>\\(\\Omega\\) has finitely many outcomes. Examples:</p>
<ul>
<li>Single die: \\(\\Omega = \\{1, 2, 3, 4, 5, 6\\}\\)</li>
<li>Two coins: \\(\\Omega = \\{HH, HT, TH, TT\\}\\)</li>
<li>Drawing one card: \\(\\Omega\\) has 52 outcomes</li>
</ul>
</div>

<div class="concept-box">
<h4>Countably Infinite Sample Spaces</h4>
<p>\\(\\Omega\\) is infinite but countable (can be listed as \\(\\omega_1, \\omega_2, \\ldots\\)). Example:</p>
<ul>
<li>Number of coin flips until first heads: \\(\\Omega = \\{1, 2, 3, \\ldots\\}\\)</li>
<li>Count of emails received in a day: \\(\\Omega = \\{0, 1, 2, \\ldots\\}\\)</li>
</ul>
</div>

<div class="concept-box">
<h4>Uncountably Infinite (Continuous) Sample Spaces</h4>
<p>\\(\\Omega\\) cannot be listed—it is dense (like real numbers). Examples:</p>
<ul>
<li>Waiting time until next customer: \\(\\Omega = [0, \\infty)\\)</li>
<li>Temperature tomorrow: \\(\\Omega = \\mathbb{R}\\)</li>
<li>Coordinates of a dart on a board: \\(\\Omega = [0,1]^2\\)</li>
</ul>
</div>

<h3>Notation and Terminology</h3>

<p>We denote a sample space by \\(\\Omega\\) (capital omega). Each element \\(\\omega \\in \\Omega\\) is an <strong>outcome</strong> or <strong>elementary event</strong>. The pair \\((\\Omega, \\mathcal{F})\\) where \\(\\mathcal{F}\\) is a collection of subsets of \\(\\Omega\\) forms a <strong>measurable space</strong>.</p>
"""
    },
    {
        "id": "ss_events",
        "title": "Events: Subsets of the Sample Space",
        "body": """
<h3>What Is an Event?</h3>

<p>An <strong>event</strong> is any subset of \\(\\Omega\\). In the context of a probability space, we assign a probability to each event. An event \\(A\\) occurs if the outcome \\(\\omega\\) that materializes belongs to \\(A\\).</p>

<div class="worked-example">
<h4>Dice Example: Events from \\(\\Omega = \\{1, 2, 3, 4, 5, 6\\}\\)</h4>
<ul>
<li>\\(A = \\{2\\}\\): rolling exactly a 2 (an event with one outcome)</li>
<li>\\(B = \\{2, 4, 6\\}\\): rolling an even number</li>
<li>\\(C = \\{1, 2, 3\\}\\): rolling at most 3</li>
<li>\\(D = \\{4, 5, 6\\}\\): rolling at least 4</li>
<li>\\(\\Omega = \\{1, 2, 3, 4, 5, 6\\}\\): the certain event (something happens)</li>
<li>\\(\\emptyset = \\{\\}\\): the impossible event (nothing happens)</li>
</ul>
</div>

<h3>Event Operations: Set Algebra</h3>

<p>Events combine using standard set operations. If \\(A\\) and \\(B\\) are events, then:</p>

<div class="concept-box">
<h4>Union: \\(A \\cup B\\)</h4>
<p>The event that \\(A\\) occurs <em>or</em> \\(B\\) occurs (or both). In the sample space, \\(A \\cup B = \\{\\omega \\in \\Omega : \\omega \\in A \\text{ or } \\omega \\in B\\}\\)</p>
<p><strong>Example:</strong> With \\(B = \\{2,4,6\\}\\) (even) and \\(D = \\{4,5,6\\}\\) (≥4), we have \\(B \\cup D = \\{2,4,5,6\\}\\).</p>
</div>

<div class="concept-box">
<h4>Intersection: \\(A \\cap B\\)</h4>
<p>The event that <em>both</em> \\(A\\) and \\(B\\) occur. In the sample space, \\(A \\cap B = \\{\\omega \\in \\Omega : \\omega \\in A \\text{ and } \\omega \\in B\\}\\)</p>
<p><strong>Example:</strong> With \\(B = \\{2,4,6\\}\\) (even) and \\(D = \\{4,5,6\\}\\) (≥4), we have \\(B \\cap D = \\{4,6\\}\\).</p>
</div>

<div class="concept-box">
<h4>Complement: \\(A^c\\)</h4>
<p>The event that \\(A\\) does <em>not</em> occur. In the sample space, \\(A^c = \\{\\omega \\in \\Omega : \\omega \\notin A\\}\\)</p>
<p><strong>Example:</strong> With \\(B = \\{2,4,6\\}\\) (even), we have \\(B^c = \\{1,3,5\\}\\) (odd).</p>
</div>

<h3>Disjoint Events</h3>

<p>Two events \\(A\\) and \\(B\\) are <strong>disjoint</strong> (or <strong>mutually exclusive</strong>) if \\(A \\cap B = \\emptyset\\). They cannot both occur. This concept will be crucial when we apply Kolmogorov's axioms.</p>

<div class="worked-example">
<h4>Disjoint Events Example</h4>
<p>Events \\(A = \\{1,3\\}\\) (odd less than 5) and \\(B = \\{2,4,6\\}\\) (even) are disjoint. No outcome can satisfy both: \\(A \\cap B = \\emptyset\\).</p>
</div>
"""
    },
    {
        "id": "ss_measurable_space",
        "title": "The σ-Algebra: Measurable Events",
        "body": """
<h3>Beyond Simple Cases: The σ-Algebra</h3>

<p>In basic discrete probability (finite or countably infinite sample spaces), we often take every subset of \\(\\Omega\\) to be an event. But in continuous probability, this breaks down. Not every subset can be assigned a probability consistently.</p>

<div class="concept-box">
<h4>The σ-Algebra (Sigma-Algebra)</h4>
<p>A \\(\\sigma\\)-algebra \\(\\mathcal{F}\\) on \\(\\Omega\\) is a collection of subsets of \\(\\Omega\\) satisfying:</p>
<ol>
<li>\\(\\Omega \\in \\mathcal{F}\\) (the whole space is an event)</li>
<li>If \\(A \\in \\mathcal{F}\\), then \\(A^c \\in \\mathcal{F}\\) (complements are events)</li>
<li>If \\(A_1, A_2, A_3, \\ldots \\in \\mathcal{F}\\), then \\(\\bigcup_{i=1}^{\\infty} A_i \\in \\mathcal{F}\\) (countable unions are events)</li>
</ol>
<p>From these rules, it follows that countable intersections \\(\\bigcap_{i=1}^{\\infty} A_i\\) are also in \\(\\mathcal{F}\\).</p>
</div>

<h3>The Borel σ-Algebra</h3>

<p>For \\(\\Omega = \\mathbb{R}\\), the <strong>Borel \\(\\sigma\\)-algebra</strong> \\(\\mathcal{B}\\) is the smallest \\(\\sigma\\)-algebra containing all open intervals \\((a,b)\\). It includes:</p>
<ul>
<li>Open intervals: \\((a, b)\\)</li>
<li>Closed intervals: \\([a, b]\\)</li>
<li>Half-open intervals: \\([a, b)\\) and \\((a, b]\\)</li>
<li>Countable unions and intersections of these</li>
<li>Complements of these</li>
</ul>

<p>But it excludes certain pathological sets (non-measurable sets) that have no consistent notion of size.</p>

<div class="warning-box">
<h4>Why This Matters</h4>
<p>Kolmogorov's axioms require a \\(\\sigma\\)-algebra because they define probability on countable unions. Without \\(\\mathcal{F}\\), we cannot even state Axiom 3. And on \\(\\mathbb{R}\\), the Borel \\(\\sigma\\)-algebra is the natural choice—large enough to include all practical events, small enough to allow consistent probability measures.</p>
</div>

<h3>The Probability Space</h3>

<p>A <strong>probability space</strong> is a triple \\((\\Omega, \\mathcal{F}, P)\\) where:</p>
<ul>
<li>\\(\\Omega\\) is the sample space</li>
<li>\\(\\mathcal{F}\\) is a \\(\\sigma\\)-algebra of subsets of \\(\\Omega\\)</li>
<li>\\(P: \\mathcal{F} \\to [0,1]\\) is a probability measure (defined next section)</li>
</ul>

<p>This triple codifies the entire probabilistic setup: outcomes, events, and the rule for assigning probabilities.</p>
"""
    }
]
