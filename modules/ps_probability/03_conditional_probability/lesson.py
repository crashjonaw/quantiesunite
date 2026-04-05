TITLE = "Conditional Probability: Updating Beliefs with Evidence"

SECTIONS = [
    {
        "id": "cp_motivation",
        "title": "Why Conditioning Matters",
        "body": """
<div class="concept-box">
<h3>The Central Problem of Inference</h3>
<p>You receive a positive test for a disease. Does this mean you have the disease? Without conditioning, we cannot answer. <em>Conditional probability</em> is the mathematics of updating beliefs when we gain new information. It is the foundation of Bayesian statistics and machine learning.</p>
</div>

<h3>The Intuition</h3>

<p>Imagine the sample space \\(\\Omega\\) as a region. Initially, all outcomes in \\(\\Omega\\) are possible. But now you learn that event \\(B\\) has occurred. This eliminates all outcomes outside \\(B\\). You rescale: \\(B\\) becomes your new universe, and all probabilities are renormalized relative to it.</p>

<p>The conditional probability of event \\(A\\) given \\(B\\) is the fraction of \\(B\\) that overlaps with \\(A\\).</p>

<div class="worked-example">
<h4>Intuitive Example</h4>
<p>Roll a fair die. The sample space is \\(\\Omega = \\{1,2,3,4,5,6\\}\\), each outcome with probability \\(1/6\\).</p>
<p>You are told: "The roll is even." This means the outcome is in \\(B = \\{2,4,6\\}\\), eliminating 1, 3, 5.</p>
<p>Now, within the restricted space \\(B\\), each outcome is equally likely: \\(P(2|B) = P(4|B) = P(6|B) = 1/3\\).</p>
<p>What is the probability the roll was a 6, given it is even? It is \\(1/3\\).</p>
</div>
"""
    },
    {
        "id": "cp_definition",
        "title": "Definition and Basic Properties",
        "body": """
<h3>Formal Definition</h3>

<div class="concept-box">
<h4>Conditional Probability</h4>
<p>Given event \\(B\\) with \\(P(B) > 0\\), the <strong>conditional probability</strong> of event \\(A\\) given \\(B\\) is:</p>
$$P(A|B) = \\frac{P(A \\cap B)}{P(B)}$$
<p>This is a probability measure over a restricted sample space.</p>
</div>

<h3>Verification: A Probability Measure</h3>

<p>For fixed \\(B\\) with \\(P(B) > 0\\), the function \\(A \\mapsto P(A|B)\\) is itself a probability measure on \\(\\Omega\\). It satisfies:</p>

<ul>
<li><strong>Non-negativity:</strong> \\(P(A|B) \\geq 0\\) for all \\(A\\) (since \\(P(A \\cap B) \\geq 0\\) and \\(P(B) > 0\\))</li>
<li><strong>Normalization:</strong> \\(P(\\Omega|B) = P(\\Omega \\cap B) / P(B) = P(B) / P(B) = 1\\)</li>
<li><strong>Countable additivity:</strong> If \\(A_1, A_2, \\ldots\\) are disjoint, then \\(P(\\bigcup A_i | B) = \\sum P(A_i|B)\\)</li>
</ul>

<p>So conditioning does not break the axioms—it preserves the probability structure.</p>

<h3>Key Properties</h3>

<div class="concept-box">
<h4>1. Conditional Probability of the Conditioning Event</h4>
$$P(B|B) = \\frac{P(B \\cap B)}{P(B)} = \\frac{P(B)}{P(B)} = 1$$
<p>Given \\(B\\), the event \\(B\\) is certain.</p>
</div>

<div class="concept-box">
<h4>2. Conditional Probability of Disjoint Event</h4>
<p>If \\(A \\cap B = \\emptyset\\) (A and B are disjoint), then:</p>
$$P(A|B) = \\frac{P(\\emptyset)}{P(B)} = 0$$
<p>Given \\(B\\), the disjoint event \\(A\\) is impossible.</p>
</div>

<div class="concept-box">
<h4>3. Chain Rule (Multiplication Rule)</h4>
$$P(A \\cap B) = P(A|B) \\cdot P(B)$$
<p>Rearranging the definition, the joint probability equals the conditional probability times the marginal.</p>
</div>

<div class="worked-example">
<h4>Drawing Cards Without Replacement</h4>
<p>Draw two cards from a standard deck without replacement. What is the probability both are aces?</p>
<ul>
<li>\\(A_1\\) = first card is an ace: \\(P(A_1) = 4/52\\)</li>
<li>\\(A_2\\) = second card is an ace: \\(P(A_2|A_1) = 3/51\\) (given first was an ace)</li>
<li>By the chain rule: \\(P(A_1 \\cap A_2) = P(A_1) \\cdot P(A_2|A_1) = \\frac{4}{52} \\cdot \\frac{3}{51} = \\frac{12}{2652} = \\frac{1}{221}\\)</li>
</ul>
</div>
"""
    },
    {
        "id": "cp_bayes",
        "title": "Bayes' Rule and Total Probability",
        "body": """
<h3>Bayes' Rule: Inverting Conditioning</h3>

<p>Often we know \\(P(B|A)\\) but want \\(P(A|B)\\). Bayes' rule inverts the direction of conditioning.</p>

<div class="concept-box">
<h4>Bayes' Rule (Simple Form)</h4>
$$P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)}$$
<p><strong>Derivation:</strong> From the definition of conditional probability:</p>
$$P(A|B) = \\frac{P(A \\cap B)}{P(B)} = \\frac{P(B|A) \\cdot P(A)}{P(B)}$$
</div>

<div class="worked-example">
<h4>Medical Test: Bayes' Rule in Action</h4>
<p>A test for disease has:</p>
<ul>
<li>Sensitivity (true positive rate): \\(P(+|D) = 0.95\\)</li>
<li>Specificity (true negative rate): \\(P(-|D^c) = 0.90\\), so \\(P(+|D^c) = 0.10\\)</li>
<li>Disease prevalence: \\(P(D) = 0.01\\)</li>
</ul>
<p>You test positive. What is \\(P(D|+)\\)?</p>
<p>First, find \\(P(+)\\) using the law of total probability (below):</p>
$$P(+) = P(+|D) \\cdot P(D) + P(+|D^c) \\cdot P(D^c) = 0.95 \\times 0.01 + 0.10 \\times 0.99 = 0.0095 + 0.0990 = 0.1085$$
<p>Now apply Bayes:</p>
$$P(D|+) = \\frac{P(+|D) \\cdot P(D)}{P(+)} = \\frac{0.95 \\times 0.01}{0.1085} \\approx 0.0876$$
<p>Even with a positive test, you are only about 8.76% likely to have the disease! This counterintuitive result is the <em>base rate fallacy</em>: a high test sensitivity does not overcome a low disease prevalence.</p>
</div>

<h3>The Law of Total Probability</h3>

<p>If events \\(B_1, B_2, \\ldots, B_n\\) form a <strong>partition</strong> of \\(\\Omega\\) (they are disjoint and \\(\\bigcup B_i = \\Omega\\)), then for any event \\(A\\):</p>

<div class="concept-box">
<h4>Law of Total Probability</h4>
$$P(A) = \\sum_{i=1}^{n} P(A|B_i) \\cdot P(B_i)$$
<p>We "average" the conditional probabilities \\(P(A|B_i)\\), weighted by the probability of each partition element.</p>
</div>

<p><strong>Derivation:</strong> Since \\(A = \\bigcup_{i=1}^{n} (A \\cap B_i)\\) and the intersections are disjoint:</p>

$$P(A) = \\sum_{i=1}^{n} P(A \\cap B_i) = \\sum_{i=1}^{n} P(A|B_i) \\cdot P(B_i)$$

<div class="worked-example">
<h4>Factory Defect Rate</h4>
<p>A factory has two machines:</p>
<ul>
<li>Machine A produces 60% of items with 2% defect rate</li>
<li>Machine B produces 40% of items with 3% defect rate</li>
</ul>
<p>A randomly selected item is found to be defective. What is the probability it came from machine A?</p>
<p>First, find \\(P(\\text{defective})\\) by total probability:</p>
$$P(D) = P(D|A) \\cdot P(A) + P(D|B) \\cdot P(B) = 0.02 \\times 0.6 + 0.03 \\times 0.4 = 0.012 + 0.012 = 0.024$$
<p>Now use Bayes:</p>
$$P(A|D) = \\frac{P(D|A) \\cdot P(A)}{P(D)} = \\frac{0.02 \\times 0.6}{0.024} = \\frac{0.012}{0.024} = 0.5$$
</div>

<h3>Bayes' Rule with Multiple Events</h3>

<p>More generally, combining Bayes' rule with the law of total probability:</p>

<div class="concept-box">
<h4>Bayes' Rule (Extended Form)</h4>
<p>If \\(H_1, H_2, \\ldots, H_n\\) partition \\(\\Omega\\) and we observe event \\(E\\):</p>
$$P(H_i|E) = \\frac{P(E|H_i) \\cdot P(H_i)}{\\sum_{j=1}^{n} P(E|H_j) \\cdot P(H_j)}$$
<p>Here \\(H_i\\) are <em>hypotheses</em> (competing explanations) and \\(E\\) is <em>evidence</em>. Bayes' rule tells us how to update our belief in each hypothesis given the evidence.</p>
</div>

<h3>Terminology</h3>

<p>In Bayesian statistics:</p>
<ul>
<li>\\(P(H_i)\\): the <strong>prior probability</strong> of hypothesis \\(H_i\\)</li>
<li>\\(P(E|H_i)\\): the <strong>likelihood</strong> of the evidence given \\(H_i\\)</li>
<li>\\(P(H_i|E)\\): the <strong>posterior probability</strong> of \\(H_i\\) after observing \\(E\\)</li>
<li>\\(P(E)\\): the <em>total probability of the evidence</em>, computed by the law of total probability</li>
</ul>

<p>Bayes' rule formalizes how to update prior beliefs into posterior beliefs: <em>posterior ∝ likelihood × prior</em>.</p>
"""
    },
    {
        "id": "cp_independence_revisited",
        "title": "Independence Through Conditioning",
        "body": """
<h3>Independence: A Conditional Perspective</h3>

<p>Events \\(A\\) and \\(B\\) are independent if knowing one tells you nothing about the other. This can be expressed via conditioning:</p>

<div class="concept-box">
<h4>Independence via Conditional Probability</h4>
<p>\\(A\\) and \\(B\\) are independent if and only if:</p>
$$P(A|B) = P(A) \\quad \\text{and} \\quad P(B|A) = P(B)$$
<p>(assuming \\(P(A), P(B) > 0\\))</p>
<p>Equivalently: \\(P(A \\cap B) = P(A) \\cdot P(B)\\)</p>
</div>

<p><strong>Intuition:</strong> Learning that \\(B\\) occurred does not change your assessment of the probability of \\(A\\). The conditional probability equals the unconditional probability.</p>

<div class="worked-example">
<h4>Independent Dice Rolls</h4>
<p>Roll two fair dice. Let \\(A\\) = "first die is even" and \\(B\\) = "second die is 3 or higher".</p>
<ul>
<li>\\(P(A) = 1/2\\) (outcomes 2, 4, 6 out of 6)</li>
<li>\\(P(B) = 2/3\\) (outcomes 3, 4, 5, 6 out of 6)</li>
<li>\\(P(A \\cap B)\\) = outcomes where first is even AND second is ≥3 = 9 out of 36 = 1/4</li>
<li>\\(P(A) \\cdot P(B) = 1/2 \\times 2/3 = 1/3\\)... wait, that's not 1/4.</li>
</ul>
<p>Actually, let me recalculate \\(B\\). If \\(B\\) = "second die is 3 or higher" = {3,4,5,6} out of 6, then \\(P(B) = 4/6 = 2/3\\). But this isn't right for the calculation. Let me redefine: \\(B\\) = "second die is even" = {2,4,6}, so \\(P(B) = 1/2\\). Then:</li>
<li>\\(P(A \\cap B)\\) = (first even, second even) = 9 out of 36 = 1/4</li>
<li>\\(P(A) \\cdot P(B) = 1/2 \\times 1/2 = 1/4\\) ✓</li>
</ul>
<p>So \\(A\\) and \\(B\\) are independent.</p>
</div>

<h3>Conditional Independence</h3>

<p>Two events \\(A\\) and \\(B\\) can be dependent overall, but independent <em>given</em> a third event \\(C\\). This is called <strong>conditional independence</strong>.</p>

<div class="concept-box">
<h4>Conditional Independence</h4>
<p>\\(A\\) and \\(B\\) are <em>conditionally independent</em> given \\(C\\) (written \\(A \\perp\\!\\!\\perp B | C\\)) if:</p>
$$P(A \\cap B | C) = P(A|C) \\cdot P(B|C)$$
</div>

<div class="worked-example">
<h4>Rain and Wet Ground</h4>
<p>Let \\(R\\) = "it rained" and \\(W\\) = "the ground is wet". These are not independent: rain causes wet ground. But given \\(S\\) = "the sprinkler was on", \\(R\\) and \\(W\\) are more nearly conditionally independent (the wetness comes primarily from the sprinkler, so rain adds little additional information).</p>
</div>
"""
    }
]
