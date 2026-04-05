TITLE = "Counting and Combinatorics in Probability"

SECTIONS = [
    {
        "id": "counting_motivation",
        "title": "When Counting Is All We Need",
        "body": """
<div class="concept-box">
<h3>The Fundamental Counting Principle</h3>
<p>For many finite sample spaces where all outcomes are equally likely, probability reduces to counting:</p>
$$P(A) = \\frac{|A|}{|\\Omega|} = \\frac{\\text{number of favorable outcomes}}{\\text{total number of outcomes}}$$
<p>This is the classical definition of probability, used since the 17th century. It works beautifully when outcomes are equally likely, but requires careful counting.</p>
</div>

<h3>When Does This Apply?</h3>

<p>The formula above is valid when:</p>
<ul>
<li>The sample space is finite</li>
<li>All outcomes are equally likely (e.g., fair coin, fair die, randomly selecting from a set)</li>
</ul>

<p>In such cases, probability <em>is</em> combinatorics.</p>

<div class="worked-example">
<h4>Fair Die Example</h4>
<p>A fair 6-sided die has sample space \\(\\Omega = \\{1, 2, 3, 4, 5, 6\\}\\) with each outcome equally likely. Event \\(A\\) = "rolling an even number" = \\(\\{2, 4, 6\\}\\).</p>
$$P(A) = \\frac{|\\{2,4,6\\}|}{|\\{1,2,3,4,5,6\\}|} = \\frac{3}{6} = \\frac{1}{2}$$
</div>
"""
    },
    {
        "id": "counting_factorials_permutations",
        "title": "Factorials and Permutations",
        "body": """
<h3>Factorials: Arranging Distinct Objects</h3>

<div class="concept-box">
<h4>Factorial Definition</h4>
$$n! = n \\times (n-1) \\times (n-2) \\times \\cdots \\times 2 \\times 1$$
<p>with the convention \\(0! = 1\\) (empty product).</p>
<p>Example: \\(5! = 5 \\times 4 \\times 3 \\times 2 \\times 1 = 120\\)</p>
</div>

<p>The factorial counts the number of ways to arrange \\(n\\) distinct objects in a row.</p>

<div class="worked-example">
<h4>Arranging Books</h4>
<p>You have 4 distinct books. In how many ways can you arrange them on a shelf?</p>
<ul>
<li>First position: 4 choices</li>
<li>Second position: 3 remaining choices</li>
<li>Third position: 2 remaining choices</li>
<li>Fourth position: 1 remaining choice</li>
<li>Total: \\(4! = 4 \\times 3 \\times 2 \\times 1 = 24\\)</li>
</ul>
</div>

<h3>Permutations: Arranging a Subset</h3>

<p>Often, we choose \\(k\\) objects from \\(n\\) and arrange them. The order matters.</p>

<div class="concept-box">
<h4>Permutation Formula</h4>
<p>The number of ways to arrange \\(k\\) objects chosen from \\(n\\) distinct objects is:</p>
$$P(n,k) = \\text{or } {}^nP_k = \\frac{n!}{(n-k)!}$$
</div>

<p><strong>Intuition:</strong> For the first position, choose from \\(n\\) objects. For the second, choose from \\(n-1\\). Continue until \\(k\\) positions are filled:</p>

$$P(n,k) = n \\times (n-1) \\times \\cdots \\times (n-k+1) = \\frac{n!}{(n-k)!}$$

<div class="worked-example">
<h4>Presidential Lineup</h4>
<p>Select 3 officers (president, vice-president, treasurer) from 5 candidates. Order matters.</p>
$$P(5,3) = \\frac{5!}{(5-3)!} = \\frac{5!}{2!} = \\frac{120}{2} = 60$$
</div>

<h3>Special Cases</h3>

<ul>
<li>\\(P(n, n) = n!\\) (arranging all \\(n\\) objects)</li>
<li>\\(P(n, 1) = n\\) (choosing one object)</li>
<li>\\(P(n, 0) = 1\\) (empty arrangement)</li>
</ul>
"""
    },
    {
        "id": "counting_combinations",
        "title": "Combinations: Unordered Selection",
        "body": """
<h3>When Order Doesn't Matter</h3>

<p>If we select \\(k\\) objects from \\(n\\) but order does <em>not</em> matter (we form a set, not a sequence), we use <strong>combinations</strong>.</p>

<div class="concept-box">
<h4>Combination Formula</h4>
<p>The number of ways to choose \\(k\\) objects from \\(n\\) distinct objects (order irrelevant) is:</p>
$$\\binom{n}{k} = \\text{C}(n,k) = \\text{or } {}^nC_k = \\frac{n!}{k! (n-k)!}$$
<p>Read as "n choose k."</p>
</div>

<p><strong>Derivation:</strong> Start with \\(P(n,k)\\) permutations. Each unordered set of \\(k\\) objects corresponds to \\(k!\\) different orderings. So we divide:</p>

$$\\binom{n}{k} = \\frac{P(n,k)}{k!} = \\frac{n!/(n-k)!}{k!} = \\frac{n!}{k!(n-k)!}$$

<div class="worked-example">
<h4>Committee Selection</h4>
<p>Choose 3 people from 5 for a committee (no roles, so order doesn't matter).</p>
$$\\binom{5}{3} = \\frac{5!}{3! \\cdot 2!} = \\frac{120}{6 \\times 2} = 10$$
<p>Compare to the earlier example: \\(P(5,3) = 60\\) for a ranked lineup. We have \\(60 / (3!) = 60 / 6 = 10\\) unordered committees, because each committee corresponds to \\(3! = 6\\) possible rankings.</p>
</div>

<h3>Useful Properties of Binomial Coefficients</h3>

<div class="concept-box">
<h4>Symmetry</h4>
$$\\binom{n}{k} = \\binom{n}{n-k}$$
<p>Choosing \\(k\\) objects to include is the same as choosing \\(n-k\\) objects to exclude.</p>
</div>

<div class="concept-box">
<h4>Pascal's Identity</h4>
$$\\binom{n}{k} = \\binom{n-1}{k-1} + \\binom{n-1}{k}$$
<p>This recursive formula generates Pascal's triangle and is useful for computing binomial coefficients.</p>
</div>

<div class="concept-box">
<h4>The Binomial Theorem</h4>
$$(x + y)^n = \\sum_{k=0}^{n} \\binom{n}{k} x^k y^{n-k}$$
<p>The binomial coefficients appear as coefficients in the expansion of \\((x+y)^n\\).</p>
</div>

<h3>Edge Cases</h3>

<ul>
<li>\\(\\binom{n}{0} = 1\\) (one way to choose nothing)</li>
<li>\\(\\binom{n}{n} = 1\\) (one way to choose everything)</li>
<li>\\(\\binom{n}{1} = n\\) (n ways to choose one object)</li>
</ul>
"""
    },
    {
        "id": "counting_multinomial",
        "title": "Multinomial Coefficients and Extensions",
        "body": """
<h3>Beyond Binary: Multinomial Coefficients</h3>

<p>Binomial coefficients count ways to partition \\(n\\) objects into two groups (chosen and not chosen). Sometimes, we need to partition into more groups.</p>

<div class="concept-box">
<h4>Multinomial Coefficient</h4>
<p>The number of ways to partition \\(n\\) distinct objects into \\(r\\) disjoint groups of sizes \\(k_1, k_2, \\ldots, k_r\\) (where \\(k_1 + k_2 + \\cdots + k_r = n\\)) is:</p>
$$\\binom{n}{k_1, k_2, \\ldots, k_r} = \\frac{n!}{k_1! \\cdot k_2! \\cdot \\ldots \\cdot k_r!}$$
</div>

<p><strong>Derivation:</strong> Choose \\(k_1\\) objects for group 1: \\(\\binom{n}{k_1}\\) ways. Then choose \\(k_2\\) from the remaining \\(n - k_1\\): \\(\\binom{n-k_1}{k_2}\\) ways. Continue:</p>

$$\\binom{n}{k_1} \\cdot \\binom{n-k_1}{k_2} \\cdot \\binom{n-k_1-k_2}{k_3} \\cdots = \\frac{n!}{k_1!(n-k_1)!} \\cdot \\frac{(n-k_1)!}{k_2!(n-k_1-k_2)!} \\cdots = \\frac{n!}{k_1! k_2! \\cdots k_r!}$$

<div class="worked-example">
<h4>Anagram Counting</h4>
<p>How many distinct arrangements of the letters in MISSISSIPPI?</p>
<ul>
<li>Total letters: 11</li>
<li>Frequency: M appears 1 time, I appears 4 times, S appears 4 times, P appears 2 times</li>
</ul>
$$\\text{Arrangements} = \\binom{11}{1, 4, 4, 2} = \\frac{11!}{1! \\cdot 4! \\cdot 4! \\cdot 2!} = \\frac{39,916,800}{1 \\times 24 \\times 24 \\times 2} = \\frac{39,916,800}{1,152} = 34,650$$
</div>

<h3>The Multinomial Theorem</h3>

<p>Generalizing the binomial theorem:</p>

<div class="concept-box">
<h4>Multinomial Expansion</h4>
$$(x_1 + x_2 + \\cdots + x_r)^n = \\sum_{k_1+k_2+\\cdots+k_r=n} \\binom{n}{k_1, k_2, \\ldots, k_r} x_1^{k_1} x_2^{k_2} \\cdots x_r^{k_r}$$
<p>The multinomial coefficients are the coefficients in this expansion.</p>
</div>
"""
    },
    {
        "id": "counting_applications",
        "title": "Applications: Classic Probability Problems",
        "body": """
<h3>Counting Leading to Probability</h3>

<p>Once we know how to count, many probability problems reduce to arithmetic.</p>

<div class="worked-example">
<h4>The Birthday Problem</h4>
<p>In a room of \\(n\\) people, what is the probability at least two share a birthday?</p>
<p><strong>Solution:</strong> It is easier to compute the complement. Assume 365 days in a year and independence.</p>
<ul>
<li>Total ways to assign \\(n\\) people to days: \\(365^n\\)</li>
<li>Ways such that all have different birthdays: \\(365 \\times 364 \\times \\cdots \\times (365-n+1) = P(365, n)\\)</li>
</ul>
$$P(\\text{all different}) = \\frac{365 \\times 364 \\times \\cdots \\times (365-n+1)}{365^n}$$
$$P(\\text{at least one match}) = 1 - P(\\text{all different})$$
<p>For \\(n = 23\\): \\(P(\\text{match}) \\approx 0.507\\). Surprisingly, less than 25 people gives > 50% chance of a match!</p>
</div>

<div class="worked-example">
<h4>Poker Hand Probabilities</h4>
<p>In a 5-card hand from a standard 52-card deck:</p>
<ul>
<li>Total hands: \\(\\binom{52}{5} = 2,598,960\\)</li>
<li>Probability of a royal flush (A, K, Q, J, 10 of the same suit): \\(\\frac{4}{2,598,960} \\approx 1.54 \\times 10^{-6}\\)</li>
<li>Probability of four of a kind: \\(\\frac{624}{2,598,960} \\approx 0.00024\\)</li>
</ul>
</div>

<div class="worked-example">
<h4>Sampling Without Replacement</h4>
<p>Draw 3 cards from a deck without replacement. What is the probability all are aces?</p>
$$P(\\text{all aces}) = \\frac{4}{52} \\times \\frac{3}{51} \\times \\frac{2}{50} = \\frac{24}{132,600} = \\frac{1}{5,525}$$
<p>Alternatively, using counting:</p>
$$P(\\text{all aces}) = \\frac{\\text{ways to choose 3 aces from 4}}{\\text{ways to choose 3 cards from 52}} = \\frac{\\binom{4}{3}}{\\binom{52}{3}} = \\frac{4}{22,100} = \\frac{1}{5,525}$$
</div>

<h3>Inclusion-Exclusion with Counting</h3>

<p>For finite sample spaces with equally likely outcomes, inclusion-exclusion becomes:</p>

<div class="concept-box">
<h4>Counting-Based Inclusion-Exclusion</h4>
$$|A \\cup B| = |A| + |B| - |A \\cap B|$$
<p>which translates to:</p>
$$P(A \\cup B) = \\frac{|A| + |B| - |A \\cap B|}{|\\Omega|}$$
</div>

<div class="worked-example">
<h4>Counting Arrangements with Restrictions</h4>
<p>How many 4-digit numbers have at least one repeated digit?</p>
<ul>
<li>Total 4-digit numbers: \\(9 \\times 10^3 = 9,000\\) (first digit 1-9, others 0-9)</li>
<li>Numbers with all different digits: \\(9 \\times 9 \\times 8 \\times 7 = 4,536\\)</li>
<li>Numbers with at least one repeat: \\(9,000 - 4,536 = 4,464\\)</li>
<li>Probability: \\(4,464 / 9,000 \\approx 0.496\\)</li>
</ul>
</div>
"""
    }
]
