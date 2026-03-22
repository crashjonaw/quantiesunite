SECTIONS = [
    {
        "title": "Basic Probability Concepts and Sample Space",
        "body": """
<p><strong>What is Probability?</strong></p>
<p>Probability is a measure of how likely something is to happen. It tells us the chance or likelihood of an event occurring.</p>

<p><strong>Key Terms:</strong></p>
<ul>
<li><strong>Experiment:</strong> A process with an uncertain outcome (e.g., rolling a die, flipping a coin)</li>
<li><strong>Outcome:</strong> A possible result of an experiment (e.g., getting a 4 when rolling a die)</li>
<li><strong>Event:</strong> A set of one or more outcomes (e.g., getting an even number)</li>
<li><strong>Sample Space:</strong> The set of ALL possible outcomes</li>
</ul>

<div class='example-box'>
<p><strong>Example: Rolling a die</strong></p>
<pre class='code-block'>
Experiment: Roll a standard 6-sided die

Sample Space (all possible outcomes):
{1, 2, 3, 4, 5, 6}

Possible Events:
- Getting a 4: {4}
- Getting an even number: {2, 4, 6}
- Getting a number greater than 3: {4, 5, 6}
- Getting a 1 or 6: {1, 6}
</pre>
</div>

<div class='example-box'>
<p><strong>Example: Flipping a coin</strong></p>
<pre class='code-block'>
Experiment: Flip a coin

Sample Space:
{Head, Tail}

Possible Events:
- Getting Heads: {Head}
- Getting Tails: {Tail}
</pre>
</div>

<div class='example-box'>
<p><strong>Example: Spinning a spinner</strong></p>
<pre class='code-block'>
A spinner has 4 equal sections: Red, Blue, Green, Yellow

Sample Space:
{Red, Blue, Green, Yellow}

Events might be:
- Getting a warm color: {Red, Yellow}
- Getting Blue: {Blue}
- Getting a primary color: {Red, Blue, Yellow}
</pre>
</div>

<p><strong>Equally Likely Outcomes:</strong></p>
<p>In many experiments, each outcome is equally likely. For example, with a fair coin or fair die, each outcome has the same chance of occurring.</p>

<div class='example-box'>
<p><strong>Fair vs Unfair:</strong></p>
<pre class='code-block'>
Fair die: Each number (1-6) has equal chance: 1/6
Unfair die: Some numbers might be weighted to occur more often

Fair coin: Heads and Tails equally likely: 1/2 each
Biased coin: One side might be weighted
</pre>
</div>
"""
    },
    {
        "title": "Theoretical Probability",
        "body": """
<p><strong>Theoretical Probability</strong> is calculated based on mathematical reasoning about the structure of the experiment (assuming fair/unbiased equipment).</p>

<p><strong>Formula: P(event) = Number of favorable outcomes / Total number of possible outcomes</strong></p>

<div class='example-box'>
<p><strong>Example 1: Rolling a die</strong></p>
<pre class='code-block'>
What is the probability of rolling a 4?

Total possible outcomes: 6 (the die shows 1, 2, 3, 4, 5, or 6)
Favorable outcomes (rolling a 4): 1

P(rolling a 4) = 1/6 ≈ 0.167 or about 16.7%
</pre>
</div>

<div class='example-box'>
<p><strong>Example 2: Rolling an even number</strong></p>
<pre class='code-block'>
What is the probability of rolling an even number?

Total possible outcomes: 6
Favorable outcomes (even numbers): 3 (the numbers 2, 4, 6)

P(even) = 3/6 = 1/2 = 0.5 or 50%
</pre>
</div>

<div class='example-box'>
<p><strong>Example 3: Picking from a bag</strong></p>
<pre class='code-block'>
A bag contains: 3 red balls, 2 blue balls, 5 green balls

Total balls: 10

P(red) = 3/10 = 0.3 or 30%
P(blue) = 2/10 = 1/5 = 0.2 or 20%
P(green) = 5/10 = 1/2 = 0.5 or 50%

Check: 0.3 + 0.2 + 0.5 = 1.0 ✓ (probabilities must sum to 1)
</pre>
</div>

<p><strong>The Probability Scale:</strong></p>
<p>All probabilities are between 0 and 1 (or 0% and 100%).</p>

<div class='example-box'>
<p><strong>Understanding the scale:</strong></p>
<pre class='code-block'>
Probability 0 (0%): Impossible event - will never happen
Probability 0.25 (25%): Unlikely
Probability 0.5 (50%): Even chance (equally likely to happen or not)
Probability 0.75 (75%): Likely
Probability 1 (100%): Certain - will definitely happen

Examples:
- Getting a 7 on a standard die: P = 0 (impossible)
- Getting a number from 1-6 on a die: P = 1 (certain)
- Getting heads on a fair coin: P = 0.5 (even chance)
</pre>
</div>

<p><strong>The Complement Rule:</strong></p>
<p>If P(event happens) = p, then P(event doesn't happen) = 1 - p</p>

<div class='example-box'>
<p><strong>Examples:</strong></p>
<pre class='code-block'>
P(rolling a 4) = 1/6
P(NOT rolling a 4) = 1 - 1/6 = 5/6

P(red ball) = 3/10
P(NOT red ball) = 1 - 3/10 = 7/10

P(heads) = 1/2
P(NOT heads, i.e., tails) = 1 - 1/2 = 1/2
</pre>
</div>
"""
    },
    {
        "title": "Experimental Probability",
        "body": """
<p><strong>Experimental Probability</strong> is based on actually performing the experiment and recording the results.</p>

<p><strong>Formula: P(event) = Number of times event occurred / Total number of trials</strong></p>

<p>This is also called <strong>relative frequency</strong> or <strong>observed probability</strong>.</p>

<div class='example-box'>
<p><strong>Example: Flipping a coin 100 times</strong></p>
<pre class='code-block'>
Experiment: Flip a fair coin 100 times

Results:
- Heads: 52 times
- Tails: 48 times

Experimental probability:
P(Heads) = 52/100 = 0.52 or 52%
P(Tails) = 48/100 = 0.48 or 48%

Theoretical probability:
P(Heads) = 1/2 = 0.5 or 50%
P(Tails) = 1/2 = 0.5 or 50%

The experimental results are close to theoretical,
with small differences due to chance.
</pre>
</div>

<div class='example-box'>
<p><strong>Example: Rolling a die 60 times</strong></p>
<pre class='code-block'>
Rolling a die and recording results:

Number | Times | Experimental | Theoretical
        | rolled| Probability | Probability
--------|-------|-------------|------------
   1    |   12  |   12/60 = 0.2|    1/6 ≈ 0.167
   2    |   10  |   10/60 ≈ 0.167| 1/6 ≈ 0.167
   3    |   11  |   11/60 ≈ 0.183| 1/6 ≈ 0.167
   4    |    9  |    9/60 = 0.15| 1/6 ≈ 0.167
   5    |   10  |   10/60 ≈ 0.167| 1/6 ≈ 0.167
   6    |    8  |    8/60 ≈ 0.133| 1/6 ≈ 0.167

Total: 60 trials

Notice the experimental results vary from theoretical,
but are reasonably close.
</pre>
</div>

<p><strong>The Law of Large Numbers:</strong></p>
<p>As we perform more and more trials, the experimental probability gets closer and closer to the theoretical probability.</p>

<div class='example-box'>
<p><strong>Coin flip example:</strong></p>
<pre class='code-block'>
After 10 flips: Got 7 heads, so P = 7/10 = 0.7 (far from 0.5)
After 100 flips: Got 52 heads, so P = 52/100 = 0.52 (closer to 0.5)
After 1000 flips: Got 503 heads, so P = 503/1000 = 0.503 (very close to 0.5)

With more trials, the experimental probability
approaches the theoretical probability!
</pre>
</div>

<p><strong>When to Use Which:</strong></p>
<ul>
<li><strong>Theoretical:</strong> When the equipment is fair and we can count outcomes mathematically</li>
<li><strong>Experimental:</strong> When equipment might be biased, or to verify theoretical predictions</li>
</ul>
"""
    },
    {
        "title": "Simple Combined Events",
        "body": """
<p><strong>Combined Events</strong> involve multiple outcomes or multiple experiments happening together.</p>

<p><strong>Two-Stage Experiments:</strong></p>

<div class='example-box'>
<p><strong>Example 1: Coin then die</strong></p>
<pre class='code-block'>
Flip a coin, then roll a die.

Sample Space:
{(H,1), (H,2), (H,3), (H,4), (H,5), (H,6),
 (T,1), (T,2), (T,3), (T,4), (T,5), (T,6)}

Total outcomes: 2 × 6 = 12

P(Heads and 4) = 1/12
P(Tails and even number) = P(T) × P(even) = 1/2 × 3/6 = 3/12 = 1/4
</pre>
</div>

<div class='example-box'>
<p><strong>Example 2: Spinner twice</strong></p>
<pre class='code-block'>
A spinner has Red, Blue, Green.
Spin twice (without replacing the arrow between spins).

Sample Space:
{(R,R), (R,B), (R,G), (B,R), (B,B), (B,G), (G,R), (G,B), (G,G)}

Total outcomes: 3 × 3 = 9

P(first Red, second Blue) = 1/9
P(both Red) = 1/9
P(at least one Red) = (R,R), (R,B), (R,G), (B,R), (G,R) = 5/9
</pre>
</div>

<p><strong>Using Tree Diagrams:</strong></p>

<div class='example-box'>
<p><strong>Example: Coin then die</strong></p>
<pre class='code-block'>
                    Start
                    /  \
                   H    T
                  / \    / \
                1-6  1-6 1-6  1-6

Each path represents an outcome.
Total paths = 2 × 6 = 12

P(H and 5) = 1/12
P(any result) = 12/12 = 1
</pre>
</div>

<p><strong>The Multiplication Rule for Independent Events:</strong></p>
<p><strong>P(A and B) = P(A) × P(B)</strong></p>
<p>(when A and B are independent - one doesn't affect the other)</p>

<div class='example-box'>
<p><strong>Example: Rolling two dice</strong></p>
<pre class='code-block'>
What is P(both dice show 3)?

P(first die is 3) = 1/6
P(second die is 3) = 1/6

P(both are 3) = 1/6 × 1/6 = 1/36

What is P(first is 3, second is even)?

P(first is 3) = 1/6
P(second is even) = 3/6 = 1/2

P(first is 3 AND second is even) = 1/6 × 1/2 = 1/12
</pre>
</div>

<p><strong>The Addition Rule for Mutually Exclusive Events:</strong></p>
<p><strong>P(A or B) = P(A) + P(B)</strong></p>
<p>(when A and B cannot both happen - they're mutually exclusive)</p>

<div class='example-box'>
<p><strong>Example: Rolling a die</strong></p>
<pre class='code-block'>
What is P(rolling a 2 OR a 5)?

P(rolling a 2) = 1/6
P(rolling a 5) = 1/6

These cannot both happen at once, so:
P(2 or 5) = 1/6 + 1/6 = 2/6 = 1/3

What is P(rolling odd)?

Odd numbers: 1, 3, 5
P(1) = 1/6, P(3) = 1/6, P(5) = 1/6

P(odd) = 1/6 + 1/6 + 1/6 = 3/6 = 1/2
</pre>
</div>
"""
    },
    {
        "title": "Probability and Risk Assessment",
        "body": """
<p><strong>Real-World Applications of Probability:</strong></p>
<p>Probability is used in many real-world situations to assess risk and make decisions.</p>

<div class='example-box'>
<p><strong>Example 1: Weather forecasting</strong></p>
<pre class='code-block'>
A weather report says "30% chance of rain tomorrow"

This means:
- P(rain) = 0.3 or 30%
- P(no rain) = 0.7 or 70%

The weather is more likely NOT to rain.
</pre>
</div>

<div class='example-box'>
<p><strong>Example 2: Lottery odds</strong></p>
<pre class='code-block'>
A lottery might have 1 in 1,000,000 chance of winning.

P(winning) = 1/1,000,000 = 0.000001 = 0.0001%

This is an extremely small probability.
</pre>
</div>

<div class='example-box'>
<p><strong>Example 3: Medical test accuracy</strong></p>
<pre class='code-block'>
A medical test is 95% accurate.

This means:
- If you have the disease, it correctly identifies it
  95% of the time (5% false negatives)
- If you don't have the disease, it correctly says no
  95% of the time (5% false positives)
</pre>
</div>

<p><strong>Understanding Risk:</strong></p>
<ul>
<li><strong>High probability (close to 1):</strong> Very likely to happen - high risk or high chance</li>
<li><strong>Low probability (close to 0):</strong> Very unlikely - low risk or rare chance</li>
<li><strong>Probability 0.5:</strong> Even chance - 50/50</li>
</ul>

<p><strong>Misunderstandings About Probability:</strong></p>

<div class='example-box'>
<p><strong>The "Hot Hand" Fallacy</strong></p>
<pre class='code-block'>
Mistake: If a coin shows heads 5 times in a row,
tails must be due next.

Reality: The coin has no memory.
P(heads on next flip) is still 0.5

Each flip is independent.
Previous results don't affect future flips.
</pre>
</div>

<div class='example-box'>
<p><strong>The Gambler's Fallacy</strong></p>
<pre class='code-block'>
Mistake: A number hasn't come up in the lottery
for a while, so it's due to come up soon.

Reality: Each draw is independent.
Just because 7 hasn't appeared doesn't make
it more likely to appear next time.

P(7) is the same every draw.
</pre>
</div>

<p><strong>Probability Does NOT Guarantee Outcomes:</strong></p>
<ul>
<li>Even if P(event) = 0.99 (99% likely), it might not happen</li>
<li>Even if P(event) = 0.01 (1% likely), it might still happen</li>
<li>Probability describes the long-term frequency, not individual outcomes</li>
</ul>
"""
    }
]
