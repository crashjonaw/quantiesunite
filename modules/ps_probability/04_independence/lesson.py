TITLE = "Independence: When Events Don't Affect Each Other"

SECTIONS = [
    {
        "id": "indep_intuition",
        "title": "The Concept of Independence",
        "body": """
<div class="concept-box">
<h3>What Does Independence Mean?</h3>
<p><strong>Independence</strong> is perhaps the most important concept in probability after the axioms. Two events are independent if one has no bearing on the other. Learning that one occurred tells you nothing new about the probability of the other.</p>
</div>

<h3>Real-World Examples</h3>

<p><strong>Independent Events:</strong></p>
<ul>
<li>Two coin flips: the first flip does not affect the second</li>
<li>Rolling a die and flipping a coin: the die roll does not influence the coin flip</li>
<li>Rainfall in New York and rainfall in Tokyo (assuming no global climate feedback)</li>
</ul>

<p><strong>Dependent Events:</strong></p>
<ul>
<li>Drawing cards from a deck without replacement: each draw changes the composition of the remaining deck</li>
<li>Traffic delay and arrival time: delay affects when you arrive</li>
<li>Smoking and lung cancer: smoking increases cancer risk</li>
</ul>

<p>Independence is not about logical separation—it is about <em>probabilistic irrelevance</em>. Two events can be independent even if they seem logically related (if they happen to be probabilistically uncorrelated).</p>

<div class="worked-example">
<h4>A Subtle Example</h4>
<p>Flip a coin and roll a die. Let \\(A\\) = "coin is heads" and \\(B\\) = "die shows 1 or 2". Are these independent?</p>
<p>Intuitively, yes: the coin flip has no effect on the die roll. Mathematically:</p>
<ul>
<li>\\(P(A) = 1/2\\)</li>
<li>\\(P(B) = 2/6 = 1/3\\)</li>
<li>\\(P(A \\cap B)\\) = P(heads AND (1 or 2)) = (1/2) × (1/3) = 1/6 (by multiplying independent experiments)</li>
<li>\\(P(A) \\cdot P(B) = 1/2 \\times 1/3 = 1/6\\) ✓</li>
</ul>
<p>So yes, they are independent.</p>
</div>
"""
    },
    {
        "id": "indep_definition",
        "title": "Formal Definition and Characterizations",
        "body": """
<h3>Definition of Independence</h3>

<div class="concept-box">
<h4>Two Events Are Independent If:</h4>
$$P(A \\cap B) = P(A) \\cdot P(B)$$
<p>Equivalently (when \\(P(B) > 0\\)):</p>
$$P(A|B) = P(A)$$
</div>

<p>This is the fundamental definition. It formalizes the idea: knowing \\(B\\) occurred does not change the probability of \\(A\\).</p>

<h3>Three Equivalent Characterizations</h3>

<p>The following are all equivalent to independence of \\(A\\) and \\(B\\):</p>

<div class="concept-box">
<h4>Characterization 1: Multiplicative Rule</h4>
$$P(A \\cap B) = P(A) \\cdot P(B)$$
</div>

<div class="concept-box">
<h4>Characterization 2: Conditional Probability (A given B)</h4>
$$P(A|B) = P(A) \\quad \\text{(assuming } P(B) > 0\\text{)}$$
</div>

<div class="concept-box">
<h4>Characterization 3: Conditional Probability (B given A)</h4>
$$P(B|A) = P(B) \\quad \\text{(assuming } P(A) > 0\\text{)}$$
</div>

<p><strong>Proof of Equivalence:</strong> If \\(P(A|B) = P(A)\\), then by rearranging the conditional probability formula:</p>
$$P(A) = P(A|B) = \\frac{P(A \\cap B)}{P(B)} \\implies P(A \\cap B) = P(A) \\cdot P(B)$$

<h3>Complement Events</h3>

<p>If \\(A\\) and \\(B\\) are independent, then so are \\(A\\) and \\(B^c\\), and \\(A^c\\) and \\(B\\), and \\(A^c\\) and \\(B^c\\).</p>

<p><strong>Intuition:</strong> If learning \\(B\\) tells you nothing about \\(A\\), then learning \\(B^c\\) (the opposite of \\(B\\)) also tells you nothing about \\(A\\).</p>

<div class="worked-example">
<h4>Proof Sketch</h4>
<p>If \\(P(A \\cap B) = P(A) \\cdot P(B)\\), then:</p>
$$P(A \\cap B^c) = P(A) - P(A \\cap B) = P(A) - P(A) \\cdot P(B) = P(A) \\cdot (1 - P(B)) = P(A) \\cdot P(B^c)$$
</div>
"""
    },
    {
        "id": "indep_multiple_events",
        "title": "Independence of Multiple Events",
        "body": """
<h3>Extending to Three or More Events</h3>

<p>When we have three or more events, we must be careful. There are two levels of independence.</p>

<div class="concept-box">
<h4>Pairwise Independence</h4>
<p>Events \\(A_1, A_2, A_3\\) are <em>pairwise independent</em> if every pair is independent:</p>
$$P(A_i \\cap A_j) = P(A_i) \\cdot P(A_j) \\quad \\text{for all } i \\neq j$$
</div>

<div class="concept-box">
<h4>Mutual Independence</h4>
<p>Events \\(A_1, A_2, A_3\\) are <em>mutually independent</em> (or just <em>independent</em>) if every pair is independent AND every higher-order combination satisfies:</p>
$$P(A_1 \\cap A_2 \\cap A_3) = P(A_1) \\cdot P(A_2) \\cdot P(A_3)$$
<p>More generally, for any subset \\(\\{i_1, \\ldots, i_k\\}\\):</p>
$$P(A_{i_1} \\cap \\cdots \\cap A_{i_k}) = P(A_{i_1}) \\cdots P(A_{i_k})$$
</div>

<h3>Pairwise vs. Mutual Independence</h3>

<p><strong>Critical observation:</strong> Pairwise independence does NOT imply mutual independence!</p>

<div class="worked-example">
<h4>A Famous Counterexample</h4>
<p>Flip two fair coins. Define:</p>
<ul>
<li>\\(A\\): first coin is heads</li>
<li>\\(B\\): second coin is heads</li>
<li>\\(C\\): the two coins match (both heads or both tails)</li>
</ul>
<p><strong>Check pairwise independence:</strong></p>
<ul>
<li>\\(P(A \\cap B) = P(HH) = 1/4\\), and \\(P(A) \\cdot P(B) = 1/2 \\times 1/2 = 1/4\\) ✓</li>
<li>\\(P(A \\cap C) = P(HH) = 1/4\\), and \\(P(A) \\cdot P(C) = 1/2 \\times 1/2 = 1/4\\) ✓</li>
<li>\\(P(B \\cap C) = P(HH) = 1/4\\), and \\(P(B) \\cdot P(C) = 1/2 \\times 1/2 = 1/4\\) ✓</li>
</ul>
<p><strong>Check mutual independence:</strong></p>
<ul>
<li>\\(P(A \\cap B \\cap C) = P(HH) = 1/4\\)</li>
<li>\\(P(A) \\cdot P(B) \\cdot P(C) = 1/2 \\times 1/2 \\times 1/2 = 1/8\\)</li>
<li>Since \\(1/4 \\neq 1/8\\), they are NOT mutually independent!</li>
</ul>
<p>This is counterintuitive: the three events are pairwise independent, yet not mutually independent. The dependency arises because if you know \\(A\\) and \\(B\\), the event \\(C\\) is completely determined.</p>
</div>

<h3>General Definition for Multiple Events</h3>

<p>Events \\(A_1, \\ldots, A_n\\) are <strong>mutually independent</strong> if for every non-empty subset \\(I \\subseteq \\{1, \\ldots, n\\}\\):</p>

$$P\\left(\\bigcap_{i \\in I} A_i\\right) = \\prod_{i \\in I} P(A_i)$$

<p>This requires checking \\(2^n - n - 1\\) conditions (all non-empty proper subsets and intersections).</p>

<h3>Practical Implications</h3>

<p>In applications, we often <em>assume</em> mutual independence to simplify calculations. For example:</p>

<ul>
<li>Repeated coin flips: assume each flip is independent</li>
<li>Sample survey: assume each respondent's answer is independent</li>
<li>Product reliability: assume components fail independently</li>
</ul>

<p>These assumptions are not always true in reality but are often reasonable as approximations.</p>
"""
    },
    {
        "id": "indep_applications",
        "title": "Applications and Common Pitfalls",
        "body": """
<h3>Power of Independence: Simplifying Calculations</h3>

<p>Independence is valuable precisely because it simplifies calculations. Without independence, we need full knowledge of joint distributions—exponentially more data. With independence, probabilities multiply.</p>

<div class="worked-example">
<h4>Repeated Independent Experiments</h4>
<p>Roll a fair die 10 times. What is the probability all rolls show 6?</p>
<p>If rolls are independent:</p>
$$P(\\text{all 6}) = P(\\text{roll 6}) \\times \\cdots \\times P(\\text{roll 6}) = (1/6)^{10} \\approx 1.65 \\times 10^{-8}$$
<p>This is incredibly small—about 1 in 60 million. Without independence, we would need to specify the joint distribution of all 10 rolls.</p>
</div>

<h3>Common Pitfall 1: Assuming Independence When There Is Dependence</h3>

<p>This is the most dangerous error in probability and statistics.</p>

<div class="worked-example">
<h4>Lottery Fallacy</h4>
<p>You play a lottery where you pick 6 numbers from 1-49. If the lottery is fair, what is the probability of winning?</p>
$$P(\\text{win}) = \\frac{1}{\\binom{49}{6}} = \\frac{1}{10,068,347}$$
<p>Now, suppose you lose the first week. Does this increase your chances next week? <em>No.</em> Each week is independent. A common fallacy: "I'm due to win" or "the numbers I didn't pick are more likely next time." They are not.</p>
</div>

<h3>Common Pitfall 2: Confusing Disjointness with Independence</h3>

<p>Disjoint events and independent events are different!</p>

<div class="concept-box">
<h4>Disjoint (Mutually Exclusive) Events</h4>
<p>\\(A \\cap B = \\emptyset\\), so they cannot both occur.</p>
<p>Example: "die shows 1" and "die shows 2"</p>
</div>

<div class="concept-box">
<h4>Independent Events</h4>
<p>\\(P(A \\cap B) = P(A) \\cdot P(B)\\), so knowing one tells you nothing about the other.</p>
<p>Example: "first die shows 1" and "second die shows 2"</p>
</div>

<p><strong>Key fact:</strong> If \\(A\\) and \\(B\\) are disjoint with \\(P(A), P(B) > 0\\), then they are <em>not</em> independent! (Because \\(P(A|B) = 0 \\neq P(A)\\).)</p>

<h3>Common Pitfall 3: Ignoring Conditional Dependencies</h3>

<p>Events can be independent unconditionally but dependent conditionally (or vice versa).</p>

<div class="worked-example">
<h4>Simpson's Paradox (Related to Conditional Independence)</h4>
<p>Two schools have the same overall graduation rate (80%). If you condition on student income level, School A has a higher graduation rate for poor students and for wealthy students. Yet overall rates are equal. This happens because the student populations differ in composition.</p>
<p>The point: always be careful about conditioning. A relationship can vanish or appear when you condition on a third variable.</p>
</div>

<h3>When to Assume Independence</h3>

<p><strong>Reasonable assumptions:</strong></p>
<ul>
<li>Repeated trials of a fair experiment (coin flips, dice rolls)</li>
<li>Measurements from different, unrelated sources</li>
<li>Processes with no causal connection (rainfall in two distant cities)</li>
</ul>

<p><strong>Questionable assumptions:</strong></p>
<ul>
<li>Correlated measurements (temperature over consecutive days)</li>
<li>Data with time trends</li>
<li>Events with common causes</li>
</ul>

<p>In data science and statistics, independence is often <strong>assumed</strong> to make problems tractable, but you should validate this assumption whenever possible.</p>
"""
    }
]
