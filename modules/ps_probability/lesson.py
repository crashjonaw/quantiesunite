SECTIONS = [
    {
        "id": "ps_prob_motivation",
        "title": "Probability in the Real World",
        "content": """
<div class="concept-box">
<h3>Why Probability Matters</h3>
<p>Probability is the mathematical language for uncertainty. From drug efficacy trials to stock market crashes, from weather forecasting to quantum mechanics, probability underpins modern decision-making. This course builds probability from first principles—not as recipes, but as logical structures.</p>
</div>

<div class="example-box">
<h4>Real-World Problem</h4>
<p>A pharmaceutical company runs a clinical trial: 150 patients receive Drug A, 147 recover. Does this prove the drug works? How confident are we? Probability gives us precise answers—no hunches, no guesses.</p>
</div>

<h3>The Conceptual Journey Ahead</h3>

<p>We begin with <strong>Kolmogorov's axioms</strong>, the bedrock of all probability. These three simple rules generate every result in probability theory—from coin flips to weather models. Then we explore the concept of <strong>random experiments</strong>, <strong>events</strong>, and <strong>probability measures</strong>.</p>

<p>Probability is not about mystical unpredictability. It's about quantifying <em>our information</em> regarding possible outcomes. A coin flip has a definite outcome; we don't know it beforehand, so we assign probability. Imagine recording a coin flip on video, then watching it in slow motion—you could predict the outcome perfectly if you knew the initial conditions. But we don't, so probability captures our <em>epistemic uncertainty</em>.</p>

<h3>What You'll Learn</h3>
<ul>
<li>Kolmogorov axioms and their consequences</li>
<li>Sample spaces and events</li>
<li>Conditional probability and Bayes' rule</li>
<li>Independence of events</li>
<li>Combinatorial counting for discrete outcomes</li>
</ul>
"""
    },
    {
        "id": "ps_prob_axioms",
        "title": "Kolmogorov Axioms: The Foundation",
        "content": """
<h3>The Three Sacred Axioms</h3>

<p>In 1933, Andrey Kolmogorov proposed a minimal set of assumptions that would make probability rigorous. Everything follows from these three.</p>

<div class="formula-box">
<h4>Axiom 1: Non-negativity</h4>
<p>For any event \\(A\\) in the sample space \\(\\Omega\\):</p>
$$P(A) \\geq 0$$
</div>

<div class="formula-box">
<h4>Axiom 2: Unitarity</h4>
<p>The entire sample space has probability 1:</p>
$$P(\\Omega) = 1$$
</div>

<div class="formula-box">
<h4>Axiom 3: Countable Additivity</h4>
<p>For any countable collection of <em>disjoint</em> events \\(A_1, A_2, A_3, \\ldots\\):</p>
$$P\\left(\\bigcup_{i=1}^{\\infty} A_i\\right) = \\sum_{i=1}^{\\infty} P(A_i)$$
</div>

<h3>Why These Three Rules?</h3>

<p><strong>Axiom 1</strong> is intuitive: probability can't be negative. We can't be "less than zero" confident in an outcome.</p>

<p><strong>Axiom 2</strong> is a normalization: probabilities represent shares of total certainty. Something must happen, so the total probability is 1.</p>

<p><strong>Axiom 3</strong> is the workhorse. It says: if events don't overlap (disjoint), their probabilities add. This is non-obvious! It assumes a particular form of regularity—that probability is <em>countably additive</em>, not just finitely additive. This matters for probability on infinite spaces (like the real numbers).</p>

<h3>Immediate Consequences</h3>

<p>From these three axioms, we can derive everything:</p>

<div class="success-box">
<h4>Consequence 1: Empty Set Has Zero Probability</h4>
<p>Consider \\(A_1 = \\Omega\\) and \\(A_i = \\emptyset\\) for \\(i \\geq 2\\). These are disjoint, and \\(\\bigcup A_i = \\Omega\\). By Axiom 3:</p>
$$P(\\Omega) = P(\\Omega) + P(\\emptyset) + P(\\emptyset) + \\cdots$$
<p>Since \\(P(\\Omega) = 1\\) (Axiom 2), we must have:</p>
$$P(\\emptyset) = 0$$
</div>

<div class="success-box">
<h4>Consequence 2: Complement Rule</h4>
<p>For any event \\(A\\), the complement \\(A^c\\) is disjoint from \\(A\\) and \\(A \\cup A^c = \\Omega\\). By Axiom 3:</p>
$$P(A) + P(A^c) = P(\\Omega) = 1$$
$$P(A^c) = 1 - P(A)$$
</div>

<div class="success-box">
<h4>Consequence 3: Monotonicity</h4>
<p>If \\(A \\subseteq B\\), then \\(P(A) \\leq P(B)\\). This makes intuitive sense: a narrower event can't be more probable than a broader one containing it.</p>
</div>

<div class="success-box">
<h4>Consequence 4: Union Bound (Boole's Inequality)</h4>
<p>For any events \\(A_1, A_2, \\ldots\\):</p>
$$P\\left(\\bigcup_{i=1}^{n} A_i\\right) \\leq \\sum_{i=1}^{n} P(A_i)$$
<p>Equality holds only if the events are disjoint.</p>
</div>

<h3>Intuition: Why Countable Additivity?</h3>

<p>Why not just finite additivity? Consider an infinite sequence of coin flips. If we only had finite additivity, the probability of getting infinitely many heads would be ill-defined. Countable additivity lets us handle infinite sample spaces properly.</p>
"""
    },
    {
        "id": "ps_prob_sample_space",
        "title": "Sample Spaces and Events",
        "content": """
<h3>Building Blocks: Sample Space, Events, Outcomes</h3>

<p>A <strong>probability space</strong> is a triple \\((\\Omega, \\mathcal{F}, P)\\):</p>
<ul>
<li>\\(\\Omega\\): the <strong>sample space</strong> — all possible outcomes</li>
<li>\\(\\mathcal{F}\\): a \\(\\sigma\\)-algebra — a collection of events</li>
<li>\\(P\\): a probability measure — a function assigning numbers to events</li>
</ul>

<h3>Sample Space \\(\\Omega\\)</h3>

<p>The sample space is simply <em>all possible outcomes</em> of an experiment. For a fair die, \\(\\Omega = \\{1, 2, 3, 4, 5, 6\\}\\). For a coin, \\(\\Omega = \\{H, T\\}\\). For measuring temperature tomorrow, \\(\\Omega = \\mathbb{R}\\) (or at least some interval of real numbers).</p>

<div class="example-box">
<h4>Examples</h4>
<ul>
<li><strong>Single die roll:</strong> \\(\\Omega = \\{1,2,3,4,5,6\\}\\) — finite</li>
<li><strong>Two coin flips:</strong> \\(\\Omega = \\{HH, HT, TH, TT\\}\\) — finite</li>
<li><strong>Waiting time until next phone call:</strong> \\(\\Omega = [0, \\infty)\\) — infinite</li>
<li><strong>Temperature readings over a month:</strong> \\(\\Omega = \\mathbb{R}^{30}\\) — very high-dimensional</li>
</ul>
</div>

<h3>Events: Subsets of \\(\\Omega\\)</h3>

<p>An <strong>event</strong> is any subset of \\(\\Omega\\) (though in measure-theoretic probability, not all subsets; only those in \\(\\mathcal{F}\\)). An event occurs if the outcome lies in that subset.</p>

<div class="example-box">
<h4>Dice Example</h4>
<p>For a die roll, \\(\\Omega = \\{1,2,3,4,5,6\\}\\). Some events:</p>
<ul>
<li>\\(A = \\{1\\}\\): rolling a 1</li>
<li>\\(B = \\{2,4,6\\}\\): rolling an even number</li>
<li>\\(C = \\{4,5,6\\}\\): rolling at least 4</li>
<li>\\(\\Omega = \\{1,2,3,4,5,6\\}\\): rolling something (certain)</li>
<li>\\(\\emptyset\\): rolling nothing (impossible)</li>
</ul>
</div>

<h3>Event Operations</h3>

<p>Events combine using set operations:</p>

<div class="formula-box">
<h4>Union: \\(A \\cup B\\)</h4>
<p>\\(A \\cup B\\) occurs if \\(A\\) happens <em>or</em> \\(B\\) happens (or both).</p>
</div>

<div class="formula-box">
<h4>Intersection: \\(A \\cap B\\)</h4>
<p>\\(A \\cap B\\) occurs if \\(A\\) <em>and</em> \\(B\\) both happen.</p>
</div>

<div class="formula-box">
<h4>Complement: \\(A^c\\)</h4>
<p>\\(A^c\\) occurs if \\(A\\) does not occur.</p>
</div>

<div class="example-box">
<h4>Set Operations Example</h4>
<p>With the die: \\(B = \\{2,4,6\\}\\) (even), \\(C = \\{4,5,6\\}\\) (≥4)</p>
<ul>
<li>\\(B \\cup C = \\{2,4,5,6\\}\\) — even <em>or</em> at least 4</li>
<li>\\(B \\cap C = \\{4,6\\}\\) — even <em>and</em> at least 4</li>
<li>\\(B^c = \\{1,3,5\\}\\) — odd</li>
</ul>
</div>

<h3>The \\(\\sigma\\)-Algebra \\(\\mathcal{F}\\)</h3>

<p>In measure-theoretic probability, not every subset of \\(\\Omega\\) is necessarily an event. We restrict to a \\(\\sigma\\)-algebra \\(\\mathcal{F}\\), which is a collection of subsets satisfying:</p>
<ol>
<li>\\(\\Omega \\in \\mathcal{F}\\)</li>
<li>If \\(A \\in \\mathcal{F}\\), then \\(A^c \\in \\mathcal{F}\\)</li>
<li>If \\(A_1, A_2, \\ldots \\in \\mathcal{F}\\), then \\(\\bigcup A_i \\in \\mathcal{F}\\)</li>
</ol>

<p>For discrete sample spaces (like a die), we usually take \\(\\mathcal{F}\\) to be the <em>power set</em> — all subsets. For continuous spaces (like \\(\\mathbb{R}\\)), we take the <strong>Borel \\(\\sigma\\)-algebra</strong>, which includes intervals and countable unions/intersections of intervals, but excludes pathological subsets that have no natural size.</p>

<div class="warning-box">
<h4>Why This Matters</h4>
<p>On \\(\\mathbb{R}\\), you cannot assign probability to <em>every</em> subset consistently. Some sets (like non-measurable sets) have no well-defined probability. The Borel \\(\\sigma\\)-algebra is the minimal collection we need to describe reasonable events.</p>
</div>
"""
    },
    {
        "id": "ps_prob_conditional",
        "title": "Conditional Probability",
        "content": """
<h3>The Essence: Updating Beliefs</h3>

<p>Conditional probability is how we <em>update</em> our beliefs when we gain new information. If you know event \\(B\\) has occurred, how does this change your assessment of event \\(A\\)?</p>

<h3>Definition</h3>

<div class="formula-box">
<h4>Conditional Probability</h4>
<p>Given \\(P(B) > 0\\), the conditional probability of \\(A\\) given \\(B\\) is:</p>
$$P(A|B) = \\frac{P(A \\cap B)}{P(B)}$$
</div>

<h3>Intuition via Restriction</h3>

<p>Imagine the sample space \\(\\Omega\\) as a region. Event \\(B\\) carves out a sub-region. Given that \\(B\\) occurred, we now treat \\(B\\) as our new sample space. The probability of \\(A\\) given \\(B\\) is the fraction of \\(B\\) that overlaps with \\(A\\):</p>

$$P(A|B) = \\frac{\\text{size of } A \\cap B}{\\text{size of } B} = \\frac{P(A \\cap B)}{P(B)}$$

<div class="example-box">
<h4>Disease Testing</h4>
<p>A test has 95% sensitivity (correctly identifies sick people) and 90% specificity (correctly identifies healthy people). The disease affects 1% of the population.</p>
<ul>
<li>\\(D\\): person has disease</li>
<li>\\(+\\): test is positive</li>
</ul>
<p>You test positive. What is the probability you are actually sick?</p>
<p>We know:</p>
<ul>
<li>\\(P(D) = 0.01\\)</li>
<li>\\(P(+|D) = 0.95\\)</li>
<li>\\(P(+|D^c) = 1 - 0.90 = 0.10\\)</li>
</ul>
<p>We want \\(P(D|+)\\). Using the definition:</p>
$$P(D|+) = \\frac{P(+ \\cap D)}{P(+)}$$
</div>

<h3>The Multiplication Rule</h3>

<p>Rearranging the definition of conditional probability:</p>

<div class="formula-box">
<h4>Multiplication Rule</h4>
$$P(A \\cap B) = P(A|B) \\cdot P(B)$$
</div>

<p>More generally, for a sequence of events:</p>

$$P(A_1 \\cap A_2 \\cap \\cdots \\cap A_n) = P(A_1) \\cdot P(A_2|A_1) \\cdot P(A_3|A_1 \\cap A_2) \\cdots P(A_n | A_1 \\cap \\cdots \\cap A_{n-1})$$

<h3>Bayes' Rule</h3>

<p>From the definition of conditional probability, we can flip the conditioning:</p>

<div class="formula-box">
<h4>Bayes' Rule (Simple Form)</h4>
$$P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)}$$
</div>

<p>This inverts the conditional direction. If we know \\(P(B|A)\\), we can find \\(P(A|B)\\) using the base rate \\(P(A)\\).</p>

<h3>The Law of Total Probability</h3>

<p>If \\(B_1, B_2, \\ldots, B_n\\) partition the sample space (disjoint and cover \\(\\Omega\\)), then:</p>

<div class="formula-box">
<h4>Law of Total Probability</h4>
$$P(A) = \\sum_{i=1}^{n} P(A|B_i) \\cdot P(B_i)$$
</div>

<p>This is the key step in computing \\(P(B)\\) in Bayes' rule when we know \\(P(B|A_i)\\) for all cases \\(A_i\\).</p>

<div class="example-box">
<h4>Disease Testing (Continued)</h4>
<p>First, find \\(P(+)\\) using total probability. \\(D\\) and \\(D^c\\) partition \\(\\Omega\\):</p>
$$P(+) = P(+|D) \\cdot P(D) + P(+|D^c) \\cdot P(D^c)$$
$$= 0.95 \\times 0.01 + 0.10 \\times 0.99$$
$$= 0.0095 + 0.0990 = 0.1085$$
<p>Now apply Bayes:</p>
$$P(D|+) = \\frac{P(+|D) \\cdot P(D)}{P(+)} = \\frac{0.95 \\times 0.01}{0.1085} = \\frac{0.0095}{0.1085} \\approx 0.0876$$
<p>Even with a positive test, you are only approximately 8.76% likely to have the disease! This counterintuitive result—called the <em>base rate fallacy</em>—arises because the disease is rare.</p>
</div>
"""
    },
    {
        "id": "ps_prob_independence",
        "title": "Independence of Events",
        "content": """
<h3>When Events Don't Affect Each Other</h3>

<p>Two events are <strong>independent</strong> if knowing one occurred tells us nothing about the other. Formally:</p>

<div class="formula-box">
<h4>Independence</h4>
<p>Events \\(A\\) and \\(B\\) are independent if:</p>
$$P(A \\cap B) = P(A) \\cdot P(B)$$
</div>

<p>Equivalently (when \\(P(B) > 0\\)):</p>
$$P(A|B) = P(A)$$

<p>That is, knowing \\(B\\) occurred does not change the probability of \\(A\\).</p>

<h3>Intuition</h3>

<p>Independence is not about logical separation; it is probabilistic. Two coin flips are independent: the first flip does not affect the second. But if you flip a coin and look at whether it landed heads (\\(A\\)) and whether you dropped it on your foot (\\(B\\)), these might be correlated—a heads flip might be less likely to cause a dropped coin.</p>

<div class="example-box">
<h4>Fair Dice</h4>
<p>Roll two fair dice. Let:</p>
<ul>
<li>\\(A\\): first die is even</li>
<li>\\(B\\): second die is even</li>
</ul>
<p>Then \\(P(A) = 0.5\\) and \\(P(B) = 0.5\\). The events are independent:</p>
$$P(A \\cap B) = \\frac{\\text{# of (even, even) outcomes}}{36} = \\frac{9}{36} = \\frac{1}{4}$$
$$P(A) \\cdot P(B) = 0.5 \\times 0.5 = 0.25 \\checkmark$$
</div>

<h3>Pairwise vs. Mutual Independence</h3>

<p>For three or more events, we must distinguish:</p>

<div class="formula-box">
<h4>Pairwise Independence</h4>
<p>Events \\(A_1, A_2, A_3\\) are <em>pairwise independent</em> if:</p>
$$P(A_i \\cap A_j) = P(A_i) \\cdot P(A_j) \\text{ for all } i \\neq j$$
</div>

<div class="formula-box">
<h4>Mutual Independence</h4>
<p>Events \\(A_1, A_2, A_3\\) are <em>mutually independent</em> if pairwise independence holds, and additionally:</p>
$$P(A_1 \\cap A_2 \\cap A_3) = P(A_1) \\cdot P(A_2) \\cdot P(A_3)$$
</div>

<p>Pairwise independence does <em>not</em> imply mutual independence! You can have three events that are pairwise independent but not mutually independent.</p>

<div class="example-box">
<h4>A Famous Counterexample</h4>
<p>Flip two fair coins. Define:</p>
<ul>
<li>\\(A\\): first coin is heads</li>
<li>\\(B\\): second coin is heads</li>
<li>\\(C\\): the two coins match (both H or both T)</li>
</ul>
<p>Then \\(A\\) and \\(B\\) are independent, \\(A\\) and \\(C\\) are independent, and \\(B\\) and \\(C\\) are independent.</p>
<p>But \\(P(A \\cap B \\cap C) = P(\\text{HH}) = 0.25\\), while \\(P(A) \\cdot P(B) \\cdot P(C) = 0.125\\). Not equal! So they are not mutually independent.</p>
</div>

<h3>Why Independence Matters</h3>

<p>Independence simplifies calculations enormously. If \\(A_1, \\ldots, A_n\\) are mutually independent:</p>

$$P(A_1 \\cap \\cdots \\cap A_n) = P(A_1) \\cdots P(A_n)$$

<p>Without independence, we would need the full joint distribution—exponentially more data. This is why we make independence assumptions in statistics and data science.</p>
"""
    },
    {
        "id": "ps_prob_combinatorics",
        "title": "Counting: Combinatorics for Probability",
        "content": """
<h3>When All Outcomes Are Equally Likely</h3>

<p>For many finite sample spaces, all outcomes are equally likely. Then:</p>

$$P(A) = \\frac{\\text{number of outcomes in } A}{\\text{total number of outcomes}}$$

<p>This reduces probability to <em>counting</em>. So we need efficient counting formulas.</p>

<h3>Factorials and Permutations</h3>

<div class="formula-box">
<h4>Factorial</h4>
$$n! = n \\times (n-1) \\times \\cdots \\times 2 \\times 1$$
<p>with the convention \\(0! = 1\\).</p>
</div>

<div class="formula-box">
<h4>Permutations</h4>
<p>The number of ways to arrange \\(k\\) objects from \\(n\\) objects (order matters):</p>
$$P(n,k) = \\frac{n!}{(n-k)!}$$
</div>

<div class="example-box">
<h4>Permutation Example</h4>
<p>Choose 3 people from 5 for a lineup (president, VP, treasurer):</p>
$$P(5,3) = \\frac{5!}{2!} = \\frac{120}{2} = 60$$
</div>

<h3>Combinations</h3>

<p>Often, order does not matter. Choosing a subset is a <strong>combination</strong>.</p>

<div class="formula-box">
<h4>Combinations</h4>
<p>The number of ways to choose \\(k\\) objects from \\(n\\) (order irrelevant):</p>
$$\\binom{n}{k} = \\frac{n!}{k!(n-k)!}$$
<p>Read as "n choose k."</p>
</div>

<div class="example-box">
<h4>Combination Example</h4>
<p>Choose 3 people from 5 for a committee (no hierarchy):</p>
$$\\binom{5}{3} = \\frac{5!}{3! \\cdot 2!} = \\frac{120}{6 \\times 2} = 10$$
</div>

<h3>Multinomial Coefficients</h3>

<p>Generalizing combinations: partition \\(n\\) objects into groups of sizes \\(k_1, k_2, \\ldots, k_r\\) (where \\(\\sum k_i = n\\)).</p>

<div class="formula-box">
<h4>Multinomial Coefficient</h4>
$$\\binom{n}{k_1, k_2, \\ldots, k_r} = \\frac{n!}{k_1! k_2! \\cdots k_r!}$$
</div>

<div class="example-box">
<h4>Multinomial Example</h4>
<p>Arrange the letters in MISSISSIPPI (11 letters: 1 M, 4 I, 4 S, 2 P):</p>
$$\\binom{11}{1,4,4,2} = \\frac{11!}{1! \\cdot 4! \\cdot 4! \\cdot 2!} = \\frac{39916800}{1 \\times 24 \\times 24 \\times 2} = 34650$$
</div>

<h3>Applications: Discrete Probability Calculations</h3>

<div class="example-box">
<h4>Birthday Problem</h4>
<p>In a room of \\(n\\) people, what is the probability at least two share a birthday?</p>
<p>It is easier to compute the complement:</p>
$$P(\\text{all different}) = \\frac{365 \\times 364 \\times \\cdots \\times (365-n+1)}{365^n}$$
<p>For \\(n=23\\), this is about 0.49, so \\(P(\\text{at least one match}) \\approx 0.51\\). Surprisingly high!</p>
</div>

<div class="example-box">
<h4>Poker Hands</h4>
<p>Total 5-card hands: \\(\\binom{52}{5} = 2,598,960\\).</p>
<p>Royal flush (A,K,Q,J,10 of same suit): 4 hands. Probability: \\(\\frac{4}{2598960} \\approx 1.5 \\times 10^{-6}\\).</p>
</div>

<h3>Binomial Coefficient Properties</h3>

<p>The binomial coefficients satisfy useful identities:</p>

<div class="formula-box">
<h4>Symmetry</h4>
$$\\binom{n}{k} = \\binom{n}{n-k}$$
</div>

<div class="formula-box">
<h4>Pascal Identity</h4>
$$\\binom{n}{k} = \\binom{n-1}{k-1} + \\binom{n-1}{k}$$
<p>This generates Pascal's triangle.</p>
</div>

<div class="formula-box">
<h4>Binomial Theorem</h4>
$$(x+y)^n = \\sum_{k=0}^{n} \\binom{n}{k} x^k y^{n-k}$$
</div>
"""
    },
    {
        "id": "ps_prob_summary",
        "title": "Synthesis and Key Insights",
        "content": """
<h3>From Axioms to Real-World Application</h3>

<p>We have traveled from Kolmogorov's three axioms to practical counting and Bayes' rule. Let us synthesize:</p>

<div class="concept-box">
<h4>The Probability Foundation</h4>
<ol>
<li><strong>Kolmogorov axioms</strong> → non-negativity, normalization, countable additivity</li>
<li><strong>Sample spaces and events</strong> → rigor in defining what we are measuring</li>
<li><strong>Conditional probability</strong> → updating beliefs from evidence</li>
<li><strong>Bayes' rule</strong> → inverting conditional probabilities</li>
<li><strong>Independence</strong> → identifying when events do not interact</li>
<li><strong>Combinatorics</strong> → counting outcomes when equally likely</li>
</ol>
</div>

<h3>Common Pitfalls</h3>

<div class="warning-box">
<h4>Pitfall 1: Assuming Independence</h4>
<p>The biggest error: treating dependent events as independent. Always ask: does knowing one event change the probability of another?</p>
</div>

<div class="warning-box">
<h4>Pitfall 2: Base Rate Blindness</h4>
<p>When applying Bayes' rule, neglecting \\(P(A)\\) (the prior) is fatal. A high \\(P(B|A)\\) does not mean \\(P(A|B)\\) is high if \\(A\\) is rare.</p>
</div>

<div class="warning-box">
<h4>Pitfall 3: Confusing \\(P(A|B)\\) and \\(P(B|A)\\)</h4>
<p>These are not the same. \\(P(\\text{raining}|\\text{wet ground})\\) is not equal to \\(P(\\text{wet ground}|\\text{raining})\\).</p>
</div>

<h3>Looking Ahead</h3>

<p>Probability is now in your hands. Next, we build <strong>random variables</strong> — functions from outcomes to numbers. Random variables let us assign numerical meaning to experiments, and from them, we will derive entire distributions. Then we will explore expectation, variance, and the remarkable Central Limit Theorem.</p>
"""
    }
]
