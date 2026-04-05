TITLE = "Sample Space & Probability Basics"

SECTIONS = [
    {
        "title": "Understanding Sample Space and Probability",
        "body": """
        <h3>Foundations of Probability</h3>
        <p>Before we calculate probabilities, we need to understand what we're calculating. <strong>Probability</strong> is the likelihood of an event occurring, expressed as a fraction, decimal, or percentage (0 to 1 or 0% to 100%).</p>

        <p>The key insight is that probability measures <em>uncertainty</em>. If something is certain to happen, P = 1. If it cannot happen, P = 0. Everything else falls in between.</p>

        <h4>Why Start with Sample Space?</h4>
        <p>To find any probability, we first need to know what outcomes are <em>possible</em>. This is where the <strong>sample space</strong> comes in.</p>

        <p>The <strong>sample space</strong> is the <em>complete set of all possible outcomes</em> of an experiment. Once we know the sample space, counting favorable outcomes becomes straightforward.</p>

        <div class="concept-box">
            <h4>Example 1: Rolling a Standard Die</h4>
            <p><strong>Sample space:</strong> {1, 2, 3, 4, 5, 6}</p>
            <p><strong>Total outcomes:</strong> 6</p>
            <ul>
                <li>P(rolling a 4) = 1/6 (one favorable outcome)</li>
                <li>P(rolling an even number) = 3/6 = 1/2 (three favorable outcomes: 2, 4, 6)</li>
                <li>P(rolling > 3) = 3/6 = 1/2 (outcomes: 4, 5, 6)</li>
            </ul>
        </div>

        <h4>The Basic Formula</h4>
        <div style="text-align: center; border-radius: 8px; padding: 20px; margin: 20px 0">
            <p style="font-size: 1.2em; margin: 0"><strong>P(A) = (Number of favorable outcomes) / (Total number of possible outcomes)</strong></p>
        </div>

        <p><strong>Key principle:</strong> All outcomes in the sample space must be equally likely for this formula to work directly.</p>

        <div class="concept-box">
            <h4>Example 2: Flipping a Fair Coin</h4>
            <p><strong>Sample space:</strong> {Heads, Tails}</p>
            <p><strong>P(Heads) = 1/2</strong> (assuming a fair coin)</p>
            <p><strong>Why?</strong> 1 favorable outcome (Heads) divided by 2 total possible outcomes.</p>
        </div>

        <h4>Why This Matters</h4>
        <p>Understanding sample space helps us avoid making mistakes. For example:</p>
        <ul>
            <li>A "sample space" of {Heads, Tails, Stands on edge} is incorrect for a real coin flip (extremely unlikely)</li>
            <li>A "sample space" of {Heads, Tails} for a die roll is incomplete (missing 1-6)</li>
        </ul>
        <p>Always list <em>all</em> realistic, equally likely outcomes.</p>
        """
    },
    {
        "title": "Key Properties and the Complement Rule",
        "body": """
        <h3>Fundamental Properties of Probability</h3>
        <p>All probabilities follow certain rules. Understanding these rules helps us solve problems quickly and avoid errors.</p>

        <h4>Property 1: Probability is Always Between 0 and 1</h4>
        <div class="formula-box" style="text-align: center;">
            <p style="margin: 0;"><strong>0 ≤ P(A) ≤ 1</strong></p>
        </div>

        <ul>
            <li><strong>P(A) = 0</strong> means event A is <em>impossible</em> (will never happen)</li>
            <li><strong>P(A) = 1</strong> means event A is <em>certain</em> (will definitely happen)</li>
            <li><strong>0 < P(A) < 1</strong> means event A is <em>possible but not certain</em></li>
        </ul>

        <div class="worked-example">
            <p><strong>Why this matters:</strong> If you calculate a probability and get something like 1.5 or −0.3, you've made an error. Check your work!</p>
        </div>

        <h4>Property 2: The Complement Rule</h4>
        <p>If A is an event, then A' (pronounced "A complement") is the event that A does <em>not</em> occur.</p>

        <div class="formula-box" style="text-align: center;">
            <p style="margin: 0;"><strong>P(A) + P(A') = 1</strong></p>
        </div>

        <p><strong>Why?</strong> Either event A happens or it doesn't. These are the only two possibilities, and together they cover the entire sample space.</p>

        <p><strong>Rearranged:</strong> P(A') = 1 − P(A)</p>

        <p><strong>Why is this useful?</strong> Sometimes it's easier to calculate the probability that something <em>doesn't</em> happen, then subtract from 1.</p>

        <div class="concept-box">
            <h4>Example 3: Drawing from a Standard Deck</h4>
            <p>P(drawing a red card) = 26/52 = 1/2</p>
            <p>P(not drawing a red card) = 1 − 1/2 = 1/2</p>
            <p>(These are the black cards: 26 spades and clubs)</p>
        </div>

        <div class="concept-box">
            <h4>Example 4: Rolling a Die</h4>
            <p>P(rolling a 6) = 1/6</p>
            <p>P(not rolling a 6) = 1 − 1/6 = 5/6</p>
            <p>(Outcomes: 1, 2, 3, 4, 5)</p>
        </div>

        <h4>When to Use the Complement Rule</h4>
        <p>Use this trick when:</p>
        <ul>
            <li><em>"At least one"</em> appears in the problem (use complement to count "none")</li>
            <li>Counting favorable outcomes directly is tedious</li>
            <li>The complement is simpler to calculate</li>
        </ul>

        <div class="warning-box">
            <h4>Common Mistake</h4>
            <p>Students sometimes forget that complements must sum to 1. If you find P(A) = 0.6 and P(A') = 0.5, something is wrong!</p>
        </div>
        """
    },
    {
        "title": "Working with Multiple Events",
        "body": """
        <h3>Building from Sample Spaces to Complex Events</h3>
        <p>Now that we understand single events, let's think about combinations. When an experiment has multiple stages or we combine different events, the sample space grows.</p>

        <h4>Creating Larger Sample Spaces</h4>
        <p>When we perform <em>multiple</em> experiments, the sample space is the product of individual sample spaces.</p>

        <div class="concept-box">
            <h4>Example 5: Flip a Coin and Roll a Die</h4>
            <p><strong>Coin outcomes:</strong> 2 (H, T)</p>
            <p><strong>Die outcomes:</strong> 6 (1, 2, 3, 4, 5, 6)</p>
            <p><strong>Combined sample space:</strong> 2 × 6 = 12 outcomes</p>
            <p><strong>Complete sample space:</strong> {H1, H2, H3, H4, H5, H6, T1, T2, T3, T4, T5, T6}</p>
            <p><strong>P(Heads and rolling a 4) = 1/12</strong> (one favorable outcome out of 12)</p>
        </div>

        <h4>Focusing on Specific Outcomes</h4>
        <p>We can ask questions about subsets of this larger sample space.</p>

        <div class="concept-box">
            <h4>Example 6: Drawing Two Balls (With Replacement)</h4>
            <p>A bag contains 3 red and 2 blue balls (5 total).</p>
            <p><strong>First draw:</strong> 5 possible outcomes</p>
            <p><strong>Second draw:</strong> 5 possible outcomes (ball returned)</p>
            <p><strong>Total outcomes:</strong> 5 × 5 = 25</p>
            <p><strong>P(first red AND second red) = (3 × 3) / 25 = 9/25</strong></p>
            <p><strong>P(first red AND second blue) = (3 × 2) / 25 = 6/25</strong></p>
            <p><strong>P(first blue AND second red) = (2 × 3) / 25 = 6/25</strong></p>
        </div>

        <h4>Understanding "And" vs "Or"</h4>
        <p><strong>"And"</strong> means both events must occur. We multiply probabilities (in simple cases).</p>
        <p><strong>"Or"</strong> means at least one event occurs. We add probabilities (but must be careful about overlaps).</p>

        <div class="worked-example">
            <h4>Example 7: Simple "Or" Question</h4>
            <p>P(rolling a 1 OR rolling a 2) with one die:</p>
            <p>P(1 or 2) = P(1) + P(2) = 1/6 + 1/6 = 2/6 = 1/3</p>
            <p><strong>Why add?</strong> These outcomes don't overlap. In one roll, we can't get both 1 and 2.</p>
        </div>

        <p><strong>Key insight:</strong> The structure of the sample space determines everything. Always build it carefully.</p>
        """
    }
]
