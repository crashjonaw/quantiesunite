TITLE = "What is Probability?"

SECTIONS = [
    {
        "title": "From Chance to Certainty: The Big Picture",
        "body": """<div class="concept-box">
<p><strong>Will it rain tomorrow? Will I roll a 6? Will my team win?</strong></p>
<p>We can't predict the future perfectly, but we <strong>CAN measure how LIKELY something is</strong>. That's what probability does.</p>
<p><strong>Probability is a number from 0 (impossible) to 1 (certain) that measures chance.</strong></p>
</div>

<h3>Key Ideas</h3>
<ul>
<li><strong>Experiment:</strong> A process with an uncertain outcome (rolling a die, flipping a coin)</li>
<li><strong>Outcome:</strong> A possible result (rolling a 4, getting heads)</li>
<li><strong>Event:</strong> One or more outcomes we're interested in (getting an even number)</li>
<li><strong>Sample Space:</strong> The complete set of ALL possible outcomes</li>
</ul>

<div class="worked-example">
<h4>Rolling a Die: Identifying the Sample Space</h4>
<p><strong>Experiment:</strong> Roll a standard 6-sided die</p>
<p><strong>Sample Space (all possible outcomes):</strong> {1, 2, 3, 4, 5, 6}</p>
<p><strong>Some events we might care about:</strong></p>
<ul>
<li>Rolling a 4: {4} (one outcome)</li>
<li>Rolling an even number: {2, 4, 6} (three outcomes)</li>
<li>Rolling a number greater than 3: {4, 5, 6} (three outcomes)</li>
<li>Rolling a 1 or 6: {1, 6} (two outcomes)</li>
</ul>
</div>

<div class="worked-example">
<h4>Flipping a Coin: Simple Sample Space</h4>
<p><strong>Experiment:</strong> Flip a fair coin</p>
<p><strong>Sample Space:</strong> {H, T} (only 2 outcomes)</p>
<p><strong>Events:</strong></p>
<ul>
<li>Getting Heads: {H}</li>
<li>Getting Tails: {T}</li>
<li>Getting either Heads or Tails: {H, T} (certain event)</li>
</ul>
</div>

<div class="worked-example">
<h4>Spinning a Spinner: Identifying Outcomes</h4>
<p><strong>Experiment:</strong> Spin a spinner with 4 equal colored sections</p>
<p><strong>Sample Space:</strong> {Red, Blue, Green, Yellow}</p>
<p><strong>Events:</strong></p>
<ul>
<li>Getting Red: {Red}</li>
<li>Getting a warm color: {Red, Yellow}</li>
<li>Getting Blue or Green: {Blue, Green}</li>
</ul>
</div>"""
    },
    {
        "title": "Fair vs Biased: Equally Likely Outcomes",
        "body": """<h3>What Does "Fair" Mean?</h3>
<p>In many experiments, each outcome has the <strong>same chance of occurring</strong>. We call this <strong>equally likely outcomes</strong>.</p>

<div class="concept-box">
<p><strong>Fair Equipment:</strong> Each outcome is equally likely</p>
<p><strong>Biased Equipment:</strong> Some outcomes are more likely than others</p>
</div>

<div class="worked-example">
<h4>Fair Coin</h4>
<p>When you flip a fair coin:</p>
<ul>
<li>\(P(\text{Heads}) = \frac{1}{2} = 50\%\)</li>
<li>\(P(\text{Tails}) = \frac{1}{2} = 50\%\)</li>
<li>Both outcomes are equally likely</li>
</ul>
</div>

<div class="worked-example">
<h4>Fair Die</h4>
<p>When you roll a fair die:</p>
<ul>
<li>Each number (1, 2, 3, 4, 5, 6) has equal chance: \(\frac{1}{6}\) each</li>
<li>No number is more likely than another</li>
</ul>
</div>

<div class="worked-example">
<h4>Fair Spinner</h4>
<p>A spinner with 4 equal-sized sections:</p>
<ul>
<li>Each section has equal area</li>
<li>Landing on any color: \(\frac{1}{4}\) each</li>
</ul>
</div>

<div class="warning-box">
<h4>Biased Equipment Can Happen!</h4>
<p>Real coins, dice, or spinners might not be perfectly fair:</p>
<ul>
<li>A worn coin might land heads more often</li>
<li>A weighted die favors certain numbers</li>
<li>A spinner with unequal sections has unequal probabilities</li>
</ul>
</div>"""
    },
    {
        "title": "Calculating Basic Probability",
        "body": """<h3>The Basic Formula</h3>
<div class="concept-box">
<p><strong>P(event) = Number of favorable outcomes / Total number of possible outcomes</strong></p>
<p>Or in math notation: \\(P(A) = \\frac{\\text{favorable outcomes}}{\\text{total outcomes}}\\)</p>
</div>

<div class="worked-example">
<h4>Rolling a Die: What's P(rolling a 4)?</h4>
<p><strong>Sample Space:</strong> {1, 2, 3, 4, 5, 6} — 6 total outcomes</p>
<p><strong>Favorable outcomes (rolling a 4):</strong> {4} — 1 outcome</p>
<p><strong>Calculation:</strong></p>
<p>\\(P(4) = \\frac{1}{6} \\approx 0.167 \\text{ or about } 16.7\\%\\)</p>
</div>

<div class="worked-example">
<h4>Rolling a Die: What's P(rolling an even number)?</h4>
<p><strong>Sample Space:</strong> {1, 2, 3, 4, 5, 6} — 6 total outcomes</p>
<p><strong>Favorable outcomes (even: 2, 4, 6):</strong> {2, 4, 6} — 3 outcomes</p>
<p><strong>Calculation:</strong></p>
<p>\\(P(\\text{even}) = \\frac{3}{6} = \\frac{1}{2} = 0.5 \\text{ or } 50\\%\\)</p>
</div>

<div class="worked-example">
<h4>Drawing from a Bag of Colored Balls</h4>
<p><strong>Bag contains:</strong> 3 red, 2 blue, 5 green balls</p>
<p><strong>Total outcomes:</strong> 3 + 2 + 5 = 10 balls</p>
<p><strong>Probabilities:</strong></p>
<ul>
<li>\\(P(\\text{red}) = \\frac{3}{10} = 0.3 \\text{ or } 30\\%\\)</li>
<li>\\(P(\\text{blue}) = \\frac{2}{10} = \\frac{1}{5} = 0.2 \\text{ or } 20\\%\\)</li>
<li>\\(P(\\text{green}) = \\frac{5}{10} = \\frac{1}{2} = 0.5 \\text{ or } 50\\%\\)</li>
</ul>
<p><strong>Check:</strong> 0.3 + 0.2 + 0.5 = 1.0 ✓ (all probabilities sum to 1)</p>
</div>

<div class="success-box">
<h4>Key Insight: Probabilities Always Sum to 1</h4>
<p>All the probabilities of all possible outcomes must add up to 1 (or 100%). This makes sense because one of the outcomes must happen!</p>
</div>"""
    },
    {
        "title": "Practice: Sample Spaces and Basic Probability",
        "body": """<h3>Check Your Understanding</h3>

<div class="worked-example">
<h4>Problem 1: Listing a Sample Space</h4>
<p><strong>Question:</strong> You flip a coin twice. What is the complete sample space?</p>
<p><strong>Answer:</strong> {HH, HT, TH, TT} (4 outcomes)</p>
<p><strong>Explanation:</strong> The first flip can be H or T, and the second flip can be H or T. That gives us \(2 \times 2 = 4\) total possibilities.</p>
</div>

<div class="worked-example">
<h4>Problem 2: Finding a Probability</h4>
<p><strong>Question:</strong> A spinner has sections labeled A, B, B, C (so B appears twice). What is P(spinning B)?</p>
<p><strong>Answer:</strong> \\(P(B) = \\frac{2}{4} = \\frac{1}{2} = 0.5 \\text{ or } 50\\%\\)</p>
<p><strong>Explanation:</strong> There are 4 sections total. 2 of them are labeled B. So \(P(B) = \frac{2}{4}\).</p>
</div>

<div class="worked-example">
<h4>Problem 3: Comparing Probabilities</h4>
<p><strong>Question:</strong> In the spinner above (A, B, B, C), which is more likely: spinning A or spinning C?</p>
<p><strong>Answer:</strong> A and C are equally likely (both \(P = \frac{1}{4}\))</p>
<p><strong>Explanation:</strong> \\(P(A) = \\frac{1}{4}\\) and \\(P(C) = \\frac{1}{4}\\). They're the same!</p>
</div>"""
    }
]
